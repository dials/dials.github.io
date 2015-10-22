=========================================================
DIALS: Diffraction Integration for Advanced Light Sources
=========================================================
.. container:: logoheader

  .. image:: images/dials_header.png

.. This is a comment.
   This document is reStructuredText.


Introduction
============

The field of structural biology by X-ray crystallography has benefitted
greatly from technological advances in recent years. Automation, highly
brilliant beamlines at 3rd generation synchrotron sources and high
frame-rate pixel array detectors have together enabled extremely rapid
collection of most MX datasets. In tandem, large area photon-counting
detection, microfocus beams and high quality X-ray optics have brought
more challenging projects within reach. At the cutting edge of this
technological advance, the demonstration of FEL nano-crystallography
offers the tantalizing prospect of a new era of structural biology at
large facilities, with a concomitant step change in data rates and
requirements for computationally intensive processing.

There is a clear need for new software for diffraction data analysis,
designed to cope with the ever increasing volumes and rates of data
collection, and with the developments in experimental methodology, from
shutterless, fine-sliced rotation scans through to the randomly-oriented
snapshots of serial crystallography. To keep up with these technological
advances it is to be expected that this new software would utilize
techniques of parallel processing using multiple CPU and GPU machines,
facilitating not just speed, but highly accurate analysis based on a
comprehensive physical model.

Builds
======
Beamline developers and other alpha-test users are invited to download our pre-release code.

Nightly builds for various platforms may be downloaded from `LBNL`_ or `Diamond`_.

DIALS may be used as part of a data processing pipeline within `xia2-download here`_.

| Developers corner:
|   * Set up a DIALS `developer environment`_.
|   * Download the large `dials_regression`_ test suite with diffraction images (several GB).

.. _`xia2-download here`: http://www.ccp4.ac.uk/xia/
.. _`dials_regression`: developers/dials_regression.tgz
.. _`developer environment`: developers.html

Documentation
=============

`Journal and newsletter articles`_.

`DIALS documentation`_ is automatically built using Sphinx, and can be built locally alongside
a DIALS installation. This documentation is also periodically uploaded here.

Test data for DIALS is available at `ZENODO`_.

News regarding DIALS will be published at the `blog`_.

Links
=====

`Meetings and workshops`_

`Reports`_

`Source code browser`_ and `DIALS project page`_.

Mirror sites: `DIALS-East`_, `DIALS-West`_, `dials.sf.net`_.

.. _Meetings and workshops: meetings.html
.. _Journal and newsletter articles: publications.html
.. _Reports: reports.html
.. _dials.sf.net: http://dials.sf.net
.. _`DIALS-East`: http://dials.diamond.ac.uk/
.. _`DIALS-West`: http://dials.lbl.gov/
.. _`LBNL`: http://cci.lbl.gov/dials/installers/
.. _`Diamond`: http://dials.diamond.ac.uk/builds/
.. _`DIALS documentation`: doc/index.html
.. _`ZENODO`: http://zenodo.org/record/10271
.. _`DIALS project page`: https://sourceforge.net/projects/dials/
.. _`Source code browser`: http://sourceforge.net/p/dials/code/
.. _`BioStruct-X`: http://www.biostruct-x.org/
.. _`CCP4`: http://www.ccp4.ac.uk/
.. _`Diamond Light Source`: http://www.diamond.ac.uk/
.. _`Lawrence Berkeley National Laboratory`: http://www.lbl.gov/
.. _`National Institutes of Health`: http://www.nih.gov/
.. _`National Institute of General Medical Sciences`: http://www.nigms.nih.gov/
.. _`Department of Energy`: http://www.energy.gov/
.. _`blog`: http://dials-news.blogspot.co.uk/

Funding
=======

DIALS development at `Diamond Light Source`_ is supported by the `BioStruct-X`_ EU grant,
`Diamond Light Source`_, and `CCP4`_.

DIALS development at `Lawrence Berkeley National Laboratory`_ is
supported by `National Institutes of Health`_ / `National Institute of General Medical Sciences`_
grant R01-GM095887.  Work at LBNL is performed under
`Department of Energy`_ contract DE-AC02-05CH11231.
