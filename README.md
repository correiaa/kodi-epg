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
	        <episode-num system="dd_progid">EP00337003.2361</episode-num>
	        <audio>
	          <stereo>stereo</stereo>
	        </audio>
	        <subtitles type="teletext" />
	    </programme>
    </tv>


m3u Example
------
Here is a sample m3u playlist file.
Note that the first line must always be #EXTM3U
The file then proceeds in pairs of lines.
Line 1 (of the pair) is the EXTINF information and Line 2 is the data source.


    #EXTM3U
    #EXTINF:-1, group-title="KTV",11 KTVT
    http://<your media source here>
    #EXTINF:-1, group-title="KTV",13 KERA
    http://<your media source here>

The EXTINF line has no well defined format but you can read more about it [here](https://en.wikipedia.org/wiki/M3U)
For our purposes the EXTINF above breaks down into 

    #EXTINF: (duration) (attributes), (channel title). Required params are: duration and channel title. 

In case of live TV links the duaration has always to be 0 or -1.
The group-title can be used to groups channels in the IPTV client (ie sports, cinema or by conuntry. It is up to you).

Correlating the two sources
------
In order to get the EPG and video source to work together correctly we need to ensure that the IPTV client in Kodi can map an entry in the m3u file to a channel tag in the XMLTV file in order to look up the program data in the XMLTV file.
There is some automatic rules to this, but the easiest way to ensure compatability is to edit the m3u file to include the tvg-id tag for each EXINF entry and have that match a channel id tag in the XMLTV file.

So we would change the EXTINF above to be
    #EXTM3U
    #EXTINF:-1, tvg-id="I10759.labs.zap2it.com" group-title="KTV",11 KTVT
    http://<your media source here>
    #EXTINF:-1, tvg-id="I10436.labs.zap2it.com" group-title="KTV",13 KERA
    http://your media source here


Now our IPTV client can correlate the Channels with the Program Data.

Point to note, you can edit the m3u file as much as you like as long as you follow the "standard". The first line must be #EXTM3U and then follows pairs of lines.
You can change the channel title (the last thing after the last comma), the group-title (to group into logical entities), can change the order (again as log as you move pairs of lines), can add the tvg-id
I use the offical [Kodi Simple IPTV client](http://kodi.wiki/view/Add-on:IPTV_Simple_Client) which supports the following options

* tvg-id is value of channel id in EPG xml file. If the tag is absent then addon will use tvg-name for map channel to EPG;
* tvg-name is value of display-name in EPG there all space chars replaced to _ (underscore char) if this value is not found in xml then addon will use the channel name to find correct EPG.
* tvg-logo is name of channel logo file without extension (.png). If this tag is absent then addon will use channel name to find logo.
* tvg-shift is value in hours to shift EPG time. This tag can be used in #EXTM3U for apply shift to all channels or in #EXTINF for apply shift only to current channel.
* group-title is channels group name. If the tag is absent then addon will use group name from the previous channel.
* radio is flag that indicate what group or cahnnel is radio. If the tag is absent then addon will use value from current group (if exists).