import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from des_ecb import DES

class ECBTests(unittest.TestCase):
    def test_known_vector(self):
        cipher = DES(bytes.fromhex("133457799BBCDFF1"))
        plain = bytes.fromhex("0123456789ABCDEF")
        encrypted = bytes.fromhex("85E813540F0AB405")
        self.assertEqual(cipher.Encrypt(plain), encrypted)
        self.assertEqual(cipher.Decrypt(encrypted), plain)

    def test_archived_example(self):
        self.assertEqual(DES(b"00101010").Encrypt(b"wanwei33").hex(), "eeae7f72480d69f4")

    def test_zero_padding(self):
        cipher = DES(b"12345678")
        self.assertEqual(cipher.Decrypt(cipher.Encrypt(b"hello")), b"hello\x00\x00\x00")

    def test_repeated_blocks(self):
        encrypted = DES(b"12345678").Encrypt(b"abcdefghabcdefgh")
        self.assertEqual(encrypted[:8], encrypted[8:])

if __name__ == "__main__":
    unittest.main()
