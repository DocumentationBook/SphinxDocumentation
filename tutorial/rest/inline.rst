.. _rest_inline:

Inline Markup
#############

In a text block, reST provides the following typical inline markups:

.. list-table::
   :widths: 3 5 11
   :header-rows: 1

   *  -  Markup type
      -  reST example
      -  HTML
   *  -  Emphasized
      -  \*emphasized\*
      -  <em>emphasized</em>
   *  -  Cited
      -  \`citation\`
      -  <cite>citation</cite>
   *  -  Bold
      -  \*\*bold text\*\*
      -  <strong>bold text</strong>
   *  -  Inline literal
      -  \`\`inline literal\`\`
      -  | <code class="docutils literal notranslate">
         | <span class="pre">inline</span>
         | <span class="pre">literals</span>
         | </code>



This is a simple example of the marked up source::

   Text block contains *emphasized* and `citation` elements,
   **bold text**, and ``inline literals``.

After building the document, you will see the following text:

Text block contains *emphasized* and `citation` elements,
**bold text**, and ``inline literals``.
