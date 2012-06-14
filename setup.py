from distutils.core import setup

setup(
    name='Qi',
    version='0.1.0',
    author='Vinhthuy Phan',
    author_email='vphan@memphis.edu',
    packages=['qi'],
    scripts=['qi/qi.py'],
    url='https://github.com/vtphan/qi',
    license='MIT',
    description='A Python web framework.',
    long_description='A Python web framework.',
    install_requires=[
        "webob",
    ],
)