"""
Quantum-Resistant Blockchain Architecture

This module implements a quantum-resistant blockchain using post-quantum
cryptographic algorithms to ensure security against quantum computer attacks.
"""

import hashlib
import json
import time
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field


@dataclass
class Block:
    """Represents a block in the quantum-resistant blockchain."""
    
    index: int
    timestamp: float
    transactions: List[Dict[str, Any]]
    previous_hash: str
    nonce: int = 0
    hash: str = field(default="", init=False)
    
    def __post_init__(self):
        """Calculate block hash after initialization."""
        if not self.hash:
            self.hash = self.calculate_hash()
    
    def calculate_hash(self) -> str:
        """
        Calculate quantum-resistant hash of the block.
        Uses SHA3-256 which is considered quantum-resistant.
        """
        block_data = {
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }
        block_string = json.dumps(block_data, sort_keys=True)
        return hashlib.sha3_256(block_string.encode()).hexdigest()
    
    def mine_block(self, difficulty: int = 4) -> None:
        """
        Mine the block using proof-of-work with quantum-resistant hashing.
        
        Args:
            difficulty: Number of leading zeros required in hash
        """
        target = "0" * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()


class QuantumBlockchain:
    """
    Quantum-Resistant Blockchain Implementation.
    
    Features:
    - Post-quantum cryptographic hash functions (SHA3-256)
    - Secure chain validation
    - Transaction management
    - Proof-of-work consensus
    """
    
    def __init__(self, difficulty: int = 4):
        """
        Initialize the quantum blockchain.
        
        Args:
            difficulty: Mining difficulty (number of leading zeros)
        """
        self.chain: List[Block] = []
        self.difficulty = difficulty
        self.pending_transactions: List[Dict[str, Any]] = []
        self.mining_reward = 100
        
        # Create genesis block
        self._create_genesis_block()
    
    def _create_genesis_block(self) -> None:
        """Create the first block in the blockchain."""
        genesis_block = Block(
            index=0,
            timestamp=time.time(),
            transactions=[{"type": "genesis", "message": "ScrollSoul Sovereign Treasury Genesis"}],
            previous_hash="0"
        )
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)
    
    def get_latest_block(self) -> Block:
        """Get the most recent block in the chain."""
        return self.chain[-1]
    
    def add_transaction(self, transaction: Dict[str, Any]) -> None:
        """
        Add a new transaction to pending transactions.
        
        Args:
            transaction: Transaction data to add
        """
        # Validate transaction has required fields
        if "from" not in transaction or "to" not in transaction or "amount" not in transaction:
            raise ValueError("Transaction must contain 'from', 'to', and 'amount' fields")
        
        self.pending_transactions.append(transaction)
    
    def mine_pending_transactions(self, miner_address: str) -> Block:
        """
        Mine all pending transactions into a new block.
        
        Args:
            miner_address: Address to receive mining reward
            
        Returns:
            The newly mined block
        """
        # Create new block with pending transactions
        new_block = Block(
            index=len(self.chain),
            timestamp=time.time(),
            transactions=self.pending_transactions.copy(),
            previous_hash=self.get_latest_block().hash
        )
        
        # Mine the block
        new_block.mine_block(self.difficulty)
        
        # Add to chain
        self.chain.append(new_block)
        
        # Reset pending transactions and add mining reward
        self.pending_transactions = [
            {
                "from": "system",
                "to": miner_address,
                "amount": self.mining_reward,
                "type": "mining_reward"
            }
        ]
        
        return new_block
    
    def get_balance(self, address: str) -> float:
        """
        Calculate the balance for a given address.
        
        Args:
            address: Address to calculate balance for
            
        Returns:
            Current balance
        """
        balance = 0
        
        for block in self.chain:
            for transaction in block.transactions:
                if transaction.get("from") == address:
                    balance -= transaction.get("amount", 0)
                if transaction.get("to") == address:
                    balance += transaction.get("amount", 0)
        
        return balance
    
    def is_chain_valid(self) -> bool:
        """
        Validate the entire blockchain.
        
        Returns:
            True if chain is valid, False otherwise
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            # Verify current block's hash
            if current_block.hash != current_block.calculate_hash():
                return False
            
            # Verify link to previous block
            if current_block.previous_hash != previous_block.hash:
                return False
            
            # Verify proof-of-work
            if not current_block.hash.startswith("0" * self.difficulty):
                return False
        
        return True
    
    def get_chain_info(self) -> Dict[str, Any]:
        """
        Get information about the blockchain.
        
        Returns:
            Dictionary containing chain statistics
        """
        return {
            "length": len(self.chain),
            "difficulty": self.difficulty,
            "is_valid": self.is_chain_valid(),
            "pending_transactions": len(self.pending_transactions),
            "latest_block": {
                "index": self.get_latest_block().index,
                "hash": self.get_latest_block().hash,
                "timestamp": self.get_latest_block().timestamp
            }
        }
