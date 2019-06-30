Import
======

Import and register *aioli_rdbms* (if not imported already) and *aioli_guestbook* Packages.

.. code-block:: python

    import aioli_guestbook
    import aioli_rdbms

    import toml

    from aioli import Application

    app = Application(
        config=toml.load("aioli.cfg"),
        packages=[
            aioli_guestbook,
            aioli_rdbms,
        ]
    )

