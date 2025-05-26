
import sys
import os
import argparse
import tiktoken
import csv
from rich import print
from rich.table import Table
from rich.console import Console

console = Console()

ENCODING = tiktoken.encoding_for_model("gpt-3.5-turbo")

def load_prompt(path):
    if not os.path.exists(path):
        console.print(f"[bold red]File not found:[/bold red] {path}")
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def count_tokens(text):
    return len(ENCODING.encode(text))

def analyze_prompt(text, model_limits=[4096, 8192, 32768], save_report=False):
    total_tokens = count_tokens(text)

    results = []
    table = Table(title="Token Pressure Report")
    table.add_column("Model Context", style="cyan")
    table.add_column("Status", style="magenta")

    for limit in model_limits:
        if total_tokens >= limit:
            status = "TRUNCATES"
            table.add_row(f"{limit} tokens", "[red]TRUNCATES[/red]")
        elif total_tokens >= limit * 0.75:
            status = "Approaching Limit"
            table.add_row(f"{limit} tokens", "[yellow]Approaching Limit[/yellow]")
        else:
            status = "Safe"
            table.add_row(f"{limit} tokens", "[green]Safe[/green]")
        results.append((limit, status))

    console.print(f"\n[bold]Total Tokens:[/bold] {total_tokens}")
    console.print(table)

    # Write CSV output
    with open("token_pressure_output.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["total_tokens", "context_limit", "status"])
        for limit, status in results:
            writer.writerow([total_tokens, limit, status])

    # Optional: write .report.txt
    if save_report:
        with open("token_pressure_report.txt", "w", encoding="utf-8") as f:
            f.write("Token Pressure Report\n")
            f.write("---------------------\n")
            f.write(f"Total Tokens: {total_tokens}\n\n")
            for limit, status in results:
                f.write(f"{limit} tokens  → {status}\n")

def main():
    parser = argparse.ArgumentParser(description="Token Pressure Sandbox (CLI)")
    parser.add_argument("input", help="Path to prompt file (.txt)")
    parser.add_argument("--save-report", action="store_true", help="Also save a .txt summary report")
    args = parser.parse_args()

    prompt = load_prompt(args.input)
    analyze_prompt(prompt, save_report=args.save_report)

if __name__ == "__main__":
    main()
