Description: Do not install box.py
 to /usr/bin as box is python module.
 /usr/bin/box.py is useless.
Author: Michal Arbet <michal.arbet@ultimum.io>
Forwarded: not-needed
Last-Update: 2020-03-31

diff --git a/setup.py b/setup.py
index 5eaef7b..3a76663 100644
--- a/setup.py
+++ b/setup.py
@@ -29,7 +29,7 @@ setup(
     author_email='chris@cdgriffith.com',
     description='Advanced Python dictionaries with dot notation access',
     long_description=long_description,
-    scripts=['box.py'],
+    #scripts=['box.py'],
     py_modules=['box'],
     include_package_data=True,
     platforms='any',
