=================
ReST Instructions
=================

reStructuredText (reST) is a legible plain text format from which documents such as
web pages may be generated, using the Python package docutils_. Writing the DIALS
web page using reST is much less annoying than hacking HTML directly. A primer for
the use of reST may be found `here`__.

.. _docutils: http://docutils.sourceforge.net/
.. __: http://docutils.sourceforge.net/docs/user/rst/quickref.html

Once you have installed docutils, basic HTML compilation of a reST source file can
be achieved using the frontend script rst2html::

    rst2html foo.rst > foo.html

DIALS webpage
-------------

Edit ``index.rst`` or sources for other pages linked from this. Edit
``dials.css`` to change the style sheet. The web page can be compiled, if
you have ``rst2html`` installed by running ``compile.sh``. 

Once the pages have been updated and committed back to the repository they
can be made live by running a script using the Sourceforge shell service.
The easiest way to do this is to add your sourceforge username information
to the script ``update.sh`` then run it.

More complex operations can be performed using the Sourceforge interactive
shell. There are some instructions on how to access that service `here`__.

.. __: https://sourceforge.net/p/forge/documentation/Shell%20Service/#interactive-shell-service

Briefly, that requires you enter the following command, substituting your
sourceforge username for USER::

  ssh -t USER,dials@shell.sourceforge.net create

.. _website: http://dials.sourceforge.net/

