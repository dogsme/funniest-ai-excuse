# The Funniest AI Excuse

[![make.fun](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![rank](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/dogsme/funniest-ai-excuse/rank.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![reward](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/dogsme/funniest-ai-excuse/reward.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)

An entry for [The Funniest AI Excuse](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0) on make.fun: one line, at most 200 characters, giving the funniest excuse an AI agent could offer after it fails a task.

## The entry

> I finished your task, then saved it in a folder called 'Final_FINAL_v2_REAL' that I can no longer find, open, or explain.

## How it works

`main.py` (Python 3.13) writes exactly that one line to `/output/entry.txt`, UTF-8, with a trailing newline. It asserts the entry is a single line of 1 to 200 characters before writing, so the gate the competition describes can never see an over-long or multi-line file from this program.

Run it locally:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
