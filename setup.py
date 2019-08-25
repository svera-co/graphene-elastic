from setuptools import find_packages, setup

setup(
    name="graphene-elastic",
    version="0.0.2",
    description="Graphene Elasticsearch (DSL) integration",
    long_description=open("README.rst").read(),
    url="https://github.com/barseghyanartur/graphene-elastic",
    author="Artur Barseghyan",
    author_email="artur.barseghyan@gmail.com",
    license="GPL 2.0/LGPL 2.1",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        # "Programming Language :: Python :: 2.7",
        # 'Programming Language :: Python :: 3.5',
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="api graphql protocol rest relay graphene elasticsearch "
    "elasticsearch-dsl",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "graphene>=2.1.3,<3",
        "elasticsearch>=5.0",
        "elasticsearch-dsl>=5.0",
        "singledispatch>=3.4.0.3",
        "iso8601>=0.1.12",
    ],
    python_requires=">=2.7",
    zip_safe=True,
    tests_require=[
        "pytest>=3.3.2",
        # 'mongomock',
        "mock",
    ],
)