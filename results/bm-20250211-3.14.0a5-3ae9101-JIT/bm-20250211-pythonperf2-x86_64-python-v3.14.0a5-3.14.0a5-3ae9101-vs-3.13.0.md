# Results vs. 3.13.0

- fork: python
- ref: v3.14.0a5
- machine: linux-x86_64
- commit hash: 3ae9101
- commit date: 2025-02-11
- overall geometric mean: 1.045x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 290 ms: 1.01x faster                                             |
| docutils       | 2.83 sec                                                     | 2.94 sec: 1.04x slower                                           |
| html5lib       | 73.5 ms                                                      | 67.3 ms: 1.09x faster                                            |
| sphinx         | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                           |
| Geometric mean | (ref)                                                        | 1.02x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 341 ms: 1.37x faster                                             |
| async_tree_io              | 843 ms                                                       | 650 ms: 1.30x faster                                             |
| async_tree_io_tg           | 831 ms                                                       | 644 ms: 1.29x faster                                             |
| async_tree_none            | 376 ms                                                       | 296 ms: 1.27x faster                                             |
| async_tree_memoization     | 453 ms                                                       | 359 ms: 1.26x faster                                             |
| async_tree_none_tg         | 346 ms                                                       | 282 ms: 1.23x faster                                             |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 526 ms: 1.15x faster                                             |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 514 ms: 1.13x faster                                             |
| async_generators           | 457 ms                                                       | 428 ms: 1.07x faster                                             |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.02x faster                                            |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                             |
| Geometric mean             | (ref)                                                        | 1.18x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 70.2 ms: 1.16x faster                                            |
| pidigits       | 252 ms                                                       | 253 ms: 1.00x slower                                             |
| nbody          | 89.3 ms                                                      | 101 ms: 1.13x slower                                             |
| Geometric mean | (ref)                                                        | 1.01x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.14 ms: 1.17x faster                                            |
| regex_v8       | 26.1 ms                                                      | 24.5 ms: 1.07x faster                                            |
| regex_compile  | 143 ms                                                       | 136 ms: 1.05x faster                                             |
| regex_dna      | 247 ms                                                       | 244 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                        | 1.07x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.05 sec: 1.20x faster                                           |
| xml_etree_parse      | 150 ms                                                       | 136 ms: 1.10x faster                                             |
| xml_etree_generate   | 86.5 ms                                                      | 79.0 ms: 1.10x faster                                            |
| xml_etree_process    | 61.2 ms                                                      | 56.2 ms: 1.09x faster                                            |
| xml_etree_iterparse  | 103 ms                                                       | 95.5 ms: 1.08x faster                                            |
| unpickle_pure_python | 217 us                                                       | 205 us: 1.06x faster                                             |
| pickle_pure_python   | 323 us                                                       | 335 us: 1.04x slower                                             |
| json_dumps           | 11.1 ms                                                      | 11.6 ms: 1.04x slower                                            |
| json_loads           | 24.7 us                                                      | 26.9 us: 1.09x slower                                            |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.00 ms: 1.01x slower                                            |
| python_startup         | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                            |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako           | 10.4 ms                                                      | 9.74 ms: 1.06x faster                                            |
| genshi_text    | 26.2 ms                                                      | 24.8 ms: 1.06x faster                                            |
| genshi_xml     | 57.1 ms                                                      | 55.5 ms: 1.03x faster                                            |
| Geometric mean | (ref)                                                        | 1.04x faster                                                     |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-pythonperf2-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| deepcopy                   | 392 us                                                       | 283 us: 1.39x faster                                             |
| async_tree_memoization_tg  | 466 ms                                                       | 341 ms: 1.37x faster                                             |
| deepcopy_memo              | 38.6 us                                                      | 29.2 us: 1.32x faster                                            |
| async_tree_io              | 843 ms                                                       | 650 ms: 1.30x faster                                             |
| async_tree_io_tg           | 831 ms                                                       | 644 ms: 1.29x faster                                             |
| async_tree_none            | 376 ms                                                       | 296 ms: 1.27x faster                                             |
| async_tree_memoization     | 453 ms                                                       | 359 ms: 1.26x faster                                             |
| async_tree_none_tg         | 346 ms                                                       | 282 ms: 1.23x faster                                             |
| deepcopy_reduce            | 3.54 us                                                      | 2.91 us: 1.22x faster                                            |
| tomli_loads                | 2.46 sec                                                     | 2.05 sec: 1.20x faster                                           |
| pyflate                    | 503 ms                                                       | 428 ms: 1.17x faster                                             |
| regex_effbot               | 3.67 ms                                                      | 3.14 ms: 1.17x faster                                            |
| spectral_norm              | 97.0 ms                                                      | 83.1 ms: 1.17x faster                                            |
| float                      | 81.3 ms                                                      | 70.2 ms: 1.16x faster                                            |
| richards_super             | 59.6 ms                                                      | 51.4 ms: 1.16x faster                                            |
| scimark_sor                | 123 ms                                                       | 106 ms: 1.16x faster                                             |
| telco                      | 8.79 ms                                                      | 7.63 ms: 1.15x faster                                            |
| richards                   | 52.9 ms                                                      | 46.0 ms: 1.15x faster                                            |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 526 ms: 1.15x faster                                             |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 514 ms: 1.13x faster                                             |
| generators                 | 33.6 ms                                                      | 29.8 ms: 1.13x faster                                            |
| scimark_fft                | 328 ms                                                       | 294 ms: 1.12x faster                                             |
| bpe_tokeniser              | 5.09 sec                                                     | 4.57 sec: 1.11x faster                                           |
| xml_etree_parse            | 150 ms                                                       | 136 ms: 1.10x faster                                             |
| xml_etree_generate         | 86.5 ms                                                      | 79.0 ms: 1.10x faster                                            |
| go                         | 162 ms                                                       | 148 ms: 1.09x faster                                             |
| html5lib                   | 73.5 ms                                                      | 67.3 ms: 1.09x faster                                            |
| scimark_monte_carlo        | 66.1 ms                                                      | 60.6 ms: 1.09x faster                                            |
| xml_etree_process          | 61.2 ms                                                      | 56.2 ms: 1.09x faster                                            |
| pylint                     | 347 ms                                                       | 320 ms: 1.08x faster                                             |
| xml_etree_iterparse        | 103 ms                                                       | 95.5 ms: 1.08x faster                                            |
| connected_components       | 432 ms                                                       | 402 ms: 1.07x faster                                             |
| regex_v8                   | 26.1 ms                                                      | 24.5 ms: 1.07x faster                                            |
| async_generators           | 457 ms                                                       | 428 ms: 1.07x faster                                             |
| mako                       | 10.4 ms                                                      | 9.74 ms: 1.06x faster                                            |
| unpickle_pure_python       | 217 us                                                       | 205 us: 1.06x faster                                             |
| pathlib                    | 17.5 ms                                                      | 16.6 ms: 1.06x faster                                            |
| k_core                     | 2.17 sec                                                     | 2.05 sec: 1.06x faster                                           |
| genshi_text                | 26.2 ms                                                      | 24.8 ms: 1.06x faster                                            |
| thrift                     | 901 us                                                       | 856 us: 1.05x faster                                             |
| regex_compile              | 143 ms                                                       | 136 ms: 1.05x faster                                             |
| shortest_path              | 460 ms                                                       | 438 ms: 1.05x faster                                             |
| json                       | 5.69 ms                                                      | 5.43 ms: 1.05x faster                                            |
| scimark_lu                 | 98.7 ms                                                      | 94.3 ms: 1.05x faster                                            |
| sqlite_synth               | 2.91 us                                                      | 2.78 us: 1.05x faster                                            |
| pprint_safe_repr           | 843 ms                                                       | 812 ms: 1.04x faster                                             |
| pprint_pformat             | 1.72 sec                                                     | 1.67 sec: 1.03x faster                                           |
| genshi_xml                 | 57.1 ms                                                      | 55.5 ms: 1.03x faster                                            |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.02x faster                                            |
| sqlalchemy_declarative     | 148 ms                                                       | 146 ms: 1.02x faster                                             |
| sqlalchemy_imperative      | 18.3 ms                                                      | 18.0 ms: 1.02x faster                                            |
| sphinx                     | 1.12 sec                                                     | 1.11 sec: 1.01x faster                                           |
| sqlglot_parse              | 1.40 ms                                                      | 1.38 ms: 1.01x faster                                            |
| sqlglot_transpile          | 1.79 ms                                                      | 1.77 ms: 1.01x faster                                            |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                             |
| 2to3                       | 293 ms                                                       | 290 ms: 1.01x faster                                             |
| regex_dna                  | 247 ms                                                       | 244 ms: 1.01x faster                                             |
| logging_format             | 6.94 us                                                      | 6.90 us: 1.01x faster                                            |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.75 ms: 1.01x faster                                            |
| mdp                        | 2.54 sec                                                     | 2.55 sec: 1.00x slower                                           |
| pidigits                   | 252 ms                                                       | 253 ms: 1.00x slower                                             |
| python_startup_no_site     | 8.96 ms                                                      | 9.00 ms: 1.01x slower                                            |
| sympy_sum                  | 155 ms                                                       | 155 ms: 1.01x slower                                             |
| sympy_str                  | 298 ms                                                       | 300 ms: 1.01x slower                                             |
| sympy_integrate            | 23.6 ms                                                      | 23.7 ms: 1.01x slower                                            |
| python_startup             | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                            |
| sympy_expand               | 509 ms                                                       | 514 ms: 1.01x slower                                             |
| pycparser                  | 1.24 sec                                                     | 1.26 sec: 1.01x slower                                           |
| deltablue                  | 3.42 ms                                                      | 3.47 ms: 1.02x slower                                            |
| meteor_contest             | 130 ms                                                       | 132 ms: 1.02x slower                                             |
| sqlglot_optimize           | 59.3 ms                                                      | 60.5 ms: 1.02x slower                                            |
| coverage                   | 80.0 ms                                                      | 82.0 ms: 1.02x slower                                            |
| pickle_pure_python         | 323 us                                                       | 335 us: 1.04x slower                                             |
| bench_thread_pool          | 942 us                                                       | 979 us: 1.04x slower                                             |
| json_dumps                 | 11.1 ms                                                      | 11.6 ms: 1.04x slower                                            |
| docutils                   | 2.83 sec                                                     | 2.94 sec: 1.04x slower                                           |
| typing_runtime_protocols   | 169 us                                                       | 176 us: 1.04x slower                                             |
| chaos                      | 60.2 ms                                                      | 62.9 ms: 1.05x slower                                            |
| crypto_pyaes               | 73.3 ms                                                      | 76.6 ms: 1.05x slower                                            |
| fannkuch                   | 363 ms                                                       | 381 ms: 1.05x slower                                             |
| nqueens                    | 90.7 ms                                                      | 98.6 ms: 1.09x slower                                            |
| many_optionals             | 930 us                                                       | 1.01 ms: 1.09x slower                                            |
| hexiom                     | 6.55 ms                                                      | 7.14 ms: 1.09x slower                                            |
| json_loads                 | 24.7 us                                                      | 26.9 us: 1.09x slower                                            |
| raytrace                   | 273 ms                                                       | 299 ms: 1.10x slower                                             |
| comprehensions             | 17.0 us                                                      | 18.9 us: 1.11x slower                                            |
| nbody                      | 89.3 ms                                                      | 101 ms: 1.13x slower                                             |
| gc_traversal               | 4.74 ms                                                      | 6.29 ms: 1.33x slower                                            |
| subparsers                 | 17.5 ms                                                      | 23.4 ms: 1.34x slower                                            |
| bench_mp_pool              | 5.12 ms                                                      | 1.74 sec: 340.14x slower                                         |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                     |

Benchmark hidden because not significant (6): logging_silent, logging_simple, dulwich_log, create_gc_cycles, sqlglot_normalize, django_template
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.045x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x