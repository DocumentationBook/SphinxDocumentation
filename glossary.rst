.. _sphinx_glossary:

Glossary
########

.. glossary::
   :sorted:

   BOM
   Byte Order Mark
      When using the UTF encoding, it is important to know the sequence of bytes, when a character requires more than
      one byte.
      A character can be started with the largest byte (big-endian order) or smallest byte (little-endian order).
      In some encoding types (UTF-8-sig, UTF-16, UTF-32), BOM is specified at the beginning of a file.
      In other encoding types (UTF-16BE, UTF-16LE, UTF-32BE, UTF-32LE) the byte order is fixed.
      (`Source <https://unicode.org/faq/utf_bom.html>`_)

   Docutils
      A Python package installed along with Sphinx and being the main reST interpreter.

   DTD
      Docutils `DTD <https://docutils.sourceforge.io/docs/ref/docutils.dtd>`_ (document type definition) created in
      accordance with the `DocBook <https://tdg.docbook.org/>`_ standard.

   Glob-style pattern
   Wildcard
      The standard shell constructs * (any characters), ? (any one character),
      [list] (match any character in the list),
      and [!list] (matches any character, except for the characters in the specified list).

   Outdated documents
      These are the documents that were not updated but dependant updated documents.

   UML
   Unified Modeling Language
      UML is a language used to visually represent hardware and software systems, logical objects, math objects,
      sequences, and other materialized and non-materialized objects and processes.

   Updated documents
      A list of updated source documents.
