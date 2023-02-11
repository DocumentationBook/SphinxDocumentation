.. _rest_links:

Hyperlinks
##########

You can use different ways to reference a user to various documents and their parts. Sphinx converts all types of
references to the HTML `href` attribute inside an <a> element, for example:

*  An external reference (a link to a document on another web site)::

      <a class="reference external" href="https://www.sphinx-doc.org/en/master/">Sphinx</a>

*  An internal reference (a link to a document within this documentation set)::

      <a class="reference internal" href="blocks/#rest-blocks"><span class="std std-ref">Text Blocks</span></a>


External hyperlinks
===================

When referring to an external site, you must provide the full URL to the respective document. You can use the markup
rules from the Docutils specification or a Sphinx extension. The former rule provides the following syntax::

   `label <URL>`_

This construction contains the following elements:

*  A pair of back quotes.
*  Underscore at the end.
*  A label that the user will see in the text.
*  A full URL to the external document or its part.

.. note:: The label and URL must be separated by a space.

An example::

   `Sphinx <https://www.sphinx-doc.org/en/master/>`_

To check the validity of all external links, use the
`CheckExternalLinksBuilder <https://www.sphinx-doc.org/en/master/usage/builders/index.html#sphinx.builders.linkcheck.CheckExternalLinksBuilder>`_
builder::

   $ make linkcheck


Internal hyperlinks
===================

In an HTML document (a page), a link can lead to a resource inside this document or inside another document.


Links to headers
----------------

The simplest way to refer to a section is using its header with an underscore sign appended to it. For example, if
the header is "Internal hyperlinks", you can refer to it as::

   Internal hyperlinks_

.. note:: This method is applicable only within a document and prone to header changes.


Links to hyperlink targets
--------------------------

The most universal way of creating internal links within the documentation set is using hyperlink targets. A target
looks as follows::

   .. _target_name:

This construction is left-aligned and consists of the following elements:

*  two dots (``..``)
*  followed by a space
*  followed by an underscore ``_``
*  followed by the target name ("target_name" in the example)
*  ended with a column ``:``

A hyperlink target can be used as follows:

*  Before a section header, for example::

      .. _target_name:

      Section header
      --------------

   In the HTML code, this will add one more ID to the section header as in this example (an underscore is replaced with
   a hyphen)::

      <section id="section-header">
         <span id="target-name"></span><h3>Section header<a class="headerlink" href="#section-header" title="Permalink to this heading">¶</a></h3>
         <p>Section text Section text Section text Section text Section text Section text Section text
      sdfasdfsdf</p>
      </section>

*  Before a hypertext link whether internal or external, for example::

      .. _Python web site: https://www.python.org/

.. note:: A hyperlink target must be unique with the whole documentation set (which is also known as the book or
   the documentation tree). This enables you to refer from any document to any other document within the same
   documentation tree.

To reference a resource marked with a hyperlink target, use the ``:ref:`` role following this syntax::

   :ref:`label <target name>`

This is a typical syntax for a role that uses the following elements:

*  "target name" is the name that you assigned to the respective hyperlink target.
*  "label" is the text that the document reader will see. This is an optional element.
   If you omit it when referring to a target placed before a section header, that header will be displayed in the text.
   This might be convenient, because if you change the header, the label will be changed automatically without loosing
   the link.
