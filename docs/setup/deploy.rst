Import
======

Import and register `aioli_rdbms <https://github.com/aioli-framework/aioli-rdbms>`_ (if not imported already) and *aioli_guestbook* Packages.
Furthermore, the  `aioli_openapi <https://github.com/aioli-framework/aioli-openapi>`_ can be imported to enable OAS3 schema generation of the
Guestbook HTTP API.

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

