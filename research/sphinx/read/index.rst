.. _research_sphinx_read:

Read
####

.. graphviz:: phases_read.gv

At the READING phase Sphinx reads all new and updated files.
This phase is declared by the ``app.build`` method as described in :ref:`research_sphinx_process_phases`.

Process
=======

As mentioned earlier, the ``app.build`` method calls the ``app.builder.get_outdated_docs`` method that supplies
a generator of discovered updated documents, but this list is used after the READING phase.

The main steps of the READING phase are performed by the ``app.builder.read`` method as presented
on the following diagram:

.. uml:: read.uml
   :alt: The READING phase

#. Start the ``app.builder.read`` method defined in the ``sphinx.builders.Builder`` class.
   It doesn't have any input parameters declared.
   So it gets everything from the objects created during the INITIALIZATION phase.
   This method starts with logging the beginning of a phrase that will be later printed out on the screen::

      updating environment:

#. Call the ``app.env.find_files`` method defined in the ``sphinx.environment.BuildEnvironment`` class.
   This methods searches and returns three kinds of source documents: ``removed``, ``changed``, and ``added``.

   .. note:: This is where you can handle the 'env-get-outdated' event emitted by the ``app.builder.read`` method.

   In a handler, you are able to make additional changes.
   The handler gets the names of all the three groups of source documents and it
   must return a list of updated sets of documents or an empty list.
   This is how ``app.builder.read`` method emits the event and updates the ``changed`` set::

        # allow user intervention as well
        for docs in self.events.emit('env-get-outdated', self.env, added, changed, removed):
            changed.update(set(docs) & self.env.found_docs)

#. Call the ``app.env.clear_doc`` method to remove those built documents whose source files were removed.
   Before calling this method, the ``app.build.read`` method emits the 'env-purge-doc' event::

        for docname in removed:
            self.events.emit('env-purge-doc', self.env, docname)
            self.env.clear_doc(docname)

   .. note:: This is where you can handle the 'env-purge-doc' event emitted by the ``app.builder.read`` method
      before removing the documents.

#. Verify if the parallel processing is required by checking the ``self.app.parallel`` attribute and respectively
   call the ``app.builder._read_parallel`` or the ``app.builder._read_serial`` method.
   This example process uses the latter. This is the method that takes most time at the READING phase.




Project state
=============


