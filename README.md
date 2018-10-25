# INF0617_Tarefa4

Comandos

$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.0.0.jar -input /tmp/data/books -output /tmp/data/author_vocabulary -mapper "python map_author_vocabulary.py"
 
$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.0.0.jar -input /tmp/data/author_vocabulary/part-00000 -output /tmp/data/vocabulary -mapper '/bin/cat' -reducer "python reduce_vocabulary.py"
 
$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.0.0.jar -input /tmp/data/author_vocabulary/part-00000 -output /tmp/data/author_complexity -mapper '/bin/cat' -reducer "python reduce_author_complexity.py"

$HADOOP_HOME/bin/hdfs dfs -cat /tmp/data/author_complexity/part-00000
