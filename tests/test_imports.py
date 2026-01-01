def test_imports():
    """
    Verifies that the core components are accessible through the package 
    structure as defined in the __init__.py files.
    """
    # Test Data module exports
    from ml_core.data import PCAMDataset, get_dataloaders
    
    # Test Models module exports
    from ml_core.models import MLP
    
    # Test Solver module exports
    from ml_core.solver import Trainer
    
    # Test Utils module exports
    from ml_core.utils import (
        ExperimentTracker, 
        load_config, 
        seed_everything, 
        setup_logger
    )
    
    assert True
