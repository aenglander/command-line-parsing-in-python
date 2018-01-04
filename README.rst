Command Line Parsing in Python
==============================

This is an example project for showing argument parsing with argparse_, cliff_, and click_.

Installation
------------

Install the requirements and binaries using `Setup Tools`_. A development install is suggested to allow you to
manipulate the source and have the binaries react to the changes.

.. code-block:: bash

    python setup.py develop

Running the Examples
--------------------

The example binaries will have ben installed to the local Python binary path. As such, they should be in the current
path for your shell and can be executed without the path. If they are not in the current path for your shell, you
must prepend the commands with the same path as your python executable.

click_ Example:

.. code-block:: bash

    click-example


cliff_ Example:

.. code-block:: bash

    cliff-example help


argparse_ Hello Example:

.. code-block:: bash

    argparse-hello-example


argparse_ Goodbye Example:

.. code-block:: bash

    argparse-goodbye-example


.. _argparse: https://docs.python.org/3/library/argparse.html#module-argparse
.. _click: http://click.pocoo.org/6/
.. _cliff: https://docs.openstack.org/cliff/latest/
.. _Setup Tools: https://setuptools.readthedocs.io/en/latest/
