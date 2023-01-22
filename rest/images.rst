.. _rest_images:

Images
######

The ``image`` directive enables you to insert images on a new line or an image after another image if their total width
doesn't exceed the page width. Its argument is a path or a URL to the image that must be displayed. I can also contain
options to specify the alternate text (``alt``), width, height, scale, and alignment.

Examples of the image directives:

*  Default options::

      .. image:: path/myimage.svg

*  Specifying the width in percentage of the document line width::

      .. image:: path/myimage.svg
         :width: 60%

For more details about images, see the
`docutils <https://docutils.sourceforge.io/docs/ref/rst/directives.html#images>`_ specification.
