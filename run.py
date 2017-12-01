import os
from automagic_api import app

port = int(os.environ.get("PORT", 33507))
app.run(debug=True, port=port)

# app.run(debug=True, host='0.0.0.0', port=5000)
# postgresql-graceful-65432
# https://bright-core.herokuapp.com/api/policy
