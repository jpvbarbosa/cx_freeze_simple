from cx_Freeze import setup, Executable
import sys

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': [], 'build_exe': "build-setup"}

executables = [
    Executable('main.py', target_name="main_setup", base=None)
]

print(sys.path)

setup(name='Main-setup',
      version = '1.0',
      description = 'Main setup',
      options = {'build_exe': build_options},
      executables = executables)
