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

Using with Docker Devstack
--------------------------

This can be run locally with docker.  It uses the ``devstack_default`` network.  To bring up the application container, memcache container, and DB container, do::

  make up

To bring these containers down::

  make down

License
-------

The code in this repository is licensed under version 3 of the AGPL unless otherwise noted. Please see the LICENSE_ file for details.

.. _LICENSE: https://github.com/edx/registrar/blob/master/LICENSE
