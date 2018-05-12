import string
import secrets
import math
import pickle
from spass.exceptions import ParameterError


def generate_random_password(length=9, letters=True, digits=True, punctuation=True, ignored_chars=''):
    """
    Generates a cryptographically secure random password
    :param length: Length of password
    :param letters: True to use letters in password
    :param digits: True to use digits in password
    :param punctuation: True to use punctuation in password
    :param ignored_chars: str containing all the characters that should be ignored during generation
    :return: A dictionary containing the password and entropy
    """
    if not (letters or digits or punctuation):
        raise ParameterError('At least one set of characters must be selected for a password to be generated')

    char_pool = ''
    if letters:
        char_pool += string.ascii_letters
    if digits:
        char_pool += string.digits
    if punctuation:
        char_pool += string.punctuation

    char_list = [char for char in char_pool if char not in ignored_chars]

    result = ''
    for _ in range(length):
        result += secrets.choice(char_list)

    return {'password': result, 'entropy': __calc_entropy_password(result, len(char_list))}


def generate_passphrase(word_count=5, pad_length=0, digits=True, punctuation=True, ignored_symbols=''):
    """
    Generates a passphrase with the specified amount of padding
    :param word_count: Number of words in passphrase
    :param pad_length: The number of padding characters
    :param digits: True to use digits in padding
    :param punctuation: True to use punctuation in padding
    :param ignored_symbols: str containing all the symbols to ignore during padding generation
    :return: A dictionary containing the passphrase, entropy and the +- deviation of the entropy
    """
    if word_count < 2:
        raise ParameterError('You need at least two words to make a passphrase')

    with open('object/word_map.pickle', 'rb') as words:
        word_bank = pickle.load(words)

    placements, pad_bank_size = {}, 0
    if pad_length > 0:
        if not (digits or punctuation):
            raise ParameterError('At least one set of characters must be selected for the padding')
        placements, pad_bank_size = __scatter_padding(word_count, pad_length, digits, punctuation, ignored_symbols)

    result, words_used, coin = '', [], [0, 1]
    for i in range(word_count):
        if i in placements:
            result += ''.join(sym for sym in placements[i])

        word = secrets.choice(word_bank)
        if secrets.choice(coin) == 0:
            word = word[0].upper() + word[1:]

        result += word
        words_used.append(word)

    if word_count in placements:
        result += ''.join(sym for sym in placements[word_count])

    entropy, deviation = __calc_entropy_passphrase(word_count, len(word_bank), pad_length, pad_bank_size)
    return {'password': result, 'entropy': entropy, 'deviation': deviation}


def __scatter_padding(word_count, pad_length, digits, punctuation, ignored_symbols):
    """
    Randomly decides where to add padding and which characters to use
    :param word_count: Number of words in passphrase
    :param pad_length: Number of characters to use for padding
    :param digits: True to use digits in padding
    :param punctuation: True to use punctuation in padding
    :param ignored_symbols: str containing all characters to ignore during padding generation
    :return: A tuple containing the padding placements and the size of the character pool used to pad
    """
    char_pool = ''
    if digits:
        char_pool += string.digits
    if punctuation:
        char_pool += string.punctuation

    char_list = [char for char in char_pool if char not in ignored_symbols]
    indexes = [index for index in range(word_count + 1)]
    placements = {}
    for _ in range(pad_length):
        idx = secrets.choice(indexes)

        if idx not in placements:
            placements.update({idx: [secrets.choice(char_list)]})
        else:
            placements[idx].append(secrets.choice(char_list))

    return placements, len(char_list)


def __calc_entropy_password(password, pool_size):
    """
    Calculates the entropy of a random password
    :param password: The password
    :param pool_size: The size of the character pool used to generate password
    :return: Entropy
    """
    if not password or not pool_size:
        return 0

    # entropy = log_2(P^L) { R: Total number of possible choices, L: Length of the password }
    inner = math.pow(pool_size, len(password))
    return math.log(inner, 2)


def __calc_entropy_passphrase(word_count, word_bank_size, pad_length, pad_bank_size):
    """
    Approximates the minimum entropy of the passphrase with its possible deviation
    :param word_count: Number of words in passphrase
    :param word_bank_size: Total number of words in the word bank
    :param pad_length: Number of characters used in padding
    :param pad_bank_size: The size of the character pool used to generate padding
    :return: A tuple containing the minimum entropy and deviation
    """
    # Multiply word bank size by 2 since there are uppercase or lower case words
    inner = math.pow(word_bank_size*2, word_count)
    entropy = math.log(inner, 2)

    inner = math.pow(pad_bank_size, pad_length)
    deviation = math.log(inner, 2)

    return entropy, deviation
