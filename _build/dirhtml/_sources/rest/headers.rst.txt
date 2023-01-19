.. _rest_headers:

Headers
#######

Each HTML section has its own header. The headers can be of different levels marked up in HTML as <H1>, <H2>, and so on.
In reST, the corresponding headers a marked up as described in the following sections.


Syntax
======

You can use various underline elements to markup headers. Docutils is smart enough to recognize what header level is
specified. It implies that you first mark up the first level header, then second level and so on. However in a styleguide
to you documentation, you should specify what elements you use to mark up the headers of different levels. For example,
the headers in this documentation are marked up as follows (although you won't find more than four levels in it)::

   First-Level Title
   #################

   Second-Level Title
   ==================

   Third-Level Title
   -----------------

   Forth-Level Title
   ^^^^^^^^^^^^^^^^^

   Fifth-Level Title
   *****************

   Sixth-Level Title
   '''''''''''''''''

You can extend the numbers even more by using a pair of overline and underline elements (also known in Docutils
as document titles versus section titles marked with only underline elements), for example, as proposed in
`PEP 12 <https://peps.python.org/pep-0012/#section-headings>`_::

   ============================
   First-Level Title (optional)
   ============================

   -----------------------------
   Second-Level Title (optional)
   -----------------------------

   Third-Level Title
   =================

   Fourth-Level Title
   ------------------

   Fifth-Level Title
   '''''''''''''''''


Best practice
=============

*  Use two blank lines between the last line of a section’s body and the next section heading::

      Section text contains one or more lines.
      One more line.


      One more header
      ===============

*  If a subsection heading immediately follows a section heading, a single blank line in-between is sufficient::

      Second-level header
      ===================

      Third-level header
      ------------------
