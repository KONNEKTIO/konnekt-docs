# Sites missing or folders empty

## Problem

Some sites are not shown in the KONNEKT node.\
or

Some folders of mapped sites/libraries are empty.

## Cause

Currently we see more and more error responses (e.g. 500) for proper requests to SharePoint Online Search. Sometimes the site discovery of KONNEKT is affected by this.&#x20;

In some cases/tenants, SharePoint Online does permanently fail to search at all. If this is the case, KONNEKT will not work properly.

## Check if your tenant is affected

You can check if your tenant is affected, by calling this site multiple times at different times at the day:

`https://<YourTenant>.sharepoint.com/_layouts/15/osssearchresults.aspx`

If you see a result like this frequently, please open a ticket at Microsoft:

![](<../../../.gitbook/assets/image (3).png>)

## Solution

We made KONNEKT more robust to failures of SharePoint Online Search. This applies to the following KONNEKT releases:

* 2.1.0 - 2.2.1
* 2.6.0 or newer

If the error responses happen **sometimes**, these builds may circumvent the problem.

{% hint style="warning" %}
If the error responses happen **frequently or permanently**, KONNEKT will not work properly, since KONNEKT relies on a proper availability of SharePoint Online.
{% endhint %}

## Similar Problems

Please also check this pages:&#x20;

[Some sites or libraries do not appear in KONNEKT](some-sites-or-libraries-do-not-appear-in-konnekt.md)

[Libraries are empty](../empty-libraries/libraries-are-empty.md)
