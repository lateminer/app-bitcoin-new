from bitcoin_client.command import BitcoinCommand
from bitcoin_client.common import AddressType
from bitcoin_client.wallet import MultisigWallet

from .utils import automation

import pytest

# TODO: add tests with UI
# TODO: UI does not currently work


def test_get_wallet_address_legacy(cmd: BitcoinCommand):
    # test for a legacy p2sh wallet

    wallet = MultisigWallet(
        name="Cold storage",
        address_type=AddressType.LEGACY,
        threshold=2,
        keys_info=[
            f"[5c9e228d/48'/1'/0'/0']tpubDEGquuorgFNb8bjh5kNZQMPtABJzoWwNm78FUmeoPkfRtoPF7JLrtoZeT3J3ybq1HmC3Rn1Q8wFQ8J5usanzups5rj7PJoQLNyvq8QbJruW/**",
            f"[f5acc2fd/48'/1'/0'/0']tpubDFAqEGNyad35WQAZMmPD4vgBXnjH16RGciLdWekPe4f4d5JzoHVu1PS86Sy4Tm63vDf8rfV3UjifhrRuSUDfiZj5KPffTPyZ4ZXBKvjD8jm/**",
        ],
    )
    wallet_hmac = bytes.fromhex(
        "9eca5a688f4330ffd1d0dbe4a7ddc246a22ca77b061a45be26101f564ea49016"
    )

    print(wallet.policy_map)

    res = cmd.get_wallet_address(wallet, wallet_hmac, 0)
    print(res)
    assert res == "2Mx69MjHC4ViZAH1koVXPvVgaazbBCdr89j"


def test_get_wallet_address_sh_wit(cmd):
    # test for a wrapped segwit wallet

    wallet = MultisigWallet(
        name="Cold storage",
        address_type=AddressType.SH_WIT,
        threshold=2,
        keys_info=[
            f"[76223a6e/48'/1'/0'/1']tpubDE7NQymr4AFtcJXi9TaWZtrhAdy8QyKmT4U6b9qYByAxCzoyMJ8zw5d8xVLVpbTRAEqP8pVUxjLE2vDt1rSFjaiS8DSz1QcNZ8D1qxUMx1g/**",
            f"[f5acc2fd/48'/1'/0'/1']tpubDFAqEGNyad35YgH8zxvxFZqNUoPtr5mDojs7wzbXQBHTZ4xHeVXG6w2HvsKvjBpaRpTmjYDjdPg5w2c6Wvu8QBkyMDrmBWdCyqkDM7reSsY/**",
        ],
    )
    wallet_hmac = bytes.fromhex(
        "da0066f82b1d067703f97f5b3cf64a640442c482a2568c144bf1dae8024ad003"
    )

    res = cmd.get_wallet_address(wallet, wallet_hmac, 0)
    assert res == "2MxAUTJh27foYtyp9dcSxP7RgaSwkkVCHTU"


def test_get_wallet_address_wit(cmd: BitcoinCommand):
    # test for a native segwit wallet (bech32 address)

    wallet = MultisigWallet(
        name="Cold storage",
        address_type=AddressType.WIT,
        threshold=2,
        keys_info=[
            f"[76223a6e/48'/1'/0'/2']tpubDE7NQymr4AFtewpAsWtnreyq9ghkzQBXpCZjWLFVRAvnbf7vya2eMTvT2fPapNqL8SuVvLQdbUbMfWLVDCZKnsEBqp6UK93QEzL8Ck23AwF/**",
            f"[f5acc2fd/48'/1'/0'/2']tpubDFAqEGNyad35aBCKUAXbQGDjdVhNueno5ZZVEn3sQbW5ci457gLR7HyTmHBg93oourBssgUxuWz1jX5uhc1qaqFo9VsybY1J5FuedLfm4dK/**",
        ],
    )
    wallet_hmac = bytes.fromhex(
        "5dab4a4dfa5ae128c3aeff877ca474eecf4ce1ef9d75e42311b1f335e022c4f9"
    )

    res = cmd.get_wallet_address(wallet, wallet_hmac, 0)
    assert res == "tb1qmyauyzn08cduzdqweexgna2spwd0rndj55fsrkefry2cpuyt4cpsn2pg28"
