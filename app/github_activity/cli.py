import click
from app.github_activity.api import get_activity  # adjust path as needed


@click.command()
@click.argument("username")
def github_activity(username):
    """Fetch and display recent GitHub activity for a user."""
    events = get_activity(username)

    if not events:
        return

    click.echo(f"\nRecent GitHub activity for '{username}':\n")
    for i, event in enumerate(events, 1):
        event_type = event.get("type", "UnknownEvent")
        repo = event.get("repo", {}).get("name", "unknown/repo")
        created_at = event.get("created_at", "unknown time")
        click.echo(f"{i}. {event_type} on {repo} at {created_at}")
