import setup_db  # to execute the script once at startup of a container
import api


print(' ### ### initialize setup_db from start.py')
setup_db.setup()

print(' ### ### run xapo app')
api.app.run(host='0.0.0.0', debug=False)
