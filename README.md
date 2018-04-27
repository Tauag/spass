# SPass: Simple & Secure Passwords #

Generate secure passphrases to use instead of random strings! (Random strings are also an option) <br>
<br>
Do you want cryptographically strong passwords for your applications/accounts/anything you want? Then
never fear as SPass is here! SPass leverages the built in secrets library and over 7776 words to randomly
generate passphrases or even passwords. It even calculates the entropy for you.**
<br><br>
**It calculates the entropy of passwords, however at this point in time it only calculates the minimum entropy
of passphrases as well as a deviation. So for passphrases the true value is (entropy +- deviation)
<br><br>

## How to use ##
Try generating passwords:

```python
import spass
spass.generate_passphrase()
# Will output something like:
# {'password': 'movieChipcorrectvertigomany', 'entropy': 69.62406251802891, 'deviation': 0.0}
```

<br>
You can even add a bit of padding to it:

```python
import spass
spass.generate_passphrase(pad_length=2)
# {'password': 'poroustrimester#landslide4UneditedSlacking', 'entropy': 69.62406251802891, 'deviation': 10.784634845557521}

spass.generate_passphrase(pad_length=2, punctuation=False)
# {'password': '4undrilleddilationfifteenGloater7Wager', 'entropy': 69.62406251802891, 'deviation': 6.643856189774725}
```
<br>
You can specify exactly what symbols you don't want in your padding:

```python
import spass
spass.generate_passphrase(pad_length=5, ignored_symbols=',./;:\'\"\\|[]{}()')
# The generated passphrase will not have any of the characters you ignored in the padding
# {'password': 'Unnamed<>`retract#Tighten-exemptionstitch', 'entropy': 69.62406251802891, 'deviation': 23.774437510817343}
```
<br>
Or be old fashioned and go with a very secure random password:

```python
import spass
spass.generate_random_password(length=20)
# {'password': "uOp/J:2Mejvz#-v`h'?1", 'entropy': 131.09177703355275}

spass.generate_random_password(length=20, punctuation=False)
# You can turn off digits, punctuation or even letters
# {'password': 'GNLbfgCOehmeZXXHUf6E', 'entropy': 119.08392620773752}

spass.generate_random_password(length=20, ignored_chars='\'\":;<>,./?[]{}\\()')
# Or just ignore specific symbols
# {'password': 'rLr3oku%J7a|*y28SjHv', 'entropy': 131.09177703355275}
```

## Installation ##
Just use pip:
```
pip install spass
```

## Contribution ##
This is my first open source project and I'm really putting myself out in the wild for the sake of
learning. I appreciate all feedback and any contributions to improve this package. Thanks!