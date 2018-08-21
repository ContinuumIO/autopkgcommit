from setuptools import setup
import versioneer

requirements = [
    # package requirements go here
]

setup(
    name='autopkgcommit',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Commit index changes with a list of what has changed (package name, version, build number)",
    author="Anaconda, Inc.",
    author_email='conda@anaconda.com',
    url='https://github.com/continuumio/autopkgcommit',
    packages=['autopkgcommit'],
    entry_points={
        'console_scripts': [
            'autopkgcommit=autopkgcommit.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='autopkgcommit',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ]
)
