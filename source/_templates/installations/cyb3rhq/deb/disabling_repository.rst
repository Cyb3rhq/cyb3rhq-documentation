.. Copyright (C) 2015, Cyb3rhq, Inc.

.. code-block:: console

  # sed -i "s/^deb/#deb/" /etc/apt/sources.list.d/cyb3rhq.list
  # apt-get update

Alternatively, you can set the package state to ``hold``. This action stops updates but you can still upgrade it manually using ``apt-get install``.

.. code-block:: console

  # echo "cyb3rhq-agent hold" | dpkg --set-selections

.. End of include file
