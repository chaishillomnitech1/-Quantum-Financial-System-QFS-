"""
Rose Gold Encryption - Triple-Layer Security

This module implements a triple-layer encryption system using multiple
algorithms for enhanced security.
"""

import hashlib
import secrets
from typing import Tuple, Optional
from base64 import b64encode, b64decode


class RoseGoldEncryption:
    """
    Triple-Layer Security Encryption System.
    
    Implements three layers of encryption:
    1. XOR-based symmetric encryption (Layer 1)
    2. Substitution cipher with key (Layer 2) 
    3. SHA3-256 integrity verification (Layer 3)
    
    Features:
    - Multi-layer encryption for enhanced security
    - Quantum-resistant hash functions
    - Secure key generation
    - Data integrity verification
    """
    
    def __init__(self, master_key: Optional[str] = None):
        """
        Initialize Rose Gold Encryption.
        
        Args:
            master_key: Optional master encryption key. If not provided, generates one.
        """
        if master_key:
            self.master_key = master_key.encode()
        else:
            self.master_key = self._generate_master_key()
        
        # Generate layer-specific keys from master key
        self.layer1_key = hashlib.sha3_256(self.master_key + b"layer1").digest()
        self.layer2_key = hashlib.sha3_256(self.master_key + b"layer2").digest()
        self.layer3_key = hashlib.sha3_256(self.master_key + b"layer3").digest()
    
    @staticmethod
    def _generate_master_key(length: int = 32) -> bytes:
        """
        Generate a secure master key.
        
        Args:
            length: Key length in bytes
            
        Returns:
            Randomly generated key
        """
        return secrets.token_bytes(length)
    
    def _layer1_encrypt(self, data: bytes) -> bytes:
        """
        Layer 1: XOR-based encryption.
        
        Args:
            data: Data to encrypt
            
        Returns:
            Encrypted data
        """
        key_len = len(self.layer1_key)
        return bytes([data[i] ^ self.layer1_key[i % key_len] for i in range(len(data))])
    
    def _layer1_decrypt(self, data: bytes) -> bytes:
        """
        Layer 1: XOR-based decryption (same as encryption).
        
        Args:
            data: Data to decrypt
            
        Returns:
            Decrypted data
        """
        return self._layer1_encrypt(data)  # XOR is symmetric
    
    def _layer2_encrypt(self, data: bytes) -> bytes:
        """
        Layer 2: Substitution cipher encryption.
        
        Args:
            data: Data to encrypt
            
        Returns:
            Encrypted data
        """
        key_len = len(self.layer2_key)
        return bytes([(data[i] + self.layer2_key[i % key_len]) % 256 for i in range(len(data))])
    
    def _layer2_decrypt(self, data: bytes) -> bytes:
        """
        Layer 2: Substitution cipher decryption.
        
        Args:
            data: Data to decrypt
            
        Returns:
            Decrypted data
        """
        key_len = len(self.layer2_key)
        return bytes([(data[i] - self.layer2_key[i % key_len]) % 256 for i in range(len(data))])
    
    def _layer3_sign(self, data: bytes) -> bytes:
        """
        Layer 3: Create quantum-resistant signature.
        
        Args:
            data: Data to sign
            
        Returns:
            Signature hash
        """
        return hashlib.sha3_256(data + self.layer3_key).digest()
    
    def _layer3_verify(self, data: bytes, signature: bytes) -> bool:
        """
        Layer 3: Verify data integrity.
        
        Args:
            data: Original data
            signature: Signature to verify
            
        Returns:
            True if signature is valid
        """
        expected_signature = self._layer3_sign(data)
        return secrets.compare_digest(expected_signature, signature)
    
    def encrypt(self, plaintext: str) -> str:
        """
        Encrypt data using triple-layer Rose Gold encryption.
        
        Args:
            plaintext: Data to encrypt
            
        Returns:
            Base64-encoded encrypted data with signature
        """
        # Convert to bytes
        data = plaintext.encode('utf-8')
        
        # Apply Layer 1 encryption
        encrypted = self._layer1_encrypt(data)
        
        # Apply Layer 2 encryption
        encrypted = self._layer2_encrypt(encrypted)
        
        # Apply Layer 3 signature
        signature = self._layer3_sign(encrypted)
        
        # Combine encrypted data and signature
        combined = encrypted + signature
        
        # Encode to base64 for safe transmission
        return b64encode(combined).decode('utf-8')
    
    def decrypt(self, ciphertext: str) -> Tuple[Optional[str], bool]:
        """
        Decrypt data using triple-layer Rose Gold decryption.
        
        Args:
            ciphertext: Base64-encoded encrypted data
            
        Returns:
            Tuple of (decrypted data, verification status)
            Returns (None, False) if verification fails
        """
        try:
            # Decode from base64
            combined = b64decode(ciphertext.encode('utf-8'))
            
            # Split encrypted data and signature (SHA3-256 produces 32 bytes)
            encrypted = combined[:-32]
            signature = combined[-32:]
            
            # Verify Layer 3 signature
            if not self._layer3_verify(encrypted, signature):
                return None, False
            
            # Apply Layer 2 decryption
            decrypted = self._layer2_decrypt(encrypted)
            
            # Apply Layer 1 decryption
            decrypted = self._layer1_decrypt(decrypted)
            
            # Convert to string
            plaintext = decrypted.decode('utf-8')
            
            return plaintext, True
            
        except Exception:
            return None, False
    
    def get_master_key_hash(self) -> str:
        """
        Get hash of master key for verification.
        
        Returns:
            Hex-encoded hash of master key
        """
        return hashlib.sha3_256(self.master_key).hexdigest()
    
    def rotate_keys(self, new_master_key: Optional[str] = None) -> str:
        """
        Rotate encryption keys.
        
        Args:
            new_master_key: Optional new master key
            
        Returns:
            Hash of new master key
        """
        if new_master_key:
            self.master_key = new_master_key.encode()
        else:
            self.master_key = self._generate_master_key()
        
        # Regenerate layer keys
        self.layer1_key = hashlib.sha3_256(self.master_key + b"layer1").digest()
        self.layer2_key = hashlib.sha3_256(self.master_key + b"layer2").digest()
        self.layer3_key = hashlib.sha3_256(self.master_key + b"layer3").digest()
        
        return self.get_master_key_hash()
