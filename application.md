# <Flow.Study-Code Intelligence of Cadence>

# Grant category

Please select one or more of:

- Developer tools / services

# Description

## Problem statement

- Target audience

Flow cadence developer 

Solidity developer want to transfer app to Flow


- Evidence for the need

Contract big data analysis: 

1 There are only 1000+ contracts in Flow,  Ethereum has 10,000,000.

2 Most transactions is produced by top 10 Contracts. The contracts has only two categories, NFT and token.

Detailed analysis:
https://medium.com/@maris205/where-to-copy-flow-cadence-code-flow-1000-contracts-big-data-analysis-13b0757e353c

3 Actual teaching feedback, especially for beginner：
- steep learning curve
- why not adopt mainstream coding paradigm 
- unclear code logic, hard to understand why
- awkward language syntax 
- have no idea what else to code with besides NTFs 

## Proposed solution

More Contracts is the most urgent need of Flow.
Our solution is flow code intelligence.

We design our solution refer to  MSFT CodeXGLUE System.
The solution contains 3 parts:

1 cadence code search. Include cadence codebase, cadence code Search,Similar code detection. Realized by CodeBERT,FFNN+softmax algorithm.

2 code translation. Include solidity to cadence migrate， cadence doc translation, .Realized by CodeBERT as Encoder, Decoder algorithm.

3 code generate. include code completion，Typical function code generation.Realized by CodeGPT algorithm.


Feasibility Analysis

1 OpenSource Technique. Most deep learning algorithms related to code intelligence are open-sourceFrameworks like CodeXGLUE & Copilot are available. Flow contracts are also open source. 

2 Clear CodingParadigm. Cadence paradigm is strict and clear with less core syntax, which is very suitable for the application of intelligent algorithms such as code semantic comprehension.

3 Clear ApplicationFields. Flow ecosystem mainly focus in NFT field at presentVarious intelligent algorithms tends to have good preformance with a specific field


## Impact
Flow code intelligence could bring:

1 Lower coding threshold.Significantly reduce the threshold to adopt Deploy Flow Apps within a few minutes

2 Enrich Contracts.Enrich Flow contract codes rapidly Migration of application ecosystems such as Solidity

3 Development Ecosystem.Support automatic test deployment, contract reference and docking in the development process.


# Milestones and funding

Overall duration to deliver future milestones: ~6 months. Total FLOW requested: 45,000

| Milestone | Deliverables   | Timeline | Risks                   |FLOW requested |
| --------- | -------------- | -------- | ----------------------- | -------------- |
| 1 - Flow Cadence codebase   | code databases | 2 weeks  | - | 2,000           |
| 2 - Flow Cadence search   | code searching platform| 2 weeks  | - | 3,000           |
| 3 - Flow playground integration   |  playground-based online learning platform integrated | 1 month  | - | 10,000           |
| 4 - Cadence code parser   | Static Cadence code parser/python written | 1 month   | - | 5,000           |
| 5 - Solidity automigrating service   | providing auto migration service for Solidity main functions  | 1 month   | - | 10,000           |
| 6 - Flow Intelligent Programming Platform    | Intelligent Cadence code generation for main functions/python written | 1 month  | - | 7,000           |
| 7 - Intelligent Cadence code completion     | vs code extention | 1 month  | - | 8,000           |


# Team

| Name | Role                | Bio | Contact         |
| ---- | ------------------- | --- | --------------- |
|mariswang | AI Engineer | PhD, 10+ years AI research experience, head of several artificial intelligence systems of Tencent,Sogou,etc| @maris205 |
| HoppingChar | Full-Stack Engineer | 5 years experience in blockchain research, responsible for IPFs Minerva and other blockchain products| @HoppingChar|
| xingqi | Full-Stack Engineer | Leader of several big data projects, several years of NLP research experience, proficient in Code AI algorithms | @harboart |