# Security

This section covers the permissions KONNEKT requires in your Microsoft 365 environment and how it interacts with Conditional Access policies. Use the checklist below before KONNEKT goes into production.

## Checklist for security teams

| Check | Why | Details |
|---|---|---|
| Grant tenant-wide admin consent | Without consent, users can't sign in, and KONNEKT isn't covered by "All cloud apps" | [Grant tenant-wide admin consent](grant-admin-consent-in-enterprise-applications.md) |
| Target Conditional Access policies at "All cloud apps" | KONNEKT calls several Microsoft APIs. Policies scoped to single apps miss some of them | [Conditional Access](conditional-access.md) |
| Exclude `Konnekt.exe` and `KonnektStarter.exe` from the attack surface reduction rule that blocks Office apps from creating child processes | Without the exclusion, KONNEKT crashes when opening or previewing Office files | [Risky action blocked](../../troubleshooting/risky-action-blocked.md) |
| Exclude KONNEKT drive letters and processes from real-time and full antivirus scans | Every scanned file is a SharePoint download. A full scan can get the tenant throttled | [Slow performance or errors caused by antivirus scanning](../../troubleshooting/slow-performance-or-errors-caused-by-antivirus-scanning.md) |
| Allow the KONNEKT and Microsoft 365 endpoints | Sign-in, file access and the license check need them | [System requirements](../system-requirements.md#firewall-and-network-settings) |

## In this section

{% content-ref url="grant-admin-consent-in-enterprise-applications.md" %}
[grant-admin-consent-in-enterprise-applications.md](grant-admin-consent-in-enterprise-applications.md)
{% endcontent-ref %}

{% content-ref url="conditional-access.md" %}
[conditional-access.md](conditional-access.md)
{% endcontent-ref %}

## Related pages

- [System requirements](../system-requirements.md)
- [Deployment](../README.md)
