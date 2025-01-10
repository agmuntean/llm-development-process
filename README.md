# LLM Development Process

A structured system for maintaining context and progress in LLM-assisted development projects.

## Project Structure

project_context/
├── 0_foundation/ # Immutable project foundation documents
├── 1_sessions/ # Individual session logs and progress
├── 2_current_state/ # Active project state and progress
├── 3_technical/ # Technical documentation and architecture
└── 4_process/ # Process documentation and templates

## How to Use This Repository

1. **Starting a New Project**

   - Initialize project foundation in `0_foundation/`
   - Set up initial technical architecture in `3_technical/`
   - Create first session log in `1_sessions/`

2. **During Development**

   - Document each session in `1_sessions/`
   - Keep `2_current_state/` updated
   - Maintain technical documentation in `3_technical/`

3. **Session Structure**
   - Each session has a pre-session brief
   - Active development documentation
   - Post-session summary and state update

## Documentation Standards

All documentation follows these principles:

- Clear and consistent structure
- Progressive detail levels
- Traceable decision history
- Actionable next steps

## Directory Details

### 0_foundation/

Contains the immutable foundation documents that define the project's scope, requirements, and initial architecture. These documents are treated as stable, with changes made only when significant pivots occur.

### 1_sessions/

Contains detailed logs of each development session. Each session includes:

- Pre-session context
- Session objectives
- Progress logs
- Decisions made
- Next steps

### 2_current_state/

Maintains the active state of the project:

- Implemented features
- In-progress work
- Pending tasks
- Current blockers
- Recent changes

### 3_technical/

Houses all technical documentation:

- System architecture
- Component specifications
- Data structures
- API documentation
- Performance considerations
- Security standards

### 4_process/

Contains process documentation and templates:

- Session templates
- Documentation guidelines
- Review checklists
- Best practices

## Session Management

### Pre-Session

Before each development session:

1. Review current state documentation
2. Prepare session objectives
3. Gather relevant technical context
4. Update context document for LLM

### During Session

While working with the LLM:

1. Document all decisions
2. Track changes and progress
3. Note any blockers or challenges
4. Update technical documentation as needed

### Post-Session

After each session:

1. Summarize progress
2. Update state documentation
3. Prepare context for next session
4. Push documentation updates

## Context Management

The repository maintains three levels of context:

1. **Foundation Context**

   - Project requirements
   - Architectural decisions
   - Technical constraints
   - Core objectives

2. **Active Context**

   - Current state
   - Active development
   - Recent changes
   - Immediate goals

3. **Session Context**
   - Session-specific objectives
   - Relevant background
   - Required decisions
   - Expected outcomes

## Best Practices

1. **Documentation Updates**

   - Update documentation in real-time during sessions
   - Keep current state accurate and up-to-date
   - Document decisions as they are made
   - Maintain clear next steps

2. **Context Management**

   - Provide focused, relevant context to LLM
   - Maintain clear decision history
   - Track changes and their rationale
   - Keep dependencies updated

3. **Process Consistency**
   - Follow session templates
   - Maintain documentation standards
   - Regular state updates
   - Clear communication protocols

## Contributing

When contributing to this process:

1. Follow the established directory structure
2. Use provided templates
3. Maintain documentation standards
4. Update context appropriately
5. Document any process improvements

## Process Evolution

This process is designed to evolve based on:

- Project needs
- Team feedback
- LLM capabilities
- Development patterns

Document any process improvements or modifications in the 4_process/evolution.md file.
