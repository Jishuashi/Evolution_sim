
 # @ Author: Hugo Chartier
 # @ Create Time: 2026-09-10 18:27:18
 # @ Modified by: Hugo Chartier
 # @ Modified time: 2026-09-10 18:33:45
 # @ Description:

GREEN = \033[1;32m
BLUE  = \033[1;34m
RED   = \033[1;31m
RESET = \033[0m

.PHONY: all install run clean re

all: install

install:
	@printf "$(BLUE)▶ Installing project in development mode...$(RESET)\n"
	pip install -e .
	@printf "$(GREEN)✔ Project installed successfully!$(RESET)\n"

run:
	@printf "$(GREEN)▶ Starting simulation...$(RESET)\n"
	run

clean:
	@printf "$(RED)▶ Cleaning Python temporary files...$(RESET)\n"
	@rm -rf src/__pycache__
	@rm -rf __pycache__
	@rm -rf *.egg-info
	@rm -rf build/ dist/
	@rm -rf .pytest_cache
	@printf "$(GREEN)✔ Cleanup complete!$(RESET)\n"

re: clean all