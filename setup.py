from setuptools import setup

version = '1.0.0'

requirements = []
dev_requirements = [
      'pytest>=3.5.1'
]

setup(name='python-edu-system-search',
      version=version,
      description="Exercise to demonstrate how to use Python to interact with the file system",
      author='Jonathon Carlyon',
      author_email='JonathonCarlyon@gmail.com',
      url='https://github.com/JonnyFb421/python-edu-search-system',
      install_requires=requirements,
      extras_require={'dev': dev_requirements},
      packages=['search_system'],
      entry_points={
            'console_scripts': [
                  'search_system = search_system.search.main'
            ]
      }
)
