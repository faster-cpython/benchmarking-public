# Results

- fork: saulshanabrook
- version: 3.14.0a0
- config: JIT
- commit hash: [9d6171d](https://github.com/saulshanabrook/cpython/commit/9d6171d)
- commit date: 2024-05-29T06:58:58+08:00
- commit merge base: [548a11d5cf1dbb32d86ce0c045130c77f50c1427](https://github.com/saulshanabrook/cpython/commit/548a11d5cf1dbb32d86ce0c045130c77f50c1427)
- ref: optimizer_type_versi

## linux x86_64 (azure)

- [pystats raw](bm-20240529-azure-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d-pystats.json)
- [pystats table](bm-20240529-azure-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d-pystats.md)

### vs. base

- [pystats diff](bm-20240529-azure-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d-pystats-vs-base.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9278899214)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240529-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d.json)

### vs. 3.10.4

- Geometric mean: 1.34x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240529-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d-vs-3.10.4.md)
- [📈time plot](bm-20240529-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x faster (HPT: reliability of 98.47%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240529-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d-vs-3.12.0.md)
- [📈time plot](bm-20240529-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 68.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, bpe_tokeniser, chameleon, djangocms, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240529-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d-vs-3.13.0b2.md)
- [📈time plot](bm-20240529-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 61.22%, 1.00x faster at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240529-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d-vs-base-mem.svg)
- [📄table](bm-20240529-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d-vs-base.md)
- [📈time plot](bm-20240529-linux-x86_64-saulshanabrook-optimizer_type_versi-3.14.0a0-9d6171d-vs-base.svg)

