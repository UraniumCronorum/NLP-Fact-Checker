#!/bin/bash

export STANFORD_MODELS=$(pwd)/stanford-ner-2015-12-09/classifiers/english.all.3class.distsim.crf.ser.gz
export CLASSPATH=$CLASSPATH:CLASSPATH=:$(pwd)/stanford-ner-2015-12-09/:

