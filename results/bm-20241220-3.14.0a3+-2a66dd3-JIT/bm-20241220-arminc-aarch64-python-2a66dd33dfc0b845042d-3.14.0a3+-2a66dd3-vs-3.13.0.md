# Results vs. 3.13.0

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: linux-aarch64
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.024x slower
- HPT reliability: 93.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.26 sec: 1.10x slower                                                   |
| html5lib       | 65.6 ms                                                  | 71.4 ms: 1.09x slower                                                    |
| sphinx         | 1.20 sec                                                 | 1.27 sec: 1.06x slower                                                   |
| Geometric mean | (ref)                                                    | 1.07x slower                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 502 ms: 1.32x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 935 ms: 1.25x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 535 ms: 1.24x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 399 ms: 1.21x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 962 ms: 1.18x faster                                                     |
| async_tree_none            | 504 ms                                                   | 428 ms: 1.18x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 683 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 703 ms: 1.12x faster                                                     |
| async_generators           | 500 ms                                                   | 543 ms: 1.09x slower                                                     |
| Geometric mean             | (ref)                                                    | 1.14x faster                                                             |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.04 ms: 1.26x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 31.3 ms: 1.04x faster                                                    |
| regex_compile  | 134 ms                                                   | 142 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                    | 1.05x faster                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 182 ms: 1.11x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 144 ms: 1.10x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.54 sec: 1.05x faster                                                   |
| Geometric mean      | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (6): xml_etree_generate, json_loads, xml_etree_process, unpickle_pure_python, json_dumps, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.12 ms: 1.04x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 14.0 ms                                                  | 13.5 ms: 1.04x faster                                                    |
| genshi_text     | 28.6 ms                                                  | 33.1 ms: 1.16x slower                                                    |
| django_template | 39.4 ms                                                  | 47.8 ms: 1.21x slower                                                    |
| genshi_xml      | 61.6 ms                                                  | 83.4 ms: 1.35x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.16x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo              | 53.0 us                                                  | 38.7 us: 1.37x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 502 ms: 1.32x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.04 ms: 1.26x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 935 ms: 1.25x faster                                                     |
| deepcopy                   | 479 us                                                   | 385 us: 1.25x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 535 ms: 1.24x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 399 ms: 1.21x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 962 ms: 1.18x faster                                                     |
| async_tree_none            | 504 ms                                                   | 428 ms: 1.18x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 683 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 703 ms: 1.12x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 182 ms: 1.11x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 21.9 ms: 1.11x faster                                                    |
| scimark_fft                | 463 ms                                                   | 418 ms: 1.11x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 144 ms: 1.10x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.93 us: 1.08x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.82 ms: 1.06x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.54 sec: 1.05x faster                                                   |
| bpe_tokeniser              | 6.02 sec                                                 | 5.78 sec: 1.04x faster                                                   |
| regex_v8                   | 32.5 ms                                                  | 31.3 ms: 1.04x faster                                                    |
| mako                       | 14.0 ms                                                  | 13.5 ms: 1.04x faster                                                    |
| richards                   | 54.5 ms                                                  | 56.3 ms: 1.03x slower                                                    |
| mdp                        | 3.45 sec                                                 | 3.57 sec: 1.04x slower                                                   |
| python_startup_no_site     | 8.79 ms                                                  | 9.12 ms: 1.04x slower                                                    |
| shortest_path              | 565 ms                                                   | 587 ms: 1.04x slower                                                     |
| scimark_lu                 | 146 ms                                                   | 155 ms: 1.06x slower                                                     |
| sphinx                     | 1.20 sec                                                 | 1.27 sec: 1.06x slower                                                   |
| regex_compile              | 134 ms                                                   | 142 ms: 1.06x slower                                                     |
| logging_silent             | 135 ns                                                   | 144 ns: 1.07x slower                                                     |
| typing_runtime_protocols   | 197 us                                                   | 212 us: 1.07x slower                                                     |
| logging_format             | 8.10 us                                                  | 8.73 us: 1.08x slower                                                    |
| sqlglot_parse              | 1.43 ms                                                  | 1.55 ms: 1.08x slower                                                    |
| sqlalchemy_imperative      | 16.1 ms                                                  | 17.4 ms: 1.08x slower                                                    |
| sqlglot_normalize          | 131 ms                                                   | 142 ms: 1.08x slower                                                     |
| pycparser                  | 1.34 sec                                                 | 1.46 sec: 1.08x slower                                                   |
| async_generators           | 500 ms                                                   | 543 ms: 1.09x slower                                                     |
| create_gc_cycles           | 3.39 ms                                                  | 3.68 ms: 1.09x slower                                                    |
| sympy_expand               | 472 ms                                                   | 514 ms: 1.09x slower                                                     |
| html5lib                   | 65.6 ms                                                  | 71.4 ms: 1.09x slower                                                    |
| logging_simple             | 7.25 us                                                  | 7.93 us: 1.09x slower                                                    |
| meteor_contest             | 117 ms                                                   | 128 ms: 1.10x slower                                                     |
| fannkuch                   | 478 ms                                                   | 524 ms: 1.10x slower                                                     |
| crypto_pyaes               | 84.9 ms                                                  | 93.2 ms: 1.10x slower                                                    |
| docutils                   | 2.96 sec                                                 | 3.26 sec: 1.10x slower                                                   |
| deltablue                  | 3.97 ms                                                  | 4.44 ms: 1.12x slower                                                    |
| sympy_sum                  | 151 ms                                                   | 171 ms: 1.13x slower                                                     |
| sympy_integrate            | 21.4 ms                                                  | 24.5 ms: 1.14x slower                                                    |
| genshi_text                | 28.6 ms                                                  | 33.1 ms: 1.16x slower                                                    |
| sympy_str                  | 265 ms                                                   | 311 ms: 1.17x slower                                                     |
| raytrace                   | 310 ms                                                   | 369 ms: 1.19x slower                                                     |
| comprehensions             | 20.8 us                                                  | 25.0 us: 1.20x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 7.13 ms: 1.20x slower                                                    |
| django_template            | 39.4 ms                                                  | 47.8 ms: 1.21x slower                                                    |
| nqueens                    | 105 ms                                                   | 129 ms: 1.22x slower                                                     |
| chaos                      | 70.7 ms                                                  | 87.5 ms: 1.24x slower                                                    |
| many_optionals             | 626 us                                                   | 787 us: 1.26x slower                                                     |
| generators                 | 40.3 ms                                                  | 51.9 ms: 1.29x slower                                                    |
| hexiom                     | 7.34 ms                                                  | 9.59 ms: 1.31x slower                                                    |
| pprint_safe_repr           | 962 ms                                                   | 1.26 sec: 1.31x slower                                                   |
| pprint_pformat             | 1.99 sec                                                 | 2.65 sec: 1.33x slower                                                   |
| genshi_xml                 | 61.6 ms                                                  | 83.4 ms: 1.35x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 27.6 ms: 1.36x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 1.37 sec: 169.73x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.08x slower                                                             |

Benchmark hidden because not significant (33): scimark_monte_carlo, xml_etree_generate, scimark_sor, coverage, pylint, float, json_loads, sqlite_synth, spectral_norm, xml_etree_process, k_core, coroutines, asyncio_websockets, scimark_sparse_mat_mult, json, unpickle_pure_python, regex_dna, richards_super, connected_components, djangocms, thrift, sqlalchemy_declarative, nbody, pidigits, pyflate, python_startup, 2to3, json_dumps, go, sqlglot_optimize, pickle_pure_python, sqlglot_transpile, bench_thread_pool
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (2) of results/bm-20241220-3.14.0a3+-2a66dd3-JIT/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: dulwich_log, mypy2

- Geometric mean (including insignificant results): 1.024x slower

# HPT report

- Reliability score: 93.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.04x