# D1

## Layout

## FileSystem

Create folders

- assets
	- `import assets`
- resources 
	- `import assets`
- scenes
- scripts

## Project Settings

- Application
	- Config
		Icon: res://assets/textures/icon.png
	- Run
		Main Scene: res://scenes/game.tscn
	- boot splash
		Image: res://assets/textures/splash_screen.png

- Display
	- viewpoint width 540
	- viewpoint height 960

## Begin D1

- Create first scene: 2D Scene > name: **Game**
	- change **Game** to type `CanvasLayer`

- **Game** > add child note > type `control`, name: **UI**
	- Select **UI** > inspector > Layout > *Anchors Preset*: `Full Rect`

- **UI** > add child > `Label` name **BestScore**
	- Text: Best: 0
	- Horizontal Alignment: *Center*
	- Vertical Alignment: *Center*
	- Layout Mode: *Anchors*
	- Anchors Preset *Center*
	- Label Settings: `New LableSettings`
		- Line Spacing: 3px
		- Font: res://assets/fonts/Unitblock/Unitblock.ttf
		- Font Size: 40px
		- Outline Color: black
		- Shadow size: 10px
		- Shadow color: #0000003b
		- Shadow offset x: 3px
		- Shadow offset y: 3px
	- transform Position y: 140px
	- Visibility Self Modulate: #555555

- **UI** > add child > `Label` name **Score**
	- Text: Best: 0
	- Horizontal Alignment: *Center*
	- Vertical Alignment: *Center*
	- Layout Mode: *Anchors*
	- Anchors Preset *Center*
	- Label Settings: `New LableSettings`
		- Line Spacing: 3px
		- Font: res://assets/fonts/Unitblock/Unitblock.ttf
		- Font Size: 40px
		- Outline Color: black
		- Shadow size: 10px
		- Shadow color: #0000003b
		- Shadow offset x: 3px
		- Shadow offset y: 3px
	- transform Position y: 140px

### `F5`

- **UI** > add child > `TextureButton` name **Restart**
	- Stretch Mode: Keep Aspect Centered
	- Textures Normal: res://assets/textures/restart.png
	- Layout Mode: *Anchors*
	- Anchors Preset *Center*
	- transform Position y: 790px

### `F5`

- **UI** > add child > `ColorRect` name **GameOver**
	- Color: #000000a8
	- Layout Mode: *Anchors*
	- Anchors Preset *FUll Rect*
	
- **GameOver** > add child > `Label`
	- Text: Game Over!
	- Layout Mode: *Anchors*
	- Anchors Preset *Center*
	- Label Settings: `New LableSettings`
		- Line Spacing: 3px
		- Font: res://assets/fonts/Unitblock/Unitblock.ttf
		- Font Size: 80px
		- Outline Color: black
		- Shadow size: 10px
		- Shadow color: #0000003b
		- Shadow offset x: 3px
		- Shadow offset y: 3px

### `F5`

- **GameOver** > Toggle Visible off

### `F5`

- **UI** > add child > `Control` name **Grid**
	- Transform Size x: 512px
	- Transform Size y: 512px
	- Anchors Preset *Center*

### `F5`

- **Grid** > add child > `Panel` name **Background**
	- Layout Mode: *Anchors*
	- Anchors Preset *Full Rect*
	- Theme Overrides > style > panel > res://resources/styles/background.tres

- **Grid** > add child > `GridContainer` name **Container**
	- Columns: 4
	- Layout custom minimum size 512x512
	- Anchors Preset: Center
	- Transform size: 512x512
	- Position: 4x4
	- Theme Overrides > constants > H,V Separation 8x8

- New Scene > 2D Scene
	- name: GridCell, save as name grid_cell.tscn in scenes folder
	- type panel
		- custom minimum size x: 120
		- custom minimum size y: 120
		- Anchors Preset *Center*
		- Transform size 128x128
		- Transform position 206x416
		- Transform pivot offset 64x64
		- Theme Overrides > style > panel > res://resources/styles/grid_cell.tres

- **Grid > Container** > instanceciate child note > grid_cell.tscn > GridCell

- **Grid > Container > GridCell** > Ctrl + D to create 15 remaining grid cell

### `F5`
