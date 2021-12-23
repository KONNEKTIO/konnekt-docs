# Licensing

{% hint style="success" %}
The subscription for KONNEKT is **user-based**.&#x20;
{% endhint %}

## User definition

The licensing is per seat, which means that the subscription of a "user" is required for each user (UPN), who is using KONNEKT to log into OneDrive for Business or SharePoint online.

A user subscription is bound to the using UPN and cannot be shared with other UPNs. The assignment of a user subscription to a UPN is detached and can be rebound to another UPN after KONNEKT has not been used for a calendar-month with the already issued UPN.

{% hint style="info" %}
In many cases the required amount of KONNEKT subscriptions equals the amount of Microsoft Office 365 / OneDrive for Business / SharePoint Online subscriptions.
{% endhint %}

## Device limits per user

A single user may have up to 5 Windows devices or terminal sessions (e.g. Citrix XenApp).

## Subscription scope

The subscription of KONNEKT may be used for the users of one organization. Users from this one organization may access multiple Microsoft 365 tenants with KONNEKT.

It is **not** allowed to&#x20;

* use one KONNEKT subscription for users from multiple organizations,
* split one KONNEKT subscription and/or re-sell it to multiple organizations.



## Azure Marketplace

### Pricing Model

* KONNEKT is offered as an **annual subscription plan** with different [User Segments](licensing.md#user-segments). The correct **user segment** is automatically selected by our platform based on the amount of desired users.
* The annual subscription plan consists of a **base fee** which includes a certain amount of users per year - depending on the **user segment**. For example, the **base fee** for the user segment _KONNEKT 25_ includes 25 users per year.
* If more than the included amount of users is required, **additional users** can be added to the  plan. For each additional user, we charge an additional annual per-user fee.
* The logic on our platform will always choose the cheapest user segment based on your desired amount of total users. For example, if you require 300 users, we will charge you based on the user segment _KONNEKT 250_. This includes the __ base fee for 250 users plus 50 additional users in the user segment _KONNEKT 250_.
* You will be prompted for your desired total user count on our platform during the subscription enrolment process.
* Upon initial subscription enrolment or during an intermediate subscription upgrade, our platform will inform you about the billing items we will report to Microsoft as well as the associated licensing costs in _your_ currency.

{% hint style="warning" %}
For CSP deals we cannot display the licensing costs as CSP margins might be in place.
{% endhint %}

### Invoicing

* During the first subscription interval, your subscription fees are not immediately due after completing the subscription enrolment. Instead we will report them to Microsoft after your cancellation grace period has expired.&#x20;
* Upon every renewal date, we will report your fees to Microsoft immediately.
* The related items should appear on your Microsoft Azure invoice (Pay-As-You-Go) the month after we have reported your fees to Microsoft.

{% hint style="info" %}
Both (if applicable), the base fee as well as the additional users fee will appear as separate items on your Microsoft Azure invoice.
{% endhint %}

### Plan Overview

Subscriptions for KONNEKT are available based on an annual renewal interval.

| **Plan** | **Renewal Interval** |
| -------- | -------------------- |
| KONNEKT  | Annually             |

#### User Segments

The following user segments are available.

| **User Segment** | **Included Users in Base Fee** | **Maximum Total User** |
| ---------------- | ------------------------------ | ---------------------- |
| KONNEKT 25       | 25                             | 249                    |
| KONNEKT 250      | 250                            | 999                    |
| KONNEKT 1000     | 1,000                          | 4,999                  |
| KONNEKT 5000     | 5,000                          | 9,999                  |
| KONNEKT 10000    | 10,000                         | unlimited              |

For prices in Euro (EUR), please check out our <mark style="color:green;"></mark> [website](https://www.konnekt.io). For prices in _your_ currency, please directly refer to the Azure Marketplace in the [Azure Portal](https://portal.azure.com).

### User Up- and Downgrades

#### Upgrades

* If you would like to upgrade your user count, you can do that any time during the current subscription cycle by navigating to your **KONNEKT subscription** in the [Azure SaaS portal](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.SaaS%2Fresources) <mark style="color:green;"></mark> and by clicking on "Open SaaS Account on publisher's site" (see screenshot below). This will re-direct you to our landing page where the amount of users can be upgraded.
* In case the upgrade occurs within the current subscription interval, only the prorated amount of fees incurred by the additional users will be reported to Microsoft for this interval.
* Our landing page will inform you about the new fees for a **complete** subscription cycle.
* After confirming your choice and once we have updated the license in our backend, you will receive a confirmation email from us.

![](.gitbook/assets/SaaSPortal\_changeSubscription.png)

#### Downgrades

* Downgrading the amount of users is currently not possible without cancelling the subscription.
* If you want to perform a downgrade, please cancel your current subscription from the <mark style="color:green;"></mark> [Azure SaaS portal](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.SaaS%2Fresources) towards the end of the current cycle by clicking "Cancel subscription" (see screenshot below) and re-subscribe with the desired user amount once the cancellation becomes effective.
* Please do not forget to update the license key in your KONNEKT installation(s) afterwards as described in [here](https://docs.konnekt.io/configuration/other/license-key-on-multi-user-environments).

![](.gitbook/assets/SaaSPortal\_cancelSubscription.png)

### **Trials**

By default, when you purchase a plan from the Azure Marketplace, we will apply a 30-day trial period, for which we will not charge any subscription fees.&#x20;

This applies only to those customers who have never had a trial period before.

#### **Custom Trials**

In case you have special requirements or constraints that require more than 30 days of testing period, please [get in contact with us](https://www.konnekt.io/start-now/#try) directly or send us an email to [sales@konnekt.io](mailto:sales@konnekt.io) for an individual trial offer.

### How to Get Started

To get started with your KONNEKT subscription,

* Locate KONNEKT on the **Marketplace** in your [**Azure Portal**](https://portal.azure.com/#create/glueckkanja-gabag.radiusaas-transactable-prod/preview).&#x20;

![](<.gitbook/assets/image (29).png>)

* Click "Set up + subscribe". The annual plan for KONNEKT is already pre-selected. We recommend to keep **Recurring billing** **on** so that you do not have to worry about a manual renewal of your subscription. Click "Review + subscribe" to deploy the subscription to your Azure SaaS.

![](<.gitbook/assets/image (30).png>)

{% hint style="info" %}
The random order of **Base Fees** und **Additional Users** under the **Price** information is attributed to limitations of the Azure Marketplace. Later during the the enrolment process, we will provide you with transparent information on the expected licensing costs.
{% endhint %}

* Once you have successfully deployed the SaaS subscription into your Azure SaaS portal, please navigate to our subscription landing page by clicking "Configure account now"

{% hint style="info" %}
You will only be charged by Microsoft, once you have completed the enrolment on our landing page. Until then the subscription will remain in status "Fulfillment pending".
{% endhint %}

* After authenticating on our landing page using your Microsoft credentials, you will be prompted for additional information, such as the desired User amount
* Based on the amount of users provided on our landing page, we will charge the relevant base fee for your user segment as well as additional users, in case you require more than the included amount in your base fee.
* The landing page will show you the licensing fees you have to expect
* If you are happy with it, please complete the enrolment, which triggers us to generate a **KONNEKT license key**. You will receive this key as part of our welcome email including all relevant information on the next steps regarding the installation of KONNEKT. This won't take any longer than one business day.
