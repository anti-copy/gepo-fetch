#!/bin/sh

DIR=$(cd "$(dirname "$0")"; pwd)

ps -ef|grep auto_syncer | grep -v grep
ps -ef|grep auto_syncer|grep -v grep |awk -F" " '{print $2}' | while read PID
do
    echo "kill $PID "
    kill -9 "${PID}"
done

echo "Create logs dir ${DIR}/logs"
mkdir -p "${DIR}/logs"
log=${DIR}/logs/syncer.log
#备份日志
TIMESTAMP=`date +'%Y-%M-%d_%H%M%S'`
mv ${log} ${log}${TIMESTAMP}
echo "backup logs ${log}"
python auto_syncer.py |tee -a ${log} &
