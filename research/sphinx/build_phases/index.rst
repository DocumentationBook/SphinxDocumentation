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

#. Call the ``read`` method::

      with logging.pending_warnings():
         updated_docnames = set(self.read())


Project state
=============


