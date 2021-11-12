CHANGELOG 
==========

**as alunari**

0.0.1 (16/08/2021)
- initial release.

0.0.2 (16/08/2021)
- reupload for functionality.

0.0.3 (16/08/2021)
- README update.
- LICENSE update.
- stability downgrade to 4 - Beta in order to provide more testing and feedback.

0.0.4 (17/08/2021)
- minor README update.
- functionality confirmed in testing environment (Visual Studio Code, PyCharm, JupyterLab, Google Colab).

0.0.5 (23/08/2021)
-minor README update with Documentation link changed.

1.0.0 (28/08/2021)
- first stable release.
- major functionality changes.
- reworked 2 functions (.stats is now .get_stats, .risk is now .get_risk).
- added 1 new function (.get_change).
- .documentation updated.
- .montecarlo.functions updated.
- developement status is now 5 - Production/Stable.

1.0.1 (28/08/2021)
- small repository update.

1.0.2 (28/08/2021)
- LICENSE website change.
- updated information in the functions.

1.1.0 (30/08/2021)
- README update.
- alunariTools class created to distinguish logistics tools and functions from original montecarlo class.
- created a counter of iterations to track live progress.

1.1.1 (31/08/2021)
- now requires alunariTools in order to provide less confusing code, done outside of the original function.

1.1.2 (09/09/2021)
- confirmed functionality in Sublime Text.
- added __name__ == '__main__' info.
- minor README update.

1.1.3 (10/09/2021)
- redefined documentation.

1.1.4 (13/09/2021)
- improved user experience and stability.

1.1.5 (13/09/2021)
- typo corrections.

1.1.6 (19/09/2021)
- adjustments to montecarlo.execute() following the dependency changes of alunariTools package.
- stability and functionality confirmed in repl.it environment.

1.1.7 (19/09/2021)
- dependencies bug fix.

1.1.8 (19/09/2021)
- upload bug fix.

1.1.9+ (22/09/2021)
- merge test.

1.2.0 (22/09/2021)
- alunari and alunariTools are now merged into alunari. Former alunariTools functions are now called with alunari.essence.

1.2.1+ (24/09/2021)
- EOQ setup test.
- montecarlo class is now Configuration.

1.3.1 (25/09/2021)
- major rework and functionality update.
- code structure redifined.

1.3.2 (26/09/2021)
- code structure redifined.

1.3.3 (26/09/2021)
- cleaner and better defined code.
- partial imports from the library instead of whole modules applied.

1.3.4 (26/09/2021)
- minor bug fix.

1.3.5 (27/09/2021)
- alunari.montecarlo.Configuration().get_risk() now works independently with it's unique simulation counter that is set to 5000 by default.
- alunari.montecarlo.Configuration.help() updated to match the changes made to the function.

1.3.6 (27/09/2021)
- dependencies updated to meet repl.it requirements.

1.3.7 (29/09/2021)
- Configuration function now prints the confirmation of the simulation set up.

1.3.7+ (11/10/2021)
- redefined hist() function test.

**as vandal**

0.0.1 (03/10/2021)
- initial release.

0.0.2 (03/10/2021)
- vandal replaces the functionality of the currently discarded alunari python package.

1.1.0 (11/10/2021)
- redefined code of .hist() function.
- added event log that tracks the execution time and duration of functions.

1.1.1 (11/10/2021)
- log tracking now applies on all relevant class functions.

2.0.0 (11/10/2021)
- vandal transcedents alunari versions by becoming v2+

2.0.1 (12/10/2021)
- minor tweaks to CHANGELOG and README
- .help() now properly shows requirements of .get_logs() function.

2.0.2+ (12/10/2021)
- photo added to the header.

2.0.3 (12/10/2021)
- confirmed stabile version after test.

2.1.0 (12/10/2021)
- republished.

2.1.1 (13/10/2021)
- replaced alunari with vandal where it was initially missed out.
- now propely applies highly fragmented dataframe warning removal for simulations over 102.

2.1.2 (13/10/2021)
- stability update.

2.1.3 (22/10/2021)
- EOQ implementation.
- vandal.essence renamed to vandal.hub.
- this is an unstable version that has yet to be tested.

2.2.0 (22/10/2021)
- confirmed stability.

2.2.1 (22/10/2021)
- README and flexibility update.

2.2.2 (28/10/2021)
- now properly shows CHANGELOG of discarded alunari package.

2.2.3 (28/10/2021)
- discarded package.

2.2.4 (12/10/2021)
- due to multiple requests to make vandal alive, it now fetches the functionality of the newest duality package as a temporary solution.

2.2.5 (12/10/2021)
- dependency resolve.

2.2.6 (12/10/2021)
- README merge.