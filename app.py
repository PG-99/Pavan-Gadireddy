"""
Flask entry point for Pavan Gadireddy's data engineering portfolio.

Renders a single-page portfolio site and serves the resume file for download.
All resume-derived content lives in the PORTFOLIO dict below, so the site can
be updated without touching any HTML.
"""

import os

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

RESUME_DIRECTORY = os.path.join(app.static_folder, "resume")
RESUME_FILENAME = "Pavan_Gadireddy_Resume.docx"

PORTFOLIO = {
    "name": "Pavan Gadireddy",
    "title": "ETL Developer | Master Data Management | Data Quality & Integration Analyst",
    "tagline": (
        "Data Engineer specializing in Ab Initio ETL development, enterprise "
        "data warehousing, and legacy-to-cloud migration for banking and "
        "financial services, with hands-on experience across PySpark, "
        "Databricks, and Azure."
    ),
    "location": "Florida, USA",
    "email": "pavangadireddy1999@gmail.com",
    "linkedin_url": "https://www.linkedin.com/in/pavan-gadireddy/",
    # No GitHub profile URL was listed on the resume — replace this
    # placeholder with the real profile link when available.
    "github_url": "",
    "about": (
        "Ab Initio Data Engineer with hands-on experience designing, "
        "developing, and optimizing enterprise-scale ETL workflows for "
        "high-impact banking and financial services data warehousing "
        "initiatives. Skilled across the full ETL lifecycle — requirements "
        "gathering, technical design, development, testing, deployment, and "
        "production support — with a focus on scalable, restartable batch "
        "processing, legacy-to-PySpark migration, and metadata-driven "
        "architectures. Experienced with cloud and big-data platforms "
        "including Databricks, Azure Data Factory, ADLS Gen2, and Snowflake, "
        "and comfortable working across Agile/Scrum teams to deliver "
        "reliable, well-governed data pipelines."
    ),
    "skills": [
        {
            "category": "ETL & Data Integration",
            "tools": [
                "Ab Initio (GDE, Co>Operating System, EME, Express>It, Conduct>It, Query>IT, Control Center)",
                "Profisee (FastApp Studio)",
                "Databricks",
                "Azure Data Factory",
                "PySpark",
                "Delta Lake",
                "API Integrations",
            ],
        },
        {
            "category": "Programming & Scripting",
            "tools": [
                "Python (Pandas, NumPy)",
                "Unix/Linux Shell Scripting (Bash, KSH)",
                "SQL",
                "R",
                "Java",
                "C",
            ],
        },
        {
            "category": "Databases & Data Warehousing",
            "tools": [
                "Snowflake",
                "Oracle / PL-SQL",
                "MS SQL Server",
                "PostgreSQL",
                "Cassandra",
                "MongoDB",
                "Stored Procedures, CTEs, Complex Joins",
                "Indexing, Partitioning, Query Optimization",
            ],
        },
        {
            "category": "Cloud & Big Data Platforms",
            "tools": [
                "Azure Data Factory",
                "Azure Synapse Analytics",
                "ADLS Gen2",
                "Databricks",
                "AWS (S3, Redshift)",
                "Google Cloud Platform (GCP)",
                "Hadoop (Hive, HDFS)",
            ],
        },
        {
            "category": "Scheduling & Orchestration",
            "tools": [
                "Control-M (time-based, event-based, file-based triggers)",
                "Apache Airflow",
                "Apache Kafka",
            ],
        },
        {
            "category": "DevOps & CI/CD",
            "tools": [
                "Git",
                "Azure DevOps",
                "CI/CD Pipeline Automation",
                "Release & Environment Promotion",
            ],
        },
        {
            "category": "Reporting & Visualization",
            "tools": [
                "Power BI",
                "Tableau",
                "Microsoft Excel",
            ],
        },
        {
            "category": "Master Data Management & Governance",
            "tools": [
                "Profisee MDM, FastApp Studio, FastApp Portal",
                "Match & Merge, Survivorship Rules, Golden Record Management",
                "Metadata Management & Data Lineage",
                "Data Quality Rule Frameworks & Profiling",
                "HIPAA-Compliant Data Handling",
            ],
        },
    ],
    "experience": [
        {
            "company": "Blue Cross Blue Shield Association (BCBSA)",
            "location": "Remote",
            "role": "ETL Developer",
            "dates": "September 2025 - Present",
            "highlights": [
                "Design, develop, and maintain high-performance enterprise ETL pipelines using Ab Initio GDE, Co>Operating System, Conduct>It, Plans, reusable components, and EME for enterprise data warehouse environments.",
                "Optimize complex Ab Initio graphs, PSETs, XFRs, DMLs, and continuous flows with a focus on parallelism, partitioning, restartability, fault tolerance, and performance tuning for high-volume batch processing.",
                "Work extensively with Oracle, PL/SQL, and Snowflake for complex data extraction, transformation, loading, reconciliation, and reporting.",
                "Build Unix/Linux shell scripting and Python-based automation for ETL orchestration, batch execution, monitoring, and SFTP integrations.",
                "Handle L2/L3 production support, incident management, and change management to ensure high system availability and reliability.",
                "Implement metadata management and end-to-end data lineage using Ab Initio Metadata Hub and EME repositories.",
                "Leverage PySpark, Databricks, and Azure Data Factory to support modernized enterprise data integration architectures.",
            ],
            "technologies": [
                "Ab Initio (GDE, Co>Operating System, Conduct>It, Express>It, Query>It)",
                "EME Repository", "Oracle / PL-SQL", "Toad DB", "Control-M",
                "Unix/Linux Shell Scripting", "Hadoop", "ServiceNow", "JIRA",
                "Git", "Databricks", "Python", "PySpark", "Delta Lake",
                "Azure Data Factory", "ADLS Gen2", "Synapse Analytics",
            ],
        },
        {
            "company": "IGATE Solutions LLC",
            "location": "Remote",
            "role": "MDM Developer",
            "dates": "August 2024 - September 2025",
            "highlights": [
                "Designed and implemented scalable enterprise MDM and ETL solutions using Profisee and Ab Initio, aligned with data governance standards and regulatory compliance requirements in banking and financial services.",
                "Defined and deployed Match & Merge strategies, survivorship rules, and golden record creation logic via Profisee FastApp Studio, improving data trust and lineage tracking across Provider and Reference domains.",
                "Built staging layers, base MDM tables, and complex SQL logic using Oracle, Teradata, and Azure SQL for large-scale master data integration.",
                "Developed production-grade ETL pipelines using Ab Initio, Azure Data Factory, and SnapLogic integrating cloud and on-premises sources into Azure SQL DB.",
                "Configured FastApp Portal interfaces for Data Stewards, enabling user-driven validation, issue resolution, and workflow routing.",
                "Implemented monitoring of data quality dimensions (completeness, accuracy, consistency, uniqueness) using Profisee DQ rules and metadata-driven validation frameworks, contributing to a 30% improvement in enterprise data health metrics.",
                "Supported CI/CD pipeline automation via Azure DevOps and Control-M workflows, managing build and release processes.",
            ],
            "technologies": [
                "Profisee MDM", "Ab Initio", "Hadoop", "FastApp Studio",
                "Informatica", "SnapLogic", "Azure Data Factory", "GCP",
                "Azure Synapse Analytics", "PL/SQL", "Python", "Oracle",
                "Azure DevOps", "Git", "JIRA", "API Integrations",
            ],
        },
        {
            "company": "Skill-Lync",
            "location": "",
            "role": "Data Analyst",
            "dates": "January 2020 - July 2022",
            "highlights": [
                "Designed scalable, cloud-native data platforms and ETL pipelines using Azure Data Factory and Azure Synapse Analytics to process student engagement, course enrollment, and learning analytics data.",
                "Developed automated data ingestion and transformation workflows in Azure Synapse, reducing manual effort by 50% and improving SLA compliance for reporting.",
                "Built and maintained data models and data marts using Azure SQL, SQL Server, and Oracle for learning platform, payment, and student performance data.",
                "Implemented workflow orchestration using Apache Airflow combined with Unix/Linux shell scripting for scheduling, retries, and alerting on critical pipelines.",
                "Created interactive Tableau dashboards visualizing student acquisition, course completion, engagement trends, and revenue performance.",
                "Engineered distributed PySpark data processing workflows with Azure Data Lake Storage and Hadoop (Hive) for high-volume clickstream and user interaction data.",
                "Designed and developed AutoDoc, a Python/VBA-based automation tool to generate standardized documentation (SRS, SUD, SAD), reducing manual effort and improving consistency.",
                "Optimized SQL and Oracle database performance through query tuning and indexing, improving report performance by up to 40%.",
            ],
            "technologies": [
                "Ab Initio GDE", "PySpark", "Unix/Linux Shell Scripting",
                "Hadoop (Hive, HDFS)", "AWS (S3, Redshift)",
                "Azure Data Factory", "Azure Synapse Analytics", "ADLS Gen2",
                "Python", "Pandas", "NumPy", "SQL", "Oracle", "SSIS",
                "Tableau", "Apache Airflow", "Git",
            ],
        },
    ],
    "projects": [
        {
            "title": "Enterprise ETL Modernization & Legacy-to-Cloud Migration",
            "source": "Blue Cross Blue Shield Association (BCBSA)",
            "problem": (
                "The enterprise data warehouse relied on high-volume Ab "
                "Initio batch pipelines that needed stronger fault "
                "tolerance, performance, and a path toward cloud-native "
                "processing without disrupting production reporting."
            ),
            "role": "ETL Developer",
            "technologies": [
                "Ab Initio GDE", "Co>Operating System", "EME", "Oracle",
                "PL/SQL", "Snowflake", "Control-M", "Python", "PySpark",
                "Databricks", "Azure Data Factory", "ADLS Gen2",
            ],
            "implementation": (
                "Built and optimized Ab Initio graphs, PSETs, and XFRs with "
                "parallelism and partitioning strategies for restartable "
                "batch processing, added Python/shell automation for "
                "orchestration and monitoring, and introduced PySpark and "
                "Databricks components to support legacy-to-cloud migration "
                "alongside metadata-driven lineage tracking via EME."
            ),
            "outcome": (
                "Improved batch reliability and production support "
                "turnaround, ensuring high system availability while laying "
                "groundwork for cloud-based data processing."
            ),
        },
        {
            "title": "Master Data Management & Golden Record Governance",
            "source": "IGATE Solutions LLC",
            "problem": (
                "Provider and reference data was fragmented across "
                "systems, making it difficult to trust a single golden "
                "record for downstream banking and financial reporting."
            ),
            "role": "MDM Developer",
            "technologies": [
                "Profisee FastApp Studio", "Ab Initio", "Azure Data Factory",
                "SnapLogic", "Oracle", "Teradata", "Azure SQL", "Azure DevOps",
            ],
            "implementation": (
                "Configured Match & Merge strategies, survivorship rules, "
                "and golden record logic in Profisee, built staging layers "
                "and SQL transformation logic for master data integration, "
                "and delivered FastApp Portal workflows for data stewards "
                "to validate and resolve data quality issues."
            ),
            "outcome": (
                "Contributed to a 30% improvement in enterprise data "
                "health metrics through metadata-driven data quality "
                "monitoring and governed stewardship workflows."
            ),
        },
        {
            "title": "Cloud Data Platform & Learning Analytics Pipeline",
            "source": "Skill-Lync",
            "problem": (
                "Business teams needed reliable, near-real-time visibility "
                "into student engagement, course completion, and revenue "
                "metrics drawn from disparate learning and payment systems."
            ),
            "role": "Data Analyst",
            "technologies": [
                "Azure Data Factory", "Azure Synapse Analytics", "PySpark",
                "ADLS Gen2", "Apache Airflow", "Tableau", "SSIS",
            ],
            "implementation": (
                "Built cloud-native ingestion and transformation pipelines "
                "into Azure Synapse, orchestrated scheduling and retries "
                "with Apache Airflow, engineered distributed PySpark "
                "processing for clickstream data, and delivered Tableau "
                "dashboards for business stakeholders."
            ),
            "outcome": (
                "Reduced manual reporting effort by 50%, improved SLA "
                "compliance, and improved dashboard/report performance by "
                "up to 40% through query and indexing optimization."
            ),
        },
    ],
    "education": [
        {
            "school": "University of South Florida",
            "location": "Tampa, Florida",
            "degree": "Master's, Engineering Management",
            "details": (
                "Advanced Database and Management Systems, Data Mining, "
                "Technology and Finance, Principles of Engineering "
                "Management, Optimization Methods with APPS"
            ),
        },
        {
            "school": "SRM Institute of Science and Technology",
            "location": "Chennai, India",
            "degree": "Bachelor's, Automobile Engineering",
            "details": "",
        },
    ],
    "certifications": [
        {
            "name": "Databases and SQL for Data Science with Python",
            "issuer": "IBM",
            "url": "https://coursera.org/share/b130d32a7688b80e8cb816972b7abdc6",
            "status": "Completed",
        },
        {
            "name": "Google Data Analytics",
            "issuer": "Google",
            "url": "https://coursera.org/share/51f1e19d2b7cc1166c9ce23a824ec633",
            "status": "Completed",
        },
        {
            "name": "Microsoft Certified: Azure Databricks Data Engineer Associate",
            "issuer": "Microsoft",
            "url": "",
            "status": "In Progress",
        },
        {
            "name": "Claude code 101",
            "issuer": "Anthropic",
            "url": "https://verify.skilljar.com/c/x3xfnb6mknmz",
            "status": "Completed",
        },
    ],
}


@app.route("/")
def home():
    """Render the single-page portfolio."""
    return render_template("index.html", data=PORTFOLIO)


@app.route("/resume")
def download_resume():
    """Serve the resume file as a downloadable attachment."""
    return send_from_directory(
        RESUME_DIRECTORY, RESUME_FILENAME, as_attachment=True
    )


if __name__ == "__main__":
    # Debug mode and port are controlled via environment variables so the
    # same entry point works for local development and production hosting.
    debug_mode = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=debug_mode)
