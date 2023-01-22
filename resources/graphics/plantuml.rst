.. _ resources_graphics_plantuml:

PlantUML
########

`PlantUML <https://plantuml.com/>`_ is tool widely used by software analytics, engineers, developers, and others
to create various types of graphic diagrams.


Setup
=====

PlantUML is a Java package that you need to install on your computer. The installation process depends on your
Operating System. You can find the most convenient way at the `PlantUML <https://plantuml.com/>`_ official site.
This package requires the Graphviz package, so you need to install it too if you didn't do it yet.
For example, on Mac, you can use Homebrew package manager::

   $ brew install graphviz
   $ brew install plantuml

The ``sphinxcontrib-plantuml`` package is available in the Github
`sphinx-contrib <https://github.com/sphinx-contrib/plantuml>`_ repository.
Use the following steps to set it up:

#. Install the ``sphinxcontrib-plantuml`` extension::

      $ pip install sphinxcontrib-plantuml

#. Add this extension to the ``conf.py`` file::

      extensions = [
          'sphinxcontrib.plantuml',
      ]

#. Try this updated by add the following simplest test directory to a reST file::

      .. uml::

         @startuml
         user -> (use PlantUML)

         note left of user
            Hello!
         end note
         @enduml

#. Build the documentation as you usually do. You will get the following graphic:

   .. uml::

      @startuml
      user -> (use PlantUML)

      note left of user
         Hello!
      end note


Diagrams
========


