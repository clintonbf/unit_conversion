from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')
package_dir = 'unit_conversion'

setup(
    name='unitconversions',
    version="0.0.1",
    description="a package for converting units",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/clintonbf/unit_conversion",
    author="Clinton Fernandes",
    author_email="clint.fernandes@gmail.com",

    keywords="unit, conversion, math, measurement, science",

    package_dir={'': package_dir},
    packages=find_packages(where=package_dir)

)