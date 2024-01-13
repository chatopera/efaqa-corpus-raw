#! /bin/bash 
###########################################
#
###########################################

# constants
baseDir=$(cd `dirname "$0"`;pwd)
cwdDir=$PWD
export PYTHONUNBUFFERED=1
export PATH=/opt/miniconda3/envs/venv-py3/bin:$PATH
export TS=$(date +%Y%m%d%H%M%S)
export DATE=`date "+%Y%m%d"`
export DATE_WITH_TIME=`date "+%Y%m%d-%H%M%S"` #add %3N as we want millisecond too

# functions

# main 
[ -z "${BASH_SOURCE[0]}" -o "${BASH_SOURCE[0]}" = "$0" ] || return
cd $baseDir/../tmp

if [ ! -f 002.format_file.utf8 ]; then
    echo "Run 002.format_file.sh first to generate file."
    exit 1
fi

mv 002.format_file.utf8 ../efaqa_corpus_raw/data
cd ../efaqa_corpus_raw/data

mv 002.format_file.utf8 efaqa_corpus_raw.utf8
gzip efaqa_corpus_raw.utf8