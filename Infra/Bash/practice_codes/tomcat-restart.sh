#!/bin/bash
date=$(date +%F)
retry=true

while LOOP_FLAG; do

    service tomcat7 restart

    # tomcat
    echo "checking catalina.out ..."
    while true; do
        line=$(tail -n1 /instancelocal/logs/tomcat/catalina.$date.out)
        if [ -n "$(echo $line | grep -i 'Server startup in')" ]; then
            echo "tomcat log : Checked"
            echo $line
            break
        fi
    done

    # jmxexport
    echo "checking jmxexport.log..."
    while true; do
        line=$(tail -n1 /instancelocal/logs/tomcat/jmxexport.log)
        if [ -n "$(echo $line | grep -i 'Server startup in')" ]; then
            echo "jmxexport log: Checked"
            echo $line
            break
        fi
    done

    # memcache connection check
    echo "Checking Memcache connection..."
    while true; do
        line=$(tail -n1 /instancelocal/logs/tomcat/catalina.$date.out)
        if [ -n "$(echo $line | grep -i 'connection is stable')" ]; then
            echo "memcache connection: chekced"
            echo $line
            retry=false
            break
        fi
        if [ -n "$(echo $line | grep -i 'connection is unstable')" o -n "$(echo $line | grep -i 'exception')"]; then
            echo "memcache connection: unstable"
            echo $line
            echo "Restarts tomcat..."
            break
        fi
    done
done

echo "All Done."