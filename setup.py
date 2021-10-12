from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: Apache Software License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='vandal',
  version='insert_the_version',
  description='Data science and Machine learning package.',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(), 
  author='David Kundih',
  author_email='kundihdavid@gmail.com',
  url='http://github.com/dkundih/vandal',
  license='Apache Software License', 
  classifiers=classifiers,
  keywords='data science, machine learning, artificial intelligence, AI, vandal',
  packages=find_packages(),
  install_requires=['pandas >= 1.2.3', 'numpy >= 1.19.5', 'matplotlib >= 3.4.3']
)
