# Results vs. 3.13.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: windows-amd64
- commit hash: 6041480
- commit date: 2025-08-11
- overall geometric mean: 1.086x faster
- HPT reliability: 96.29%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 222 ms: 1.03x slower                                                               |
| docutils       | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                             |
| html5lib       | 38.2 ms                                                     | 39.1 ms: 1.02x slower                                                              |
| sphinx         | 617 ms                                                      | 643 ms: 1.04x slower                                                               |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.90x faster                                                               |
| async_tree_io              | 513 ms                                                      | 383 ms: 1.34x faster                                                               |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                               |
| async_tree_memoization     | 265 ms                                                      | 204 ms: 1.30x faster                                                               |
| async_tree_io_tg           | 497 ms                                                      | 387 ms: 1.28x faster                                                               |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.27x faster                                                               |
| async_tree_none_tg         | 200 ms                                                      | 166 ms: 1.20x faster                                                               |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 335 ms: 1.14x faster                                                               |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 339 ms: 1.13x faster                                                               |
| async_generators           | 223 ms                                                      | 246 ms: 1.11x slower                                                               |
| coroutines                 | 12.5 ms                                                     | 14.8 ms: 1.19x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 45.2 ms: 1.47x faster                                                              |
| float          | 50.8 ms                                                     | 43.7 ms: 1.16x faster                                                              |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.3 ms: 1.79x faster                                                              |
| regex_effbot   | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                                              |
| regex_compile  | 80.7 ms                                                     | 78.0 ms: 1.04x faster                                                              |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                       |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.11 sec: 1.23x faster                                                             |
| unpickle_pure_python | 130 us                                                      | 108 us: 1.21x faster                                                               |
| json_dumps           | 6.19 ms                                                     | 5.60 ms: 1.10x faster                                                              |
| xml_etree_generate   | 53.5 ms                                                     | 50.2 ms: 1.07x faster                                                              |
| xml_etree_parse      | 92.2 ms                                                     | 87.1 ms: 1.06x faster                                                              |
| json_loads           | 15.1 us                                                     | 14.3 us: 1.05x faster                                                              |
| xml_etree_process    | 36.5 ms                                                     | 35.0 ms: 1.04x faster                                                              |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.1 ms: 1.04x slower                                                              |
| pickle_pure_python   | 186 us                                                      | 204 us: 1.10x slower                                                               |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.5 ms: 1.09x slower                                                              |
| python_startup_no_site | 16.9 ms                                                     | 19.7 ms: 1.16x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.47 ms: 1.20x faster                                                              |
| genshi_text     | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                              |
| django_template | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                                              |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                                       |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 499 us: 16.96x faster                                                              |
| pathlib                    | 75.3 ms                                                     | 31.7 ms: 2.38x faster                                                              |
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.90x faster                                                               |
| mdp                        | 1.43 sec                                                    | 796 ms: 1.80x faster                                                               |
| regex_v8                   | 23.8 ms                                                     | 13.3 ms: 1.79x faster                                                              |
| nbody                      | 66.3 ms                                                     | 45.2 ms: 1.47x faster                                                              |
| deepcopy                   | 223 us                                                      | 166 us: 1.35x faster                                                               |
| deepcopy_memo              | 23.1 us                                                     | 17.2 us: 1.34x faster                                                              |
| async_tree_io              | 513 ms                                                      | 383 ms: 1.34x faster                                                               |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                               |
| async_tree_memoization     | 265 ms                                                      | 204 ms: 1.30x faster                                                               |
| async_tree_io_tg           | 497 ms                                                      | 387 ms: 1.28x faster                                                               |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.27x faster                                                               |
| tomli_loads                | 1.37 sec                                                    | 1.11 sec: 1.23x faster                                                             |
| unpickle_pure_python       | 130 us                                                      | 108 us: 1.21x faster                                                               |
| async_tree_none_tg         | 200 ms                                                      | 166 ms: 1.20x faster                                                               |
| mako                       | 6.56 ms                                                     | 5.47 ms: 1.20x faster                                                              |
| scimark_fft                | 175 ms                                                      | 147 ms: 1.19x faster                                                               |
| fannkuch                   | 252 ms                                                      | 212 ms: 1.19x faster                                                               |
| float                      | 50.8 ms                                                     | 43.7 ms: 1.16x faster                                                              |
| telco                      | 4.85 ms                                                     | 4.25 ms: 1.14x faster                                                              |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 335 ms: 1.14x faster                                                               |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 339 ms: 1.13x faster                                                               |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.32 ms: 1.12x faster                                                              |
| bpe_tokeniser              | 2.87 sec                                                    | 2.56 sec: 1.12x faster                                                             |
| deepcopy_reduce            | 2.02 us                                                     | 1.81 us: 1.12x faster                                                              |
| go                         | 84.7 ms                                                     | 75.7 ms: 1.12x faster                                                              |
| pprint_safe_repr           | 485 ms                                                      | 437 ms: 1.11x faster                                                               |
| json_dumps                 | 6.19 ms                                                     | 5.60 ms: 1.10x faster                                                              |
| regex_effbot               | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                                              |
| pprint_pformat             | 977 ms                                                      | 898 ms: 1.09x faster                                                               |
| json                       | 3.30 ms                                                     | 3.05 ms: 1.08x faster                                                              |
| pyflate                    | 283 ms                                                      | 262 ms: 1.08x faster                                                               |
| xml_etree_generate         | 53.5 ms                                                     | 50.2 ms: 1.07x faster                                                              |
| xml_etree_parse            | 92.2 ms                                                     | 87.1 ms: 1.06x faster                                                              |
| json_loads                 | 15.1 us                                                     | 14.3 us: 1.05x faster                                                              |
| xml_etree_process          | 36.5 ms                                                     | 35.0 ms: 1.04x faster                                                              |
| k_core                     | 1.70 sec                                                    | 1.63 sec: 1.04x faster                                                             |
| regex_compile              | 80.7 ms                                                     | 78.0 ms: 1.04x faster                                                              |
| sqlite_synth               | 1.59 us                                                     | 1.54 us: 1.03x faster                                                              |
| meteor_contest             | 72.0 ms                                                     | 70.2 ms: 1.03x faster                                                              |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.8 ms: 1.02x faster                                                              |
| scimark_sor                | 76.2 ms                                                     | 75.4 ms: 1.01x faster                                                              |
| shortest_path              | 355 ms                                                      | 353 ms: 1.01x faster                                                               |
| scimark_lu                 | 56.7 ms                                                     | 56.9 ms: 1.00x slower                                                              |
| richards                   | 26.3 ms                                                     | 26.6 ms: 1.01x slower                                                              |
| richards_super             | 29.8 ms                                                     | 30.1 ms: 1.01x slower                                                              |
| comprehensions             | 10.4 us                                                     | 10.5 us: 1.01x slower                                                              |
| logging_silent             | 54.6 ns                                                     | 55.3 ns: 1.01x slower                                                              |
| generators                 | 19.0 ms                                                     | 19.4 ms: 1.02x slower                                                              |
| sympy_str                  | 167 ms                                                      | 171 ms: 1.02x slower                                                               |
| html5lib                   | 38.2 ms                                                     | 39.1 ms: 1.02x slower                                                              |
| dulwich_log                | 40.1 ms                                                     | 41.3 ms: 1.03x slower                                                              |
| genshi_text                | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                              |
| 2to3                       | 215 ms                                                      | 222 ms: 1.03x slower                                                               |
| sympy_sum                  | 85.2 ms                                                     | 87.8 ms: 1.03x slower                                                              |
| sympy_integrate            | 12.3 ms                                                     | 12.7 ms: 1.03x slower                                                              |
| sympy_expand               | 286 ms                                                      | 297 ms: 1.04x slower                                                               |
| sphinx                     | 617 ms                                                      | 643 ms: 1.04x slower                                                               |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.1 ms: 1.04x slower                                                              |
| spectral_norm              | 63.4 ms                                                     | 66.5 ms: 1.05x slower                                                              |
| logging_simple             | 5.77 us                                                     | 6.08 us: 1.05x slower                                                              |
| nqueens                    | 56.1 ms                                                     | 59.1 ms: 1.05x slower                                                              |
| logging_format             | 6.18 us                                                     | 6.60 us: 1.07x slower                                                              |
| chaos                      | 37.9 ms                                                     | 40.5 ms: 1.07x slower                                                              |
| create_gc_cycles           | 1.22 ms                                                     | 1.31 ms: 1.07x slower                                                              |
| hexiom                     | 3.84 ms                                                     | 4.13 ms: 1.07x slower                                                              |
| docutils                   | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                             |
| python_startup             | 24.4 ms                                                     | 26.5 ms: 1.09x slower                                                              |
| gc_traversal               | 1.96 ms                                                     | 2.13 ms: 1.09x slower                                                              |
| coverage                   | 45.3 ms                                                     | 49.5 ms: 1.09x slower                                                              |
| pickle_pure_python         | 186 us                                                      | 204 us: 1.10x slower                                                               |
| async_generators           | 223 ms                                                      | 246 ms: 1.11x slower                                                               |
| raytrace                   | 153 ms                                                      | 177 ms: 1.15x slower                                                               |
| python_startup_no_site     | 16.9 ms                                                     | 19.7 ms: 1.16x slower                                                              |
| coroutines                 | 12.5 ms                                                     | 14.8 ms: 1.19x slower                                                              |
| django_template            | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                                              |
| deltablue                  | 1.89 ms                                                     | 2.29 ms: 1.21x slower                                                              |
| many_optionals             | 361 us                                                      | 569 us: 1.58x slower                                                               |
| subparsers                 | 10.9 ms                                                     | 29.9 ms: 2.76x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                                       |

Benchmark hidden because not significant (8): pylint, pycparser, regex_dna, typing_runtime_protocols, pidigits, crypto_pyaes, connected_components, genshi_xml
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250811-3.15.0a0-6041480-JIT/bm-20250811-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.086x faster

# HPT report

- Reliability score: 96.29% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown