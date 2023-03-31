alias pyfile="mkfile -AEXs '/usr/bin/python3'"
alias tpyfile="mkfile -IEXs '/usr/bin/python3'"
alias testfile="mkfile -IE"
alias projfile="mkfile -AE"
alias pyrun='python3 -c "$(xclip -o)"'

function pastefile {
	xclip -o > "$1"
}

function gitsend {
	git add .
       	git commit -m "$1"
	git push
}

function gitammend {
	git commit -aC HEAD --amend
	git push -f
}

function newproject {
	mkdir "$1"
	cd "$1"
       	echo "# $2" > README.md
       	echo '__pycache__' > .gitignore
	git add .
	git commit -m "Setup For $1"
}
