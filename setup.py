#!/usr/bin/env python
# -*- coding: latin1 -*-


def main():
    from setuptools import setup

    ver_dic = {}
    version_file = open("cnd/version.py")
    try:
        version_file_contents = version_file.read()
    finally:
        version_file.close()

    exec(compile(version_file_contents, "cnd/version.py", 'exec'), ver_dic)

    setup(name="cnd",
          version=ver_dic["VERSION_TEXT"],
          description="A preprocessor that gives C multidimensional arrays",
          long_description=open("README.rst", "rt").read(),
          author=u"Andreas Kloeckner",
          author_email="inform@tiker.net",
          license="MIT",
          url="http://mathema.tician.de/software/cnd",
          zip_safe=False,

          install_requires=["pycparser", "pycparserext", "ply"],

          scripts=["bin/cnd", "bin/cndcc"],
          packages=["cnd"]
          )

if __name__ == "__main__":
    main()
