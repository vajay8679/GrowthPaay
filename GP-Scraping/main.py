from growthpaayscraping.aws_config_profile.utils_aws_s3 import push_parquet_file_to_S3_bucket
from growthpaayscraping.utils.utils_json import convert_to_json_file
from growthpaayscraping.utils.utils_parquet import convert_json_to_parquet_file

if __name__ == "__main__":
    
    print(push_parquet_file_to_S3_bucket.__doc__)
    print(convert_to_json_file.__doc__)
    print(convert_json_to_parquet_file.__doc__)
