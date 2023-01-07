import csv
import requests
import urllib.request
import zipfile
from dagster import asset, AssetIn


# AssetKey = name of decorated function ('cereals')
# Op = the cereals function
# Upstream assets = empty (Optional)
@asset
def cereals():
    response = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = response.text.split("\n")
    cereal_rows = [row for row in csv.DictReader(lines)]

    return cereal_rows


@asset
def nabisco_cereals(cereals):
    """Cereals manufactured by Nabisco"""
    return [row for row in cereals if row["mfr"] == "N"]


# @asset(ins={"input_asset": AssetIn("cereals")})
# def nabisco_cereals_2(input_asset):       # Operation param name must match "input_asset"
#     """Cereals manufactured by Nabisco"""
#     return [row for row in cereals if row["mfr"] == "N"]


@asset
def cereal_protein_fractions(cereals):
    """
    For each cereal, records its protein content as a fraction of its total mass.
    """
    result = {}
    for cereal in cereals:
        total_grams = float(cereal["weight"]) * 28.35
        result[cereal["name"]] = float(cereal["protein"]) / total_grams

    return result


@asset
def highest_protein_nabisco_cereal(nabisco_cereals, cereal_protein_fractions):
    """
    The name of the nabisco cereal that has the highest protein content.
    """
    sorted_by_protein = sorted(
        nabisco_cereals, key=lambda cereal: cereal_protein_fractions[cereal["name"]]
    )
    return sorted_by_protein[-1]["name"]


# Assets without Arguments and Return Values

# Includes a 'None' annotation for the return type.
@asset
def cereal_ratings_zip() -> None:
    # No return value, saving the result to storage is handled by this operation
    # No Dasgter I/O manager is involved

    urllib.request.urlretrieve(
        "https://dagster-git-tutorial-nothing-elementl.vercel.app/assets/cereal-ratings.csv.zip",
        "cereal-ratings.csv.zip",
    )

# This depends on 'cereal_ratings_zip' asset
@asset(non_argument_deps={"cereal_ratings_zip"})
def cereal_ratings_csv() -> None:
    with zipfile.ZipFile("cereal-ratings.csv.zip", "r") as zip_ref:
        zip_ref.extractall(".")


# We can combine both way of passing data between assets operations
@asset(non_argument_deps={"cereal_ratings_csv"})
def nabisco_cereal_ratings(nabisco_cereals):
    with open("cereal-ratings.csv", "r") as f:
        cereal_ratings = {
            row["name"]: row["rating"] for row in csv.DictReader(f.readlines())
        }

    result = {}
    for nabisco_cereal in nabisco_cereals:
        name = nabisco_cereal["name"]
        result[name] = cereal_ratings[name]

    return result