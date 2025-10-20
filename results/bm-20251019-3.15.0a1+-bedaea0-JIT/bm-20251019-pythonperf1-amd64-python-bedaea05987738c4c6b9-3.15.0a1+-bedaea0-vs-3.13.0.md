# Results vs. 3.13.0

- fork: python
- ref: bedaea05987738c4c6b9
- machine: windows-amd64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.104x faster
- HPT reliability: 99.74%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 1.53 sec                                                    | 1.61 sec: 1.05x slower                                                      |
| html5lib       | 38.2 ms                                                     | 37.4 ms: 1.02x faster                                                       |
| sphinx         | 617 ms                                                      | 627 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 143 ms: 2.10x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.33x faster                                                        |
| async_tree_io              | 513 ms                                                      | 386 ms: 1.33x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 377 ms: 1.32x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 201 ms: 1.32x faster                                                        |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.28x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 165 ms: 1.21x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 333 ms: 1.15x faster                                                        |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 14.2 ms: 1.14x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.24x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 40.8 ms: 1.25x faster                                                       |
| nbody          | 66.3 ms                                                     | 54.6 ms: 1.21x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.4 ms: 1.78x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.52 ms: 1.11x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 77.6 ms: 1.04x faster                                                       |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.09 sec: 1.26x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 104 us: 1.25x faster                                                        |
| json_dumps           | 6.19 ms                                                     | 5.51 ms: 1.12x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 84.9 ms: 1.09x faster                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 49.5 ms: 1.08x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.1 us: 1.07x faster                                                       |
| xml_etree_process    | 36.5 ms                                                     | 35.6 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 60.1 ms: 1.01x faster                                                       |
| pickle_pure_python   | 186 us                                                      | 198 us: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.2 ms: 1.03x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 18.8 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.32 ms: 1.23x faster                                                       |
| genshi_text     | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                       |
| django_template | 20.3 ms                                                     | 23.8 ms: 1.17x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 495 us: 17.11x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 29.2 ms: 2.58x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 143 ms: 2.10x faster                                                        |
| mdp                        | 1.43 sec                                                    | 781 ms: 1.83x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 13.4 ms: 1.78x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 16.9 us: 1.37x faster                                                       |
| deepcopy                   | 223 us                                                      | 163 us: 1.37x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.33x faster                                                        |
| async_tree_io              | 513 ms                                                      | 386 ms: 1.33x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 377 ms: 1.32x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 201 ms: 1.32x faster                                                        |
| scimark_fft                | 175 ms                                                      | 134 ms: 1.31x faster                                                        |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.28x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.09 sec: 1.26x faster                                                      |
| unpickle_pure_python       | 130 us                                                      | 104 us: 1.25x faster                                                        |
| telco                      | 4.85 ms                                                     | 3.88 ms: 1.25x faster                                                       |
| float                      | 50.8 ms                                                     | 40.8 ms: 1.25x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.32 ms: 1.23x faster                                                       |
| nbody                      | 66.3 ms                                                     | 54.6 ms: 1.21x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 165 ms: 1.21x faster                                                        |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.16 ms: 1.20x faster                                                       |
| fannkuch                   | 252 ms                                                      | 211 ms: 1.19x faster                                                        |
| json                       | 3.30 ms                                                     | 2.83 ms: 1.16x faster                                                       |
| pprint_safe_repr           | 485 ms                                                      | 416 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 333 ms: 1.15x faster                                                        |
| pprint_pformat             | 977 ms                                                      | 850 ms: 1.15x faster                                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 2.54 sec: 1.13x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.80 us: 1.13x faster                                                       |
| json_dumps                 | 6.19 ms                                                     | 5.51 ms: 1.12x faster                                                       |
| pyflate                    | 283 ms                                                      | 252 ms: 1.12x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.52 ms: 1.11x faster                                                       |
| go                         | 84.7 ms                                                     | 76.4 ms: 1.11x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 84.9 ms: 1.09x faster                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 49.5 ms: 1.08x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.1 us: 1.07x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.59 sec: 1.07x faster                                                      |
| pylint                     | 205 ms                                                      | 193 ms: 1.06x faster                                                        |
| regex_compile              | 80.7 ms                                                     | 77.6 ms: 1.04x faster                                                       |
| pycparser                  | 695 ms                                                      | 670 ms: 1.04x faster                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.53 us: 1.04x faster                                                       |
| shortest_path              | 355 ms                                                      | 343 ms: 1.04x faster                                                        |
| xml_etree_process          | 36.5 ms                                                     | 35.6 ms: 1.03x faster                                                       |
| typing_runtime_protocols   | 103 us                                                      | 101 us: 1.03x faster                                                        |
| connected_components       | 320 ms                                                      | 313 ms: 1.02x faster                                                        |
| html5lib                   | 38.2 ms                                                     | 37.4 ms: 1.02x faster                                                       |
| dulwich_log                | 40.1 ms                                                     | 39.3 ms: 1.02x faster                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 44.8 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 60.1 ms: 1.01x faster                                                       |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.01x faster                                                        |
| spectral_norm              | 63.4 ms                                                     | 63.0 ms: 1.01x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 76.7 ms: 1.01x slower                                                       |
| sympy_expand               | 286 ms                                                      | 289 ms: 1.01x slower                                                        |
| sympy_integrate            | 12.3 ms                                                     | 12.5 ms: 1.01x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 41.3 ms: 1.01x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.2 ms: 1.01x slower                                                       |
| sphinx                     | 617 ms                                                      | 627 ms: 1.02x slower                                                        |
| create_gc_cycles           | 1.22 ms                                                     | 1.25 ms: 1.02x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 57.8 ms: 1.02x slower                                                       |
| comprehensions             | 10.4 us                                                     | 10.7 us: 1.03x slower                                                       |
| richards                   | 26.3 ms                                                     | 27.0 ms: 1.03x slower                                                       |
| richards_super             | 29.8 ms                                                     | 30.7 ms: 1.03x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 56.4 ns: 1.03x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.2 ms: 1.03x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 841 us: 1.04x slower                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 88.5 ms: 1.05x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.61 sec: 1.05x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.07 ms: 1.06x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.09 ms: 1.06x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.13 us: 1.06x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 198 us: 1.07x slower                                                        |
| logging_format             | 6.18 us                                                     | 6.58 us: 1.07x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 60.4 ms: 1.08x slower                                                       |
| chaos                      | 37.9 ms                                                     | 41.1 ms: 1.09x slower                                                       |
| async_generators           | 223 ms                                                      | 248 ms: 1.11x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 18.8 ms: 1.11x slower                                                       |
| coverage                   | 45.3 ms                                                     | 51.3 ms: 1.13x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.2 ms: 1.14x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.18 ms: 1.15x slower                                                       |
| raytrace                   | 153 ms                                                      | 179 ms: 1.17x slower                                                        |
| django_template            | 20.3 ms                                                     | 23.8 ms: 1.17x slower                                                       |
| many_optionals             | 361 us                                                      | 575 us: 1.59x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 31.3 ms: 2.88x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.10x faster                                                                |

Benchmark hidden because not significant (6): sympy_str, meteor_contest, sympy_sum, pidigits, 2to3, genshi_xml
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251019-3.15.0a1+-bedaea0-JIT/bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.104x faster

# HPT report

- Reliability score: 99.74% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown