#!/usr/bin/env bash
echo $1
curl -X POST -H "Content-Type: application/json" -d "{
  \"greeting\":[{
    \"text\": \"Hi {{user_first_name}}. Let\'s play Tic-tac-toe with me. Start new game from the menu\",
    \"locale\":\"default\",
  }]
}" "https://graph.facebook.com/v2.6/me/messenger_profile?access_token=$PAGE_ACCESS_TOKEN"