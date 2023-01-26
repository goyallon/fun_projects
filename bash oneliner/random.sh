while :
do
        tr -dc 'a-zA-Z0-9~!@#$%^&*_()+}{?></";.,[]=-' < /dev/urandom | fold -w 128 | head -n 1
        sleep 0.1
done
