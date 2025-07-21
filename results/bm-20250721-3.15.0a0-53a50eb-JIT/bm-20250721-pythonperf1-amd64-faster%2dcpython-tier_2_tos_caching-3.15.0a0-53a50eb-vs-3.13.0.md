# Results vs. 3.13.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: windows-amd64
- commit hash: 53a50eb
- commit date: 2025-07-21
- overall geometric mean: 1.086x faster
- HPT reliability: 94.89%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 218 ms: 1.01x slower                                                               |
| docutils       | 1.53 sec                                                    | 1.65 sec: 1.07x slower                                                             |
| sphinx         | 617 ms                                                      | 636 ms: 1.03x slower                                                               |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                       |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.87x faster                                                               |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                               |
| async_tree_memoization     | 265 ms                                                      | 202 ms: 1.31x faster                                                               |
| async_tree_none            | 219 ms                                                      | 167 ms: 1.31x faster                                                               |
| async_tree_io              | 513 ms                                                      | 394 ms: 1.30x faster                                                               |
| async_tree_io_tg           | 497 ms                                                      | 389 ms: 1.28x faster                                                               |
| async_tree_none_tg         | 200 ms                                                      | 165 ms: 1.21x faster                                                               |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 332 ms: 1.15x faster                                                               |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                               |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                               |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.14x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 46.2 ms: 1.43x faster                                                              |
| float          | 50.8 ms                                                     | 43.0 ms: 1.18x faster                                                              |
| pidigits       | 146 ms                                                      | 145 ms: 1.01x faster                                                               |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.5 ms: 1.64x faster                                                              |
| regex_effbot   | 1.69 ms                                                     | 1.56 ms: 1.08x faster                                                              |
| regex_compile  | 80.7 ms                                                     | 78.9 ms: 1.02x faster                                                              |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                                               |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.10 sec: 1.25x faster                                                             |
| unpickle_pure_python | 130 us                                                      | 107 us: 1.21x faster                                                               |
| xml_etree_parse      | 92.2 ms                                                     | 86.8 ms: 1.06x faster                                                              |
| xml_etree_generate   | 53.5 ms                                                     | 51.1 ms: 1.05x faster                                                              |
| json_loads           | 15.1 us                                                     | 14.5 us: 1.04x faster                                                              |
| xml_etree_process    | 36.5 ms                                                     | 35.6 ms: 1.03x faster                                                              |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.4 ms: 1.05x slower                                                              |
| pickle_pure_python   | 186 us                                                      | 200 us: 1.08x slower                                                               |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                                       |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.9 ms: 1.06x slower                                                              |
| python_startup_no_site | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.62 ms: 1.17x faster                                                              |
| genshi_text     | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                              |
| django_template | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                              |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                                       |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250721-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 493 us: 17.19x faster                                                              |
| pathlib                    | 75.3 ms                                                     | 30.1 ms: 2.50x faster                                                              |
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.87x faster                                                               |
| mdp                        | 1.43 sec                                                    | 798 ms: 1.79x faster                                                               |
| regex_v8                   | 23.8 ms                                                     | 14.5 ms: 1.64x faster                                                              |
| nbody                      | 66.3 ms                                                     | 46.2 ms: 1.43x faster                                                              |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                               |
| deepcopy                   | 223 us                                                      | 170 us: 1.31x faster                                                               |
| async_tree_memoization     | 265 ms                                                      | 202 ms: 1.31x faster                                                               |
| async_tree_none            | 219 ms                                                      | 167 ms: 1.31x faster                                                               |
| async_tree_io              | 513 ms                                                      | 394 ms: 1.30x faster                                                               |
| deepcopy_memo              | 23.1 us                                                     | 17.9 us: 1.29x faster                                                              |
| async_tree_io_tg           | 497 ms                                                      | 389 ms: 1.28x faster                                                               |
| tomli_loads                | 1.37 sec                                                    | 1.10 sec: 1.25x faster                                                             |
| unpickle_pure_python       | 130 us                                                      | 107 us: 1.21x faster                                                               |
| async_tree_none_tg         | 200 ms                                                      | 165 ms: 1.21x faster                                                               |
| scimark_fft                | 175 ms                                                      | 147 ms: 1.19x faster                                                               |
| float                      | 50.8 ms                                                     | 43.0 ms: 1.18x faster                                                              |
| mako                       | 6.56 ms                                                     | 5.62 ms: 1.17x faster                                                              |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 332 ms: 1.15x faster                                                               |
| telco                      | 4.85 ms                                                     | 4.24 ms: 1.14x faster                                                              |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.31 ms: 1.13x faster                                                              |
| go                         | 84.7 ms                                                     | 75.3 ms: 1.12x faster                                                              |
| pyflate                    | 283 ms                                                      | 252 ms: 1.12x faster                                                               |
| fannkuch                   | 252 ms                                                      | 224 ms: 1.12x faster                                                               |
| deepcopy_reduce            | 2.02 us                                                     | 1.81 us: 1.12x faster                                                              |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                               |
| bpe_tokeniser              | 2.87 sec                                                    | 2.58 sec: 1.11x faster                                                             |
| pprint_safe_repr           | 485 ms                                                      | 443 ms: 1.09x faster                                                               |
| json                       | 3.30 ms                                                     | 3.02 ms: 1.09x faster                                                              |
| regex_effbot               | 1.69 ms                                                     | 1.56 ms: 1.08x faster                                                              |
| pprint_pformat             | 977 ms                                                      | 902 ms: 1.08x faster                                                               |
| xml_etree_parse            | 92.2 ms                                                     | 86.8 ms: 1.06x faster                                                              |
| k_core                     | 1.70 sec                                                    | 1.62 sec: 1.05x faster                                                             |
| xml_etree_generate         | 53.5 ms                                                     | 51.1 ms: 1.05x faster                                                              |
| json_loads                 | 15.1 us                                                     | 14.5 us: 1.04x faster                                                              |
| scimark_sor                | 76.2 ms                                                     | 74.1 ms: 1.03x faster                                                              |
| xml_etree_process          | 36.5 ms                                                     | 35.6 ms: 1.03x faster                                                              |
| regex_compile              | 80.7 ms                                                     | 78.9 ms: 1.02x faster                                                              |
| sqlite_synth               | 1.59 us                                                     | 1.56 us: 1.02x faster                                                              |
| spectral_norm              | 63.4 ms                                                     | 62.2 ms: 1.02x faster                                                              |
| pidigits                   | 146 ms                                                      | 145 ms: 1.01x faster                                                               |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.4 ms: 1.01x faster                                                              |
| logging_silent             | 54.6 ns                                                     | 54.2 ns: 1.01x faster                                                              |
| crypto_pyaes               | 45.6 ms                                                     | 45.8 ms: 1.00x slower                                                              |
| genshi_text                | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                              |
| richards_super             | 29.8 ms                                                     | 30.2 ms: 1.01x slower                                                              |
| richards                   | 26.3 ms                                                     | 26.6 ms: 1.01x slower                                                              |
| 2to3                       | 215 ms                                                      | 218 ms: 1.01x slower                                                               |
| sympy_str                  | 167 ms                                                      | 170 ms: 1.02x slower                                                               |
| meteor_contest             | 72.0 ms                                                     | 73.2 ms: 1.02x slower                                                              |
| sympy_expand               | 286 ms                                                      | 292 ms: 1.02x slower                                                               |
| sympy_sum                  | 85.2 ms                                                     | 87.6 ms: 1.03x slower                                                              |
| sphinx                     | 617 ms                                                      | 636 ms: 1.03x slower                                                               |
| logging_simple             | 5.77 us                                                     | 5.95 us: 1.03x slower                                                              |
| sympy_integrate            | 12.3 ms                                                     | 12.7 ms: 1.03x slower                                                              |
| generators                 | 19.0 ms                                                     | 19.6 ms: 1.03x slower                                                              |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.03x slower                                                               |
| logging_format             | 6.18 us                                                     | 6.44 us: 1.04x slower                                                              |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.4 ms: 1.05x slower                                                              |
| chaos                      | 37.9 ms                                                     | 39.9 ms: 1.05x slower                                                              |
| scimark_lu                 | 56.7 ms                                                     | 60.0 ms: 1.06x slower                                                              |
| python_startup             | 24.4 ms                                                     | 25.9 ms: 1.06x slower                                                              |
| hexiom                     | 3.84 ms                                                     | 4.08 ms: 1.06x slower                                                              |
| nqueens                    | 56.1 ms                                                     | 60.0 ms: 1.07x slower                                                              |
| docutils                   | 1.53 sec                                                    | 1.65 sec: 1.07x slower                                                             |
| pickle_pure_python         | 186 us                                                      | 200 us: 1.08x slower                                                               |
| coverage                   | 45.3 ms                                                     | 49.1 ms: 1.08x slower                                                              |
| create_gc_cycles           | 1.22 ms                                                     | 1.33 ms: 1.08x slower                                                              |
| gc_traversal               | 1.96 ms                                                     | 2.14 ms: 1.09x slower                                                              |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                               |
| deltablue                  | 1.89 ms                                                     | 2.16 ms: 1.14x slower                                                              |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.14x slower                                                              |
| python_startup_no_site     | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                                              |
| raytrace                   | 153 ms                                                      | 177 ms: 1.16x slower                                                               |
| django_template            | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                              |
| many_optionals             | 361 us                                                      | 569 us: 1.57x slower                                                               |
| subparsers                 | 10.9 ms                                                     | 30.1 ms: 2.77x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                                       |

Benchmark hidden because not significant (10): pylint, pycparser, shortest_path, comprehensions, typing_runtime_protocols, dulwich_log, connected_components, genshi_xml, json_dumps, html5lib
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250721-3.15.0a0-53a50eb-JIT/bm-20250721-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.086x faster

# HPT report

- Reliability score: 94.89% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown