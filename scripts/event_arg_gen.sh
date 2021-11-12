#!/bin/bash

find $1 | grep -E ".pointer" | xargs -I {} grep -Po "([^;]+EVENT[^;]+)" {} | sort | uniq > $1/event.txt

find $1 | grep -E ".pointer" | xargs -I {} grep -Po "([^;]+ARG)" {} | sort | uniq > $1/arg.txt
