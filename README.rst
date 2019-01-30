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


How Authentication Works
------------------------

Authentication from the Registrar service against LMS or Discovery
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Create a registrar_worker user on LMS.

#. Using the worker user above, setup a Django Oauth Toolkit (DOT) application for Registrar service on LMS. See examples at http://localhost:18000/admin/oauth2_provider/application/

#. Store the client_key and client_secret created from step above in Registrar service settings

#. When making API calls into LMS or Discovery service within Registrar, leverage the edx-rest-api-client library https://github.com/edx/edx-rest-api-client/blob/master/edx_rest_api_client/client.py#L88 by providing the client_key and client_secret above


Authentication from External system against Registrar API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Configure the registrar service with the proper value for JWT token authentication. This should be automatically done using the configuration playbook at https://github.com/edx/configuration/blob/master/playbooks/roles/edx_django_service/defaults/main.yml#L158

#. Create a new worker user for the school's system on LMS

#. Using the worker user above, setup a Django Oauth Toolkit (DOT) application on LMS. This is done at http://localhost:18000/admin/oauth2_provider/application/

#. Send the school their client_key and client_secret created from the step above

#. The school's system need to use the client_key and client_secret above to get auth token from LMS, then use the auth token for API calls against registrar service


License
-------

The code in this repository is licensed under version 3 of the AGPL unless otherwise noted. Please see the LICENSE_ file for details.

.. _LICENSE: https://github.com/edx/registrar/blob/master/LICENSE
