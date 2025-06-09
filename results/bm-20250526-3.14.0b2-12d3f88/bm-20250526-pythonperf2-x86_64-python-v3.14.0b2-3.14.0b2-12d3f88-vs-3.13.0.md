# Results vs. 3.13.0

- fork: python
- ref: v3.14.0b2
- machine: linux-x86_64
- commit hash: 12d3f88
- commit date: 2025-05-26
- overall geometric mean: 1.061x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 284 ms: 1.03x faster                                             |
| docutils       | 2.83 sec                                                     | 2.90 sec: 1.03x slower                                           |
| html5lib       | 73.5 ms                                                      | 66.8 ms: 1.10x faster                                            |
| Geometric mean | (ref)                                                        | 1.03x faster                                                     |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 335 ms: 1.39x faster                                             |
| async_tree_memoization     | 453 ms                                                       | 332 ms: 1.37x faster                                             |
| async_tree_io              | 843 ms                                                       | 626 ms: 1.35x faster                                             |
| async_tree_none            | 376 ms                                                       | 286 ms: 1.31x faster                                             |
| async_tree_io_tg           | 831 ms                                                       | 650 ms: 1.28x faster                                             |
| async_tree_none_tg         | 346 ms                                                       | 273 ms: 1.27x faster                                             |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 506 ms: 1.19x faster                                             |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 508 ms: 1.14x faster                                             |
| async_generators           | 457 ms                                                       | 433 ms: 1.05x faster                                             |
| asyncio_websockets         | 388 ms                                                       | 382 ms: 1.01x faster                                             |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                            |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 69.0 ms: 1.18x faster                                            |
| pidigits       | 252 ms                                                       | 257 ms: 1.02x slower                                             |
| nbody          | 89.3 ms                                                      | 94.6 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                        | 1.03x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 24.3 ms: 1.08x faster                                            |
| regex_compile  | 143 ms                                                       | 133 ms: 1.07x faster                                             |
| regex_effbot   | 3.67 ms                                                      | 3.46 ms: 1.06x faster                                            |
| regex_dna      | 247 ms                                                       | 235 ms: 1.05x faster                                             |
| Geometric mean | (ref)                                                        | 1.06x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.08 sec: 1.19x faster                                           |
| xml_etree_parse      | 150 ms                                                       | 138 ms: 1.09x faster                                             |
| xml_etree_iterparse  | 103 ms                                                       | 96.9 ms: 1.06x faster                                            |
| xml_etree_process    | 61.2 ms                                                      | 59.3 ms: 1.03x faster                                            |
| unpickle_pure_python | 217 us                                                       | 211 us: 1.03x faster                                             |
| json_dumps           | 11.1 ms                                                      | 11.4 ms: 1.02x slower                                            |
| pickle_pure_python   | 323 us                                                       | 333 us: 1.03x slower                                             |
| json_loads           | 24.7 us                                                      | 27.1 us: 1.10x slower                                            |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                     |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 8.79 ms: 1.02x faster                                            |
| python_startup         | 15.9 ms                                                      | 16.3 ms: 1.02x slower                                            |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.5 ms: 1.11x faster                                            |
| genshi_xml      | 57.1 ms                                                      | 53.8 ms: 1.06x faster                                            |
| django_template | 36.4 ms                                                      | 36.0 ms: 1.01x faster                                            |
| mako            | 10.4 ms                                                      | 10.8 ms: 1.04x slower                                            |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.31 sec: 1.94x faster                                           |
| deepcopy                   | 392 us                                                       | 278 us: 1.41x faster                                             |
| async_tree_memoization_tg  | 466 ms                                                       | 335 ms: 1.39x faster                                             |
| deepcopy_memo              | 38.6 us                                                      | 27.9 us: 1.39x faster                                            |
| async_tree_memoization     | 453 ms                                                       | 332 ms: 1.37x faster                                             |
| async_tree_io              | 843 ms                                                       | 626 ms: 1.35x faster                                             |
| go                         | 162 ms                                                       | 123 ms: 1.31x faster                                             |
| async_tree_none            | 376 ms                                                       | 286 ms: 1.31x faster                                             |
| async_tree_io_tg           | 831 ms                                                       | 650 ms: 1.28x faster                                             |
| async_tree_none_tg         | 346 ms                                                       | 273 ms: 1.27x faster                                             |
| deepcopy_reduce            | 3.54 us                                                      | 2.96 us: 1.20x faster                                            |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 506 ms: 1.19x faster                                             |
| tomli_loads                | 2.46 sec                                                     | 2.08 sec: 1.19x faster                                           |
| pyflate                    | 503 ms                                                       | 426 ms: 1.18x faster                                             |
| float                      | 81.3 ms                                                      | 69.0 ms: 1.18x faster                                            |
| richards                   | 52.9 ms                                                      | 44.9 ms: 1.18x faster                                            |
| generators                 | 33.6 ms                                                      | 28.9 ms: 1.17x faster                                            |
| richards_super             | 59.6 ms                                                      | 51.2 ms: 1.16x faster                                            |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 508 ms: 1.14x faster                                             |
| scimark_sor                | 123 ms                                                       | 108 ms: 1.14x faster                                             |
| telco                      | 8.79 ms                                                      | 7.84 ms: 1.12x faster                                            |
| genshi_text                | 26.2 ms                                                      | 23.5 ms: 1.11x faster                                            |
| dulwich_log                | 68.2 ms                                                      | 61.9 ms: 1.10x faster                                            |
| html5lib                   | 73.5 ms                                                      | 66.8 ms: 1.10x faster                                            |
| hexiom                     | 6.55 ms                                                      | 5.97 ms: 1.10x faster                                            |
| pprint_pformat             | 1.72 sec                                                     | 1.57 sec: 1.10x faster                                           |
| deltablue                  | 3.42 ms                                                      | 3.12 ms: 1.10x faster                                            |
| xml_etree_parse            | 150 ms                                                       | 138 ms: 1.09x faster                                             |
| bpe_tokeniser              | 5.09 sec                                                     | 4.68 sec: 1.09x faster                                           |
| pprint_safe_repr           | 843 ms                                                       | 775 ms: 1.09x faster                                             |
| regex_v8                   | 26.1 ms                                                      | 24.3 ms: 1.08x faster                                            |
| regex_compile              | 143 ms                                                       | 133 ms: 1.07x faster                                             |
| scimark_fft                | 328 ms                                                       | 308 ms: 1.06x faster                                             |
| pylint                     | 347 ms                                                       | 326 ms: 1.06x faster                                             |
| sympy_integrate            | 23.6 ms                                                      | 22.2 ms: 1.06x faster                                            |
| xml_etree_iterparse        | 103 ms                                                       | 96.9 ms: 1.06x faster                                            |
| scimark_monte_carlo        | 66.1 ms                                                      | 62.4 ms: 1.06x faster                                            |
| genshi_xml                 | 57.1 ms                                                      | 53.8 ms: 1.06x faster                                            |
| regex_effbot               | 3.67 ms                                                      | 3.46 ms: 1.06x faster                                            |
| async_generators           | 457 ms                                                       | 433 ms: 1.05x faster                                             |
| regex_dna                  | 247 ms                                                       | 235 ms: 1.05x faster                                             |
| spectral_norm              | 97.0 ms                                                      | 92.7 ms: 1.05x faster                                            |
| meteor_contest             | 130 ms                                                       | 124 ms: 1.04x faster                                             |
| 2to3                       | 293 ms                                                       | 284 ms: 1.03x faster                                             |
| xml_etree_process          | 61.2 ms                                                      | 59.3 ms: 1.03x faster                                            |
| unpickle_pure_python       | 217 us                                                       | 211 us: 1.03x faster                                             |
| sympy_str                  | 298 ms                                                       | 290 ms: 1.03x faster                                             |
| pathlib                    | 17.5 ms                                                      | 17.1 ms: 1.03x faster                                            |
| sympy_expand               | 509 ms                                                       | 496 ms: 1.03x faster                                             |
| connected_components       | 432 ms                                                       | 422 ms: 1.03x faster                                             |
| sympy_sum                  | 155 ms                                                       | 151 ms: 1.02x faster                                             |
| json                       | 5.69 ms                                                      | 5.57 ms: 1.02x faster                                            |
| scimark_lu                 | 98.7 ms                                                      | 96.7 ms: 1.02x faster                                            |
| python_startup_no_site     | 8.96 ms                                                      | 8.79 ms: 1.02x faster                                            |
| shortest_path              | 460 ms                                                       | 452 ms: 1.02x faster                                             |
| k_core                     | 2.17 sec                                                     | 2.13 sec: 1.02x faster                                           |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.70 ms: 1.02x faster                                            |
| asyncio_websockets         | 388 ms                                                       | 382 ms: 1.01x faster                                             |
| pycparser                  | 1.24 sec                                                     | 1.23 sec: 1.01x faster                                           |
| django_template            | 36.4 ms                                                      | 36.0 ms: 1.01x faster                                            |
| nqueens                    | 90.7 ms                                                      | 92.0 ms: 1.01x slower                                            |
| sqlalchemy_declarative     | 148 ms                                                       | 151 ms: 1.01x slower                                             |
| fannkuch                   | 363 ms                                                       | 369 ms: 1.02x slower                                             |
| comprehensions             | 17.0 us                                                      | 17.3 us: 1.02x slower                                            |
| pidigits                   | 252 ms                                                       | 257 ms: 1.02x slower                                             |
| python_startup             | 15.9 ms                                                      | 16.3 ms: 1.02x slower                                            |
| json_dumps                 | 11.1 ms                                                      | 11.4 ms: 1.02x slower                                            |
| docutils                   | 2.83 sec                                                     | 2.90 sec: 1.03x slower                                           |
| pickle_pure_python         | 323 us                                                       | 333 us: 1.03x slower                                             |
| logging_simple             | 6.39 us                                                      | 6.61 us: 1.03x slower                                            |
| sqlalchemy_imperative      | 18.3 ms                                                      | 19.0 ms: 1.04x slower                                            |
| mako                       | 10.4 ms                                                      | 10.8 ms: 1.04x slower                                            |
| raytrace                   | 273 ms                                                       | 285 ms: 1.05x slower                                             |
| create_gc_cycles           | 2.68 ms                                                      | 2.81 ms: 1.05x slower                                            |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                            |
| typing_runtime_protocols   | 169 us                                                       | 178 us: 1.05x slower                                             |
| nbody                      | 89.3 ms                                                      | 94.6 ms: 1.06x slower                                            |
| logging_format             | 6.94 us                                                      | 7.41 us: 1.07x slower                                            |
| crypto_pyaes               | 73.3 ms                                                      | 78.3 ms: 1.07x slower                                            |
| coverage                   | 80.0 ms                                                      | 85.6 ms: 1.07x slower                                            |
| json_loads                 | 24.7 us                                                      | 27.1 us: 1.10x slower                                            |
| many_optionals             | 930 us                                                       | 1.05 ms: 1.13x slower                                            |
| gc_traversal               | 4.74 ms                                                      | 6.21 ms: 1.31x slower                                            |
| subparsers                 | 17.5 ms                                                      | 25.4 ms: 1.45x slower                                            |
| logging_silent             | 97.9 ns                                                      | 518 ns: 5.29x slower                                             |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                     |

Benchmark hidden because not significant (4): sphinx, xml_etree_generate, chaos, sqlite_synth
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250526-3.14.0b2-12d3f88/bm-20250526-pythonperf2-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.061x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.06x