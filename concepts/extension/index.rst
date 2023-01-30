.. _concepts_ext:

Sphinx Extensions
#################


Extension types
===============

Every extension is a Python package that adds a specific functionality to Sphinx such as:

*  Sphinx directives and roles
*  Templates of HTML output
*  Sphinx builders
*  Source parsers
*


. To use an extension, you need
to add its name to the ``extensions`` list in the ``conf.py`` file.

Sphinx can work with the following groups of extensions:

*  Embedded extensions are installed along with the Sphinx package.
   To add such an extension to your project, you need only to add its name to the ``extensions`` list.
   These packages are in the ``site-packages/sphinx/ext/`` folder. Therefore, a module name that you can add
   to the ``extensions`` list is ``sphinx.ext.<module_name>``.

*  Custom extensions from known groups: `Sphinx contribution <https://github.com/sphinx-contrib/>`_ and
   `Sphinx Extensions <https://sphinx-extensions.readthedocs.org>`_.
   You need to install such an extension and add its name to the ``extensions`` list.

*  Custom extensions from arbitrary source, for example, from `PyPi <https.pypi.org>`_.
   You need to install such an extension and add its name to the ``extensions`` list.

*  Project specific extension as a separate module. You can add a custom Python package inside the project folder,
   for example, ``_ext`` and add this folder to the Python ``sys.path`` list::

      $ sys.path.append(os.path.abspath('_ext'))

   Then you can add the respective name to the ``extensions`` list.

*  Project specific extension in the ``conf.py`` file.
   You can add a small extension directly to the ``conf.py`` file using the ``setup()`` function.

