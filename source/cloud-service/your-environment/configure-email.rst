.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Cyb3rhq can be configured to send email alerts to one or more email addresses when certain rules are triggered. Learn more about it here. 

.. _cloud_your_environment_configure_email_alerts:

SMTP configuration
==================

Cyb3rhq can be :ref:`configured to send email alerts <configuring_email_alerts>` to one or more email addresses when certain rules are triggered or for daily event reports.

This configuration requires an SMTP and you can use your own SMTP or the Cyb3rhq Cloud SMTP.

  .. note::

    If your SMTP requires authentication, you need to open a ticket through the **Help** section of your Cyb3rhq Cloud Console to configure it.

The Cyb3rhq Cloud SMTP is limited to 100 emails per hour, regardless of the ``email_maxperhour`` setting. To enable the Cyb3rhq Cloud SMTP, configure the following settings:

.. code-block::

   <global>
     . . .
     <smtp_server>cyb3rhq-smtp</smtp_server>
     <email_from>no-reply@cyb3rhq.com</email_from>
     ...
   </global>

The Cyb3rhq Cloud SMTP is now successfully configured.
