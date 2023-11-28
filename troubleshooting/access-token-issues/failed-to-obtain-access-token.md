# Failed to obtain access token

## Problem

When you are trying to log in to KONNEKT you get the error message "Failed to obtain access token".

## Cause

KONNEKT does not support having "Excluded Apps" in the Microsoft Entra ID (Azure AD) Conditional Access policy.

## Workaround

Please make sure to use a Conditional Access Policy without "Excluded Apps".

Please also see [Conditional Access configuration](../../installation/security/conditional-access.md).

## Solution

Not available, yet. We are working to support this scenario in a future release of KONNEKT.
