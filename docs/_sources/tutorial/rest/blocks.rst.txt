.. _rest_blocks:

Text Blocks
###########

Blocks of text are identified by the following markups:

*  Indentation is as important in reST as it is in Python
*  Double column element ``::``
*  Docutils directives


Paragraph
=========

Paragraph is a left-aligned text block. Docutils convert it to an HTML paragraph. For example, this paragraph, you are
reading now, looks as follows in HTML::

   <p>
      "Paragraph is a left-aligned text block. Docutils converts it to an HTML paragraph. For example, this paragraph,
      you are reading now, looks as follows in HTML:"
   </p>


.. _rest_blocks_quote:

Block quote
===========

Typically, block quotes contain quotations from other sources. To mark up a paragraph as a block quote, move all its
lines to the right, that is, make it indented, similar to this example::

   Normal paragraph that is left-aligned. The following is a block quote:

      Block quote is indented with 3-4 spaces.

Docutils converts this construction to the following group of HTML elements::

   <blockquote>
      <div>
         <p>Block quote is indented with 3-4 spaces.</p>
      </div>
   </blockquote>

If you make several block quotes separated by blank lines, you will get the corresponding <div></div> pair for each.


.. _rest_blocks_literal:

Literal block
=============

A literal block presents source data as it is without any changes. It does not change even line breaks in the text
that it presents. To make a literal block from a paragraph, move it to the right and mark it up with one of
the following elements:

*  To the previous paragraph, append a double column (``::``), so that the preceding paragraph and a literal block look
   similar to this::

      A normal paragraph ended with double column::

         A literal block indented to the right.

*  Use the left-aligned special markup directive ``code-block`` as follows::

      .. code-block:: <language>

         A literal block indented to the right.

   The <language> parameter specifies the code language of the literal block, for example, ``rst`` means reST.


Lists
=====

Classification
--------------

Lists can be of two different types:

*  A ordered list presents a sequence of actions enumerated by numbers (1, 2, ...), Roman numerals (i, ii, ...), lower
   case alphabet (a, b, ...), or upper case alphabet (A, B, ...). In addition, these numbers or letters can be
   arranged with the following formatting:

   -  Followed by period, for example, ``1.``, ``2.``, and so on.
   -  Surrounded by parenthesis, for example, ``(a)``, ``(b)``, and so on.
   -  Followed by a right round bracket, for example, ``1)``, ``2)``, and so on.

*  An unordered list presents any list of items that don't require ordering. An item is preceded with one of the
   symbols: ``*`` (asterisk), ``-`` (hyphen), or ``+`` (plus sign).

Ordered and unordered list can be nested within each other using indentation.


Examples
--------

Nested unordered lists::

   *  First item of the parent list.

      - First item of the nested list.
      - Second item of the nested list.

   *  Second item of the parent list.

Ordered list with nested unordered list::

   1. First item of the parent list.

      * First item of the nested list.
      * Second item of the nested list.

   2. Second item of the parent list.

You can have Sphinx enumerate items automatically. For this purpose, use the ``#.`` markup element, for example::

   #. First item of the parent list.
   #. Second item.

This will be the same as::

   1. First item of the parent list.
   2. Second item.



