#!/usr/bin/env python3
import os
import json
import uuid
import argparse
from datetime import datetime
from pathlib import Path


class LLMProject:
    def __init__(self, project_path="."):
        self.project_path = Path(project_path)
        self.state_dir = self.project_path / "state"
        self.sessions_dir = self.project_path / "sessions"
        self.config_dir = self.project_path / "config"

    def init_project(self, name, project_type="default"):
        """Initialize new project structure"""
        # Create directory structure
        for dir_path in [self.state_dir, self.sessions_dir / "archive", self.config_dir / "templates"]:
            dir_path.mkdir(parents=True, exist_ok=True)

        # Initialize project configuration
        project_config = {
            "name": name,
            "type": project_type,
            "created_date": datetime.now().isoformat(),
            "settings": {
                "state_tracking": {"enabled": True},
                "session_management": {"auto_archive": True},
                "automation_rules": {"context_generation": "auto"}
            }
        }
        self._save_json(self.config_dir / "project.json", project_config)

        # Initialize current state
        initial_state = {
            "version": "1.0",
            "last_updated": datetime.now().isoformat(),
            "current_phase": "initialization",
            "active_features": [],
            "pending_tasks": [],
            "recent_changes": [],
            "decisions": []
        }
        self._save_json(self.state_dir / "current.json", initial_state)

        print(f"Initialized LLM project: {name}")

    def start_session(self):
        """Start new development session"""
        session_id = str(uuid.uuid4())
        current_state = self._load_json(self.state_dir / "current.json")

        session_data = {
            "session_id": session_id,
            "start_time": datetime.now().isoformat(),
            "context": {
                "project_state": current_state,
                # Top 5 pending tasks
                "active_tasks": current_state.get("pending_tasks", [])[:5],
                # Last 5 changes
                "relevant_history": current_state.get("recent_changes", [])[:5]
            },
            "progress": {
                "changes": [],
                "decisions": [],
                "new_tasks": []
            }
        }
        self._save_json(self.sessions_dir / "current.json", session_data)

        # Generate context for LLM
        context = self.generate_context()
        print("\nContext for LLM session:")
        print("------------------------")
        print(json.dumps(context, indent=2))

        return session_id

    def end_session(self):
        """End current session and update project state"""
        try:
            current_session = self._load_json(
                self.sessions_dir / "current.json")
            current_state = self._load_json(self.state_dir / "current.json")

            # Update state with session progress
            current_state["recent_changes"].extend(
                current_session["progress"]["changes"])
            current_state["decisions"].extend(
                current_session["progress"]["decisions"])
            current_state["pending_tasks"].extend(
                current_session["progress"]["new_tasks"])
            current_state["last_updated"] = datetime.now().isoformat()

            # Archive session
            archive_path = self.sessions_dir / "archive" / \
                f"session_{current_session['session_id']}.json"
            current_session["end_time"] = datetime.now().isoformat()
            self._save_json(archive_path, current_session)

            # Update current state
            self._save_json(self.state_dir / "current.json", current_state)

            # Clean up current session
            (self.sessions_dir / "current.json").unlink(missing_ok=True)

            print("Session ended and state updated")
        except FileNotFoundError:
            print("No active session found")

    def update_state(self, changes=None, decisions=None, new_tasks=None):
        """Update current session progress"""
        try:
            current_session = self._load_json(
                self.sessions_dir / "current.json")

            if changes:
                current_session["progress"]["changes"].extend(changes)
            if decisions:
                current_session["progress"]["decisions"].extend(decisions)
            if new_tasks:
                current_session["progress"]["new_tasks"].extend(new_tasks)

            self._save_json(self.sessions_dir /
                            "current.json", current_session)
            print("Session progress updated")
        except FileNotFoundError:
            print("No active session found")

    def generate_context(self):
        """Generate context for LLM"""
        try:
            current_session = self._load_json(
                self.sessions_dir / "current.json")
            current_state = self._load_json(self.state_dir / "current.json")
            project_config = self._load_json(self.config_dir / "project.json")

            context = {
                "project_info": {
                    "name": project_config["name"],
                    "type": project_config["type"],
                    "current_phase": current_state["current_phase"]
                },
                "current_state": {
                    "active_features": current_state["active_features"],
                    "pending_tasks": current_state["pending_tasks"],
                    # Last 5 changes
                    "recent_changes": current_state["recent_changes"][-5:]
                },
                "session_info": {
                    "session_id": current_session["session_id"],
                    "progress": current_session["progress"]
                }
            }
            return context
        except FileNotFoundError:
            return {"error": "No active session or missing configuration"}

    def _save_json(self, path, data):
        """Save data to JSON file"""
        with open(path, 'w') as f:
            json.dump(data, indent=2, default=str, fp=f)

    def _load_json(self, path):
        """Load data from JSON file"""
        with open(path, 'r') as f:
            return json.load(f)


def main():
    parser = argparse.ArgumentParser(description='LLM Project Management Tool')
    subparsers = parser.add_subparsers(
        dest='command', help='Available commands')

    # Init command
    init_parser = subparsers.add_parser('init', help='Initialize new project')
    init_parser.add_argument('name', help='Project name')
    init_parser.add_argument('--type', default='default', help='Project type')

    # Start command
    subparsers.add_parser('start', help='Start new session')

    # End command
    subparsers.add_parser('end', help='End current session')

    # Update command
    update_parser = subparsers.add_parser(
        'update', help='Update session progress')
    update_parser.add_argument(
        '--changes', '-c', nargs='+', help='Changes made')
    update_parser.add_argument(
        '--decisions', '-d', nargs='+', help='Decisions made')
    update_parser.add_argument('--tasks', '-t', nargs='+', help='New tasks')

    # Context command
    subparsers.add_parser('context', help='Generate context for LLM')

    args = parser.parse_args()
    project = LLMProject()

    if args.command == 'init':
        project.init_project(args.name, args.type)
    elif args.command == 'start':
        project.start_session()
    elif args.command == 'end':
        project.end_session()
    elif args.command == 'update':
        project.update_state(args.changes, args.decisions, args.tasks)
    elif args.command == 'context':
        print(json.dumps(project.generate_context(), indent=2))
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
