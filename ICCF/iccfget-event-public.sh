#/bin/bash

eventid="$@"
domurl="https://www.iccf.com/GetEventPGN.aspx?id="
pgnurl=$domurl$eventid
pgnpath=$HOME/Downloads/chess
pgnfile=$pgnpath/iccfevent-$eventid.pgn

exec /usr/local/bin/wget --no-check-certificate -O $pgnfile -t 0 $pgnurl
