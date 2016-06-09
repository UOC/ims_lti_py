import sys

from setuptools import setup, find_packages

v = sys.version_info
if v[:2] < (3, 0):
    error = "ERROR: ims_lti_py requires Python version 3.0 or above."
    print(error, file=sys.stderr)
    sys.exit(1)

setup_args = dict(
    name='ims_lti_py',
    version='0.7',
    description=('A Python library to help implement IMS '
                 'LTI tool consumers and providers'),
    author='Anson MacKeracher',
    author_email='anson@tophatmonocle.com',
    url='https://github.com/tophatmonocle/ims_lti_py',
    packages=find_packages(),
    dependency_links=["https://github.com/simplegeo/python-oauth2#egg=python-oauth2-uocbeta"],
    license='MIT License',
    keywords='lti',
    zip_safe=True,
    test_suite='tests',
)

if 'bdist_wheel' in sys.argv:
    import setuptools

# setuptools requirements
if 'setuptools' in sys.modules:
    setup_args['install_requires'] = install_requires = []
    with open('requirements.txt') as f:
        for line in f.readlines():
            req = line.strip()
            if not req or req.startswith(('-e', '#')):
                continue
            install_requires.append(req)


def main():
    setup(**setup_args)

if __name__ == '__main__':
    main()