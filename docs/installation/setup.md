# Setup

{% hint style="info" %}
It's recommended to restart your device following any installation or update.&#x20;
{% endhint %}

## Security

To setup KONNEKT you first have to meet the security requirements:

* admin consent
* conditional access config (if used)

Please see [here](security/) for details.

## Download current setup files

You can get the latest version of KONNEKT [here](https://trial.konnekt.io/).

If you want (as an admin) to grant tenant-wide consent for KONNEKT please visit [here ](security/grant-admin-consent-in-enterprise-applications.md)

## Interactive Installation

{% hint style="warning" %}
This KONNEKT setup requires local admin permissions.
{% endhint %}

You can install KONNEKT by running the MSI file interactively. The setup dialog will start:

<figure><img src="../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>

Click next.

<figure><img src="../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>

Accept the license terms and click next.

<figure><img src="../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>

You may then enter your license key.

{% hint style="info" %}
If you do not enter a license key, you start a 14 days trial version.
{% endhint %}

<figure><img src="../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>

KONNEKT is now ready to start the setup.

<figure><img src="../.gitbook/assets/image (72).png" alt=""><figcaption></figcaption></figure>

Click Finish to finalize the setup.

After the installation is successfully finished, a pop up window shows up automatically to connect your Microsoft 365 (formerly Office 365) account and grant the required permissions to create an Enterprise Application in your tenant (see screenshots below).

<figure><img src="../.gitbook/assets/image (73).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (74).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
To grant the permissions, you have to log in with an admin account or an account that has permissions to create an Enterprise Application in your tenant.

To grant the permissions tenant-wide please check [Grant tenant-wide admin consent](security/grant-admin-consent-in-enterprise-applications.md)&#x20;
{% endhint %}

## Silent Installation

If you want a silent installation without any user interface interaction you can use the following [msiexec](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/msiexec) command after downloading the msi installation file from [here ](https://trial.konnekt.io/)and rename it to `konnekt`:\
\
`msiexec /quiet /qn /norestart /i konnekt.msi LICENSE_KEY=<YourKey>`

Instead of the `<YourKey>` in the end, enter your license key.

{% hint style="info" %}
After the trial period, it is recommended to set the license key to machine level (HKLM).
{% endhint %}
