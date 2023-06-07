"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: data.py : python script for data collection                                                 -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: THE LICENSE TYPE AS STATED IN THE REPOSITORY                                               -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""



import json
import pyarrow.parquet as pq



##### --------------------                         PART 1                          -------------------- #####



def read_file(file_name:str=None, folder_route:str=None) -> dict:
    """
    Read data from a local file

    Parameters
    ----------

    file_name: str, (default=None)
        name of the file to be read

    folder_route: str, (default=None)
        Relative or full path to the file

    Returns
    -------

    A json object with the contents of the file
    
    """
    
    # Opening JSON file
    f=open(folder_route+file_name)
    
    # Returns JSON object as a dictionary
    orderbooks_data=json.load(f)

    return orderbooks_data



##### --------------------                         PART 2                          -------------------- #####



def read_data(file_name:str=None, folder_route:str=None) -> dict:
    """
    Read data from a local file

    Parameters
    ----------

    file_name: str, (default=None)
        name of the file to be read

    folder_route: str, (default=None)
        Relative or full path to the file

    Returns
    -------

    A parquet object with the contents of the file
    
    """
    
    # Read PARQUET file
    parquet_data=pq.read_table(source=folder_route+file_name+'.parquet')

    return parquet_data

