#!/bin/bash
echo "Getting playlist from Server"
url=$(cat subscription_url)
curl $url > remote.m3u

echo "Comparing files"

diff remote.m3u Original.m3u.m3u 
if [ $? -ne 0 ] 
then 
echo "Files are different"
echo The Playlist file on server has been updated | mail -s Remote Updated -a remote.m3u kenneth.oneill@gmail.com
fi

echo "removing remote file"
rm remote.m3u
