# Results vs. 3.13.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: windows-amd64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.023x faster
- HPT reliability: 93.16%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 229 ms: 1.06x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.75 sec: 1.14x slower                                                      |
| html5lib       | 38.2 ms                                                     | 41.2 ms: 1.08x slower                                                       |
| sphinx         | 617 ms                                                      | 671 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                       | 1.09x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.90x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                        |
| async_tree_io              | 513 ms                                                      | 417 ms: 1.23x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 412 ms: 1.21x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 221 ms: 1.20x faster                                                        |
| async_tree_none            | 219 ms                                                      | 188 ms: 1.17x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 337 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 177 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 336 ms: 1.13x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                       |
| async_generators           | 223 ms                                                      | 249 ms: 1.12x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 59.7 ms: 1.11x faster                                                       |
| float          | 50.8 ms                                                     | 48.3 ms: 1.05x faster                                                       |
| pidigits       | 146 ms                                                      | 149 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.8 ms: 1.73x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                       |
| regex_dna      | 115 ms                                                      | 118 ms: 1.03x slower                                                        |
| regex_compile  | 80.7 ms                                                     | 86.5 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.23 sec: 1.11x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 123 us: 1.06x faster                                                        |
| xml_etree_parse      | 92.2 ms                                                     | 89.0 ms: 1.04x faster                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 54.2 ms: 1.01x slower                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.4 ms: 1.03x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 38.3 ms: 1.05x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 7.04 ms: 1.14x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 217 us: 1.17x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.7 ms: 1.05x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 20.2 ms: 1.19x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.88 ms: 1.12x faster                                                       |
| genshi_text     | 15.2 ms                                                     | 17.4 ms: 1.14x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 40.8 ms: 1.20x slower                                                       |
| django_template | 20.3 ms                                                     | 26.6 ms: 1.31x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.13x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 525 us: 16.11x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 33.1 ms: 2.28x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.90x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 13.8 ms: 1.73x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                        |
| async_tree_io              | 513 ms                                                      | 417 ms: 1.23x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 412 ms: 1.21x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 221 ms: 1.20x faster                                                        |
| deepcopy                   | 223 us                                                      | 188 us: 1.19x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                       |
| async_tree_none            | 219 ms                                                      | 188 ms: 1.17x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 20.0 us: 1.16x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.27 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 337 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 177 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 336 ms: 1.13x faster                                                        |
| mako                       | 6.56 ms                                                     | 5.88 ms: 1.12x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.23 sec: 1.11x faster                                                      |
| nbody                      | 66.3 ms                                                     | 59.7 ms: 1.11x faster                                                       |
| scimark_fft                | 175 ms                                                      | 158 ms: 1.10x faster                                                        |
| json                       | 3.30 ms                                                     | 3.08 ms: 1.07x faster                                                       |
| unpickle_pure_python       | 130 us                                                      | 123 us: 1.06x faster                                                        |
| spectral_norm              | 63.4 ms                                                     | 60.2 ms: 1.05x faster                                                       |
| float                      | 50.8 ms                                                     | 48.3 ms: 1.05x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.63 ms: 1.05x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 89.0 ms: 1.04x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.79 sec: 1.03x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.54 us: 1.03x faster                                                       |
| pyflate                    | 283 ms                                                      | 276 ms: 1.03x faster                                                        |
| k_core                     | 1.70 sec                                                    | 1.66 sec: 1.02x faster                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.24 ms: 1.01x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 54.2 ms: 1.01x slower                                                       |
| pidigits                   | 146 ms                                                      | 149 ms: 1.02x slower                                                        |
| connected_components       | 320 ms                                                      | 325 ms: 1.02x slower                                                        |
| shortest_path              | 355 ms                                                      | 362 ms: 1.02x slower                                                        |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.03x slower                                                        |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.4 ms: 1.03x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.04 ms: 1.04x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 38.3 ms: 1.05x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.50 sec: 1.05x slower                                                      |
| python_startup             | 24.4 ms                                                     | 25.7 ms: 1.05x slower                                                       |
| go                         | 84.7 ms                                                     | 89.2 ms: 1.05x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 88.7 ms: 1.05x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 80.6 ms: 1.06x slower                                                       |
| generators                 | 19.0 ms                                                     | 20.1 ms: 1.06x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 76.3 ms: 1.06x slower                                                       |
| 2to3                       | 215 ms                                                      | 229 ms: 1.06x slower                                                        |
| scimark_lu                 | 56.7 ms                                                     | 60.5 ms: 1.07x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.04 sec: 1.07x slower                                                      |
| regex_compile              | 80.7 ms                                                     | 86.5 ms: 1.07x slower                                                       |
| pycparser                  | 695 ms                                                      | 746 ms: 1.07x slower                                                        |
| pprint_safe_repr           | 485 ms                                                      | 520 ms: 1.07x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 91.8 ms: 1.08x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 43.9 ms: 1.08x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 875 us: 1.08x slower                                                        |
| html5lib                   | 38.2 ms                                                     | 41.2 ms: 1.08x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 49.5 ms: 1.08x slower                                                       |
| sphinx                     | 617 ms                                                      | 671 ms: 1.09x slower                                                        |
| sympy_str                  | 167 ms                                                      | 182 ms: 1.09x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 43.9 ms: 1.10x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.5 ms: 1.10x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 62.3 ms: 1.11x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 115 us: 1.11x slower                                                        |
| coverage                   | 45.3 ms                                                     | 50.4 ms: 1.11x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                       |
| async_generators           | 223 ms                                                      | 249 ms: 1.12x slower                                                        |
| sympy_expand               | 286 ms                                                      | 322 ms: 1.13x slower                                                        |
| logging_silent             | 54.6 ns                                                     | 61.8 ns: 1.13x slower                                                       |
| richards                   | 26.3 ms                                                     | 29.8 ms: 1.14x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 7.04 ms: 1.14x slower                                                       |
| richards_super             | 29.8 ms                                                     | 33.9 ms: 1.14x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.75 sec: 1.14x slower                                                      |
| comprehensions             | 10.4 us                                                     | 11.9 us: 1.14x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 17.4 ms: 1.14x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.61 us: 1.15x slower                                                       |
| chaos                      | 37.9 ms                                                     | 43.8 ms: 1.16x slower                                                       |
| logging_format             | 6.18 us                                                     | 7.18 us: 1.16x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 217 us: 1.17x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 20.2 ms: 1.19x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 40.8 ms: 1.20x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.82 ms: 1.25x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.41 ms: 1.27x slower                                                       |
| many_optionals             | 361 us                                                      | 463 us: 1.28x slower                                                        |
| raytrace                   | 153 ms                                                      | 199 ms: 1.30x slower                                                        |
| django_template            | 20.3 ms                                                     | 26.6 ms: 1.31x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.8 ms: 1.55x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (4): json_loads, fannkuch, pylint, deepcopy_reduce
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.023x faster

# HPT report

- Reliability score: 93.16% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown