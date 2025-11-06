import dlt
from pyspark.sql.functions import *

# Retrieve credentials from Databricks Secrets
access_key = dbutils.secrets.get("aws-connection", "aws-access-key")
secret_key = dbutils.secrets.get("aws-connection", "aws-secret-key")

S3_PATH = "s3://insurance-assesment-dbx-e2e-data/telematics/"

@dlt.table(
    name="telematics_test",
    comment="Bronze telematics data loaded from S3",
    table_properties={"quality": "bronze"}
)
def bronze_table():
    return (
        spark.read
        .format("parquet")
        .option("fs.s3a.access.key", access_key)
        .option("fs.s3a.secret.key", secret_key)
        .load(S3_PATH)
    );
