from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import subprocess
from config import OPEN_PORT, TEAMS_WEBHOOK_URL, REMOTE_SERVER, USER_NAME, USER_PASSWORD, PATCH_TO_SCRIPT
# import winrm


class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        try:
            data = json.loads(post_data.decode('utf-8'))

            # Розділення ПІБ
            full_name_ua = data.get("FullNameUA", "").strip().split()
            full_name_en = data.get("FullNameEN", "").strip().split()

            first_name_ua = full_name_ua[1] if len(full_name_ua) > 0 else ""
            last_name_ua = full_name_ua[0] if len(full_name_ua) > 1 else ""

            first_name_en = full_name_en[0] if len(full_name_en) > 0 else ""
            last_name_en = full_name_en[1] if len(full_name_en) > 1 else ""
            
            # Формування аргументів для PowerShell
            # args = [
            #     "powershell.exe",
            #     "-ExecutionPolicy", "Bypass",
            #     "-File", "create_user_ad.ps1",
            #     "-FirstNameUA", first_name_ua,
            #     "-LastNameUA", last_name_ua,
            #     "-FirstNameEN", first_name_en,
            #     "-LastNameEN", last_name_en,
            #     # "-UserUPNlogon", "f{FirstNameEN}.{LastNameEN}@tsum.ua",
            #     "-UserUPNlogon", f"{first_name_en}.{last_name_en}@tsum.ua",
            #     "-Office", "ЦУМ", 
            #     "-Email", f"{first_name_en}.{last_name_en}@tsum.ua",
            #     "-WebPage", "TSUM.UA",
            #     "-Phone", data.get("Phone", ""),
            #     # "-Title", data.get("Title", ""), #
            #     # "-Title", f"{data.get('TitleEN', '')}|{data.get('TitleUA', '')}",
            #     "-Title", f"{data.get('Title', '')}",
            #     "-DepartmentName", data.get("DepartmentName", ""), 
            #     "-Company", "TSUM", 
            #     "-ManagerName", data.get("ManagerName", ""), 
            #     # "-Description", data.get("Description", "")
            #     # "-Description", f"{data.get('TitleEN', '')} | {data.get('TitleUA', '')}"
            #     "-Description", f"{data.get('Title', '')}"
            # ]
            args_dict = {
                "FirstNameUA": first_name_ua,
                "LastNameUA": last_name_ua,
                "FirstNameEN": first_name_en,
                "LastNameEN": last_name_en,
                "UserUPNlogon": f"{first_name_en}.{last_name_en}@tsum.ua",
                "Office": "ЦУМ",
                "Email": f"{first_name_en}.{last_name_en}@tsum.ua",
                "WebPage": "TSUM.UA",
                "Phone": data.get("Phone", ""),
                "Title": data.get("Title", ""),
                "DepartmentName": data.get("DepartmentName", ""),
                "Company": "TSUM",
                "ManagerName": data.get("ManagerName", ""),
                "Description": data.get("Title", "")
            }


            # print("Running PowerShell with args:")
            # print(f" ".join(args))
            # #############################
            ps_params = " ".join([f"-{k} '{v}'" for k, v in args_dict.items()])
            ps_script = f"& '{PATCH_TO_SCRIPT}' {ps_params}"

            s = winrm.Session(f'{REMOTE_SERVER}', auth=(f'{USER_NAME}', f'{USER_PASSWORD}'))
            # ps_script = f"""
            # & '{PATCH_TO_SCRIPT}' -FirstNameUA '{first_name_ua}' -LastNameUA '{last_name_ua}' -FirstNameEN '{first_name_en}' -LastNameEN '{last_name_en}'
            # """
            r = s.run_ps(ps_script)
            print(r.std_out.decode())
            print(r.std_err.decode())
            # ############################
            
            # result = subprocess.run(args, capture_output=True, text=True)

            # self.send_response(200)
            # self.send_header('Content-type', 'application/json')
            # self.end_headers()
            # response = {
            #     "status": "ok",
            #     "stdout": result.stdout,
            #     "stderr": result.stderr
            # }
            # self.wfile.write(json.dumps(response).encode('utf-8'))
            
        except Exception as error:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(error).encode('utf-8'))


# Перевірка заповнення зміних в файлі .env
def start_logs():
    env_variables = {
        "TEAMS_WEBHOOK_URL":  TEAMS_WEBHOOK_URL,
        "OPEN_PORT":          OPEN_PORT
    }
    status_variables_logs = []

    print("Перевірка змінних оточення ...\n"
    "---------------------------------------------------------------------------------------\n"
    f"{'ЗМІННА ОТОЧЕННЯ':<30} {'ЗАПОВНЕНО':<20} ПОВІДОМЛЕННЯ\n"
    "---------------------------------------------------------------------------------------\n")
    for name, value in env_variables.items():
        is_filled = bool(value and value.split())
        status_variables_logs.append(is_filled)
        print(f"{name:<30} {str(is_filled):<20} {"Заповніть змінну оточення" if not is_filled else "OK"}")
    print("---------------------------------------------------------------------------------------")


    if not all(status_variables_logs):
        raise EnvironmentError("Не всі змінні оточення заповнено!")
    # return True


# Запуск серверу
def run(server_class=HTTPServer, handler_class=RequestHandler, port=None):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Listening on port {port}...")

    # Обробка закриття серверу 
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер зупинено вручную (Ctrl+C)")
    finally:
        httpd.server_close()
        print("З'єднання закрито")



if __name__ == "__main__":
    try:
        start_logs()
        open_port = int(OPEN_PORT)
        if open_port != None: # Перевірка заповнення змінної порт в .env
            print("Start")
            run(port=open_port)
    except EnvironmentError as error:
        print(str(error))