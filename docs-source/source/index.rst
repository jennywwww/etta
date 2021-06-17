.. ExoFOP Python API documentation master file, created by
   sphinx-quickstart on Thu Jun  3 18:39:32 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ExoFOP Python API's documentation!
=============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

The ExoFOP Python API allows you to easily access ExoFOP-TESS data programmatically.

>>> import php_wrappers
>>> dataframe = php_wrappers.download_toi(toi=125)
Fetching data from https://exofop.ipac.caltech.edu/tess/download_toi.php?output=pipe&toi=125
>>> dataframe
          TIC ID  Previous CTOI  Master  ...  Date TOI Updated (UTC)        Date Modified                                           Comments
TOI                                      ...                                                                                                
125.03  52368076            NaN       1  ...              2019-12-17  2021-06-01 12:02:45  period is likely correct but possibly two inde...
125.01  52368076            NaN       1  ...              2020-10-26  2021-06-01 12:02:45                                          TOI-125 b
125.02  52368076            NaN       2  ...              2020-10-05  2021-06-01 12:02:45                             second planet (125.02)
[3 rows x 57 columns]
>>> php_wrappers.download_toi(toi=127, output='pipe', path='.')
Fetching data from https://exofop.ipac.caltech.edu/tess/download_toi.php?output=pipe&toi=127
Result written to /home/jenny/TSP/github-exofop-api/download_toi.php?output=pipe&toi=127


.. toctree::
   :maxdepth: 1
   :caption: Getting Started

Bug Reports & Questions
-----------------------

The ExoFOP Python API is an open source project under the MIT license. The source code is available on `GitHub`_. In case of any questions or problems, please contact us via the `Git Issues`_.

.. toctree::
   :maxdepth: 2
   :caption: Documentation

   php_wrappers
   helpers

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _GitHub: https://github.com/jennywwww/exofop-tess-api
.. _Git Issues: https://github.com/jennywwww/exofop-tess-api/issues
