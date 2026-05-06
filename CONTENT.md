# Cloud Resume - Content

All copy, resume content, and section text for the site. This is the source of truth for everything that appears on the page.

---

## Meta

- **Page title:** Sam Gardner | IT Engineer
- **Domain:** resume.sam-gardner.com

---

## Hero Section

**Name:** Sam Gardner

**Typed.js items** (cycling animated text after "I'm a"):
- Systems Thinker
- Systems Administrator
- Problem Slayer
- IT Engineer

**Social links:**
- LinkedIn: https://www.linkedin.com/in/samwgardner
- GitHub: https://github.com/Slammywhammy

*(Remove Twitter, Facebook, Instagram from template)*

---

## About Section

**Profile photo:** Photo of Sam and his Golden Retriever Rudy

**Headline:** IT Engineer & Systems Thinker

**Bio:**
IT professional running the show at a K-8 school in Denver, where "the show" means everything from the firewall to the faculty laptop that won't connect to the projector five minutes before class. I keep the lights on for a school full of kids and the educators who learn alongside them. Before IT I spent five years managing airline operations, which taught me that systems fail, people adapt, and the goal is always to minimize how much the second thing has to compensate for the first. I work best in environments where technology exists to serve people, not the other way around.

**Info block (left column):**
- **Role:** IT Engineer, MSP
- **Location:** Denver, CO
- **GitHub:** github.com/Slammywhammy
- **LinkedIn:** linkedin.com/in/samwgardner

**Info block (right column):**
- **Credly:** credly.com/users/sam-gardner.e5311d46
- **Currently:** CompTIA A+, Security+ certified
- **In Progress:** Cisco CCNA (est. completion Q3 2026)
- **Open to:** New opportunities

*(Remove Birthday, Phone, Website, Freelance fields from template)*

---

## Certifications Section

*(Replaces the Stats/counters section entirely)*

**Section title:** Certifications

Two certification cards:

**Card 1:**
- Name: CompTIA Security+
- Issuer: CompTIA
- Badge image: [from Credly]
- Verify link: https://www.credly.com/badges/e164290b-c67f-48fc-8249-db336e3e9dfd/public_url

**Card 2:**
- Name: CompTIA A+
- Issuer: CompTIA
- Badge image: [from Credly]
- Verify link: https://www.credly.com/badges/77ab0bbb-0f10-45ff-9009-61bcfb80602f/public_url

---

## Skills Section

*(Replace progress bars with grouped tag/grid layout. No percentages.)*

**Section title:** Skills & Tools

**Cloud & Infrastructure:**
AWS, Azure, Proxmox, Hyper-V, Veeam, Docker

**Networking:**
Routing & Switching, VLANs, DNS, DHCP, VPN, Cloudflare, Sophos, pfSense, UniFi

**Systems:**
Windows Server, Linux, macOS, Active Directory, Entra ID, Group Policy

**Security:**
Firewalls, Network Segmentation, Wireshark, Fail2ban

**Endpoint & Device Management:**
Jamf Pro, Kandji, Mosyle, MDM

**Tools & Platforms:**
GitHub Actions, CI/CD, FreePBX, Nginx

---

## Resume Section

**Section title:** Resume

### Summary

*(Optional - can add a one-liner summary at the top of the resume section)*
IT engineer with a background in high-pressure operations management, focused on infrastructure that serves people and systems that don't need babysitting.

---

### Education & Training

**Metropolitan State University of Denver**
Aviation Management | 2013 - 2017
Denver, Colorado

*(No degree designation. Let the certifications section carry the credentials story.)*

---

### Professional Experience

**Alerio Technology Group**
IT Engineer | Feb 2024 - Present | Denver, CO

- Serve as sole embedded IT engineer for a private K-8 school, owning end-to-end IT operations across 120 staff including infrastructure, endpoints, security, and end-user support
- Manage and maintain multi-building network infrastructure including Sophos firewall, UniFi switching and wireless, VLAN segmentation, VoIP (FreePBX/Grandstream), and Starlink WAN failover
- Led full email platform migration from Outlook to Google Workspace, coordinating stakeholder communication, staff training, and cutover logistics across the full staff
- Architect and maintain virtualization, backup, and disaster recovery solutions using Hyper-V and Veeam
- Develop infrastructure proposals and multi-year capital planning for network hardware refreshes, balancing operational continuity with budget constraints

---

**Frontier Airlines**
Denver, CO | Oct 2018 - Jan 2024

*Crew Scheduling Manager | Feb 2022 - Jan 2024*
- Led a team of 35-40 employees across multiple levels during a period of rapid post-COVID expansion, helping scale daily flight operations from ~300 to 600+ daily departures while building out the department's operational leadership structure
- Identified, promoted, and directly mentored frontline employees into supervisory roles, owning their development from individual contributor to team lead during a high-pressure period of organizational growth
- Served as the operational last line of defense within the airline's operations center, managing FAR and contractual compliance, crew continuity, and real-time irregular operations response across a complex, high-stakes environment

*Crew Scheduling Supervisor | Mar 2021 - Feb 2022*
- Acted as shift lead for the crew scheduling operation, serving as direct supervisor for frontline schedulers and primary point of contact for real-time operational decisions during assigned shifts
- Responsible for coaching, counseling, and day-to-day development of frontline scheduling staff, including performance conversations and corrective action

*Crew Scheduling Coordinator | May 2019 - Mar 2021*
- Collaborated on the airline's operational bridge alongside representatives from maintenance control, aircraft routing, customer service, and SOC to communicate and coordinate crew scheduling concerns in real time
- Oversaw frontline schedulers through delegation of recrews and time-sensitive tasks, monitored FAR and contractual compliance, and served as trainer and mentor for newly hired staff

*Crew Scheduler | Oct 2018 - May 2019*
- Rotated across multiple scheduling functions for both pilot and flight attendant operations, including current-day crew support, multi-day reserve administration, and trip transactions
- Took initiative to learn beyond the scheduler role by working alongside crew coordinators during live operations, building familiarity with higher-level decision making that supported a quick progression to Crew Coordinator

---

## Projects Section

*(Replaces Portfolio section. Masonry image grid replaced with project cards.)*

**Section title:** Projects

---

**Project 1: Homelab Hawaii**

Tag: Infrastructure

Description:
A personal homelab environment built on dedicated hardware and designed to mirror real infrastructure patterns. Running Proxmox as the hypervisor across multiple nodes, with a structured network featuring VLAN segmentation, dedicated subnets per service tier, Technitium DNS with conditional forwarding, Nginx Proxy Manager for reverse proxy, and an authentication layer via Authentik. Used as a sandbox for testing, learning, and running self-hosted services with production-level discipline around uptime, backup, and security.

Technologies: Proxmox, VLANs, Technitium DNS, Nginx Proxy Manager, Authentik, Docker, Cloudflare, UniFi

GitHub: *(no public repo - describe only)*

---

**Project 2: Cloud Resume Challenge**

Tag: Cloud / CI/CD

Description:
This site. An adaptation of Forrest Brazeal's Cloud Resume Challenge, built with a static frontend hosted on Hostinger, a serverless AWS backend (Lambda + API Gateway + DynamoDB) powering the visitor counter, and GitHub Actions CI/CD pipelines for both frontend and backend. Built with AI assistance, openly documented in the repo's PROCESS.md.

Technologies: AWS Lambda, API Gateway, DynamoDB, GitHub Actions, AWS SAM, Python, Cloudflare

GitHub: https://github.com/Slammywhammy/cloud-resume-frontend *(update with actual repo URL)*

Live: https://resume.sam-gardner.com

---

**Project 3: Applied.**

Tag: Web App

Description:
An invite-only job application tracker built solo. Full-stack web app with a React + TypeScript frontend, Supabase backend, and GitHub Actions CI/CD pipeline deployed to Hostinger. *(Demo version coming soon.)*

Technologies: React, TypeScript, Vite, Tailwind CSS, Supabase, GitHub Actions

GitHub: *(private - demo version coming soon)*

---

## What I Do Section

*(Replaces Services section. Four competency cards.)*

**Section title:** What I Do

**Card 1: Infrastructure & Networking**
Icon: bi-diagram-3
Firewall management, VLAN design, switching, DNS, DHCP, VPN, and WAN failover. Building networks that stay up and segment properly when they don't.

**Card 2: Systems & Endpoints**
Icon: bi-hdd-stack
Windows Server, Hyper-V, Active Directory, Entra ID, and MDM platforms including Jamf, Kandji, and Mosyle. Keeping devices managed and users unblocked.

**Card 3: Cloud & Automation**
Icon: bi-cloud
Azure infrastructure, AWS serverless, backup and DR with Veeam, and CI/CD pipelines with GitHub Actions. Automating the things that shouldn't require a human.

**Card 4: Self-Hosted & Homelab**
Icon: bi-server
Proxmox virtualization, containerization with Docker, self-hosted services, and network segmentation. Running production-like infrastructure at home because the best way to learn is to break things on your own hardware first.

---

## Contact Section

*(PHP form removed entirely. Replaced with three link cards.)*

**Section title:** Get In Touch

**Subtitle:** Open to new opportunities and conversations about infrastructure, systems, or anything IT.

**Card 1:**
Icon: bi-linkedin
Label: LinkedIn
Link: https://www.linkedin.com/in/samwgardner
Button text: Connect

**Card 2:**
Icon: bi-github
Label: GitHub
Link: https://github.com/Slammywhammy
Button text: View Profile

**Card 3:**
Icon: bi-envelope
Label: Email
Link: mailto:[email address - add before publishing]
Button text: Send Email

---

## Visitor Counter

Small badge/pill element, placed in the footer or bottom of hero section.

Display text: `[count] visitors`

Behavior:
- On page load, fetch GET request to AWS API Gateway endpoint
- Display returned count
- API endpoint URL: *(set after AWS deployment, store as a JS variable at top of main.js)*

Example JS (to be placed in main.js or inline script):
```javascript
async function updateVisitorCount() {
  const response = await fetch('YOUR_API_GATEWAY_URL');
  const data = await response.json();
  document.getElementById('visitor-count').innerText = data.count + ' visitors';
}
updateVisitorCount();
```

---

## Footer

**Name:** Sam Gardner

**Tagline:** IT Engineer. Systems Thinker. Problem Slayer.

**Social links:** LinkedIn, GitHub *(same URLs as header)*

**AI transparency note (small text):**
Built with AI assistance. Infrastructure decisions and content by Sam Gardner, code by Claude.

**Template credit (required by BootstrapMade license):**
Design template by BootstrapMade.

---

## PROCESS.md (for GitHub repo)

```markdown
# How This Site Was Built

This project is an adaptation of the Cloud Resume Challenge. I'm not hiding that AI helped build it.

## What I designed and decided
- Overall architecture: Hostinger frontend, AWS serverless backend, Cloudflare DNS
- Section structure and what to include/cut from the base template
- All resume content, bio, project descriptions, and copy
- Infrastructure decisions: SAM over Terraform, API Gateway + Lambda + DynamoDB, FTP deploy to Hostinger
- CI/CD pipeline design and GitHub Actions workflow structure

## What AI wrote
- HTML/CSS modifications to the base template
- AWS Lambda function (Python)
- AWS SAM template (template.yaml)
- GitHub Actions workflow files
- This site, basically

## Why I'm okay with that
I'm not selling myself as a developer. I'm demonstrating that I understand how cloud infrastructure fits together, how CI/CD pipelines work, and how to ship something real end to end. The code is a means to that end. Understanding what it does and why it's structured that way is the actual skill on display.
```
