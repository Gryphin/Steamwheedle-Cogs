# recruit
Base command for handling scheduling of tasks

## Usage
All settings are available under `[p]recruit`.

## Guild Commands
| Command        | Description                                                  |
| :------------- | :----------------------------------------------------------- |
| `add`          | Add a new task to this guild's task list                     |  

### Add Triggers
`[p]recruit addtrigger`
| Command        | Description                                                  |
| :------------- | :----------------------------------------------------------- |
| `cron`         | Add a cron "time of day" trigger to the specified task       |
| `date`         | Add a "run once" datetime trigger to the specified task      |
| `interval`     | Add an interval trigger to the specified task                |
| `relative`     | trigger at a time relative from now to the specified task    |

### Check Tasks
`[p]recruit checktask`
| Command | Description                                    |
| :------ | :--------------------------------------------- |
| `checktask`  | Returns the next 10 scheduled executions of the task|

### count
`[p]recruit count`
| Command    | Description                                   |
| :--------- | :-------------------------------------------- |
| `color`    | Set the color of the counter using RGB values |
| `position` | Set the position of the member count overlay  |
| `size`     | Set the font size of the counter              |

### member
`[p]recruit member`
| Command         | Description                                      |
| :-------------- | :----------------------------------------------- |
| `join_image`    | Enable or disable image when a member joins      |
| `join_message`  | Set the message to send when a member joins      |
| `join_roles`    | Set the roles to give to a member when they join |
| `leave_image`   | Enable or disable image when a member leaves     |
| `leave_message` | Set the message to send when a member leaves     |
| `leave_toggle`  | Enable or disable the leave message altogether   |

### text
`[p]recruit text`
| Command    | Description                                   |
| :--------- | :-------------------------------------------- |
| `color`    | Set the color of the text using RGB values    |
| `position` | Set the position of the member joined overlay |
| `size`     | Set the font size of the text                 |
