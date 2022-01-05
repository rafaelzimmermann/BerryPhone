#!/bin/bash

parse_yaml() {
   local prefix=$2
   local s='[[:space:]]*' w='[a-zA-Z0-9_]*' fs=$(echo @|tr @ '\034')
   sed -ne "s|^\($s\)\($w\)$s:$s\"\(.*\)\"$s\$|\1$fs\2$fs\3|p" \
        -e "s|^\($s\)\($w\)$s:$s\(.*\)$s\$|\1$fs\2$fs\3|p"  $1 |
   awk -F$fs '{
      indent = length($1)/2;
      vname[indent] = $2;
      for (i in vname) {if (i > indent) {delete vname[i]}}
      if (length($3) > 0) {
         vn=""; for (i=0; i<indent; i++) {vn=(vn)(vname[i])("_")}
         printf("%s%s%s=\"%s\"\n", "'$prefix'",vn, $2, $3);
      }
   }'
}

eval $(parse_yaml config.yml "config_")

TOKEN=$config_telegram_token
CHAT_ID=$config_telegram_chat_id

# no need to change anything below.

URL="https://api.telegram.org/bot${TOKEN}/sendMessage"

NL=$'\n'
declare -i i MSGS
MSGS=${SMS_MESSAGES}
CONTENT="${SMS_1_NUMBER}${NL}"
i=1
while [ $i -le $MSGS ]; do
    declare "PART"="SMS_${i}_TEXT"
    CONTENT="${CONTENT}${!PART}"
    i=$(($i+1))
done
CONTENT=${CONTENT//&/%26}
CONTENT=${CONTENT//</%3C}
CONTENT=${CONTENT//>/%3E}

eval "curl -s -X POST $URL -d chat_id=\"${CHAT_ID}\" -d text=\"${CONTENT}\""