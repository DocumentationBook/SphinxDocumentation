.. _tutorial_ui:

User Interface Customization
############################

Sphinx enables you to customize the appearance of documentation in various ways:

*  Choosing a theme.
*  Customizing the chosen theme.
*  Developing your own theme.
*  Customization via CSS.
*  Customization via JavaScript.


Adding announcement
===================

Sometimes you may need to add an announcement to every documentation page.
Sphinx provides you with two convenient configuration options to set in the ``conf.py`` file:

*  ``rst_prolog`` is a string to be added to the beginning of every ``reST`` file during compilation.
*  ``rst_epilog`` is a string to be added to the end of every ``reST`` file.

.. note:: You won't see those elements in actual ``reST`` files, because they are only added at build time.

For example, to announce that the documentation is in its draft version, use this prolog::

   rst_prolog = """
   .. warning:: This draft documentation is under development.
   """


Adding custom CSS
=================

#. Create a custom CSS. Usually it is placed in the ``_static/css/`` folder.
#. Ensure the ``_static/`` folder is specified in the ``conf.py`` file::

      html_static_path = ['_static']

#. If the CSS file name is ``custom.css``, then add the following statement to the ``conf.py`` file::

      html_css_files = [
          'css/custom.css',
      ]


Examples
========

Adding a border around any image::

   img {
      border: 1px solid #e1e4e5;
   }

Override the default Graphviz (class ``graphviz``) configuration of the image borders::

   img.graphviz {
       border: 1px solid #e1e4e5;
   }

