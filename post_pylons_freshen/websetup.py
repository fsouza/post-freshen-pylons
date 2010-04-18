"""Setup the post_pylons_freshen application"""
import logging

import pylons.test

from post_pylons_freshen.config.environment import load_environment
from post_pylons_freshen.model.meta import Session, metadata

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup post_pylons_freshen here"""
    # Don't reload the app if it was loaded under the testing environment
    if not pylons.test.pylonsapp:
        load_environment(conf.global_conf, conf.local_conf)

    # Create the tables if they don't already exist
    metadata.create_all(bind=Session.bind)
