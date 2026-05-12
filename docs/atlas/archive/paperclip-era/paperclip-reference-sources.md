# Paperclip Reference Sources

Status: Active reference note
Date: 2026-05-09

## Purpose

Track where DavidOS and Atlas should look for Paperclip setup, architecture, runtime, and governance documentation before making Paperclip configuration recommendations.

## Local Reference Mirror

Local Paperclip repo mirror:

/home/hermes/reference/paperclip

Primary documentation folders:

- /home/hermes/reference/paperclip/docs
- /home/hermes/reference/paperclip/doc

## Usage Rule

Before recommending non-trivial Paperclip setup changes, Atlas should review the relevant local Paperclip docs and, when needed, inspect current Paperclip runtime behavior.

Atlas should distinguish between:

1. Paperclip documented capabilities.
2. Observed local runtime behavior.
3. DavidOS/iZZi AI Systems policy decisions.
4. Experimental setup assumptions.

## Current Known Gap

Paperclip successfully produced the Atlas activation memo, but the DAV-1 run showed auto-resume/recovery-loop behavior. Treat Paperclip as promising but not yet fully trusted for production-grade autonomous work until this runtime behavior is understood.

## License Note

Paperclip documentation should be used as an internal setup/reference source. Do not republish or commercialize copied documentation content without checking the applicable license and permissions.
