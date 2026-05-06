# Cloud Resume Challenge - Project Brief

## Overview

An online resume and IT portfolio hosted at **resume.sam-gardner.com**, built as an adaptation of the Cloud Resume Challenge. The frontend is hosted on Hostinger, DNS is managed through Cloudflare, and the backend (visitor counter) runs on AWS serverless infrastructure. The project is fully open source on GitHub with CI/CD pipelines via GitHub Actions.

AI assistance is not hidden. A note in the footer and a PROCESS.md in the repo document what was architected by the human and what was written by AI. This is a deliberate framing choice.

---

## Goals

- A public-facing resume and portfolio that shows a hiring manager both the person and the infrastructure competency
- A live CI/CD pipeline visible on GitHub that demonstrates real DevOps practice
- AWS backend skills signal (Lambda, API Gateway, DynamoDB) without paying for redundant hosting
- Something that looks like a human made it, not a template dump

---

## Architecture

```
resume.sam-gardner.com (Cloudflare DNS)
        |
        v
Hostinger (static frontend hosting)
        |
        | fetch()
        v
AWS API Gateway (HTTPS endpoint)
        |
        v
AWS Lambda (Python, visitor counter logic)
        |
        v
AWS DynamoDB (visitor count table, on-demand pricing)
```

### Frontend
- Static HTML/CSS/JS site based on BootstrapMade MyResume template
- Hosted on Hostinger
- Deployed via GitHub Actions on push to main
- Cloudflare handles DNS, no Route 53 needed

### Backend
- Single Lambda function written in Python (boto3)
- Reads and increments visitor count in DynamoDB
- Exposed via API Gateway (HTTPS)
- No authentication required (public read/increment endpoint)
- CORS configured to allow requests from resume.sam-gardner.com only
- Deployed via GitHub Actions using AWS SAM on push to main

### AWS Services Used
- Lambda (permanent free tier, 1M requests/month)
- API Gateway (1M calls/month free for 12 months, then ~$0)
- DynamoDB (permanent free tier, on-demand pricing)
- Estimated cost: $0/year

---

## Repository Structure

Two GitHub repositories:

### `cloud-resume-frontend`
```
/
├── index.html
├── assets/
│   ├── css/
│   │   └── main.css
│   ├── js/
│   │   └── main.js
│   ├── img/
│   └── vendor/
├── PROCESS.md
└── .github/
    └── workflows/
        └── deploy.yml        # deploys to Hostinger on push to main
```

### `cloud-resume-backend`
```
/
├── template.yaml             # AWS SAM template
├── visitor_counter/
│   └── app.py                # Lambda function
├── tests/
│   └── test_app.py           # basic smoke tests
└── .github/
    └── workflows/
        └── deploy.yml        # runs tests, deploys SAM on push to main
```

---

## CI/CD

### Frontend Pipeline (GitHub Actions)
Trigger: push to main on `cloud-resume-frontend`
Steps:
1. Checkout code
2. Deploy to Hostinger via FTP/SFTP using Hostinger credentials stored as GitHub secrets
3. Done

### Backend Pipeline (GitHub Actions)
Trigger: push to main on `cloud-resume-backend`
Steps:
1. Checkout code
2. Set up Python
3. Run tests (`pytest tests/`)
4. If tests pass: package and deploy SAM application to AWS
5. Uses AWS credentials stored as GitHub secrets (never committed to repo)

---

## AWS Setup Notes

- Use AWS SAM CLI for backend infrastructure definition
- DynamoDB table: `visitor-count`, partition key `id` (string), single item with key `"visitors"`
- Lambda function reads current count, increments by 1, returns new count
- API Gateway: single GET endpoint `/visitors`
- CORS: restrict origin to `https://resume.sam-gardner.com`
- IAM: Lambda execution role with minimum permissions (DynamoDB read/write on that table only)
- Do NOT commit AWS credentials. Use GitHub Actions secrets: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`

---

## Section Map

### Keep (structural changes only)
- **Hero** - update content, keep typed.js and layout
- **About** - keep two-column layout, swap all placeholder content
- **Resume** - keep timeline layout, update all content
- **Contact** - strip the PHP form, replace with link cards (LinkedIn, GitHub, Email)
- **Footer** - update name, add AI transparency note

### Repurpose
- **Stats** → **Certifications** - replace animated counters with cert badges (CompTIA A+, Security+), Credly links
- **Skills** - keep section, replace progress bars with grouped skill tags (no percentages)
- **Portfolio** → **Projects** - replace masonry image grid with project cards (Homelab Hawaii, Cloud Resume Challenge, Applied. [coming soon])
- **Services** → **What I Do** - replace generic service cards with 4 competency areas

### Cut
- **Testimonials** - remove entirely, not relevant

### Add
- **Visitor counter** - small badge element in hero or footer, calls AWS API endpoint
- **PROCESS.md** in repo - documents AI assistance, architectural decisions

---

## What I Do (Services Section Replacement)

Four competency cards replacing the six generic service cards:

1. **Infrastructure & Networking** - Firewall management, VLAN design, switching, DNS, VPN, WAN failover
2. **Systems & Endpoints** - Windows Server, Hyper-V, Active Directory, Entra ID, MDM (Jamf, Kandji, Mosyle)
3. **Cloud & Automation** - Azure, AWS, backup and DR (Veeam), scripting, CI/CD pipelines
4. **Self-Hosted & Homelab** - Proxmox, containerization, self-hosted services, network segmentation

---

## AI Transparency

Footer note (small text):
> "Built with AI assistance. Infrastructure decisions and content by Sam Gardner, code by Claude."

PROCESS.md in the frontend repo should document:
- What was designed/decided by the human (architecture, content, section structure, copy direction)
- What was written by AI (HTML/CSS modifications, Lambda function, GitHub Actions workflows, SAM template)
- Why this approach was chosen (honest signal: understands infrastructure, not selling himself as a developer)

---

## Hostinger Deployment Notes

- Use Hostinger's FTP credentials for GitHub Actions deployment
- Store as GitHub secrets: `FTP_SERVER`, `FTP_USERNAME`, `FTP_PASSWORD`
- Use `SamKirkland/FTP-Deploy-Action` or equivalent in the workflow
- Target directory: the public_html directory or subdomain folder for resume.sam-gardner.com
- Subdomain will need to be created in Hostinger's hPanel and pointed at Cloudflare nameservers

---

## Cloudflare DNS Notes

- Create CNAME record: `resume` → Hostinger server hostname
- Cloudflare proxy (orange cloud) is fine for the frontend
- No Route 53 required
- API Gateway endpoint is on AWS's domain, called directly from frontend JS

---

## Template Notes

- Base template: BootstrapMade MyResume (https://bootstrapmade.com/free-html-bootstrap-template-my-resume/)
- CSS is in `assets/css/main.css` (separate file, not included in this handoff)
- Vendor dependencies loaded from local `assets/vendor/` directory
- Bootstrap 5.3.3, AOS animations, Typed.js, Swiper, GLightbox, Isotope, PureCounter
- Swiper (testimonials) can be fully removed along with its initialization in main.js
- PureCounter (stats section) will be removed with the stats section
- Isotope (portfolio filtering) can be simplified or removed depending on final projects section design
