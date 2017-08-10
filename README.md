kodi-epg
======
A set of scripts to generate xmltv files for use with m3u playlist for Kodi simple iptv


Procedure
======
The procedure for doing this is as follows
* Get a Raspberry Pi
* Install Kodi
* Enable PVR Simple IPTV
* Get an IPTV subscription in an m3u playlist format
* Run this script, giving it the m3u file, to get the xmltv file (required for EPG)
  * The script will
    * Ask you which tv listings you require
    * Will download those xml files and combine into 1 uber xml file
    * Will update the m3u playlist with channel ids from xml files
    * Will create a cron job to down xml files and combine.
* Add the m3u playlist to PVR Simple IPTV
* Add the XML tv file to PVR Simple IPTV

XMLTV and m3u
======
XMLTV is the standard xml definition for EPG (Electronic Program Guide) data. In terms of IPTV it defines the channel names and content
m3u is a standard playlist format which can be used for music or video. In terms of IPTV it defines the available channels and the source for the video stream

Put the two of these together and we have a file that defines the data source and another file that defines the content.

The problem is that the two of them need to match.

XMLTV Example
------
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE tv SYSTEM "xmltv.dtd">

<tv source-info-url="http://www.schedulesdirect.org/" source-info-name="Schedules Direct" generator-info-name="XMLTV/$Id: tv_grab_na_dd.in,v 1.70 2008/03/03 15:21:41 rmeden Exp $" generator-info-url="http://www.xmltv.org/">
  <channel id="I10436.labs.zap2it.com">
    <display-name>13 KERA</display-name>
  </channel>
  <channel id="I10759.labs.zap2it.com">
    <display-name>11 KTVT</display-name>
  </channel>
  <programme id="someId" start="20080715003000 -0600" stop="20080715010000 -0600" channel="I10436.labs.zap2it.com">
    <title lang="en">NOW on PBS</title>
    <desc lang="en">Jordan's Queen Rania has made job creation a priority to help curb the staggering unemployment rates among youths in the Middle East.</desc>
    <date>20080711</date>
    <category lang="en">Newsmagazine</category>
    <category lang="en">Interview</category>
    <category lang="en">Public affairs</category>
    <category lang="en">Series</category>
    <episode-num system="dd_progid">EP01006886.0028</episode-num>
    <episode-num system="onscreen">427</episode-num>
    <audio>
      <stereo>stereo</stereo>
    </audio>
    <previously-shown start="20080711000000" />
    <subtitles type="teletext" />
  </programme>
  <programme start="20080715060000 -0600" stop="20080715080000 -0600" channel="I10759.labs.zap2it.com">
    <title lang="en">The Early Show</title>
    <desc lang="en">Republican candidate John McCain; premiere of the film "The Dark Knight."</desc>
    <date>20080715</date>
    <category lang="en">Talk</category>
    <category lang="en">News</category>
    <category lang="en">Series</category>
    <episode-num system="dd_progid">EP00337003.2361</episode-num>
    <audio>
      <stereo>stereo</stereo>
    </audio>
    <subtitles type="teletext" />
  </programme>
</tv>
```