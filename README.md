# OwnerRez API Python SDK

NOTE: You will need to obtain a Personal Access Token for the API  [https://www.ownerreservations.com/support/articles/api-auth#personal-access-tokens](https://www.ownerreservations.com/support/articles/api-auth#personal-access-tokens).  Without a token you will not be able to successfully obtain valid API results.

### Windows setup Solcast API Key

Setup System/User `environment variable`.  Details on advanced editing [StackOverflow superuser walkthrough](https://superuser.com/questions/949560/how-do-i-set-system-environment-variables-in-windows-10)

```
WinKey + R
```

Copy and Paste the following text to the **Open:** input text box for the Run Dialog

```
%windir%\System32\rundll32.exe sysdm.cpl,EditEnvironmentVariables
```

Add a user or system `environment variable` to hold the `owner_rez_username` and `owner_rez_token` keys.  User environment variables will only be available to your particular user, system environment variables are shared for all users on the system
