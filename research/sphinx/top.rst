.. _research_sphinx_process_top:

Top Level Operations
####################

The top level operations prepare the environment and start the documentation build process.


The process
===========

The first steps are presented in the following diagram:

.. uml:: top.uml

The process includes the following operations:

#. The ``sphinx-build`` module initiates the process and returns the resultant code to the system, so that you can check this code
   in your shell commands and scripts::

      sys.exit(main)

#. The ``sphinx.cmd.builds.main`` function sets up the locale and calls the top-level orchestrator of the processes ``build_main``::

      sphinx.locale.setlocale(locale.LC_ALL, '')
      sphinx.locale.init_console(os.path.join(package_dir, 'locale'), 'sphinx')

      return build_main(argv)

#. The ``sphinx.cmd.builds.build_main`` function validates and collects arguments passed
   to the ``sphinx-build`` command (``argv``),
   requests creation of the main application, and starts the building processes as follows:

   #. Use the Python standard class ``argparse.ArgumentParser`` to validate and collect all command line arguments.
      If it detects an error, it completes the operations with an error message. Otherwise, it stores the arguments
      in the ``args`` (not displayed in the diagram)::

         parser = get_parser()
         args = parser.parse_args(argv)

   #. Validate deeper the arguments collected in the ``args`` object.
   #. Request creation of the main object of the whole documentation build process. It is created from the
      ``sphinx.application.Sphinx`` class::

         with patch_docutils(confdir), docutils_namespace():
            app = Sphinx(args.sourcedir, args.confdir, args.outputdir,
                         args.doctreedir, args.builder, confoverrides, status,
                         warning, args.freshenv, args.warningiserror,
                         args.tags, args.verbosity, args.jobs, args.keep_going)

      The ``app`` object is created using the arguments collected in the ``args`` object.

   #. Start the documentation build process and return the status code after that. The following commands are inside
      the ``with`` statement of the previous step::

         app.build(args.force_all, filenames)
         return app.statuscode

Project phases
==============

The whole process consists of several phases declared in the ``sphinx.util.build_phase.BuildPhase`` enum class::

   class BuildPhase(IntEnum):
       """Build phase of Sphinx application."""
       INITIALIZATION = 1
       READING = 2
       CONSISTENCY_CHECK = 3
       RESOLVING = 3
       WRITING = 4

.. graphviz:: phases.gv


The first phase, INITIALIZATION, is implemented during creation and initialization of the ``app`` object,
the others are orchestrated by the ``app.build`` method.


More details
============

At the moment, the process consists of the following two global sets of operations presented in more detail
in the following documents:

*  :ref:`research_sphinx_process_app`
*  :ref:`research_sphinx_process_phases`

