# -*- encoding: iso-8859-1 -*-
# Setup code, stay away
items = []
item = lambda *x: items.append(x)

# News items go here, most recent ones at top. Dates can be either
# strings or time(3) output.
#
# item("INSERT TITLE HERE",
#      (1901, 3, 1),
#      """
#      INSERT TEXT HERE
#      """)

item("New tutorial about Glade and PyGTK",
     (2004, 11, 9),
     """
     Sandino Flores (aka tigrux) has written an excellent tutorial about
     writting PyGTK applications with Glade and some libraries he wrote so now
     coding gnome python applications is easier than ever before. Check it
     out at <a href="http://primates.ximian.com/~sandino/python-glade/">http://primates.ximian.com/~sandino/python-glade/</a>.
     """)

item("PyGTK 2.4.1 is here!",
     (2004, 11, 4),
     """
     The PyGTK team is pleased to announce PyGTK 2.4.1.
     This is a bugfix release but also some new examples were added too.
     So, go
     <a href="http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.4/">download</a>
     it and give new life to your phantasmagoricial applications right now!.
     Read the whole announcement at
     <a href="http://www.daa.com.au/pipermail/pygtk/2004-November/008968.html">the mailing list</a>.
     """)


item("Pygtk 2.4.0, Gnome-Python 2.6.0 and PyOrbit 2.0.1 hit the streets",
     (2004, 10, 5),
     """
     The PyGtk team is very happy to announce the final version of
     <a href="http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.4/">PyGTK
     2.4.0</a> and other important related packages like
     <a href="http://ftp.gnome.org/pub/GNOME/sources/gnome-python/2.6/">Gnome-Python 2.6.0</a> and
     <a href="http://ftp.gnome.org/pub/GNOME/sources/pyorbit/2.0/">PyOrbit 2.0.1</a>. A lot of exciting functionality from GTK+ 2.4.0 is
     inside this new version so better applications can be developed with it.
     As always we are eager to listen your feedback!
     """)

item("PyGTK 2.4.0 rc1 (aka PyGTK 2.3.97)",
     (2004, 9, 28),
     """
     After some nasty threading issues the PyGTK team is proud to announce
     PyGTK 2.3.97 which will be 2.4.0 if everything goes fine. How will we
     know that? By intensive testing!! So please,
     <a href="http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.3/pygtk-2.3.97.tar.gz">download</a>
     it and test your fancy applications right now! Reports from applications
     with threads have a bonus added. Read the whole announce at
     <a href="http://www.daa.com.au/pipermail/pygtk/2004-September/008694.html">the mailing list</a>.
     """)

item("We got RSS!",
     (2004, 9, 8),
     """
     <a href="http://cs.annauniv.edu/~rsridhar">Sridhar R.</a>
     contributed code to the PyGTK.org website that generates an <a
     href="news.rss">RSS feed</a> of the latest news items posted. This
     code has been integrated over the weekend and is currently live.
     Please send feedback and report problems to pygtk-web at pygtk dot
     org.
     """)

item("Devhelp support added to the PyGTK Reference manual v2.4.10",
     (2004, 8, 12),
     """
     Johan Dahlin added <a
     href="http://www.imendio.com/projects/devhelp/">devhelp</a> index
     creation support to the <a
     href="http://www.pygtk.org/pygtk2reference/index.html">PyGTK
     Reference</a>. The manual and tarballs have been updated to include
     devhelp indexes. There were no other significant changes from the
     2.4.9 version. The devhelp index alone for use with the 2.4.9
     version is also available: get the <a
     href="http://www.moeraki.com/pygtkreference/pygtk2reference.devhelp.gz">gzip'd
     PyGTK Reference devhelp index</a>.
     """)

item("New versions of the PyGTK Tutorial and Reference released",
     (2004, 8, 5),
     """
     John Finlay announced new releases of his <a
     href="http://www.pygtk.org/pygtk2tutorial/index.html">PyGTK Tutorial</a>
     and <a href="http://www.pygtk.org/pygtk2reference/index.html">PyGTK
     Reference</a>. Additions include ComboBox, ComboBoxEntry, EntryCompletion,
     Expander, Clipboard, FileChooser (by Alex Roitman) and several bug fixes!
     """)

item("PyGTK 2.3.94 (unstable) released",
     (2004, 7, 21),
     """
     The PyGTK team has released PyGTK 2.3.94 today. This is a small bug fix
     release and should be stable enough to use for developing new
     applications. The official announce is <a
     href="http://www.daa.com.au/pipermail/pygtk/2004-July/008242.html">here</a>
     and you can download it from <a
     href="http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.3/pygtk-2.3.94.tar.gz">here</a>.
     We'd really appreciate testing and bug reports on this release.
     """)

item("PyGTK 2.3.93 (unstable) released",
     (2004, 7, 19),
     """
     The PyGTK team has released PyGTK 2.3.93 today. We are now in frozen state
     so no more changes are expected until 2.4.0, just bug fixes. The official
     announce is <a href="http://www.daa.com.au/pipermail/pygtk/2004-July/008199.html">here</a> and you can download it from
     <a href="http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.3/pygtk-2.3.93.tar.gz">here</a>.
     We'd really appreciate testing and bug reports on this release.
     """)

item("Article: Rapid Application Development with Python and Glade",
     (2004, 7, 19),
     """
     David Reed's <a
     href="http://www.linuxjournal.com/index.php">Linux Journal</a> article
     is available online: <a
     href="http://www.linuxjournal.com/article.php?sid=7421">Rapid
     Application Development with Python and Glade</a>.
     """)

item("Article: Developing with Gnome (in C, C++, Perl and Python)",
     (2004, 7, 16),
     """
     Elijah P. Newren submitted <a
     href="http://www.gnome.org/~newren/tutorials/developing-with-gnome/">a
     new article</a>, which describes Gnome development using four different
     languages: C, C++, Perl and Python.
     """)

item("PyGTK 0.6.12 (obsolete) released",
     (2004, 7, 12),
     """
     The PyGTK team has released the latest (and perhaps last) version off
     the 0.6 branch, PyGTK 0.6.12. This version contains a number of <a
     href="http://lists.gnome.org/archives/gnome-announce-list/2004-July/msg00029.html">small
     bugfixes and two API additions</a> that were accumulated over the past
     two years in CVS. <a
     href="ftp://ftp.gtk.org/pub/gtk/python/v1.2/">Download it from
     gtk.org</a> while it's hot.. or not!
     """)

item("New versions of the PyGTK Tutorial and Reference released",
     (2004, 7, 6),
     """
     John Finlay announced new releases of his <a
     href="http://www.pygtk.org/pygtk2tutorial/index.html">PyGTK Tutorial</a>
     and <a href="http://www.pygtk.org/pygtk2reference/index.html">PyGTK
     Reference</a>. Additions include GenericTreeModel, sorting of TreeModel
     rows, editable and activatable TreeView cells, more TreeView examples,
     updated timeout, IO and idle sections, updated drag and drop section
     updated and several bug fixes! Thanks again John.
     """)

item("PyGTK 2.3.92 (unstable) released",
     (2004, 5, 22),
     """
     The PyGTK team has released PyGTK 2.3.92 which implement most of the
     new GTK+2.4 APIs. The official announce is <a
     href="http://www.daa.com.au/pipermail/pygtk/2004-May/007644.html">here</a>
     and you can download it from <a
     href="http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.3/pygtk-2.3.92.tar.gz">here</a>.
     We'd really appreciate testing and bug reports on this release.
     """)

item("PyGTK 2.3.91 (unstable) released",
     (2004, 4, 16),
     """
     The PyGTK team has released PyGTK 2.3.91 which implement most of the
     new GTK+2.4 APIs. The official announce is <a
     href="http://www.daa.com.au/pipermail/pygtk/2004-April/007447.html">here</a>
     and you can download it from <a
     href="http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.3/pygtk-2.3.91.tar.gz">here</a>.
     We'd really appreciate testing and bug reports on this release.
     """)

item("GNOME-Python 2.0.2 (stable) released!",
     (2004, 4, 8),
     """
     We are happy to announce version 2.0.2 of GNOME Python. We have
     quite a few of bug fixes and new functions wrapped so don't wait
     until your friends try it and do it by yourself. As always you can
     find the files at <a
     href="http://ftp.gnome.org/pub/GNOME/sources/gnome-python/2.0/">http://ftp.gnome.org/pub/GNOME/sources/gnome-python/2.0/</a>.
     After a previous 2.0.1 version on the 30th of March we released
     2.0.2 just to fix a build problem with the vfs bindings.
     """)

item("PyGTK 2.2.0 (stable) released!",
     (2004, 3, 11),
     """
     After one week from the rc1 we finally have PyGTK 2.2.0. Go to the
     <a href="./downloads.html">Downloads</a> section and install this new version
     of your favourite Python graphical toolkit. As always testing and bug reports
     are very much appreciated!.
     """)

item("PyGtkSpell 0.3.1 \"Static Cling\" released!",
     (2004, 3, 8),
     """
     John (J5) Palmieri released a new version of <a
     href="http://martianrock.com/pygtkspell/">PyGtkSpell</a>, the Python
     bindings for the easy-to-use GtkSpell spell checker. GtkSpell works in
     conjunction with the GtkTextView widget to give programs spell checking
     capabilities with only a few lines of code. Download the <a
     href="http://martianrock.com/dropzone/pygtkspell-0.3.1.tar.gz">PyGtkSpell
     source tarball.</a>
     """)

item("PyGTK 2.2.0 Release Candidate 1",
     (2004, 3, 5),
     """
     The first <a href="http://www.gnome.org/~jdahlin/pygtk-2.2.0-RC1.tar.gz
     ">release candidate for PyGTK 2.2.0</a> is out. Testing and bug reports
     are very much appreciated! Lorenzo has prepared a <a
     href="http://www.sicem.biz/personal/lgs/cosas/pygtk-2-2-0-changes
     ">summary of changes</a>, and you can also check out Bonsai's <a
     href="http://cvs.gnome.org/bonsai/cvsquery.cgi?treeid=default&branch=HEAD&branchtype=match&dir=gnome-python%2Fpygtk&file=&filetype=match&who=&whotype=match&sortby=Date&hours=2&date=explicit&mindate=2003-09-02&maxdate=2004-03-05&cvsroot=%2Fcvs%2Fgnome">detailed
     checkin list</a>.
     """)

item("gnome-print bounty announced by GRAMPS team",
     (2004, 2, 20),
     """
     <a href="http://gramps.sf.net/">GRAMPS</a> is a pygtk/gnome-python based
     genealogy program. The GRAMPS team is looking for a person to step
     forward to claim the task of gnome-print integration into GRAMPS. This
     will use the GNOME print infrastructure to allow print preview and
     direct printing of reports.
     <p>
     <a href="mailto:dallingham@users.sourceforge.net">Don Allingham</a>,
     GRAMPS maintainer writes: ''We have a start on the code, but not enough
     resources to complete the task as quickly as we would like.  With the
     donations we have received, we have been able to set the bounty for this
     task at $100. While it may not be a tremendous amount, it should buy a
     few books, quite a bit of pizza, or a new disk drive.''
     <p>
     For more information and the requirements, see the 
     <a href="http://gramps.sourceforge.net/phpwiki/index.php/GnomePrintBounty">
     Gnome Print Bounty page</a> on the GRAMPS wiki.
     <p><strong>Updated 2004-03-11</strong>: Alex Roitman took up the challenge and has
     finished integration of gnome-python with GRAMPS.
     """)

item("Gnome applets tutorial",
     (2004, 2, 10),
     """
     Arturo González has written a great tutorial on building applets
     for the Gnome panel in our favourite language. Check it out in the <a
     href="articles.html">Articles</a> section. By the way, Arturo says
     ''comments and suggestions are more than welcome!''
     """)

item("New website",
     (2003, 12, 8),
     """
     We are happy to announce a new website for PyGTK. We already had
     extremely good resources like the docs, the mailing list and the FAQ
     but we needed a place to put all together. We hope that with this
     website people will find the information about PyGTK faster and better.
     """)

item("PyGTK-2.0.0 is out",
     (2003, 9, 2),
     """
     We are pleased to announce version 2.0 of the Python bindings for
     GTK. The new release is available from <a
     href="ftp://ftp.gtk.org">ftp.gtk.org</a> or <a
     href="http://ftp.gnome.org">ftp.gnome.org</a> and its mirrors: 
     <ul>
     <li><a
     href="ftp://ftp.gtk.org/pub/gtk/python/v2.0/pygtk-2.0.0.tar.gz">ftp://ftp.gtk.org/pub/gtk/python/v2.0/pygtk-2.0.0.tar.gz</a>
     <li><a href="http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.0/">http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.0/pygtk-2.0.0.tar.gz</a>
     </ul>
     """)

