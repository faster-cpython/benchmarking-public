# Results

- fork: brandtbucher
- version: 3.14.0a0
- config: JIT
- commit hash: [81f8369](https://github.com/brandtbucher/cpython/commit/81f8369)
- commit date: 2024-08-09T11:37:53-07:00
- commit merge base: [b5e142ba7c2063efe9bb8065c3b0bad33e2a9afa](https://github.com/brandtbucher/cpython/commit/b5e142ba7c2063efe9bb8065c3b0bad33e2a9afa)
- ref: jump_backward_0

## linux x86_64 (azure)

- [pystats raw](bm-20240809-azure-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369-pystats.json)
- [pystats table](bm-20240809-azure-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369-pystats.md)

### vs. base

- [pystats diff](bm-20240809-azure-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10324105308)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369.json)

### vs. 3.10.4

- Geometric mean: 1.40x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.28x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369-vs-3.10.4.md)
- [📈time plot](bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.06x faster (HPT: reliability of 99.32%, 1.00x faster at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369-vs-3.12.0.md)
- [📈time plot](bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.01x slower (HPT: reliability of 60.73%, 1.00x faster at 99th %ile)
- Memory usage: 1.15x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369-vs-3.13.0.md)
- [📈time plot](bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.02x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.06x
- [🧠memory plot](bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369-vs-base-mem.svg)
- [📄table](bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369-vs-base.md)
- [📈time plot](bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369-vs-3.13.0b2.md)
- [📈time plot](bm-20240809-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a0-81f8369-vs-3.13.0b2.svg)

