from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: Apache Software License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='alunari',
  version='1.3.6',
  description='Data science and Machine learning package.',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(), 
  author='David Kundih',
  author_email='kundihdavid@gmail.com',
  url='http://github.com/dkundih/alunari',
  license='Apache Software License', 
  classifiers=classifiers,
  keywords='data science, machine learning, artificial intelligence, AI, alunari',
  packages=find_packages(),
  install_requires=['pandas >= 1.2.3', 'numpy >= 1.19.5', 'matplotlib >= 3.4.3', 'UNIN >= 0.0.2']
)
