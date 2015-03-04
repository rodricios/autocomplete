from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='autocomplete',
      version='0.0.104',
      description='tiny \'autocomplete\' tool using a "hidden markov model"',
      keywords='autocomplete autosuggest suggest complete spell spellsuggest \
                hidden markov model HMM hmm markov chain iPhone iphone suggest \
                Google suggest search as you type searchsuggest type spell \
                automatic spelling word suggest machine learning ai text \
                conditional probability model probabilistic perspective \
                Rodrigo Palacios rodrigo palacios im-rodrigo im_rodrigo \
                rodricios',

      author='Rodrigo Palacios',
      author_email='rodrigopala91@gmail.com',
      license='MIT',
      packages=['autocomplete'],
      install_requires=['bottle'],
      url='https://github.com/rodricios/autocomplete',
      scripts=['bin/autocomplete_server.py'],
      package_data={'autocomplete': ['autocomplete/big.txt']},
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)
