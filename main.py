from pathlib import Path

import subprocess, shutil


def main() -> None:
    styles_path = Path.cwd() / 'styles'
    if not styles_path.exists():
        raise FileNotFoundError('styles/ has not been found. \nplease redownload the repo and try again')

    dartsass_path = Path(shutil.which('sass'))
    if not dartsass_path.exists():
        raise FileNotFoundError('dart-sass is not installed. \bplease get it and come back')

    subprocess.run([dartsass_path, styles_path])

    styles = sorted(styles_path.rglob('*.css'))

    # the usercss thing needs to be at the top !!.,
    index = None
    for style in styles:
        if style.name == 'user.css':
            index = styles.index(style)

    if not index:
        raise FileNotFoundError('styles/user.css has not been found. \nplease redownload the repo and try again')

    styles.insert(0, styles.pop(index))

    css = ''
    for style in styles:
        with open(style, 'r') as f:
            css += f.read() + '\n'

    compiled_path = Path.cwd() / 'style.css'
    with open(compiled_path, 'w') as f:
        f.write(css)


if __name__ == '__main__':
    main()

