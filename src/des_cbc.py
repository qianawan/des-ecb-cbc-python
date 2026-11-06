from pyDes import des, CBC, PAD_PKCS5
import binascii


def des_encrypt(s, key='00101010'):
    """
    DES encryption
    :param s: the original string
    :param key: encryption key: 8 bytes
    :return: the encrypted string, in hexadecimal
    """
    secret_key = key
    iv = '12345678'      # Fixed 8-byte demonstration IV; not for real data
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en)


def des_descrypt(s, key='00101010'):
    """
     DES decryption
    :param s: the encrypted string, in hex
    :return: the decrypted string
    """
    secret_key = key
    iv = '12345678'      # Fixed 8-byte demonstration IV; not for real data
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de


if __name__ == '__main__':
    s = 'wanwei'
    encry_s = des_encrypt(s)
    print(encry_s)
    descry_s = des_descrypt(encry_s)
    print(descry_s)
