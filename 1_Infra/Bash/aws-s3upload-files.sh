BASEDIR="/tmp/infra/scripts/configuration-service/init-store"
DEBUG=""
PROFILE=${PROFILE:-default}
S3_PATH="porters-dr-configuration-storage/search/connection/es/v1"

CMD="cd $BASEDIR"
echo -n "Exec: $CMD ... "
[ -z "$DEBUG" ] && eval $CMD;
echo "done"

ARRAY=("master.json" "text.json" "file.json")

success_count=0
total_file_count=${#ARRAY[@]}

for item in ${ARRAY[@]}; do
	if [ ! -f $item ]; then
		echo "[ERROR] $item is not existed."
		echo "Result - Success file count/Total file count: $success_count/$total_file_count"
		exit 1
	fi

	if [ $item == "master.json" ]; then
		echo "Uploading $item to S3..."
		aws --profile $PROFILE s3 cp $item s3://${S3_PATH}/${item}
		((success_count++))
		echo "$success_count/$total_file_count done"
	else
		echo "Uploading $item to S3..."
		aws --profile $PROFILE s3 cp $item s3://${S3_PATH}/mapping/${item}
		((success_count++))
		echo "$success_count/$total_file_count done"
	fi
done

echo "Process is Done."
echo "Result - Success file count/Total file count: $success_count/$total_file_count"
exit 0;
