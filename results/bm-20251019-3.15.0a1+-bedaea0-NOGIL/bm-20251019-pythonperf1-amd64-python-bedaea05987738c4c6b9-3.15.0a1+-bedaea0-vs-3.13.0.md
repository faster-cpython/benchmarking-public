# Results vs. 3.13.0

- fork: python
- ref: bedaea05987738c4c6b9
- machine: windows-amd64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.038x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 220 ms: 1.02x slower                                                        |
| docutils       | 1.53 sec                                                    | 2.82 sec: 1.84x slower                                                      |
| html5lib       | 38.2 ms                                                     | 39.0 ms: 1.02x slower                                                       |
| sphinx         | 617 ms                                                      | 643 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.19x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 139 ms: 2.17x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 323 ms: 1.54x faster                                                        |
| async_tree_io              | 513 ms                                                      | 344 ms: 1.49x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 191 ms: 1.47x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 145 ms: 1.38x faster                                                        |
| async_tree_none            | 219 ms                                                      | 169 ms: 1.30x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 303 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 324 ms: 1.18x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.10x slower                                                       |
| async_generators           | 223 ms                                                      | 252 ms: 1.13x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.31x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 46.2 ms: 1.10x faster                                                       |
| pidigits       | 146 ms                                                      | 136 ms: 1.08x faster                                                        |
| nbody          | 66.3 ms                                                     | 76.7 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.2 ms: 1.80x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.57 ms: 1.08x faster                                                       |
| regex_dna      | 115 ms                                                      | 112 ms: 1.03x faster                                                        |
| regex_compile  | 80.7 ms                                                     | 89.8 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 6.19 ms                                                     | 5.97 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 59.9 ms: 1.01x faster                                                       |
| json_loads           | 15.1 us                                                     | 15.9 us: 1.05x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 148 us: 1.14x slower                                                        |
| xml_etree_generate   | 53.5 ms                                                     | 61.9 ms: 1.16x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 43.2 ms: 1.18x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 223 us: 1.20x slower                                                        |
| tomli_loads          | 1.37 sec                                                    | 2.32 sec: 1.69x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.14x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.9 ms: 1.06x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.2 ms: 1.14x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 37.7 ms: 1.11x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 18.3 ms: 1.20x slower                                                       |
| django_template | 20.3 ms                                                     | 26.1 ms: 1.29x slower                                                       |
| mako            | 6.56 ms                                                     | 10.1 ms: 1.54x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.28x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 563 us: 15.04x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 28.8 ms: 2.61x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 139 ms: 2.17x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 13.2 ms: 1.80x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 323 ms: 1.54x faster                                                        |
| gc_traversal               | 1.96 ms                                                     | 1.31 ms: 1.50x faster                                                       |
| async_tree_io              | 513 ms                                                      | 344 ms: 1.49x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 191 ms: 1.47x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 145 ms: 1.38x faster                                                        |
| mdp                        | 1.43 sec                                                    | 1.05 sec: 1.36x faster                                                      |
| async_tree_none            | 219 ms                                                      | 169 ms: 1.30x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 303 ms: 1.26x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 18.6 us: 1.24x faster                                                       |
| deepcopy                   | 223 us                                                      | 183 us: 1.22x faster                                                        |
| create_gc_cycles           | 1.22 ms                                                     | 1.03 ms: 1.19x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.34 us: 1.18x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 324 ms: 1.18x faster                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 74.2 ms: 1.14x faster                                                       |
| float                      | 50.8 ms                                                     | 46.2 ms: 1.10x faster                                                       |
| json                       | 3.30 ms                                                     | 3.03 ms: 1.09x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.57 ms: 1.08x faster                                                       |
| pidigits                   | 146 ms                                                      | 136 ms: 1.08x faster                                                        |
| json_dumps                 | 6.19 ms                                                     | 5.97 ms: 1.04x faster                                                       |
| regex_dna                  | 115 ms                                                      | 112 ms: 1.03x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.96 us: 1.03x faster                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 59.9 ms: 1.01x faster                                                       |
| dulwich_log                | 40.1 ms                                                     | 40.8 ms: 1.02x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 39.0 ms: 1.02x slower                                                       |
| 2to3                       | 215 ms                                                      | 220 ms: 1.02x slower                                                        |
| telco                      | 4.85 ms                                                     | 5.02 ms: 1.04x slower                                                       |
| sphinx                     | 617 ms                                                      | 643 ms: 1.04x slower                                                        |
| json_loads                 | 15.1 us                                                     | 15.9 us: 1.05x slower                                                       |
| go                         | 84.7 ms                                                     | 89.4 ms: 1.06x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.9 ms: 1.06x slower                                                       |
| scimark_fft                | 175 ms                                                      | 187 ms: 1.07x slower                                                        |
| pyflate                    | 283 ms                                                      | 307 ms: 1.09x slower                                                        |
| scimark_sor                | 76.2 ms                                                     | 83.3 ms: 1.09x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 59.9 ns: 1.10x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.10x slower                                                       |
| sympy_expand               | 286 ms                                                      | 315 ms: 1.10x slower                                                        |
| generators                 | 19.0 ms                                                     | 21.0 ms: 1.10x slower                                                       |
| sympy_str                  | 167 ms                                                      | 185 ms: 1.11x slower                                                        |
| pprint_safe_repr           | 485 ms                                                      | 536 ms: 1.11x slower                                                        |
| scimark_lu                 | 56.7 ms                                                     | 63.0 ms: 1.11x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.5 us: 1.11x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 94.7 ms: 1.11x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 37.7 ms: 1.11x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 89.8 ms: 1.11x slower                                                       |
| spectral_norm              | 63.4 ms                                                     | 70.8 ms: 1.12x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.8 ms: 1.12x slower                                                       |
| async_generators           | 223 ms                                                      | 252 ms: 1.13x slower                                                        |
| logging_simple             | 5.77 us                                                     | 6.53 us: 1.13x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.2 ms: 1.14x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 148 us: 1.14x slower                                                        |
| logging_format             | 6.18 us                                                     | 7.04 us: 1.14x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.39 ms: 1.14x slower                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 3.00 ms: 1.15x slower                                                       |
| nbody                      | 66.3 ms                                                     | 76.7 ms: 1.16x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 61.9 ms: 1.16x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 85.1 ms: 1.18x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 43.2 ms: 1.18x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 223 us: 1.20x slower                                                        |
| genshi_text                | 15.2 ms                                                     | 18.3 ms: 1.20x slower                                                       |
| chaos                      | 37.9 ms                                                     | 45.6 ms: 1.20x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 49.4 ms: 1.21x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 126 us: 1.22x slower                                                        |
| fannkuch                   | 252 ms                                                      | 310 ms: 1.23x slower                                                        |
| crypto_pyaes               | 45.6 ms                                                     | 56.3 ms: 1.23x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.35 ms: 1.24x slower                                                       |
| richards                   | 26.3 ms                                                     | 32.9 ms: 1.25x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 1.02 ms: 1.26x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 71.4 ms: 1.27x slower                                                       |
| django_template            | 20.3 ms                                                     | 26.1 ms: 1.29x slower                                                       |
| richards_super             | 29.8 ms                                                     | 38.5 ms: 1.29x slower                                                       |
| raytrace                   | 153 ms                                                      | 208 ms: 1.35x slower                                                        |
| coverage                   | 45.3 ms                                                     | 67.1 ms: 1.48x slower                                                       |
| mako                       | 6.56 ms                                                     | 10.1 ms: 1.54x slower                                                       |
| k_core                     | 1.70 sec                                                    | 2.66 sec: 1.57x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.62 sec: 1.66x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 2.32 sec: 1.69x slower                                                      |
| many_optionals             | 361 us                                                      | 628 us: 1.74x slower                                                        |
| shortest_path              | 355 ms                                                      | 650 ms: 1.83x slower                                                        |
| docutils                   | 1.53 sec                                                    | 2.82 sec: 1.84x slower                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 5.44 sec: 1.89x slower                                                      |
| connected_components       | 320 ms                                                      | 613 ms: 1.92x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 35.1 ms: 3.24x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                                |

Benchmark hidden because not significant (3): pylint, xml_etree_parse, pycparser
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251019-3.15.0a1+-bedaea0-NOGIL/bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.038x slower

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown