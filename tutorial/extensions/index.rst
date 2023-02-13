.. _tutorial_ext:

Extension Management
####################

This is a set of exercises with Sphinx extensions.

Switch to a specific theme
==========================

In the following process, you will switch your documentation site to the ``sphinx_rtd_theme`` theme.
This is an external theme, therefore you need to install the respective Python package.

#. Install the ``sphinx_rtd_theme`` package using a conda or pip package manager, for example::

      $ conda install -c conda-forge sphinx_rtd_theme

#. In the ``conf.py`` file assign  '`sphinx_rtd_theme`' to the ``html_theme`` variable::

       html_theme = `sphinx_rtd_theme`

#. Build your documentation using the theme brought by this extension::

      $ make dirhtml

   Ensure that there are no errors preventing the build process.

#. Verify how the rebuilt web site look now.


