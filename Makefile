
 # @ Author: Hugo Chartier
 # @ Create Time: 2026-09-10 18:27:18
 # @ Modified by: Hugo Chartier
 # @ Modified time: 2026-09-10 18:33:45
 # @ Description:

GREEN = \033[1;32m
BLUE  = \033[1;34m
RED   = \033[1;31m
RESET = \033[0m

VENV = .venv
PIP = $(VENV)/bin/pip
RUN_CMD = $(VENV)/bin/run

all: install

install:
	@printf "$(BLUE)▶ Creating virtual environment...$(RESET)\n"
	python3 -m venv $(VENV)
	@printf "$(BLUE)▶ Installing project in development mode...$(RESET)\n"
	$(PIP) install -e .
	@printf "$(GREEN)✔ Project installed successfully!$(RESET)\n"

run:
	@printf "$(GREEN)▶ Starting simulation...$(RESET)\n"
	$(RUN_CMD)

clean:
	@printf "$(RED)▶ Cleaning Python temporary files...$(RESET)\n"
	@rm -rf src/__pycache__
	@rm -rf __pycache__
	@rm -rf *.egg-info
	@rm -rf build/ dist/
	@rm -rf .pytest_cache
	@rm -rf $(VENV)
	@printf "$(GREEN)✔ Cleanup complete!$(RESET)\n"

re: clean all

.PHONY: all install run clean re