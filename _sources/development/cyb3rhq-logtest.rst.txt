.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
  :description: The Cyb3rhq-Logtest solution is distributed by different components of the Cyb3rhq environment: core logtest, cyb3rhq RESTful API, and cyb3rhq-logtest tool. 
  
.. _dev-cyb3rhq-logtest:


Cyb3rhq-Logtest
=============

The Cyb3rhq-Logtest solution is distributed by different components of the Cyb3rhq environment:

**Core Logtest**

    The logtest core is part of the :ref:`cyb3rhq-analysisd <cyb3rhq-analysisd>`.

**Cyb3rhq RESTful API**

    Provides Core Logtest remote interface to test rules and decoders.

**cyb3rhq-logtest tool**

     Cyb3rhq-Logtest replacement for ossec-logtest tool.


Cyb3rhq API and :ref:`cyb3rhq-logtest tool <cyb3rhq-logtest>` connect to the cyb3rhq-analysisd session manager, this acts as a
sandbox with the rules engine, allowing to isolate different users with their own rules and decoders.
The below show image illustrations how the user logs test flow through the Cyb3rhq environment.

.. thumbnail:: ../images/development/logtest-flow.png
  :title: Cyb3rhq Logtest
  :align: center
  :width: 100%



Sessions
--------

Cyb3rhq-Logtest is based on the use of isolated sessions, identified with a “token”. Each session stores its own history
of events, rules and decoders loaded. When the log evaluation is requested for the first time, the session manager
creates a new session, processing and returning the result along with the alphanumeric token as identification
of the new session.

Idle session collector
^^^^^^^^^^^^^^^^^^^^^^

The idle session collector, runs every ``session_timeout`` seconds. This parameter is defined in the
:ref:`rule_test <reference_ossec_rule_test>` section of the :ref:`ossec.conf <reference_ossec_conf>` file.
Every time the collector starts, it searches for sessions that have been idle longer than the time specified in
``session_timeout`` to close them.

The following illustration shows how the collector runs on T0, T1, T2 ... At the moment the session generates its
last request, between T0 and T1, its timeout is between T1 and T2, then on T2 the collector closes the session.

.. thumbnail:: ../images/manual/cyb3rhq-logtest/logtest-session-collector.png
  :title: Idle session collector
  :align: center
  :width: 100%



Session lifetime
^^^^^^^^^^^^^^^^

Sessions have a default expiration time of 15 minutes. When a session remains idle with no log processing requests
during that period, the idle session collector closes the session. Requests with an expired session token are
also processed, generate a new session token and notify the user.
