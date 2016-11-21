Author: Wesley Nuzzo
____
Files in main folder:
(All files created by me)

knowledge_base.py defines the object used to store and analyze claims.
rule_base.py defines the abstract class used for defining the logic functions used with databases.
kb_tests.py contains the unit tests for knowledge_base.py and rule_base.py

numericalTT.py defines a subclass of the class in rule_base.py that treats numbers as truth tables for the purpose of logical deduction. This subclass is used by kb_tests.py

syllogism_rulebase defines a subclass of RuleBase that deals with syllogistic logic. This the files in the logic/ folder.

____
Files in logic/:
(These were also created by me, although parts of them -- particularly driver.py -- were based off the examples that came with PyKE)

NOTE: These files won't work unless PyKE has been downloaded and installed.

__init__.py is an empty file. This file is necessary for driver.py to be accessible to syllogism_rulebase.py

fc_syll.krb contains a definition of syllogistic logic in PyKE's forward-chaining syntax.
bc_syll.krb contains a definition of syllogistic logic in PyKE's backward-chaining syntax. This syntax seems to have several more limitations than the forward-chaining syntax, but its advantage is its ability to be used "on the fly".
syll.kfb contains a few claims that can be used to demonstrate PyKE's ability to draw conclusions based on the information it has.

driver.py creates a PyKE knowledge engine using the previous three files and defines a few functions that can be used to test that things are working.

