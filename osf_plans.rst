

API-based design

- Single API endpoint
- Our site will be a single-page design, hitting this endpoint.

Testing server
==============

- Top priority
- Stricter protocol prior to deployment

    1. Developer test on local machine
    1. Automated testing should run when pushed to production (or dev branch?)
    1. Melissa should manually test on dev server, and/or write tests to cover

- We need a canonical dataset for testing (a base state)

    - I will be responsible for the merge into master and deploy to production
        - As part of this step, email:
            - Summary of changes, and what they are anticipated to impact
            - Send to OSF dev list


OSF Dev List
============

Anyone who interacts with users should be on this list.

It is a Google group.


App Deploy Process
==================

Scrap salt for now. Use Fabric + Github config/build repo
Use a per-application build process. Fabric.

* Jeff to send Rob an email re: deployment process with or without salt.

Changes to OSF
==============

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