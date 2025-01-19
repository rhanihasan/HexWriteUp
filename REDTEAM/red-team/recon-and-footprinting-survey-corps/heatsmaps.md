# HeatsMaps

### Heat Map (Uploads)

* Integrate 3th party
  * &#x20;XSS
* Self Uploads
  * XML Based (Docx , PDF)
    * SSRF,XSS,XXE
  * Images
    * XSS, Shell
      * Name
      * Binary Header
      * Metadara
  * Where its data stored

### Heat Map (Content Types)

"When checking proxy data, pay attention to requests or responses with multipart-form, XML, or JSON data. These can contain important information and deserve a closer look."

* Content Types
  * Look for Mutipart-forms
    * Shell Injections and more...
  * Look for Content Type XML
    * XXE
  * Look for Content Type JSON
    * API Vulnerabilities
      * Hidden Methods
      * Lack of authentication

### Heat Map (Account Section)



When testing an app, the part that needs you to sign in often lets you see and manage your personal information. In my case, this is where a lot of data gets saved or kept, making it a good target for stored XSS attacks. Also, the account area is where you can add new features that let the app connect to other apps. These connections can have different security risks. Additionally, there's a chance to put in a "blind XSS payload" in your profile or account area, which isn't immediately obvious.



<table><thead><tr><th width="160">Subsection</th><th width="292">Vulnerabilities</th><th>Testing Focus Areas</th></tr></thead><tbody><tr><td><strong>Profile</strong></td><td>Stored XSS</td><td>Input validation on profile fields, test for script injection.</td></tr><tr><td></td><td></td><td>Review profile image upload for potential image-based vulnerabilities.</td></tr><tr><td><strong>App Custom Fields</strong></td><td>Stored XSS, Server-Side Template Injection (SSTI)</td><td>Test for injection in custom field inputs, especially those rendered in HTML or templates.</td></tr><tr><td><strong>Integrations</strong></td><td>Server-Side Request Forgery (SSRF)</td><td>Test integration endpoints for SSRF vulnerabilities, validate URL parsing and handling.</td></tr><tr><td></td><td>Cross-Site Scripting (XSS)</td><td>Check for XSS vulnerabilities in integration input fields and callbacks.</td></tr><tr><td><strong>Additional Tips</strong></td><td>Blind XSS Payloads</td><td>Consider adding blind XSS payloads in user profiles and monitor for any execution signals.</td></tr><tr><td></td><td></td><td>Investigate the interaction between integrated applications for potential security issues.</td></tr></tbody></table>

#### Testing Focus Areas:

1. **Stored XSS (Cross-Site Scripting):**
   * Perform thorough input validation testing on user profile fields.
   * Check for HTML, JavaScript, and image-based injection points in profile settings.
2. **Server-Side Template Injection (SSTI):**
   * Examine custom fields and templates for potential SSTI vulnerabilities.
   * Input crafted payloads to assess if there's any server-side template processing.
3. **Server-Side Request Forgery (SSRF):**
   * Test integration endpoints for SSRF vulnerabilities by manipulating URLs.
   * Ensure proper URL validation and parsing in integration features.
4. **Cross-Site Scripting (XSS):**
   * Evaluate input fields and callback mechanisms in integration settings.
   * Check for potential XSS issues that could arise from interaction with integrated applications.
5. **Blind XSS Payloads:**
   * Embed blind XSS payloads in user profiles or account settings.
   * Monitor external systems for any signs of payload execution.
6. **Integration Security:**
   * Investigate the security of integrated applications and their communication channels.
   * Look for potential authentication bypass or sensitive data exposure in the integration features.



###



### Heat Map: Errors

When dealing with errors in an application, security testers can leverage the occurrence of errors as indicators of potential vulnerabilities. By analyzing error messages and their triggers, testers can identify areas prone to exotic injections, application-level denial-of-service (App DOS), and other security issues.

| Area                  | Potential Vulnerabilities   | Testing Focus Areas                                  |
| --------------------- | --------------------------- | ---------------------------------------------------- |
| **Errors**            | Exotic Injections, App DOS  | Use interception proxies to analyze error responses. |
|                       |                             | Trigger errors intentionally to identify patterns.   |
| **Exotic Injections** | Real Injection Exploitation | Play with error-triggering inputs in Burp Intruder.  |
|                       |                             | Explore possibilities of injection-based exploits.   |
| **App DOS**           | Application-Level DOS       | Manipulate inputs to cause application-level errors. |
|                       |                             | Assess the impact of intentional denial-of-service.  |

### Heat Map: Passing Paths (URLs)

When applications pass paths or URLs as part of parameters or in routes, it introduces the potential for vulnerabilities related to URL parsing. Security testers can focus on identifying Server-Side Request Forgery (SSRF) and Redirect vulnerabilities.

| Area                               | Potential Vulnerabilities | Testing Focus Areas                               |
| ---------------------------------- | ------------------------- | ------------------------------------------------- |
| **Paths or URLs Passed as Values** | SSRF, Redirects           | Analyze how the application parses and uses URLs. |
|                                    |                           | Test for SSRF by manipulating URL parameters.     |
|                                    |                           | Check for security of URL redirection mechanisms. |

### Heat Map: Help Chatbots

Chatbots designed to assist users with customer service can be potential targets for security testing. Blind Cross-Site Scripting (XSS) vulnerabilities may arise due to misconfigurations or coding issues in these chatbots.



| Area              | Potential Vulnerabilities | Testing Focus Areas                                        |
| ----------------- | ------------------------- | ---------------------------------------------------------- |
| **Help Chatbots** | Blind XSS                 | Test for misconfigurations or coding issues in chatbot.    |
|                   |                           | Attempt blind XSS attacks by interacting with the chatbot. |

### Heat Map: AI Chatbots

As companies introduce AI-enabled chatbots, a new avenue for offensive security emerges. Security testers can explore prompt injection techniques to uncover potential data leakage through these AI chatbots.

| Area            | Potential Vulnerabilities | Testing Focus Areas                                                |
| --------------- | ------------------------- | ------------------------------------------------------------------ |
| **AI Chatbots** | Prompt Injection          | Investigate if AI chatbots are susceptible to prompt injection.    |
|                 |                           | Attempt to smuggle out sensitive data through prompt manipulation. |





## Web Fuzzing (SSWLR) - Interpreting Results:

1. **SENSITIVE (Status Code):**
   * Check the HTTP status codes returned for each request.
   * Focus on any unexpected or sensitive status codes (e.g., 200 OK, 403 Forbidden, 500 Internal Server Error).
2. **SECRETS (Size):**
   * Analyze the size of the responses.
   * Look for variations in response sizes, as anomalies may indicate potential issues.
   * Pay attention to unusually large or small responses.
3. **WERE (Word Count):**
   * Count the number of words in the responses.
   * Identify responses with a high or low word count, as this might reveal unexpected content.
4. **LEAKED (Lines):**
   * Count the number of lines in each response.
   * Focus on responses with a large number of lines, as they may indicate excessive information disclosure.
5. **RECENTLY (Response Times):**
   * Evaluate the response times for each request.
   * Look for responses that take significantly longer or shorter times, as this may point to potential vulnerabilities.

#### Example Command (Assuming you're using a tool like wfuzz):

```bash
wfuzz -c -z file,big_wordlist.txt -u "https://example.com/FUZZ" -H "Authorization: Bearer YOUR_TOKEN" --hl 50 --hw 100
```

In this example, `big_wordlist.txt` is your wordlist of payloads, and `https://example.com/FUZZ` is the target URL with the FUZZ placeholder. The `-c` option shows the output in color. The `-H` option adds a custom header for authentication. `--hl` and `--hw` filter responses based on line count.

These considerations can help you interpret the results of your web fuzzing and identify potential vulnerabilities in terms of sensitivity, secrets, leaks, and response times. Adjust the parameters based on your specific testing requirements and the tool you are using.

