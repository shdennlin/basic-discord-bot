# Discord Bot

## My bot link

[Shawn Bot](https://discord.com/api/oauth2/authorize?client_id=1015569548440780880&permissions=3094&scope=bot)

## command list

1. `!echo <message>`: replay the same message to a user
   example:
   1. `!echo msgTest`: replay `msgTest` to the user

2. `!broadcast <channel> <message> <second>`: send messages to a specific channel periodically
   example:
   1. `!broadcast #general test1 5`: send message `test1` to `#general` every 5 seconds
   2. `!broadcast #announce msgTest 10`: send message `msgText` to `#announce` every 10 seconds

3. `!get_broadcast`: get the broadcast list
   example:
   `!get_broadcast`: return below:

   ``` text
     id:0x7f119a5797c0 channel:#general msg:test2 sleep_time:20s
     id:0x7f119a579640 channel:#general msg:test3 sleep_time:10s
   ```

4. `!cancel_broadcast <broadcast_id>`: cancel the broadcast
   example:
   1. `!cancel_broadcast 0x7f119a579640`: cancel the broadcast with id `0x7f119a579640`

5. `!cancel_all_broadcast`: cancel all the broadcast

6. `!create_channel`: create a new channel
   example:
   1. `!create_channel test`: create a new channel named `test`

7. `!kick`: kick the specific user
   example:
   1. `!kick @user`: kick the user `@user`

8. `!ban`: ban the specific user
   example:
   1. `!ban @user`: ban the user `@user`

## Develop prerequisites

1. python >3.8, 3.9
2. poetry

## How to build a project

1. `cp .env.example .env`
2. edit env file
3. `make run`

## Ref

1. [Welcome to discord.py](https://discordpy.readthedocs.io/en/latest/index.html)
