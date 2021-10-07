Deep Learning in 540 minutes
============================

The mission that this repo serves:

- 540 minutes
- 70-100 people
- get together remotely
- 2 weeks to prepare
- teach deep learning

.. Note::
   Visit `<https://deeplearning540.github.io>`_ to dive into the content.


Build this project locally
--------------------------

Prerequisites
^^^^^^^^^^^^^
Poetry
******
Please refer to https://python-poetry.org/docs/#installation for the
installation of `Poetry <https://python-poetry.org>`_.
You can verify your installation using below command:

.. code-block:: bash

    $ poetry --version


Build steps
^^^^^^^^^^^

1. Clone the repository to some folder of your choice on your local system and
   change your current directory into the root of the project.

.. code-block:: bash

    $ git clone https://github.com/deeplearning540/deeplearning540.github.io.git
    $ cd deeplearning540.github.io

2. The project's dependencies are managed with `Poetry <https://python-poetry.org>`_.
   To build the project locally run below lines of code in your terminal:

.. code-block:: bash

    $ poetry install
    $ poetry run make html

If all dependencies are properly installed you only are required to execute
the last command:

.. code-block:: bash

    $ poetry run make html

    $ # Alternative way
    $ poetry shell # This enables the environment for the current session
    $ make html

This will place the generated documentation in :code:`build/html`. Open
:code:`index.html` with the browser of your choice to see the changes you
made in action, for example:

.. code-block:: bash

    $ firefox build/html/index.html
