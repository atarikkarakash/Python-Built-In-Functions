
'memoryview()'

'Returns a memory view object.'

b = bytearray('xyz', 'utf-8')
m = memoryview(b)
print(m[0])  # Output: 120
