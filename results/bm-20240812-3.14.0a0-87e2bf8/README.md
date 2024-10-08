# Results

- fork: faster-cpython
- version: 3.14.0a0
- config: 
- commit hash: [87e2bf8](https://github.com/faster%2dcpython/cpython/commit/87e2bf8)
- commit date: 2024-08-12T11:46:46+01:00
- commit merge base: [253c6a0b2f88b3327b7113860b99d665346fe43c](https://github.com/faster%2dcpython/cpython/commit/253c6a0b2f88b3327b7113860b99d665346fe43c)
- ref: fix_122821

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10350492312)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240812-linux-x86_64-faster%252dcpython-fix_122821-3.14.0a0-87e2bf8.json)

### vs. 3.10.4

- Geometric mean: 1.42x faster (HPT: reliability of 100.00%, 1.29x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240812-linux-x86_64-faster%252dcpython-fix_122821-3.14.0a0-87e2bf8-vs-3.10.4.md)
- [📈time plot](bm-20240812-linux-x86_64-faster%252dcpython-fix_122821-3.14.0a0-87e2bf8-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.02x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240812-linux-x86_64-faster%252dcpython-fix_122821-3.14.0a0-87e2bf8-vs-3.12.0.md)
- [📈time plot](bm-20240812-linux-x86_64-faster%252dcpython-fix_122821-3.14.0a0-87e2bf8-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240812-linux-x86_64-faster%252dcpython-fix_122821-3.14.0a0-87e2bf8-vs-3.13.0b2.md)
- [📈time plot](bm-20240812-linux-x86_64-faster%252dcpython-fix_122821-3.14.0a0-87e2bf8-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x slower (HPT: reliability of 99.11%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240812-linux-x86_64-faster%252dcpython-fix_122821-3.14.0a0-87e2bf8-vs-base-mem.svg)
- [📄table](bm-20240812-linux-x86_64-faster%252dcpython-fix_122821-3.14.0a0-87e2bf8-vs-base.md)
- [📈time plot](bm-20240812-linux-x86_64-faster%252dcpython-fix_122821-3.14.0a0-87e2bf8-vs-base.svg)

