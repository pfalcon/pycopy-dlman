HOST = nas
DEPLOY_DIR = dlman
#DEPLOY_DIR = .

all:

deploy: lib
	ssh $(HOST) mkdir -p $(DEPLOY_DIR)
	scp dlman.* $(HOST):$(DEPLOY_DIR)/
	scp config.py.nas $(HOST):$(DEPLOY_DIR)/config.py
	rsync -rtv --delete --delete-excluded --executability \
	    --exclude="*.egg-info" lib $(HOST):$(DEPLOY_DIR)/

# This target prepares snapshot of all dependency modules, for
# self-contained install
lib:
	PIP_MICROPY_DEST=$$PWD pip-micropython install -r requirements.txt
