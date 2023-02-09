.. _research_sphinx_process_app:

App Initialization
##################

.. graphviz:: phases_init.gv

The ``app`` object is the documentation build root that binds together all other objects necessary for building
the documentation:

*  ``project``
*  ``builder``
*  ``environment``
*  ``registry`` is an object of class ``sphinx.registry.SphinxComponentRegistry`` that contains the app components,
   which are building blocks and tools discovered and used in the process.
*  ``events`` is an object of class ``sphinx.events.EventManager`` that emits events at some
   program checkpoints addressing to event subscribers.
*  ``config`` is an object of class ``sphinx.config.Config`` containing all configuration parameters, those that are
   Sphinx builtin and those that are read in the ``conf.py`` file.


Process
=======

The app initialization process figures out the absolute paths of the following input and output folders:

*  ``srcdir`` containing input data
*  ``confdir`` containing the ``conf.py`` file
*  ``doctreedir`` for storing pickled documentation tree (``doctree``)
*  ``outdir`` for storing build documents

The ``app.__init__`` method performs various validations and calls as presented in this diagram:

.. uml:: app_init.uml

The initialization goes in the following order (see the numbers in the diagram):

#. Create and pre-initialize the ``app.config`` object. After this, it contains the list of extensions
   ``config.extensions`` collected from ``conf.py``.
#. Call the ``app.setup_extension`` for every builtin extension (``builtin_extensions``) and every extension
   in ``config.extensions`` collected in the previous step.
   The ``app.registry`` object created from the ``sphinx.registry.SphinxComponentRegistry`` class executes
   the ``load_extension`` method to import the Python module (``mod``) by the extension name ``extname``,
   find its ``setup`` method, and apply this method to the ``app`` object, that is,
   call ``setup(app)`` to get ``metadata``.
   Finally, the  ``load_extension`` method adds the extension to the ``app.extensions`` dictionary::

      app.extensions[extname] = Extension(extname, mod, **metadata)

#. Call the ``app.preload_builder`` method to initiate the Sphinx builder specified by the ``-b`` argument
   in the command line.
   This starts a chain of calls: ``app.registry.preload_builder`` and ``app.registry.load_extension``
   (considered in the previous step).
   The latter adds the builder to the ``app.extensions`` dictionary.
#. Call the ``app.config.init_values`` to collect all configuration parameters from ``conf.py``.
#. Call the ``app.events.emit`` method to run all handlers subscribed to the event called ``config-inited``::

      self.events.emit('config-inited', self.config)

   .. note:: This is where you can handle the event emitted after the ``app.config`` object is initialized.

   For more information about subscribing to events,
   see `Sphinx core events <https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx-core-events>`_.

#. Create and initialize the ``app.project`` object from the ``project.Project`` class::

      self.project = Project(self.srcdir, self.config.source_suffix)

   The initialized project will have an empty set of document names ``app.project.docnames``.

#. Call the ``app.create_builder(buildername)`` method to create the ``app.builder`` object
   from the and initialize the Sphinx builder. In this particular case, we consider one of Sphinx builders, which
   name is ``dirhtml``
   The ``app.create_builder`` method calls the ``app.register.create_builder`` and passes the builder name to it.
   The builder name defines the class that is used to create the build object::

      return self.builders[name](app)

   With the builder name ``dirhtml``, the class will be ``sphinx.builders.dirhtml.DirectoryHTMLBuilder``.
   This causes consequent calls of the ``__init__`` methods in the ancestor classes.
   From bottom to top the ancestors are: ``sphinx.builders.html.StandaloneHTMLBuilder`` and ``sphinx.builders.Builder``.

#. Call the ``app._init_env`` method to create and initialize the ``app.env`` object of the
   ``sphinx.environment.BuildEnvironment`` class. It will collect all information about documents and the doctree.
#. Call the ``app._init_build`` method to initialize the ``app.build`` object. The main job is done the
   inherited ``sphinx.builders.html.StandaloneHTMLBuilder.init`` method. After this, the builder will have all
   the objects to process HTML documents one by one. For every current document, it will use: ``current_docname``,
   ``secnumbers``, templates, a list of CSS files, a list of Javascript files, and so on.
   Finally the ``app._init_build`` method calls ``app.events.emit`` to run all handlers subscribed
   to the event called ``builder-inited``::

      self.events.emit('builder-inited')

   .. note:: This is where you can handle the event emitted after the builder object is
      created and available as ``app.builder``.

Project state
=============

The initialization phase completes with creation of the ``app`` object (class ``Sphinx``) with the other main objects:

.. uml:: structure_init.uml

The diagram displays incomplete lists of components.
Some objects have a back-reference to ``app``, such as ``env.app``, as well as links to each other,
such as ``env.project`` and ``builder.env``.

