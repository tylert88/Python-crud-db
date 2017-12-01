import os
from automagic_api import app


port = int(os.environ.get("PORT", 33507))
print("port:")
print(port)
app.run(host='0.0.0.0', port=port, debug=True)
