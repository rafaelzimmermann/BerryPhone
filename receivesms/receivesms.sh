#!/bin/bash

./session.sh
./token.sh

TOKEN=$(<token.txt)

DATA="<request><PageIndex>1</PageIndex><ReadCount>1</ReadCount><BoxType>1</BoxType><SortType>0</SortType><Ascending>0</Ascending><UnreadPreferred>1</UnreadPreferred></request>"

curl -b session.txt -c session.txt -H "X-Requested-With: XMLHttpRequest" --data "$DATA" http://192.168.8.1/api/sms/sms-list --header "__RequestVerificationToken: $TOKEN" --header "Content-Type:text/xml"
