#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Copyright (C) 2004 R. Sridhar <sridharinfinity@users.sf.net>.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software 
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

import time, cgi

#
# Convenience function imported by newsitems.py; this is essentially a
# circular import but it's not really important and uses less files
#
def setup_rss_item(title, date, desc):
    ret = {}
    ret['title'] = cgi.escape(title)
    date = time.strptime("%s %s %s" % date, "%Y %m %d")
    # XXX someday the time and GMT hack will bite us in the rear
    ret['pubDate'] = time.strftime("%a, %d %b %Y %H:%M:%S GMT", date)
    ret['description'] = cgi.escape(desc)
    return ret

def setup_item(title, date, desc):
    ret = {}
    ret['title'] = title
    date = time.strptime("%s %s %s" % date, "%Y %m %d")
    ret['pubDate'] = time.strftime("%A %d %B %Y", date)
    ret['description'] = desc
    return ret

# RSS generation; note that the <xml bits *must* come at the very top of
# the document, no whitespace before it allowed.
# http://www.feedvalidator.org/ can be used to check validity of the RSS.

rss_header = r"""<?xml version="1.0"?>
<rss version="2.0">

  <channel>
    <title>PyGTK News</title>
    <description>PyGTK provides a convenient wrapper for the GTK library 
    for use in Python programs, and takes care of many of the boring details 
    such as managing memory and type casting. When combined with PyORBit and 
    gnome-python, it can be used to write full featured Gnome applications.
    </description>
    <language>en-us</language>
    <link>http://pygtk.org</link>
    <copyright> © 2003 by The GNOME Project</copyright>
    <webMaster>pygtk-web@pygtk.org</webMaster>
"""

rss_footer = r"""
  </channel>
</rss>
"""

rss_image = r"""
  <image>
    <title>PyGTK</title>
    <url>http://pygtk.org/img/gnome-64.png</url>
    <link>http://pygtk.org</link>
  </image>
"""

rss_item_template = r"""
  <item>
    <title>%(title)s</title>
    <pubDate>%(pubDate)s</pubDate>
    <description>%(description)s</description>
  </item>
"""

def write_rss(fp, items):
    sections = [rss_header, rss_image]
    for item in items:
        sections.append(rss_item_template % setup_rss_item(*item))
    sections.append(rss_footer)
    fp.write(''.join(sections))
    
# STP .src generation

src_item_template = r"""
<div class="news">
<h4>%(title)s</h4>
<h5>%(pubDate)s</h5>
<p>%(description)s</p>
</div>
"""

def write_src(fp, items):
    sections = []
    for item in items:
        sections.append(src_item_template % setup_item(*item))
    fp.write(''.join(sections))
    
def items_to_rss(items, rss_file, maxitems=0):
    "Convert items to rss file"
    if maxitems:
        items = items[:maxitems]
    write_rss(file(rss_file, 'w'), items)
    
def items_to_src(items, src_file, maxitems=0):
    "Convert items to STP src file"
    if maxitems:
        items = items[:maxitems]
    write_src(file(src_file, 'w'), items)

if __name__ == "__main__":
    from newsitems import items
    items_to_rss(items, 'news.rss', 10)
    items_to_src(items, 'newsitems-index.src', 5)
    items_to_src(items, 'newsitems.src')

