from behave import fixture, use_fixture
import os

# It is necessary to chage directory after one feature is done 
# due to working directory be previus testing envioroment.
def after_feature(context, feature):
    os.chdir('../')