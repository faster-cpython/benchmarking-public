# Results

- fork: diegorusso
- version: 3.14.0a0
- config: JIT
- commit hash: [cebe632](https://github.com/diegorusso/cpython/commit/cebe632)
- commit date: 2024-06-25T17:30:04+01:00
- commit merge base: [42b2c9d78da7ebd6bd5925a4d4c78aec3c9e78e6](https://github.com/diegorusso/cpython/commit/42b2c9d78da7ebd6bd5925a4d4c78aec3c9e78e6)
- ref: gh_119726_trampoline

## linux aarch64 (arminc)

- [GitHub Action run](https://github.com/faster-cpython/benchmarking/actions/runs/9671258814)
- cpu model: missing
- platform: Linux-5.15.0-101-generic-aarch64-with-glibc2.35
- [raw results](bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632.json)

### vs. 3.10.4

- Geometric mean: 1.21x faster (HPT: reliability of 100.00%, 1.08x faster at 99th %ile)
- Memory usage: 1.25x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
- [📄table](bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632-vs-3.10.4.md)
- [📈time plot](bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632-vs-3.10.4.svg)

### vs. 3.12.0

- Geometric mean: 1.05x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.01x
- missing benchmarks: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
- new benchmarks: bpe_tokeniser
- [📄table](bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632-vs-3.12.0.md)
- [📈time plot](bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632-vs-3.12.0.svg)

### vs. 3.13.0b2

- Geometric mean: 1.06x slower (HPT: reliability of 100.00%, 1.02x slower at 99th %ile)
- Memory usage: 1.10x
- missing benchmarks: aiohttp, chameleon, flaskblogging, gunicorn, mypy2
- [📄table](bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632-vs-3.13.0b2.md)
- [📈time plot](bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632-vs-3.13.0b2.svg)

### vs. base

- Geometric mean: 1.00x faster (HPT: reliability of 86.26%, 1.00x faster at 99th %ile)
- Memory usage: 1.00x
- [🧠memory plot](bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632-vs-base-mem.svg)
- [📄table](bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632-vs-base.md)
- [📈time plot](bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632-vs-base.svg)

