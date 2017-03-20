#!/usr/bin/env bash
echo $1
curl -X POST -H "Content-Type: application/json" -d "{
  \"greeting\":[{
    \"text\": \"Play Tic-tac-toe with GameClub bot. See the menu to start new game\",
    \"locale\":\"default\",
  }]
}" "https://graph.facebook.com/v2.6/me/messenger_profile?access_token=$PAGE_ACCESS_TOKEN"