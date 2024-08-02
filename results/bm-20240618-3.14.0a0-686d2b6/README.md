# Results

- fork: encukou
- version: 3.14.0a0
- config: 
- commit hash: [686d2b6](https://github.com/encukou/cpython/commit/686d2b6)
- commit date: 2024-06-18T09:48:30+02:00
- commit merge base: [ac37a806018cc40fafebcd0fa90250c3e0261e0c](https://github.com/encukou/cpython/commit/ac37a806018cc40fafebcd0fa90250c3e0261e0c)
- ref: immortal_interned

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9564946859)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6.json)

### vs. 3.10.4

- Geometric mean: 1.36x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.11x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6-vs-3.10.4.md)
- [📈time plot](bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 0.98x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6-vs-3.12.0.md)
- [📈time plot](bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6-vs-3.13.0b2.md)
- [📈time plot](bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 91.84%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6-vs-base-mem.svg)
- [📄table](bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6-vs-base.md)
- [📈time plot](bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6-vs-base.svg)

