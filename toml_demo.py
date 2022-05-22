from tomllib import loads
from pprint import pprint

with open('pyproject.toml', 'r') as f:
    project = loads(f.read())
pprint(project)
