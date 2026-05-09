# Paperclip v0 Workspace Structure

Status: Active v0 setup
Date: 2026-05-09

## Company

iZZi AI Systems

## Control Plane

Paperclip is the current UI/control plane for organizing agents, projects, issues, routines, goals, activity, and system-health work.

## Active Agent

- Atlas: Chief Systems Advisor

Atlas is the only active agent for now. Additional project-lead agents should not be created until Paperclip runtime behavior is more stable and role boundaries are clearer.

## Projects

1. DavidOS / Personal AI Workspace
2. FamilyAI / FamilyOS
3. DavidAIStory
4. AI Workspace Diagnostic Service
5. Onboarding, temporary bootstrap project

## Initial Issues

DavidOS / Personal AI Workspace:
- Review Atlas Activation Memo v0 and decide what becomes policy
- Investigate Paperclip auto-resume loop after completed Atlas run
- Revise tool-selection policy into an adaptive decision framework
- Design reusable Domain Deep Dive skill for strategic decision agents
- Evaluate Agentic OS architecture, memory, and observability patterns

FamilyAI / FamilyOS:
- Run Bark wedge decision council

DavidAIStory:
- Define low-friction daily story capture workflow

AI Workspace Diagnostic Service:
- Validate AI-system diagnostic service wedge

## Current Operating Decision

Use Paperclip as the workspace/control plane, DavidOS as durable operating memory, Atlas as system-layer advisor, and Hermes/Opus as the current Atlas runtime.

Do not create more agents yet. First stabilize Paperclip runtime behavior, review tool-selection policy, and validate project-lead role boundaries through real usage.
