# Microsoft Graph API Python

### Create an application is Azure AD

1. Login to portal.azure.com
2. Navigate to Azure Active Directory
3. Create a new application. (Application Type: Native)
4. Copy the Application ID. This is your <strong>CLIENT_ID</strong> in <em>sample.py</em>.

### Enable Modern Authentication in Exchange Online

Refer: <https://support.office.com/en-gb/article/enable-or-disable-modern-authentication-in-exchange-online-58018196-f918-49cd-8238-56f57f38d662>

Set 

<pre>auto=True</pre> 
in line 22 to automatically open the browser and copy the code to the clipboard.

<strong><em>sample.py</em> lists all the user's calendar and creates an event in the user's default calendar.<strong>
  
Graph API Reference: <https://developer.microsoft.com/en-us/graph/docs/api-reference/beta/beta-overview>
