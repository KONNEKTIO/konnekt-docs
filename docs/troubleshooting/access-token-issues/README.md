# Access token issues

Authentication token errors are the most common KONNEKT issues. The pages below cover specific error messages and their solutions.



1. [Error message about missing token](error-message-about-missing-token.md) \
   Admin consent for the KONNEKT app registration is missing, was revoked, or has not been granted for the required scopes in Microsoft Entra ID. This is the typical cause at initial rollout and after tenant-wide consent resets.
2. [Failed to obtain access token](failed-to-obtain-access-token.md)\
   The user's sign-in fails before a token is issued, usually because a Conditional Access policy (most often MFA) cannot be satisfied without a Primary Refresh Token (PRT) on the device.
3. [Failed to obtain access token to your OneDrive account](failed-to-obtain-access-token-to-your-onedrive-account.md)\
   The OneDrive-specific token request fails while other sign-ins succeed. Start by checking the interactive and non-interactive sign-in logs in Microsoft Entra ID for the affected user.

If none of these resolve the issue, prepare a [debug log](../debug-log-preparation.md) and open a support ticket.

### Related pages

* [Conditional Access](../../installation/security/conditional-access.md)
* [Debug log preparation](../debug-log-preparation.md)
