============
 SciPy 2103
============
:dates: June 24-29 2013

Links
=====

`GraphTerm <https://github.com/mitotic/graphterm>`_
---------------------------------------------------

:Presenter: `Ramalingam Saravanan <http://github.com/mitotic/>`_
A graphical terminal replacement, built to be compatible with xterm.

`Dexy <http://www.dexy.it/>`_
-----------------------------

:Presenter: `Ana Nelson <http://ananelson.com/>`_

`Presentation <https://github.com/ananelson/talks/tree/master/2013/scipy>`__

SIDUS
-----

Run a given OS identically on mutliple workstations - including cloudy stuff.

Term: COMOD (_C_ompute _O_n _M_y _O_wn _D_evice)

The OS is stored remotely - but local resources are used for computation

Project Ideas
=============

* Clone of `nbViewer <nbviewer.ipython.org>`_, but that outputs reveal-js slideshows.
    * Just roll this functionality into nbViewer? It's on Github...


IP[y]thon
=========

Misc. Notes
-----------

Worksheets are going to be going away at some point.

Notebooks > Reveal.js
---------------------

`Example Presentation <http://damianavila.github.io/scipy2013_talks/index.html>`
`source <https://github.com/damianavila/scipy2013_talks/tree/gh-pages>`_

Primary conversion mechanism is through nbconvert.

Themes (and presumably other options) are exposed via URL params.

    Example: ``http://<IPython server>/<notebook>/?theme=sky``

Reproducibility
===============

Workflow
--------

:Presenter: Trevor Bekolay
:Github: https://github.com/tbekolay
:Google Plus: https://plus.google.com/102042862862925800695/

Recommends keeping a narrative on how to reproduce in a README.

Decouple analysis from meta-analysis, so that plots with results from multiple
analyses are composited in a single, documented step.

Recommends run.py

- Seems to be a home-rolled build system, in Python
- Use CLI args to toggle variables
- Recommends docopt! :)

Recommends trying to release results of analysis if the dataset cannot be open.
