# Results

- fork: faster-cpython
- version: 3.14.0a0
- config: T2
- commit hash: [af5ed4b](https://github.com/faster%2dcpython/cpython/commit/af5ed4b)
- commit date: 2024-08-19T16:31:13+01:00
- commit merge base: [e077b201f49a6007ddad7c1b6e3069a037b6d952](https://github.com/faster%2dcpython/cpython/commit/e077b201f49a6007ddad7c1b6e3069a037b6d952)
- ref: call_class_tier_2

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10454522176)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-192-generic-x86_64-with-glibc2.31
- [raw results](bm-20240819-linux-x86_64-faster%252dcpython-call_class_tier_2-3.14.0a0-af5ed4b.json)

### vs. 3.10.4

- Geometric mean: 1.23x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.14x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240819-linux-x86_64-faster%252dcpython-call_class_tier_2-3.14.0a0-af5ed4b-vs-3.10.4.md)
- [📈time plot](bm-20240819-linux-x86_64-faster%252dcpython-call_class_tier_2-3.14.0a0-af5ed4b-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.04x slower at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240819-linux-x86_64-faster%252dcpython-call_class_tier_2-3.14.0a0-af5ed4b-vs-3.12.0.md)
- [📈time plot](bm-20240819-linux-x86_64-faster%252dcpython-call_class_tier_2-3.14.0a0-af5ed4b-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.14x slower (HPT: reliability of 100.00%, 1.10x slower at 99th %ile)
- Memory usage: 1.02x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- [📄table](bm-20240819-linux-x86_64-faster%252dcpython-call_class_tier_2-3.14.0a0-af5ed4b-vs-3.13.0.md)
- [📈time plot](bm-20240819-linux-x86_64-faster%252dcpython-call_class_tier_2-3.14.0a0-af5ed4b-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.13x faster (HPT: reliability of 100.00%, 1.06x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240819-linux-x86_64-faster%252dcpython-call_class_tier_2-3.14.0a0-af5ed4b-vs-base-mem.svg)
- [📄table](bm-20240819-linux-x86_64-faster%252dcpython-call_class_tier_2-3.14.0a0-af5ed4b-vs-base.md)
- [📈time plot](bm-20240819-linux-x86_64-faster%252dcpython-call_class_tier_2-3.14.0a0-af5ed4b-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20240819-linux-x86_64-faster%252dcpython-call_class_tier_2-3.14.0a0-af5ed4b-vs-3.13.0b2.md)
- [📈time plot](bm-20240819-linux-x86_64-faster%252dcpython-call_class_tier_2-3.14.0a0-af5ed4b-vs-3.13.0b2.svg)

