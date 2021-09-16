About etta
===========================

``etta`` consists of a series of lightweight wrappers around
the PHP functions which are offered by the Exoplanet Follow-up Observing Program for TESS (ExoFOP-TESS).
You can read about the underlying PHP functions in the `ExoFOP-TESS documentation`_. 

The package contains two modules:

* php_wrappers
    Contains a wrapper for every PHP function provided by ExoFOP-TESS, except functions under the "Files" heading (i.e. download_files, download_files_zip, download_filelist, download_tag_files, download_tag_files_zip).

* helpers
    Contains helper functions used by php_wrappers. Provides a more flexible and extensible way to call ExoFOP-TESS PHP functions.

Versioning
----------
The documentation contains three versions:

* stable
    Corresponds to the latest PyPi release.
* latest
    Corresponds to the main branch in the GitHub repo.
* dev
    Corresponds to the dev branch in the GitHub repo. Contains the most up-to-date code. 
    Documentation may not accurately reflect the code. Code may not have been tested yet.

.. _ExoFOP-TESS documentation: https://exofop.ipac.caltech.edu/tess/Introduction_to_ExoFOP_php_functions.php