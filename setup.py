from setuptools import setup, find_packages

setup(name='spass',
      version='0.1',
      description='Simple and Secure passphrases',
      keywords='cryptography password passphrase secure',
      classifiers=['Development Status :: 3 - Alpha',
                   'License :: OSI Approved :: MIT License',
                   'Intended Audience :: Developers',
                   'Programming Language :: Python :: 3'],
      project_urls={
          'Source': 'https://github.com/Tauag/spass',
          'Tracker': 'https://github.com/Tauag/spass/issues'
      },
      python_requires='>=3',

      url='https://github.com/Tauag/spass',
      author='Tauag',
      author_email='dev.gavin.li@gmail.com',

      license='MIT',
      packages=find_packages(),
      install_requires=[],
      zip_safe=False)
