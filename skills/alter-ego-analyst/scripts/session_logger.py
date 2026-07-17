#!/usr/bin/env python3
"""
Alter Ego Analyst — Session Logger & Progress Tracker

Logs performance sessions and tracks progress toward unconscious competence.

Usage:
    python scripts/session_logger.py log --profile PATH --date YYYY-MM-DD --field "Boardroom" --duration 45 --activation-speed 3 --stability 40 --slippage 1 --forbidden 0 --command 5 --decompression 10 --bleed N --rating 8 --notes "Nailed the close"
    python scripts/session_logger.py stats --profile PATH
    python scripts/session_logger.py export --profile PATH --format csv
"""

import json
import csv
import sys
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional

SESSION_LOG_FILE = "alter_ego_sessions.json"


def load_sessions(profile_path: Path) -> List[Dict]:
    """Load session log for a profile."""
    log_file = profile_path.parent / SESSION_LOG_FILE
    if log_file.exists():
        with open(log_file, 'r') as f:
            return json.load(f)
    return []


def save_sessions(profile_path: Path, sessions: List[Dict]) -> None:
    """Save session log for a profile."""
    log_file = profile_path.parent / SESSION_LOG_FILE
    with open(log_file, 'w') as f:
        json.dump(sessions, f, indent=2)


def log_session(profile_path: Path, args) -> None:
    """Log a new session."""
    sessions = load_sessions(profile_path)
    
    session = {
        "date": args.date or datetime.now().strftime("%Y-%m-%d"),
        "field_of_play": args.field,
        "duration_minutes": args.duration,
        "activation_speed_seconds": args.activation_speed,
        "state_stability_minutes": args.stability,
        "slippage_count": args.slippage,
        "forbidden_words_used": args.forbidden,
        "command_words_used": args.command,
        "decompression_time_minutes": args.decompression,
        "identity_bleed": args.bleed.upper() == 'Y',
        "performance_rating": args.rating,
        "notes": args.notes or "",
        "logged_at": datetime.now().isoformat()
    }
    
    sessions.append(session)
    save_sessions(profile_path, sessions)
    
    print(f"✅ Session logged for {session['date']} — {session['field_of_play']}")
    print(f"   Rating: {session['performance_rating']}/10 | Slippage: {session['slippage_count']} | Activation: {session['activation_speed_seconds']}s")


def show_stats(profile_path: Path) -> None:
    """Show aggregated statistics."""
    sessions = load_sessions(profile_path)
    
    if not sessions:
        print("📭 No sessions logged yet.")
        return
    
    print(f"\n📊 ALTER EGO PERFORMANCE STATS ({len(sessions)} sessions)")
    print("=" * 60)
    
    # Overall averages
    avg_rating = sum(s['performance_rating'] for s in sessions) / len(sessions)
    avg_activation = sum(s['activation_speed_seconds'] for s in sessions) / len(sessions)
    avg_stability = sum(s['state_stability_minutes'] for s in sessions) / len(sessions)
    avg_slippage = sum(s['slippage_count'] for s in sessions) / len(sessions)
    avg_decompression = sum(s['decompression_time_minutes'] for s in sessions) / len(sessions)
    bleed_count = sum(1 for s in sessions if s['identity_bleed'])
    
    print(f"\nOverall Averages:")
    print(f"  Performance Rating:     {avg_rating:.1f}/10")
    print(f"  Activation Speed:       {avg_activation:.1f} seconds")
    print(f"  State Stability:        {avg_stability:.1f} minutes")
    print(f"  Slippage/Session:       {avg_slippage:.1f}")
    print(f"  Decompression Time:     {avg_decompression:.1f} minutes")
    print(f"  Identity Bleed Rate:    {bleed_count}/{len(sessions)} ({bleed_count/len(sessions)*100:.0f}%)")
    
    # Recent trend (last 5)
    recent = sessions[-5:]
    if len(recent) >= 2:
        print(f"\nRecent Trend (last {len(recent)} sessions):")
        recent_rating = sum(s['performance_rating'] for s in recent) / len(recent)
        recent_activation = sum(s['activation_speed_seconds'] for s in recent) / len(recent)
        recent_slippage = sum(s['slippage_count'] for s in recent) / len(recent)
        print(f"  Rating: {recent_rating:.1f} | Activation: {recent_activation:.1f}s | Slippage: {recent_slippage:.1f}")
    
    # By Field of Play
    fields = {}
    for s in sessions:
        field = s['field_of_play']
        if field not in fields:
            fields[field] = []
        fields[field].append(s)
    
    print(f"\nBy Field of Play:")
    for field, field_sessions in fields.items():
        avg_r = sum(s['performance_rating'] for s in field_sessions) / len(field_sessions)
        avg_s = sum(s['slippage_count'] for s in field_sessions) / len(field_sessions)
        print(f"  {field}: {len(field_sessions)} sessions | Rating: {avg_r:.1f} | Slippage: {avg_s:.1f}")


def export_csv(profile_path: Path, output_file: Optional[Path] = None) -> None:
    """Export sessions to CSV."""
    sessions = load_sessions(profile_path)
    
    if not sessions:
        print("📭 No sessions to export.")
        return
    
    if output_file is None:
        output_file = profile_path.parent / f"alter_ego_sessions_{datetime.now().strftime('%Y%m%d')}.csv"
    
    fieldnames = [
        "date", "field_of_play", "duration_minutes", "activation_speed_seconds",
        "state_stability_minutes", "slippage_count", "forbidden_words_used",
        "command_words_used", "decompression_time_minutes", "identity_bleed",
        "performance_rating", "notes", "logged_at"
    ]
    
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sessions)
    
    print(f"✅ Exported {len(sessions)} sessions to: {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Alter Ego Session Logger")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # Log command
    log_parser = subparsers.add_parser("log", help="Log a new session")
    log_parser.add_argument("--profile", required=True, help="Path to profile .md file")
    log_parser.add_argument("--date", help="Session date (YYYY-MM-DD)")
    log_parser.add_argument("--field", required=True, help="Field of Play")
    log_parser.add_argument("--duration", type=int, required=True, help="Duration in minutes")
    log_parser.add_argument("--activation-speed", type=int, required=True, help="Activation speed in seconds")
    log_parser.add_argument("--stability", type=int, required=True, help="State stability in minutes")
    log_parser.add_argument("--slippage", type=int, required=True, help="Slippage count")
    log_parser.add_argument("--forbidden", type=int, required=True, help="Forbidden words used")
    log_parser.add_argument("--command", type=int, required=True, help="Command words used")
    log_parser.add_argument("--decompression", type=int, required=True, help="Decompression time in minutes")
    log_parser.add_argument("--bleed", required=True, choices=['Y', 'N', 'y', 'n'], help="Identity bleed (Y/N)")
    log_parser.add_argument("--rating", type=int, required=True, choices=range(1, 11), help="Performance rating 1-10")
    log_parser.add_argument("--notes", help="Session notes")
    
    # Stats command
    stats_parser = subparsers.add_parser("stats", help="Show performance statistics")
    stats_parser.add_argument("--profile", required=True, help="Path to profile .md file")
    
    # Export command
    export_parser = subparsers.add_parser("export", help="Export sessions to CSV")
    export_parser.add_argument("--profile", required=True, help="Path to profile .md file")
    export_parser.add_argument("--output", help="Output CSV file path")
    export_parser.add_argument("--format", default="csv", choices=["csv"], help="Export format")
    
    args = parser.parse_args()
    
    profile_path = Path(args.profile).resolve()
    if not profile_path.exists():
        print(f"❌ Profile not found: {profile_path}")
        sys.exit(1)
    
    if args.command == "log":
        log_session(profile_path, args)
    elif args.command == "stats":
        show_stats(profile_path)
    elif args.command == "export":
        output = Path(args.output) if args.output else None
        export_csv(profile_path, output)


if __name__ == "__main__":
    main()