# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY

# IMPORTATION INTERNAL
from gamestonk_terminal.helper_classes import ModelsNamespace as _models
from gamestonk_terminal.forex.technical_analysis import ta_api


def test_models():
    assert isinstance(ta_api.models, _models)
