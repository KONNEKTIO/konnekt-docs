# Deployment

This section takes IT admins from download to working drive letters: grant consent, install the MSI, push policies, and let users sign in. Each step links to the page with the full detail.

## Before you start

- Local administrator rights on the target devices
- An administrator who can grant tenant-wide admin consent in Microsoft Entra ID
- A KONNEKT license key. Without one, KONNEKT installs as an evaluation version
- A decision on how you deliver policies: Group Policy, Microsoft Intune, or the registry

Check the [System requirements](system-requirements.md) first.

## Step 1: Grant admin consent

An administrator approves KONNEKT for the tenant once, before the first user signs in. KONNEKT uses delegated permissions only, so it never acts without a signed-in user. For the consent URL and the permission set, see [Grant tenant-wide admin consent](security/grant-admin-consent-in-enterprise-applications.md).

## Step 2: Install the MSI

KONNEKT ships as one MSI per processor platform: x64, x86 and ARM64. On ARM64 devices, use the ARM64 package.

Distribute the MSI through Microsoft Intune as a Win32 app, or through your software distribution. The silent install command is:

```
msiexec /i konnekt.msi /quiet /qn /norestart LICENSE_KEY=<your-license-key>
```

{% hint style="warning" %}
KONNEKT installs a kernel-mode driver, so the device needs a restart before KONNEKT works. Restart, don't shut down: with Fast Startup enabled, a shutdown can leave the driver update unfinished.
{% endhint %}

For the interactive installer, see [Setup](setup.md).

## Step 3: Push policies

Every KONNEKT policy exists for computers and for users. Computer policies win over user policies. Group Policy and Microsoft Intune use the same ADMX template, so the policies, their names and their options are identical in both.

| Channel | How |
|---|---|
| Group Policy | Copy `Konnekt.admx` and `en-US\Konnekt.adml` into your PolicyDefinitions store. See [Settings via GPO](../configuration/management-options/settings-via-gpo.md) |
| Microsoft Intune | Import `Konnekt.admx` and `Konnekt.adml` as imported administrative templates. See [Settings for Intune-managed devices](../configuration/management-options/setting-for-intune-managed-devices/README.md) |

For every setting and its registry value, see [Management options](../configuration/management-options/README.md).

### Fallback: OMA-URI and registry

Use these only where the ADMX template can't be used:

- **Custom OMA-URI profiles in Intune**, for tenants that don't use imported administrative templates. See [Settings for Intune-managed devices (Legacy)](../configuration/management-options/setting-for-intune-managed-devices-1/README.md).
- **Registry values written by a script**, for Windows multi-session hosts and for the few settings that have no ADMX policy. See [Deploy on session hosts and VDI](deploy-on-session-hosts-and-vdi.md).

## Step 4: Users sign in

On Microsoft Entra joined devices, KONNEKT creates the first account from the Windows sign-in, silently where single sign-on allows it. Site discovery then takes one to three minutes, after which the drives appear.

To have users sign in themselves instead, see [Skip Account Wizard](../configuration/system-settings/configure-konnekt-for-a-subset-of-users.md).

## In this section

{% content-ref url="system-requirements.md" %}
[system-requirements.md](system-requirements.md)
{% endcontent-ref %}

{% content-ref url="setup.md" %}
[setup.md](setup.md)
{% endcontent-ref %}

{% content-ref url="configure-office-365-account.md" %}
[configure-office-365-account.md](configure-office-365-account.md)
{% endcontent-ref %}

{% content-ref url="deploy-on-session-hosts-and-vdi.md" %}
[deploy-on-session-hosts-and-vdi.md](deploy-on-session-hosts-and-vdi.md)
{% endcontent-ref %}

{% content-ref url="software-updates.md" %}
[software-updates.md](software-updates.md)
{% endcontent-ref %}

## Related pages

- [Security](security/README.md)
- [Management options](../configuration/management-options/README.md)
- [Managed mappings](../configuration/mappings/managed-mappings.md)
