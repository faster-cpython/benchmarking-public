# Results vs. 3.13.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: windows-amd64
- commit hash: a4de1bf
- commit date: 2025-07-22
- overall geometric mean: 1.083x faster
- HPT reliability: 91.69%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 221 ms: 1.03x slower                                                               |
| docutils       | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                             |
| sphinx         | 617 ms                                                      | 638 ms: 1.03x slower                                                               |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                       |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.87x faster                                                               |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                               |
| async_tree_none            | 219 ms                                                      | 167 ms: 1.31x faster                                                               |
| async_tree_memoization     | 265 ms                                                      | 203 ms: 1.30x faster                                                               |
| async_tree_io              | 513 ms                                                      | 397 ms: 1.29x faster                                                               |
| async_tree_io_tg           | 497 ms                                                      | 396 ms: 1.26x faster                                                               |
| async_tree_none_tg         | 200 ms                                                      | 167 ms: 1.20x faster                                                               |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 331 ms: 1.15x faster                                                               |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 341 ms: 1.12x faster                                                               |
| async_generators           | 223 ms                                                      | 250 ms: 1.12x slower                                                               |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.15x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 47.8 ms: 1.39x faster                                                              |
| float          | 50.8 ms                                                     | 44.0 ms: 1.15x faster                                                              |
| pidigits       | 146 ms                                                      | 145 ms: 1.01x faster                                                               |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.0 ms: 1.70x faster                                                              |
| regex_effbot   | 1.69 ms                                                     | 1.61 ms: 1.05x faster                                                              |
| regex_compile  | 80.7 ms                                                     | 78.7 ms: 1.03x faster                                                              |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                               |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.08 sec: 1.27x faster                                                             |
| unpickle_pure_python | 130 us                                                      | 106 us: 1.23x faster                                                               |
| json_loads           | 15.1 us                                                     | 14.2 us: 1.06x faster                                                              |
| xml_etree_generate   | 53.5 ms                                                     | 51.0 ms: 1.05x faster                                                              |
| xml_etree_process    | 36.5 ms                                                     | 35.2 ms: 1.04x faster                                                              |
| xml_etree_parse      | 92.2 ms                                                     | 89.5 ms: 1.03x faster                                                              |
| json_dumps           | 6.19 ms                                                     | 6.26 ms: 1.01x slower                                                              |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.4 ms: 1.05x slower                                                              |
| pickle_pure_python   | 186 us                                                      | 202 us: 1.09x slower                                                               |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.7 ms: 1.05x slower                                                              |
| python_startup_no_site | 16.9 ms                                                     | 19.2 ms: 1.14x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.58 ms: 1.18x faster                                                              |
| genshi_text     | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                              |
| django_template | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                              |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                                       |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 502 us: 16.87x faster                                                              |
| pathlib                    | 75.3 ms                                                     | 30.3 ms: 2.49x faster                                                              |
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.87x faster                                                               |
| mdp                        | 1.43 sec                                                    | 804 ms: 1.78x faster                                                               |
| regex_v8                   | 23.8 ms                                                     | 14.0 ms: 1.70x faster                                                              |
| nbody                      | 66.3 ms                                                     | 47.8 ms: 1.39x faster                                                              |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                               |
| deepcopy_memo              | 23.1 us                                                     | 17.3 us: 1.34x faster                                                              |
| deepcopy                   | 223 us                                                      | 168 us: 1.33x faster                                                               |
| async_tree_none            | 219 ms                                                      | 167 ms: 1.31x faster                                                               |
| async_tree_memoization     | 265 ms                                                      | 203 ms: 1.30x faster                                                               |
| async_tree_io              | 513 ms                                                      | 397 ms: 1.29x faster                                                               |
| tomli_loads                | 1.37 sec                                                    | 1.08 sec: 1.27x faster                                                             |
| async_tree_io_tg           | 497 ms                                                      | 396 ms: 1.26x faster                                                               |
| unpickle_pure_python       | 130 us                                                      | 106 us: 1.23x faster                                                               |
| async_tree_none_tg         | 200 ms                                                      | 167 ms: 1.20x faster                                                               |
| scimark_fft                | 175 ms                                                      | 148 ms: 1.18x faster                                                               |
| mako                       | 6.56 ms                                                     | 5.58 ms: 1.18x faster                                                              |
| float                      | 50.8 ms                                                     | 44.0 ms: 1.15x faster                                                              |
| fannkuch                   | 252 ms                                                      | 218 ms: 1.15x faster                                                               |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 331 ms: 1.15x faster                                                               |
| telco                      | 4.85 ms                                                     | 4.29 ms: 1.13x faster                                                              |
| go                         | 84.7 ms                                                     | 75.2 ms: 1.13x faster                                                              |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 341 ms: 1.12x faster                                                               |
| deepcopy_reduce            | 2.02 us                                                     | 1.81 us: 1.12x faster                                                              |
| bpe_tokeniser              | 2.87 sec                                                    | 2.58 sec: 1.11x faster                                                             |
| pprint_safe_repr           | 485 ms                                                      | 435 ms: 1.11x faster                                                               |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.35 ms: 1.11x faster                                                              |
| pyflate                    | 283 ms                                                      | 256 ms: 1.10x faster                                                               |
| pprint_pformat             | 977 ms                                                      | 887 ms: 1.10x faster                                                               |
| json                       | 3.30 ms                                                     | 3.00 ms: 1.10x faster                                                              |
| json_loads                 | 15.1 us                                                     | 14.2 us: 1.06x faster                                                              |
| k_core                     | 1.70 sec                                                    | 1.61 sec: 1.06x faster                                                             |
| regex_effbot               | 1.69 ms                                                     | 1.61 ms: 1.05x faster                                                              |
| xml_etree_generate         | 53.5 ms                                                     | 51.0 ms: 1.05x faster                                                              |
| xml_etree_process          | 36.5 ms                                                     | 35.2 ms: 1.04x faster                                                              |
| xml_etree_parse            | 92.2 ms                                                     | 89.5 ms: 1.03x faster                                                              |
| regex_compile              | 80.7 ms                                                     | 78.7 ms: 1.03x faster                                                              |
| scimark_sor                | 76.2 ms                                                     | 74.6 ms: 1.02x faster                                                              |
| sqlite_synth               | 1.59 us                                                     | 1.55 us: 1.02x faster                                                              |
| pidigits                   | 146 ms                                                      | 145 ms: 1.01x faster                                                               |
| spectral_norm              | 63.4 ms                                                     | 63.9 ms: 1.01x slower                                                              |
| typing_runtime_protocols   | 103 us                                                      | 104 us: 1.01x slower                                                               |
| json_dumps                 | 6.19 ms                                                     | 6.26 ms: 1.01x slower                                                              |
| generators                 | 19.0 ms                                                     | 19.3 ms: 1.02x slower                                                              |
| genshi_text                | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                              |
| sympy_str                  | 167 ms                                                      | 170 ms: 1.02x slower                                                               |
| richards_super             | 29.8 ms                                                     | 30.4 ms: 1.02x slower                                                              |
| sympy_expand               | 286 ms                                                      | 292 ms: 1.02x slower                                                               |
| sympy_sum                  | 85.2 ms                                                     | 87.1 ms: 1.02x slower                                                              |
| sympy_integrate            | 12.3 ms                                                     | 12.6 ms: 1.02x slower                                                              |
| richards                   | 26.3 ms                                                     | 26.9 ms: 1.03x slower                                                              |
| 2to3                       | 215 ms                                                      | 221 ms: 1.03x slower                                                               |
| sphinx                     | 617 ms                                                      | 638 ms: 1.03x slower                                                               |
| scimark_monte_carlo        | 40.7 ms                                                     | 42.4 ms: 1.04x slower                                                              |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.4 ms: 1.05x slower                                                              |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                               |
| hexiom                     | 3.84 ms                                                     | 4.04 ms: 1.05x slower                                                              |
| python_startup             | 24.4 ms                                                     | 25.7 ms: 1.05x slower                                                              |
| gc_traversal               | 1.96 ms                                                     | 2.08 ms: 1.06x slower                                                              |
| logging_simple             | 5.77 us                                                     | 6.14 us: 1.06x slower                                                              |
| logging_format             | 6.18 us                                                     | 6.57 us: 1.06x slower                                                              |
| nqueens                    | 56.1 ms                                                     | 59.9 ms: 1.07x slower                                                              |
| create_gc_cycles           | 1.22 ms                                                     | 1.32 ms: 1.08x slower                                                              |
| scimark_lu                 | 56.7 ms                                                     | 61.0 ms: 1.08x slower                                                              |
| chaos                      | 37.9 ms                                                     | 40.8 ms: 1.08x slower                                                              |
| docutils                   | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                             |
| pickle_pure_python         | 186 us                                                      | 202 us: 1.09x slower                                                               |
| async_generators           | 223 ms                                                      | 250 ms: 1.12x slower                                                               |
| python_startup_no_site     | 16.9 ms                                                     | 19.2 ms: 1.14x slower                                                              |
| deltablue                  | 1.89 ms                                                     | 2.16 ms: 1.14x slower                                                              |
| coverage                   | 45.3 ms                                                     | 52.2 ms: 1.15x slower                                                              |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.15x slower                                                              |
| raytrace                   | 153 ms                                                      | 180 ms: 1.17x slower                                                               |
| django_template            | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                              |
| many_optionals             | 361 us                                                      | 572 us: 1.58x slower                                                               |
| subparsers                 | 10.9 ms                                                     | 30.1 ms: 2.78x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                                       |

Benchmark hidden because not significant (11): pylint, shortest_path, pycparser, meteor_contest, logging_silent, comprehensions, crypto_pyaes, dulwich_log, connected_components, genshi_xml, html5lib
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250722-3.15.0a0-a4de1bf-JIT/bm-20250722-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.083x faster

# HPT report

- Reliability score: 91.69% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown