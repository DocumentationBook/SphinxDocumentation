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

#. Call the ``app.builder.build_update`` method that initiates the collection of source data and starts
   the build orchestration method. It calls ``app.builder.get_outdated_docs`` method to get a list of updated
   source documents and then ``app.builder.build`` to update the corresponding targeted documents.

#. Call the ``app.builder.get_outdated_docs`` method to get a list of outdated documents, which are those that
   depend on the updated documents.
   It returns a generator of the discovered source files, so that the ``to_build`` variable will yield source file paths
   similar to this::

      to_build: ['index', 'folder1/index', 'folder2/index']

   This data is taken from the ``env.found_docs`` property method, which in its turn read it from ``project.docnames``.
   The latter was prepared during :ref:`INITIALIZATION<research_sphinx_process_app>`.

#. Call the ``app.builder.build`` method that works as the phase orchestrator.
   It receives a list of source file paths and a phrase for printing that you will see on the screen.
   It is similar to this::

      targets for 3 source files that are out of date

#. Call the ``app.builder.read`` method that implements the main part of the READING phase::

      with logging.pending_warnings():
         updated_docnames = set(self.read())

   In this phase, Sphinx works closely with Docutils to parse each source document and obtain the hierarchical
   node structure of it. The ``app.builder.read`` method returns a list of names of the documents that were updated
   or added. The ``app.builder.build`` method extends this list with the names of outdated documents, which are
   those that depend on the updated documents. It creates the following name lists:

   *  ``updated_docnames`` includes the names of the *updated and outdated* documents
   *  ``outdated`` consists of the names of the *outdated* documents

   The ``app.builder.build`` method pickles the ``updated_docnames`` list.

#. Call the ``app.env.check_consistency`` method to check that all source documents are added to the
   ``env.files_to_rebuild`` list, except for the root document, orphans, and documents included by other
   documents. The method also checks for domain consistency by calling the ``domain.check_consistency`` method
   for each domain in the ``env.domains`` dictionary. In the example considered here, the method works with
   the following values:

   *  | ``env.all_docs``:
      | ``{'folder1/index':1676118279.329916,'folder2/index':1676118279.332646,``
      | ``'index':1676118279.337593}``

   *  ``env.files_to_rebuild``: ``{'folder1/index': {'index'}, 'folder2/index': {'index'}}``
   *  Domains: ``c.CDomain``, ``changeset.ChangeSetDomain``, ``citation.CitationDomain``, ``cpp.CPPDomain``,
      ``index.IndexDomain``, ``.javascript.JavaScriptDomain``, ``math.MathDomain``, ``python.PythonDomain``,
      ``rst.ReSTDomain``, ``std.StandardDomain``

   Finally, the method emits the 'env-check-consistency' event::

      self.events.emit('env-check-consistency', self)

   .. note:: This is where you can handle the 'env-check-consistency' event emitted after
      the source documents are checked on consistency.

#. Call the ``app.builder.write`` method to implement the RESOLVING and WRITING phases.
