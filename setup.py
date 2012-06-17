from setuptools import setup, find_packages

version = '1.0'

setup(
    name='tn.ploneformwidget.sourcecode',
    version=version,
    description='',
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='',
    author='TN Tecnologia e Negocios',
    author_email='ed@tecnologiaenegocios.com.br',
    url='http://www.tecnologiaenegocios.com.br',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['tn', 'tn.ploneformwidget'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Plone',
        'z3c.form',
    ],
    extras_require={
        'test': []
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
