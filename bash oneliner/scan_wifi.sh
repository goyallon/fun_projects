iw dev $WIFI scan | egrep "SSID|signal" | awk -F ":" '{print $2}' | sed 'N;s/\n/:/' | sort