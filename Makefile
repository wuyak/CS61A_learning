DEFAULT_MSG = "Auto commit by Makefile"

default: add commit push

add:
	git add .

commit:
	@if git diff --cached --quiet; then \
		echo "No changes to commit."; \
	else \
		git commit -m "$(if $(msg),$(msg),$(DEFAULT_MSG))"; \
	fi

push:
	git push

%:
	@:
