from setuptools import find_packages, setup

if __name__ == "__main__":
    setup(
        name="dagster_data_app",
        packages=find_packages(exclude=["dagster_data_app_tests"]),
        install_requires=[
            "dagster",
        ],
        extras_require={"dev": ["dagit", "pytest"]},
    )
