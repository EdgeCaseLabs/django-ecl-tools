from distutils.core import setup


version = __import__('ecl_tools').get_version()

setup(name='django-ecl-tools',
      version=version,
      packages=[
          'ecl_tools',
          'ecl_tools.config',
          'ecl_tools.mail',
          'ecl_tools.security',
          'ecl_tools.utils',
      ],
      author='Edge Case Labs, LLC',
      author_email='software@edgecaselabs.com',
      url='http://EdgeCaseLabs.com',
      extras_require={'django', 'south'}
)