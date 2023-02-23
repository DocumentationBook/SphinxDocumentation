.. _concepts_sphinx_event:

Events
######

Event management is a convenient and powerful mechanism of monitoring and controlling the processes.


Event emission
==============

To get messages about events emitted by Sphinx during documentation build process, add ``-vv` argument
to the ``sphinx-build`` command.
You will see messages similar to the following::

   writing output... [ 33%] folder1/index
   [app] emitting event: 'doctree-resolved'(<document: <section "folder 1 index file"...>>, 'folder1/index')
   [app] emitting event: 'html-page-context'('folder1/index', 'page.html', {'embedded': False, 'project': 'Python',
   'release': '', 'version': ''

