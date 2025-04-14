# Results vs. 3.13.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: d270553
- commit date: 2025-02-20
- overall geometric mean: 1.050x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 287 ms: 1.02x faster                                                            |
| docutils       | 2.83 sec                                                     | 2.88 sec: 1.02x slower                                                          |
| html5lib       | 73.5 ms                                                      | 68.4 ms: 1.07x faster                                                           |
| sphinx         | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                          |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 338 ms: 1.38x faster                                                            |
| async_tree_io              | 843 ms                                                       | 651 ms: 1.30x faster                                                            |
| async_tree_none            | 376 ms                                                       | 292 ms: 1.29x faster                                                            |
| async_tree_memoization     | 453 ms                                                       | 354 ms: 1.28x faster                                                            |
| async_tree_io_tg           | 831 ms                                                       | 655 ms: 1.27x faster                                                            |
| async_tree_none_tg         | 346 ms                                                       | 279 ms: 1.24x faster                                                            |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 522 ms: 1.16x faster                                                            |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 508 ms: 1.15x faster                                                            |
| async_generators           | 457 ms                                                       | 419 ms: 1.09x faster                                                            |
| coroutines                 | 21.6 ms                                                      | 20.7 ms: 1.04x faster                                                           |
| Geometric mean             | (ref)                                                        | 1.19x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 69.9 ms: 1.16x faster                                                           |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                            |
| nbody          | 89.3 ms                                                      | 101 ms: 1.14x slower                                                            |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.29 ms: 1.11x faster                                                           |
| regex_compile  | 143 ms                                                       | 132 ms: 1.08x faster                                                            |
| regex_dna      | 247 ms                                                       | 250 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.14 sec: 1.15x faster                                                          |
| xml_etree_parse      | 150 ms                                                       | 139 ms: 1.08x faster                                                            |
| xml_etree_iterparse  | 103 ms                                                       | 97.9 ms: 1.05x faster                                                           |
| xml_etree_process    | 61.2 ms                                                      | 59.2 ms: 1.03x faster                                                           |
| unpickle_pure_python | 217 us                                                       | 211 us: 1.03x faster                                                            |
| xml_etree_generate   | 86.5 ms                                                      | 84.4 ms: 1.02x faster                                                           |
| pickle_pure_python   | 323 us                                                       | 333 us: 1.03x slower                                                            |
| json_dumps           | 11.1 ms                                                      | 11.7 ms: 1.05x slower                                                           |
| json_loads           | 24.7 us                                                      | 26.1 us: 1.06x slower                                                           |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.04 ms: 1.01x slower                                                           |
| python_startup         | 15.9 ms                                                      | 16.2 ms: 1.02x slower                                                           |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 24.2 ms: 1.08x faster                                                           |
| genshi_xml      | 57.1 ms                                                      | 55.7 ms: 1.02x faster                                                           |
| django_template | 36.4 ms                                                      | 36.7 ms: 1.01x slower                                                           |
| mako            | 10.4 ms                                                      | 10.9 ms: 1.05x slower                                                           |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250220-pythonperf2-x86_64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 392 us                                                       | 280 us: 1.40x faster                                                            |
| async_tree_memoization_tg  | 466 ms                                                       | 338 ms: 1.38x faster                                                            |
| deepcopy_memo              | 38.6 us                                                      | 28.6 us: 1.35x faster                                                           |
| async_tree_io              | 843 ms                                                       | 651 ms: 1.30x faster                                                            |
| async_tree_none            | 376 ms                                                       | 292 ms: 1.29x faster                                                            |
| async_tree_memoization     | 453 ms                                                       | 354 ms: 1.28x faster                                                            |
| async_tree_io_tg           | 831 ms                                                       | 655 ms: 1.27x faster                                                            |
| go                         | 162 ms                                                       | 130 ms: 1.25x faster                                                            |
| async_tree_none_tg         | 346 ms                                                       | 279 ms: 1.24x faster                                                            |
| deepcopy_reduce            | 3.54 us                                                      | 2.93 us: 1.21x faster                                                           |
| generators                 | 33.6 ms                                                      | 28.6 ms: 1.18x faster                                                           |
| float                      | 81.3 ms                                                      | 69.9 ms: 1.16x faster                                                           |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 522 ms: 1.16x faster                                                            |
| richards                   | 52.9 ms                                                      | 45.9 ms: 1.15x faster                                                           |
| tomli_loads                | 2.46 sec                                                     | 2.14 sec: 1.15x faster                                                          |
| richards_super             | 59.6 ms                                                      | 51.9 ms: 1.15x faster                                                           |
| scimark_sor                | 123 ms                                                       | 108 ms: 1.15x faster                                                            |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 508 ms: 1.15x faster                                                            |
| spectral_norm              | 97.0 ms                                                      | 84.8 ms: 1.14x faster                                                           |
| pyflate                    | 503 ms                                                       | 451 ms: 1.12x faster                                                            |
| regex_effbot               | 3.67 ms                                                      | 3.29 ms: 1.11x faster                                                           |
| pylint                     | 347 ms                                                       | 315 ms: 1.10x faster                                                            |
| hexiom                     | 6.55 ms                                                      | 6.00 ms: 1.09x faster                                                           |
| async_generators           | 457 ms                                                       | 419 ms: 1.09x faster                                                            |
| bpe_tokeniser              | 5.09 sec                                                     | 4.68 sec: 1.09x faster                                                          |
| xml_etree_parse            | 150 ms                                                       | 139 ms: 1.08x faster                                                            |
| genshi_text                | 26.2 ms                                                      | 24.2 ms: 1.08x faster                                                           |
| regex_compile              | 143 ms                                                       | 132 ms: 1.08x faster                                                            |
| telco                      | 8.79 ms                                                      | 8.17 ms: 1.08x faster                                                           |
| html5lib                   | 73.5 ms                                                      | 68.4 ms: 1.07x faster                                                           |
| pprint_safe_repr           | 843 ms                                                       | 790 ms: 1.07x faster                                                            |
| pprint_pformat             | 1.72 sec                                                     | 1.61 sec: 1.06x faster                                                          |
| sqlglot_normalize          | 119 ms                                                       | 112 ms: 1.06x faster                                                            |
| sqlglot_optimize           | 59.3 ms                                                      | 56.1 ms: 1.06x faster                                                           |
| scimark_fft                | 328 ms                                                       | 311 ms: 1.05x faster                                                            |
| xml_etree_iterparse        | 103 ms                                                       | 97.9 ms: 1.05x faster                                                           |
| thrift                     | 901 us                                                       | 860 us: 1.05x faster                                                            |
| json                       | 5.69 ms                                                      | 5.44 ms: 1.05x faster                                                           |
| sqlglot_parse              | 1.40 ms                                                      | 1.34 ms: 1.04x faster                                                           |
| coroutines                 | 21.6 ms                                                      | 20.7 ms: 1.04x faster                                                           |
| scimark_monte_carlo        | 66.1 ms                                                      | 63.6 ms: 1.04x faster                                                           |
| connected_components       | 432 ms                                                       | 416 ms: 1.04x faster                                                            |
| k_core                     | 2.17 sec                                                     | 2.09 sec: 1.04x faster                                                          |
| sympy_expand               | 509 ms                                                       | 491 ms: 1.04x faster                                                            |
| sqlglot_transpile          | 1.79 ms                                                      | 1.73 ms: 1.04x faster                                                           |
| shortest_path              | 460 ms                                                       | 445 ms: 1.03x faster                                                            |
| logging_silent             | 97.9 ns                                                      | 94.6 ns: 1.03x faster                                                           |
| xml_etree_process          | 61.2 ms                                                      | 59.2 ms: 1.03x faster                                                           |
| sqlalchemy_declarative     | 148 ms                                                       | 144 ms: 1.03x faster                                                            |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.7 ms: 1.03x faster                                                           |
| unpickle_pure_python       | 217 us                                                       | 211 us: 1.03x faster                                                            |
| sympy_str                  | 298 ms                                                       | 289 ms: 1.03x faster                                                            |
| sqlite_synth               | 2.91 us                                                      | 2.82 us: 1.03x faster                                                           |
| pathlib                    | 17.5 ms                                                      | 17.0 ms: 1.03x faster                                                           |
| mdp                        | 2.54 sec                                                     | 2.47 sec: 1.03x faster                                                          |
| sympy_sum                  | 155 ms                                                       | 151 ms: 1.03x faster                                                            |
| genshi_xml                 | 57.1 ms                                                      | 55.7 ms: 1.02x faster                                                           |
| xml_etree_generate         | 86.5 ms                                                      | 84.4 ms: 1.02x faster                                                           |
| meteor_contest             | 130 ms                                                       | 127 ms: 1.02x faster                                                            |
| sympy_integrate            | 23.6 ms                                                      | 23.0 ms: 1.02x faster                                                           |
| scimark_lu                 | 98.7 ms                                                      | 96.4 ms: 1.02x faster                                                           |
| deltablue                  | 3.42 ms                                                      | 3.34 ms: 1.02x faster                                                           |
| dulwich_log                | 68.2 ms                                                      | 66.8 ms: 1.02x faster                                                           |
| 2to3                       | 293 ms                                                       | 287 ms: 1.02x faster                                                            |
| sphinx                     | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                          |
| coverage                   | 80.0 ms                                                      | 79.6 ms: 1.00x faster                                                           |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                            |
| python_startup_no_site     | 8.96 ms                                                      | 9.04 ms: 1.01x slower                                                           |
| pycparser                  | 1.24 sec                                                     | 1.25 sec: 1.01x slower                                                          |
| django_template            | 36.4 ms                                                      | 36.7 ms: 1.01x slower                                                           |
| logging_format             | 6.94 us                                                      | 7.02 us: 1.01x slower                                                           |
| regex_dna                  | 247 ms                                                       | 250 ms: 1.01x slower                                                            |
| python_startup             | 15.9 ms                                                      | 16.2 ms: 1.02x slower                                                           |
| fannkuch                   | 363 ms                                                       | 370 ms: 1.02x slower                                                            |
| docutils                   | 2.83 sec                                                     | 2.88 sec: 1.02x slower                                                          |
| comprehensions             | 17.0 us                                                      | 17.5 us: 1.03x slower                                                           |
| pickle_pure_python         | 323 us                                                       | 333 us: 1.03x slower                                                            |
| raytrace                   | 273 ms                                                       | 282 ms: 1.03x slower                                                            |
| typing_runtime_protocols   | 169 us                                                       | 175 us: 1.04x slower                                                            |
| chaos                      | 60.2 ms                                                      | 62.4 ms: 1.04x slower                                                           |
| create_gc_cycles           | 2.68 ms                                                      | 2.79 ms: 1.04x slower                                                           |
| json_dumps                 | 11.1 ms                                                      | 11.7 ms: 1.05x slower                                                           |
| mako                       | 10.4 ms                                                      | 10.9 ms: 1.05x slower                                                           |
| json_loads                 | 24.7 us                                                      | 26.1 us: 1.06x slower                                                           |
| many_optionals             | 930 us                                                       | 1.00 ms: 1.08x slower                                                           |
| crypto_pyaes               | 73.3 ms                                                      | 79.3 ms: 1.08x slower                                                           |
| nbody                      | 89.3 ms                                                      | 101 ms: 1.14x slower                                                            |
| subparsers                 | 17.5 ms                                                      | 23.0 ms: 1.31x slower                                                           |
| gc_traversal               | 4.74 ms                                                      | 6.56 ms: 1.38x slower                                                           |
| bench_mp_pool              | 5.12 ms                                                      | 1.11 sec: 216.81x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                                    |

Benchmark hidden because not significant (6): logging_simple, scimark_sparse_mat_mult, regex_v8, asyncio_websockets, nqueens, bench_thread_pool
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.050x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.02x