Registrar service  |Travis|_ |Codecov|_
===================================================
.. |Travis| image:: https://travis-ci.org/edx/registrar.svg?branch=master
.. _Travis: https://travis-ci.org/edx/registrar

.. |Codecov| image:: http://codecov.io/github/edx/registrar/coverage.svg?branch=master
.. _Codecov: http://codecov.io/github/edx/registrar?branch=master

This is the prototype to explore the concept of linking an edX learner user with an edX program stored in course discovery.
The prototype should prove the concepts below:

#. Make API call from this repo to LMS and Discovery through DOT JWT
   
   #. Have viable linkage table between LMS learner and here
   
   #. Have viable linkage table between Discovery Programs and here

#. Integrate with SSO module on LMS to facilitate LMS account creation

#. Explore a generic pending learner/enrollment concept

#. Provide API to external parties to retrieve the following:
  
   #. Given a program, which learners are enrolled in it

   #. Given a learner, which program, if any, is the learner enrolled in

   #. Given a learner, return the list of course the learner is enrolled in within the enrolled program

   #. An RESTful API endpoint for uploading enrollment information for a program (Pending Enrollments required)

   #. Can this act as a proxy to pull learner grades and completion data


Documentation
-------------
.. |ReadtheDocs| image:: https://readthedocs.org/projects/registrar/badge/?version=latest
.. _ReadtheDocs: http://registrar.readthedocs.io/en/latest/

`Documentation <https://registrar.readthedocs.io/en/latest/>`_ is hosted on Read the Docs. The source is hosted in this repo's `docs <https://github.com/edx/registrar/tree/master/docs>`_ directory. To contribute, please open a PR against this repo.

License
-------

The code in this repository is licensed under version 3 of the AGPL unless otherwise noted. Please see the LICENSE_ file for details.

.. _LICENSE: https://github.com/edx/registrar/blob/master/LICENSE

How To Contribute
-----------------

Contributions are welcome. Please read `How To Contribute <https://github.com/edx/edx-platform/blob/master/CONTRIBUTING.rst>`_ for details. Even though it was written with ``edx-platform`` in mind, these guidelines should be followed for Open edX code in general.

Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email security@edx.org.

Get Help
--------

Ask questions and discuss this project on `Slack <https://openedx.slack.com/messages/general/>`_ or in the `edx-code Google Group <https://groups.google.com/forum/#!forum/edx-code>`_.
