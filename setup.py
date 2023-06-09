import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LLAW33012023S1UC2',
      version='0.0.1',
      description=('A docassemble extension.'),
      long_description="# docassemble.LLAW33012023S1UC2\r\n\r\nThis application was created for The Consumer Credit Law Centre of South Australia. It aims to help people who are struggling to repay their loans identify whether they are dealing with a responsible lending issue. People often do not realise they can seek help for loans they should never have been given in the first place. This application aims to increase peoples' awareness of their legal rights and encourage them to seek help\r\n\r\n## Author\r\n\r\nAllison Mason, maso0192@flinders.edu.au\r\nBianca Elliott, elli0528@flinders.edu.au\r\nPhoebe Curyer, cury0011@flinders.edu.au\r\nLily Greaves, grea0081@flinders.edu.au\r\nMatthew Dell'Antonio, dell0095@flinders.edu.au\r\n",
      long_description_content_type='text/markdown',
      author='Allison Mason',
      author_email='maso0192@flinders.edu.au',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LLAW33012023S1UC2/', package='docassemble.LLAW33012023S1UC2'),
     )

