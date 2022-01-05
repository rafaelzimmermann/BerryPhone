#!/bin/bash

TOKEN=$(curl -s -b session.txt -c session.txt http://192.168.8.1/html/smsinbox.html)
TOKEN=$(echo $TOKEN | cut -d'"' -f 10)

echo $TOKEN > token.txt