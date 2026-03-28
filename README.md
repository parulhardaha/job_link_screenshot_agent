<img width="805" height="619" alt="Screenshot 2026-03-28 at 2 10 14 AM" src="https://github.com/user-attachments/assets/f2f7c5ac-e2ef-460d-9b61-f539cb5ddce3" />



## Desciption
The project uses Python, Playwright, and smtplib (SMTP library) to automate the workflow.

After running the project, an email is received in the inbox using SMTP (Gmail server).

The email contains the list of URLs and their status (SUCCESS or FAILED).

Screenshots of successfully loaded webpages are attached in the email as image files.

## Configuration & secrets

This project expects a local `.env` file (not committed) with the following environment variables:

- `EMAIL` — the address that will send the report (e.g. your Gmail address)
- `APP_PASSWORD` — the app-specific password or SMTP password for the sending account
- `RECEIVER_EMAIL` — recipient address that will receive the report
- `DRY_RUN` — set to `1` (or `true`) to prevent sending email and instead print/save a preview

To set up locally:

1. Copy the example file and edit it:

```bash
cp .env.example .env
# Then edit .env and put your real values 
```

2. The repo already ignores `.env` (see `.gitignore`), so your secrets won't be committed by default.

3. For safe displays or demos, enable dry-run in `.env`:

```bash
DRY_RUN=1
```

4. Run the project:

```bash
python3 main.py
```
