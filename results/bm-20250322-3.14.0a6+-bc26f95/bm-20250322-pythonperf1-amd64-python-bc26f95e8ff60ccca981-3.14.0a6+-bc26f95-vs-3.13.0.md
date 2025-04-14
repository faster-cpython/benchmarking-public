# Results vs. 3.13.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: windows-amd64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.005x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 226 ms: 1.05x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.69 sec: 1.10x slower                                                      |
| html5lib       | 38.2 ms                                                     | 41.0 ms: 1.07x slower                                                       |
| sphinx         | 617 ms                                                      | 660 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.86x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 212 ms: 1.33x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 220 ms: 1.20x faster                                                        |
| async_tree_io              | 513 ms                                                      | 430 ms: 1.19x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 417 ms: 1.19x faster                                                        |
| async_tree_none            | 219 ms                                                      | 189 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 337 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 176 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 338 ms: 1.12x faster                                                        |
| async_generators           | 223 ms                                                      | 230 ms: 1.03x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.09x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 46.4 ms: 1.10x faster                                                       |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                        |
| nbody          | 66.3 ms                                                     | 67.3 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.0 ms: 1.71x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.44 ms: 1.17x faster                                                       |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| regex_compile  | 80.7 ms                                                     | 87.3 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 89.7 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.0 ms: 1.06x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 58.6 ms: 1.10x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.51 sec: 1.10x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 6.92 ms: 1.12x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 42.1 ms: 1.15x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 150 us: 1.15x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 227 us: 1.22x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.9 ms: 1.06x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 20.3 ms: 1.20x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.84 ms: 1.04x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 17.1 ms: 1.13x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 38.4 ms: 1.13x slower                                                       |
| django_template | 20.3 ms                                                     | 26.9 ms: 1.32x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.15x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 524 us: 16.17x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 32.7 ms: 2.30x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.86x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 14.0 ms: 1.71x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 212 ms: 1.33x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 220 ms: 1.20x faster                                                        |
| deepcopy                   | 223 us                                                      | 186 us: 1.20x faster                                                        |
| async_tree_io              | 513 ms                                                      | 430 ms: 1.19x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 417 ms: 1.19x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.44 ms: 1.17x faster                                                       |
| async_tree_none            | 219 ms                                                      | 189 ms: 1.16x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 20.0 us: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 337 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 176 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 338 ms: 1.12x faster                                                        |
| float                      | 50.8 ms                                                     | 46.4 ms: 1.10x faster                                                       |
| json                       | 3.30 ms                                                     | 3.03 ms: 1.09x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 59.3 ms: 1.07x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.96 us: 1.03x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 89.7 ms: 1.03x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.57 us: 1.01x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.82 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.62 ms: 1.01x slower                                                       |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                        |
| nbody                      | 66.3 ms                                                     | 67.3 ms: 1.02x slower                                                       |
| k_core                     | 1.70 sec                                                    | 1.73 sec: 1.02x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.25 ms: 1.02x slower                                                       |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| async_generators           | 223 ms                                                      | 230 ms: 1.03x slower                                                        |
| scimark_fft                | 175 ms                                                      | 181 ms: 1.04x slower                                                        |
| generators                 | 19.0 ms                                                     | 19.7 ms: 1.04x slower                                                       |
| mako                       | 6.56 ms                                                     | 6.84 ms: 1.04x slower                                                       |
| shortest_path              | 355 ms                                                      | 370 ms: 1.04x slower                                                        |
| connected_components       | 320 ms                                                      | 335 ms: 1.05x slower                                                        |
| 2to3                       | 215 ms                                                      | 226 ms: 1.05x slower                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 88.8 ms: 1.05x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 3.04 sec: 1.06x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.0 ms: 1.06x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.08 ms: 1.06x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 42.4 ms: 1.06x slower                                                       |
| go                         | 84.7 ms                                                     | 89.9 ms: 1.06x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.9 ms: 1.06x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 90.7 ms: 1.07x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 110 us: 1.07x slower                                                        |
| sympy_str                  | 167 ms                                                      | 178 ms: 1.07x slower                                                        |
| sphinx                     | 617 ms                                                      | 660 ms: 1.07x slower                                                        |
| pycparser                  | 695 ms                                                      | 745 ms: 1.07x slower                                                        |
| sympy_integrate            | 12.3 ms                                                     | 13.2 ms: 1.07x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 41.0 ms: 1.07x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 871 us: 1.08x slower                                                        |
| scimark_lu                 | 56.7 ms                                                     | 61.2 ms: 1.08x slower                                                       |
| sympy_expand               | 286 ms                                                      | 309 ms: 1.08x slower                                                        |
| scimark_sor                | 76.2 ms                                                     | 82.4 ms: 1.08x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 87.3 ms: 1.08x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 78.3 ms: 1.09x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 44.4 ms: 1.09x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.09x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 58.6 ms: 1.10x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.57 sec: 1.10x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.51 sec: 1.10x slower                                                      |
| coverage                   | 45.3 ms                                                     | 49.8 ms: 1.10x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.69 sec: 1.10x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 50.3 ms: 1.10x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 60.4 ns: 1.11x slower                                                       |
| chaos                      | 37.9 ms                                                     | 42.3 ms: 1.12x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.92 ms: 1.12x slower                                                       |
| pyflate                    | 283 ms                                                      | 318 ms: 1.12x slower                                                        |
| fannkuch                   | 252 ms                                                      | 282 ms: 1.12x slower                                                        |
| genshi_text                | 15.2 ms                                                     | 17.1 ms: 1.13x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 38.4 ms: 1.13x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.11 sec: 1.14x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 554 ms: 1.14x slower                                                        |
| nqueens                    | 56.1 ms                                                     | 64.5 ms: 1.15x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 42.1 ms: 1.15x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 150 us: 1.15x slower                                                        |
| hexiom                     | 3.84 ms                                                     | 4.44 ms: 1.16x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.71 us: 1.16x slower                                                       |
| logging_format             | 6.18 us                                                     | 7.22 us: 1.17x slower                                                       |
| richards                   | 26.3 ms                                                     | 30.7 ms: 1.17x slower                                                       |
| comprehensions             | 10.4 us                                                     | 12.2 us: 1.18x slower                                                       |
| richards_super             | 29.8 ms                                                     | 35.0 ms: 1.18x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 20.3 ms: 1.20x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.30 ms: 1.21x slower                                                       |
| many_optionals             | 361 us                                                      | 440 us: 1.22x slower                                                        |
| pickle_pure_python         | 186 us                                                      | 227 us: 1.22x slower                                                        |
| raytrace                   | 153 ms                                                      | 200 ms: 1.30x slower                                                        |
| django_template            | 20.3 ms                                                     | 26.9 ms: 1.32x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.8 ms: 1.55x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (2): json_loads, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown