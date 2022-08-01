import hashlib

s = "Python Bootcamp"

# using hash() method
hash_value = hash(s)
print(hash_value)

# using module hashlib with MD5 algorithm
hash_object = hashlib.md5(s.encode())
print(hash_object.hexdigest())

# using module hashlib with SHA1 algorithm
hash_object = hashlib.sha1(s.encode())
print(hash_object.hexdigest())

# using module hashlib with SHA224 algorithm
hash_object = hashlib.sha224(s.encode())
print(hash_object.hexdigest())

# using module hashlib with SHA256 algorithm
hash_object = hashlib.sha256(s.encode())
print(hash_object.hexdigest())

# using module hashlib with SHA384 algorithm
hash_object = hashlib.sha384(s.encode())
print(hash_object.hexdigest())

# using module hashlib with SHA512 algorithm
hash_object = hashlib.sha512(s.encode())
print(hash_object.hexdigest())
