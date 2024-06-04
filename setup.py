from cx_Freeze import setup, Executable
import sys

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': [], 'build_exe': "build-setuptools"}

executables = [
    Executable('main.py', target_name="main_setuptools", base=None)
]

print(sys.path)

setup(name='Main-setuptools',
      version = '1.0',
      description = 'Main setuptool',
      options = {'build_exe': build_options},
      executables = executables)
