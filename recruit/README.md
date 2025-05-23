# Recruit Cog

Provides commands for listing recruitment information and looking up details for specific guilds by their acronym.

## Usage

The main command group is `[p]recruit`.

## Commands

| Command                       | Description                                                                              |
| :---------------------------- | :--------------------------------------------------------------------------------------- |
| `[p]recruit list`             | Displays the list of currently recruiting guilds from the main recruitment sheet.        |
| `[p]recruit acronym <acronym>` | Displays detailed information for a specific guild, looked up by its acronym (e.g., XYZ). The acronym corresponds to a specific worksheet in the Google Sheet. Information is pulled from range B7:F26 of that worksheet. |

### Notes

*   The Cog relies on a Google Spreadsheet named "Steamwheedle Recruitment".
*   For the `acronym` command, each acronym must have its own worksheet in the spreadsheet.
*   Ensure the bot has correct permissions and API access to the Google Sheet.
```
