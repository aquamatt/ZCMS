from setuptools import setup, find_packages

setup(
    name='zcms',
    version='0.0.1',
    description='Experimental CMS functionality',
    author='Matthew Pontefract',
    author_email='matthew@zorinholdings.com',
    packages=['zcms','zcms.templatetags'],
    package_data={'': ["templates/*.html",]},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)

