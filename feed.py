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

import time

#
# Convenience function imported by newsitems.py; this is essentially a
# circular import but it's not really important and uses less files
#
def setup_item(item):
    title, date, desc = item
    ret = {}
    if type(date) is int:
        date = time.strftime("%Y-%m-%d %a %H:%M", time.localtime(date))
    ret['title'] = title
    ret['pubDate'] = date
    ret['description'] = desc
    return ret

# RSS generation

rss_header = r"""
<?xml version="1.0"?>

<!DOCTYPE rss PUBLIC "-//Netscape Communications//DTD RSS 0.91//EN"
"http://my.netscape.com/publish/formats/rss-0.91.dtd">

<rss version="0.91">

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
        # XXX handle escaping of invalid RSS content
        sections.append(rss_item_template % setup_item(item))
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
        sections.append(src_item_template % setup_item(item))
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

