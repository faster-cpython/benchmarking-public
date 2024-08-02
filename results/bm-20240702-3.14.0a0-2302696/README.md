# Results

- fork: Fidget-Spinner
- version: 3.14.0a0
- config: 
- commit hash: [2302696](https://github.com/Fidget%2dSpinner/cpython/commit/2302696)
- commit date: 2024-07-02T22:23:39+08:00
- commit merge base: [6343486eb60ac5a9e15402a592298259c5afdee1](https://github.com/Fidget%2dSpinner/cpython/commit/6343486eb60ac5a9e15402a592298259c5afdee1)
- ref: macro_ify

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9765724010)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240702-linux-x86_64-Fidget%252dSpinner-macro_ify-3.14.0a0-2302696.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.31x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240702-linux-x86_64-Fidget%252dSpinner-macro_ify-3.14.0a0-2302696-vs-3.10.4.md)
- [📈time plot](bm-20240702-linux-x86_64-Fidget%252dSpinner-macro_ify-3.14.0a0-2302696-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240702-linux-x86_64-Fidget%252dSpinner-macro_ify-3.14.0a0-2302696-vs-3.12.0.md)
- [📈time plot](bm-20240702-linux-x86_64-Fidget%252dSpinner-macro_ify-3.14.0a0-2302696-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240702-linux-x86_64-Fidget%252dSpinner-macro_ify-3.14.0a0-2302696-vs-3.13.0b2.md)
- [📈time plot](bm-20240702-linux-x86_64-Fidget%252dSpinner-macro_ify-3.14.0a0-2302696-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 99.82%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240702-linux-x86_64-Fidget%252dSpinner-macro_ify-3.14.0a0-2302696-vs-base-mem.svg)
- [📄table](bm-20240702-linux-x86_64-Fidget%252dSpinner-macro_ify-3.14.0a0-2302696-vs-base.md)
- [📈time plot](bm-20240702-linux-x86_64-Fidget%252dSpinner-macro_ify-3.14.0a0-2302696-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9764247137)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240702-pythonperf1-amd64-Fidget%252dSpinner-macro_ify-3.14.0a0-2302696.json)

### vs. 3.10.4

- Geometric mean: 1.27x faster (HPT: reliability of 100.00%, 1.16x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240702-pythonperf1-amd64-Fidget%252dSpinner-macro_ify-3.14.0a0-2302696-vs-3.10.4.md)
- [📈time plot](bm-20240702-pythonperf1-amd64-Fidget%252dSpinner-macro_ify-3.14.0a0-2302696-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240702-pythonperf1-amd64-Fidget%252dSpinner-macro_ify-3.14.0a0-2302696-vs-3.12.0.md)
- [📈time plot](bm-20240702-pythonperf1-amd64-Fidget%252dSpinner-macro_ify-3.14.0a0-2302696-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x faster (HPT: reliability of 99.99%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240702-pythonperf1-amd64-Fidget%252dSpinner-macro_ify-3.14.0a0-2302696-vs-3.13.0b2.md)
- [📈time plot](bm-20240702-pythonperf1-amd64-Fidget%252dSpinner-macro_ify-3.14.0a0-2302696-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240702-pythonperf1-amd64-Fidget%252dSpinner-macro_ify-3.14.0a0-2302696-vs-base.md)
- [📈time plot](bm-20240702-pythonperf1-amd64-Fidget%252dSpinner-macro_ify-3.14.0a0-2302696-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9764250031)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240702-pythonperf1_win32-x86-Fidget%252dSpinner-macro_ify-3.14.0a0-2302696.json)

### vs. 3.10.4

- Geometric mean: 1.14x faster (HPT: reliability of 100.00%, 1.03x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240702-pythonperf1_win32-x86-Fidget%252dSpinner-macro_ify-3.14.0a0-2302696-vs-3.10.4.md)
- [📈time plot](bm-20240702-pythonperf1_win32-x86-Fidget%252dSpinner-macro_ify-3.14.0a0-2302696-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.15x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240702-pythonperf1_win32-x86-Fidget%252dSpinner-macro_ify-3.14.0a0-2302696-vs-3.12.0.md)
- [📈time plot](bm-20240702-pythonperf1_win32-x86-Fidget%252dSpinner-macro_ify-3.14.0a0-2302696-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x slower (HPT: reliability of 100.00%, 1.03x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240702-pythonperf1_win32-x86-Fidget%252dSpinner-macro_ify-3.14.0a0-2302696-vs-3.13.0b2.md)
- [📈time plot](bm-20240702-pythonperf1_win32-x86-Fidget%252dSpinner-macro_ify-3.14.0a0-2302696-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240702-pythonperf1_win32-x86-Fidget%252dSpinner-macro_ify-3.14.0a0-2302696-vs-base.md)
- [📈time plot](bm-20240702-pythonperf1_win32-x86-Fidget%252dSpinner-macro_ify-3.14.0a0-2302696-vs-base.svg)

