from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
  scripts=['scripts/pathplanner_node.py'],
  scripts=['scripts/Collision_dector.py'],)
setup(**d)
