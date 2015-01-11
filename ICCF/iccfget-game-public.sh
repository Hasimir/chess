#/bin/bash

gameid="$@"
domurl="https://www.iccf.com/GetPGN.aspx?id="
pgnurl=$domurl$gameid
pgnpath=$HOME/Downloads/chess
pgnfile=iccfgame-$gameid.pgn

exec /usr/local/bin/wget --no-check-certificate -O $pgnfile -t 0 $pgnurl
