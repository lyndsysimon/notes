========================
 Open Science Framework
========================


Task Responsibilities
=====================

This section is based on a meeting between Jeff, Josh and myself on 17 Jul 2013.

Josh will be becoming a bigger part of OSF development.

    * Responsible for incremental refactors (immediately above)
    * Integrating components developed by others in COS

        * hGrid
        * Solr search

Nan will assist me in writing and maintaining Selenium tests.

I will be responsible for deployment, testing, and managing our git workflow.

My current projects:

    1. Familiarize myself with Selenium + Sauce Labs
    1. Review code in osf-ui-tests
    1. Integrate testing into our deployment

I should also consider how unit tests would fit into the deployment workflow,
though we probably won't have them until we begin to make architectural changes
to the OSF.

Ongoing responsibilities:

    * Stay on top of bugs in the Github Issues list
    * Refactor / fix templates as I can (coordinated with Josh)

API-based design
================

Over time, we'll be moving to a more modular, API-based design. The ultimate
goal is a single-pages design, backed by a documented, public API. This should
be considered as we add features and refactor existing features.

Deployment Process
==================


- We need a canonical dataset for testing (a base state)

    - I will be responsible for the merge into master and deploy to production
        - As part of this step, email:
            - Summary of changes, and what they are anticipated to impact
            - Send to OSF dev list


OSF Dev List
============

Anyone who interacts with users should be on this list.

It is a Google group.


Current Refactor Plan
=====================

Small, incremental changes

    - examples:
        - moving settings file
        - moving cache and uploads folder
        - lowercase folder names
        - pep8 (naming conventions)
        - logic in templates needs to be pulled out
        - members needs to be broken in to pieces: "wiki","project","user", etc.

Routes should be stay consistent.
    - generate all public-facing URLs
    - parse logfiles for URLs that have been hit

We don't change collection names.