"""
Unit tests for Quantum Financial System (QFS)

Tests all five key features:
1. Quantum-Resistant Blockchain
2. Rose Gold Encryption
3. Automated Wealth Distribution
4. NESARA/GESARA Compliance
5. Galactic Federation Framework
"""

import unittest
from qfs import (
    QuantumBlockchain,
    RoseGoldEncryption,
    WealthDistributor,
    NESARAGESARACompliance,
    GalacticFederationFramework
)
from qfs.wealth_distribution.distribution_algorithm import (
    Participant,
    DistributionStrategy
)
from qfs.galactic_framework.federation_framework import DimensionType


class TestQuantumBlockchain(unittest.TestCase):
    """Test Quantum-Resistant Blockchain."""
    
    def setUp(self):
        self.blockchain = QuantumBlockchain(difficulty=2)
    
    def test_genesis_block(self):
        """Test genesis block creation."""
        self.assertEqual(len(self.blockchain.chain), 1)
        self.assertEqual(self.blockchain.chain[0].index, 0)
    
    def test_add_transaction(self):
        """Test adding transactions."""
        self.blockchain.add_transaction({
            "from": "alice",
            "to": "bob",
            "amount": 100
        })
        self.assertEqual(len(self.blockchain.pending_transactions), 1)
    
    def test_mine_block(self):
        """Test mining blocks."""
        self.blockchain.add_transaction({
            "from": "alice",
            "to": "bob",
            "amount": 100
        })
        block = self.blockchain.mine_pending_transactions("miner")
        self.assertTrue(block.hash.startswith("0" * self.blockchain.difficulty))
    
    def test_chain_validation(self):
        """Test blockchain validation."""
        self.blockchain.add_transaction({
            "from": "alice",
            "to": "bob",
            "amount": 100
        })
        self.blockchain.mine_pending_transactions("miner")
        self.assertTrue(self.blockchain.is_chain_valid())
    
    def test_balance_calculation(self):
        """Test balance calculation."""
        self.blockchain.add_transaction({
            "from": "system",
            "to": "alice",
            "amount": 100
        })
        self.blockchain.mine_pending_transactions("miner")
        balance = self.blockchain.get_balance("alice")
        self.assertEqual(balance, 100)


class TestRoseGoldEncryption(unittest.TestCase):
    """Test Rose Gold Triple-Layer Encryption."""
    
    def setUp(self):
        self.encryption = RoseGoldEncryption("test_master_key")
    
    def test_encrypt_decrypt(self):
        """Test encryption and decryption."""
        plaintext = "Test data for QFS"
        encrypted = self.encryption.encrypt(plaintext)
        decrypted, verified = self.encryption.decrypt(encrypted)
        
        self.assertEqual(plaintext, decrypted)
        self.assertTrue(verified)
    
    def test_integrity_verification(self):
        """Test data integrity verification."""
        plaintext = "Sensitive financial data"
        encrypted = self.encryption.encrypt(plaintext)
        
        # Tamper with encrypted data
        tampered = encrypted[:-10] + "xxxxxxxxxx"
        decrypted, verified = self.encryption.decrypt(tampered)
        
        self.assertFalse(verified)
        self.assertIsNone(decrypted)
    
    def test_key_rotation(self):
        """Test key rotation."""
        old_hash = self.encryption.get_master_key_hash()
        new_hash = self.encryption.rotate_keys()
        self.assertNotEqual(old_hash, new_hash)


class TestWealthDistribution(unittest.TestCase):
    """Test Automated Wealth Distribution."""
    
    def setUp(self):
        self.distributor = WealthDistributor()
        self.participants = [
            Participant(address="p1", stake=100, need_score=0.5, contribution_score=50),
            Participant(address="p2", stake=200, need_score=0.8, contribution_score=30),
        ]
    
    def test_equal_distribution(self):
        """Test equal distribution."""
        allocation = self.distributor.distribute(
            1000,
            self.participants,
            DistributionStrategy.EQUAL
        )
        
        # Each should get 500
        for amount in allocation.values():
            self.assertEqual(amount, 500)
    
    def test_proportional_distribution(self):
        """Test proportional distribution."""
        allocation = self.distributor.distribute(
            1000,
            self.participants,
            DistributionStrategy.PROPORTIONAL
        )
        
        # Total should equal input
        self.assertAlmostEqual(sum(allocation.values()), 1000)
    
    def test_galactic_abundance_distribution(self):
        """Test galactic abundance distribution."""
        allocation = self.distributor.distribute(
            1000,
            self.participants,
            DistributionStrategy.GALACTIC_ABUNDANCE
        )
        
        # Total should equal input
        self.assertAlmostEqual(sum(allocation.values()), 1000)
        
        # All participants should receive something
        for amount in allocation.values():
            self.assertGreater(amount, 0)
    
    def test_gini_coefficient(self):
        """Test Gini coefficient calculation."""
        equal_allocation = {"p1": 100, "p2": 100}
        unequal_allocation = {"p1": 180, "p2": 20}
        
        equal_gini = self.distributor.calculate_gini_coefficient(equal_allocation)
        unequal_gini = self.distributor.calculate_gini_coefficient(unequal_allocation)
        
        # Equal distribution should have Gini close to 0
        self.assertAlmostEqual(equal_gini, 0.0, places=2)
        # Unequal distribution should have higher Gini (without abs)
        self.assertGreater(unequal_gini, equal_gini)


class TestNESARAGESARACompliance(unittest.TestCase):
    """Test NESARA/GESARA Compliance."""
    
    def setUp(self):
        self.compliance = NESARAGESARACompliance()
    
    def test_compliant_transaction(self):
        """Test compliant transaction."""
        transaction = {
            "from": "treasury",
            "to": "citizen",
            "amount": 1000,
            "type": "debt_forgiveness",
            "redistribution_enabled": True,
            "consent": True,
            "quantum_secure": True,
            "galactic_compliant": True
        }
        
        report = self.compliance.check_compliance("entity_001", transaction)
        self.assertTrue(report["compliant"])
        self.assertEqual(len(report["violations"]), 0)
    
    def test_non_compliant_transaction(self):
        """Test non-compliant transaction."""
        transaction = {
            "from": "treasury",
            "to": "citizen",
            "amount": 1000,
            "type": "transfer",
            "redistribution_enabled": False,
            "consent": False
        }
        
        report = self.compliance.check_compliance("entity_002", transaction)
        # Should have some violations
        self.assertGreater(len(report["violations"]), 0)
    
    def test_exemption(self):
        """Test compliance exemptions."""
        self.compliance.add_exemption("entity_003", "DEBT_ELIMINATION")
        
        transaction = {
            "from": "treasury",
            "to": "citizen",
            "amount": -100  # Would normally fail
        }
        
        report = self.compliance.check_compliance("entity_003", transaction)
        # DEBT_ELIMINATION should be exempt
        self.assertEqual(
            report["detailed_results"]["DEBT_ELIMINATION"]["status"],
            "exempt"
        )
    
    def test_get_rules(self):
        """Test getting compliance rules."""
        rules = self.compliance.get_rules()
        self.assertGreater(len(rules), 0)
        self.assertIn("rule_id", rules[0])


class TestGalacticFederationFramework(unittest.TestCase):
    """Test Galactic Federation Framework."""
    
    def setUp(self):
        self.framework = GalacticFederationFramework()
    
    def test_deposit_treasury(self):
        """Test depositing to galactic treasury."""
        balance = self.framework.deposit_to_galactic_treasury(10000)
        self.assertEqual(balance, 10000)
    
    def test_anchor_portal(self):
        """Test anchoring abundance portal."""
        portal = self.framework.anchor_abundance_portal(
            "test_portal",
            DimensionType.QUANTUM,
            5000,
            {"x": 0, "y": 0, "z": 0, "dimensional_frequency": 432.0}
        )
        
        self.assertEqual(portal.portal_id, "test_portal")
        self.assertEqual(portal.dimension, DimensionType.QUANTUM)
    
    def test_activate_portal(self):
        """Test portal activation."""
        self.framework.anchor_abundance_portal(
            "test_portal",
            DimensionType.QUANTUM,
            5000,
            {"x": 0, "y": 0, "z": 0, "dimensional_frequency": 432.0}
        )
        
        activated = self.framework.activate_portal("test_portal")
        self.assertTrue(activated)
    
    def test_synchronize_portals(self):
        """Test portal synchronization."""
        # Create and activate portal
        self.framework.anchor_abundance_portal(
            "test_portal",
            DimensionType.QUANTUM,
            5000,
            {"x": 0, "y": 0, "z": 0, "dimensional_frequency": 432.0}
        )
        self.framework.activate_portal("test_portal")
        
        sync_report = self.framework.synchronize_portals()
        self.assertGreater(sync_report["active_portals"], 0)
    
    def test_distribute_galactic_abundance(self):
        """Test galactic abundance distribution."""
        self.framework.deposit_to_galactic_treasury(10000)
        
        recipients = ["citizen_1", "citizen_2", "citizen_3"]
        allocation = self.framework.distribute_galactic_abundance(3000, recipients)
        
        # Each should get equal share
        for amount in allocation.values():
            self.assertEqual(amount, 1000)
    
    def test_federation_compliance(self):
        """Test Federation compliance verification."""
        # Setup compliant state
        self.framework.deposit_to_galactic_treasury(10000)
        self.framework.anchor_abundance_portal(
            "test_portal",
            DimensionType.QUANTUM,
            5000,
            {"x": 0, "y": 0, "z": 0, "dimensional_frequency": 432.0}
        )
        self.framework.activate_portal("test_portal")
        
        verification = self.framework.verify_federation_compliance()
        self.assertIn("compliant", verification)


def run_tests():
    """Run all tests."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestQuantumBlockchain))
    suite.addTests(loader.loadTestsFromTestCase(TestRoseGoldEncryption))
    suite.addTests(loader.loadTestsFromTestCase(TestWealthDistribution))
    suite.addTests(loader.loadTestsFromTestCase(TestNESARAGESARACompliance))
    suite.addTests(loader.loadTestsFromTestCase(TestGalacticFederationFramework))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
