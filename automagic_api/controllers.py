from automagic_api import app, s, manager
from automagic_api.models\
    import Features, Policy

policy_api_blueprint = manager.create_api_blueprint(Policy,
        methods=['GET', 'PATCH', 'POST', 'DELETE'])

features_api_blueprint = manager.create_api_blueprint(Features,
        methods=['GET', 'PATCH', 'POST', 'DELETE'])
