# Results vs. base

- fork: python
- ref: v3.13.0a2
- machine: darwin-arm64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| 2to3           | 192 ms                                                                                               | 179 ms: 1.07x faster                                                                                             |
| chameleon      | 4.73 ms                                                                                              | 4.93 ms: 1.04x slower                                                                                            |
| docutils       | 1.46 sec                                                                                             | 1.51 sec: 1.04x slower                                                                                           |
| Geometric mean | (ref)                                                                                                | 1.02x faster                                                                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 522 ms                                                                                               | 532 ms: 1.02x slower                                                                                             |
| async_tree_cpu_io_mixed_tg | 539 ms                                                                                               | 549 ms: 1.02x slower                                                                                             |
| async_tree_io_tg           | 690 ms                                                                                               | 703 ms: 1.02x slower                                                                                             |
| async_tree_io              | 706 ms                                                                                               | 719 ms: 1.02x slower                                                                                             |
| async_tree_memoization     | 331 ms                                                                                               | 339 ms: 1.02x slower                                                                                             |
| async_tree_none            | 255 ms                                                                                               | 263 ms: 1.03x slower                                                                                             |
| async_tree_none_tg         | 267 ms                                                                                               | 277 ms: 1.04x slower                                                                                             |
| async_tree_memoization_tg  | 332 ms                                                                                               | 346 ms: 1.04x slower                                                                                             |
| Geometric mean             | (ref)                                                                                                | 1.03x slower                                                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| pidigits       | 283 ms                                                                                               | 284 ms: 1.00x slower                                                                                             |
| float          | 56.4 ms                                                                                              | 68.2 ms: 1.21x slower                                                                                            |
| nbody          | 70.8 ms                                                                                              | 86.3 ms: 1.22x slower                                                                                            |
| Geometric mean | (ref)                                                                                                | 1.14x slower                                                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 2.57 ms                                                                                              | 2.56 ms: 1.00x faster                                                                                            |
| regex_v8       | 17.1 ms                                                                                              | 17.4 ms: 1.02x slower                                                                                            |
| regex_dna      | 152 ms                                                                                               | 155 ms: 1.02x slower                                                                                             |
| regex_compile  | 74.9 ms                                                                                              | 85.5 ms: 1.14x slower                                                                                            |
| Geometric mean | (ref)                                                                                                | 1.04x slower                                                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| pickle_list          | 2.98 us                                                                                              | 2.93 us: 1.01x faster                                                                                            |
| unpickle             | 9.10 us                                                                                              | 8.99 us: 1.01x faster                                                                                            |
| json_loads           | 17.2 us                                                                                              | 17.1 us: 1.01x faster                                                                                            |
| pickle               | 7.39 us                                                                                              | 7.36 us: 1.00x faster                                                                                            |
| pickle_pure_python   | 198 us                                                                                               | 201 us: 1.01x slower                                                                                             |
| xml_etree_process    | 39.5 ms                                                                                              | 41.2 ms: 1.04x slower                                                                                            |
| xml_etree_generate   | 56.2 ms                                                                                              | 59.6 ms: 1.06x slower                                                                                            |
| xml_etree_parse      | 99.9 ms                                                                                              | 107 ms: 1.07x slower                                                                                             |
| unpickle_pure_python | 155 us                                                                                               | 168 us: 1.08x slower                                                                                             |
| tomli_loads          | 1.53 sec                                                                                             | 1.67 sec: 1.09x slower                                                                                           |
| xml_etree_iterparse  | 71.3 ms                                                                                              | 81.1 ms: 1.14x slower                                                                                            |
| Geometric mean       | (ref)                                                                                                | 1.03x slower                                                                                                     |

Benchmark hidden because not significant (3): json_dumps, unpickle_list, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                                                              | 12.7 ms: 1.10x faster                                                                                            |
| python_startup_no_site | 12.4 ms                                                                                              | 11.4 ms: 1.09x faster                                                                                            |
| Geometric mean         | (ref)                                                                                                | 1.09x faster                                                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|-----------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| mako      | 7.39 ms                                                                                              | 9.60 ms: 1.30x slower                                                                                            |

All benchmarks:
===============

| Benchmark                  | results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json | results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json |
|----------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| python_startup             | 13.9 ms                                                                                              | 12.7 ms: 1.10x faster                                                                                            |
| python_startup_no_site     | 12.4 ms                                                                                              | 11.4 ms: 1.09x faster                                                                                            |
| 2to3                       | 192 ms                                                                                               | 179 ms: 1.07x faster                                                                                             |
| pickle_list                | 2.98 us                                                                                              | 2.93 us: 1.01x faster                                                                                            |
| unpickle                   | 9.10 us                                                                                              | 8.99 us: 1.01x faster                                                                                            |
| richards                   | 33.9 ms                                                                                              | 33.6 ms: 1.01x faster                                                                                            |
| richards_super             | 38.0 ms                                                                                              | 37.7 ms: 1.01x faster                                                                                            |
| json_loads                 | 17.2 us                                                                                              | 17.1 us: 1.01x faster                                                                                            |
| pickle                     | 7.39 us                                                                                              | 7.36 us: 1.00x faster                                                                                            |
| generators                 | 28.0 ms                                                                                              | 28.0 ms: 1.00x faster                                                                                            |
| regex_effbot               | 2.57 ms                                                                                              | 2.56 ms: 1.00x faster                                                                                            |
| pidigits                   | 283 ms                                                                                               | 284 ms: 1.00x slower                                                                                             |
| gc_traversal               | 2.40 ms                                                                                              | 2.40 ms: 1.00x slower                                                                                            |
| json                       | 2.97 ms                                                                                              | 2.99 ms: 1.01x slower                                                                                            |
| pickle_pure_python         | 198 us                                                                                               | 201 us: 1.01x slower                                                                                             |
| logging_format             | 3.84 us                                                                                              | 3.90 us: 1.01x slower                                                                                            |
| logging_simple             | 3.54 us                                                                                              | 3.60 us: 1.02x slower                                                                                            |
| pycparser                  | 694 ms                                                                                               | 706 ms: 1.02x slower                                                                                             |
| deepcopy_reduce            | 1.92 us                                                                                              | 1.95 us: 1.02x slower                                                                                            |
| async_tree_cpu_io_mixed    | 522 ms                                                                                               | 532 ms: 1.02x slower                                                                                             |
| async_tree_cpu_io_mixed_tg | 539 ms                                                                                               | 549 ms: 1.02x slower                                                                                             |
| coverage                   | 47.1 ms                                                                                              | 47.9 ms: 1.02x slower                                                                                            |
| async_tree_io_tg           | 690 ms                                                                                               | 703 ms: 1.02x slower                                                                                             |
| async_tree_io              | 706 ms                                                                                               | 719 ms: 1.02x slower                                                                                             |
| regex_v8                   | 17.1 ms                                                                                              | 17.4 ms: 1.02x slower                                                                                            |
| telco                      | 4.54 ms                                                                                              | 4.63 ms: 1.02x slower                                                                                            |
| async_generators           | 294 ms                                                                                               | 301 ms: 1.02x slower                                                                                             |
| scimark_sor                | 104 ms                                                                                               | 106 ms: 1.02x slower                                                                                             |
| regex_dna                  | 152 ms                                                                                               | 155 ms: 1.02x slower                                                                                             |
| async_tree_memoization     | 331 ms                                                                                               | 339 ms: 1.02x slower                                                                                             |
| dulwich_log                | 29.2 ms                                                                                              | 30.1 ms: 1.03x slower                                                                                            |
| deepcopy                   | 218 us                                                                                               | 224 us: 1.03x slower                                                                                             |
| logging_silent             | 69.9 ns                                                                                              | 72.1 ns: 1.03x slower                                                                                            |
| async_tree_none            | 255 ms                                                                                               | 263 ms: 1.03x slower                                                                                             |
| pathlib                    | 24.4 ms                                                                                              | 25.3 ms: 1.03x slower                                                                                            |
| docutils                   | 1.46 sec                                                                                             | 1.51 sec: 1.04x slower                                                                                           |
| sqlite_synth               | 1.58 us                                                                                              | 1.64 us: 1.04x slower                                                                                            |
| async_tree_none_tg         | 267 ms                                                                                               | 277 ms: 1.04x slower                                                                                             |
| sqlglot_parse              | 807 us                                                                                               | 838 us: 1.04x slower                                                                                             |
| sqlglot_transpile          | 980 us                                                                                               | 1.02 ms: 1.04x slower                                                                                            |
| sympy_expand               | 234 ms                                                                                               | 243 ms: 1.04x slower                                                                                             |
| chameleon                  | 4.73 ms                                                                                              | 4.93 ms: 1.04x slower                                                                                            |
| xml_etree_process          | 39.5 ms                                                                                              | 41.2 ms: 1.04x slower                                                                                            |
| async_tree_memoization_tg  | 332 ms                                                                                               | 346 ms: 1.04x slower                                                                                             |
| scimark_lu                 | 72.7 ms                                                                                              | 76.1 ms: 1.05x slower                                                                                            |
| typing_runtime_protocols   | 73.6 us                                                                                              | 77.1 us: 1.05x slower                                                                                            |
| mdp                        | 1.56 sec                                                                                             | 1.63 sec: 1.05x slower                                                                                           |
| bench_thread_pool          | 493 us                                                                                               | 523 us: 1.06x slower                                                                                             |
| xml_etree_generate         | 56.2 ms                                                                                              | 59.6 ms: 1.06x slower                                                                                            |
| sqlglot_normalize          | 179 ms                                                                                               | 191 ms: 1.06x slower                                                                                             |
| go                         | 105 ms                                                                                               | 112 ms: 1.06x slower                                                                                             |
| xml_etree_parse            | 99.9 ms                                                                                              | 107 ms: 1.07x slower                                                                                             |
| sqlglot_optimize           | 33.3 ms                                                                                              | 35.9 ms: 1.08x slower                                                                                            |
| deepcopy_memo              | 24.8 us                                                                                              | 26.7 us: 1.08x slower                                                                                            |
| meteor_contest             | 73.0 ms                                                                                              | 78.7 ms: 1.08x slower                                                                                            |
| unpickle_pure_python       | 155 us                                                                                               | 168 us: 1.08x slower                                                                                             |
| tomli_loads                | 1.53 sec                                                                                             | 1.67 sec: 1.09x slower                                                                                           |
| raytrace                   | 178 ms                                                                                               | 195 ms: 1.09x slower                                                                                             |
| sympy_str                  | 137 ms                                                                                               | 149 ms: 1.09x slower                                                                                             |
| pyflate                    | 335 ms                                                                                               | 369 ms: 1.10x slower                                                                                             |
| sympy_integrate            | 10.6 ms                                                                                              | 11.7 ms: 1.10x slower                                                                                            |
| sympy_sum                  | 72.0 ms                                                                                              | 80.2 ms: 1.12x slower                                                                                            |
| pprint_safe_repr           | 496 ms                                                                                               | 561 ms: 1.13x slower                                                                                             |
| crypto_pyaes               | 48.0 ms                                                                                              | 54.5 ms: 1.14x slower                                                                                            |
| xml_etree_iterparse        | 71.3 ms                                                                                              | 81.1 ms: 1.14x slower                                                                                            |
| regex_compile              | 74.9 ms                                                                                              | 85.5 ms: 1.14x slower                                                                                            |
| pprint_pformat             | 1.01 sec                                                                                             | 1.15 sec: 1.14x slower                                                                                           |
| chaos                      | 41.2 ms                                                                                              | 47.5 ms: 1.15x slower                                                                                            |
| nqueens                    | 58.4 ms                                                                                              | 69.7 ms: 1.19x slower                                                                                            |
| fannkuch                   | 270 ms                                                                                               | 324 ms: 1.20x slower                                                                                             |
| float                      | 56.4 ms                                                                                              | 68.2 ms: 1.21x slower                                                                                            |
| nbody                      | 70.8 ms                                                                                              | 86.3 ms: 1.22x slower                                                                                            |
| scimark_fft                | 200 ms                                                                                               | 246 ms: 1.23x slower                                                                                             |
| scimark_monte_carlo        | 46.6 ms                                                                                              | 57.9 ms: 1.24x slower                                                                                            |
| hexiom                     | 4.77 ms                                                                                              | 6.21 ms: 1.30x slower                                                                                            |
| mako                       | 7.39 ms                                                                                              | 9.60 ms: 1.30x slower                                                                                            |
| scimark_sparse_mat_mult    | 3.08 ms                                                                                              | 4.04 ms: 1.31x slower                                                                                            |
| comprehensions             | 11.4 us                                                                                              | 15.7 us: 1.38x slower                                                                                            |
| spectral_norm              | 74.0 ms                                                                                              | 102 ms: 1.38x slower                                                                                             |
| deltablue                  | 2.44 ms                                                                                              | 3.59 ms: 1.48x slower                                                                                            |
| Geometric mean             | (ref)                                                                                                | 1.06x slower                                                                                                     |

Benchmark hidden because not significant (11): mypy2, tornado_http, asyncio_tcp_ssl, coroutines, asyncio_tcp, json_dumps, asyncio_websockets, create_gc_cycles, unpickle_list, pickle_dict, bench_mp_pool
Ignored benchmarks (17) of results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json: aiohttp, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
Ignored benchmarks (2) of results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json: dask, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.00x