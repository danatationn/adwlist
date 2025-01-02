from pathlib import Path


def main() -> None:
	styles_path = Path.cwd() / 'styles'
	if not styles_path.exists():
		raise FileNotFoundError('styles/ has not been found. \nplease redownload the repo and try again')

	styles = sorted(styles_path.rglob('*.less'))
	usercss_path = Path.cwd() / 'styles' / 'user.css'
	if not usercss_path.exists():
		raise FileNotFoundError('kldjfklsdjkfl')

	with open(usercss_path, 'r') as f:
		compiled_less = f.read() + '\n'

	compiled_less += '@-moz-document url-prefix("https://filelist.io") {' + '\n'

	for style in styles:
		with open(style, 'r') as f:
			compiled_less += f.read() + '\n'

	compiled_less += '}' + '\n'

	compiled_path = Path.cwd() / 'style.user.css'
	with open(compiled_path, 'w') as f:
		f.write(compiled_less)

	print('succesfully compiled style.user.css 😎\n')


if __name__ == '__main__':
	main()

