.. _tutorial_setup:

Sphinx Setup
############

Sphinx is a Python package, so that you can install it like any other Packages packages.


Installation
============

Depending on your development environment Sphinx can be preinstalled or you can install it within the environment.
Let us consider some widely used environments:

*  `Anaconda <https://docs.anaconda.com/>`_ is a data science collection (distribution) of packages that contains
   a Sphinx package among many other packages.

*  `Conda <https://docs.conda.io/en/latest/>`_ for Python is a package and environment management system. With this
   system, you can create various Python virtual environments. To use Sphinx in an environment, for example,
   environment called `py10` (meaning Python 3.10), install it as follows::

      $ conda install -y sphinx

   .. note:: in the conda environment, you can also use pip if conda cannot find a required Python package.

*  `pip <https://pip.pypa.io/en/stable/>`_ is a package installation tool for Python. Typical implementation is to use
   it in a Python virtual environment created by
   `venv <https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment>`_.
   Inside an environment, install Sphinx using the following command::

      $ pip install -y sphinx

   pip can also work in the conda environment. This is helpful when the conda repository (being more reliable and
   conservative) doesn't contain a required package.


Quick configuration
===================

The Sphinx package contains a special utility called ``sphinx-build`` that walks you through several Sphinx configuration
steps as follows:

#. Run the utility::

      $ sphinx-quickstart

   You will get the welcome message that informs you that the Sphinx framework root path is the current folder. It also
   provides you with a choice of an option for the two:

   *  Make the current folder the root of the source reST documentation tree and build the final documents
      (usually HTML documentation tree) in the ``./_build/`` subfolder.
   *  Make two subfolders, one ``./source/`` for the source reST documentation tree and the other ``build`` for the
      final documentation tree.

   The message looks as follows::

      Welcome to the Sphinx 5.0.2 quickstart utility.

      Please enter values for the following settings (just press Enter to
      accept a default value, if one is given in brackets).

      Selected root path: .

      You have two options for placing the build directory for Sphinx output.
      Either, you use a directory "_build" within the root path, or you separate
      "source" and "build" directories within the root path.
      > Separate source and build directories (y/n) [n]:

#. Both of the two proposed options are widely used. Let us consider the default option. To take it, just press ENTER.

   You are prompted to assign a name for your documentation project::

      The project name will occur in several places in the built documentation.
      > Project name:

#. Enter your project name that suits your goals.

   You are prompted to enter the author's name::

      > Author name(s):

#. Enter your first and last name or a pseudonym.

   You are prompted to enter the documentation project release number::

      > Project release []:

#. Enter the release number you want to assign to the first release of you documentation project.
   For example, enter 0.1.

   Sphinx enables you to select a human language of your documentation other than English::

      If the documents are to be written in a language other than English,
      you can select a language here by its language code. Sphinx will then
      translate text that it generates into that language.

      For a list of supported codes, see
      https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
      > Project language [en]:

#. For your first project, it's easier to select English, so press ENTER.

   This was the last step. Sphinx created the simplest infrastructure consisting of the following typical files and
   folders:

   *  ``index.rst`` is the root document in your documentation tree.
   *  ``conf.py`` is the main configuration file for your documentation project.
   *  ``Makefile`` is a configuration file for the ``make`` utility that is used in every Unix and Linux OS to build
      projects. You can use this utility to have Sphinx build your documentation project.
   *  ``make.bat`` is used in Windows OS instead of the ``make`` utility.
   *  ``_build/`` is a subfolder where Sphinx will created the built project files.
   *  ``_static/`` is a subfolder with custom files for HTML, CSS, and JavaScript. Sphinx will copy all those
      files to the ``_static/`` subfolder in the built project, thus overriding files with the same name created
      by default.
   *  ``_templates/`` contains custom templates. If you place your own templates here, they will override
      Jinja2 templates shipped with Sphinx or Sphinx extensions. Jinja2 templates are used to build HTML files.

   The final message contains an advice to use the ``make`` utility::

      You should now populate your master file /workspace/PythonDocumentationTips/index.rst
      and create other documentation source files. Use the Makefile to build the docs, like so:
         make builder
      where "builder" is one of the supported builders, e.g. html, latex or linkcheck.


Verification
============

After the required components are created, verify if you can build HTML documents using one of the
following commands with the ``html`` or ``dirhtml`` Sphinx builders
(run the commands from your project root folder where the ``Makefile`` file exists)::

   $ make html

or preferably::

   $ make dirhtml

There is the following difference between these two builders:

*  When you use the ``html`` builder, Sphinx compiles an HTML file called, for example, ``name.html`` from a reST file
   called ``name.rst``. So, in a browser, your users will open this file by its name, that is, ``name.html``.
*  The ``dirhtml`` builder creates a folder for each reST file. This folder is named after the source file and it
   contains the ``index.html`` file compiled from the respective reST file.
   For example, if the source file name is ``name.rst``,
   you will get the ``name/index.html`` file. Your users can open this HTML file in their browser by the folder
   name, that is, ``name/`` or ``name``, which looks shorter and simpler than old-school ``name.html``.

For more Sphinx builders, see `Builders <https://www.sphinx-doc.org/en/master/usage/builders/index.html>`_

On completion of the documentation building process you will get the compiled set of HTML documents in a subfolder of
the ``_build/`` folder. The subfolder is named after the Sphinx builder that you have chosen. If the builder is
``dirhtml``, the documentation will be in the ``_build/dirhtml/`` subfolder.

If the verification is successful, you are ready to continue studying the course.
