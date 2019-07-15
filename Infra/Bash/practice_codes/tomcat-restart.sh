#!/bin/bash
date=$(date +%F)
retry=true

echo "$date Memcache Recovery Process starts..."
while $retry; do

    sudo service tomcat7 restart
    sudo kill $(ps axo pid,cmd|grep jmx|grep -v grep|sed -e 's/^ *//'|cut -d" " -f1) && sudo service jmx-exporter start

    # tomcat
    echo "checking catalina.$date.log ..."
    while true; do
        line=$(tail -n1 /instancelocal/log/tomcat/catalina.$date.log)
        if [ -n "$(echo $line | grep -i 'Queue started')" ]; then
            echo "[SUCCESS] catalina.$date.log : OK -> $line"
            break
        fi
    done

    # jmxexport
    echo "checking jmxexport.log..."
    while true; do
        line=$(tail -n1 /instancelocal/log/tomcat/jmxexport.log)
        if [ -n "$(echo $line | grep -i 'Publisher porters.jmxexport.aws.CloudwatchPublisher loaded')" ]; then
            echo "[SUCCESS] jmxexport.log: OK -> $line"
            break
        fi
    done

    # memcache connection check
    echo "Checking Memcache connection..."
    while true; do
        line=$(tail -n1 /instancelocal/log/tomcat/catalina.$date.log)
        if [ -n "$(echo $line | grep -i 'connection is stable')" ]; then
            echo "[SUCCESS] memcache connection check: OK -> $line"
            retry=false
            break
        fi
        if [ -n "$(echo $line | grep -i 'connection is unstable')" ]; then
            echo "[WARNING] memcache connection: unstable!!! -> $line"
            echo "[WARNING] Retry Restarting tomcat...!"
            break
        fi
    done
done

echo "All Done."
