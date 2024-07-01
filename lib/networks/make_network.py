import os
import importlib as imp


def make_network(cfg):
    module = cfg.network_module
    path = cfg.network_path
    network = imp.import_module(module, path).Network()
    return network
