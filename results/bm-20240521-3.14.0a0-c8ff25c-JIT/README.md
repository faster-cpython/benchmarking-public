# Results

- fork: saulshanabrook
- version: 3.14.0a0
- config: JIT
- commit hash: [c8ff25c](https://github.com/saulshanabrook/cpython/commit/c8ff25c)
- commit date: 2024-05-21T12:40:58-04:00
- commit merge base: [642b25b9a82c368b045709f0b94e7d5a02400ed2](https://github.com/saulshanabrook/cpython/commit/642b25b9a82c368b045709f0b94e7d5a02400ed2)
- ref: optimizer_type_versi

## linux x86_64 (azure)

- [pystats raw](bm-20240521-azure-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c-pystats.json)
- [pystats table](bm-20240521-azure-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c-pystats.md)

### vs. base

- [pystats diff](bm-20240521-azure-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9178235205)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.24x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: aiohttp, djangocms, gunicorn, hexiom, mdp, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c-vs-3.10.4.md)
- [📈time plot](bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 98.42%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, gunicorn, hexiom, mdp, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c-vs-3.12.0.md)
- [📈time plot](bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 75.74%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, bpe_tokeniser, djangocms, gunicorn, hexiom, mdp, mypy2
- [📄table](bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c-vs-3.13.0b2.md)
- [📈time plot](bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 99.97%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: 🔴 hexiom, mdp
- [🧠memory plot](bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c-vs-base-mem.svg)
- [📄table](bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c-vs-base.md)
- [📈time plot](bm-20240521-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-c8ff25c-vs-base.svg)

