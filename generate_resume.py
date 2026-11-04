import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


OUTPUT = sys.argv[1] if len(sys.argv) > 1 else "resume.pdf"
NAVY = colors.HexColor("#123B4A")
TEAL = colors.HexColor("#0E7490")
TEXT = colors.HexColor("#17202A")
MUTED = colors.HexColor("#455A64")
LINE = colors.HexColor("#8CA5AE")
PALE = colors.HexColor("#F2F7F8")

styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="ResumeName",
        parent=styles["Heading1"],
        alignment=TA_CENTER,
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=22,
        textColor=NAVY,
        spaceAfter=2,
    )
)
styles.add(
    ParagraphStyle(
        name="Headline",
        alignment=TA_CENTER,
        fontName="Helvetica-Bold",
        fontSize=9.4,
        leading=12,
        textColor=TEAL,
        spaceAfter=3,
    )
)
styles.add(
    ParagraphStyle(
        name="Contact",
        alignment=TA_CENTER,
        fontName="Helvetica",
        fontSize=7.7,
        leading=10,
        textColor=TEXT,
        spaceAfter=6,
    )
)
styles.add(
    ParagraphStyle(
        name="Section",
        fontName="Helvetica-Bold",
        fontSize=9.7,
        leading=12,
        textColor=NAVY,
        spaceBefore=5,
        spaceAfter=4,
        borderWidth=0,
        borderPadding=0,
    )
)
styles.add(
    ParagraphStyle(
        name="BodySmall",
        fontName="Helvetica",
        fontSize=8.25,
        leading=10.5,
        textColor=TEXT,
        spaceAfter=1.5,
    )
)
styles.add(
    ParagraphStyle(
        name="Skill",
        parent=styles["BodySmall"],
        fontSize=7.8,
        leading=9.5,
        spaceAfter=1.5,
    )
)
styles.add(
    ParagraphStyle(
        name="JobTitle",
        fontName="Helvetica-Bold",
        fontSize=8.9,
        leading=11,
        textColor=NAVY,
    )
)
styles.add(
    ParagraphStyle(
        name="JobDate",
        fontName="Helvetica-Bold",
        fontSize=7.8,
        leading=10,
        alignment=2,
        textColor=MUTED,
    )
)
styles.add(
    ParagraphStyle(
        name="ResumeBullet",
        parent=styles["BodySmall"],
        leftIndent=11,
        firstLineIndent=-7,
        bulletIndent=2,
        spaceAfter=1.3,
    )
)
styles.add(
    ParagraphStyle(
        name="ProjectTitle",
        fontName="Helvetica-Bold",
        fontSize=9,
        leading=11,
        textColor=NAVY,
        spaceAfter=1,
    )
)
styles.add(
    ParagraphStyle(
        name="ProjectMeta",
        fontName="Helvetica-Bold",
        fontSize=7.5,
        leading=9,
        textColor=MUTED,
        spaceAfter=2,
    )
)


def rule():
    table = Table([[""]], colWidths=[184 * mm], rowHeights=[0.35 * mm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), LINE),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    return table


def section(title):
    return [Paragraph(title.upper(), styles["Section"]), rule(), Spacer(1, 2.5)]


def job_header(title, date):
    table = Table(
        [[Paragraph(title, styles["JobTitle"]), Paragraph(date, styles["JobDate"])]],
        colWidths=[140 * mm, 44 * mm],
    )
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
            ]
        )
    )
    return table


def bullet(text):
    return Paragraph(f"&#8226;&nbsp; {text}", styles["ResumeBullet"])


def page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(MUTED)
    canvas.drawCentredString(A4[0] / 2, 6 * mm, f"{doc.page}")
    canvas.restoreState()


doc = BaseDocTemplate(
    OUTPUT,
    pagesize=A4,
    leftMargin=13 * mm,
    rightMargin=13 * mm,
    topMargin=10 * mm,
    bottomMargin=11 * mm,
    title="Bandi Raveendra Reddy - DevOps Engineer",
    author="Bandi Raveendra Reddy",
)
frame = Frame(
    doc.leftMargin,
    doc.bottomMargin,
    doc.width,
    doc.height,
    leftPadding=0,
    rightPadding=0,
    topPadding=0,
    bottomPadding=0,
)
doc.addPageTemplates(PageTemplate(id="Resume", frames=[frame], onPage=page_number))

story = [
    Paragraph("BANDI RAVEENDRA REDDY", styles["ResumeName"]),
    Paragraph(
        "DevOps Engineer | Cloud Infrastructure | CI/CD | Kubernetes | IaC | AI Agents",
        styles["Headline"],
    ),
    Paragraph(
        '<link href="tel:+918618880260">+91 8618880260</link> &nbsp;|&nbsp; '
        '<link href="mailto:bandiraveendradevops@gmail.com">bandiraveendradevops@gmail.com</link> &nbsp;|&nbsp; '
        '<link href="https://linkedin.com/in/bandiraveendra-reddy">linkedin.com/in/bandiraveendra-reddy</link> &nbsp;|&nbsp; '
        "Bengaluru, Karnataka, India",
        styles["Contact"],
    ),
]

story += section("Professional Summary")
story.append(
    Paragraph(
        "Results-driven DevOps Engineer with 4+ years of experience architecting and automating CI/CD pipelines, "
        "cloud-native infrastructure, and container orchestration at scale. Deep expertise across AWS (25+ services), "
        "Kubernetes (EKS), Helm, Docker, Terraform, and Jenkins. Proven record in high-stakes production environments, "
        "achieving 99.9% uptime, reducing deployment time by 60%, and cutting security incidents by 70%. Experienced "
        "in Kong API Gateway, Cloudflare security, full-stack observability, and AI-agent-assisted DevOps "
        "troubleshooting and incident triage.",
        styles["BodySmall"],
    )
)

story += section("Technical Skills")
skills = [
    ("Cloud Platforms", "AWS (EC2, EKS, ECS, Lambda, S3, RDS, Aurora, DocumentDB, SQS, SNS, VPC, IAM, ECR, Route 53, CloudWatch, Secrets Manager, KMS) | Azure (VMs, AKS, Storage, Virtual Networks)"),
    ("CI/CD &amp; Automation", "Jenkins, Jenkins Shared Libraries (Groovy), GitHub Actions, GitLab CI, Azure DevOps, ArgoCD"),
    ("Containers &amp; Orchestration", "Docker, Kubernetes (EKS/AKS), Helm, HPA, Auto-Healing, Pod Debugging, Amazon ECS"),
    ("IaC &amp; Configuration", "Terraform, Ansible, AWS CloudFormation, ARM Templates"),
    ("Networking &amp; Security", "Kong API Gateway, Cloudflare, VPC, VPN, ALB/NLB, Route 53, IAM, Secrets Manager, KMS, SonarQube, Trivy, OWASP"),
    ("Observability", "Prometheus, Grafana, CloudWatch, ELK/EFK, Coralogix, New Relic APM, Splunk, Datadog"),
    ("AI Agents", "AI-assisted DevOps troubleshooting, incident triage, log and metric analysis, root-cause investigation, and remediation guidance"),
    ("Scripting &amp; SCM", "Python, Bash, Groovy, YAML, JSON | Git, GitHub, GitLab, Bitbucket, Nexus"),
]
for label, value in skills:
    story.append(Paragraph(f"<b>{label}:</b> {value}", styles["Skill"]))

story += section("Professional Experience")
story.append(job_header("DevOps Engineer | Acko - Bengaluru, India", "Jan 2025 - Present"))
for item in [
    "Architected production-grade CI/CD pipelines using Jenkins and GitHub Actions, cutting deployment time by 60% and enabling 50+ daily zero-downtime releases.",
    "Designed Helm charts for EKS microservice deployments with parameterized <i>values.yaml</i> across Dev/UAT/Prod, eliminating configuration drift and automating rollbacks.",
    "Configured Kong API Gateway for authentication, logging, and request transformation, and Cloudflare for DNS, DDoS protection, and SSL/TLS termination.",
    "Managed multi-region AWS infrastructure via Terraform, including EC2 Auto Scaling, RDS/Aurora, DocumentDB, EKS, Lambda, SQS/SNS, ECR, and VPC networking.",
    "Implemented Route 53 failover and latency routing with ALB/NLB load balancing across 100+ microservices, sustaining a 99.9% uptime SLA.",
    "Built an observability stack with Prometheus, Grafana, Coralogix, and CloudWatch, reducing MTTR by 45% through proactive alerting and SLA dashboards.",
    "Enforced Trivy and SonarQube scanning, IAM least privilege, Secrets Manager rotation, and KMS encryption, reducing security incidents by 70%.",
    "Automated end-to-end service onboarding from Terraform provisioning to Kubernetes deployment, eliminating manual steps and accelerating delivery.",
]:
    story.append(bullet(item))

story.append(PageBreak())
story += section("Professional Experience - Continued")
story.append(job_header("DevOps Engineer | Cognizant - Bengaluru, India", "May 2022 - Dec 2024"))
for item in [
    "Built CI/CD pipelines for 25+ enterprise applications using Jenkins, GitHub Actions, and Azure DevOps, automating build, test, and multi-environment deployments.",
    "Containerized legacy applications with Docker and migrated them to Kubernetes, improving resource utilization by 40% and enabling horizontal scaling.",
    "Provisioned AWS and Azure infrastructure with Terraform, maintaining consistent staging and production environments across multiple regions.",
    "Deployed centralized ELK logging and Grafana dashboards for real-time application performance and system health visibility.",
    "Integrated Allure/Selenium testing and SonarQube scanning into delivery pipelines, improving code quality by 35%.",
    "Developed Python and Bash automation for incident response, backup management, and optimization, saving 20+ hours weekly.",
    "Mentored junior engineers on DevOps practices and authored runbooks for disaster recovery and incident response.",
]:
    story.append(bullet(item))

story += section("AI Agents Project")
project_content = [
    Paragraph("AI-Assisted DevOps Troubleshooting &amp; Incident Triage Agent", styles["ProjectTitle"]),
    Paragraph("AI Agents | Observability | Kubernetes | Cloud Operations | Incident Response", styles["ProjectMeta"]),
]
for item in [
    "Developed an AI-agent workflow to support DevOps troubleshooting by analyzing logs, metrics, alerts, and deployment context during incidents.",
    "Used the agent to summarize symptoms, correlate operational signals, propose likely root causes, and recommend structured remediation and verification steps.",
    "Applied the workflow to Kubernetes pod failures, CI/CD pipeline errors, infrastructure issues, and production alert triage while retaining engineer approval for operational actions.",
    "Standardized troubleshooting output into incident summaries and reusable runbook guidance to improve consistency and knowledge sharing.",
]:
    project_content.append(bullet(item))
project_table = Table([[project_content]], colWidths=[184 * mm])
project_table.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, -1), PALE),
            ("BOX", (0, 0), (-1, -1), 0.5, LINE),
            ("LINEBEFORE", (0, 0), (0, -1), 3, TEAL),
            ("LEFTPADDING", (0, 0), (-1, -1), 8),
            ("RIGHTPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ]
    )
)
story.append(project_table)

story += section("Key Achievements")
for item in [
    "Reduced infrastructure costs by 30% through resource rightsizing, optimization, and automated shutdown policies.",
    "Achieved 99.9% availability through automated failover, health checks, and multi-region monitoring.",
    "Led the migration of 20+ applications from on-premise infrastructure to AWS and Azure ahead of schedule.",
    "Executed a Bitbucket-to-GitHub repository migration with zero disruption to live delivery pipelines.",
]:
    story.append(bullet(item))

story += section("Education")
story.append(
    job_header(
        "Bachelor of Engineering | Saveetha School of Engineering, Chennai",
        "May 2019 - Apr 2022",
    )
)

doc.build(story)
print(f"Generated {OUTPUT}")
