# LangSmith Crash Course 🚀

This repository contains my learning and implementation from the **LangSmith Crash Course by Nitish Singh Sir (CampusX)**.

I completed the course to understand how **LangSmith can be used for observability, tracing, debugging, testing, and monitoring of LLM applications**.

---

## 📌 What I Learnt

### 1. What is LangSmith?

I learnt that **LangSmith is an observability and evaluation platform for LLM applications**.

It helps me see what is happening inside an application instead of looking only at the final answer.

```text
User Query
     ↓
LLM Application
     ↓
LangSmith Trace
     ↓
Inputs + Outputs + Intermediate Steps
```

---

### 2. Observability in LLM Applications

I learnt why observability is important in Generative AI applications.

A normal application may look like:

```text
User → Application → Answer
```

But internally, many things can happen:

```text
User Query
     ↓
Prompt
     ↓
Retriever
     ↓
Documents
     ↓
LLM
     ↓
Output Parser
     ↓
Final Answer
```

If the final answer is wrong, it is difficult to know which step caused the problem.

**LangSmith makes these internal steps visible.**

---

### 3. Tracing

I learnt the concept of a **Trace**.

A trace represents the execution of an application for a particular request.

For example:

```text
Trace
│
├── Prompt
│
├── LLM
│
├── Retriever
│
└── Output Parser
```

By inspecting a trace, I can understand:

- What input was received
- What prompt was generated
- What the LLM received
- What the LLM returned
- Which documents were retrieved
- How long each step took
- Where an error occurred

---

### 4. Runs

I learnt that individual operations inside an application can be represented as **runs**.

For example:

```text
Trace
  │
  ├── Prompt Run
  │
  ├── LLM Run
  │
  └── Parser Run
```

So, a useful way to understand it is:

```text
Trace = Complete execution
Run   = Individual operation inside that execution
```

---

### 5. Tracing a Simple LLM Application

I learnt how a simple LLM call can be observed using LangSmith.

```text
Input
  ↓
Prompt
  ↓
LLM
  ↓
Output
```

Instead of treating the LLM as a black box, LangSmith allows me to inspect the execution.

---

### 6. Sequential Chains

I learnt how tracing becomes more useful when an application contains multiple steps.

```text
Input
  ↓
Chain 1
  ↓
Chain 2
  ↓
Chain 3
  ↓
Final Output
```

LangSmith helps me inspect each individual step of the chain.

---

### 7. RAG Tracing

I learnt how LangSmith can be used with **Retrieval-Augmented Generation (RAG)** applications.

A RAG pipeline can be represented as:

```text
User Question
      ↓
Retriever
      ↓
Relevant Documents
      ↓
Prompt
      ↓
LLM
      ↓
Answer
```

The important thing I learnt is that when a RAG application gives a wrong answer, I should not immediately blame the LLM.

The problem could be:

```text
Wrong Answer
    │
    ├── Wrong documents retrieved
    ├── Relevant document not retrieved
    ├── Poor prompt
    ├── LLM generated an incorrect response
    └── Output processing problem
```

LangSmith helps identify **where the problem actually occurred**.

---

### 8. Query Testing

I learnt how queries can be tested and inspected to understand the behaviour of an LLM application.

This is useful for finding cases where:

- The application gives incorrect answers
- Retrieval is poor
- The prompt needs improvement
- The model produces unexpected output

---

### 9. Debugging with LangSmith

I learnt a practical debugging workflow:

```text
Run Application
      ↓
Open Trace
      ↓
Inspect Input
      ↓
Inspect Retrieval
      ↓
Inspect Prompt
      ↓
Inspect LLM Output
      ↓
Inspect Final Answer
      ↓
Find the Problem
      ↓
Improve the Application
```

This is one of the most useful concepts I learnt from the course.

---

### 10. Agents

I learnt why tracing becomes even more important when working with **Agents**.

An agent can decide what action or tool to use:

```text
User
 ↓
Agent
 ↓
LLM decides action
 ↓
Tool
 ↓
Tool Result
 ↓
Agent
 ↓
Final Answer
```

LangSmith allows these intermediate steps to be inspected.

---

### 11. LangGraph + LangSmith

I learnt how LangSmith can be used with **LangGraph applications**.

The basic difference I understood is:

```text
LangGraph
    ↓
Builds and manages the workflow

LangSmith
    ↓
Observes and evaluates the workflow
```

Together:

```text
                LangGraph
             ┌──────────────┐
             │ Nodes        │
             │ State        │
             │ Edges        │
             │ Workflow     │
             └──────┬───────┘
                    ↓
                LangSmith
             ┌──────────────┐
             │ Tracing      │
             │ Debugging    │
             │ Evaluation   │
             │ Monitoring   │
             └──────────────┘
```

---

## 🧠 Important Concepts I Understood

| Concept | What I learnt |
|---|---|
| **LangSmith** | Platform for observing and evaluating LLM applications |
| **Observability** | Ability to understand what is happening inside an application |
| **Trace** | Complete execution of an application request |
| **Run** | Individual operation inside a trace |
| **Tracing** | Recording application execution for inspection |
| **RAG Tracing** | Inspecting retrieval, prompt, LLM and final output |
| **Agent Tracing** | Inspecting agent decisions and tool calls |
| **LangGraph** | Framework for building stateful LLM workflows |
| **LangSmith + LangGraph** | Workflow execution can be observed and debugged |

---

## 🔄 Overall Learning

The overall concept I learnt from the course is:

```text
              LLM Application
                     │
        ┌────────────┼────────────┐
        ↓            ↓            ↓
      Chain         RAG         Agent
        │            │            │
        └────────────┼────────────┘
                     ↓
                 LangGraph
                     ↓
                 LangSmith
                     ↓
          ┌──────────┼──────────┐
          ↓          ↓          ↓
       Tracing   Debugging   Evaluation
```

---

## 🛠️ Technologies

- Python
- LangChain
- LangGraph
- LangSmith
- LLMs
- RAG
- Agents
- Prompt Engineering

---

## 📂 Course Topics Completed

- [x] Introduction to LangSmith
- [x] Understanding Observability
- [x] Understanding Traces
- [x] Understanding Runs
- [x] Simple LLM Call Tracing
- [x] Sequential Chain Tracing
- [x] RAG Tracing
- [x] Query Testing
- [x] Debugging LLM Applications
- [x] Agent Tracing
- [x] LangGraph + LangSmith

---

## 🎯 Final Takeaway

The biggest thing I learnt is:

> **Building an LLM application is not enough. I also need to understand what is happening inside the application.**

LangSmith helps me move from:

```text
"Why did my application give this answer?"
```

to:

```text
"Which step caused this answer?"
```

This makes **debugging, improving, evaluating, and monitoring LLM applications much easier.**

---

## ✅ Status

**Completed 🎉**

I have completed this LangSmith crash course and documented the key concepts and practical learnings here for future reference.
