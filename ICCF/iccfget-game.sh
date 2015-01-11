#/bin/bash

cookies=$HOME/.mozilla/cookies.txt
gameid="$@"
domurl="https://www.iccf.com/GetPGN.aspx?id="
pgnurl=$domurl$gameid
pgnpath=$HOME/Downloads/chess
pgnfile=iccfgame-$gameid.pgn

exec /usr/local/bin/wget --no-check-certificate --load-cookies=$cookies -O $pgnfile -t 0 $pgnurl
