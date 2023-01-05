#!/bin/bash

for d in tests/*/
do
    cd $d
    test_id=$(echo $d | grep -o '[0-9a-f]\{8\}-[0-9a-f]\{4\}-[0-9a-f]\{4\}-[0-9a-f]\{4\}-[0-9a-f]\{12\}')
    echo -e "Compiling ${test_id}"
    GOOS=darwin GOARCH=arm64 go build -o "${test_id}_darwin-arm64" "${test_id}.go"
    GOOS=darwin GOARCH=amd64 go build -o "${test_id}_darwin-x86_64" "${test_id}.go"
    GOOS=linux GOARCH=arm64 go build -o "${test_id}_linux-arm64" "${test_id}.go"
    GOOS=linux GOARCH=amd64 go build -o "${test_id}_linux-x86_64" "${test_id}.go"
    GOOS=windows GOARCH=amd64 go build -o "${test_id}_windows-x86_64" "${test_id}.go"
    cd ../..
done
