# -*- coding: utf-8 -*-
DEFAULT_HOST = "localhost"
DEFAULT_PORT = 40401
DEFAULT_INTERNAL_PORT = 40402
STATUS_CHECK_DELAY = 2
STATUS_TIMEOUT = 180  # 3 minutes
VISUALIZE_DAG_STREAM_DELAY = 5

ED25519_HEX_PREFIX = "01"
ED25519_KEY_ALGORITHM = "ed25519"

SECP256K1_HEX_PREFIX = "02"
SECP256K1_KEY_ALGORITHM = "secp256k1"
# To be used in ECO-463 with SECR256K1_SECURE_ENCLAVE_KEY_ALGORITHM = "secr256k1"

HEX_PREFIX_LEN: int = 2
SUPPORTED_KEY_ALGORITHMS = (ED25519_KEY_ALGORITHM, SECP256K1_KEY_ALGORITHM)
HEX_KEY_PREFIXES = {
    ED25519_HEX_PREFIX: ED25519_KEY_ALGORITHM,
    SECP256K1_HEX_PREFIX: SECP256K1_KEY_ALGORITHM,
}

PRIVATE_KEY_FILENAME: str = "secret_key.pem"
PUBLIC_KEY_FILENAME: str = "public_key.pem"
PUBLIC_KEY_HEX_FILENAME: str = "public_key_hex"

ACCOUNT_HASH_LENGTH: int = 32

NODE_PRIVATE_KEY_FILENAME = "node.key.pem"
NODE_CERTIFICATE_FILENAME = "node.certificate.pem"
NODE_ID_FILENAME = "node-id"
