.. _concepts_sphinx_templates:

Theme Templates
###############


Sidebar
=======

The sidebar consists of several templates. Some of them are in the theme and added automatically:

*  ``globaltoc.html`` defines a table of contents for the whole documentation set.
*  ``localtoc.html`` is a table of contents for the current document.
*  ``relations.html`` contains links to the previous and the next documents.
*  ``sourcelink.html`` is a link to the source of the current document (reST file)
   if enabled by the ``html_show_sourcelink`` property.
*  ``searchbox.html`` defines a “quick search” box.

You can define a list of templates explicitly with the ``html_sidebars`` dictionary.
In this dictionary, a key is a glob-style pattern of document names and a value is a list of template files.

Example::

   html_sidebars = {
      '**': ['globaltoc.html', 'sourcelink.html', 'searchbox.html'],
      'using/windows': ['windowssidebar.html', 'searchbox.html'],
   }

.. note:: This property has no effect if the chosen theme does not possess a sidebar,
   for example, the built-in ``scrolls`` and ``haiku`` themes.
