# Results

- fork: savannahostrowski
- version: 3.14.0a0
- config: JIT
- commit hash: [7f9fe5a](https://github.com/savannahostrowski/cpython/commit/7f9fe5a)
- commit date: 2024-09-26T14:48:23-07:00
- commit merge base: [54dd77fb8c880d7655fffab934978e277b4275fe](https://github.com/savannahostrowski/cpython/commit/54dd77fb8c880d7655fffab934978e277b4275fe)
- ref: jit_llvm_19

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11061943927)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json)

### vs. 3.10.4

- Geometric mean: 1.19x faster (HPT: reliability of 100.00%, 1.05x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence
- [📄table](bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.10.4.md)
- [📈time plot](bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.00x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, unpack_sequence
- [📄table](bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.12.0.md)
- [📈time plot](bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.07x slower (HPT: reliability of 100.00%, 1.01x slower at 99th %ile)
- Memory usage: 1.09x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.13.0b2.md)
- [📈time plot](bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.01x faster (HPT: reliability of 100.00%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-base-mem.svg)
- [📄table](bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-base.md)
- [📈time plot](bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-base.svg)

## linux x86_64 (linux)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11061943927)
- cpu model: Intel(R) Xeon(R) W-2255 CPU @ 3.70GHz
- platform: Linux-5.4.0-193-generic-x86_64-with-glibc2.31
- [raw results](bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json)

### vs. 3.10.4

- Geometric mean: 1.38x faster (HPT: reliability of 100.00%, 1.27x faster at 99th %ile)
- Memory usage: 1.21x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.10.4.md)
- [📈time plot](bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.07x faster (HPT: reliability of 100.00%, 1.01x faster at 99th %ile)
- Memory usage: 1.05x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.12.0.md)
- [📈time plot](bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.05x faster (HPT: reliability of 99.99%, 1.01x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.13.0b2.md)
- [📈time plot](bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 100.00%, 1.00x slower at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-base-mem.svg)
- [📄table](bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-base.md)
- [📈time plot](bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-base.svg)

## linux x86_64 (pythonperf2)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11061943927)
- cpu model: 12th Gen Intel(R) Core(TM) i9-12900
- platform: Linux-5.15.0-105-generic-x86_64-with-glibc2.35
- [raw results](bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json)

### vs. 3.10.4

- Geometric mean: 1.29x faster (HPT: reliability of 100.00%, 1.20x faster at 99th %ile)
- Memory usage: 1.22x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.10.4.md)
- [📈time plot](bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.01x faster (HPT: reliability of 66.69%, 1.00x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.12.0.md)
- [📈time plot](bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.01x faster (HPT: reliability of 81.57%, 1.00x faster at 99th %ile)
- Memory usage: 1.08x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.13.0b2.md)
- [📈time plot](bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 92.32%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-base-mem.svg)
- [📄table](bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-base.md)
- [📈time plot](bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-base.svg)

## windows amd64 (pythonperf1)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11061943927)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json)

### vs. 3.10.4

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.10x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.10.4.md)
- [📈time plot](bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 71.41%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.12.0.md)
- [📈time plot](bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.02x slower (HPT: reliability of 99.90%, 1.01x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, flaskblogging, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.13.0b2.md)
- [📈time plot](bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 97.25%, 1.00x faster at 99th %ile)
- Memory usage: unknown
- [📄table](bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-base.md)
- [📈time plot](bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-base.svg)

## windows x86 (pythonperf1_win32)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11061943927)
- cpu model: missing
- platform: Windows-11-10.0.22631-SP0
- [raw results](bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json)

### vs. 3.10.4

- Geometric mean: 1.18x faster (HPT: reliability of 100.00%, 1.09x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg
- [📄table](bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.10.4.md)
- [📈time plot](bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.20x faster (HPT: reliability of 100.00%, 1.11x faster at 99th %ile)
- Memory usage: unknown
- missing benchmarks: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.12.0.md)
- [📈time plot](bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.03x faster (HPT: reliability of 98.98%, 1.00x slower at 99th %ile)
- Memory usage: unknown
- missing benchmarks: chameleon, flaskblogging
- new benchmarks: dulwich_log, unpack_sequence
- [📄table](bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.13.0b2.md)
- [📈time plot](bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.13.0b2.svg)

## darwin arm64 (darwin)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/11061943927)
- cpu model: missing
- platform: macOS-14.6.1-arm64-arm-64bit-Mach-O
- [raw results](bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json)

### vs. 3.10.4

- Geometric mean: 1.21x faster (HPT: reliability of 100.00%, 1.13x faster at 99th %ile)
- Memory usage: 0.99x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.10.4.md)
- [📈time plot](bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.03x faster (HPT: reliability of 96.60%, 1.00x faster at 99th %ile)
- Memory usage: 0.89x
- missing benchmarks: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift
- [📄table](bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.12.0.md)
- [📈time plot](bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.04x slower (HPT: reliability of 99.98%, 1.00x slower at 99th %ile)
- Memory usage: 0.93x
- missing benchmarks: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
- new benchmarks: unpack_sequence
- [📄table](bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.13.0b2.md)
- [📈time plot](bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x slower (HPT: reliability of 80.11%, 1.00x slower at 99th %ile)
- Memory usage: 1.01x
- [🧠memory plot](bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-base-mem.svg)
- [📄table](bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-base.md)
- [📈time plot](bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a-vs-base.svg)

