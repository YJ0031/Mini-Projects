import ecdsa
from hashlib import sha256

#ECDSA

sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
vk = sk.get_verifying_key()
sig = sk.sign(b"message")

print (sig)

print(vk.verify(sig, b"message"))

