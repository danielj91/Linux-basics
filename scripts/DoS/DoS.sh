#! /bin/bash

for (( i=1; i<=50000; i++ )); do
curl --header "connection keep alive" 3.72.82.9 && echo "x" & echo "Test nr. $i."
done