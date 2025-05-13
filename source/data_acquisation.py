import pandas as pd
import pandas as pd
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_data(file_path):
    """
    Reads data from a CSV file and returns a DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: The DataFrame containing the data from the CSV file.
    """
    try:
        logger.info(f"Attempting to read data from {file_path}")
        data = pd.read_csv(file_path)
        logger.info("Data successfully read.")
        return data
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise
    except pd.errors.ParserError:
        logger.error(f"Error parsing the file: {file_path}")
        raise
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        raise
