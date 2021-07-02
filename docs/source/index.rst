etta: programmatic access to ExoFOP-TESS data
=============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

``etta`` is a Python package which allows you to access ExoFOP-TESS data programmatically. The package contains wrapper functions for the `ExoFOP-TESS PHP functions`_.

>>> import etta
>>> dataframe = etta.download_toi(toi=125)
Fetching data from https://exofop.ipac.caltech.edu/tess/download_toi.php?output=pipe&toi=125
>>> dataframe
          TIC ID  Previous CTOI  Master  ...  Date TOI Updated (UTC)        Date Modified                                           Comments
TOI                                      ...                                                                                                
125.03  52368076            NaN       1  ...              2019-12-17  2021-06-01 12:02:45  period is likely correct but possibly two inde...
125.01  52368076            NaN       1  ...              2020-10-26  2021-06-01 12:02:45                                          TOI-125 b
125.02  52368076            NaN       2  ...              2020-10-05  2021-06-01 12:02:45                             second planet (125.02)
[3 rows x 57 columns]
>>> etta.download_toi(toi=127, output='pipe', path='.')
Fetching data from https://exofop.ipac.caltech.edu/tess/download_toi.php?output=pipe&toi=127
Result written to /home/jenny/TSP/github-exofop-api/download_toi.php?output=pipe&toi=127

.. toctree::
   :maxdepth: 1
   :caption: Getting Started

   getting-started/about
   getting-started/installation
   getting-started/tutorial

.. toctree::
   :maxdepth: 2
   :caption: Documentation

   php_wrappers
   helpers

Bug Reports & Questions
-----------------------

``etta`` is an open source project under the MIT license. The source code is available on `GitHub`_. In case of any questions or problems, please contact us via the `Git Issues`_.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _GitHub: https://github.com/jennywwww/exofop-tess-api
.. _Git Issues: https://github.com/jennywwww/exofop-tess-api/issues
.. _ExoFOP-TESS PHP functions: https://exofop.ipac.caltech.edu/tess/Introduction_to_ExoFOP_php_functions.php