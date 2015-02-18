from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='autocomplete',
      version='0.0.001',
      description='tiny \'autocomplete\' engine',
      keywords='autocomplete autosuggest suggest complete spell spellsuggest \
                automatic spelling word suggest machine learning ai text \
                conditional probability model probabilistic perspective \
                Rodrigo Palacios rodrigo palacios im-rodrigo im_rodrigo \
                rodricios',
      
      author='Rodrigo Palacios',
      author_email='rodrigopala91@gmail.com',
      license='MIT',
      packages=['autocomplete'],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)
