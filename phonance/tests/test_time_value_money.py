import unittest

from phonance import nir_approx, nir_exact


class TestNirApprox(unittest.TestCase):
    def test_positive_rates(self):
        """Test nir_approx with positive real and inflation rates."""
        self.assertAlmostEqual(nir_approx(0.03, 0.02), 0.05)

    def test_zero_rates(self):
        """Test nir_approx with zero real and inflation rates."""
        self.assertAlmostEqual(nir_approx(0.0, 0.0), 0.0)

    def test_negative_rates(self):
        """Test nir_approx with negative real or inflation rates."""
        self.assertAlmostEqual(nir_approx(-0.01, 0.02), 0.01)
        self.assertAlmostEqual(nir_approx(0.03, -0.02), 0.01)
        self.assertAlmostEqual(nir_approx(-0.01, -0.02), -0.03)

    def test_invalid_inputs(self):
        """Test nir_approx with invalid inputs."""
        with self.assertRaises(TypeError):
            nir_approx("0.03", 0.02)
        with self.assertRaises(TypeError):
            nir_approx(0.03, "0.02")
        with self.assertRaises(TypeError):
            nir_approx(None, 0.02)


class TestNirExact(unittest.TestCase):
    def test_positive_rates(self):
        """Test nir_exact with positive real and inflation rates."""
        self.assertAlmostEqual(nir_exact(0.03, 0.02), 0.0506, places=4)

    def test_zero_rates(self):
        """Test nir_exact with zero real and inflation rates."""
        self.assertAlmostEqual(nir_exact(0.0, 0.0), 0.0)

    def test_negative_rates(self):
        """Test nir_exact with negative real or inflation rates."""
        self.assertAlmostEqual(nir_exact(-0.01, 0.02), 0.0098, places=4)
        self.assertAlmostEqual(nir_exact(0.03, -0.02), 0.0094, places=4)
        self.assertAlmostEqual(nir_exact(-0.01, -0.02), -0.0298, places=4)

    def test_invalid_inputs(self):
        """Test nir_exact with invalid inputs."""
        with self.assertRaises(TypeError):
            nir_exact("0.03", 0.02)
        with self.assertRaises(TypeError):
            nir_exact(0.03, "0.02")
        with self.assertRaises(TypeError):
            nir_exact(None, 0.02)


if __name__ == '__main__':
    unittest.main()
