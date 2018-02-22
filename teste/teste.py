from usuario import Usuario
import unittest

class TestBD(unittest.TestCase):

    def get_user_test(self):
        user = Usuario("thiago@gmail.com","12345","Thiago","Advogado","Masculino")
        return user