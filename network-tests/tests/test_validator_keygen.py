# -*- coding: utf-8 -*-
import os
import tempfile
from pathlib import Path


def test_validator_keygen(casperlabs_client):
    with tempfile.TemporaryDirectory() as d:
        directory = Path(d)
        print(directory)
        casperlabs_client.validator_keygen(directory)
        expected_files = (
            "node.certificate.pem",
            "node.key.pem",
            "validator-id-hex",
            "validator-pk-hex",
            "validator-public.pem",
            "node-id",
            "validator-id",
            "validator-pk",
            "validator-private.pem",
        )
        for file_name in expected_files:
            assert os.path.exists(
                directory / file_name
            ), f"Expected {file_name} to exist"
