import sys

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos]
        self.symbol_table = {}  # Memori Variabel

    def error(self, message):
        raise Exception(f"[Syntax Error] {message} pada token {self.current_token}")

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.pos += 1
            if self.pos < len(self.tokens):
                self.current_token = self.tokens[self.pos]
        else:
            self.error(f"Mengharapkan {token_type}, mendapat {self.current_token.type}")

    # --- ATURAN PRODUKSI (Grammar 1LP Final) ---

    def parse(self):
        print(f"{'='*10} PROSES PARSING & SEMANTIK {'='*10}")
        self.stm()
        if self.current_token.type != 'EOF':
            self.error("Sisa input deteksi setelah parsing selesai.")
        print("\n[INFO] Parsing Sukses. Struktur valid.")

    def stm(self):
        # Stm -> Stm' SiStm
        self.stm_prime()
        self.si_stm()

    def si_stm(self):
        # SiStm -> ; Stm' SiStm | epsilon
        if self.current_token.type == 'SEMI':
            self.eat('SEMI')
            # Cek apakah setelah titik koma masih ada statement atau habis (epsilon)
            if self.current_token.type in ('ID', 'PRINT'):
                self.stm_prime()
                self.si_stm()
        else:
            pass # Epsilon

    def stm_prime(self):
        # Stm' -> id := Exp | print ( ExpList )
        if self.current_token.type == 'ID':
            var_name = self.current_token.value
            self.eat('ID')
            self.eat('ASSIGN')
            val = self.exp()
            # Semantic: Simpan ke memori
            self.symbol_table[var_name] = val
            print(f"--> Eksekusi: {var_name} = {val}")

        elif self.current_token.type == 'PRINT':
            self.eat('PRINT')
            self.eat('LPAREN')
            vals = self.exp_list()
            self.eat('RPAREN')
            # Semantic: Cetak output
            print(f"--> OUTPUT LAYAR: {vals}")
        else:
            self.error("Awal statement harus 'id' atau 'print'")

    def exp(self):
        # Exp -> Exp' SiExp (Level Penjumlahan)
        val = self.exp_prime()
        return self.si_exp(val)

    def si_exp(self, inherited_value):
        if self.current_token.type == 'PLUS':
            self.eat('PLUS')
            term_val = self.exp_prime()
            return self.si_exp(inherited_value + term_val)
        elif self.current_token.type == 'MINUS':
            self.eat('MINUS')
            term_val = self.exp_prime()
            return self.si_exp(inherited_value - term_val)
        return inherited_value

    def exp_prime(self):
        # Exp' -> Exp" SiExp' (Level Perkalian)
        val = self.exp_double_prime()
        return self.si_exp_prime(val)

    def si_exp_prime(self, inherited_value):
        if self.current_token.type == 'TIMES':
            self.eat('TIMES')
            factor_val = self.exp_double_prime()
            return self.si_exp_prime(inherited_value * factor_val)
        elif self.current_token.type == 'DIVIDE':
            self.eat('DIVIDE')
            factor_val = self.exp_double_prime()
            if factor_val == 0: raise Exception("[Runtime Error] Pembagian nol")
            return self.si_exp_prime(inherited_value / factor_val)
        return inherited_value

    def exp_double_prime(self):
        # Exp" -> id | num | ( Stm , Exp )
        if self.current_token.type == 'NUM':
            val = self.current_token.value
            self.eat('NUM')
            return val
        elif self.current_token.type == 'ID':
            name = self.current_token.value
            self.eat('ID')
            if name in self.symbol_table:
                return self.symbol_table[name]
            else:
                raise Exception(f"[Semantic Error] Variabel '{name}' belum didefinisikan")
        elif self.current_token.type == 'LPAREN':
            # Aturan unik: ( Stm , Exp )
            self.eat('LPAREN')
            self.stm() # Eksekusi statement side-effect
            self.eat('COMMA')
            val = self.exp()
            self.eat('RPAREN')
            return val
        else:
            self.error("Ekspresi harus dimulai id, num, atau '('")

    def exp_list(self):
        # ExpList -> Exp ExpList'
        res = [self.exp()]
        res.extend(self.exp_list_prime())
        return res

    def exp_list_prime(self):
        if self.current_token.type == 'COMMA':
            self.eat('COMMA')
            return self.exp_list()
        return []