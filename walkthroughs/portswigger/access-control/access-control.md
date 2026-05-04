# Access control vulnerabilities and privilege escalation

## What is access control?
Access control is the application of constraints on who or what is authorized to perform action or access resources. In the context of web applications, access control is dependent on:
- **Authentication**
- **Session management**
- **Access control**

### Vertical access controls
Vertical access controls are mechanisms that restrict access to sensitive functionality to specific types of users.

### Horizontal access controls
Horizontal access controls are mechanisms that restrict access to resources to specific users.

### Context-dependent access controls
Context-dependent access controls restrict to functionality and resources based upon the state of the application or the user's interaction with it.

## Vertical privilege escalation
If a user can gain access to functionality that they are not permitted to access then this is vertical privilege escalation.

### Unprotected functionality
At its most basic, vertical privilege escalation arises where an application does not enforce any protection for sensitive functionality.

### Parameter-based access control methods
Some applications determine the user's access rights or role at login, and then store this information in a user-controllable location. This could be: 
- A hidden field.
- A cookie.
- A preset query string parameter.
The application makes access control decisions based on the submitted value.

### Broken access control resulting from platform misconfiguration

Some applications enforce access controls at the platform layer. they do this by restricting access to specific URLs and HTTP methods based on the user's role. 

### Broken access control resulting from URL-matching discrepancies

Websites can vary in how strictly they match the path of an incoming request to a defined endpoint.

## Horizontal privilege escalation
Horizontal privilege escalation occurs if a user is able to gain access to resources belonging to another user, instead of their own resources of that type.

## Horizontal to vertical privilege escalation

Often, a horizontal privilege escalation attack can be turned into a vertical privilege escalation, by compromising a more privileged user. 

For example, a horizontal escalation might allow an attacker to reset or capture the password belonging to another user. If the attacker targets an administrative user and compromises their account, then they can gain administrative access and so perform vertical privilege escalation. 

## Insecure direct object references (IDOR)

Insecure direct object references (IDORs) are a subcategory of access control vulnerabilities. IDORs occur if an application uses user-supplied input to access objects directly and an attacker can modify the input to obtain unauthorized access. 

## Access control vulnerabilities in multi-step processes

Many websites implement important functions over a series of steps. This is common when:
- A variety of inputs or options need to be captured.
- The user needs to review and confirm details before the action is performed.

## Location-based access control

Some websites enforce access controls based on the user's geographical location.

## How to prevent access control vulnerabilities

Access control vulnerabilities can be prevented by taking a defense-in-depth approach and applying the following principles:
- Never rely on obfuscation alone for access control.
- Unless a resource is intended to be publicly accessible, deny access by default.
- Wherever possible, use a single application-wide mechanism for enforcing access controls.
- At the code level, make it mandatory for developers to declare the access that is allowed for each resource, and deny access by default.
- Thoroughly audit and test access controls to ensure they work as designed.
