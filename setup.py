from setuptools import setup, find_packages
import pathlib
from cx_Freeze import setup, Executable
import sys
import src.version

## Import SRC
sys.path.insert(0,'./src')

here = pathlib.Path(__file__).parent.resolve()
base = None
long_description = (here / 'README.md').read_text(encoding='utf-8')

if sys.platform == "win32":
    base = "Win32GUI"

files = {"include_files": [
                        "./images",
                        "./templates",
                        "./config.cfg",
                       ],
                       }

setup(
    name='Joystick Diagrams',
    version='1.0.0',
    description='Automatically create diagrams for your throttles, joysticks and custom HID devices',
    long_description=long_description, 
    long_description_content_type='text/markdown',
    url='https://github.com/Rexeh/joystick-diagrams', 
    author='Robert Cox',
    keywords='joystick, HID, diagrams, joystick gremlin',
    packages=find_packages(), 
    python_requires='>=3.8, <4',
    install_requires=['pillow'],
    project_urls={ 
        'Bug Reports': 'https://github.com/Rexeh/joystick-diagrams/issues',
        'Funding': 'https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=WLLDYGQM5Z39W&source=url',
        'Source': 'https://github.com/Rexeh/joystick-diagrams/src',
    },

    options={'build_exe': files},
    executables = [Executable("./src/joystick-diagram.py", base = base, icon = './images/logo.ico')]
)