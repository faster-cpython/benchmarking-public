# Results

- fork: python
- version: 3.14.0a0
- config: JIT
- commit hash: [7b0c247](https://github.com/python/cpython/commit/7b0c247)
- commit date: 2024-05-08T12:20:40-06:00
- commit merge base: [c68311df8543384e04fe994b3d4f4718cca1040e](https://github.com/python/cpython/commit/c68311df8543384e04fe994b3d4f4718cca1040e)
- ref: 7b0c247f1c176e092777

## linux x86_64 (azure)

- [pystats raw](bm-20240508-azure-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247-pystats.json)
- [pystats table](bm-20240508-azure-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247-pystats.md)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9007419889)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-164-generic-x86_64-with-glibc2.31
- [raw results](bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.20x
- missing benchmarks: djangocms, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247-vs-3.10.4.md)
- [📈time plot](bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x slower (HPT: reliability of 90.94%, 1.00x faster at 99th %ile)
- Memory usage: 1.06x
- missing benchmarks: mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
- new benchmarks: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247-vs-3.12.0.md)
- [📈time plot](bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x slower (HPT: reliability of 80.31%, 1.00x slower at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: bpe_tokeniser, djangocms, mypy2
- [📄table](bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247-vs-3.13.0b2.md)
- [📈time plot](bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247-vs-3.13.0b2.svg)

