# -*- encoding: utf-8
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
#      """,
#      "INSERT AUTHOR HERE")

# http://news.gmane.org/gmane.comp.gnome.gtk%2B.python/
item("New article - Building an application with PyGTK and Glade",
     (2006, 6, 3), """<a
     href="http://www.learningpython.com/2006/05/30/building-an-application-with-pygtk-and-glade/">
     This new article</a> by Mark Mruss explains how to build a simple application using glade
     and PyGTK, and expands on the basics explained in the previous <a
     href="http://www.learningpython.com/2006/05/07/creating-a-gui-using-pygtk-and-glade/">
     Creating a GUI using PyGTK and Glade</a> article.
     """, 'Rafael Villar Burke')

item("New article - Creating a GUI using PyGTK and Glade",
     (2006, 5, 19), """<a
     href="http://www.learningpython.com/2006/05/07/creating-a-gui-using-pygtk-and-glade/">
     This article</a> by Mark Mruss explains how to start using glade
     to build your PyGTK application interfaces. This is a perfect start for beginners
     who want to enjoy the power of glade.
     """, 'Rafael Villar Burke')

item("Gazpacho 0.6.6 released",
     (2006, 5, 3),
     """
     After more than 3 months and 30 bugzilla reports, closed Gazpacho 0.6.6
     has finally been released. This releases is the first one that takes
     advantages of kiwi features and it provides better defaults for
     common widgets, multiple selection support and it can now open up
     compressed files (gzip and bzip2).<br>
     <small><a href="http://article.gmane.org/gmane.comp.gnome.gtk%2B.python/8119">Read the complete release announcement</a></small>.""",
     "Johan Dahlin")

item("Kiwi 1.9.8 released",
     (2006, 4, 25),
     """
     New features in this release are improved distribution support,
     a replacement for distutils.setup() which makes it easier to distribute
     graphical and internationalized python applications. Included are also
     improvements and bugfixes for ObjectList, KiwiEntry masks and
     threading fixes for the Kiwi UI Test.<br>
     <small><a href="http://article.gmane.org/gmane.comp.gnome.gtk%2B.python/8081">Read the complete release announcement</a></small>.""",
     "Johan Dahlin")

item("PyGTK 2.8.6 released",
     (2006, 4, 12),
     """
     PyGTK 2.8.6 is a bug fix only release. An important leak was fixed by Michael Smith, so
     if you had issues with leaky enums and flags, then this release is for you.
     It can be fetched
     <a href="http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.8/pygtk-2.8.6.tar.gz">here</a>.
     Check out <a href="http://article.gmane.org/gmane.comp.gnome.gtk%2B.python/8028">the release announcement</a> or, for a complete list of changes, read <a href="http://live.gnome.org/PyGTK/WhatsNew28">this page</a> at the wiki.""",
     "Johan Dahlin")

item("PyGTK 2.9.0 released",
     (2006, 3, 30),
     """
     PyGTK 2.9.0 is the first release in the 2.9.x series. It's unstable, so
     it should be used with caution. Lot's of new apis were added,
     It can be fetched from:
     <a href="http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.9/pygtk-2.9.0.tar.gz">here</a>.
     Check out <a href="http://article.gmane.org/gmane.comp.gnome.gtk%2B.python/7973">the release announcement</a> or, for a complete list of changes, read <a href="http://live.gnome.org/PyGTK/WhatsNew210">this page</a> at the wiki.""",
     "Johan Dahlin")

item("PyGTK 2.8.5 released",
     (2006, 3, 30),
     """
     PyGTK 2.8.5 contains only a small amount of bug fixes. The main feature is
     that it can be built against pygobject, so it's suitable for inclusing in
     GNOME 2.14. It can be fetched
     <a href="http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.8/pygtk-2.8.5.tar.gz">here</a>.
     Check out <a href="http://article.gmane.org/gmane.comp.gnome.gtk%2B.python/7917">the release announcement</a> or, for a complete list of changes, read <a href="http://live.gnome.org/PyGTK/WhatsNew28">this page</a> at the wiki.""",
     "Johan Dahlin")

item("New article - Writing a Widget Using Cairo and PyGTK 2.8, Part2",
     (2006, 02, 27), """Continue to learn how to write pygtk widgets using the
     new Cairo API.
     <a href="./articles/cairo-pygtk-widgets/cairo-pygtk-widgets2.htm">
     This article</a> is a translation of Davyd Madeley's
     <a href="http://gnomejournal.org/article/36/writing-a-widget-using-cairo-and-gtk28-part-2">
     Writing a Widget Using Cairo and GTK+2.8, Part 2</a> article using pygtk
     concepts and idioms. It has been cooked for you by Lawrence Oluyede and
     its firt part is reachable
     <a href="./articles/cairo-pygtk-widgets/cairo-pygtk-widgets.htm">here</a>.
     """, 'Rafael Villar Burke')

item("GnomePythonDesktop 2.13.3 and GnomePythonExtras 2.13.3 released",
     (2006, 1, 24),
     """
     <a href="http://ftp.gnome.org/pub/GNOME/sources/gnome-python-desktop/2.13/">GnomePythonDesktop</a>
     provides python interfacing modules for some GNOME
     libraries part of the GNOME Desktop (gnomeapplet,
     gnomeprint, gnomeprint.ui, gtksourceview, wnck, totem.plparser,
     gtop, nautilusburn, mediaprofiles, metacity).
     
     <a href="http://ftp.gnome.org/pub/GNOME/sources/gnome-python-extras/2.13/">GnomePythonExtras</a>
     provides python interfacing modules for some GNOME
     libraries not part of the Developer or Desktop platforms (gtkhtml2,
     egg.trayicon, egg.recent, gtkspell, gtkmozembed, gdl, gda, gksu, gksu.ui).
     """,
     'Rafael Villar Burke')

item("New article - C&oacute;mo hacer widgets con Pygtk y Cairo 2.8",
     (2006, 1, 23),
     """This new article expands on previous articles on
     how to write pygtk widgets using the new avaliable Cairo API.
     <a href="./articles/cairo-pygtk-widget-signals-es/cairo-pygtk-widget-signals.html">
     The article</a> has been written (in spanish) by Alberto Ruiz.
     """,
     'Rafael Villar Burke')

item("PyGTK 2.8.4 released",
     (2006, 1, 11),
     """
     PyGTK 2.8.4 contains only a small amount of bug fixes. The main feature is
     that it can be built against pygobject, so it's suitable for inclusing in
     GNOME 2.14. It can be fetched 
     <a href="http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.8/pygtk-2.8.4.tar.gz">here</a>.
     Check out <a href="http://article.gmane.org/gmane.comp.gnome.gtk%2B.python/7525">the release announcement</a> or, for a complete list of changes, read <a href="http://live.gnome.org/PyGTK/WhatsNew28">this page</a> at the wiki.""",
     "Johan Dahlin")

item("PyGObject 2.9.0 released",
     (2006, 1, 9),
     """2.9.0 marks the first release of PyGObject, the python bindings for GObject. It has just been split off from PyGTK and is now a separate package. Fetch it  <a href="http://ftp.gnome.org/pub/GNOME/sources/pygobject/2.9/pygobject-2.9.0.tar.gz">here</a>.
     Check out <a href="http://mail.gnome.org/archives/gnome-announce-list/2006-January/msg00023.html">the release announcement</a>.""",
     "Johan Dahlin")

item("New reference docs - GnomeVFS",
     (2006, 1, 02), """Thanks to the hard work of David Trowbridge,
     <a href="pygnomevfs/index.html">documentation</a> of the gnomevfs python module (from GnomePython)
     has started.  It is not complete yet, however, any help is appreciated.""", 'Gustavo Carneiro')

item("New article - Writing a Widget Using Cairo and PyGTK 2.8",
     (2005, 12, 05), """Learn how to write pygtk widgets using the
     new Cairo API.
     <a href="./articles/cairo-pygtk-widgets/cairo-pygtk-widgets.htm">
     The article</a> translates Davyd Madeley's
     <a href="http://gnomejournal.org/article/34/writing-a-widget-using-cairo-and-gtk28">
     Writing a Widget Using Cairo and GTK+2.8</a> into pygtk concepts
     and idioms. The article has been cooked by Lawrence Oluyede.
     """, 'Rafael Villar Burke')

item("PyGTK 2.8.2 released",
     (2005, 10, 4),
     """
     2.8.2 contains only a small bugfix related to GIOChannel, you can find it
     <a href="http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.8/pygtk-2.8.2.tar.gz">here</a>.
     Check out <a href="http://article.gmane.org/gmane.comp.gnome.gtk%2B.python/7097">the release announcement</a> or, for a complete list of changes, read <a href="http://live.gnome.org/PyGTK/WhatsNew28">this page</a> at the wiki.""",
     "Johan Dahlin")

item("PyGTK 2.8.1 released",
     (2005, 10, 4),
     """
     Finally, the second stable version of PyGTK 2.8.x is out!
     <a href="http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.8/pygtk-2.8.1.tar.gz">here</a>.
     Check out <a href="http://article.gmane.org/gmane.comp.gnome.gtk%2B.python/7068">the release announcement</a> or, for a complete list of changes, read <a href="http://live.gnome.org/PyGTK/WhatsNew28">this page</a> at the wiki.""",
     "Johan Dahlin")

item("New article -  Writing win32 applications with python and glade",
     (2005, 9, 17), """Learn how to write pygtk applications on win32
     and create your own podcasting tool at the same time. You can start
     with this tutorial by Nzeka Gilbert
     <a href="http://pygtk.org/articles/bitpodder/BitPodder.htm">here</a>.
     """, 'Rafael Villar Burke')

item("Version 2.8.1 of the PyGTK Reference released", (2005, 9, 17), """ A
     new version (2.8.1) of the <a
     href="http://www.pygtk.org/pygtk2reference/index.html">PyGTK
     Reference</a> is available. This release adds documentation on: the
     pangocairo module and its CaiorContext and CairoFontMap classes; the
     gdk.PangoRenderer class; the pango.Renderer class; the pango.LayoutLine
     class. Other additions include: gdk.Drawable.cairo_create() method,
     gobject.child_watch_add() and gobject.spawn_async() functions, and
     gtk.binding_entry_remove() function. Some bug fixes were made thanks to
     Nikos Kouremenos.""", 'John Finlay')

item("Version 2.8.0 of the PyGTK Reference released", (2005, 9, 7), """ A
     new version (2.8.0) of the <a
     href="http://www.pygtk.org/pygtk2reference/index.html">PyGTK
     Reference</a> is available. This release includes much of the new PyGTK
     2.8 API and many bugfixes - thanks to Nikos Kouremenos, Gian Mario
     Tagliaretti, Steve Langer, Sridhar Ratna, Gustavo Rahal and brett for
     bug reports. And thanks to Gian Mario Tagliaretti for a patch.""",
     'John Finlay')

item("PyGTK 2.8.0 is out!",
     (2005, 9, 3),
     """
     Finally, the new stable version of PyGTK is ready for production usage!
     Fetch it from here: 
     <a href="http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.8/pygtk-2.8.0.tar.gz">here</a>.
     Check out <a href="http://article.gmane.org/gmane.comp.gnome.gtk%2B.python/6874">the release announcement</a> or, for a complete list of changes, read <a href="http://live.gnome.org/PyGTK/WhatsNew28">this page</a> at the wiki.""",
     "Johan Dahlin")

item("PyGTK 2.7.4 is released",
     (2005, 8, 24),
     """
     This is yet another release which contains <i>mostly</i> bug fixes, Get it 
     <a href="http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.7/">here</a>.
     You can also read the the full <a href="http://article.gmane.org/gmane.comp.gnome.gtk%2B.python/6833">release announcement</a>.""",
     "Johan Dahlin")

item("PyGTK 2.7.3 is released",
     (2005, 8, 10),
     """
     This is another minor release which contains only bug fixes, Get it 
     <a href="http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.7/">here</a>.
     You can also read the the full <a href="http://article.gmane.org/gmane.comp.gnome.gtk%2B.python/6699">release announcement</a>.""",
     "Johan Dahlin")

item("PyGTK 2.7.2 is released",
     (2005, 8, 2),
     """
     This is a minor release which contains only bug fixes, Get it 
     <a href="http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.7/">here</a>.
     You can also read the the full <a href="http://article.gmane.org/gmane.comp.gnome.gtk%2B.python/6630">release announcement</a>.""",
     "Johan Dahlin")

item("PyGTK 2.7.1 is released",
     (2005, 7, 10),
     """
     This is a minor release which mostly bug fixes and small (final for 2.7)
     api additions. Fetch it from here: 
     <a href="http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.7/">here</a>.""",
     "Johan Dahlin")

item("PyGTK 2.7.0 is released",
     (2005, 7, 10),
     """
     The first 2.7.x release of PyGTK is now spreading itself through the world.
     Catch it while it's hot, at the usual places. This is release with lots
     of new <b>major</b> features. Cairo, GIOChannel, GSource are among the
     long list of new gadgets.
     Download it from 
     <a href="http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.7/">here</a>.""",
     "Johan Dahlin")

item("GUADEC slides now online",
     (2005, 6, 3),
     """
     The slides of the "Rapid Application Development with PyGTK and libglade"
     talk are now
     <a href="http://www.gdesklets.org/~pycage/rad-slides.tar.bz2">online</a>.
     The slides show how to use Sandino Flores' simple-glade-codegen for
     creating applications in no time. An example is included.""",
     "Martin Grimme")

item("GnomePythonExtras documentation now online",
     (2005, 5, 21),
     """
     The documentation for some of the GnomePythonExtras modules is now
     <a href="http://pygtk.org/reference.html">online</a>.
     Many thanks to Gian Mario Tagliaretti for writing these docs!""",
     "Gustavo Carneiro")

item("GnomePython 2.11.2 released",
     (2005, 5, 18),
     """
     This is a development release for testing pleasure.
     GnomePython 
     It adds some more methods in the gconf, gnomecanvas and gnomevfs modules.
     Download it from 
     <a href="http://ftp.gnome.org/pub/GNOME/sources/gnome-python/2.11/">here</a>.
     The full announcement with the complete list of changes can be found at
     <a href="http://www.daa.com.au/pipermail/pygtk/2005-May/010258.html">the mailing list</a>.""",
     "Rafael Villar Burke")

item("GnomePythonExtras 2.11.2 released",
     (2005, 5, 18),
     """
     This is an unstable release for the joy of testing purpouses.
     GnomePyhtonExtras provides python interfacing modules for some GNOME
     libraries not in the Developer Platform, such as gtkhtml2, gnomeapplet, wnck...
     This release adds some fixes and improvements, and a whole bunch of new
     documentation contributed by Gian Mario Tagliaretti.
     Get the source
     <a href="http://ftp.gnome.org/pub/GNOME/sources/gnome-python-extras/2.11/">here</a>.
     The full announcement with the complete list of changes can be found at
     <a href="http://www.daa.com.au/pipermail/pygtk/2005-May/010260.html">the mailing list</a>.""",
     "Rafael Villar Burke")

item("PyGTK 2.6.2 roars the world!",
     (2005, 5, 15),
     """
     Finally, after almost 2 <b>whole</b> months of waiting, the PyGTK team can produly
     present the latest stable version. As usually in the stable branch there is only
     bug fixes.
     Download it from 
     <a href="http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.6/">here</a>.
     The full announcement containing a list of changes can be found at
     <a href="http://www.daa.com.au/pipermail/pygtk/2005-May/010172.html">the mailing list</a>.""",
     "Johan Dahlin")

item("New version of the PyGTK Tutorial released",
     (2005, 4, 13),
     """
     A new version (2.4) of the <a
     href="http://www.pygtk.org/pygtk2tutorial/index.html">PyGTK
     Tutorial</a> is available. The example programs have been updated to 
     avoid most of the deprecation warnings""",
     'John Finlay')

item("Version 2.6.0 of the PyGTK Reference released",
     (2005, 4, 10),
     """
     A new version (2.6.0) of the <a
     href="http://www.pygtk.org/pygtk2reference/index.html">PyGTK
     Reference</a> is available. This is mostly a bug fix release with
     thanks to John Ehresman, Nikos Kouremenos and Johan Dahlin for bug
     reports. And thanks to Gian Mario Tagliaretti for a patch.""",
     'John Finlay')

item("PyGTK 2.6.1 is here!",
     (2005, 3, 15),
     """
     The PyGTK team has done it again! This is PyGTK's new stable release.
     It will get you some improvements and improvements, as well as fixes.
     Download it from 
     <a href="http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.6/">here</a>.
     The full announcement containing a list of changes can be found at
     <a href="http://www.daa.com.au/pipermail/pygtk/2005-March/009795.html">the mailing list</a>.""",
     "Johan Dahlin")


item("PyGTK 2.6.0 released!",
     (2005, 3, 7),
     """
     This is pyGTK's new stable release.
     Please, use with joy! You'll get the coolest, most stable and most featurefull release ever to make your GTK+ apps smile!. Download it from 
     <a href="http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.6/">here</a>.
     Read the happy announcement and list of changes at
     <a href="http://www.daa.com.au/pipermail/pygtk/2005-March/009757.html">the mailing list</a>.""",
     "Johan Dahlin")


item("Version 2.5.2 of the PyGTK Reference released",
     (2005, 3, 5),
     """
     A new version (2.5.2) of the <a
     href="http://www.pygtk.org/pygtk2reference/index.html">PyGTK
     Reference</a> is available. Changes include documentation on the
     gtk.glade module thanks to Johan Dahlin and many bug fixes thanks to
     Rafael Villar Burke and Gian Mario Tagliaretti.""",
     'John Finlay')

item("PyGTK 2.5.4 released!",
     (2005, 2, 23),
     """
     This will be the final release before 2.6.0 (unless some serious bugs shows up). 
     Please test carefully! You'll be rewarded with the stablest PyGTK release ever!
     <a href="http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.5/">here</a>.
     Read the whole party announcement at
     <a href="http://www.daa.com.au/pipermail/pygtk/2005-February/009654.html">the mailing list</a>.""",
     "Johan Dahlin")
item("Gazpacho 0.5.0",
     (2005, 2, 4),
     """
     Next week, next Gazpacho release. Many exciting new features in this
     0.5.0 version. From here, it will probably only have bug fixes until 1.0.
     See the <a href="http://www.sicem.biz/pipermail/gazpacho/2005-February/000103.html">announce</a> and get the
     <a href="http://gruppy.sicem.biz/descargas">files</a>.
     """,
     "Lorenzo Gil Sanchez")

item("Gazpacho 0.4.0",
     (2005, 1, 28),
     """
     We're glade to announce another version of this interface designer. This
     time a lot of people contributed so you can expect fancy cool new
     features. Don't wait, see the <a href="http://www.sicem.biz/pipermail/gazpacho/2005-January/000098.html">announce</a> and get the <a href="http://gruppy.sicem.biz/descargas">bytes!</a>.
     """,
     "Lorenzo Gil Sanchez")

item("PyGTK 2.5.3 has hit streets!",
     (2005, 1, 23),
     """
     The streets are in rage, they're celebrating the release of PyGTK,
     you can join the party, by downloading it from:
     <a href="http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.5/">here</a>.
     Read the whole party announcement at
     <a href="http://www.daa.com.au/pipermail/pygtk/2005-January/009481.html">the mailing list</a>.""",
     "Johan Dahlin")

item("Tutorial de PyGTK en castellano actualizado",
     (2004, 12, 21),
     """
     An updated spanish translation of the PyGTK tutorial by John Finlay has
     been released. This is the PyGTK way of celebrating this Cervantes' year
     and also an intent to help everybody having fun while learning PyGTK.
     Enjoy it at the usual <a href="http://www.pygtk.org/pygtk2tutorial-es/index.html">www.pygtk.org</a> place!.

     Sale una nueva versi&oacute;n actualizada de la traducci&oacute;n del
     tutorial de PyGTK de John Finlay. De esta manera celebramos este
     a&ntilde;o Cervantes e intentamos que todo el mundo se lo pase bien
     aprendiendo PyGTK. Disfruta del excelente tutorial en el lugar habitual
     <a href="http://www.pygtk.org/pygtk2tutorial-es/index.html">www.pygtk.org</a>!.
     """)

item("Gazpacho 0.3.2 hits the streets",
     (2005, 1, 17),
     """
     We have news about the last version of this Graphical User Interface
     Designer. Maybe not a lot of new features but tons of bug fixes and
     code cleanups, which are necessary for next major features. Check it out
     at <a href="http://gruppy.sicem.biz/descargas">Gazpacho page!</a>
     """)
     
item("GnomePython 2.9.4 is out",
     (2005, 1, 17),
     """
     We are proud to announce the last unstable version of GnomePython which
     includes some fixes related to gnomevfs, gconf and gnome.ui. We would be
     very happy if you could <a href="http://ftp.gnome.org/pub/GNOME/sources/gnome-python/2.9/">download</a> it,
     test it and give us some <a href="http://bugzilla.gnome.org/enter_bug.cgi?product=gnome-python">feedback</a>
     about it. As always, thank you very much Gustavo!
     """)

item("PyGTK 2.5.2 is waiting to be downloaded!",
     (2005, 1, 10),
     """
     We couldn't wait longer than 10 days of the new year before doing a release,
     We're proud to announce that 2.5.2 or PyGTK is now available from the usual places!
     Please note that this is an unstable release, so be careful. Bring em on!
     If you're brave enough:
     <a href="http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.5/">download it now</a>!
     Read the whole announcement at
     <a href="http://www.daa.com.au/pipermail/pygtk/2005-January/009384.html"q>the mailing list</a>.
     """)					     

item("Happy New Year",
     (2005, 1, 1),
     """
     Happy to see you all safe on the other side.<p>From the PyGTK team
     straight to you, a happy new year. And remember, 2005 is going to
     be the year PyGTK takes over the world!
     <p>
     -- kiko, on behalf of the CAPS-LOVING OFFICIAL PYGTK TEAM
     </p>
     """)

item("GnomePython release bonanza!",
     (2004, 12, 31),
     """
     Gustavo's been busy while the rest of us are trying to digest
     fatty holidays meals. He's released updated versions of practically
     all gnome-python components:
     <ul>
        <li><a href="http://ftp.gnome.org/pub/GNOME/sources/gnome-python/2.6/">GnomePython 2.6.2</a><br>(Fixes in gnome.vfs)</li>
        <li><a href="http://ftp.gnome.org/pub/GNOME/sources/gnome-python/2.9/">GnomePython 2.9.2</a><br>(gnome.vfs, bonobo and gconf improvements)</li>
        <li><a href="http://ftp.gnome.org/pub/GNOME/sources/gnome-python-extras/2.9/">GnomePythonExtras 2.9.2</a><br>(egg.recent, gtkspell, pymozembed added)</li>
     </ul>
     Links are to the source tarball download directories. See the
     mailing list release announcements for more detailed infomrmation.
     <p>
     -- kiko
     </p>
     """)

item("So just what is GnomePythonExtras?",
     (2004, 12, 31),
     """
     It's worth mentioning (though we have had a release in the news
     here before) that <a
     href="http://ftp.gnome.org/pub/GNOME/sources/gnome-python-extras/">GnomePythonExtras</a>
     is a new package in the PyGTK family, consisting of add-ons to
     GnomePython that aren't part of the official Gnome platform. It
     serves as a standard place to release bindings for additional
     gnome-related libraries in the hope that they receive attention
     from a larger userbase, with the side-intent of being folded into
     the main distribution. GnomePythonExtras is currently maintained by
     the expert Gustavo Carneiro of Portugal (though he probably
     wouldn't like to describe himself that way, I think I can get away
     with it).
     </p>
     <p>
     -- kiko
     </p>
     """)

item("New version of the PyGTK Tutorial released",
     (2004, 12, 24),
     """
     A new version (2.3) of the <a
     href="http://www.pygtk.org/pygtk2tutorial/index.html">PyGTK
     Tutorial</a> is available. Changes include the addition of sections
     on ColorButtons, FontButtons, Actions, ActionGroups and the UIManager
     and many bug fixes due to: Rafael Villar Burke, Marc Verney, Joey Tsai,
     Steve George, kraai and Jens Knutson.
     """)

item("New version of the PyGTK Reference released",
     (2004, 12, 23),
     """
     A new version (2.5.1) of the <a
     href="http://www.pygtk.org/pygtk2reference/index.html">PyGTK
     Reference</a> is available. Changes include updates to reflect changes in
     PyGTK 2.5.1 and many bug fixes (thanks to Rafael Villar Burke,
     Johan Dahlin, Erik Grinaker, Doug Quale, and Gian Mario Tagliaretti).
     """)

item("PyGTK 2.5.1 is out in the wild!",
     (2004, 12, 23),
     """
     The PyGTK team is pleased to announce PyGTK 2.5.1.
     Please note that this is an unstable release, so be careful
     If you're brave enough:
     <a href="http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.5/">download it now</a>!
     Read the whole announcement at
     <a href="http://www.daa.com.au/pipermail/pygtk/2004-December/009335.html">the mailing list</a>.
     """)

item("PyGTK BOF at the Mataro Ubuntu Conference",
     (2004, 12, 1),
     """
     We are having a BOF at the <a href="http://www.ubuntulinux.org/wiki/Conference/">Mataro Ubuntu Conference</a>. We have a <a href="http://www.ubuntulinux.org/wiki/PyGTKMegaBOF">Wiki page</a> where you can see who is going and what
     are we going to do. By the way, Mataro is close to Barcelona (Spain) and
     the pygtk bof is on the weekend of the 11th and 12th of December.
     """)

item("A bunch of updates",
     (2004, 12, 1),
     """
     We have <a href="ftp://ftp.gnome.org/pub/GNOME/sources/gnome-python/2.5/">PyGTK 2.5.0</a>,
     <a href="http://ftp.gnome.org/pub/GNOME/sources/gnome-python/2.9/">Gnome Python 2.9.1</a> and
     <a href="http://ftp.gnome.org/pub/GNOME/sources/gnome-python-extras/2.9/">Gnome Python Extras 2.9.1</a>. They are all unstable versions so the need your
     help to find bugs and fix them. More information is given in the regular
     mailing list but feel free to ask in our irc channel if you find any
     problem with this packages.
     """)

item("New versions of the PyGTK Reference released",
     (2004, 11, 15),
     """
     A new version (2.5.0) of the <a
     href="http://www.pygtk.org/pygtk2reference/index.html">PyGTK
     Reference</a> is available. Additions include the new GTK+ 2.5.5
     AboutDialog, CellRendererCombo, CellRendererProgress, CellView,
     FileChooserButton, IconView, MenuToolButton widgets and many new
     functions and methods.
     """)

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

