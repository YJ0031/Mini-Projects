from tinyec import registry
import secrets

#Diffie-Hellman

def compress(publicKey):
    return hex(publicKey.x) + hex(publicKey.y%2)[2:]

curve = registry.get_curve('secp192r1')
Ka = secrets.randbelow(curve.field.n)
X = Ka * curve.g
print("X:", compress(X))
Kb = secrets.randbelow(curve.field.n)
Y = Kb * curve.g
print("Y:", compress(Y))
print("Currently exchange the publickey (e.g. through Internet)")
aliceSharedKey = Ka * Y
print("Alice shared key :",compress(aliceSharedKey))
bobSharedKey = Kb * X
print("Bob shared key :",compress(bobSharedKey))
print("Equal shared keys:", aliceSharedKey == bobSharedKey)

