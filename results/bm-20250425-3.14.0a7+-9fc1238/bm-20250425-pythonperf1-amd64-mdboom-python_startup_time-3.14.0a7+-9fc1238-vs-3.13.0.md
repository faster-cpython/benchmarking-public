# Results vs. 3.13.0

- fork: mdboom
- ref: python_startup_time
- machine: windows-amd64
- commit hash: 9fc1238
- commit date: 2025-04-25
- overall geometric mean: 1.029x faster
- HPT reliability: 88.38%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 220 ms: 1.02x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                     |
| sphinx         | 617 ms                                                      | 649 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 156 ms: 1.92x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 205 ms: 1.29x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 393 ms: 1.26x faster                                                       |
| async_tree_io              | 513 ms                                                      | 408 ms: 1.26x faster                                                       |
| async_tree_none            | 219 ms                                                      | 178 ms: 1.23x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 331 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 337 ms: 1.13x faster                                                       |
| async_generators           | 223 ms                                                      | 221 ms: 1.01x faster                                                       |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 42.6 ms: 1.19x faster                                                      |
| nbody          | 66.3 ms                                                     | 62.2 ms: 1.06x faster                                                      |
| pidigits       | 146 ms                                                      | 150 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.7 ms: 1.63x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.47 ms: 1.15x faster                                                      |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 88.5 ms: 1.04x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.9 us: 1.01x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                     |
| unpickle_pure_python | 130 us                                                      | 136 us: 1.05x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 56.3 ms: 1.05x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.5 ms: 1.07x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 6.69 ms: 1.08x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 39.9 ms: 1.09x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 210 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.2 ms: 1.08x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.9 ms: 1.18x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.65 ms: 1.01x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                      |
| django_template | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 32.0 ms: 2.36x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 156 ms: 1.92x faster                                                       |
| mdp                        | 1.43 sec                                                    | 781 ms: 1.83x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.7 ms: 1.63x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                       |
| deepcopy                   | 223 us                                                      | 171 us: 1.31x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 205 ms: 1.29x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 393 ms: 1.26x faster                                                       |
| async_tree_io              | 513 ms                                                      | 408 ms: 1.26x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.5 us: 1.25x faster                                                      |
| async_tree_none            | 219 ms                                                      | 178 ms: 1.23x faster                                                       |
| float                      | 50.8 ms                                                     | 42.6 ms: 1.19x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 54.7 ms: 1.16x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.47 ms: 1.15x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 331 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 337 ms: 1.13x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.79 us: 1.13x faster                                                      |
| go                         | 84.7 ms                                                     | 77.3 ms: 1.10x faster                                                      |
| json                       | 3.30 ms                                                     | 3.08 ms: 1.07x faster                                                      |
| nbody                      | 66.3 ms                                                     | 62.2 ms: 1.06x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.61 ms: 1.05x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.48 ms: 1.05x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 88.5 ms: 1.04x faster                                                      |
| scimark_fft                | 175 ms                                                      | 171 ms: 1.02x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.83 sec: 1.02x faster                                                     |
| json_loads                 | 15.1 us                                                     | 14.9 us: 1.01x faster                                                      |
| pyflate                    | 283 ms                                                      | 281 ms: 1.01x faster                                                       |
| async_generators           | 223 ms                                                      | 221 ms: 1.01x faster                                                       |
| fannkuch                   | 252 ms                                                      | 255 ms: 1.01x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.2 ms: 1.01x slower                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 41.3 ms: 1.01x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                     |
| mako                       | 6.56 ms                                                     | 6.65 ms: 1.01x slower                                                      |
| chaos                      | 37.9 ms                                                     | 38.4 ms: 1.01x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.5 ms: 1.02x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 105 us: 1.02x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                      |
| sympy_str                  | 167 ms                                                      | 170 ms: 1.02x slower                                                       |
| shortest_path              | 355 ms                                                      | 363 ms: 1.02x slower                                                       |
| pidigits                   | 146 ms                                                      | 150 ms: 1.02x slower                                                       |
| 2to3                       | 215 ms                                                      | 220 ms: 1.02x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.26 ms: 1.03x slower                                                      |
| sympy_expand               | 286 ms                                                      | 293 ms: 1.03x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 58.5 ms: 1.03x slower                                                      |
| connected_components       | 320 ms                                                      | 332 ms: 1.04x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 88.5 ms: 1.04x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 47.4 ms: 1.04x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 74.8 ms: 1.04x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 504 ms: 1.04x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.02 sec: 1.05x slower                                                     |
| dulwich_log                | 40.1 ms                                                     | 41.9 ms: 1.05x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 136 us: 1.05x slower                                                       |
| sphinx                     | 617 ms                                                      | 649 ms: 1.05x slower                                                       |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 56.3 ms: 1.05x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 59.2 ms: 1.06x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 89.0 ms: 1.06x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.07 ms: 1.06x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.08 ms: 1.06x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 862 us: 1.06x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.5 ms: 1.07x slower                                                      |
| python_startup             | 24.4 ms                                                     | 26.2 ms: 1.08x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                     |
| logging_simple             | 5.77 us                                                     | 6.22 us: 1.08x slower                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.69 ms: 1.08x slower                                                      |
| richards                   | 26.3 ms                                                     | 28.4 ms: 1.08x slower                                                      |
| richards_super             | 29.8 ms                                                     | 32.4 ms: 1.09x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.73 us: 1.09x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 39.9 ms: 1.09x slower                                                      |
| comprehensions             | 10.4 us                                                     | 11.4 us: 1.10x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.10x slower                                                      |
| raytrace                   | 153 ms                                                      | 173 ms: 1.13x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 210 us: 1.13x slower                                                       |
| coverage                   | 45.3 ms                                                     | 51.7 ms: 1.14x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.17 ms: 1.15x slower                                                      |
| many_optionals             | 361 us                                                      | 424 us: 1.17x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.9 ms: 1.18x slower                                                      |
| django_template            | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                      |
| subparsers                 | 10.9 ms                                                     | 16.1 ms: 1.48x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (9): pylint, html5lib, genshi_xml, regex_compile, scimark_sor, sqlite_synth, logging_silent, k_core, pycparser
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250425-3.14.0a7+-9fc1238/bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.029x faster

# HPT report

- Reliability score: 88.38% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown