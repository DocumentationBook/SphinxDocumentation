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


Event gallery
=============

While processing documentation, Sphinx emits events from different steps of its phases.
The following sections present events in the order they are emitted in a test project.


config-inited
-------------

Logged message::

   [app] emitting event: 'config-inited'(<sphinx.config.Config object at 0x7f96d21ec760>,)


builder-inited
--------------

Logged message::

   [app] emitting event: 'builder-inited'()


env-get-outdated
----------------

Logged message::

   updating environment: locale_dir /Users/albertbagdasaryan/workspace/SphinxDetailed/__test/locales/en/LC_MESSAGES does not exists
   [app] emitting event: 'env-get-outdated'(<sphinx.environment.BuildEnvironment object at 0x7f96d21ec880>, {'folder1/index', 'index', 'folder2


env-before-read-docs
--------------------

Logged message::

   [new config] 3 added, 0 changed, 0 removed
   [app] emitting event: 'env-before-read-docs'(<sphinx.environment.BuildEnvironment object at 0x7f96d21ec880>, ['folder1/index', 'folder2/index',



env-purge-doc
-------------

This and the following two event are emitted after reading a source document, for example after reading one of
three documents (33% read)::

Logged message::

   reading sources... [ 33%] folder1/index
   [app] emitting event: 'env-purge-doc'(<sphinx.environment.BuildEnvironment object at 0x7f96d21ec880>, 'folder1/index')


source-read
-----------

Logged message::

   [app] emitting event: 'source-read'('folder1/index', ['Folder 1 Index File\n###################\n\nFile content of the Folder 1 index i


doctree-read
------------

Logged message::

   [app] emitting event: 'doctree-read'(<document: <section "folder 1 index file"...>>,)


env-updated
-----------

This event is emitted after all source documents are read.

Logged message::

   [app] emitting event: 'env-updated'(<sphinx.environment.BuildEnvironment object at 0x7f96d21ec880>,)


env-get-updated
---------------

Logged message::

   looking for now-outdated files... [app] emitting event: 'env-get-updated'(<sphinx.environment.BuildEnvironment object at 0x7f96d21ec880>,)
   none found


env-check-consistency
---------------------

Logged message::

   pickling environment... done
   checking consistency... [app] emitting event: 'env-check-consistency'(<sphinx.environment.BuildEnvironment object at 0x7f96d21ec880>,)
   done


doctree-resolved
----------------

This and the next event are emitted after writing every document, for example, after writing one of three documents:

Logged message::

   docnames to write: folder1/index, folder2/index, index
   preparing documents... done
   writing output... [ 33%] folder1/index
   [app] emitting event: 'doctree-resolved'(<document: <section "folder 1 index file"...>>, 'folder1/index')


html-page-context
-----------------

Logged message::

   [app] emitting event: 'html-page-context'('folder1/index', 'page.html', {'embedded': False, 'project': 'Python', 'release': '', 'version': ''


html-page-context of the general index
--------------------------------------

Logged message::

   generating indices... genindex [app] emitting event: 'html-page-context'('genindex', 'genindex.html', {'embedded': False, 'project': 'Python', 'release': '', 'version': '',
   done


html-collect-pages
------------------

Logged message::

   [app] emitting event: 'html-collect-pages'()


html-page-context of additional pages
-------------------------------------

Logged message::

   writing additional pages... search [app] emitting event: 'html-page-context'('search', 'search.html', {'embedded': False, 'project': 'Python', 'release': '', 'version': '', 'la
   done


build-finished
--------------

Logged message::

   copying static files... done
   copying extra files... done
   dumping search index in English (code: en)... done
   dumping object inventory... done
   [app] emitting event: 'build-finished'(None,)
   build succeeded.

