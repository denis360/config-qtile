# Configuracion del WM Qtile
_Estas intrucciones te permitiran tener esta configuracion funcionando en tu dispositivo con una distribucion de linux instalada :)_

![](docs/screenshot.png)

Primero lo primero instala Qtile y dependencias
```bash
sudo pacman -S qtile pacman-contrib nm-applet cbatticon volumeicon
yay -S nerd-fonts-ubuntu-mono
pip install psutil
```

Descargar las fuente de la barra de tareas
* [Mononoki NF](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/Mononoki.zip)
* [Caskaydia NF](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/CascadiaCode.zip)

Llevar las fuentes a la carpeta de las fuentes
```bash
sudo mkdir /usr/share/fonts/mononoki && sudo mkdir /usr/share/fonts/caskaydia
cd ~/Downloads && sudo mv Mononoki.zip /usr/share/fonts/mononoki && sudo mv CascadiaCode.zip /usr/share/fonts/caskaydia
cd /usr/share/fonts/mononoki && sudo unzip Mononoki.zip
cd /usr/share/fonts/caskaydia && sudo unzip CascadiaCode.zip && cd
```

Clona este repositorio y copia el archivo donde se encuentran estas configuraciones
```bash
git clone https://github.com/denis360/config-qtile.git ~/.config/qtile
```

Instala un menu como dmenu o rofi
```
sudo pacman -S rofi
```
Puedes editar el atajo para abrir el menu en:
```python
key([mod], "space", lazy.spawn("rofi -show drun"))
```

## Control del volumen
```bash
sudo pacman -S pamixer alsa-tools alsa-utils
```
Puedes editar la configuracion en:
```python
key([mod, "control"], "Up", lazy.spawn("pamixer --decrease 5")),
key([mod, "control"], "Down", lazy.spawn("pamixer --increase 5")),
key([mod, "control"], "m", lazy.spawn("pamixer --toggle-mute")),
```

## Control del brillo
No tendras control de tu brillo en pantalla asi que instala brightnessctl
```bash
sudo pacman -S brightnessctl
```
Puedes cambiar la configuracion en:
```python
Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 10%+")),
Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
```

