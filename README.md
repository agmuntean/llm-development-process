# LLM Development Process

A structured system for maintaining context and progress in LLM-assisted development projects.

## Project Structure

```
project_context/
├── 0_foundation/         # Immutable project foundation documents
├── 1_sessions/          # Individual session logs and progress
├── 2_current_state/     # Active project state and progress
├── 3_technical/         # Technical documentation and architecture
└── 4_process/          # Process documentation and templates
```

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