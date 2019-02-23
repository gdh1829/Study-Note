#!/bin/bash -x

#database 
DB1="Db1"
DB2="Db2"
DB3="Db3"
DB4="Db4"
DB5="Db5"
DB6="Db6"
DB7="Db7"
DB8="Db8"
DB10="Db10"

echo -e "Insert target date(format ex. 20180909). If you enter nothing, yesterday will be automatically assigned: \c"
read date
[ -z $date ] && date=`date --date="1 day ago" +%Y%m%d`
echo "$date is set as target date"

table_head=`head -n1 /home/aggregate/hrbc-system-report/logs/daily-report/resource-count/hrbc-daily-resource-count-report_$DB1.csv`
db_resource_table="$table_head"

databases=($DB1 $DB2 $DB3 $DB4 $DB5 $DB6 $DB7 $DB8 $DB10)
formated_date=`date -d $date +%Y/%m/%d`
for db in ${databases[@]}; do
    db_resource_data="`cat /home/aggregate/hrbc-system-report/logs/daily-report/resource-count/hrbc-daily-resource-count-report_$db.csv | grep $formated_date`"
    db_resource_table="$db_resource_table\n$db_resource_data"
done

echo -e $db_resource_table > db_resource_$date.csv

echo "db_resource_$date.csv has been created. Check out the file."

