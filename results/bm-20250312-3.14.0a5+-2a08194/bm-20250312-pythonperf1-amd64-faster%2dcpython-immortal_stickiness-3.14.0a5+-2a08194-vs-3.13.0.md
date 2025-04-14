# Results vs. 3.13.0

- fork: faster-cpython
- ref: immortal_stickiness
- machine: windows-amd64
- commit hash: 2a08194
- commit date: 2025-03-12
- overall geometric mean: 1.004x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 229 ms: 1.06x slower                                                                 |
| docutils       | 1.53 sec                                                    | 1.69 sec: 1.11x slower                                                               |
| html5lib       | 38.2 ms                                                     | 40.7 ms: 1.07x slower                                                                |
| sphinx         | 617 ms                                                      | 654 ms: 1.06x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 216 ms: 1.30x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 424 ms: 1.21x faster                                                                 |
| async_tree_memoization     | 265 ms                                                      | 222 ms: 1.19x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 420 ms: 1.18x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 191 ms: 1.15x faster                                                                 |
| async_tree_none_tg         | 200 ms                                                      | 177 ms: 1.13x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                                 |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 342 ms: 1.11x faster                                                                 |
| async_generators           | 223 ms                                                      | 227 ms: 1.02x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                                         |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 45.4 ms: 1.12x faster                                                                |
| nbody          | 66.3 ms                                                     | 67.4 ms: 1.02x slower                                                                |
| pidigits       | 146 ms                                                      | 152 ms: 1.04x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.2 ms: 1.81x faster                                                                |
| regex_effbot   | 1.69 ms                                                     | 1.40 ms: 1.21x faster                                                                |
| regex_dna      | 115 ms                                                      | 111 ms: 1.04x faster                                                                 |
| regex_compile  | 80.7 ms                                                     | 86.5 ms: 1.07x slower                                                                |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.8 us: 1.02x faster                                                                |
| xml_etree_parse      | 92.2 ms                                                     | 90.9 ms: 1.01x faster                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                               |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.0 ms: 1.06x slower                                                                |
| xml_etree_generate   | 53.5 ms                                                     | 59.2 ms: 1.11x slower                                                                |
| json_dumps           | 6.19 ms                                                     | 7.02 ms: 1.13x slower                                                                |
| unpickle_pure_python | 130 us                                                      | 150 us: 1.16x slower                                                                 |
| xml_etree_process    | 36.5 ms                                                     | 42.4 ms: 1.16x slower                                                                |
| pickle_pure_python   | 186 us                                                      | 232 us: 1.25x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.4 ms: 1.08x slower                                                                |
| python_startup_no_site | 16.9 ms                                                     | 20.5 ms: 1.21x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.15x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.96 ms: 1.06x slower                                                                |
| genshi_text     | 15.2 ms                                                     | 17.4 ms: 1.14x slower                                                                |
| genshi_xml      | 33.9 ms                                                     | 39.1 ms: 1.15x slower                                                                |
| django_template | 20.3 ms                                                     | 25.9 ms: 1.28x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.16x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 533 us: 15.88x faster                                                                |
| pathlib                    | 75.3 ms                                                     | 32.2 ms: 2.34x faster                                                                |
| regex_v8                   | 23.8 ms                                                     | 13.2 ms: 1.81x faster                                                                |
| async_tree_memoization_tg  | 281 ms                                                      | 216 ms: 1.30x faster                                                                 |
| deepcopy                   | 223 us                                                      | 180 us: 1.24x faster                                                                 |
| regex_effbot               | 1.69 ms                                                     | 1.40 ms: 1.21x faster                                                                |
| async_tree_io              | 513 ms                                                      | 424 ms: 1.21x faster                                                                 |
| deepcopy_memo              | 23.1 us                                                     | 19.3 us: 1.19x faster                                                                |
| async_tree_memoization     | 265 ms                                                      | 222 ms: 1.19x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 420 ms: 1.18x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 191 ms: 1.15x faster                                                                 |
| async_tree_none_tg         | 200 ms                                                      | 177 ms: 1.13x faster                                                                 |
| spectral_norm              | 63.4 ms                                                     | 56.6 ms: 1.12x faster                                                                |
| float                      | 50.8 ms                                                     | 45.4 ms: 1.12x faster                                                                |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                                 |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 342 ms: 1.11x faster                                                                 |
| json                       | 3.30 ms                                                     | 3.05 ms: 1.08x faster                                                                |
| deepcopy_reduce            | 2.02 us                                                     | 1.93 us: 1.05x faster                                                                |
| regex_dna                  | 115 ms                                                      | 111 ms: 1.04x faster                                                                 |
| json_loads                 | 15.1 us                                                     | 14.8 us: 1.02x faster                                                                |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.56 ms: 1.02x faster                                                                |
| xml_etree_parse            | 92.2 ms                                                     | 90.9 ms: 1.01x faster                                                                |
| telco                      | 4.85 ms                                                     | 4.90 ms: 1.01x slower                                                                |
| create_gc_cycles           | 1.22 ms                                                     | 1.24 ms: 1.01x slower                                                                |
| generators                 | 19.0 ms                                                     | 19.3 ms: 1.02x slower                                                                |
| nbody                      | 66.3 ms                                                     | 67.4 ms: 1.02x slower                                                                |
| async_generators           | 223 ms                                                      | 227 ms: 1.02x slower                                                                 |
| k_core                     | 1.70 sec                                                    | 1.74 sec: 1.02x slower                                                               |
| scimark_lu                 | 56.7 ms                                                     | 58.2 ms: 1.03x slower                                                                |
| shortest_path              | 355 ms                                                      | 365 ms: 1.03x slower                                                                 |
| scimark_fft                | 175 ms                                                      | 180 ms: 1.03x slower                                                                 |
| gc_traversal               | 1.96 ms                                                     | 2.03 ms: 1.03x slower                                                                |
| pidigits                   | 146 ms                                                      | 152 ms: 1.04x slower                                                                 |
| scimark_sor                | 76.2 ms                                                     | 79.0 ms: 1.04x slower                                                                |
| tomli_loads                | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                               |
| connected_components       | 320 ms                                                      | 336 ms: 1.05x slower                                                                 |
| bench_mp_pool              | 84.2 ms                                                     | 88.7 ms: 1.05x slower                                                                |
| bpe_tokeniser              | 2.87 sec                                                    | 3.03 sec: 1.05x slower                                                               |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.0 ms: 1.06x slower                                                                |
| sympy_expand               | 286 ms                                                      | 303 ms: 1.06x slower                                                                 |
| sphinx                     | 617 ms                                                      | 654 ms: 1.06x slower                                                                 |
| sympy_str                  | 167 ms                                                      | 177 ms: 1.06x slower                                                                 |
| mako                       | 6.56 ms                                                     | 6.96 ms: 1.06x slower                                                                |
| sympy_sum                  | 85.2 ms                                                     | 90.4 ms: 1.06x slower                                                                |
| 2to3                       | 215 ms                                                      | 229 ms: 1.06x slower                                                                 |
| html5lib                   | 38.2 ms                                                     | 40.7 ms: 1.07x slower                                                                |
| dulwich_log                | 40.1 ms                                                     | 42.8 ms: 1.07x slower                                                                |
| logging_silent             | 54.6 ns                                                     | 58.4 ns: 1.07x slower                                                                |
| bench_thread_pool          | 810 us                                                      | 868 us: 1.07x slower                                                                 |
| regex_compile              | 80.7 ms                                                     | 86.5 ms: 1.07x slower                                                                |
| go                         | 84.7 ms                                                     | 90.8 ms: 1.07x slower                                                                |
| typing_runtime_protocols   | 103 us                                                      | 111 us: 1.08x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                                |
| scimark_monte_carlo        | 40.7 ms                                                     | 44.0 ms: 1.08x slower                                                                |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.08x slower                                                                |
| pycparser                  | 695 ms                                                      | 752 ms: 1.08x slower                                                                 |
| meteor_contest             | 72.0 ms                                                     | 77.9 ms: 1.08x slower                                                                |
| python_startup             | 24.4 ms                                                     | 26.4 ms: 1.08x slower                                                                |
| coverage                   | 45.3 ms                                                     | 49.4 ms: 1.09x slower                                                                |
| docutils                   | 1.53 sec                                                    | 1.69 sec: 1.11x slower                                                               |
| mdp                        | 1.43 sec                                                    | 1.58 sec: 1.11x slower                                                               |
| xml_etree_generate         | 53.5 ms                                                     | 59.2 ms: 1.11x slower                                                                |
| pyflate                    | 283 ms                                                      | 314 ms: 1.11x slower                                                                 |
| crypto_pyaes               | 45.6 ms                                                     | 50.7 ms: 1.11x slower                                                                |
| pprint_safe_repr           | 485 ms                                                      | 541 ms: 1.12x slower                                                                 |
| fannkuch                   | 252 ms                                                      | 282 ms: 1.12x slower                                                                 |
| pprint_pformat             | 977 ms                                                      | 1.10 sec: 1.12x slower                                                               |
| richards_super             | 29.8 ms                                                     | 33.7 ms: 1.13x slower                                                                |
| logging_simple             | 5.77 us                                                     | 6.54 us: 1.13x slower                                                                |
| json_dumps                 | 6.19 ms                                                     | 7.02 ms: 1.13x slower                                                                |
| hexiom                     | 3.84 ms                                                     | 4.39 ms: 1.14x slower                                                                |
| genshi_text                | 15.2 ms                                                     | 17.4 ms: 1.14x slower                                                                |
| logging_format             | 6.18 us                                                     | 7.07 us: 1.15x slower                                                                |
| comprehensions             | 10.4 us                                                     | 11.9 us: 1.15x slower                                                                |
| richards                   | 26.3 ms                                                     | 30.2 ms: 1.15x slower                                                                |
| genshi_xml                 | 33.9 ms                                                     | 39.1 ms: 1.15x slower                                                                |
| unpickle_pure_python       | 130 us                                                      | 150 us: 1.16x slower                                                                 |
| xml_etree_process          | 36.5 ms                                                     | 42.4 ms: 1.16x slower                                                                |
| nqueens                    | 56.1 ms                                                     | 65.4 ms: 1.16x slower                                                                |
| chaos                      | 37.9 ms                                                     | 44.1 ms: 1.17x slower                                                                |
| deltablue                  | 1.89 ms                                                     | 2.25 ms: 1.19x slower                                                                |
| python_startup_no_site     | 16.9 ms                                                     | 20.5 ms: 1.21x slower                                                                |
| many_optionals             | 361 us                                                      | 440 us: 1.22x slower                                                                 |
| pickle_pure_python         | 186 us                                                      | 232 us: 1.25x slower                                                                 |
| django_template            | 20.3 ms                                                     | 25.9 ms: 1.28x slower                                                                |
| raytrace                   | 153 ms                                                      | 200 ms: 1.30x slower                                                                 |
| subparsers                 | 10.9 ms                                                     | 16.5 ms: 1.52x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                                         |

Benchmark hidden because not significant (3): pylint, sqlite_synth, asyncio_websockets
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250312-3.14.0a5+-2a08194/bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown