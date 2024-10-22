# Results

- fork: Yhg1s
- version: 3.13.0rc2+
- config: 
- commit hash: [8504cc0](https://github.com/Yhg1s/cpython/commit/8504cc0)
- commit date: 2024-09-30T21:02:15+00:00
- ref: 3.13_revert_incremen

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11112544532)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-196-generic-x86_64-with-glibc2.31
- [raw results](bm-20240930-linux-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-8504cc0.json)

### vs. 3.10.4

- Geometric mean: 1.36x faster (HPT: reliability of 100.00%, 1.30x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240930-linux-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-8504cc0-vs-3.10.4.md)
- [📈time plot](bm-20240930-linux-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-8504cc0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.97x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240930-linux-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-8504cc0-vs-3.12.0.md)
- [📈time plot](bm-20240930-linux-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-8504cc0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.00x slower (HPT: reliability of 56.89%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [📄table](bm-20240930-linux-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-8504cc0-vs-3.13.0.md)
- [📈time plot](bm-20240930-linux-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-8504cc0-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240930-linux-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-8504cc0-vs-3.13.0b2.md)
- [📈time plot](bm-20240930-linux-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-8504cc0-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11112544532)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-8504cc0.json)

### vs. 3.10.4

- Geometric mean: 1.21x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-8504cc0-vs-3.10.4.md)
- [📈time plot](bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-8504cc0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-8504cc0-vs-3.12.0.md)
- [📈time plot](bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-8504cc0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.00x slower (HPT: reliability of 94.13%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-8504cc0-vs-3.13.0.md)
- [📈time plot](bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-8504cc0-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-8504cc0-vs-3.13.0b2.md)
- [📈time plot](bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-8504cc0-vs-3.13.0b2.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11112544532)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-8504cc0.json)

### vs. 3.10.4

- Geometric mean: 1.12x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-8504cc0-vs-3.10.4.md)
- [📈time plot](bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-8504cc0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.17x faster (HPT: reliability of 100.00%, 1.17x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-8504cc0-vs-3.12.0.md)
- [📈time plot](bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-8504cc0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.04x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-8504cc0-vs-3.13.0.md)
- [📈time plot](bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-8504cc0-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-8504cc0-vs-3.13.0b2.md)
- [📈time plot](bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2%2B-8504cc0-vs-3.13.0b2.svg)

