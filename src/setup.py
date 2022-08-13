from setuptools import setup

setup(name='netilion_api',
      version='1.0.8',
      description='',
      url='',
      author='Andrey Dodonov',
      author_email='Andrey.Dodonov@endress.com',
      license='MIT',
      packages=['netilion_api'],
       install_requires=[
          'certifi',
          'six',
          'python_dateutil',
          'setuptools',
          'urllib3'
      ],
      zip_safe=False)
