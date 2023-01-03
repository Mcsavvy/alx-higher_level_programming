alias pyfile="mkfile -AEXs '/usr/bin/python3'"
alias tpyfile="mkfile -IEXs '/usr/bin/python3'"
alias testfile="mkfile -IE"
alias projfile="mkfile -AE"
alias pyrun='python3 -c "$(xclip -o)"'

function pastefile {
	xclip -o > "$1"
}

function gitsend {
	git add . && git commit -m "$1" && git push
}

function gitammend {
	git add . && git commit -C HEAD --amend && git push -f
}

function newproject {
	mkdir "$1" && cd "$1" && echo "# $2" > README.md && gitignore __pycache__ && git add . && git commit -m "Setup For $1"
}
