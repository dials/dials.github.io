#!/bin/bash

# Instruction for compiling front page from index.rst using a stylesheet
# Depends on: docutils (http://docutils.sourceforge.net/)

# find rst2html
if command -v rst2html.py > /dev/null 2>&1; then
    RSTCMD=rst2html.py
elif command -v rst2html > /dev/null 2>&1; then
    RSTCMD=rst2html
else
 echo "Please install Docutils"
    exit 1
fi

# compile
for file in *.rst
do
$RSTCMD --stylesheet-path=dials.css $file > ${file/.rst/.html}
sed -i 's!</head>!<link href="images/dials_icon.png" type="image/x-icon" rel="shortcut icon" />\n</head>!' ${file/.rst/.html}
done

BIOPYEXE=python
if [ -e /usr/local_cci/bin/python ]; then
  BIOPYEXE=/usr/local_cci/bin/python
fi
if $BIOPYEXE -c "from Bio import Entrez" > /dev/null 2>&1; then
   echo "OK Biopython"
   $BIOPYEXE generate_pubs.py
else
   echo "Please install Biopython"
fi

if [ -d "developers" ]; then
  # pass
  echo "developers directory exists"
else
  mkdir developers
fi

if [ -f "developers/dials_regression.tgz" ]; then
  # pass
  echo "dials_regression tarball exists"
else
  # first time, just get it
  cd developers
  curl http://dials.lbl.gov/developers/dials_regression.tgz > dials_regression.tgz
fi

