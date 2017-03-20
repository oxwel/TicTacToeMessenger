#!/usr/bin/env bash
echo $1
curl -X POST -H "Content-Type: application/json" -d "{
  \"greeting\":[{
    \"text\": \"Hi {{user_first_name}}. Let\'s play Tic-tac-toe with me. Start new game from the menu - come on!\",
    \"locale\":\"default\",
  },{
   \"greeting\":[{
    \"text\": \"Привіт, {{user_first_name}}. Зіграємо у Хрестики-нулики? Так, я не зовсім людина - але ми ще подивимось, хто кого обіграє!\",
    \"locale\":\"uk_UA\",
  },{
   \"greeting\":[{
    \"text\": \"Привет, {{user_first_name}}. Поиграем в Крестики-нолики? Я не совсем человек, но мы еще посмотрим, кто кого!\",
    \"locale\":\"ru_RU\",
  }]
}" "https://graph.facebook.com/v2.6/me/messenger_profile?access_token=$PAGE_ACCESS_TOKEN"