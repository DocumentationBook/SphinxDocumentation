.. _tutorial_qa:

Quality Assurance
#################

Quality assurance is a key step in the CI and CD processes.
Sphinx provides you with some tools to use at this stage.
In this guide, you will get to know some of them and learn how to use them.


Tools
=====

*  ``sphinx.ext.doctest`` is an embedded extension for testing Sphinx syntax and examples in documents.
*  The ``linkcheck`` builder checks validity of external links.
*  The `coverage <https://www.sphinx-doc.org/en/master/usage/extensions/coverage.html>`_ builder checks if during
   the build process some documentation parts of source documents were missed. This is important for the autodoc
   process that can miss some docstrings due to the absence of some docstring parts or due to author's mistakes.
   After you execute ``make coverage``, the result will be saved in the ``_build/coverage/`` folder.
*  ``sphinxcontrib.spelling`` is an extension that checks word spelling
   based on `Enchant <https://abiword.github.io/enchant/>`_.


Spelling tool
=============

I had quite a battle of installing the required ``enchant`` and ``pychant`` packages in my conda environment.
Probably this works better if you use a pip environment.
This is how I did it on my Mac:

#. Install the ``enchant`` package using::

      $ brew install enchant

#. Install the ``pyenchant`` and ``sphinxcontrib-spelling`` packages using ``pip`` or ``conda``.
   When using the latter, specify the repository.

       pip install -y pyenchant
       pip install -y sphinxcontrib-spelling

#. Set the PYENCHANT_LIBRARY_PATH environment variable that must refer to the enchant library installed with
   the brew utility. This is the most crucial moment and it looks as follows::

      $ conda env config vars set \
        PYENCHANT_LIBRARY_PATH=/<path_to_your_home_folder>/homebrew/Cellar/enchant/2.3.3/lib/libenchant-2.2.dylib

#. Reactivate the conda environment as proposed by conda. For example, if the environment name is ``py10``, run
   this command::

      $ conda activate py10

#. Check the environment variable::

      $  conda env config vars list

#. Update the list of extensions in ``conf.py``::

      extensions.append('sphinxcontrib.spelling')

Run spell checking as follows::

   $ make spelling

You will see the results on the screen and in the ``/_build/spelling/output.txt`` file.
If you think that some of words marked as misspelled are actually spelled correctly,
add them (one per line) to the ``./spelling_wordlist.txt`` file, which the new extension creates in your project.
