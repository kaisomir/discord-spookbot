## Spookbot

### Setup

1. Create a bot application from the Discord developers page.

2. Install the `discord.py` module:

    $ sudo -H pip3 install discord

3. Create the file `auth.json` with the following contents:

```json
{
    "token":"Your Discord Auth Token Here",
    "clientId":"Your Discord Bot Client ID Here"
}
```

4. Run `python3 spookbot.py`. It should print out an invite as it starts:

    $ python3 spookbot.py
    https://discordapp.com/oauth2/authorize?&client_id=123456789&scope=bot&permissions=0

5. Invite the bot on your server, and you're set!