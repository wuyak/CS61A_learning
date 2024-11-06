# 默认提交信息
DEFAULT_MSG = "Auto commit by Makefile"

# 默认目标：执行 add、commit 和 push
default: add commit push

# 添加所有更改到暂存区
add:
	git add .

# 自动提交更改
commit:
	@if git diff --cached --quiet; then \
		echo "No changes to commit."; \
	else \
		git commit -m "$(if $(COMMIT_MSG),$(COMMIT_MSG),$(DEFAULT_MSG))"; \
	fi

# 推送更改到远程仓库
push:
	git push

# 防止 make 将提交信息视为目标并报错
%:
	@:
