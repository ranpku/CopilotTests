from __future__ import absolute_import, print_function, unicode_literals
import os
import re
import fnmatch
def was_processed(processed, path_name, verbose):
    """
    Check if a file or directory has already been processed.

    To prevent recursion, expand the path name to an absolution path
    call this function with a set that will store all the entries and
    the entry to test. If the entry is already in the set, report the issue
    and return ``True``. Otherwise, add the entry to the set and return
    ``False`` to allow the path to be processed.

    Args:
        processed: Set to store processed pathnames
        path_name: Path to a directory or file
        verbose: True if verbose output is requested

    Returns:
        True if it's already in the set. False if not.
    """

    # Test for recursion
    if path_name in processed:
        if verbose:
            print('{} has already been processed'.format(path_name))
        return True

    # Mark this list as "processed" to prevent recursion
    if verbose:
        print('Processing {}.'.format(path_name))
    processed.add(path_name)
    return False

def test_was_processed():
    """
    Check the corretness of was_processed
    """
    assert was_processed(set(), "A", True) == False
    assert was_processed(set(), "A", False) == False