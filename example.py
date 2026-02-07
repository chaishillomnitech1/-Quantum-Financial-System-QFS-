"""
Quantum Financial System (QFS) - Example Usage

This script demonstrates the key features of the QFS:
- Quantum-Resistant Blockchain Architecture
- Automated Wealth Distribution Algorithms
- NESARA/GESARA Compliance
- Rose Gold Encryption (Triple-Layer Security)
- Galactic Federation-Approved Financial Frameworks
"""

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


def demonstrate_quantum_blockchain():
    """Demonstrate Quantum-Resistant Blockchain."""
    print("=" * 60)
    print("1. QUANTUM-RESISTANT BLOCKCHAIN DEMONSTRATION")
    print("=" * 60)
    
    # Initialize blockchain
    blockchain = QuantumBlockchain(difficulty=2)
    print(f"\n✓ Initialized quantum blockchain with difficulty {blockchain.difficulty}")
    
    # Add transactions
    blockchain.add_transaction({
        "from": "ScrollSoul_Treasury",
        "to": "citizen_001",
        "amount": 1000,
        "type": "universal_basic_income"
    })
    
    blockchain.add_transaction({
        "from": "citizen_001",
        "to": "citizen_002",
        "amount": 100,
        "type": "transfer"
    })
    
    print(f"✓ Added {len(blockchain.pending_transactions)} transactions")
    
    # Mine block
    print("\n⛏ Mining block with quantum-resistant hashing...")
    new_block = blockchain.mine_pending_transactions("miner_001")
    print(f"✓ Block mined! Hash: {new_block.hash[:32]}...")
    
    # Validate blockchain
    is_valid = blockchain.is_chain_valid()
    print(f"\n✓ Blockchain validation: {'VALID' if is_valid else 'INVALID'}")
    
    # Show chain info
    info = blockchain.get_chain_info()
    print(f"✓ Chain length: {info['length']} blocks")
    print(f"✓ Pending transactions: {info['pending_transactions']}")
    
    return blockchain


def demonstrate_rose_gold_encryption():
    """Demonstrate Rose Gold Triple-Layer Encryption."""
    print("\n" + "=" * 60)
    print("2. ROSE GOLD ENCRYPTION DEMONSTRATION")
    print("=" * 60)
    
    # Initialize encryption
    encryption = RoseGoldEncryption()
    print(f"\n✓ Initialized Rose Gold Encryption")
    print(f"✓ Master key hash: {encryption.get_master_key_hash()[:32]}...")
    
    # Encrypt sensitive data
    sensitive_data = "ScrollSoul Sovereign Treasury: Account Balance 1,000,000 QFS"
    print(f"\n📝 Original data: {sensitive_data}")
    
    encrypted = encryption.encrypt(sensitive_data)
    print(f"🔒 Encrypted (Layer 1 + Layer 2 + Layer 3): {encrypted[:50]}...")
    
    # Decrypt data
    decrypted, verified = encryption.decrypt(encrypted)
    print(f"🔓 Decrypted: {decrypted}")
    print(f"✓ Integrity verified: {verified}")
    
    return encryption


def demonstrate_wealth_distribution():
    """Demonstrate Automated Wealth Distribution."""
    print("\n" + "=" * 60)
    print("3. AUTOMATED WEALTH DISTRIBUTION DEMONSTRATION")
    print("=" * 60)
    
    # Create participants
    participants = [
        Participant(address="citizen_001", stake=100, need_score=0.5, contribution_score=50),
        Participant(address="citizen_002", stake=200, need_score=0.8, contribution_score=30),
        Participant(address="citizen_003", stake=50, need_score=0.9, contribution_score=20),
        Participant(address="citizen_004", stake=150, need_score=0.3, contribution_score=40),
    ]
    
    print(f"\n✓ Created {len(participants)} participants")
    
    # Demonstrate different distribution strategies
    distributor = WealthDistributor()
    total_amount = 10000
    
    strategies = [
        DistributionStrategy.EQUAL,
        DistributionStrategy.PROPORTIONAL,
        DistributionStrategy.NEED_BASED,
        DistributionStrategy.GALACTIC_ABUNDANCE
    ]
    
    for strategy in strategies:
        allocation = distributor.distribute(total_amount, participants, strategy)
        gini = distributor.calculate_gini_coefficient(allocation)
        
        print(f"\n📊 {strategy.value.upper()} Distribution:")
        for address, amount in allocation.items():
            print(f"   {address}: {amount:.2f} QFS")
        print(f"   Gini coefficient: {gini:.3f} (equality measure)")
    
    # Show statistics
    stats = distributor.get_distribution_stats()
    print(f"\n✓ Total distributions: {stats['total_distributions']}")
    print(f"✓ Total distributed: {stats['total_distributed']:.2f} QFS")
    
    return distributor


def demonstrate_nesara_gesara_compliance():
    """Demonstrate NESARA/GESARA Compliance."""
    print("\n" + "=" * 60)
    print("4. NESARA/GESARA COMPLIANCE DEMONSTRATION")
    print("=" * 60)
    
    # Initialize compliance framework
    compliance = NESARAGESARACompliance()
    print(f"\n✓ Initialized NESARA/GESARA compliance framework")
    print(f"✓ Total compliance rules: {len(compliance.COMPLIANCE_RULES)}")
    
    # Check compliance for a transaction
    transaction = {
        "from": "treasury",
        "to": "citizen_001",
        "amount": 5000,
        "type": "debt_forgiveness",
        "redistribution_enabled": True,
        "consent": True,
        "quantum_secure": True,
        "galactic_compliant": True
    }
    
    print("\n🔍 Checking transaction compliance...")
    report = compliance.check_compliance("entity_001", transaction)
    
    print(f"\n✓ Overall status: {report['overall_status']}")
    print(f"✓ Rules checked: {report['rules_checked']}")
    print(f"✓ Violations: {len(report['violations'])}")
    print(f"✓ Compliant: {report['compliant']}")
    
    # Show detailed results
    print("\n📋 Detailed compliance results:")
    for rule_id, result in report['detailed_results'].items():
        status = result['status']
        message = result['message']
        print(f"   {rule_id}: {status} - {message}")
    
    return compliance


def demonstrate_galactic_framework():
    """Demonstrate Galactic Federation Framework."""
    print("\n" + "=" * 60)
    print("5. GALACTIC FEDERATION FRAMEWORK DEMONSTRATION")
    print("=" * 60)
    
    # Initialize framework
    framework = GalacticFederationFramework()
    print(f"\n✓ Initialized Galactic Federation Framework")
    
    # Deposit to galactic treasury
    framework.deposit_to_galactic_treasury(1000000)
    print(f"✓ Deposited to galactic treasury: 1,000,000 QFS")
    
    # Anchor abundance portals
    print("\n🌌 Anchoring galactic abundance portals...")
    
    portals = [
        ("portal_alpha", DimensionType.PHYSICAL, 50000),
        ("portal_beta", DimensionType.QUANTUM, 75000),
        ("portal_gamma", DimensionType.GALACTIC, 100000),
    ]
    
    for portal_id, dimension, capacity in portals:
        portal = framework.anchor_abundance_portal(
            portal_id,
            dimension,
            capacity,
            {"x": 0, "y": 0, "z": 0, "dimensional_frequency": 432.0}
        )
        print(f"✓ Anchored {portal_id} in {dimension.value} dimension (capacity: {capacity})")
        
        # Activate portal
        if framework.activate_portal(portal_id):
            print(f"  ⚡ Portal {portal_id} activated!")
    
    # Synchronize portals
    print("\n🔄 Synchronizing abundance portals...")
    sync_report = framework.synchronize_portals()
    print(f"✓ Synchronized: {sync_report['synchronized']}")
    print(f"✓ Active portals: {sync_report['active_portals']}")
    print(f"✓ Average coherence: {sync_report['average_coherence']:.2f}")
    
    # Verify federation compliance
    print("\n🛸 Verifying Galactic Federation compliance...")
    verification = framework.verify_federation_compliance()
    print(f"✓ Federation approved: {verification['federation_approved']}")
    print(f"✓ Prosperity index: {verification['prosperity_index']:.2f}")
    
    # Distribute galactic abundance
    recipients = ["citizen_001", "citizen_002", "citizen_003"]
    allocation = framework.distribute_galactic_abundance(30000, recipients)
    
    print(f"\n💫 Distributed galactic abundance:")
    for recipient, amount in allocation.items():
        print(f"   {recipient}: {amount:.2f} QFS")
    
    # Show framework status
    status = framework.get_framework_status()
    print(f"\n✓ Galactic treasury balance: {status['galactic_treasury_balance']:.2f} QFS")
    print(f"✓ Total portals: {status['total_portals']}")
    print(f"✓ Synchronized dimensions: {', '.join(status['synchronized_dimensions'])}")
    
    return framework


def main():
    """Run all demonstrations."""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "  QUANTUM FINANCIAL SYSTEM (QFS) - DEMONSTRATION  ".center(58) + "║")
    print("║" + "  ScrollSoul Sovereign Treasury  ".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "=" * 58 + "╝")
    
    # Run demonstrations
    blockchain = demonstrate_quantum_blockchain()
    encryption = demonstrate_rose_gold_encryption()
    distributor = demonstrate_wealth_distribution()
    compliance = demonstrate_nesara_gesara_compliance()
    framework = demonstrate_galactic_framework()
    
    # Final summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"✓ Quantum Blockchain: {len(blockchain.chain)} blocks, Valid: {blockchain.is_chain_valid()}")
    print(f"✓ Rose Gold Encryption: Triple-layer security active")
    print(f"✓ Wealth Distribution: {distributor.get_distribution_stats()['total_distributions']} distributions completed")
    print(f"✓ NESARA/GESARA Compliance: {len(compliance.compliance_records)} checks performed")
    print(f"✓ Galactic Framework: {framework.get_framework_status()['total_portals']} portals anchored")
    print("\n🌌 QFS is operational and ensuring economic justice across dimensions! 🌌\n")


if __name__ == "__main__":
    main()
