.. _tutorial_ui:

User Interface Customization
############################

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

