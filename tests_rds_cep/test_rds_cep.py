# -*- coding: utf-8 -*-
import unittest


import rds_cep


class TestCep(unittest.TestCase):
    def test_get__valid(self):
        self.assertIsInstance(rds_cep.get("59015"), dict)

        self.assertIsInstance(rds_cep.get("59.015"), dict)
        self.assertIsInstance(rds_cep.get("59015-"), dict)
        self.assertIsInstance(rds_cep.get("59.015-"), dict)

        self.assertIsInstance(rds_cep.get("59015000"), dict)
        self.assertIsInstance(rds_cep.get("59015-000"), dict)
        self.assertIsInstance(rds_cep.get("59.015000"), dict)
        self.assertIsInstance(rds_cep.get("59.015-000"), dict)

    def test_get__invalid_silently(self):
        self.assertFalse(rds_cep.get("5912", True))
        self.assertFalse(rds_cep.get("59.12", True))
        self.assertFalse(rds_cep.get("5912-", True))
        self.assertFalse(rds_cep.get("59.12-", True))

        self.assertFalse(rds_cep.get("590154", True))
        self.assertFalse(rds_cep.get("59.0154", True))
        self.assertFalse(rds_cep.get("590154-", True))
        self.assertFalse(rds_cep.get("59.0154-", True))

        self.assertFalse(rds_cep.get("590151234", True))
        self.assertFalse(rds_cep.get("59015-1234", True))
        self.assertFalse(rds_cep.get("59.0151234", True))
        self.assertFalse(rds_cep.get("59.015-1234", True))
        self.assertFalse(rds_cep.get("usuario", True))

    def test_get__invalid_raising(self):
        with self.assertRaises(ValueError):
            rds_cep.get("5912", False)

        with self.assertRaises(ValueError):
            rds_cep.get("59.12", False)

        with self.assertRaises(ValueError):
            rds_cep.get("5912-", False)

        with self.assertRaises(ValueError):
            rds_cep.get("59.12-", False)

        with self.assertRaises(ValueError):
            rds_cep.get("590154", False)

        with self.assertRaises(ValueError):
            rds_cep.get("59.0154", False)

        with self.assertRaises(ValueError):
            rds_cep.get("590154-", False)

        with self.assertRaises(ValueError):
            rds_cep.get("59.0154-", False)

        with self.assertRaises(ValueError):
            rds_cep.get("590151234", False)

        with self.assertRaises(ValueError):
            rds_cep.get("59015-1234", False)

        with self.assertRaises(ValueError):
            rds_cep.get("59.0151234", False)

        with self.assertRaises(ValueError):
            rds_cep.get("59.015-1234", False)

        with self.assertRaises(ValueError):
            rds_cep.get("usuario", False)

    def test_get__not_exists_silently(self):
        self.assertFalse(rds_cep.get("12345"))
        self.assertFalse(rds_cep.get("12345", True))
        self.assertFalse(rds_cep.get("12345-"))
        self.assertFalse(rds_cep.get("12.345"))
        self.assertFalse(rds_cep.get("12.345-"))

        self.assertFalse(rds_cep.get("12345678"))
        self.assertFalse(rds_cep.get("12345-678"))
        self.assertFalse(rds_cep.get("12.345678"))
        self.assertFalse(rds_cep.get("12.345-678"))

    def test_get__not_exists_raising(self):
        with self.assertRaises(ValueError):
            rds_cep.get("12345", False)

        with self.assertRaises(ValueError):
            rds_cep.get("12345-", False)

        with self.assertRaises(ValueError):
            rds_cep.get("12.345", False)

        with self.assertRaises(ValueError):
            rds_cep.get("12.345-", False)

        with self.assertRaises(ValueError):
            rds_cep.get("12345678", False)

        with self.assertRaises(ValueError):
            rds_cep.get("12345-678", False)

        with self.assertRaises(ValueError):
            rds_cep.get("12.345678", False)

        with self.assertRaises(ValueError):
            rds_cep.get("12.345-678", False)

    def test_validate__valid(self):
        self.assertEqual("59015000", rds_cep.validate("59015"))
        self.assertEqual("59015000", rds_cep.validate("59.015"))
        self.assertEqual("59015000", rds_cep.validate("59015-"))
        self.assertEqual("59015000", rds_cep.validate("59.015-"))

        self.assertEqual("59015000", rds_cep.validate("59015000"))
        self.assertEqual("59015000", rds_cep.validate("59015-000"))
        self.assertEqual("59015000", rds_cep.validate("59.015000"))
        self.assertEqual("59015000", rds_cep.validate("59.015-000"))

    def test_validate__invalid_silently(self):
        self.assertFalse(rds_cep.validate("5912", True))
        self.assertFalse(rds_cep.validate("59.12", True))
        self.assertFalse(rds_cep.validate("5912-", True))
        self.assertFalse(rds_cep.validate("59.12-", True))

        self.assertFalse(rds_cep.validate("590154", True))
        self.assertFalse(rds_cep.validate("59.0154", True))
        self.assertFalse(rds_cep.validate("590154-", True))
        self.assertFalse(rds_cep.validate("59.0154-", True))

        self.assertFalse(rds_cep.validate("590151234", True))
        self.assertFalse(rds_cep.validate("59015-1234", True))
        self.assertFalse(rds_cep.validate("59.0151234", True))
        self.assertFalse(rds_cep.validate("59.015-1234", True))
        self.assertFalse(rds_cep.validate("usuario", True))

    def test_validate__invalid_raising(self):
        with self.assertRaises(ValueError):
            rds_cep.validate("5912", False)

        with self.assertRaises(ValueError):
            rds_cep.validate("59.12", False)

        with self.assertRaises(ValueError):
            rds_cep.validate("5912-", False)

        with self.assertRaises(ValueError):
            rds_cep.validate("59.12-", False)

        with self.assertRaises(ValueError):
            rds_cep.validate("590154", False)

        with self.assertRaises(ValueError):
            rds_cep.validate("59.0154", False)

        with self.assertRaises(ValueError):
            rds_cep.validate("590154-", False)

        with self.assertRaises(ValueError):
            rds_cep.validate("59.0154-", False)

        with self.assertRaises(ValueError):
            rds_cep.validate("590151234", False)

        with self.assertRaises(ValueError):
            rds_cep.validate("59015-1234", False)

        with self.assertRaises(ValueError):
            rds_cep.validate("59.0151234", False)

        with self.assertRaises(ValueError):
            rds_cep.validate("59.015-1234", False)

        with self.assertRaises(ValueError):
            rds_cep.validate("usuario", False)
