<!--
Copyright (c) 2022 Dell Inc., or its subsidiaries. All Rights Reserved.

Licensed under the GPL, Version 3.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.gnu.org/licenses/gpl-3.0.txt
-->

# Triage issues

The main goals of an issue triage are to categorize open issues based on priority and to ensure that these issues contain adequate information for contributors to work on them.

> **Note:** This information is for project Maintainers, Owners, and Admins. If you are a Contributor, then you will not be able to perform most of the tasks in this topic.

The core maintainers of this project are responsible for categorizing all incoming issues and delegating any critical or important issue to other maintainers. Triage provides an important way to contribute to an open source project.

A triage helps resolve issues quickly by :

- Ensuring the intent of an issue is clear. The issue should clearly describe the problem the end user is experiencing as well as the steps to reproduce the problem.
- Giving a contributor the information they need before they commit to resolving an issue.
- Streamlining the development process by identifying and closing duplicate issues.

If you don't have the knowledge or time to code, consider helping with triage. The community will thank you for saving them time by spending some of yours.

## 1. Find issues that need triage

The easiest way to find issues that haven't been triaged is to search for issues with the `needs-triage` label.

## 2. Ensure the issue contains basic information

When creating a new issue, the author must provide all of the information required by the project's GitHub issue template

### Standard issue information that must be included

The following section describes the various issue templates and the expected content.

#### Bug reports

A bug report should contain explanation of what the problem is, what the expected outcome is, and how to reproduce the problem. Additionally, any other supporting information such as screenshots, console logs, and environment details should be included in the bug report. 

 - Product Name/Version
 - Component/Module Name
 - Ansible Collection Version	
 - Configuration
 - Steps to Reproduce
 - Expected/Actual Behavior
 - Logs/Screenshots
 - Any other additional information...

#### Feature requests

Should explain what feature that the author wants to be added and why that is needed.

#### Ask a Question requests

In general, if the issue description and title are perceived as questions no more information is needed.

### Good practices

To make issue handling easier for everyone, it is suggested to:

- Make sure that issue titles are named to explain the subject of the issue, have correct spelling, and don't include irrelevant information and/or sensitive information.
- Make sure that issue descriptions don't include irrelevant information.
- Make sure that issues do not contain sensitive information.
- Make sure that issues have all relevant fields filled in.
- If an issue is unclear, then try to edit the title and description for more clarity or leave a comment requesting that edits to the issue be made.

### Dealing with missing information

Depending on the issue, you might not feel all this information is needed. Use your best judgement. If you cannot triage an issue using what its author provided, explain kindly to the author that they must provide the above information to clarify the problem. Label issue with `triage/needs-information`.

If the author provides the standard information but you are still unable to triage the issue, then request additional information. Do this kindly and politely because you are asking for more of the author's time. Label issue with `triage/needs-information`. 

If the author does not respond to the requested information within the timespan of a week, close the issue with a kind note stating that the author can request for the issue to be reopened when the necessary information is provided.

If you receive a notification that additional information was provided but you are no longer working on issue triage, then you should delegate the issue to the current person working on issue triage.

## 3. Categorizing an issue

### Duplicate issues

Make sure it's not a duplicate by searching existing issues using related terms from the issue title and description. If you think the issue may be a potential duplicate and can't find the original existing issue, then please reach out to one of the maintainers and ask for help. If you identify that the issue is a duplicate of an existing issue:

1. Add a comment `duplicate of #<issue number>`
2. Add the `triage/duplicate` label

### Bug reports

If it's not perfectly clear that it's an actual bug, quickly try to reproduce it.

**It's a bug/it can be reproduced:**

1. Add a comment describing detailed steps for how to reproduce it, if applicable.
2. If maintainers aren't able to address the issue in a timely manner, then label the issue with `help wanted` and an optional `beginner friendly`. Also, include pointers to the problematic source code. Doing this allows us to solicit help from the community to get the issue resolved.
3. Move on to [prioritizing the issue](#4-prioritization-of-issues).

**It can't be reproduced:**

1. Either request that [more information](#2-ensure-the-issue-contains-basic-information) is needed to investigate the issue more thoroughly. Provide details in a comment. <br>
or <br>
2. [delegate further investigations](#investigation-of-issues) to someone else.  Provide details in a comment.

**It works as intended/by design:**

1. Kindly and politely add a comment explaining briefly why we think it works as intended and close the issue.
2. Label the issue `triage/works-as-intended`.
3. Remove the `needs-triage` label.

### Feature requests

1. If the feature request does not align with the product vision, add a comment indicating so, remove the `needs-triage` label and close the issue
2. Otherwise, move on to [prioritizing the issue](#4-prioritization-of-issues).  Assign the appropriate priority label to the issue, add the appropriate comments to the issue, and remove the `needs-triage` label.

## 4. Prioritization of issues
In general, bugs and feature request issues should be labeled with a priority.

This can be the most difficult task when triaging issues since it requires a lot of knowledge, context, and experience before being able to start feeling comfortable adding a certain priority label.

In order to gain comfort with prioritizing issues, consulting with experienced project members on issues is highly encouraged.

In case there is an uncertainty around the prioritization of an issue, please ask the maintainers for help.

| Label                             | Description                                                                                                              |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `priority/critical`               | Highest priority. Must be actively worked on as someone's immediate top priority.                                        |
| `priority/high`                   | Must be worked on soon, ideally in time for the next release.                                                            |
| `priority/low`                    | Lowest priority. Possibly useful, but not critical to functionality.                                                     |

### Critical priority

1. If an issue has been categorized and any of the following criteria apply to it, then the issue should be labeled as critical and must be actively worked on as someone's immediate top priority.

   - Results in any data loss
   - Critical security or performance issues
   - Problem that makes a feature unusable
   - Multiple users experience a severe problem affecting their business, users, etc.

2. Label the issue `priority/critical`.
3. Escalate the problem to the maintainers.
4. Assign the issue or ask a maintainer for help assigning the issue to someone as their immediate top priority.
5. Add the issue to the next upcoming release milestone.

### High priority

1. Label the issue `priority/high`.
2. Add the issue to the next upcoming release milestone.
3. Prioritize it or assign someone to work on it now or very soon.
4. Consider requesting [help from the community](#5-requesting-help-from-the-community).

### Low priority

1. If the issue is deemed possibly useful but is a low priority, then label the issue `priority/low`.
2. The functional impact of an issue determines how high of a priority the issue is.
3. Consider requesting [help from the community](#5-requesting-help-from-the-community).

## 5. Requesting help from the community

Due to constraints, maintainers aren't always able to resolve issues in a timely manner, especially those of lower priority. For such issues, consider requesting help from the community. Use your best judgement. In general, requesting help from the community means that a contribution has a good chance of getting accepted and merged.

In many cases, the issue author or the community is most suitable to contribute changes since they're experts in their domain. Also, it's very common for someone to seek help from the community on a problem.

1. Kindly and politely add a comment which will notify the users subscribed to the issue of any updates.
   - Explain that the issue would be nice to get resolved, but it isn't prioritized to be worked on by maintainers for the foreseeable future.
   - If possible or applicable, try to help contributors get started by adding pointers to relevant source code or files as well as adding any helpful input on how to resolve the issue.
2. Label the issue with `help wanted`.
3. If applicable, label the issue with `beginner friendly` to denote that the issue is suitable for a beginner to work on.

## Investigation of issues

When an issue has all basic information provided, but the reported problem cannot be reproduced at a first glance, label the issue `triage/needs-information` and post a comment explaining why this label is being applied. Depending on the perceived severity and/or number of upvotes, the investigation will either be delegated to another maintainer for further investigation or put on hold until someone else (maintainer or contributor) picks it up and eventually starts investigating it.


Even if you don't have the time or the knowledge to investigate an issue we highly recommend that you upvote the issue if you happen to have the same problem. If you have further details that may help with investigating the issue please provide as much information as possible.

## External pull requests

Part of issue triage should also be triaging of external PRs. The main goal should be to make sure PRs from external contributors have an owner/reviewer and are not forgotten.

1. Check new external PRs which do not have a reviewer.
1. Check if there is a link to an existing issue.
1. If not and you know which issue it is solving, add the link yourself, otherwise ask the author to link the issue or create one.
1. Assign a reviewer based on who was handling the linked issue or what code or feature the PR touches (look at who was the last to make changes there if all else fails).

## GitHub issue management workflow

The following section describes the triage workflow for new GitGHub issues that get created.

### GitHub Issue: Bug

This workflow starts off with a GitHub issue of type bug being created.

1. Collaborator or maintainer creates a GitHub bug using the appropriate GitHub issue template
2. By default a bug will be created with the `type/bug` and `needs-triage` labels

The following flowchart defines the workflow,


```                                                                                                                                                     
                                               +--------------------------+                                                                              
                                               | New bug issue opened/more|                                                                              
                                               | information added        |                                                                              
                                               +-------------|------------+                                                                              
                                                             |                                                                                           
                                                             |                                                                                           
   +----------------------------------+  NO   +--------------|-------------+                                                                             
   | label: triage/needs-information  ---------  All required information  |                                                                             
   |                                  |       |  contained in issue?       |                                                                             
   +-----------------------------|----+       +--------------|-------------+                                                                             
                                 |                           | YES                                                                                       
                                 |                           |                                                                                           
   +--------------------------+  |                +---------------------+ YES +---------------------------------------+                                  
   |label:                    |  |                |  Duplicate Issue?    ------- Comment `Duplicate of #<issue number>`                                   
   |triage/needs-investigation|  | NO             |                     |     | Remove needs-triage label             |                                  
   +------|-------------------+  |                +----------|----------+     | label: triage/duplicate               |                                  
          |                      |                           | NO             +-----------------|---------------------+                                  
      YES |                      |                           |                                  |                                                        
          |      +---------------|----+   NO    +------------|------------+                     |                                                        
          |      |Needs investigation?|----------  Can it be reproduced?  |                     |                                                        
          |-------                    |         +------------|------------+                     |                                                        
                 +--------------------+                      | YES                              |                                                        
                                                             |                       +----------|----------+                                             
    +-------------------------+                 +------------|------------+          |  Close Issue        |                                             
    | Add release-found label |------------------  Works as intended?     |          |                     |                                             
    | label: release-found/*  |        NO       |                         |          +----------|----------+                                             
    +------------|------------+                 +------------|------------+                     |                                                        
                 |                                           |                                  |                                                        
                 |                                           | YES                              |                                                        
                 |                          +----------------|----------------+                 |                                                        
   +--------------------------+             | Add comment                     |                 |                                                        
   |   Add area label         |             | Remove needs-triage label       ------------------|                                                        
   |   label: area/*          |             | label: triage/works-as-intended |                                                                          
   +-------------|------------+             +---------------------------------+                                                                          
                 |                                                                                                                                       
                 |                        +----------+                                                                                                   
                 |                        |   Done   ----------------------------------------                                                            
                 |                        +----|-----+                                      |                                                            
                 |                             |NO                                          |                                                            
                 |                             |                         +------------------|------------------+                                         
    +------------|-------------+          +----|----------------+ YES    |  Add details to issue               |                                         
    |                          ------------  Signal Community?  ----------  label: help wanted                 |                                         
    |Remove needs-triage label |          |                     |        |  label: beginner friendly (optional)|                                         
    +--------------------------+          +---------------------+        +-------------------------------------+                                          
                                                                                                                                                                                       
```

### GitHub Issue: Feature request
 
```         
                                            +---------------------------------+                                                  
                                            |New feature request issue opened/|                                                  
                                            |more information added           |                                                  
                                            +----------------|----------------+                                                  
                                                             |                                                                   
                                                             |                                                                   
    +---------------------------------+ NO     +-------------|------------+                                                      
    | label: triage/needs-information ---------- All required information |                                                      
    |                                 |        | contained in issue?      |                                                      
    +---------------------------------+        +-------------|------------+                                                      
                                                             |                                                                   
                                                             |                                                                   
    +---------------------------------------+                |                                                                   
    |Comment `Duplicate of #<issue number>` | YES +----------|----------+                                                        
    |Remove needs-triage label              -------  Duplicate issue?   |                                                        
    |label: triage/duplicate                |     |                     |                                                        
    +-----|---------------------------------+     +-----------|---------+                                                        
          |                                                   |NO                                                                
          |  +-------------------------+  NO   +-----------------------------+                                                   
          |  |Add comment              |--------  Is this a valid feature?   |                                                   
          |  |Remove needs-triage label|       |                             |                                                   
          |  +------|------------------+       +--------------|--------------+                                                   
          |         |                                         | YES                                                              
          |         |                                         |                                                                  
          |         |                         +---------------|--------------+                                                                                                    
          |         |                         | label: type/feature          |                                                   
        +-|---------|---+       +--------+    | Remove needs-triage label    |                                                   
        |  Close issue  |       |  Done  ------ Remove type/feature-request  |                                                   
        |               |       |        |    | milestone?                   |                                                   
        +---------------+       +--------+    +------------------------------+           
```
If the author does not respond to a request for more information within the timespan of a week, close the issue with a kind note stating that the author can request for the issue to be reopened when the necessary information is provided.

In some cases you may receive a request you do not wish to accept.  Perhaps the request doesn't align with the project scope or vision.  It is important to tactfully handle requests that don't meet the project standards.

1. Acknowledge the person behind the request and thank them for their interest and request.
2. Explain why it didn't fit into the scope of the project or vision.
3. Don't leave an unwanted request open.  Immediately close the request you do not wish to accept.



