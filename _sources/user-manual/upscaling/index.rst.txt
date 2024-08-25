.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: This documentation provides a guide on upscaling your Cyb3rhq infrastructure to add new Cyb3rhq indexer and Cyb3rhq server nodes.
  
Upscaling a Cyb3rhq deployment
============================

This documentation provides a guide on upscaling your Cyb3rhq infrastructure to add new Cyb3rhq indexer or Cyb3rhq server nodes. Thus maximizing the potential of Cyb3rhq to effectively monitor and protect your growing IT infrastructure.

The Cyb3rhq platform is composed of a universal :doc:`Cyb3rhq agent </getting-started/components/cyb3rhq-agent>` and three central components; the :doc:`Cyb3rhq server </getting-started/components/cyb3rhq-server>`, the :doc:`Cyb3rhq indexer </getting-started/components/cyb3rhq-indexer>`, and the :doc:`Cyb3rhq dashboard </getting-started/components/cyb3rhq-dashboard>`.  The Cyb3rhq agent is deployed on the endpoints you want to monitor. The central components can be deployed in two ways; as a single unit on one server (all-in-one deployment) using our :ref:`quickstart install script <quickstart_installing_cyb3rhq>`, or as separate entities (distributed deployment) by following our step-by-step guide (applicable to Cyb3rhq :doc:`indexer </installation-guide/cyb3rhq-indexer/step-by-step>`, :doc:`server </installation-guide/cyb3rhq-server/step-by-step>`, and :doc:`dashboard </installation-guide/cyb3rhq-dashboard/step-by-step>`) or using the install assistant (for Cyb3rhq :doc:`indexer </installation-guide/cyb3rhq-indexer/installation-assistant>`, :doc:`server </installation-guide/cyb3rhq-indexer/installation-assistant>`, and :doc:`dashboard </installation-guide/cyb3rhq-dashboard/installation-assistant>`). Hence, the scaling strategy for your infrastructure depends on the deployment method you initially performed.

This guide covers the following:

.. toctree::
   :maxdepth: 1

   adding-indexer-node
   adding-server-node