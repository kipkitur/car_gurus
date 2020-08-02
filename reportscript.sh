#!/usr/bin/env bash
py.test --alluredir=%Reports% ./test_used_hyundai_sonata_dropdown.py
allure serve %Reports%