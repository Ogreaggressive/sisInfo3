from dagster import load_assets_from_package_module, repository

from dagster_data_app import assets
from dagster_data_app.jobs.sample_job import complex_job

@repository
def dagster_data_app():
    return [load_assets_from_package_module(assets), complex_job]
