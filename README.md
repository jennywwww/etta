# etta: programmatic access to ExoFOP-TESS data

`etta` is a Python package which allows you to access data from the [Exoplanet Follow-up Observing Program for TESS (ExoFOP-TESS)](https://exofop.ipac.caltech.edu/tess/). The package consists of a series of lightweight wrappers around the [PHP functions](https://exofop.ipac.caltech.edu/tess/Introduction_to_ExoFOP_php_functions.php) which are offered by ExoFOP-TESS. 

```pycon
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
```

## Installation
You can install the current development version of etta:

```bash
git clone https://github.com/jennywwww/etta.git
cd etta
python setup.py install
```

## More information
For more information, please refer to the [documentation](https://etta.readthedocs.io/en/latest/index.html). 

`etta` is an open source project under the MIT license. In case of any questions or problems, please contact us via the [Git Issues](https://github.com/jennywwww/etta/issues).
