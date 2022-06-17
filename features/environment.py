from behave import fixture, use_fixture
import os

def after_feature(context, feature):
    os.chdir('../')