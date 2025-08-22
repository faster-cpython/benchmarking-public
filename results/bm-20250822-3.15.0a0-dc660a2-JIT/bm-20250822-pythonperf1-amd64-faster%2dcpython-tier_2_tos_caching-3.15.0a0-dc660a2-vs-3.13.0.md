# Results vs. 3.13.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: windows-amd64
- commit hash: dc660a2
- commit date: 2025-08-22
- overall geometric mean: 1.103x faster
- HPT reliability: 99.11%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| docutils       | 1.53 sec                                                    | 1.61 sec: 1.05x slower                                                             |
| sphinx         | 617 ms                                                      | 629 ms: 1.02x slower                                                               |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                       |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 167 ms: 1.80x faster                                                               |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                               |
| async_tree_io              | 513 ms                                                      | 385 ms: 1.33x faster                                                               |
| async_tree_io_tg           | 497 ms                                                      | 377 ms: 1.32x faster                                                               |
| async_tree_memoization     | 265 ms                                                      | 203 ms: 1.31x faster                                                               |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                               |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                               |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                               |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 333 ms: 1.15x faster                                                               |
| async_generators           | 223 ms                                                      | 239 ms: 1.07x slower                                                               |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.15x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 42.6 ms: 1.56x faster                                                              |
| float          | 50.8 ms                                                     | 43.6 ms: 1.17x faster                                                              |
| pidigits       | 146 ms                                                      | 145 ms: 1.01x faster                                                               |
| Geometric mean | (ref)                                                       | 1.22x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.0 ms: 1.70x faster                                                              |
| regex_effbot   | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                                              |
| regex_compile  | 80.7 ms                                                     | 78.3 ms: 1.03x faster                                                              |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                                               |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.08 sec: 1.27x faster                                                             |
| unpickle_pure_python | 130 us                                                      | 105 us: 1.23x faster                                                               |
| json_dumps           | 6.19 ms                                                     | 5.32 ms: 1.16x faster                                                              |
| xml_etree_parse      | 92.2 ms                                                     | 83.1 ms: 1.11x faster                                                              |
| xml_etree_generate   | 53.5 ms                                                     | 48.8 ms: 1.09x faster                                                              |
| json_loads           | 15.1 us                                                     | 14.0 us: 1.08x faster                                                              |
| xml_etree_process    | 36.5 ms                                                     | 35.0 ms: 1.04x faster                                                              |
| pickle_pure_python   | 186 us                                                      | 203 us: 1.09x slower                                                               |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                                       |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.3 ms: 1.04x slower                                                              |
| python_startup_no_site | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.53 ms: 1.19x faster                                                              |
| genshi_text     | 15.2 ms                                                     | 15.6 ms: 1.03x slower                                                              |
| genshi_xml      | 33.9 ms                                                     | 35.2 ms: 1.04x slower                                                              |
| django_template | 20.3 ms                                                     | 24.1 ms: 1.19x slower                                                              |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 478 us: 17.70x faster                                                              |
| pathlib                    | 75.3 ms                                                     | 29.5 ms: 2.55x faster                                                              |
| mdp                        | 1.43 sec                                                    | 793 ms: 1.81x faster                                                               |
| asyncio_websockets         | 300 ms                                                      | 167 ms: 1.80x faster                                                               |
| regex_v8                   | 23.8 ms                                                     | 14.0 ms: 1.70x faster                                                              |
| nbody                      | 66.3 ms                                                     | 42.6 ms: 1.56x faster                                                              |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                               |
| async_tree_io              | 513 ms                                                      | 385 ms: 1.33x faster                                                               |
| deepcopy                   | 223 us                                                      | 169 us: 1.32x faster                                                               |
| async_tree_io_tg           | 497 ms                                                      | 377 ms: 1.32x faster                                                               |
| async_tree_memoization     | 265 ms                                                      | 203 ms: 1.31x faster                                                               |
| telco                      | 4.85 ms                                                     | 3.77 ms: 1.29x faster                                                              |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                               |
| tomli_loads                | 1.37 sec                                                    | 1.08 sec: 1.27x faster                                                             |
| unpickle_pure_python       | 130 us                                                      | 105 us: 1.23x faster                                                               |
| scimark_fft                | 175 ms                                                      | 142 ms: 1.23x faster                                                               |
| deepcopy_memo              | 23.1 us                                                     | 19.0 us: 1.22x faster                                                              |
| fannkuch                   | 252 ms                                                      | 209 ms: 1.20x faster                                                               |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                               |
| mako                       | 6.56 ms                                                     | 5.53 ms: 1.19x faster                                                              |
| pprint_safe_repr           | 485 ms                                                      | 412 ms: 1.18x faster                                                               |
| json                       | 3.30 ms                                                     | 2.82 ms: 1.17x faster                                                              |
| float                      | 50.8 ms                                                     | 43.6 ms: 1.17x faster                                                              |
| json_dumps                 | 6.19 ms                                                     | 5.32 ms: 1.16x faster                                                              |
| bpe_tokeniser              | 2.87 sec                                                    | 2.47 sec: 1.16x faster                                                             |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                               |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 333 ms: 1.15x faster                                                               |
| pprint_pformat             | 977 ms                                                      | 851 ms: 1.15x faster                                                               |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.28 ms: 1.14x faster                                                              |
| deepcopy_reduce            | 2.02 us                                                     | 1.81 us: 1.12x faster                                                              |
| xml_etree_parse            | 92.2 ms                                                     | 83.1 ms: 1.11x faster                                                              |
| regex_effbot               | 1.69 ms                                                     | 1.54 ms: 1.10x faster                                                              |
| go                         | 84.7 ms                                                     | 77.1 ms: 1.10x faster                                                              |
| pyflate                    | 283 ms                                                      | 258 ms: 1.10x faster                                                               |
| xml_etree_generate         | 53.5 ms                                                     | 48.8 ms: 1.09x faster                                                              |
| k_core                     | 1.70 sec                                                    | 1.57 sec: 1.08x faster                                                             |
| json_loads                 | 15.1 us                                                     | 14.0 us: 1.08x faster                                                              |
| pylint                     | 205 ms                                                      | 193 ms: 1.06x faster                                                               |
| crypto_pyaes               | 45.6 ms                                                     | 43.5 ms: 1.05x faster                                                              |
| xml_etree_process          | 36.5 ms                                                     | 35.0 ms: 1.04x faster                                                              |
| regex_compile              | 80.7 ms                                                     | 78.3 ms: 1.03x faster                                                              |
| meteor_contest             | 72.0 ms                                                     | 69.8 ms: 1.03x faster                                                              |
| sqlite_synth               | 1.59 us                                                     | 1.54 us: 1.03x faster                                                              |
| shortest_path              | 355 ms                                                      | 348 ms: 1.02x faster                                                               |
| dulwich_log                | 40.1 ms                                                     | 39.3 ms: 1.02x faster                                                              |
| spectral_norm              | 63.4 ms                                                     | 62.7 ms: 1.01x faster                                                              |
| pidigits                   | 146 ms                                                      | 145 ms: 1.01x faster                                                               |
| connected_components       | 320 ms                                                      | 317 ms: 1.01x faster                                                               |
| sympy_expand               | 286 ms                                                      | 287 ms: 1.00x slower                                                               |
| sympy_str                  | 167 ms                                                      | 167 ms: 1.00x slower                                                               |
| scimark_monte_carlo        | 40.7 ms                                                     | 41.0 ms: 1.01x slower                                                              |
| sympy_integrate            | 12.3 ms                                                     | 12.5 ms: 1.01x slower                                                              |
| scimark_sor                | 76.2 ms                                                     | 77.3 ms: 1.01x slower                                                              |
| sphinx                     | 617 ms                                                      | 629 ms: 1.02x slower                                                               |
| hexiom                     | 3.84 ms                                                     | 3.94 ms: 1.03x slower                                                              |
| genshi_text                | 15.2 ms                                                     | 15.6 ms: 1.03x slower                                                              |
| richards                   | 26.3 ms                                                     | 27.0 ms: 1.03x slower                                                              |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.03x slower                                                               |
| richards_super             | 29.8 ms                                                     | 30.7 ms: 1.03x slower                                                              |
| generators                 | 19.0 ms                                                     | 19.6 ms: 1.03x slower                                                              |
| python_startup             | 24.4 ms                                                     | 25.3 ms: 1.04x slower                                                              |
| scimark_lu                 | 56.7 ms                                                     | 58.8 ms: 1.04x slower                                                              |
| genshi_xml                 | 33.9 ms                                                     | 35.2 ms: 1.04x slower                                                              |
| nqueens                    | 56.1 ms                                                     | 58.4 ms: 1.04x slower                                                              |
| logging_simple             | 5.77 us                                                     | 6.02 us: 1.04x slower                                                              |
| logging_format             | 6.18 us                                                     | 6.48 us: 1.05x slower                                                              |
| create_gc_cycles           | 1.22 ms                                                     | 1.29 ms: 1.05x slower                                                              |
| docutils                   | 1.53 sec                                                    | 1.61 sec: 1.05x slower                                                             |
| gc_traversal               | 1.96 ms                                                     | 2.07 ms: 1.05x slower                                                              |
| chaos                      | 37.9 ms                                                     | 40.3 ms: 1.06x slower                                                              |
| async_generators           | 223 ms                                                      | 239 ms: 1.07x slower                                                               |
| pickle_pure_python         | 186 us                                                      | 203 us: 1.09x slower                                                               |
| coverage                   | 45.3 ms                                                     | 49.8 ms: 1.10x slower                                                              |
| raytrace                   | 153 ms                                                      | 173 ms: 1.13x slower                                                               |
| python_startup_no_site     | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                              |
| coroutines                 | 12.5 ms                                                     | 14.3 ms: 1.15x slower                                                              |
| django_template            | 20.3 ms                                                     | 24.1 ms: 1.19x slower                                                              |
| deltablue                  | 1.89 ms                                                     | 2.26 ms: 1.20x slower                                                              |
| many_optionals             | 361 us                                                      | 565 us: 1.57x slower                                                               |
| subparsers                 | 10.9 ms                                                     | 30.4 ms: 2.80x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.10x faster                                                                       |

Benchmark hidden because not significant (8): pycparser, typing_runtime_protocols, html5lib, 2to3, xml_etree_iterparse, sympy_sum, comprehensions, logging_silent
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250822-3.15.0a0-dc660a2-JIT/bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.103x faster

# HPT report

- Reliability score: 99.11% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown