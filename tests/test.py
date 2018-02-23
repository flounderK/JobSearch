import unittest
from context import patternScore

search_regex = """[Pp]ython
(?<![A-Za-z])[Ss]cript(s|ing)*
[Ll][Ii][Nn][Uu][Xx]
([Jj][Aa][Vv][Aa](?![Ss]))
(([Dd]ata|[Ii]nformation|[Cc]yber|[Nn]etwork)(.))*[Ss]ecurity
(([Ss][Qq][Ll])|([Ss]tructured.[Qq]uery.[Ll]anguage))
[Dd]ev(elopment)*.{0,1}[Oo]p(s|erations)
([Bb][Aa][Ss][Hh]|(([Pp]ower)*[Ss]hell))
[Ss]elenium
(?<!([A-Za-z]))[Oo]([Oo][Pp]|bject.[Oo]riented.([Pp]rogramming|[Dd]esign))
(?<![A-Za-z])[Gg]it
(?<![A-Za-z])[Nn][Mm][Aa][Pp]
[Ww]eb.{0,1}[Ss]crap(e|ing)
[Nn]etwork(s|ing)*(.{0,1}([Aa]dministrat(ion|or)|[Ee]ngineer))
[Tt][Cc][Pp].[Ii][Pp]|[Dd][Nn][Ss]""".split()

scores = """4
3
4
2
5
2
3
3
1
3
1
4
2
4
3""".split()
leg = patternScore.Score_Legend()
for i in search_regex:
    leg.add(patternScore.Scored_Pattern(
                        score=scores[search_regex.index(i)],pattern=i))

posting_text="""Participate as a member of the 24x7x365 Threat Intelligence Center (TIC) responsible for identifying malicious threat actors, thwarting hackers, preventing data breaches, acting as a security advocate for clients, performing security threat analysis, and working with clients to provide remediation strategies and guidance. Perform daily incident detection and response operations. Collect host–based artifacts and perform forensic analysis to determine if the asset has been compromised. Identify compromised computers using logs, live response, and related computer–centric evidence sources. Provide peer review of both signatures for development and resulting threat detections. Provide input on new detection strategies and remediation guidance to clients. Form accurate and precise real–time host–centric analysis, including live response and digital forensics, malware analysis, and log–centric (SIEM) analysis, as needed. Analyze and assess security incidents and escalate to client resources, appropriate teammates, or internal teams for additional assistance. Present analysis to other analysts for review, fine tuning, and feedback, work with the threat intelligence team to fine tune signatures, validate and characterize threats, collaborate with others when needed, and assist the incident response team with the incident response process."""
posting_text2="""Basic Qualifications:

-Ability to document findings to report and escalate Cyber incidents to customers and management clearly and concisely

-Ability to work well both independently and in a team environment

-Ability to take ownership of analytic work and provide constructive feedback to others.

-Scheduled to obtain a BA or BS degree in Winter 2018 or Spring 2019


Additional Qualifications

-Experience with nNetwork–centric analysis (NSM)

-Experience with deploying and scripting detection solutions in Bro–IDS

-Experience with hos–based detection and prevention suites, including McAfee EPI, OSSEC, Yara, MIR, CarbonBlack, or Tanium

-Experience with IT infrastructure, including system and application vulnerabilities and exploitation and operating systems, including Windows, *Nix, and Mac

-Knowledge of Spunk and other SIEM technologies

-Knowledge of scripting and programming in Python, Perl, or C

-Knowledge of APT, Cyber Crime, and other associated tactics

-Possession of critical thinking, problem–solving, and analytical skills

-Possession of excellent oral and written communication skills

-BA or BS degree in Cybersecurity, CS, or IT preferred

Integrating a full range of consulting capabilities, Booz Allen is the one firm that helps clients solve their toughest problems by their side to help them achieve their missions.  Booz Allen is committed to delivering results that endure.

We are proud of our diverse environment, EOE, M/F/Disability/Vet."""
posting_text = posting_text + posting_text2
job_posting=patternScore.Document(legend=leg,text=posting_text)
#job_posting2=Document(legend=leg,text=posting_text2)
print("Posting rating: {:f}".format(job_posting.score_total))