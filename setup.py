import os
import setuptools


ROOT = os.path.dirname(__file__)


def get_file_content(file_name):
    with open(file_name, 'r') as fh:
        content = fh.read()
    return content


about = {}
exec(get_file_content(os.path.join(ROOT, 'git', '__version__.py')), about)


#    package_data={'': ['*.tar']},
setuptools.setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=get_file_content('README.md'),
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
