.. _rest_tables:

Tables
######

Different approaches
====================

You can use different ways of creating tables:

*  Using grid tables. With this way you use various primitive markup elements
   (``=``, ``-``, ``+``, ``|``) to draw any simple or complex table.
*  Using the ``list-table`` directive. It enables you to create simple tables without spanning
   rows or columns.
*  Using a third party extension that provides a directive similar to ``list-table`` and enables you to make rows and
   columns spanned.

Examples
========

Simple grid table::

   +--------------+----------+-----------+-----------+
   | row 1, col 1 | column 2 | column 3  | column 4  |
   +--------------+----------+-----------+-----------+
   | row 2        |                                  |
   +--------------+----------+-----------+-----------+
   | row 3        |          |           |           |
   +--------------+----------+-----------+-----------+

Even a simpler example::

   =====  =====  =======
   A      B      A and B
   =====  =====  =======
   False  False  False
   True   False  False
   False  True   False
   True   True   True
   =====  =====  =======

Complex grid table::

   +------------------------+------------+----------+----------+
   | Properties             | Attrib 1   | Attrib 2 | Attrib 3 |
   | (header rows)          |            |          |          |
   +========================+============+==========+==========+
   | Property 1             | Value 11   | Value 13 | Value 14 |
   +------------------------+------------+----------+----------+
   | Property 2             | Description (spanned columns)    |
   +------------------------+------------+---------------------+
   | Property 3             | Value 341  | - Item 1            |
   +------------------------+ (span rows)| - Item 1            |
   | Property 4             |            | - Item 1            |
   +------------------------+------------+---------------------+

Using the ``list-table`` directive, you can define the simple table presented earlier as follows::

   .. list-table:: A list table
      :widths: 3 2 2 2
      :header-rows: 1

      *  -  row 1, col 1
         -  column 2
         -  column 3
         -  column 4
      *  -  row 2
         -
         -
         -
      *  -  row 3
         -
         -
         -

Using the ``csv-table`` directive, the table contents is a list of comma-separated lists as in this example::

   .. csv-table:: A CSV-table
      :header: "Properties", "Attribute 1", "Attribute 2", "Description"
      :widths: 3, 3, 3, 5

      "Property 1", 1.11, 1.22, "Property 1 description"
      "Property 2", 2.11, 2.22, "Property 2 description"
      "Property 3", 3,11, 3,22, "Property 3 description"

For more information about the table directives, see:

*  `List-table <https://docutils.sourceforge.io/docs/ref/rst/directives.html#list-table>`_
*  `CSV-table <https://docutils.sourceforge.io/docs/ref/rst/directives.html#csv-table>`_

.. commented:

   .. csv-table:: A CSV-table
   :header: "Properties", "Attribute 1", "Attribute 2", "Description"
   :widths: 3, 3, 3, 5

   "Property 1", 1.11, 1.22, "Property 1 description"
   "Property 2", 2.11, 2.22, "Property 2 description"
   "Property 3", 3.11, 3.22, "Property 3 description"
