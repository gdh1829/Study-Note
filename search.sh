#!/bin/bash
loggedUser=4
client=5
recruiter=6
job=7
candidate=8
resume=9
process=10
sales=11
activity=12

echo -e "Insert Specific Date(ex. 2018/08/08) If nothing inserted, yesterday will be assigned: \c"
read date
[ -n date ] && date=`date --date="1 day ago" +%Y/%m/%d`
echo "$date is set as target date"

echo -e "What resource do you want to refer to?"
echo -e " logged user: $loggedUser \n client: $client \n recruiter: $recruiter \n job: $job \n candidate: $candidate \n resume: $resume \n process: $process \n sales: $sales \n activity: $activity"
echo -e "Select its number that you would like(Delimeter for multiple choices is space): \c"
read -a resource_choices

if [ -z "${#resource_choices[@]}" ]; then
    echo "No resource choices. Process is closed."
    exit
fi

for i in ${resource_choices[@]}; do
    isOk=false
    for j in "loggedUser" "client" "recruiter" "job" "candidate" "resume" "activity" "sales" "activity"; do
        if [ $i == ${!j} ]; then
            isOk=true
            selectedResourceNameList=("${selectedResourceNameList[@]}" $j)
        fi
    done
    if [ "$isOk" == "false" ] ; then
        echo "$i is an wrong input. Process is closed."
        exit;
    fi
done

index=0
while [ $index -lt ${#selectedResourceNameList[@]} ]; do
    echo -e "Minimum ${selectedResourceNameList[($index)]} number: \c"
    read min_${resource_choices[($index)]}
    echo -e "Maximum ${selectedResourceNameList[($index)]} number: \c"
    read max_${resource_choices[($index)]}
    index+=1;
done

echo -e "Search in action..."

getMin() {
    local tmp;
    tmp="min_$1";
    return ${!tmp};
}

getMax() {
    local tmp;
    tmp="max_$1";
    return ${!tmp};
}

# $1 line
# $2 resource field
# $3 filename
search_filter() {
    local resource_count=$(echo $1 | cut -d ',' -f$2)
    if [ $resource_count -ge `getMin $2` -a $resource_count -le `getMax $2` ]; then
        return "$3"
    fi
}

for i in $(ls ../resource-count-report_P*.csv); do
    for line in $(grep --regexp "$date" $i); do
        echo $line
        for resource_field  in ${resource_choices[@]}; do
            sample=`search_filter $line $resource_field $i`
            echo $sample
        done
        # #client_count=$(echo $line | cut -d ',' -f5)
        # #person_count=$(echo $line | cut -d ',' -f9)
        # resume_count=$(echo $line | cut -d ',' -f10)
        # logged_user_count=$(echo $line | cut -d ',' -f4)
        # if [ $resume_count -ge $min_resume_num -a $resume_count -le $max_resume_num ]; then
        #     if [ $logged_user_count -ge $min_user_num -a $logged_user_count -le $max_user_num ]; then
        #           echo $i
        #           break
        #     fi
        # fi
    done
done

echo -e "Done"
