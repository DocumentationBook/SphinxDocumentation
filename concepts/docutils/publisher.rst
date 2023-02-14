.. _concepts_docutils_publisher:

Publisher
#########

The central entity is the ``Publisher`` class that encapsulating the high-level logic of a Docutils system and
provides necessary methods to orchestrate the whole process in the following order:

#. Reading the source. A reader reads the source and runs parsing several times:

   * Parsing.
   * ...
   * Parsing.

#. Transforming.
#. Creating the output.

Docutils exposes several endpoints for calling the ``Publisher`` class:

*  End user front-end utilities (``rst2html.py``, ``rst2html5.py``, ``rst2latex.py``, ``rst2odt.py``, and many more)
   enable a user to convert a reST file into a required format. For this purpose, in the command line,
   specify a utility, a source, and output as in this example::

      $ rst2html5 index.rst index.html

   Each utility calls a specific Docutils writer that must output the result in a certain format.
   For example, ``rst2html5.py`` produces an HTML5 file.

*  `Publisher API <https://docutils.sourceforge.io/docs/api/publisher.html#publisher-convenience-functions>`_:
   ``docutils.core.publish_*`` functions.

   Front-end utilities call the ``docutils.core.publish_cmdline`` function. The other Publisher functions works with
   specific types of input and output data, such as file, string, dictionary, and document tree. Sphinx calls
   only the ``publish_doctree`` for testing purposes by ``sphinx/testing/restructuredtext.py``.

*  Direct creation of objects from the ``Publisher`` class. Sphinx uses this way to integrate with Docutils.
