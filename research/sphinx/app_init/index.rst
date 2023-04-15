.. _research_sphinx_process_app:

App Initialization
##################

.. graphviz:: phases_init.gv

The ``app`` object is the documentation build root that binds together all other objects necessary for building
the documentation:

*  ``project`` collects a set of document names.
*  ``builder`` is a builder object of the class chosen in the initial ``sphinx-build`` command
   (argument ``-b`` or ``-M``).
*  ``environment`` contains all information about the documents in the documentation tree.
*  ``registry`` is an object of class ``sphinx.registry.SphinxComponentRegistry`` that contains the app components,
   which are building blocks and tools discovered and used in the process.
*  ``events`` is an object of class ``sphinx.events.EventManager`` that emits events at some
   program checkpoints addressing them to event subscribers.
*  ``config`` is an object of class ``sphinx.config.Config`` containing all configuration parameters, those that are
   Sphinx builtin and those that are read in the ``conf.py`` file.


Process
=======

The app initialization process figures out the absolute paths of the following input and output folders:

*  ``srcdir`` contains input data.
*  ``confdir`` contains the ``conf.py`` file.
*  ``doctreedir`` stores pickled documentation tree (``doctree``).
*  ``outdir`` stores built documents.

The ``app.__init__`` method performs various validations and calls other methods as presented in this diagram
(your reading will be more comfortable if you open this diagram in a separate window):

.. uml:: app_init.uml
   :alt: Initialization phase

The initialization goes in the following order (see the numbers in the diagram):

#. Create and pre-initialize the ``app.config`` object. This object contains the list of extensions
   ``config.extensions`` collected from ``conf.py``.
#. Call the ``app.setup_extension`` for every builtin extension (``builtin_extensions``) and every extension
   in ``config.extensions`` collected in the previous step.
   The ``app.registry`` object created from the ``sphinx.registry.SphinxComponentRegistry`` class executes
   the ``load_extension`` method to import the Python module (``mod``) by the extension name ``extname``,
   find its ``setup`` method. After that, it applies this method to the ``app`` object, that is,
   calls ``setup(app)`` to get ``metadata``.
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

   .. note:: This is where you can handle the 'config-inited' event emitted
      after the ``app.config`` object is initialized.

   For more information about subscribing to events,
   see `Sphinx core events <https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx-core-events>`_.

#. Create and initialize the ``app.project`` object from the ``project.Project`` class::

      self.project = Project(self.srcdir, self.config.source_suffix)

   The initialized project will have an empty set of document names ``app.project.docnames``.

#. Call the ``app.create_builder(buildername)`` method to create the ``app.builder`` object
   and initialize this Sphinx builder. In this particular case, we consider one of Sphinx builders, which
   name is ``dirhtml``.
   The ``app.create_builder`` method calls the ``app.register.create_builder`` and passes the builder name to it.
   The builder name defines the class that is used to create the build object::

      return self.builders[name](app)

   With the builder name ``dirhtml``, the class will be ``sphinx.builders.dirhtml.DirectoryHTMLBuilder``.
   This causes consequent calls of the ``__init__`` methods defined in the ancestor classes.
   From bottom to top the ancestors are: ``sphinx.builders.html.StandaloneHTMLBuilder`` and ``sphinx.builders.Builder``.

#. Call the ``app._init_env`` method to create and initialize the ``app.env`` object of the
   ``sphinx.environment.BuildEnvironment`` class and then collect the information about source
   documents and the doctree::

      if freshenv or not os.path.exists(filename):
         self.env = BuildEnvironment(self)
         self.env.find_files(self.config, self.builder)

   The ``env.find_files`` method calls the ``project.discovery`` method to find the document source files. This method
   walks through the source folder and returns the discovered file names as a set similar to this::

       {'folder2/index', 'index', 'folder1/index'}

   This set is also assigned to the ``project.docnames`` variable.

#. Call the ``app._init_build`` method to initialize the ``app.builder`` object. The main job is done by the
   inherited ``sphinx.builders.html.StandaloneHTMLBuilder.init`` method. After this, the builder will have all
   the objects to process HTML documents one by one. For every current document, it will use: ``current_docname``,
   ``secnumbers``, templates, a list of CSS files, a list of JavaScript files, and so on.
   Finally the ``app._init_build`` method calls ``app.events.emit`` to run all handlers subscribed
   to the event called ``builder-inited``::

      self.events.emit('builder-inited')

   .. note:: This is where you can handle the event 'builder-inited' emitted after creation of the builder object
      that is available to handlers as ``app.builder``.


Initialized state
=================

The initialization phase completes with creation of the ``app`` object (class ``Sphinx``) with the other main objects:

.. uml:: structure_init.uml
   :alt: Initized state

The diagram displays incomplete lists of components.
The objects have the following specifics:

*  Some objects have a back-reference to ``app``, such as ``env.app``.
*  Some objects have direct links to each other, such as ``env.project`` and ``builder.env``.
   This helps to get necessary data directly bypassing ``app``.
*  Many object have duplicate links to some ``app`` components, such as ``env.srcdir`` and ``builder.outdir``.
   This helps to deal with these components directly instead of going through ``app``.
