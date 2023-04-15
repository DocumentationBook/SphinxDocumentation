.. _ tutorial_events:

Event Management
################

At certain points, Sphinx emits predefined events that your custom script can subscribe to. You can also
create an extension that emits events.


Event handlers
==============

A program that subscribes to an event is activated by Sphinx when it emits the event. The following examples illustrate
how you can create your own event handler.


Reading initial configuration (detailed)
----------------------------------------

During :ref:`research_sphinx_process_app`, the ``app`` object emits the 'config-inited' event as defined in the
``sphinx/application.py`` file::

   self.events.emit('config-inited', self.config)

By the moment of issuing the event, the ``app`` object has collected the initial configuration from the ``conf.py``
file and is now sharing this data with those handlers that are subscribed to the 'config-inited' event.

The easiest way to read the configuration is to add a handler to the ``conf.py`` file, because Sphinx executes this
file before it emits any events. Creating a handler consists of the following steps:

#. Find out the handler signature, that is, a set of its parameters. Follow these rules:

   *  The first parameter is the ``app`` object itself.
   *  The rest of the parameters are listed in the ``events.emit`` call shown earlier.
      In this case, there is one parameter, which is ``self.config``.

#. Using the found signature, start the handler definition as a function::

      def config_inited_read_handler(app, config):
         print("\nMy handler is alive\n")

   The naming rule is arbitrary. In this example, it is rather obvious - this is a *handler* that
   *reads* the data received from the *config_inited* event notification.

#. Subscribe the handler to the 'config-inited' event. Sphinx provides the ``app.connect`` method for this.
   It must be used inside the ``setup(app)`` function::

      def setup(app):
          app.connect('config-inited', config_inited_read_handler)

#. To verify that your handler works in its simplest form, run the build process in the command line::

      $ sphinx-build -b dirhtml "." "_build"

   Make sure the print function inside the handler prints its text.

#. Define the handler body. To read data, you need to know its structure.
   In the next build run, you can just print the config object as is::

      print(f"config: {config}")

   You will get information about the ``config`` object similar to this::

      config: <sphinx.config.Config object at 0x7f944560ff10>

   From here, you understand that in order to read the object properties,
   you need to know the ``sphinx.config.Config`` structure.
   You will find it in the ``sphinx/config.py`` file. Well, but which of its properties contain the configuration
   parameters collected at this moment? To answer this question, look at the statement that starts collecting this data
   before the notification is issued.
   This is ``self.config.init_values()`` in the ``sphinx.application.py`` file.
   Look at the ``init_values()`` definition in the ``sphinx.config.Config`` class.
   You will notice that it collects initial values in the ``_raw_config`` dictionary.
   To print the contents of this dictionary, add the following line to the handler::

      [print(f"{key}: {val}") for key, val in config._raw_config.items()]

#. You can add more statements to the handler, so that its final definition can look like in this example::

      def config_inited_read_handler(app, config):
          print('\nConfiguration after reading the conf.py file:')
          print(f"app.config: {app.config}\n")
          print(f"config: {config}\n")
          [print(f"{key}: {val}") for key, val in config._raw_config.items()]

   .. note:: The ``app.config`` and ``config`` arguments represent the same object as you will see in the print out.

#. To test the handler, run the build process again. This time, it prints out a lot of configuration options.

#. Now, that you have verified that the handler works as expected,
   select only those configuration properties that you need.
   The print statement might look similar to this::

      [print(f"\n{key}: {config._raw_config[key]}") for key in ('project', 'author', 'copyright')]

   The printed text contains the requested properties, for example::

      project: Detailed Sphinx
      author: Albert Bagdasarian
      copyright: 2023, Albert Bagdasarian


Additional resources
====================

*  `Sphinx core events <https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx-core-events>`_
*  `Sphinx connect <https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx.connect>`_
