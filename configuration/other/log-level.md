# Log level

You can find this setting in the preferences menu:

![](<../../.gitbook/assets/image (19).png>)

You can also configure this setting via registry/GPO/MDM:

Key name: **LogLevel**\
****Key type: **REG\_DWORD**.&#x20;

Controls the KONNEKT client log level. \
You can find the KONNEKT client logs in `%LocalAppData%\konnekt`

| Log Level | Value |
| :-------: | :---: |
|    Off    |   0   |
|   Error   |   1   |
|    Info   |   2   |
|   Debug   |   3   |

Default Log level value is 2 (Info Level).

We recommend using our [ADMX template](../management-options/settings-via-gpo.md#admx-file) to configure this setting.
