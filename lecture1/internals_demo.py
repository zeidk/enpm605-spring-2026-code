# # Viewing Python Tokenization Internals
# -------------------------------------------------------------
import io
import tokenize

code = "x = 5 + 3"
tokens = tokenize.generate_tokens(io.StringIO(code).readline)

for tok in tokens:
    print(tok)

# # Abstract Syntax Tree (AST) Demonstration
# -------------------------------------------------------------

# import ast

# code = "x = 5 + 3"
# tree = ast.parse(code)
# print(ast.dump(tree, indent=2))

# Disassembly of Python Bytecode
# -------------------------------------------------------------

# import os
# print(os.getcwd())
