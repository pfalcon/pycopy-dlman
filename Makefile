HOST = nas
DEPLOY_DIR = dlman
#DEPLOY_DIR = .

all:

deploy:
	ssh $(HOST) mkdir -p $(DEPLOY_DIR)
	scp dlman.* $(HOST):$(DEPLOY_DIR)/
	scp config.py.nas $(HOST):$(DEPLOY_DIR)/config.py
	scp -r lib $(HOST):$(DEPLOY_DIR)/
