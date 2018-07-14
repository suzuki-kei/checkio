#
# https://py.checkio.org/en/mission/caesar-cipher-encryptor/
#

def to_encrypt(text, delta):
    def encrypt(c):
        if not c.isalpha():
            return c
        return chr((ord(c) - ord("a") + delta + 26) % 26 + ord("a"))

    return "".join(map(encrypt, text))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")

