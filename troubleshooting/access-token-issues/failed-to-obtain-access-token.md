# Failed to obtain access token

## Problem

When you are trying to log in to KONNEKT you get the error message "Failed to obtain access token".

## Cause

KONNEKT does not support having "Excluded Apps" in a MFA-requiring Microsoft Entra (Azure AD) Conditional Access policy in combination with a non-SSO Windows session.

## Workaround

Our recommended workaround is to enable the Windows machine for holding a Primary Refresh Token (PRT) e.g. by Entra Join (AAD Join) or Register. Please see [here ](https://learn.microsoft.com/en-us/entra/identity/devices/concept-primary-refresh-token#how-is-a-prt-issued)for details.

Other alternatives are (not really recommended):

* Remove MFA requirement from the corresponding Conditional Access Policy. To keep some security for CA policies without MFA, you could enforce [Trusted Locations (e.g. public IP addresses of your VDI hosts)](https://learn.microsoft.com/en-us/entra/identity/conditional-access/location-condition)

or

* use a Conditional Access Policy without "Excluded Apps". Please also see [Conditional Access configuration](../../installation/security/conditional-access.md).

## Solution

Not available, yet. We are working to support this scenario in a future release of KONNEKT.
