.. _concepts_sphinx_config:

Configuration
#############

Sphinx documentation build process uses specific configuration that can be set through command-line arguments and
through a configuration file. There are so many parameters required by Sphinx that it is practically impossible to
specify all of them in a command line. That is why in a normal process, a configuration file is required. You can
specify the path to the configuration file in a command or the default rules will be used as follows:

*  The default *configuration directory* is the source folder specified in the ``sphinx-build`` command.
*  The default Sphinx configuration file is ``conf.py`` in the configuration directory. This is a Python script
   that Sphinx runs during the build process to get all configuration parameters it needs.
*  In Sphinx, there are many parameters with default values that you can change in ``conf.py``.
*  In the command line, you can override parameters specified in ``conf.py``.
*  If you need to set some Docutils specific parameters, you can add the
   `docutils.conf <https://docutils.sourceforge.io/docs/user/config.html>`_ file with those parameters
   defined in it.
