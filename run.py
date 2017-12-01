import os

from automagic_api import app
# app.run(debug=True, host='0.0.0.0', port=5000)

port = int(os.environ.get("PORT", 33507))
app.run(debug=True, port=port)


# postgresql-graceful-65432
# https://bright-core.herokuapp.com/api/policy
