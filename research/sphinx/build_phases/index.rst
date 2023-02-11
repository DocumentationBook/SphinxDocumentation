.. _research_sphinx_process_phases:

Build Phases
############

.. graphviz:: build_phases.gv

The building phases start with the ``app.build`` method called by the ``build_main`` function
after completing the INITIALIZATION phase as presented earlier in :ref:`research_sphinx_process_top`.

Process
=======

The main steps of the process are presented on the following diagram:

.. uml:: build_phases.uml

Sphinx executes the build phases in the following order at the top level (see the diagram for the order numbers):

#. Start the build phases by calling the ``app.build`` method.
   First, it declares the start of the READING phase.
   Depending ot the command requirement and the source state, it calls one of the following methods:

   *  ``build_all`` if the ``sphinx-build`` command requires to rebuild all documents.
   *  ``build_specific`` if the command requires to build the specific files.
   *  ``build_update`` to process the updated source files and build the documents from them.
      This is the default behaviour used when the other two are not required.
      This method is considered in the following steps.

   When the called method completes, the ``app.build`` method cleans up the build environment
   and prints the summary results of all the phases.

#. Call the ``app.build.build_update`` method that initiates collection of source data and starts
   the build orchestration method.

#. Call the ``app.build.get_outdated_docs`` method to get a list of updated documents.

#. that works as the phase orchestrator.  It receives a list of source files and a phrase for printing similar to this::

      targets for 3 source files that are out of date

#. Call the ``read`` method::

      with logging.pending_warnings():
         updated_docnames = set(self.read())


Project state
=============


