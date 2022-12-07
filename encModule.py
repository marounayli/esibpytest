from cryptography.fernet import Fernet
import secretKey
import json
import identity
import base64


def eval_identities():
    return (identity.matricule_1,identity.name_1, identity.matricule_2, identity.name_2)



def encrypt_grades(grades):
    fernet = Fernet(secretKey.key)
    grades_string = json.dumps(grades)
    encrypted_grades= fernet.encrypt(grades_string.encode())
    with open("{}-{}-{}-{}".format(*eval_identities()),"w") as f:
        f.write(encrypted_grades.decode())
    