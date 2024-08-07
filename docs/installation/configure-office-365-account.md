# Configure Office 365 account

KONNEKT leverages the user's account in Microsoft Entra ID (Azure AD) to access SharePoint Online.

## Single Sign On (SSO)

If your system is configured for single sign-on (SSO) with Microsoft Entra ID (Azure AD), KONNEKT will automatically set up your account.

## Manual Account Configuration

If your system is not configured for single sign-on (SSO) with Microsoft Entra ID (Azure AD), KONNEKT will open a dialog, to set up the Office 365 / Microsoft Entra ID (Azure AD) account:

![](<../.gitbook/assets/2022-08-02 15\_21\_56-Window.png>)

Click on "Connect your Office 365 Account".

KONNEKT will open the Microsoft Entra ID (Azure AD) sign-in page:

![](<../.gitbook/assets/2022-08-02 15\_22\_32-Window.png>)

Sign in with your Microsoft Entra ID (Azure AD) account.

## Autologin Mapping

After the successful setup of the Office 365 account, KONNEKT will start to search for SharePoint Online sites in the corresponding tenant, which the user has access to. KONNEKT will automatically map the default document libraries of those sites in the Windows File Explorer.

![](<../.gitbook/assets/2022-08-02 15\_24\_34-Window.png>)

If needed, libraries can be mapped to a specific driver letter (see [Assign drive letter to a KONNEKT folder](../configuration/mappings/assign-drive-letters.md)).

If additional SharePoint Online environments are to be accessed under other Azure Active Directory identities/tenants.

## Multi-Tenant Configuration

With KONNEKT it is possible to work with multiple tenants simultaneously. Just open the Windows Explorer with KONNEKT selected on the left pane and right-click on **Accounts**

<figure><img src="../.gitbook/assets/aadaccount.png" alt=""><figcaption></figcaption></figure>

Log in with the account for the tenant you want to add.

