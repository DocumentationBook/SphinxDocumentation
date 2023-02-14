.. _concepts_docutils_schema:

Document Structure
##################

The key entity in Docutils is the tree-like document structure defined by
`DTD <https://docutils.sourceforge.io/docs/ref/docutils.dtd>`_ (document type definition). This structure called
doctree is a hierarchical acyclic tree with the following specifics:

*  Every node is an object of a ``Node`` subclass.
*  The tree root is the ``document`` node.
*  Every node has a parent, except for the root, and a list of children, which is empty for leafs.

A node can be a text block (plain or special), a title, an inline element (emphasized element and other), and other.
Every node can have the following set of attributes as defined by the DTD::

   <!--
   Attributes shared by all elements in this DTD:

   - `ids` are unique identifiers, typically assigned by the system. The NMTOKENS
     attribute type is used because XML doesn't support a multiple-ID "IDS" type.
   - `names` are identifiers assigned in the markup.
   - `dupnames` is the same as `name`, used when it's a duplicate.
   - `source` is the name of the source of this document or fragment.
   - `classes` is used to transmit individuality information forward.
   -->
   <!ENTITY % basic.atts
     " ids       %ids.type;         #IMPLIED
       names     %refnames.type;    #IMPLIED
       dupnames  %refnames.type;    #IMPLIED
       source    CDATA              #IMPLIED
       classes   %classnames.type;  #IMPLIED
       %additional.basic.atts; ">


