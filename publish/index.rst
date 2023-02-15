.. _resources_pipeline:

Publishing
##########

Here you will find various ways of publishing the documentation on a web server.


On premise publishing
=====================

Doc-as-code paradigm implies that the documentation development life cycle (DDLC) looks similar
to the software development life cycle (SDLC).
This may sound arguable, but most developers and writers mean this.
The process includes the following steps:

#. (Optional) Preprocess some resources to build intermediate reST documents and images. Typically, developers
   create special scripts to extract data that must be synced with the documentation.
#. Write static documentation using reST markup.
#. Validate the documentation build process and fix the documents if needed.
#. Commit the updates in Git, push the commit to the Git server, and assign reviewers.
#. Discuss the feedback and fix the documents if needed.
#. Merge the updates with the current Git branch.
#. Publish the updated documentation on the documentation web site.


Publishing to GitHub Pages
==========================

GitHub Pages is a documentation hosting service that enables you to publish your documentation on a separate subdomain
in the ``github.io`` domain. It may look as follows:

*  ``<your-organization-name>.github.io>``
*  ``<your-github-login-name>.github.io>``

It accepts a built documentation set, that is, all HTML, CSS, and JavaScript files compiled and ready to publish,
or you can configure a special process.

.. note:: To use this hosting, you need to have a GitHub account and have your documentation project stored in a
   `GitHub <https://github.com>`_ repository synced with your local git repository.

Pay attention to the following GitHub Pages specifics when you publish compiled HTML documents:

*  It imports data only from the root folder or from the ``docs/`` folder in a GitHub repository.
*  GitHub Pages does not import folders, which names start with an underscore.
   For example, Sphinx copies images to the ``_images/`` folder and uses the ``_static/`` to store CSS, JavaScript and
   other files. One work around is to rename those folders and all links to them in all HTML files before you publish
   the documentation. This requires additional configuration steps.

The following steps help you manage these specifics:

#. In the ``Makefile`` file, add one more destination for the compiled HTML documents, for example::

      GITPAGES      = docs

#. In the ``Makefile`` file, add a rule for the new type of building, for example called ``pages``::

      pages:
         @rm -rf docs
         @$(SPHINXBUILD) -b dirhtml "$(SOURCEDIR)" "$(GITPAGES)" $(SPHINXOPTS) $(O)
         @./postbuild_gitpages.sh

   With this rule, the ``makefile`` utility will do the following:

   *  Remove the ``docs/`` folder containing HTML documents from the previous build.

      .. note:: It means you have to rebuild the whole documentation, which may take substantial time.
         Therefore, it's better to fix all problems locally using the typical procedure before you start this process.

   *  Run the ``sphinx-build`` command using the newly assigned destination path.
   *  Run the script (see the next step) to make necessary substitutions.

#. Create a shell script, for example, ``postbuild_gitpages.sh`` with the following contents::

      for file in $(find docs -name "*.html")
      do
          echo $file
          sed -i '' -e 's@_images/@images/@g' -e 's@_static/@static/@g' $file
      done

      mv docs/_static docs/static
      mv docs/_images docs/images
      echo _static/ and _images/ are renamed to static/ and images/.

   This script performs the following operations:

   *  In the ``for`` loop, open every HTML file and inside it remove the underscore prefix
      from words ``_images`` and ``_static``.

      .. note:: This sets a restriction on using these words in your documents.

   *  Remove the underscore prefix from folder names ``_images/`` and ``_static/``.

#. In the ``.gitignore`` file, add the following files and folders that are not part of the HTML documentation::

      .buildinfo, .doctrees, _plantuml, objects.inv

After completing all these steps, you can run the build-publish process as follows:

#. Run the building process::

      $ make pages

#. Add and commit the updates::

      $ git add .
      $ git commit -m "Your text message."
      $ git push

#. Follow the `GitHub Pages tutorial <https://docs.github.com/en/pages>`_ to publish
   your documentation from the ``doc/`` folder in your repository on GitHub.
   You can do it using the **Pages** item in the repository **Settings** menu.


Publishing to Read the Docs
===========================

`Read the Docs <https://readthedocs.org/>`_ is a documentation hosting service based primarily on Sphinx
as a tool for a generating documentation tree.


Minimal requirements
--------------------

Minimal requirements:

#. Sign up to the `Read the Docs <https://readthedocs.org/>`_ to have your account there.
#. In your documentation project, add
   the ``requirement.txt`` file that have a list of Python modules to be used during the build process.
   These are Sphinx and additional packages that you installed in your development environment (virtenv or conda).
#. Your Git-based repository (GitHub or another) must contain the full Sphinx-based documentation project.


Additional configuration
------------------------

A stable system, which Read The Docs is, uses reliable components that can be older than you expect.
That is why you may experience some unexpected behaviour.
For example, when I published my project for the first time, this system was using a Docker container with
an old version of Ubuntu and consequently old version of Graphviz.
This results in incorrect representation of some UML graphs.

To manage such cases, you can add the ``.readthedocs.yaml`` configuration file and specify options that are
most crucial for you project. This is an example contents::

   # .readthedocs.yaml
   # Read the Docs configuration file
   # See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

   # Required
   version: 2

   # Set the version of Python and other tools you might need
   build:
     os: ubuntu-22.04
     tools:
       python: "3.10"
       # You can also specify other tool versions:
       # nodejs: "19"
       # rust: "1.64"
       # golang: "1.19"
     apt_packages:
       - graphviz
       - plantuml


   # Build documentation in the docs/ directory with Sphinx
   sphinx:
      builder: dirhtml
      configuration: conf.py

   # If using Sphinx, optionally build your docs in additional formats such as PDF
   # formats:
   #    - pdf

   # Optionally declare the Python requirements required to build your docs
   python:
      install:
      - requirements: requirements.txt

Pay attention to the following requirements:

*  Use the OS Ubunto of the specified version.
   Specify the latest LTS (long-term support) version, as the system doesn't accept non-LTS versions.
*  Specify the Python version that you use in your project locally, which is verified on your project.
*  Specify the crucial ``apt`` packages that you want to be installed.
   In this example, they are ``graphviz`` and ``plantuml``.

Other options in this configuration are obvious. It also contains a link to the full documentation.


Additional resources
====================

* `UnlockedEdu/documentation-pipeline-generator <https://github.com/UnlockedEdu/documentation-pipeline-generator>`_ and
   a separate `documentation site <https://unlockededu.github.io/documentation-pipeline-generator/>`_
*  `Docs-as-code pipeline on GitLab using Sphinx and Docker <https://gitlab.com/papercut-docs-as-code/docs-as-code>`_
*  `Treat Docs Like Code: GitHub and Sphinx <https://www.docslikecode.com/>`_
*  `GitHub Pages <https://docs.github.com/en/pages>`_
*  `Read the Docs Tutorial <https://docs.readthedocs.io/en/stable/tutorial/>`_