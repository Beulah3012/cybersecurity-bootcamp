#!/bin/bash
# Lets create an until loop that takes a variable and adds 1 till it reachs 10
# Have the script echo out what are current number is

number=1
until [ $number -eq 11 ]; do
  echo "The number is now: $number"
  number=$((number + 1))
done

