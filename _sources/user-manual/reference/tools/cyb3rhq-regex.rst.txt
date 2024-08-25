.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: Learn more about the cyb3rhq-regex tool in this section of the Cyb3rhq documentation.

.. _cyb3rhq-regex:

cyb3rhq-regex
===========

The cyb3rhq-regex program is used to validate a regex expression.

The pattern should be enclosed in single quotes to help prevent any unintended interactions with the shell.

The syntax for cyb3rhq-regex is as follows:

``/var/ossec/bin/cyb3rhq-regex '<pattern>'``

It then reads strings from stdin and outputs matches to stdout.

``+OSRegex_Execute`` and ``+OS_Regex`` are displayed if a match is successful.
