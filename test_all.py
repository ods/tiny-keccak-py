import pytest

from tiny_keccak import keccak256


@pytest.mark.parametrize(
    "input_hex, expected_output_hex",
    [
        (
            "",
            "c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470",
        ),
        (
            "00" * 64,
            "ad3228b676f7d3cd4284a5443f17f1962b36e491b30a40b2405849e597ba5fb5",
        ),
        (
            (
                "79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798"
                "483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8"
            ),
            "c0a6c424ac7157ae408398df7e5f4552091a69125d5dfcb7b8c2659029395bdf",
        ),
    ],
)
def test_all(input_hex: str, expected_output_hex: str) -> None:
    output = keccak256(bytes.fromhex(input_hex))
    assert output.hex() == expected_output_hex
