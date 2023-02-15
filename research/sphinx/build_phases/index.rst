.. _research_sphinx_process_phases:

Building Phases
###############

.. graphviz:: build_phases.gv

The building phases start with the ``app.build`` method called by the ``build_main`` function
after completing the INITIALIZATION phase as presented earlier in :ref:`research_sphinx_process_top`.

The main steps of the process are presented on the following diagram:

.. uml:: build_phases.puml
   :alt: Build phases

Sphinx executes the build phases in the following order at the top level (see the diagram for the order numbers):

#. Start the build phases by calling the ``app.build`` method.
   First, it declares the start of the READING phase.
   Depending on the command arguments and the source state, it calls one of the following methods:

   *  ``build_all`` if the ``sphinx-build`` command requires to rebuild all documents.
   *  ``build_specific`` if the command requires to build the specific files.
   *  ``build_update`` to process the updated source files and build the documents from them.
      This is the default behaviour used when the other two are not required.
      This method is considered in the following steps.

   When the called method completes, the ``app.build`` method cleans up the build environment
   and prints the summary results of all the phases.

#. Call the ``app.build.build_update`` method that initiates collection of source data and starts
   the build orchestration method.

#. Call the ``app.build.get_outdated_docs`` method to get a list of updated documents. It returns a generator
   of the discovered source files, so that the ``to_build`` variable will yield source file paths similar to this::

      to_build: ['index', 'folder1/index', 'folder2/index']

   This data is taken from the ``env.found_docs`` property method, which in its turn read it from ``project.docnames``.
   The latter was prepare during :ref:`INITIALIZATION<research_sphinx_process_app>`.

#. Call the ``app.build.build`` method that works as the phase orchestrator.
   It receives a list of source file paths and a phrase for printing similar to this::

      targets for 3 source files that are out of date

#. Call the ``app.build.read`` method that implements the main part of the READING phase::

      with logging.pending_warnings():
         updated_docnames = set(self.read())

   At this phase, Sphinx works closely with Docutils to parse each source document and obtain the hierarchical
   node structure.

#. Call the ``app.env.check_consistency`` method to check that all source documents are added to the
   ``env.files_to_rebuild`` list except for the root document, orphans, and documents included by other
   documents. The method also checks for domain consistency by calling the ``domain.check_consistency`` method
   for each domain in the ``env.domains`` dictionary. In the example considered here, the method works with
   the following values:

   *  ``env.all_docs``: ``{'folder1/index': 1676118279.329916, 'folder2/index': 1676118279.332646,``
                           ``'index': 1676118279.337593}``
   *  ``env.files_to_rebuild``: ``{'folder1/index': {'index'}, 'folder2/index': {'index'}}``
   *  Domains: ``c.CDomain``, ``changeset.ChangeSetDomain``, ``citation.CitationDomain``, cpp.CPPDomain,
      ``index.IndexDomain``, ``.javascript.JavaScriptDomain``, ``math.MathDomain``, ``python.PythonDomain``,
      ``rst.ReSTDomain``, ``std.StandardDomain``

   Finally, the method emits the ``env-check-consistency`` event::

      self.events.emit('env-check-consistency', self)

   .. note:: This is where you can handle the event emitted after the source documents are checked
      on consistency.

#. Call the ``app.build.write`` method to implement the RESOLVING and WRITING phases.
