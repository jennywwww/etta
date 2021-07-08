from .helpers import write_to_path, create_url, call_php_function

def download_toi(toi=None, sort=None, output='pandas', path=None):
    """Accesses the full TOI table from https://exofop.ipac.caltech.edu/tess/view_toi.php

    Args:
        toi (str or int, optional): Access table information for a specific TOI. Defaults to `None`.
        sort (str, optional): Column to sort by. Defaults to `None`.
            Available columns are: tid, toidesc, toi, toiasc, master, sg1a, sg1b, sg2, sg3, sg4, sg5, 
            acwg, tmag, planetrad, planetname, planetnum, planetinsol, planetteq, planetsnr, 
            disposition, tfopwgdisp, source, ra, dec, pmra, pmdec, epoch, period, duration, depth, 
            distance, teff, logg, rad, metallicity, sectors, toi_alerted, toi_edited.
            If `sort` is `None` or the provided sort column name is invalid, the result will be
            sorted by last modified time.
        output (str, optional): Output of result. Available formats are:
            pandas: returns :py:class:`pandas.DataFrame` object with index column set to TOIs.
            csv: save csv file to `path`.
            pipe: save pipe-delimited file to `path`.
            text: save text file to `path`.
            Defaults to `'pandas'`.
        path (str, optional): Path to save the result file to. 
            Only relevant if result output is csv, pipe or text.

            * If path provided is a file, the result will be written to that file.
            * If path provided is a directory, the file will be saved in the given directory with a default filename.
            * If `path` is `None`, the file will be saved in the current directory with a default filename.
            
            Defaults to `None`.

    Returns:
        :py:class:`pandas.DataFrame` or `None`: if `output='pandas'`, a :py:class:`pandas.DataFrame`
        object is returned. Else the result is saved to file and the function returns `None`.
    """
    payload = {'output': output, 'sort': sort, 'toi': toi}
    return call_php_function('download_toi', payload, path, 1)

def download_nearbytarget(tic, sort=None, output='pandas', path=None):
    """Accesses nearby targets for a given TIC ID.

    Args:
        tic (int): TIC ID.
        sort (str, optional): Column to sort by. Defaults to `None`.
            Available columns are:  id (TIC ID), toi, ra, dec, pmra, pmdec, tmag, distance, separation.
            If `sort` is `None`, the result will be sorted by separation.
            If `sort` is an invalid column name, sort order is undefined.
        output (str, optional): Output of result. Available formats are:

            * pandas: returns :py:class:`pandas.DataFrame` object with index column set to TICs.
            * csv: save csv file to `path`.
            * pipe: save pipe-delimited file to `path`.
            * text: save text file to `path`.

            Defaults to `'pandas'`.
        path (str, optional): Path to save the result file to. 
            Only relevant if result output is csv, pipe or text.

            * If path provided is a file, the result will be written to that file.
            * If path provided is a directory, the file will be saved in the given directory with a default filename.
            * If `path` is `None`, the file will be saved in the current directory with a default filename.
            
            Defaults to `None`.

    Returns:
        :py:class:`pandas.DataFrame` or `None`: if `output='pandas'`, a :py:class:`pandas.DataFrame`
        object is returned. Else the result is saved to file and the function returns `None`.
    """
    payload = {'output': output, 'sort': sort, 'id': tic}
    return call_php_function('download_nearbytarget', payload, path, 0)

def download_imaging(target=None, sort=None, output='pandas', path=None):
    """Accesses all imaging observation summaries.

    Args:
        target (str, optional): Target's TIC ID, TOI name (including TOI prefix), or a planet name recognized by the Exoplanet Archive.
            Accepted formats: (nnnnnnnnn|TOInnn|TOInnn.nn|name).
        sort (str, optional): Column to sort by. Defaults to `None`.
            Available columns are:  id (TIC ID), tel, inst, filt, pix, imagetype, psf, cont, date, tag, notes, user, group.
            If `sort` is `None` or is an invalid column name, the result will be sorted by id.
        output (str, optional): Output of result. Available formats are:
            
            * `'pandas'`: returns :py:class:`pandas.DataFrame` object with default index column.
            * `'csv'`: save csv file to `path`.
            * `'pipe'`: save pipe-delimited file to `path`.
            * `'text'`: save text file to `path`.

            Defaults to `'pandas'`.
        path (str, optional): Path to save the result file to. 
            Only relevant if result output is csv, pipe or text.

            * If path provided is a file, the result will be written to that file.
            * If path provided is a directory, the file will be saved in the given directory with a default filename.
            * If `path` is `None`, the file will be saved in the current directory with a default filename.
            
            Defaults to `None`.

    Returns:
        :py:class:`pandas.DataFrame` or `None`: if `output='pandas'`, a :py:class:`pandas.DataFrame`
        object is returned. Else the result is saved to file and the function returns `None`.
    """
    payload = {'target': target, 'output': output, 'sort': sort}
    return call_php_function('download_imaging', payload, path)

def download_tag_imaging(tag, sort=None, output='pandas', path=None):
    """Accesses all imaging observation summaries for a given tag.

    Args:
        tag (str or int): Data tag (see https://exofop.ipac.caltech.edu/tess/tag_help.php for more information). 
            Tag can be string or associated number.
        sort (str, optional): Column to sort by. Defaults to `None`.
            Available columns are:  id (TIC ID), tel, inst, filt, pix, imagetype, psf, cont, date, tag, notes, user, group.
            If `sort` is `None` or is an invalid column name, the result will be sorted by id.
        output (str, optional): Output of result. Available formats are:
            
            * `'pandas'`: returns :py:class:`pandas.DataFrame` object with default index column.
            * `'csv'`: save csv file to `path`.
            * `'pipe'`: save pipe-delimited file to `path`.
            * `'text'`: save text file to `path`.

            Defaults to `'pandas'`.
        path (str, optional): Path to save the result file to. 
            Only relevant if result output is csv, pipe or text.

            * If path provided is a file, the result will be written to that file.
            * If path provided is a directory, the file will be saved in the given directory with a default filename.
            * If `path` is `None`, the file will be saved in the current directory with a default filename.
            
            Defaults to `None`.

    Returns:
        :py:class:`pandas.DataFrame` or `None`: if `output='pandas'`, a :py:class:`pandas.DataFrame`
        object is returned. 
        Else the result is saved to file and the function returns `None`.
    """
    payload = {'tag': tag, 'output': output, 'sort': sort}
    return call_php_function('download_tag_imaging', payload, path)

def download_spect(target=None, sort=None, output='pandas', path=None):
    """Accesses all spectroscopic observation summaries.

    Args:
        target (str, optional): Target's TIC ID, TOI name (including TOI prefix), or a planet name recognized by the Exoplanet Archive.
            Accepted formats: (nnnnnnnnn|TOInnn|TOInnn.nn|name).
        sort (str, optional): Column to sort by. Defaults to `None`.
            Available columns are: id (TIC ID), tel, inst, res, cov, snrres, snrwave, prv, date, tag, notes, user, group.
            If `sort` is `None` or is an invalid column name, the result will be sorted by id.
        output (str, optional): Output of result. Available formats are:
            
            * `'pandas'`: returns :py:class:`pandas.DataFrame` object with default index column.
            * `'csv'`: save csv file to `path`.
            * `'pipe'`: save pipe-delimited file to `path`.
            * `'text'`: save text file to `path`.

            Defaults to `'pandas'`.
        path (str, optional): Path to save the result file to. 
            Only relevant if result output is csv, pipe or text.

            * If path provided is a file, the result will be written to that file.
            * If path provided is a directory, the file will be saved in the given directory with a default filename.
            * If `path` is `None`, the file will be saved in the current directory with a default filename.
            
            Defaults to `None`.

    Returns:
        :py:class:`pandas.DataFrame` or `None`: if `output='pandas'`, a :py:class:`pandas.DataFrame`
        object is returned. 
        Else the result is saved to file and the function returns `None`.
    """
    payload = {'target': target, 'output': output, 'sort': sort}
    return call_php_function('download_spect', payload, path)

def download_tag_spect(tag, sort=None, output='pandas', path=None):
    """Accesses all spectroscopic observation summaries for a given tag.

    Args:
        tag (str or int): Data tag (see https://exofop.ipac.caltech.edu/tess/tag_help.php for more information). 
            Tag can be string or associated number.
        sort (str, optional): Column to sort by. Defaults to `None`.
            Available columns are: id (TIC ID), tel, inst, res, cov, snrres, snrwave, prv, date, tag, notes, user, group.
            If `sort` is `None` or is an invalid column name, the result will be sorted by id.
        output (str, optional): Output of result. Available formats are:
            
            * `'pandas'`: returns :py:class:`pandas.DataFrame` object with default index column.
            * `'csv'`: save csv file to `path`.
            * `'pipe'`: save pipe-delimited file to `path`.
            * `'text'`: save text file to `path`.

            Defaults to `'pandas'`.
        path (str, optional): Path to save the result file to. 
            Only relevant if result output is csv, pipe or text.

            * If path provided is a file, the result will be written to that file.
            * If path provided is a directory, the file will be saved in the given directory with a default filename.
            * If `path` is `None`, the file will be saved in the current directory with a default filename.
            
            Defaults to `None`.

    Returns:
        :py:class:`pandas.DataFrame` or `None`: if `output='pandas'`, a :py:class:`pandas.DataFrame`
        object is returned. 
        Else the result is saved to file and the function returns `None`.
    """
    payload = {'tag': tag, 'output': output, 'sort': sort}
    return call_php_function('download_tag_spect', payload, path)

def download_tseries(target=None, sort=None, output='pandas', path=None):
    """Accesses all time series observation summaries.

    Args:
        target (str, optional): Target's TIC ID, TOI name (including TOI prefix), or a planet name recognized by the Exoplanet Archive.
            Accepted formats: (nnnnnnnnn|TOInnn|TOInnn.nn|name).
        sort (str, optional): Column to sort by. Defaults to `None`.
            Available columns are: id (TIC ID), tel, camera, filt, pix, psf, photaprad, date, transcov, deltamag, tag, notes, user, group.
            If `sort` is `None` or is an invalid column name, the result will be sorted by id.
        output (str, optional): Output of result. Available formats are:
            
            * `'pandas'`: returns :py:class:`pandas.DataFrame` object with default index column.
            * `'csv'`: save csv file to `path`.
            * `'pipe'`: save pipe-delimited file to `path`.
            * `'text'`: save text file to `path`.

            Defaults to `'pandas'`.
        path (str, optional): Path to save the result file to. 
            Only relevant if result output is csv, pipe or text.

            * If path provided is a file, the result will be written to that file.
            * If path provided is a directory, the file will be saved in the given directory with a default filename.
            * If `path` is `None`, the file will be saved in the current directory with a default filename.
            
            Defaults to `None`.

    Returns:
        :py:class:`pandas.DataFrame` or `None`: if `output='pandas'`, a :py:class:`pandas.DataFrame`
        object is returned. 
        Else the result is saved to file and the function returns `None`.
    """
    payload = {'target': target, 'output': output, 'sort': sort}
    return call_php_function('download_tseries', payload, path)

def download_tag_tseries(tag, sort=None, output='pandas', path=None):
    """Accesses all time series observation summaries for a given tag.

    Args:
        tag (str or int): Data tag (see https://exofop.ipac.caltech.edu/tess/tag_help.php for more information). 
            Tag can be string or associated number.
        sort (str, optional): Column to sort by. Defaults to `None`.
            Available columns are: id (TIC ID), tel, camera, filt, pix, psf, photaprad, date, transcov, deltamag, tag, notes, user, group.
            If `sort` is `None` or is an invalid column name, the result will be sorted by id.
        output (str, optional): Output of result. Available formats are:
            
            * `'pandas'`: returns :py:class:`pandas.DataFrame` object with default index column.
            * `'csv'`: save csv file to `path`.
            * `'pipe'`: save pipe-delimited file to `path`.
            * `'text'`: save text file to `path`.

            Defaults to `'pandas'`.
        path (str, optional): Path to save the result file to. 
            Only relevant if result output is csv, pipe or text.

            * If path provided is a file, the result will be written to that file.
            * If path provided is a directory, the file will be saved in the given directory with a default filename.
            * If `path` is `None`, the file will be saved in the current directory with a default filename.
            
            Defaults to `None`.

    Returns:
        :py:class:`pandas.DataFrame` or `None`: if `output='pandas'`, a :py:class:`pandas.DataFrame`
        object is returned. 
        Else the result is saved to file and the function returns `None`.
    """
    payload = {'output': output, 'tag': tag, 'sort': sort}
    return call_php_function('download_tag_tseries', payload, path)

def download_obsnotes(tag=None, tic=None, row_id=None, output='pandas', path=None):
    """Accesses observing notes for the given TIC ID, tag, or row ID.

    Args:
        tag (str or int): Data tag (see https://exofop.ipac.caltech.edu/tess/tag_help.php for more information). 
            Tag can be string or associated number.
        tic (int): TIC ID.
        row_id (int): Row ID associated with note.
        output (str, optional): Output of result. Available formats are:
                        
            * pandas: returns :py:class:`pandas.DataFrame` object with default index column.
            * csv: save csv file to `path`.
            * pipe: save pipe-delimited file to `path`.
            
            Defaults to `'pandas'`.
        path (str, optional): Path to save the result file to. 
            Only relevant if result output is csv, pipe or text.

            * If path provided is a file, the result will be written to that file.
            * If path provided is a directory, the file will be saved in the given directory with a default filename.
            * If `path` is `None`, the file will be saved in the current directory with a default filename.
            
            Defaults to `None`.

    Returns:
        :py:class:`pandas.DataFrame` or `None`: if `output='pandas'`, a :py:class:`pandas.DataFrame`
        object is returned. 
        Else the result is saved to file and the function returns `None`.
    """
    if not (tag or tic or row_id):
        raise ValueError('You must provide tag, TIC or row ID.')
    payload = {'output': output, 'tag': tag, 'tid': tic, 'id': row_id}
    return call_php_function('download_obsnotes', payload, path)

def download_user_tags(username=None, output='pandas', path=None):
    """Accesses list of user tags made by `username`.

    Args:
        username (str, optional): username to search. 
            If username is None, search is conducted on logged-in user's username.
        output (str, optional): Output of result. Available formats are:
            
            * pandas: returns :py:class:`pandas.DataFrame` object with default index column.
            * csv: save csv file to `path`.
            * pipe: save pipe-delimited file to `path`.
            
            Defaults to `'pandas'`.
        path (str, optional): Path to save the result file to. 
            Only relevant if result output is csv, pipe or text.

            * If path provided is a file, the result will be written to that file.
            * If path provided is a directory, the file will be saved in the given directory with a default filename.
            * If `path` is `None`, the file will be saved in the current directory with a default filename.
            
            Defaults to `None`.

    Returns:
        :py:class:`pandas.DataFrame` or `None`: if `output='pandas'`, a :py:class:`pandas.DataFrame`
        object is returned. 
        Else the result is saved to file and the function returns `None`.
    """
    payload = {'output': output, 'username': username}
    return call_php_function('download_user_tags', payload, path)

def download_stellarcomp(target=None, sort=None, output='pandas', path=None):
    """Accesses all user-reported stellar companions.

    Args:
        target (str, optional): Target's TIC ID, TOI name (including TOI prefix), or a planet name recognized by the Exoplanet Archive.
            Accepted formats: (nnnnnnnnn|TOInnn|TOInnn.nn|name).
        sort (str, optional): Column to sort by. Defaults to `None`.
            Available columns are:  id (TIC ID), lastmod (descending).
            If `sort` is `None` or is an invalid column name, the result will be sorted by id.
        output (str, optional): Output of result. Available formats are

            * `'pandas'`: returns :py:class:`pandas.DataFrame` object with default index column.
            * `'csv'`: save csv file to `path`.
            * `'pipe'`: save pipe-delimited file to `path`.
            * `'text'`: save text file to `path`.

            Defaults to `'pandas'`.
        path (str, optional): Path to save the result file to. 
            Only relevant if result output is csv, pipe or text.

            * If path provided is a file, the result will be written to that file.
            * If path provided is a directory, the file will be saved in the given directory with a default filename.
            * If `path` is `None`, the file will be saved in the current directory with a default filename.

            Defaults to `None`.

    Returns:
        :py:class:`pandas.DataFrame` or `None`: if `output='pandas'`, a :py:class:`pandas.DataFrame`
        object is returned. 
        Else the result is saved to file and the function returns `None`.
    """
    payload = {'target': target, 'output': output, 'sort': sort}
    return call_php_function('download_stellarcomp', payload, path)
