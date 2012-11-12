#!/bin/bash


SOURCE="${BASH_SOURCE[0]}"
#echo $SOURCE

DIR="$( dirname "$SOURCE" )"
while [ -h "$SOURCE" ]
do 
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE"
  DIR="$( cd -P "$( dirname "$SOURCE"  )" && pwd )"
done
DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"

#echo $SOURCE
#echo $DIR

#echo dirname $(readlink -f $SOURCE)

epath="$DIR/operate_xinput_device.py" 
val=`cat "$DIR/toggle"`

if [ $val -eq 0 ]
then
  echo 1 > "$DIR/toggle"
else
  echo 0 > "$DIR/toggle"

fi


python $epath $val

