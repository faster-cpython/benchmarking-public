# Results

- fork: faster-cpython
- version: 3.14.0a0
- config: JIT
- commit hash: [71920f1](https://github.com/faster%2dcpython/cpython/commit/71920f1)
- commit date: 2024-07-30T10:12:55+01:00
- commit merge base: [d27a53fc02a87e76066fc4e15ff1fff3922a482d](https://github.com/faster%2dcpython/cpython/commit/d27a53fc02a87e76066fc4e15ff1fff3922a482d)
- ref: binary_subscr_getite

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/10192972991)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-186-generic-x86_64-with-glibc2.31
- [raw results](bm-20240730-linux-x86_64-faster%252dcpython-binary_subscr_getite-3.14.0a0-71920f1.json)

### vs. 3.10.4

- Geometric mean: 1.43x faster (HPT: reliability of 100.00%, 1.26x faster at 99th %ile)
- Memory usage: 1.19x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240730-linux-x86_64-faster%252dcpython-binary_subscr_getite-3.14.0a0-71920f1-vs-3.10.4.md)
- [📈time plot](bm-20240730-linux-x86_64-faster%252dcpython-binary_subscr_getite-3.14.0a0-71920f1-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 99.96%, 1.02x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240730-linux-x86_64-faster%252dcpython-binary_subscr_getite-3.14.0a0-71920f1-vs-3.12.0.md)
- [📈time plot](bm-20240730-linux-x86_64-faster%252dcpython-binary_subscr_getite-3.14.0a0-71920f1-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
- [📄table](bm-20240730-linux-x86_64-faster%252dcpython-binary_subscr_getite-3.14.0a0-71920f1-vs-3.13.0b2.md)
- [📈time plot](bm-20240730-linux-x86_64-faster%252dcpython-binary_subscr_getite-3.14.0a0-71920f1-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 93.66%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240730-linux-x86_64-faster%252dcpython-binary_subscr_getite-3.14.0a0-71920f1-vs-base-mem.svg)
- [📄table](bm-20240730-linux-x86_64-faster%252dcpython-binary_subscr_getite-3.14.0a0-71920f1-vs-base.md)
- [📈time plot](bm-20240730-linux-x86_64-faster%252dcpython-binary_subscr_getite-3.14.0a0-71920f1-vs-base.svg)

