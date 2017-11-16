# ErrorLib

## A LabVIEW Error Handler Library

This builds upon the LabVIEW native error handler (NEH) to allow for:
* multiple errors to be carried in an error array, 
* prioritization of errors: errors will be presented to the user with the lowest priority number first
* severity of errors: custom handlers can be made based on a text string error severity, for example an "abort" severity can tell a state mechine to exit while a "continue" error allows it to continue to the next state.

Many people do not realize that the LabVIEW native error handler "merge" function only chooses the topmost error.  Only one error is ever carried by the NEH
