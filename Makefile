
# Setup and run.
iar:
	chmod +x installer.sh && ./installer.sh

# Run backend using uvicorn.
startdev:
	cd src && poetry run uvicorn app:app --reload

# Push changes to git.
git:
	git add .
	git commit -m "$t" -m "$d"
	git push -u origin main


# Start docker compose server using 'docker compose' utility with variables from '.env' file.
startdocker:
	docker compose --env-file .env up


# Install requirements using poetry utility.
install_req:
	poetry install


# Delete '.DS_Store' and '__pycache__' files.
clean:
	find . -type d -name __pycache__ -exec rm -r {} \+ && find . -name ".DS_Store" -delete
