import hashlib

s = "Python Bootcamp"

# using hash() method
h = hash(s)
print(h)

"""
# using module hashlib with MD5 algorithm
h = hashlib.md5(s.encode())
print(h.hexdigest())

# using module hashlib with SHA1 algorithm
h = hashlib.sha1(s.encode())
print(h.hexdigest())

# using module hashlib with SHA224 algorithm
h = hashlib.sha224(s.encode())
print(h.hexdigest())

# using module hashlib with SHA256 algorithm
h = hashlib.sha256(s.encode())
print(h.hexdigest())

# using module hashlib with SHA384 algorithm
h = hashlib.sha384(s.encode())
print(h.hexdigest())

# using module hashlib with SHA512 algorithm
h = hashlib.sha512(s.encode())
print(h.hexdigest())
"""