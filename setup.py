import sys

from setuptools import setup, find_packages

setup_args = dict(
    name='ims_lti_py',
    version='0.6',
    description=('A Python library to help implement IMS '
                 'LTI tool consumers and providers'),
    author='Anson MacKeracher',
    author_email='anson@tophatmonocle.com',
    url='https://github.com/tophatmonocle/ims_lti_py',
    packages=find_packages(),
    install_requires=['lxml', 'oauth2'],
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