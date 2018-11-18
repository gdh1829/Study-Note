#!/bin/bash

S3_KEYPATH="search/connection/es/v1"

CONFIGURATION_SERVER_PORT=80
CONFIGURATION_SERVER_HOST="http://configuration.com"
BASE_CURL_PATH="${CONFIGURATION_SERVER_HOST}:${CONFIGURATION_SERVER_PORT}/item/${S3_KEYPATH}"

ARRAY=("master.json" "text.json" "file.json")

success_count=0
total_file_count=${#ARRAY[@]}

function resultMessage {
    echo "$success_count/$total_file_count done"
}

function request {
    name=`echo $1 | cut -d'.' -f1`
    result_code=$(curl --silent --write-out "%{http_code}" \
        -H "Content-Type: application/json" -H "X-IDENTITY: SERVICE=MAINTENANCE" \
        -X PUT "${BASE_CURL_PATH}/${name}" -d "@config-files/$1")
}

for item in ${ARRAY[@]}; do
    if [ ! -f config-files/${item} ]; then
        echo "[ERROR] $item is not existed."
        resultMessage
        exit 1
    fi

    echo "Uploading $item to S3..."
    if [ $item == "master.json" ]; then
        request $item
    else
        request "mapping/${item}"
    fi

    if [ "$result_code" -eq "204" ]; then
        echo "[SUCCESS] "
        ((success_count++))
    else
        echo "[ERROR] $item upload failed."
        exit 1
    fi
    resultMessage
done

echo "Process is Done."
resultMessage
exit 0;