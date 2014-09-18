from distutils.core import setup

def readme():
    from docutils.core import publish_file
    import os.path
    filename = 'README.rst'
    with open(filename, 'r') as fi:
        f, ext = os.path.splitext(filename)
        htmlfile = f + '.html'
        with open(htmlfile, "w") as fo:
            publish_file(source=fi, destination=fo, writer_name='html')

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
      extras_require={'django', 'south'},
      long_description = readme()
)


