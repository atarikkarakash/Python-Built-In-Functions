
'__import__()'

'Invoked by the import statement to find and load a module.'

math_module = __import__('math')
print(math_module.sqrt(16))  # Output: 4.0
