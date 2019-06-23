Install
---

.. code-block:: bash

   $ pip3 install aioli_guestbook


Configure
---

This example uses TOML format, read the `Configuration System <https://aioli.readthedocs.io/en/latest/setup/configure.html>`_ documentation for more info.

The *aioli_rdbms* dependency *Package* needs to be configured as well (if not configured already).

.. code-block:: toml

   [aioli_guestbook]
   path = "/guestbook"
   # Maximum number of visits per IP
   visits_max = 14

   [aioli_rdbms]
   type = "(mysql|postgres)"
   username = "user"
   password = "pass"
   host = "127.0.0.1"
   port = 3306
   database = "aioli"


Import
---

Import and register *aioli_guestbook* and *aioli_rdbms* (if not imported already) Packages.

.. code-block:: python

    import aioli_guestbook
    import aioli_rdbms

    import toml

    from aioli import Application

    app = Application(
        config=toml.load("config.toml"),
        packages=[
            aioli_guestbook,
            aioli_rdbms,
        ]
    )

