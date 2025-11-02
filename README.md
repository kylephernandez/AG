# AllGhost Django Application

This repository contains a Django implementation of the AllGhost marketplace described in the accompanying product requirements document.

## Features

* Wallet-linked identities with extended user profiles and consent preferences.
* Multimodal data asset catalog supporting previews, access rules, and analytics snapshots.
* Marketplace workflow for listings, trade requests, settlements, and disputes.
* Communications layer with conversations, messages, notifications, and presence tracking.
* Compliance tooling covering audit logs, reports, moderation actions, and KYC records.

The project is structured as a multi-app Django project so each concern can evolve independently.

## Getting started

1. Create and activate a Python virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply database migrations and create a superuser:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```

## Running tests

```bash
python manage.py test
```

## Next steps

* Integrate real storage for asset payloads and preview generation pipelines.
* Connect wallet verification, escrow, and KYC providers.
* Build API serializers and frontend interfaces tailored to the PRD flows.
