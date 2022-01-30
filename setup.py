from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Intended Audience :: Science/Research',
  'Intended Audience :: Customer Service',
  'Intended Audience :: Financial and Insurance Industry',
  'Operating System :: Microsoft :: Windows :: Windows 7',
  'Operating System :: Microsoft :: Windows :: Windows 8',
  'Operating System :: Microsoft :: Windows :: Windows 8.1',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: Apache Software License',
  'Programming Language :: Python',
   'Programming Language :: Python :: 3 :: Only',
   'Programming Language :: Python :: 3.5',
   'Programming Language :: Python :: 3.6',
   'Programming Language :: Python :: 3.7',
   'Programming Language :: Python :: 3.8',
   'Programming Language :: Python :: 3.9',
   'Programming Language :: Python :: 3.10',
    'Topic :: Database',
    'Topic :: Education',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Scientific/Engineering :: Visualization',
    'Topic :: Office/Business :: Financial :: Investment',
    'Topic :: Office/Business :: Financial :: Accounting',
    'Topic :: Office/Business :: Financial :: Point-Of-Sale',
    'Topic :: Office/Business :: Financial :: Spreadsheet',
]
 
# import current vandal version.
from vandal.misc._meta import __version__

setup(
  name = 'vandal',
  version = __version__,
  description = 'Data science, Data manipulation and Machine learning library.',
  long_description_content_type = 'text/markdown',
  long_description = open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(), 
  author = 'David Kundih',
  author_email = 'kundihdavid@gmail.com',
  maintainer = 'David Kundih',
  maintainer_email = 'kundihdavid@gmail.com',
  url = 'http://github.com/dkundih/vandal',
  download_url = f'https://github.com/dkundih/vandal/archive/refs/tags/v{__version__}.tar.gz',
  license = 'Apache Software License',
  project_urls = {
    'Documentation': 'https://github.com/dkundih/vandal/blob/master/README.md',
    'Source Code': 'https://github.com/dkundih/vandal/tree/master/vandal'
  }, 
  classifiers = classifiers,
  keywords = 'data science, machine learning, data manipulation, artificial intelligence, AI, unin, duality, duality-py, duality.py, vandal, vandal-py, vandal.py',
  packages = find_packages(),
  install_requires = [
    'colorama >= 0.4.4',
    'pandas >= 1.2.3',
    'numpy >= 1.19.5',
    'matplotlib >= 3.4.3',
    'openpyxl',
]
  )
