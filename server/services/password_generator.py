import random

class PasswordGenerator:
    def __init__(self, length=10, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
        self.length = length
        self.use_upper = use_upper
        self.use_lower = use_lower
        self.use_digits = use_digits
        self.use_symbols = use_symbols

    def generate(self):
        if self.length < 8:
            raise ValueError("Мінімальна довжина паролю — 8 символів")

        # Параментри паролю
        #######################################################
        upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        lower = list("abcdefghijklmnopqrstuvwxyz")
        digits = list("0123456789")
        symbols = list("!-+=")
        #######################################################
        sets = []
        pool = []

        if self.use_upper:
            sets.append(upper)
            pool.extend(upper)

        if self.use_lower:
            sets.append(lower)
            pool.extend(lower)

        if self.use_digits:
            sets.append(digits)
            pool.extend(digits)

        if self.use_symbols:
            sets.append(symbols)
            pool.extend(symbols)

        
        if len(pool) == 0:
            raise ValueError("Неможна створити пароль — не обрано жодного типу символів")

        # Дадаємо мінімум 1 рядок кожної категорії
        password_chars = [random.choice(s) for s in sets]

        remainig = self.length - len(password_chars)
        password_chars.extend(random.choice(pool) for _ in range(remainig))

        random.shuffle(password_chars)

        return ''.join(password_chars)