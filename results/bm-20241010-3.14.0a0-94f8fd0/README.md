# Results

- fork: faster-cpython
- version: 3.14.0a0
- config: 
- commit hash: [94f8fd0](https://github.com/faster%2dcpython/cpython/commit/94f8fd0)
- commit date: 2024-10-10T12:05:05+01:00
- commit merge base: [99400930ac1d4e5e10a5ae30f8202d8bc2661e39](https://github.com/faster%2dcpython/cpython/commit/99400930ac1d4e5e10a5ae30f8202d8bc2661e39)
- ref: more_robust_immortal

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11273307410)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20241010-pythonperf2-x86_64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0.json)

### vs. 3.10.4

- Geometric mean: 1.25x faster (HPT: reliability of 100.00%, 1.23x faster at 99th %ile)
- Memory usage: 1.12x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241010-pythonperf2-x86_64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-3.10.4.md)
- [📈time plot](bm-20241010-pythonperf2-x86_64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.04x slower (HPT: reliability of 97.23%, 1.00x faster at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241010-pythonperf2-x86_64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-3.12.0.md)
- [📈time plot](bm-20241010-pythonperf2-x86_64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.03x slower (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- [📄table](bm-20241010-pythonperf2-x86_64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-3.13.0.md)
- [📈time plot](bm-20241010-pythonperf2-x86_64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-3.13.0.svg)

### vs. 3.13.0b2

- [📄table](bm-20241010-pythonperf2-x86_64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-3.13.0b2.md)
- [📈time plot](bm-20241010-pythonperf2-x86_64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-3.13.0b2.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11273331780)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20241010-pythonperf1-amd64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0.json)

### vs. 3.10.4

- Geometric mean: 1.15x faster (HPT: reliability of 100.00%, 1.07x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20241010-pythonperf1-amd64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-3.10.4.md)
- [📈time plot](bm-20241010-pythonperf1-amd64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.02x slower (HPT: reliability of 99.36%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241010-pythonperf1-amd64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-3.12.0.md)
- [📈time plot](bm-20241010-pythonperf1-amd64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.07x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2
- [📄table](bm-20241010-pythonperf1-amd64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-3.13.0.md)
- [📈time plot](bm-20241010-pythonperf1-amd64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.02x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20241010-pythonperf1-amd64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-base.md)
- [📈time plot](bm-20241010-pythonperf1-amd64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20241010-pythonperf1-amd64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-3.13.0b2.md)
- [📈time plot](bm-20241010-pythonperf1-amd64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11273317937)
- cpu model: missing
- platform: macOS-15.0.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20241010-darwin-arm64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0.json)

### vs. 3.10.4

- Geometric mean: 1.28x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 0.78x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20241010-darwin-arm64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-3.10.4.md)
- [📈time plot](bm-20241010-darwin-arm64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 0.71x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20241010-darwin-arm64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-3.12.0.md)
- [📈time plot](bm-20241010-darwin-arm64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-3.12.0.svg)

### vs. 3.13.0

- Geometric mean: 1.08x faster (HPT: reliability of 100.00%, 1.04x faster at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- [📄table](bm-20241010-darwin-arm64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-3.13.0.md)
- [📈time plot](bm-20241010-darwin-arm64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-3.13.0.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20241010-darwin-arm64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-base-mem.svg)
- [📄table](bm-20241010-darwin-arm64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-base.md)
- [📈time plot](bm-20241010-darwin-arm64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-base.svg)

### vs. 3.13.0b2

- [📄table](bm-20241010-darwin-arm64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-3.13.0b2.md)
- [📈time plot](bm-20241010-darwin-arm64-faster%252dcpython-more_robust_immortal-3.14.0a0-94f8fd0-vs-3.13.0b2.svg)

