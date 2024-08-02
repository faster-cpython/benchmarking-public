# Results

- fork: faster-cpython
- version: 3.13.0a6+
- config: JIT
- commit hash: [a701af9](https://github.com/faster%2dcpython/cpython/commit/a701af9)
- commit date: 2024-05-07T11:33:50+01:00
- commit merge base: [976212223541b89329d81ab01e3edd14d8f6aaf5](https://github.com/faster%2dcpython/cpython/commit/976212223541b89329d81ab01e3edd14d8f6aaf5)
- ref: no_globals_builtins_

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/8983880049)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240507-linux-x86_64-faster%252dcpython-no_globals_builtins_-3.13.0a6%2B-a701af9.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240507-linux-x86_64-faster%252dcpython-no_globals_builtins_-3.13.0a6%2B-a701af9-vs-3.10.4.md)
- [📈time plot](bm-20240507-linux-x86_64-faster%252dcpython-no_globals_builtins_-3.13.0a6%2B-a701af9-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.00x slower (HPT: reliability of 92.61%, 1.00x faster at 99th %ile)
- Memory usage: 1.07x
- missing benchmarks: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240507-linux-x86_64-faster%252dcpython-no_globals_builtins_-3.13.0a6%2B-a701af9-vs-3.12.0.md)
- [📈time plot](bm-20240507-linux-x86_64-faster%252dcpython-no_globals_builtins_-3.13.0a6%2B-a701af9-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x slower (HPT: reliability of 86.58%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: bpe_tokeniser
- [📄table](bm-20240507-linux-x86_64-faster%252dcpython-no_globals_builtins_-3.13.0a6%2B-a701af9-vs-3.13.0b2.md)
- [📈time plot](bm-20240507-linux-x86_64-faster%252dcpython-no_globals_builtins_-3.13.0a6%2B-a701af9-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 74.41%, 1.00x slower at 99th %ile)
- Memory usage: 0.99x
- [🧠memory plot](bm-20240507-linux-x86_64-faster%252dcpython-no_globals_builtins_-3.13.0a6%2B-a701af9-vs-base-mem.svg)
- [📄table](bm-20240507-linux-x86_64-faster%252dcpython-no_globals_builtins_-3.13.0a6%2B-a701af9-vs-base.md)
- [📈time plot](bm-20240507-linux-x86_64-faster%252dcpython-no_globals_builtins_-3.13.0a6%2B-a701af9-vs-base.svg)

