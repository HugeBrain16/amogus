import setuptools
from amogus import __version__ as version

metadata = {
	"name": "sus-amogus",
	"version": version,
	"description": "sus",
	"author": "HugeBrain16",
	"url": "https://github.com/HugeBrain16/amogus",
	"author_email": "joshtuck373@gmail.com",
	"long_description": open('README.md', encoding='UTF-8').read(),
	"long_description_content_type": "text/markdown",
	"license": "MIT",
	"py_modules": ["amogus"]
}

setuptools.setup(**metadata)
