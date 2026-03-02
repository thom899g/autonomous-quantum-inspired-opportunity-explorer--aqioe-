"""
Autonomous Quantum-Inspired Opportunity Explorer (AQIOE)
Core system for identifying emerging trading opportunities using quantum-inspired algorithms.
"""
__version__ = "1.0.0"
__author__ = "Evolution Ecosystem AGI"

from .data_pipeline import MarketDataPipeline
from .quantum_optimizer import QuantumInspiredOptimizer
from .neuro_symbolic import NeuroSymbolicProcessor
from .strategy_executor import StrategyExecutor
from .adaptation_loop import AdaptationLoop
from .firebase_manager import FirebaseManager

__all__ = [
    'MarketDataPipeline',
    'QuantumInspiredOptimizer',
    'NeuroSymbolicProcessor',
    'StrategyExecutor', 
    'AdaptationLoop',
    'FirebaseManager'
]