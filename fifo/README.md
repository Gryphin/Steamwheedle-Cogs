# fifo
Base command for handling scheduling of tasks

## Usage
All settings are available under `[p]fifo`.

## Guild Commands
| Command        | Description                                                  |
| :------------- | :----------------------------------------------------------- |
| `background`   | Sets or removes the background image for the welcome message |
| `test`         | Send a test message in the current channel                   |
| `toggle`       | Enable or disable this cog in the current guild              |
| `reset`        | Reset all settings to the default values                     |

### avatar
`[p]fifo avatar`
| Command        | Description                                                  |
| :------------- | :----------------------------------------------------------- |
| `border`       | Set the profile picture border width                         |
| `border_color` | Set the profile picture border color using RGB values        |
| `position`     | Set the position of the profile picture                      |
| `radius`       | Set the radius of the profile picture                        |

### channel
`[p]fifo channel`
| Command | Description                                    |
| :------ | :--------------------------------------------- |
| `join`  | Set the channel to send the welcome message in |
| `leave` | Set the channel to send the leave message in   |

### count
`[p]fifo count`
| Command    | Description                                   |
| :--------- | :-------------------------------------------- |
| `color`    | Set the color of the counter using RGB values |
| `position` | Set the position of the member count overlay  |
| `size`     | Set the font size of the counter              |

### member
`[p]fifo member`
| Command         | Description                                      |
| :-------------- | :----------------------------------------------- |
| `join_image`    | Enable or disable image when a member joins      |
| `join_message`  | Set the message to send when a member joins      |
| `join_roles`    | Set the roles to give to a member when they join |
| `leave_image`   | Enable or disable image when a member leaves     |
| `leave_message` | Set the message to send when a member leaves     |
| `leave_toggle`  | Enable or disable the leave message altogether   |

### text
`[p]fifo text`
| Command    | Description                                   |
| :--------- | :-------------------------------------------- |
| `color`    | Set the color of the text using RGB values    |
| `position` | Set the position of the member joined overlay |
| `size`     | Set the font size of the text                 |
