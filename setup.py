from setuptools import setup, find_packages
from twitter_timeline_rss import __version__ as version


setup(
    name='twitter-timeline-rss',
    version=version,
    description=('Ingest a twitter timeline and render as RSS'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    keywords='twitter timeline rss atom flask',
    author='Jon Robison',
    author_email='narfman0@gmail.com',
    url='https://github.com/narfman0/twitter-timeline-rss',
    license='LICENSE',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=['tweepy', 'flask'],
    tests_require=['tox', 'coverage', 'flake8', 'wheel'],
    test_suite='tests',
    entry_points={
        'console_scripts': ['twitter_timeline_rss=twitter_timeline_rss.cli:main'],
    }
)
