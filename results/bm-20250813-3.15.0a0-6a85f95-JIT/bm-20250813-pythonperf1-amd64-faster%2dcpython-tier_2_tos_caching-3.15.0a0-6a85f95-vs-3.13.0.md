# Results vs. 3.13.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: windows-amd64
- commit hash: 6a85f95
- commit date: 2025-08-13
- overall geometric mean: 1.108x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250813-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 217 ms: 1.01x slower                                                               |
| docutils       | 1.53 sec                                                    | 1.60 sec: 1.05x slower                                                             |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                       |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250813-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 154 ms: 1.95x faster                                                               |
| async_tree_io              | 513 ms                                                      | 379 ms: 1.35x faster                                                               |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                               |
| async_tree_memoization     | 265 ms                                                      | 199 ms: 1.33x faster                                                               |
| async_tree_io_tg           | 497 ms                                                      | 374 ms: 1.33x faster                                                               |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.28x faster                                                               |
| async_tree_none_tg         | 200 ms                                                      | 164 ms: 1.22x faster                                                               |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                               |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 335 ms: 1.14x faster                                                               |
| async_generators           | 223 ms                                                      | 246 ms: 1.10x slower                                                               |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.16x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.23x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250813-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 43.5 ms: 1.52x faster                                                              |
| float          | 50.8 ms                                                     | 43.0 ms: 1.18x faster                                                              |
| Geometric mean | (ref)                                                       | 1.22x faster                                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250813-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.1 ms: 1.82x faster                                                              |
| regex_effbot   | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                                              |
| regex_compile  | 80.7 ms                                                     | 77.8 ms: 1.04x faster                                                              |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                       |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250813-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.07 sec: 1.28x faster                                                             |
| unpickle_pure_python | 130 us                                                      | 104 us: 1.25x faster                                                               |
| json_dumps           | 6.19 ms                                                     | 5.40 ms: 1.15x faster                                                              |
| json_loads           | 15.1 us                                                     | 13.9 us: 1.08x faster                                                              |
| xml_etree_generate   | 53.5 ms                                                     | 50.1 ms: 1.07x faster                                                              |
| xml_etree_parse      | 92.2 ms                                                     | 86.7 ms: 1.06x faster                                                              |
| xml_etree_process    | 36.5 ms                                                     | 34.7 ms: 1.05x faster                                                              |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.5 ms: 1.05x slower                                                              |
| pickle_pure_python   | 186 us                                                      | 201 us: 1.08x slower                                                               |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250813-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.2 ms: 1.03x slower                                                              |
| python_startup_no_site | 16.9 ms                                                     | 19.0 ms: 1.12x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250813-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.38 ms: 1.22x faster                                                              |
| genshi_text     | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                              |
| django_template | 20.3 ms                                                     | 24.0 ms: 1.18x slower                                                              |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                                       |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250813-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 490 us: 17.28x faster                                                              |
| pathlib                    | 75.3 ms                                                     | 28.6 ms: 2.63x faster                                                              |
| asyncio_websockets         | 300 ms                                                      | 154 ms: 1.95x faster                                                               |
| mdp                        | 1.43 sec                                                    | 773 ms: 1.85x faster                                                               |
| regex_v8                   | 23.8 ms                                                     | 13.1 ms: 1.82x faster                                                              |
| nbody                      | 66.3 ms                                                     | 43.5 ms: 1.52x faster                                                              |
| async_tree_io              | 513 ms                                                      | 379 ms: 1.35x faster                                                               |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                               |
| async_tree_memoization     | 265 ms                                                      | 199 ms: 1.33x faster                                                               |
| async_tree_io_tg           | 497 ms                                                      | 374 ms: 1.33x faster                                                               |
| deepcopy                   | 223 us                                                      | 169 us: 1.32x faster                                                               |
| deepcopy_memo              | 23.1 us                                                     | 17.9 us: 1.29x faster                                                              |
| tomli_loads                | 1.37 sec                                                    | 1.07 sec: 1.28x faster                                                             |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.28x faster                                                               |
| fannkuch                   | 252 ms                                                      | 200 ms: 1.26x faster                                                               |
| unpickle_pure_python       | 130 us                                                      | 104 us: 1.25x faster                                                               |
| async_tree_none_tg         | 200 ms                                                      | 164 ms: 1.22x faster                                                               |
| mako                       | 6.56 ms                                                     | 5.38 ms: 1.22x faster                                                              |
| scimark_fft                | 175 ms                                                      | 145 ms: 1.20x faster                                                               |
| float                      | 50.8 ms                                                     | 43.0 ms: 1.18x faster                                                              |
| bpe_tokeniser              | 2.87 sec                                                    | 2.47 sec: 1.16x faster                                                             |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                               |
| json_dumps                 | 6.19 ms                                                     | 5.40 ms: 1.15x faster                                                              |
| telco                      | 4.85 ms                                                     | 4.24 ms: 1.14x faster                                                              |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 335 ms: 1.14x faster                                                               |
| pprint_safe_repr           | 485 ms                                                      | 430 ms: 1.13x faster                                                               |
| pprint_pformat             | 977 ms                                                      | 867 ms: 1.13x faster                                                               |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.31 ms: 1.12x faster                                                              |
| deepcopy_reduce            | 2.02 us                                                     | 1.80 us: 1.12x faster                                                              |
| json                       | 3.30 ms                                                     | 2.96 ms: 1.11x faster                                                              |
| go                         | 84.7 ms                                                     | 76.1 ms: 1.11x faster                                                              |
| pyflate                    | 283 ms                                                      | 257 ms: 1.10x faster                                                               |
| regex_effbot               | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                                              |
| json_loads                 | 15.1 us                                                     | 13.9 us: 1.08x faster                                                              |
| k_core                     | 1.70 sec                                                    | 1.58 sec: 1.08x faster                                                             |
| pylint                     | 205 ms                                                      | 192 ms: 1.07x faster                                                               |
| xml_etree_generate         | 53.5 ms                                                     | 50.1 ms: 1.07x faster                                                              |
| xml_etree_parse            | 92.2 ms                                                     | 86.7 ms: 1.06x faster                                                              |
| xml_etree_process          | 36.5 ms                                                     | 34.7 ms: 1.05x faster                                                              |
| crypto_pyaes               | 45.6 ms                                                     | 43.5 ms: 1.05x faster                                                              |
| pycparser                  | 695 ms                                                      | 666 ms: 1.04x faster                                                               |
| meteor_contest             | 72.0 ms                                                     | 69.0 ms: 1.04x faster                                                              |
| dulwich_log                | 40.1 ms                                                     | 38.5 ms: 1.04x faster                                                              |
| spectral_norm              | 63.4 ms                                                     | 60.9 ms: 1.04x faster                                                              |
| sqlite_synth               | 1.59 us                                                     | 1.52 us: 1.04x faster                                                              |
| regex_compile              | 80.7 ms                                                     | 77.8 ms: 1.04x faster                                                              |
| shortest_path              | 355 ms                                                      | 344 ms: 1.03x faster                                                               |
| typing_runtime_protocols   | 103 us                                                      | 101 us: 1.02x faster                                                               |
| connected_components       | 320 ms                                                      | 313 ms: 1.02x faster                                                               |
| logging_silent             | 54.6 ns                                                     | 53.9 ns: 1.01x faster                                                              |
| scimark_sor                | 76.2 ms                                                     | 75.4 ms: 1.01x faster                                                              |
| comprehensions             | 10.4 us                                                     | 10.3 us: 1.01x faster                                                              |
| sympy_str                  | 167 ms                                                      | 166 ms: 1.01x faster                                                               |
| sympy_expand               | 286 ms                                                      | 288 ms: 1.01x slower                                                               |
| 2to3                       | 215 ms                                                      | 217 ms: 1.01x slower                                                               |
| sympy_integrate            | 12.3 ms                                                     | 12.5 ms: 1.01x slower                                                              |
| genshi_text                | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                              |
| scimark_lu                 | 56.7 ms                                                     | 57.4 ms: 1.01x slower                                                              |
| richards_super             | 29.8 ms                                                     | 30.4 ms: 1.02x slower                                                              |
| richards                   | 26.3 ms                                                     | 26.9 ms: 1.02x slower                                                              |
| generators                 | 19.0 ms                                                     | 19.6 ms: 1.03x slower                                                              |
| python_startup             | 24.4 ms                                                     | 25.2 ms: 1.03x slower                                                              |
| logging_simple             | 5.77 us                                                     | 5.98 us: 1.04x slower                                                              |
| create_gc_cycles           | 1.22 ms                                                     | 1.27 ms: 1.04x slower                                                              |
| nqueens                    | 56.1 ms                                                     | 58.6 ms: 1.04x slower                                                              |
| docutils                   | 1.53 sec                                                    | 1.60 sec: 1.05x slower                                                             |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.5 ms: 1.05x slower                                                              |
| chaos                      | 37.9 ms                                                     | 39.8 ms: 1.05x slower                                                              |
| gc_traversal               | 1.96 ms                                                     | 2.07 ms: 1.05x slower                                                              |
| logging_format             | 6.18 us                                                     | 6.52 us: 1.05x slower                                                              |
| hexiom                     | 3.84 ms                                                     | 4.05 ms: 1.06x slower                                                              |
| pickle_pure_python         | 186 us                                                      | 201 us: 1.08x slower                                                               |
| coverage                   | 45.3 ms                                                     | 49.2 ms: 1.09x slower                                                              |
| async_generators           | 223 ms                                                      | 246 ms: 1.10x slower                                                               |
| python_startup_no_site     | 16.9 ms                                                     | 19.0 ms: 1.12x slower                                                              |
| raytrace                   | 153 ms                                                      | 176 ms: 1.15x slower                                                               |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.16x slower                                                              |
| django_template            | 20.3 ms                                                     | 24.0 ms: 1.18x slower                                                              |
| deltablue                  | 1.89 ms                                                     | 2.26 ms: 1.20x slower                                                              |
| many_optionals             | 361 us                                                      | 559 us: 1.55x slower                                                               |
| subparsers                 | 10.9 ms                                                     | 29.3 ms: 2.70x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                                       |

Benchmark hidden because not significant (7): html5lib, pidigits, regex_dna, scimark_monte_carlo, genshi_xml, sympy_sum, sphinx
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250813-3.15.0a0-6a85f95-JIT/bm-20250813-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.108x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown