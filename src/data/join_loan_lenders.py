# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

import pandas as pd


@click.command()
@click.argument('input_filepath',
                type=click.Path(exists=True),
                help='path to raw data *directory*')
@click.argument('output_filepath',
                type=click.Path(),
                help='path to interim data *directory*')
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making the joined csv')

    df = pd.read_csv(input_filepath / 'loans.csv')
    df2 = pd.read_csv(input_filepath / 'loans_lenders.csv')
    merged = pd.merge(df, df2, on="LOAN_ID")
    merged.to_csv(output_filepath / 'loan_lender_merged.csv')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
