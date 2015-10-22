# wget http://biopython.org/DIST/biopython-1.64.tar.gz
# untar 
# python setup.py build
# python setup.py test
# sudo python setup.py install

from Bio import Entrez
Entrez.email="NKSauter@lbl.gov"

class bib(object):
  def __init__(self,PMIDs):
    handle = Entrez.efetch(db="pubmed",id=PMIDs, # must be a quoted string of comma-separated PMIDs
         retmode="xml")
    self.XML = Entrez.read(handle)
    self.PMIDs = PMIDs.split(",")
  def format1(self,out,supplementary_links):
    for i in xrange(len(self.XML)):
      print >>out,"""<li>"""
      possible_doi = [ idx for idx in self.XML[i]["PubmedData"]["ArticleIdList"] 
                       if idx.attributes["IdType"]=="doi" ]
      article = self.XML[i]["MedlineCitation"]["Article"]
      get_title = article["ArticleTitle"]
      get_title = get_title.strip(".")
      if len(possible_doi) > 0:
        print >>out, '''<a href="http://dx.doi.org/%s" target=article>
%s<br>
</a>'''%(possible_doi[0], 
         get_title.encode("ascii","xmlcharrefreplace"))
      authors = [ " ".join([elem["LastName"],elem["Initials"]]) 
                  for elem in article["AuthorList"] ]
      print >>out, "%s.<br>"%(", ".join(authors).encode("ascii","xmlcharrefreplace"))
      journal = article["Journal"]
      print >>out, '<i><font face="sans-serif">%s</font></i>'%(journal["ISOAbbreviation"])
      issue = journal["JournalIssue"]
      if issue.has_key("Volume"):
        print >>out, "<b>%s</b>,"%(issue["Volume"])
        print >>out, article["Pagination"]["MedlinePgn"]
      date = issue["PubDate"]
      if date.has_key("Month"):
        print >>out, "(%s %s %s)."%(date.get("Day",1), date["Month"], date["Year"])
      else:
        print >>out, "(%s)"%(date["Year"])
      print >>out, "[PMID:%s]"%self.PMIDs[i]
      possible_pmc = [ idx for idx in self.XML[i]["PubmedData"]["ArticleIdList"] 
                       if idx.attributes["IdType"]=="pmc" ]
      if len(possible_pmc) > 0:
        print >>out, '''[PMC reprint: <a href="http://ncbi.nlm.nih.gov/pmc/articles/%s/" target=pmc>%s</a>]'''%(
	  str(possible_pmc[0]), str(possible_pmc[0]) )
      if supplementary_links[i] is not None:
        print >>out, '''<a href="%s" target=reprints>(Reprint)</a>'''%(
	  supplementary_links[i] )
      print >>out,"""</li>
<P>
"""

if __name__=="__main__":
  frame = open("./publications.frame","r").read()
  tokens = frame.split("substitute1")
  pmid_dict = [
    ("25286849",None,"Multilattice"), 
    ("25242914",None,"dxtbx"),
    ("24507780","http://cci.lbl.gov/publications/download/diffuse.pdf","diffuse"),
    ("23793153",None,"cctbx"),
    ("22640868",None,"FABLE"),
    ]
  all_pmids = ",".join([a[0] for a in pmid_dict])
  new_bib_text = bib(PMIDs = all_pmids)

  xfel_pmid_dict = [
    ("26352473",None,"synuclein"),
    ("26280336",None,"Synaptotagmin"),
    ("26057680",None,"Ginn 2015b"),
    ("25781634",None,"prime"),
    ("25751308",None,"Ginn 2015a"),
    ("25723925",None,"Sauter postrefinement"),
    ("25664747",None,"amyloid peptides"),
    ("25664746",None,"Zeldin Toolkit"),
    ("25478847","http://cci.lbl.gov/publications/download/Mosaicity_wa5077.pdf","Mosaicity Paper"),
    ("25362050",None,"Goniometer XFEL"),
    ("25136092",None,"Sawaya"),
    ("24914169",None,"Phil Trans1"),
    ("24914152",None,"Phil Trans2"),
    ("25006873",None,"PSII-NatComm"),
    ("24633409",None,"Hattne"),
    ("23413188",None,"PSII-Science"),
    ("22665786",None,"PSII-firstPNAS"),
   ]
  xfel_pmids = ",".join([a[0] for a in xfel_pmid_dict])
  xfel_bib_text = bib(PMIDs = xfel_pmids)

  sr_pmid_dict = [
    ("26249347",None,"TLS diffuse"),
    ("25453071",None,"Diffuse MD"),
    ("25484844","http://cci.lbl.gov/publications/download/GMCA_dataprocessing_JAC.pdf","JBluIce"),
    ]
  sr_pmids = ",".join([a[0] for a in sr_pmid_dict])
  sr_bib_text = bib(PMIDs = sr_pmids)

  newfile = open("./publications.html","w")
  newfile.write(tokens[0])
  new_bib_text.format1(newfile,[a[1] for a in pmid_dict])
  newfile.write(tokens[1])
  xfel_bib_text.format1(newfile,[a[1] for a in xfel_pmid_dict])
  newfile.write(tokens[2])
  sr_bib_text.format1(newfile,[a[1] for a in sr_pmid_dict])
  newfile.write(tokens[3])
