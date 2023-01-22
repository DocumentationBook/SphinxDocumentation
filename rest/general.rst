.. _rest_general:

General Rules
#############

To start with reST, you need to know the following fundamental things:

*  reST is sensitive to text `indentation` similar to Python code. For example, a normal paragraph must be left-aligned,
   and a quotation must be indented to the right.
*  Indentation enables you to nest text blocks within each other by moving the child block to the right of its
   parent.
*  reST uses `directives` and indentation to mark up text blocks, thus making them of different types (literal
   blocks, tables, and many others).
*  reST enables you to use `roles` to mark up inline elements (for example, hyperlinks) in text blocks.
*  reST provides several markup primitives for inline markup (emphasised elements, bold elements, hyperlinks,
   and others). This enables you to make text parts emphasized, bold,
   mono-spaced, and so on.


Indentation
===========

Indentation is widely used to mark up text blocks as belonging to a certain type.
To make a :ref:`quotation block<rest_blocks_quote>`, the block indentation is enough.
To mark up other types of blocks, indentation is used along with directives.


Directives
==========

A `directive` is a reST element that marks up a block of text. Generally,
a marked up block looks as follows::

   .. <directive type>:: <argument (optional)>
      <option 1>
      <option 2>
      <...>

      <Content>

The construction ".. <directive type>:: " including two spaces in it is called a `directive marker`.

.. note:: The directive type is left-aligned to the parent block, but the text block is indented.

Another generalized example is as follows::

   .. <directive>:: Block of text.

See the examples in :ref:`rest_blocks`.


Roles
=====

A `role` is a reST element that marks up inline parts in a text block. Typically, it is used to refer to another
documentation part, for example, to a section or a glossary term definition.
Generally, a marked up text part looks as in the following schemas:

*  Specify the text label explicitly::

   :<role>:`label <invisible reference>`

*  Specify only the reference, so that the label will be substituted with the referred text::

   :<role>:`reference`

.. note:: The whole construction is embedded into the text block.

See the examples in :ref:`rest_links`.


Markup primitives
=================

Markup primitives in reST are simple usually one-char elements used for inline markups, building tables, and other
markup purposes. There are the following groups:

*  Inline markup:

   ``*``, ``**``, `````, ``````, ``<``, ``>``, ``_``

   See examples in :ref:`rest_inline` and :ref:`rest_links`.

*  Header underline and overline:

   ``#``, ``=``, ``-``, ``*``, ``^``, ``'``

   See examples in :ref:`rest_headers`.

*  Table drawing:

   ``-``, ``+``, ``-``, ``=``, ``|``.

   See examples in :ref:`rest_tables`.

*  Literal block:

   ``::``

   See an example in :ref:`rest_blocks_literal`.


Additional resources
====================

*  `A ReStructuredText Primer <https://docutils.sourceforge.io/docs/user/rst/quickstart.html>`_ from Docutils
*  `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_ from Sphinx
*  `reStructuredText Markup Specification <reStructuredText Markup Specification>`_
