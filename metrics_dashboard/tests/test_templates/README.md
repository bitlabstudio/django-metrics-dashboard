This folder contains templates that we need in our tests but that are not part
of the app.

For example, one test checks if a view redirects to the login view. Therefore
we need the `login.html` template but it is not in the scope of this app to
provide such a template.
