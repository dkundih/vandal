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
- minor README update with Documentation link changed.

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

**as duality**

3.0.0 (03/11/2021)
- initial release
- now properly shows CHANGELOG of vandal package history.

3.0.1 (04/11/2021)
- code tweaks.

3.1.1 (06/11/2021)
- MonteCarlo and EOQ now automatically perform .execute() function.
- MonteCarlo.hist() now executes get_stats() alongside to get info about standard deviation.
- MonteCarlo and EOQ are now being imported as objects.
- global_functions removed and merged into meta folder.

3.1.1+ (06/11/2021)
- functionality tests.

3.1.2 (06/11/2021)
- complete redesign pushed to public.

3.1.3 (06/11/2021)
- initial import now imports hub module as well as associated contents in order to enable print(help(duality.hub)) function.

3.1.4 (07/11/2021)
- updated README.

3.1.5 (08/11/2021)
- untracked changes.

3.1.6 (12/11/2021) - not usable.
- code cleanup in hub and montecarlo modules.

3.1.7 (12/11/2021)
- quick bug fix.

3.1.8 (12/11/2021)
- sync with recent GitHub changes.

3.1.9 (13/11/2021)
- README style update.

3.2.0 (13/11/2021)
- return_data = True added into MonteCarlo object for decision of the time of execution manually.

3.2.1 (14/11/2021)
- setup.py redefined with metadata.

3.2.2 (17/11/2021)
- regular maintainance.

3.3.0 (19/11/2021) - UNSTABLE
- package now becomes a library.
- DEVELOPER MODE introduced.
- disables @classlog functions outside of DEVELOPER MODE.
- code readability improved.
- duality.hub.hub is now duality.hub.toolkit.
- eoq and montecarlo folders merged into objects folder.
- added support for import __all__ contents of a module.

3.3.2 (19/11/2021) - UNSTABLE
- republish and 3.3.1 ghost overwrite.

3.3.3 (20/11/2021) - UNSTABLE
- initial bug fix deployed.

3.3.4 (20/11/2021) - UNSTABLE
- additional bug fixes deployed.

3.3.5 (20/11/2021) - UNSTABLE
- additional bug fixes deployed.
- code readability improved.

3.3.6 (20/11/2021)
- confirmed functionality and stability.

3.3.7 (20/11/2021)
- code reconstruction.

3.4.0 (22/11/2021)
- NEW FEATURE: duality.Dijkstra algorithm.

3.4.1 (22/11/2021)
- minor code cleanup.

3.4.2 (22/11/2021)
- functionality confirmed.

3.4.3 (22/11/2021)
- upstream/downstream fix.

3.4.4 (01/12/2021)
- CLI environment setup.

3.5.0 (01/12/2021)
- CLI environment tests.
- demonstration repository now merged into duality.
- MonteCarlo, Dijsktra and EOQ no longer define the data, data config shifted to .execute() function of every object.
- CLI can now be executed in teminal using 'duality.__main__' for IDE or 'python __main__.py' for CMD or Powershell after locating with cd.
- stability of 3.5. series will not be guaranteed, it is a transitional phase for future integrations into applications and web applications.

3.5.1 (01/12/2021)
- CLI environment tests.
- code readablity improved.

3.5.2 (01/12/2021)
- CLI environment tests.
- dualityCLI integration into the source.
- CLI contents added into __all__ and __init__ files.

3.5.3 (01/12/2021) - UNSTABLE
- first functional CLI for MonteCarlo imlpemented.
- added saving to .csv, .xlsx and .json for out-of-terminal functions.

3.5.4 (01/12/2021) - UNSTABLE
- active tests.

3.5.5 (01/12/2021) - UNSTABLE
- bug fixes.

3.5.6 (01/12/2021)
- functionality resolved using pypyxl.
- duality.dualityCLI and python __main__.py now officially work.

3.5.7 (01/12/2021)
- added block = False to plt.show() in order to unlock further actions after a graph in dualityCLI.

3.5.8 (01/12/2021) - UNSTABLE
- cli code redefined and made user friendly.
- dualityCLI is now CLI.

3.5.9 (01/12/2021) - UNSTABLE
- now contains the executable CLI file with .exe extension within CLIexe folder.
- dualityCLI.exe v1.0 functionality equalized with 3.5.9 version of python __main__.py and duality.CLI()

3.5.10 (01/12/2021) - UNSTABLE
- dualityCLI.exe release postponed, use python __main__.py or duality.CLI() to execute.

3.5.11 (01/12/2021)
- dualityCLI.exe files removed from the package.
- CLIexeversion is now CLIversion.

3.5.12+ (02-03/12/2021)
- CLI v1.1 version replaces the CLI v1.0
- added menu and help actions to Dijkstra and EOQ until they become implemented.
- bugfix of MonteCarlo simulations being period and vice versa.

3.6.1 (03/12/2021) - STABLE
- CLI v1.21 version added.
- CLI stable after initial tests.

3.6.2 (04/12/2021) - STABLE
- CLI v1.22 version added.
- colored CLI functions.
- colorama added to dependencies.
- added clear screen after exiting clients.

3.6.4 (04/12/2021)
- skips ghost 3.6.3 version.
- CLI v1.23 version added.
- quick bugfix of executing greet() after cls in CLI.

**as vandal**

3.0.0 (27/12/2021)
- duality package merged back into vandal.
- perform_block added into graph() so it fits any IDE requirements in an agile way.
- requirements added to requirements.txt

3.0.1 (28/12/2021)
- code cleanup from previous versions.
- setup for introduction of duality decorators into DEVELOPER MODE.

3.0.2 (28/12/2021) - DEVELOPER MODE TEST (IGNORE THIS VERSION!)
- duality decorators set to test in public environment

3.1.0 (28/12/2021)
- confirmed functionality of the DEVELOPER MODE, reverted to basic user mode.

3.1.1 (30/12/2021)
- create_password() added to toolkit.

3.1.2, 3.1.3 (04/01/2022)
- return of cli module put to test as vandal.App.

3.2.0 (04/01/2022)
- confirmed vandal.App functionality.
- followup changes of duality decorators added to EOQ and Dijkstra.

3.2.1 (04/01/2022)
- vandal.cli renamed to vandal.app.
- CLIsets renamed to MC_testassets.

3.2.2 (07/01/2022)
- now imports duality particles for building a CLI. 

3.2.3 (08/01/2022)
- recent duality changes fetched.

3.2.4 (25/01/2022)
- regular maintenance activities.
- create_password typo fixed.
- create_password now included in toolkit help option.

3.2.5 (25/01/2022)
- duality requirement 4.1.10 -> 4.1.11
- DEVELOPER MODE removed due to changes to duality package being only for static functions.

3.2.6 (25/01/2022)
- duality and colorama removed due to incoming argparse changes.

3.3.0 (26/01/2022)
- switch from App to argparse CLI put to test.
- App now marked as deprecated and will be set for removal after test confirmation.
- introduced save_to and file_handler features within toolkit.

3.3.1+ (26/01/2022)
- new test iterations.

3.4.0 (27/01/2022)
- new argparse application that leads to the Monte Carlo app put to test.
- old vandal.App moved to .deprecated.

3.4.1 (28/01/2022)
- confirmed functionality of Monte Carlo app.
- added an option to input values manually without having to provide a file.
- preparation for introduction of EOQ and Dijkstra modules for argparse integration.

3.4.2 (28/01/2022)
- fixed save_to bug, now properly saves change and values.

3.4.3 (28/01/2022)
- indent fix.
- fixed destination shown using save_to.

3.4.4 (28/01/2022) 
- quick bug fix related to change save to file option.

3.4.5 (28/01/2022)
- floats allowed in manual input of values instead od integers only.
- fixed .csv file save location.
- redefined README.
- now supports both 'x,y' and 'x.y' format of decimal numbers in manual input.

3.4.6+ (29/01/2022) - UNSTABLE
- UX improved.
- coloring put to test.

3.5.0 (29/01/2022)
- final changes and put to test.
- LICENSE 2022. added.

3.5.1 (29/01/2022)
- followup changes after test.
- confirmed functionality.

3.5.2 (30/01/2022)
- code cleanup.
- README update.

3.5.3 (30/01/2022)
- colorama rework.

3.5.4 (09/02/2022)
- EOQ app put to test.
- APPversion moved to _misc.meta.

3.5.5 (09/02/2022)
- initial EOQ app tests passed.
- full CLI set to test.

3.5.6 (06/03/2022)
- regular maintenance.

3.6.0 (13/03/2022)
- set of changes deployed.
- code readability improved.
- many options set for testing.

3.6.1 (13/03/2022)
- minor tests.

3.6.2+ (14/03/2022)
- bug fixes.

3.6.5 (14/03/2022)
- new set of tests deployed.

3.6.6 (14/03/2022)
- ref_value_index is now ref_row.
- ref_col added to locate the index.
- now automatically transforms the dictionary into a pandas DataFrame.
- apps now create an output in yellow color, while the module printed options are green.

3.6.7 (22/03/2022)
- dict output redefined.

3.6.8 (23/03/2022)+ - UNSTABLE
- various tests.

3.7.0 (23/03/2022)
- plugins package with meta and types added.
- annotations and type hints updated.
- created generic, structured and complex types.
- now all Vandal package particles are assigned VandalType annotations.

3.7.1 (27/03/2022)
- __all__ is now a list of strings.
