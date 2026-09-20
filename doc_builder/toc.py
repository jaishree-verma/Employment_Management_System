# Table of Contents module for Employment Management System Technical Documentation

def get_toc_html():
    return r"""
    <div class="page-break"></div>
    <h1 class="section-title"><span class="section-number">TOC</span> Table of Contents — Complete 75-Section Index</h1>
    
    <p style="font-size: 8.5pt; color: #64748b; margin-bottom: 12px;">This comprehensive technical specification is partitioned into 11 distinct architectural divisions comprising 75 verified technical chapters.</p>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; font-size: 8pt;">
        <!-- Left Column -->
        <div>
            <div style="background: #f1f5f9; padding: 5px 8px; border-radius: 4px; font-weight: 700; color: #0f172a; margin-bottom: 4px; text-transform: uppercase; font-size: 7.5pt; letter-spacing: 0.5px;">
                Division I: Executive Foundations (01–11)
            </div>
            <ul style="list-style: none; padding-left: 4px; margin-bottom: 10px;">
                <li><strong>01.</strong> Cover Page &amp; Metadata Identification</li>
                <li><strong>02.</strong> Document Control &amp; Audit Record</li>
                <li><strong>03.</strong> Executive Summary</li>
                <li><strong>04.</strong> Problem Statement &amp; Spreadsheet Vulnerabilities</li>
                <li><strong>05.</strong> Why Did We Choose This Project?</li>
                <li><strong>06.</strong> Project Objectives (Primary &amp; Secondary)</li>
                <li><strong>07.</strong> Scope Specification (In, Out &amp; Future)</li>
                <li><strong>08.</strong> Target User Personas &amp; Responsibilities</li>
                <li><strong>09.</strong> Functional Requirements (FR-01 to FR-08)</li>
                <li><strong>10.</strong> Non-Functional Requirements (NFRs)</li>
                <li><strong>11.</strong> Existing System vs. Proposed System Analysis</li>
            </ul>

            <div style="background: #f1f5f9; padding: 5px 8px; border-radius: 4px; font-weight: 700; color: #0f172a; margin-bottom: 4px; text-transform: uppercase; font-size: 7.5pt; letter-spacing: 0.5px;">
                Division II: Architecture &amp; Lifecycle (12–15)
            </div>
            <ul style="list-style: none; padding-left: 4px; margin-bottom: 10px;">
                <li><strong>12.</strong> Solution Overview &amp; Data Pipeline</li>
                <li><strong>13.</strong> Detailed System Architecture</li>
                <li><strong>14.</strong> Why Layered Architecture? (Separation of Concerns)</li>
                <li><strong>15.</strong> Complete Request Lifecycle (Sequence Trace)</li>
            </ul>

            <div style="background: #f1f5f9; padding: 5px 8px; border-radius: 4px; font-weight: 700; color: #0f172a; margin-bottom: 4px; text-transform: uppercase; font-size: 7.5pt; letter-spacing: 0.5px;">
                Division III: Technology Stack Rationale (16–27)
            </div>
            <ul style="list-style: none; padding-left: 4px; margin-bottom: 10px;">
                <li><strong>16.</strong> Technology Stack Specification</li>
                <li><strong>17.</strong> Why Java? (Type Safety &amp; Ecosystem)</li>
                <li><strong>18.</strong> Why Java 17 LTS / Java 23 Trade-offs</li>
                <li><strong>19.</strong> Why Spring Boot? (Embedded Tomcat &amp; DI)</li>
                <li><strong>20.</strong> Why Spring Boot 3.3.3? (Jakarta EE 10)</li>
                <li><strong>21.</strong> Why Spring Data JPA? (Boilerplate Elimination)</li>
                <li><strong>22.</strong> Why Hibernate ORM? (Persistence Context)</li>
                <li><strong>23.</strong> Why MySQL 8.0? (ACID Relational Storage)</li>
                <li><strong>24.</strong> Why H2 In-Memory DB? (H2 vs. MySQL)</li>
                <li><strong>25.</strong> Why Dual Database Support? (Profile Routing)</li>
                <li><strong>26.</strong> Why Maven &amp; Maven Wrapper?</li>
                <li><strong>27.</strong> Why Vanilla HTML/CSS/JavaScript?</li>
            </ul>

            <div style="background: #f1f5f9; padding: 5px 8px; border-radius: 4px; font-weight: 700; color: #0f172a; margin-bottom: 4px; text-transform: uppercase; font-size: 7.5pt; letter-spacing: 0.5px;">
                Division IV: Frontend Architecture (28–30)
            </div>
            <ul style="list-style: none; padding-left: 4px; margin-bottom: 10px;">
                <li><strong>28.</strong> Frontend Architecture &amp; Lifecycle</li>
                <li><strong>29.</strong> UI/UX Design System &amp; Ergonomics</li>
                <li><strong>30.</strong> Dark / Light Mode Implementation Mechanics</li>
            </ul>

            <div style="background: #f1f5f9; padding: 5px 8px; border-radius: 4px; font-weight: 700; color: #0f172a; margin-bottom: 4px; text-transform: uppercase; font-size: 7.5pt; letter-spacing: 0.5px;">
                Division V: Domain Model &amp; REST APIs (31–39)
            </div>
            <ul style="list-style: none; padding-left: 4px; margin-bottom: 10px;">
                <li><strong>31.</strong> Employee Data Model Specification</li>
                <li><strong>32.</strong> Database Design &amp; Relational Schema</li>
                <li><strong>33.</strong> JPA / Hibernate Mapping Annotations</li>
                <li><strong>34.</strong> RESTful API Endpoint Catalog</li>
                <li><strong>35.</strong> API Request &amp; Response Examples</li>
                <li><strong>36.</strong> HTTP Status Code Semantics</li>
                <li><strong>37.</strong> Department Filtering Implementation</li>
                <li><strong>38.</strong> Search Functionality Architecture</li>
                <li><strong>39.</strong> Dashboard Analytics &amp; Aggregations</li>
            </ul>
        </div>

        <!-- Right Column -->
        <div>
            <div style="background: #f1f5f9; padding: 5px 8px; border-radius: 4px; font-weight: 700; color: #0f172a; margin-bottom: 4px; text-transform: uppercase; font-size: 7.5pt; letter-spacing: 0.5px;">
                Division VI: Testing &amp; Security (40–45)
            </div>
            <ul style="list-style: none; padding-left: 4px; margin-bottom: 10px;">
                <li><strong>40.</strong> Testing Architecture &amp; MockMvc Harness</li>
                <li><strong>41.</strong> Automated Test Case Catalog (TC-01 to TC-06)</li>
                <li><strong>42.</strong> Why MockMvc? (Speed &amp; Servlet Emulation)</li>
                <li><strong>43.</strong> Postman Collection Integration Guide</li>
                <li><strong>44.</strong> Error Handling &amp; Exception Propagation</li>
                <li><strong>45.</strong> Security Analysis (Current vs. Production)</li>
            </ul>

            <div style="background: #f1f5f9; padding: 5px 8px; border-radius: 4px; font-weight: 700; color: #0f172a; margin-bottom: 4px; text-transform: uppercase; font-size: 7.5pt; letter-spacing: 0.5px;">
                Division VII: Containerization &amp; DevOps (46–52)
            </div>
            <ul style="list-style: none; padding-left: 4px; margin-bottom: 10px;">
                <li><strong>46.</strong> Docker Containerization Architecture</li>
                <li><strong>47.</strong> Why Multi-Stage Docker Builds?</li>
                <li><strong>48.</strong> Docker Compose Multi-Container Orchestration</li>
                <li><strong>49.</strong> Cloud Deployment Architecture (Render)</li>
                <li><strong>50.</strong> Why Render Platform? (Cloud Trade-offs)</li>
                <li><strong>51.</strong> Local Developer Setup &amp; Execution Guide</li>
                <li><strong>52.</strong> Environment Configuration &amp; Secret Masking</li>
            </ul>

            <div style="background: #f1f5f9; padding: 5px 8px; border-radius: 4px; font-weight: 700; color: #0f172a; margin-bottom: 4px; text-transform: uppercase; font-size: 7.5pt; letter-spacing: 0.5px;">
                Division VIII: Code Quality &amp; Evolution (53–60)
            </div>
            <ul style="list-style: none; padding-left: 4px; margin-bottom: 10px;">
                <li><strong>53.</strong> Project Directory Tree &amp; File Catalog</li>
                <li><strong>54.</strong> Code Quality Audit &amp; Technical Critique</li>
                <li><strong>55.</strong> Design Patterns &amp; Software Principles</li>
                <li><strong>56.</strong> Performance Characteristics &amp; Benchmarks</li>
                <li><strong>57.</strong> Scalability Analysis (100 &rarr; 100,000+ Records)</li>
                <li><strong>58.</strong> System Limitations (Objective Assessment)</li>
                <li><strong>59.</strong> Future Enhancements &amp; Strategic Roadmap</li>
                <li><strong>60.</strong> Scope Scoping &amp; Complexity Trade-Offs</li>
            </ul>

            <div style="background: #f1f5f9; padding: 5px 8px; border-radius: 4px; font-weight: 700; color: #0f172a; margin-bottom: 4px; text-transform: uppercase; font-size: 7.5pt; letter-spacing: 0.5px;">
                Division IX: Flows &amp; Traceability (61–70)
            </div>
            <ul style="list-style: none; padding-left: 4px; margin-bottom: 10px;">
                <li><strong>61.</strong> End-to-End Use Case 1: Add Employee</li>
                <li><strong>62.</strong> End-to-End Use Case 2: Filter by Department</li>
                <li><strong>63.</strong> End-to-End Use Case 3: Update Employee</li>
                <li><strong>64.</strong> Master System Data Flow Architecture</li>
                <li><strong>65.</strong> Complete Technology Decision Matrix</li>
                <li><strong>66.</strong> "Why This and Not That" Comparative Evaluations</li>
                <li><strong>67.</strong> Dependency Version Audit &amp; Upgrade Path</li>
                <li><strong>68.</strong> Requirement &rarr; Code &rarr; Test Traceability</li>
                <li><strong>69.</strong> Test &rarr; Feature Traceability &amp; Coverage</li>
                <li><strong>70.</strong> Deployment &rarr; Source Traceability</li>
            </ul>

            <div style="background: #f1f5f9; padding: 5px 8px; border-radius: 4px; font-weight: 700; color: #0f172a; margin-bottom: 4px; text-transform: uppercase; font-size: 7.5pt; letter-spacing: 0.5px;">
                Division X &amp; XI: Defense &amp; Appendix (71–75)
            </div>
            <ul style="list-style: none; padding-left: 4px; margin-bottom: 10px;">
                <li><strong>71.</strong> Project Maturity Classification</li>
                <li><strong>72.</strong> Technical Interview Questions &amp; Answers</li>
                <li><strong>73.</strong> Project Defense / Viva Questions &amp; Defense</li>
                <li><strong>74.</strong> Final Technical Summary</li>
                <li><strong>75.</strong> Appendix &amp; Technical Reference Catalog</li>
            </ul>
        </div>
    </div>
    """
