#every functions from QuantumComputer are imported and used
#Functions are only imported from QuantumComputer
import math
from unittest.mock import MagicMock, patch
import numpy as np 
import pytest
from quantum_computer import * 


def test_quantum_computer_empty_input():
    arr = np.array([1.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j,
                    0.+0.j, 0.+0.j, 0.+0.j])
    comparison = np.array_equal(arr, quantum_computer(3,[]))
    assert comparison, "test_quantum_computer_empty_input failed"

def test_compute_matrix():
    m = [[0, 1], [1, 0]]
    arr = [[0., 1., 0., 0.],
     [1., 0., 0., 0.],
     [0., 0., 0., 1.],
     [0., 0., 1., 0.]]
    comparison = np.array_equal(compute_matrix(m, 2, 0), arr)
    assert comparison, "test_compute_matrix failed"

def test_mock_quantum_computer_one_not_gate():   
    not_gate = NotGate(0)
    not_gate.create_matrix = MagicMock(return_value= np.identity(4)) 
    arr = quantum_computer(2, [not_gate])
    assert np.array_equal(arr,[1., 0., 0., 0.]), """test_mock_quantum_computer_
    one_not_gate failed"""

test_mock_quantum_computer_one_not_gate()

def test_quantum_computer_one_not_gate():   
    arr = quantum_computer(2, [NotGate(0)])
    assert np.array_equal(arr, [0., 1., 0., 0.]), """test_quantum_computer_
    one_not_gate failed"""

def test_quantum_computer_one_hadamard_gate():
    arr = quantum_computer(1, [HadamardGate(0)])
    assert np.isclose(arr, [1/math.sqrt(2), 1/math.sqrt(2) ]).all(), """
    test_quantum_computer_one_hadamard_gate failed"""

def test_quatum_computer_multiple_gate_with_one_operand():
    arr = quantum_computer(1, [NotGate(0), HadamardGate(0)])
    assert np.isclose(arr, [1/math.sqrt(2), -1/math.sqrt(2) ]).all(), """
    test_quatum_computer_multiple_gate_with_one_operand failed""" 

def test_check():
    assert check(15, 2), """test_check failed """ 
    assert not check(16, 2), """test_check failed""" 

def test_oppo():
    assert oppo(16, 3) == 24, "test_check failed"
    assert oppo(15, 3) == 7, "test_check failed"

def test_cnot():
    arr = [[1., 0., 0., 0.],
     [0., 0., 0., 1.],
     [0., 0., 1., 0.],
     [0., 1., 0., 0.]]
    assert np.array_equal(compute_cnot(2, 0, 1), arr), "test_cnot failed"

def test_quantum_computer_multiple_gate():
    arr = quantum_computer(2, [NotGate(1), CNotGate(1, 0)])
    assert np.array_equal(arr, [0, 0, 0, 1]), """test_quantum_computer
    _multiple_gate failed"""
    
def test_compute_probability():
    arr = quantum_computer(1, [NotGate(0), HadamardGate(0)])
    assert np.isclose(compute_probability(arr), [0.5, 0.5]).all(), """test_compute_
    probability failed"""

