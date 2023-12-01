#!/usr/bin/env bash
# Clean up the intermediate HDFS directories which could have been created as a part o
hdfs dfs -ls /intermediate-1
if [[ $? == 0 ]]
then
echo "Deleteing Intermediate-1 HDFS directory before starting job.."
hdfs dfs -rm -r /intermediate-1
fi
hdfs dfs -ls /intermediate-2
if [[ $? == 0 ]]
then
echo "Deleting Intermediate-2 HDFS directory before starting job.."
hdfs dfs -rm -r /intermediate-2
fi
echo "Initiating stage-1"
echo "==========================================================="
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.3.jar \
-mapper "$PWD/mapper1.py" \
-reducer "$PWD/reducer1.py" \
-input /cust_prod/dataset_sample.txt \
-output /intermediate-1
echo "==========================================================="
echo "Stage-1 done"
echo "Initiating stage-2"
echo "==========================================================="
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.3.jar \
-mapper "$PWD/mapper2.py" \
-reducer "$PWD/reducer2.py" \
-input /intermediate-1/part-00000 \
-output /intermediate-2
echo "==========================================================="
echo "Stage-2 done"
hdfs dfs -ls /task2/output
if [[ $? == 0 ]]
then
echo "Deleteing old output before starting job.."
hdfs dfs -rm -r /task2/output
fi
echo "Initializing stage-3"
echo "==========================================================="
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.3.jar \
-mapper "$PWD/mapper3.py" \
-reducer "$PWD/reducer3.py" \
-input /intermediate-2/part-00000 \
-output /task2/output
echo "==========================================================="
echo "Stage-3 done"
