# Setup

## Download current setup files

You can get the latest version of KONNEKT [here](https://trial.konnekt.io/).

If you want (as an admin) to grant tenant-wide consent for KONNEKT please visit [here ](grant-admin-consent-in-enterprise-applications.md)

## Interactive Installation

{% hint style="warning" %}
KONNEKT setup requires local admin permissions&#x20;
{% endhint %}

You can install KONNEKT by running the MSI file interactively. The setup dialog will start:

![](<../.gitbook/assets/2022-08-02 15\_18\_53-Window.png>)

Click next.

![](<../.gitbook/assets/2022-08-02 15\_19\_21-Window.png>)

Accept the license terms and click next.

![](<../.gitbook/assets/2022-08-02 15\_19\_47-Window.png>)

You may then enter your license key.

{% hint style="info" %}
If you do not enter a license key, you start a 14 days trial version.
{% endhint %}

![](<../.gitbook/assets/2022-08-02 15\_20\_34-Window.png>)

KONNEKT is now ready to start the setup.

![](<../.gitbook/assets/2022-08-02 15\_21\_06-Window.png>)

Click Finish to finalize the setup.



## Silent Installation

If you want a silent installation without any user interface interaction you can use the following command after downloading the msi installation file from [here ](https://trial.konnekt.io/)and rename it to `konnekt`:\
\
`msiexec /quiet /qn /norestart /i konnekt.msi LICENSE_KEY=<YourKey>`

Instead of the `<YourKey>` at the end, enter your license key.
