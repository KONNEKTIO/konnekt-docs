# Some sites or libraries do not appear in KONNEKT

### Problem

SharePoint Online sites or libraries which should be mapped via auto mapping do not appear in KONNEKT.

### Background

KONNEKT runs a search on SharePoint Online to discover sites & libraries. To find libraries here, the user must be a member of the site.&#x20;

In some cases, users may be owners of a site, but not members. This results in not discovered sites or libraries.

### Solution

Ensure, that owners of sites are also members. See [here](https://docs.microsoft.com/en-us/sharepoint/troubleshoot/search/search-results-dont-appear-for-group-owners) for more details.
