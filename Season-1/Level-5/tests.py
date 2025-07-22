import unittest
import code as c

class TestCrypto(unittest.TestCase): 
  
    # verifies that hash and verification are matching each other for SHA
    def test_1(self):
        rd = c.Random_generator()
        sha256 = c.SHA256_hasher()
        pass_ver = sha256.password_verification("abc", sha256.password_hash("abc",rd.generate_salt()))
        self.assertEqual(pass_ver, True)

    # verifies that random token generation produces different results (tests randomness)
    def test_2(self):
        rd = c.Random_generator()
        token1 = rd.generate_token()
        token2 = rd.generate_token()
        # Tokens should be different (very low probability they're the same if truly random)
        self.assertNotEqual(token1, token2)
        
if __name__ == '__main__':    
    unittest.main()