import importlib as imp
import os
from lib.datasets.dataset_catalog import DatasetCatalog


def _evaluator_factory(cfg):
    module = cfg.evaluator_module
    path = cfg.evaluator_path
    evaluator = imp.import_module(module, path).Evaluator()
    return evaluator


def make_evaluator(cfg):
    if cfg.skip_eval:
        return None
    else:
        return _evaluator_factory(cfg)
