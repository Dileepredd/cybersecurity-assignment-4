### Token management System:
    there are three routs in the api
    1. POST /register
    2. POST /token
    3. POST /newtoken

    using route 1 a user has to register.
    using route 2 a user can get the latest generated new token.
    using route three a user can generate new token.

    images:
    1. inject.PNG:
        this api is vulnurable to injection attack.
        as the image specifies when an sql injected password is sent.
        it generated a new token and returned it.

    2. security_misconfiguration.PNG:
        here http protocol is used instead od https.
    
    3. broken_authentication.PNG:
        since http protocol is used and during authentication username and password is used instead of digest.
        it is open to man in the midle attack.

    4. insufficiant_logging.PNG:
        in the image only usename is logged.
        if injection attack happens using password we cannot identify intrusion.

    5. lackofresourcesorratelimiting.PNG:
        as u can see in the image system is validating the user but its not limiting it.
        an authentic user can use DOS attack.
