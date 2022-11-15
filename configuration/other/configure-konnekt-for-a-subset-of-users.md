# Disable KONNEKT for a subset of users

To disable KONNEKT for some users you just need to disable the initialization wizard of KONNEKT by setting the following registry key (as a`DWORD Value`) using your favorite policy or configuration management:

```
HKCU\Software\GlueckKanja\Konnekt\SkipAccountWizard -> 1 (DWORD)
```

{% hint style="warning" %}
Once you have installed KONNEKT on a machine, you must disable the Account Setup Wizard prior the first login of the user(s) to be effective.
{% endhint %}

Please see also [here](../../troubleshooting/subscribe-a-subset-of-users.md) for related information on this topic.
