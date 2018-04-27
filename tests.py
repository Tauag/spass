import unittest
from spass.generators import *
from spass.exceptions import ParameterError


class TestGenerators(unittest.TestCase):
    def test_length(self):
        pass_set = generate_random_password()
        self.assertEqual(9, len(pass_set['password']), 'Generated password not of correct length: %s' % pass_set)

        pass_set = generate_random_password(length=40)
        self.assertEqual(40, len(pass_set['password']), 'Generated password not of correct length: %s' % pass_set)

        pass_set = generate_random_password(length=150)
        self.assertEqual(150, len(pass_set['password']), 'Generated password not of correct length: %s' % pass_set)

    def test_characters(self):
        target_chars = '<>,.?\\\'\"{}[]()=+-_^`~'
        pass_set = generate_random_password(length=150, ignored_chars=target_chars)
        for char in pass_set['password']:
            self.assertTrue(char not in target_chars, '<%s> was found and not expected' % char)

        pass_set = generate_random_password(length=150, letters=False)
        for char in pass_set['password']:
            self.assertTrue(char not in string.ascii_letters, '<%s> was found and not expected' % char)

        pass_set = generate_random_password(length=150, digits=False)
        for char in pass_set['password']:
            self.assertTrue(char not in string.digits, '<%s> was found and not expected' % char)

        pass_set = generate_random_password(length=150, punctuation=False)
        for char in pass_set['password']:
            self.assertTrue(char not in string.punctuation, '<%s> was found and not expected' % char)

        pass_set = generate_random_password(length=150, letters=False, punctuation=False)
        for char in pass_set['password']:
            self.assertTrue(char not in string.ascii_letters + string.punctuation, '<%s> was found and not expected' % char)

        pass_set = generate_random_password(length=150, letters=False, digits=False)
        for char in pass_set['password']:
            self.assertTrue(char not in string.ascii_letters + string.digits, '<%s> was found and not expected' % char)

    def test_exception(self):
        with self.assertRaises(ParameterError):
            generate_random_password(letters=False, punctuation=False, digits=False)

        with self.assertRaises(ParameterError):
            generate_passphrase(pad_length=5, punctuation=False, digits=False)

    def test_entropy(self):
        pass_set = generate_random_password()
        self.assertEqual(58.99129966509874, pass_set['entropy'], 'Unexpected entropy value')

        pass_set = generate_random_password(letters=False, digits=False)
        self.assertEqual(45, pass_set['entropy'], 'Unexpected entropy value')

        pass_set = generate_random_password(length=15)
        self.assertEqual(98.31883277516458, pass_set['entropy'], 'Unexpected entropy value')

        pass_set = generate_random_password(length=150, letters=False, digits=False)
        self.assertEqual(750.0000000000001, pass_set['entropy'], 'Unexpected entropy value')
