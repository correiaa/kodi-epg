# kodi-epg
A set of scripts to generate xmltv files for use with m3u playlist for Kodi simple iptv


The procedure for doing this is as follows
Get a Raspberry Pi
Install Kodi
Enable PVR Simple IPTV
Get an IPTV subscription in an m3u playlist format
Run this script, giving it the m3u file, to get the xmltv file (required for EPG)
  The script 
    Ask you which tv listings you require
    Will download those xml files and combine into 1 uber xml file
    Will update the m3u playlist with channel ids from xml files
    Will create a cron job to down xml files and combine.
Add the m3u playlist to PVR Simple IPTV
Add the XML tv file to PVR Simple IPTV
