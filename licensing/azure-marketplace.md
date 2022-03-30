# Azure Marketplace

## Pricing Model

* KONNEKT is offered as an **annual subscription plan** with different [User Segments](azure-marketplace.md#user-segments). The correct **user segment** is automatically selected by our platform based on the amount of desired users.
* The annual subscription plan consists of a **base fee** which includes a certain amount of users per year - depending on the **user segment**. For example, the **base fee** for the user segment _KONNEKT 25_ includes 25 users per year.
* If more than the included amount of users is required, **additional users** can be added to the  plan. For each additional user, we charge an additional annual per-user fee.

## Invoicing

* During the first subscription interval, your subscription fees are not immediately due after completing the subscription enrolment. Instead we will start billing once your cancellation grace period has expired.&#x20;
* Upon every renewal date, you will be billed immediately.
* The related items should appear on your Microsoft Azure invoice (Pay-As-You-Go) the month after we have reported your fees to Microsoft.
* In the PDF invoice you will receive from Microsoft, all SCEPman fees are lumped into an item called "SaaS". The related Publisher is "glueckkanja-gab".

![](<../.gitbook/assets/Screenshot 2022-02-18 at 12.39.15.png>)

{% hint style="info" %}
For a more detailed cost breakdown of your base and additional user fees, please refer to the invoice in your Azure portal.
{% endhint %}

## Plan Overview

Subscriptions for KONNEKT are available based on an annual renewal interval.

| **Plan** | **Renewal Interval** |
| -------- | -------------------- |
| KONNEKT  | Annually             |

### User Segments

The following user segments are available.

| **User Segment** | **Included Users in Base Fee** | **Maximum Total Users** |
| ---------------- | ------------------------------ | ----------------------- |
| KONNEKT 25       | 25                             | 249                     |
| KONNEKT 250      | 250                            | 999                     |
| KONNEKT 1000     | 1,000                          | 4,999                   |
| KONNEKT 5000     | 5,000                          | 9,999                   |
| KONNEKT 10000    | 10,000                         | unlimited               |

For prices in Euro (EUR), please check out our <mark style="color:green;"></mark> [website](https://www.konnekt.io/pricing/). For prices in _your_ currency, please directly refer to the **Marketplace** in the [Azure Portal](https://portal.azure.com).

## User Up- and Downgrades

### Upgrades

* If you would like to upgrade your user count, you can do that any time during the current subscription cycle by navigating to your **KONNEKT subscription** in the [Azure SaaS portal](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.SaaS%2Fresources) <mark style="color:green;"></mark> and by clicking "Open SaaS Account on publisher's site" (see screenshot below). This will re-direct you to our platform where the amount of users can be upgraded.

![](<../.gitbook/assets/Screenshot 2022-02-21 at 16.43.07 2.png>)

* Our platform will inform you about the new fees you to expect for a **complete** subscription cycle.
* For the current cycle, we will bill the additional users for remaining days only.
* After confirming your choice and once we have updated the license in our backend, you will receive a confirmation email from us.

### Downgrades

* Downgrading the amount of users is currently not possible without cancelling the subscription.
* If you want to perform a downgrade, please cancel your current subscription from the <mark style="color:green;"></mark> [Azure SaaS portal](https://portal.azure.com/#blade/HubsExtension/BrowseResourceBlade/resourceType/Microsoft.SaaS%2Fresources) towards the end of the current cycle by clicking "Cancel subscription" (see screenshot below) and re-subscribe with the desired user amount once the cancellation becomes effective.

![](<../.gitbook/assets/Screenshot 2022-02-21 at 16.43.07 3.png>)

* Please do not forget to update the license key in your KONNEKT installation(s) afterwards as described in [here](https://docs.konnekt.io/configuration/other/license-key-on-multi-user-environments).

## Trials

In case you would like to test KONNEKT, please [get in contact with us](https://www.konnekt.io/start-now/#try) or send us an email to [sales@konnekt.io](mailto:sales@konnekt.io).

## How to purchase KONNEKT?

To get started with your KONNEKT subscription,

* Locate KONNEKT on the **Marketplace** in your [**Azure Portal**](https://portal.azure.com/#create/glueckkanja-gabag.radiusaas-transactable-prod/preview).&#x20;
* Click "Subscribe"

![](<../.gitbook/assets/image (31).png>)

* Create or select the **Resource group** you would like to deploy the subscription to
* Assign a **Name** to later identify your SCEPman subscription
* We recommend to keep **Recurring billing** on **** so that you do not have to worry about a manual renewal of your subscription.
* Click "Review + subscribe" and in the next blade "Subscribe" to deploy the subscription to your Azure SaaS portal.

![](<../.gitbook/assets/image (30) (1).png>)

{% hint style="info" %}
The random order of **Base Fees** und **Additional Users** under the **Price** information is attributed to limitations of the Azure Marketplace. Later during the the enrolment process, we will provide you with transparent information on the expected licensing costs.
{% endhint %}

* Once the deployment is complete, please navigate to our platform by clicking "Configure account now"

![](<../.gitbook/assets/image (25) (1).png>)

* After authenticating on our platform using your Microsoft credentials, you will be prompted for additional information, such as the desired **total user amount** and a **technical admin contact**.

![](../.gitbook/assets/Screenshot\_2022-02-21\_at\_16\_38\_12.png)

* Based on the amount of users provided on our platform, we will charge the relevant base fee for your user segment as well as additional users, in case you require more than the included amount in your base fee.
* The platform will show you the licensing fees you have to expect under **Cost Projection**.

{% hint style="warning" %}
For CSP deals we cannot display the Cost Projection as CSP margins might be in place.
{% endhint %}

* If you are happy with it, please complete the enrolment by clicking S**ubmit**, which triggers us to generate a license key for KONNEKT. You will receive this key as part of our welcome email including all relevant information on the next steps (e.g. how to install KONNEKT on your clients). This won't take any longer than one business day.

{% hint style="info" %}
You will only be charged by Microsoft, once you have completed the enrolment on our landing page and received our welcome email.
{% endhint %}
