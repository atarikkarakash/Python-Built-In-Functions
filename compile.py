
'compile()'

'Compiles source into a code or AST object.'

code_str = 'print("Hello, World!")'
code = compile(code_str, 'string', 'exec')
exec(code)  # Output: Hello, World!
