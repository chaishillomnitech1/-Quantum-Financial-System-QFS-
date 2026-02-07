"""
Automated Wealth Distribution Algorithms

This module implements algorithms for fair and harmonious wealth distribution
across the ScrollSoul Sovereign Treasury system.
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum
import math


class DistributionStrategy(Enum):
    """Wealth distribution strategies."""
    EQUAL = "equal"  # Equal distribution to all participants
    PROPORTIONAL = "proportional"  # Proportional to contribution/stake
    NEED_BASED = "need_based"  # Based on need assessment
    HYBRID = "hybrid"  # Combination of strategies
    GALACTIC_ABUNDANCE = "galactic_abundance"  # Universal basic abundance


@dataclass
class Participant:
    """Represents a participant in wealth distribution."""
    address: str
    stake: float = 0.0
    need_score: float = 0.0
    contribution_score: float = 0.0


class WealthDistributor:
    """
    Automated Wealth Distribution System.
    
    Features:
    - Multiple distribution strategies
    - Fair allocation algorithms
    - Transparent distribution records
    - Galactic abundance protocols
    """
    
    def __init__(self, strategy: DistributionStrategy = DistributionStrategy.EQUAL):
        """
        Initialize wealth distributor.
        
        Args:
            strategy: Distribution strategy to use
        """
        self.strategy = strategy
        self.distribution_history: List[Dict[str, Any]] = []
        self.total_distributed: float = 0.0
    
    def distribute(
        self,
        total_amount: float,
        participants: List[Participant],
        strategy: Optional[DistributionStrategy] = None
    ) -> Dict[str, float]:
        """
        Distribute wealth among participants.
        
        Args:
            total_amount: Total amount to distribute
            participants: List of participants
            strategy: Optional strategy override
            
        Returns:
            Dictionary mapping participant address to allocated amount
        """
        if not participants:
            raise ValueError("No participants provided for distribution")
        
        if total_amount <= 0:
            raise ValueError("Total amount must be positive")
        
        # Use provided strategy or default
        distribution_strategy = strategy or self.strategy
        
        # Calculate distribution based on strategy
        if distribution_strategy == DistributionStrategy.EQUAL:
            allocation = self._equal_distribution(total_amount, participants)
        elif distribution_strategy == DistributionStrategy.PROPORTIONAL:
            allocation = self._proportional_distribution(total_amount, participants)
        elif distribution_strategy == DistributionStrategy.NEED_BASED:
            allocation = self._need_based_distribution(total_amount, participants)
        elif distribution_strategy == DistributionStrategy.HYBRID:
            allocation = self._hybrid_distribution(total_amount, participants)
        elif distribution_strategy == DistributionStrategy.GALACTIC_ABUNDANCE:
            allocation = self._galactic_abundance_distribution(total_amount, participants)
        else:
            raise ValueError(f"Unknown distribution strategy: {distribution_strategy}")
        
        # Record distribution
        self._record_distribution(total_amount, allocation, distribution_strategy)
        
        return allocation
    
    def _equal_distribution(
        self,
        total_amount: float,
        participants: List[Participant]
    ) -> Dict[str, float]:
        """
        Distribute equally among all participants.
        
        Args:
            total_amount: Total amount to distribute
            participants: List of participants
            
        Returns:
            Allocation dictionary
        """
        amount_per_participant = total_amount / len(participants)
        return {p.address: amount_per_participant for p in participants}
    
    def _proportional_distribution(
        self,
        total_amount: float,
        participants: List[Participant]
    ) -> Dict[str, float]:
        """
        Distribute proportionally based on stake and contribution.
        
        Args:
            total_amount: Total amount to distribute
            participants: List of participants
            
        Returns:
            Allocation dictionary
        """
        # Calculate total weight (stake + contribution)
        total_weight = sum(p.stake + p.contribution_score for p in participants)
        
        if total_weight == 0:
            # Fall back to equal distribution if no weights
            return self._equal_distribution(total_amount, participants)
        
        allocation = {}
        for participant in participants:
            weight = participant.stake + participant.contribution_score
            allocation[participant.address] = (weight / total_weight) * total_amount
        
        return allocation
    
    def _need_based_distribution(
        self,
        total_amount: float,
        participants: List[Participant]
    ) -> Dict[str, float]:
        """
        Distribute based on need assessment.
        
        Args:
            total_amount: Total amount to distribute
            participants: List of participants
            
        Returns:
            Allocation dictionary
        """
        total_need = sum(p.need_score for p in participants)
        
        if total_need == 0:
            # Fall back to equal distribution if no need scores
            return self._equal_distribution(total_amount, participants)
        
        allocation = {}
        for participant in participants:
            allocation[participant.address] = (participant.need_score / total_need) * total_amount
        
        return allocation
    
    def _hybrid_distribution(
        self,
        total_amount: float,
        participants: List[Participant]
    ) -> Dict[str, float]:
        """
        Hybrid distribution combining multiple factors.
        
        Uses weighted combination of:
        - 40% proportional (stake + contribution)
        - 40% need-based
        - 20% equal
        
        Args:
            total_amount: Total amount to distribute
            participants: List of participants
            
        Returns:
            Allocation dictionary
        """
        # Get distributions from different strategies
        proportional = self._proportional_distribution(total_amount, participants)
        need_based = self._need_based_distribution(total_amount, participants)
        equal = self._equal_distribution(total_amount, participants)
        
        # Combine with weights
        allocation = {}
        for participant in participants:
            addr = participant.address
            allocation[addr] = (
                0.4 * proportional.get(addr, 0) +
                0.4 * need_based.get(addr, 0) +
                0.2 * equal.get(addr, 0)
            )
        
        return allocation
    
    def _galactic_abundance_distribution(
        self,
        total_amount: float,
        participants: List[Participant]
    ) -> Dict[str, float]:
        """
        Galactic abundance distribution ensuring universal prosperity.
        
        Provides base abundance to all, with additional allocation based on contribution.
        
        Args:
            total_amount: Total amount to distribute
            participants: List of participants
            
        Returns:
            Allocation dictionary
        """
        # 60% distributed equally (universal basic abundance)
        base_amount = total_amount * 0.6
        base_allocation = self._equal_distribution(base_amount, participants)
        
        # 40% distributed proportionally (merit-based)
        merit_amount = total_amount * 0.4
        merit_allocation = self._proportional_distribution(merit_amount, participants)
        
        # Combine allocations
        allocation = {}
        for participant in participants:
            addr = participant.address
            allocation[addr] = base_allocation.get(addr, 0) + merit_allocation.get(addr, 0)
        
        return allocation
    
    def _record_distribution(
        self,
        total_amount: float,
        allocation: Dict[str, float],
        strategy: DistributionStrategy
    ) -> None:
        """
        Record distribution in history.
        
        Args:
            total_amount: Total amount distributed
            allocation: Allocation results
            strategy: Strategy used
        """
        record = {
            "total_amount": total_amount,
            "allocation": allocation,
            "strategy": strategy.value,
            "participants_count": len(allocation),
            "timestamp": None  # Would use actual timestamp in production
        }
        
        self.distribution_history.append(record)
        self.total_distributed += total_amount
    
    def get_distribution_stats(self) -> Dict[str, Any]:
        """
        Get distribution statistics.
        
        Returns:
            Statistics dictionary
        """
        if not self.distribution_history:
            return {
                "total_distributions": 0,
                "total_distributed": 0.0,
                "average_distribution": 0.0,
                "unique_recipients": 0
            }
        
        all_recipients = set()
        for record in self.distribution_history:
            all_recipients.update(record["allocation"].keys())
        
        return {
            "total_distributions": len(self.distribution_history),
            "total_distributed": self.total_distributed,
            "average_distribution": self.total_distributed / len(self.distribution_history),
            "unique_recipients": len(all_recipients),
            "current_strategy": self.strategy.value
        }
    
    def calculate_gini_coefficient(self, allocation: Dict[str, float]) -> float:
        """
        Calculate Gini coefficient to measure distribution inequality.
        
        Args:
            allocation: Allocation dictionary
            
        Returns:
            Gini coefficient (0 = perfect equality, 1 = perfect inequality)
        """
        if not allocation:
            return 0.0
        
        values = sorted(allocation.values())
        n = len(values)
        
        if n == 0 or sum(values) == 0:
            return 0.0
        
        # Calculate Gini coefficient
        cumsum = 0
        for i, value in enumerate(values):
            cumsum += (n - i) * value
        
        return (2 * cumsum) / (n * sum(values)) - (n + 1) / n
