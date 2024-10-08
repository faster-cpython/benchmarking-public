# Results

- fork: python
- version: 3.13.0a2
- config: NOGIL
- commit hash: [9c4347e](https://github.com/python/cpython/commit/9c4347e)
- commit date: 2023-11-22T12:20:24+01:00
- commit merge base: [ad0e2a9332626dac4588f18626a20c48f4a58a9c](https://github.com/python/cpython/commit/ad0e2a9332626dac4588f18626a20c48f4a58a9c)
- ref: v3.13.0a2

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9036773450)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e.json)

### vs. 3.10.4

- Geometric mean: 1.09x faster (HPT: reliability of 100.00%, 1.14x faster at 99th %ile)
- Memory usage: 0.65x
- missing benchmarks: dask, djangocms, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.10.4.md)
- [📈time plot](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.18x slower (HPT: reliability of 100.00%, 1.06x slower at 99th %ile)
- Memory usage: 0.56x
- missing benchmarks: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.12.0.md)
- [📈time plot](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.23x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 0.57x
- missing benchmarks: bpe_tokeniser, dask, djangocms
- [📄table](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0b2.md)
- [📈time plot](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.21x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: 0.61x
- missing benchmarks: 🔴 djangocms
- [🧠memory plot](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-base-mem.svg)
- [📄table](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-base.md)
- [📈time plot](bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e-vs-base.svg)

