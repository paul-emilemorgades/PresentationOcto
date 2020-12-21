from multiple_knapsack import MakePacks
from instances import Instance, Object, SnapBack
from unittest.mock import MagicMock, patch
import pytest

def test_add_object():
    sb = SnapBack(0,50)
    obj = Object(0,12,15)
    sb.add_object(obj)
    assert sb.load == 12 , "test_add_object failed, wrong load"
    assert sb.utility, "test_add_object failed, wrong utility"