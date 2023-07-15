# rev-leonardo.ai

Reverse Engineered Leonardo AI Python Client
This Python client allows you to interact with the Leonardo AI platform using the reverse-engineered API. 

Please note that reverse engineering APIs may violate the terms of service of the platform, and it's essential to use this client responsibly and at your own risk.

Configuring the Bot Accounts
The client requires you to set up your bot accounts in the config.json file. The file should be structured as follows:


```

{
    "bot_accounts": [
        {
            "email_address": "your_bot_email@example.com",
            "password": "your_bot_password"
        },
        {
            "email_address": "another_bot_email@example.com",
            "password": "another_bot_password"
        }
    ]
}

```

You can add multiple bot accounts if you want to perform actions using different identities.
Make sure to provide the correct email address and password for each bot account.
