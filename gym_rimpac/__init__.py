#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from gym.envs.registration import register

register(
    id='Rimpac-v0',
    entry_point='gym_rimpac.envs:RimpacEnv',
    kwargs={
        'worker_id': 0,
        'base_port': None,
        'seed': 0,
        'no_graphics': False
    }
)

register(
    id='Mock-Rimpac-v0',
    entry_point='gym_rimpac.envs:MockRimpacEnv'
)