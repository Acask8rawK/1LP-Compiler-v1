import sys
import os
from lexer import Lexer
from parser import Parser

def run_compiler(filepath):
    print(f"\n{'='*40}")
    print(f"RUNNING FILE: {filepath}")
    print(f"{'='*40}")
    
    try:
        # Baca File
        with open(filepath, 'r') as file:
            code = file.read()
        
        print(f"[SOURCE CODE]:\n{code}\n")

        # 1. Lexical Analysis
        lexer = Lexer(code)
        print(f"[SCANNER] Token Stream: {lexer.tokens}\n")

        # 2. Syntax & Semantic Analysis
        parser = Parser(lexer.tokens)
        parser.parse()
        
        # 3. Hasil Memori
        print(f"\n[MEMORY DUMP] Symbol Table: {parser.symbol_table}")

    except FileNotFoundError:
        print(f"Error: File '{filepath}' tidak ditemukan.")
    except Exception as e:
        print(f"\n[CRITICAL ERROR] {e}")

if __name__ == "__main__":
    # Cara pakai: python main.py <path_file>
    if len(sys.argv) < 2:
        print("Gunakan perintah: python src/main.py tests/valid_code.txt")
    else:
        run_compiler(sys.argv[1])