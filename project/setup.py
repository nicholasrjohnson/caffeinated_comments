import os
import site
import sys
from distutils.sysconfig import get_python_lib

from setuptools import setup, find_packages

# Allow editable install into user site directory.
site.ENABLE_USER_SITE = '--user' in sys.argv[1:]

# Warn if installing over top of an existing installation.
overlay_warning = False
if "install" in sys.argv:
    lib_paths = [get_python_lib()]
    if lib_paths[0].startswith("/usr/lib/"):
        #For Debian
        lib_paths.append(get_python_lib(prefix="/usr/local"))
    for lib_path in lib_paths:
        previous_path = os.path.abspath(os.path.join(lib_path, "project"))
        if os.path.exists(existing_path):
            overlay_warning = True
            break


setup(
    name='caffeinated_comments',
    version='0.1.0',
    package=find_packages(include=['project']),
    install_requires=[]
)


if overlay_warning:
    sys.stderr.write("""
========
WARNING!
========
You have just installed Caffeinated Comments over an existing installation.
It was installed at %(previous_path)s
""" % {"previous_path":previous_path})