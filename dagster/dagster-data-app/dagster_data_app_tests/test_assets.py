from dagster import materialize
from dagster_data_app.assets.cereal import nabisco_cereals, cereals, cereal_protein_fractions, \
    highest_protein_nabisco_cereal


# Probar un asset
def test_nabisco_cereals():
    cereals = [
        {"name": "cereal1", "mfr": "N"},
        {"name": "cereal2", "mfr": "K"},
    ]
    result = nabisco_cereals(cereals)  # Llamar a la operación como cualquier otra función en Python
    assert len(result) == 1
    assert result == [{"name": "cereal1", "mfr": "N"}]


def test_cereal_assets():
    assets = [
        nabisco_cereals,
        cereals,
        cereal_protein_fractions,
        highest_protein_nabisco_cereal,
    ]

    result = materialize(assets)
    print("result ", result)
    assert result.success
    assert result.output_for_node("highest_protein_nabisco_cereal") == "100% Bran"


# test_cereal_assets()

