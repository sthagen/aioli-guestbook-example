.. _setup-configure-docs:

Configure
=========

This example uses TOML. Check out the `Aioli Configuration System <https://aioli.readthedocs.io/en/latest/setup/configure.html>`_ documentation for more info.

*aioli.cfg*

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
