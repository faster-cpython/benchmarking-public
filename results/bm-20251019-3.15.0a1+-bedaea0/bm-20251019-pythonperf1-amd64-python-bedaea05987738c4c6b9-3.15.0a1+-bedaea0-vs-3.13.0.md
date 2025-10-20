# Results vs. 3.13.0

- fork: python
- ref: bedaea05987738c4c6b9
- machine: windows-amd64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.078x faster
- HPT reliability: 87.52%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 1.53 sec                                                    | 1.58 sec: 1.03x slower                                                      |
| html5lib       | 38.2 ms                                                     | 37.2 ms: 1.03x faster                                                       |
| sphinx         | 617 ms                                                      | 626 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 147 ms: 2.04x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                        |
| async_tree_io              | 513 ms                                                      | 387 ms: 1.33x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 378 ms: 1.32x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 202 ms: 1.31x faster                                                        |
| async_tree_none            | 219 ms                                                      | 173 ms: 1.26x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 166 ms: 1.21x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 333 ms: 1.15x faster                                                        |
| async_generators           | 223 ms                                                      | 234 ms: 1.05x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.16x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.24x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.4 ms: 1.15x faster                                                       |
| nbody          | 66.3 ms                                                     | 62.9 ms: 1.05x faster                                                       |
| pidigits       | 146 ms                                                      | 146 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.0 ms: 1.71x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.56 ms: 1.08x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 78.8 ms: 1.02x faster                                                       |
| regex_dna      | 115 ms                                                      | 122 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 6.19 ms                                                     | 5.44 ms: 1.14x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 86.3 ms: 1.07x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.2 us: 1.06x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.32 sec: 1.04x faster                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 61.6 ms: 1.02x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 133 us: 1.02x slower                                                        |
| xml_etree_generate   | 53.5 ms                                                     | 55.6 ms: 1.04x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 39.0 ms: 1.07x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 206 us: 1.11x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.2 ms: 1.14x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.63 ms: 1.01x slower                                                       |
| django_template | 20.3 ms                                                     | 23.0 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 494 us: 17.15x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 28.5 ms: 2.64x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 147 ms: 2.04x faster                                                        |
| mdp                        | 1.43 sec                                                    | 813 ms: 1.76x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 14.0 ms: 1.71x faster                                                       |
| deepcopy                   | 223 us                                                      | 163 us: 1.37x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 16.9 us: 1.36x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                        |
| async_tree_io              | 513 ms                                                      | 387 ms: 1.33x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 378 ms: 1.32x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 202 ms: 1.31x faster                                                        |
| async_tree_none            | 219 ms                                                      | 173 ms: 1.26x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 166 ms: 1.21x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.75 us: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 333 ms: 1.15x faster                                                        |
| telco                      | 4.85 ms                                                     | 4.23 ms: 1.15x faster                                                       |
| float                      | 50.8 ms                                                     | 44.4 ms: 1.15x faster                                                       |
| json                       | 3.30 ms                                                     | 2.89 ms: 1.14x faster                                                       |
| json_dumps                 | 6.19 ms                                                     | 5.44 ms: 1.14x faster                                                       |
| go                         | 84.7 ms                                                     | 75.7 ms: 1.12x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.56 ms: 1.08x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.44 ms: 1.07x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 86.3 ms: 1.07x faster                                                       |
| pylint                     | 205 ms                                                      | 193 ms: 1.07x faster                                                        |
| json_loads                 | 15.1 us                                                     | 14.2 us: 1.06x faster                                                       |
| nbody                      | 66.3 ms                                                     | 62.9 ms: 1.05x faster                                                       |
| scimark_fft                | 175 ms                                                      | 168 ms: 1.04x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.32 sec: 1.04x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 61.1 ms: 1.04x faster                                                       |
| scimark_lu                 | 56.7 ms                                                     | 54.6 ms: 1.04x faster                                                       |
| sympy_expand               | 286 ms                                                      | 276 ms: 1.03x faster                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.54 us: 1.03x faster                                                       |
| dulwich_log                | 40.1 ms                                                     | 39.0 ms: 1.03x faster                                                       |
| pyflate                    | 283 ms                                                      | 276 ms: 1.03x faster                                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.7 ms: 1.03x faster                                                       |
| html5lib                   | 38.2 ms                                                     | 37.2 ms: 1.03x faster                                                       |
| regex_compile              | 80.7 ms                                                     | 78.8 ms: 1.02x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.66 sec: 1.02x faster                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.1 ms: 1.02x faster                                                       |
| meteor_contest             | 72.0 ms                                                     | 70.7 ms: 1.02x faster                                                       |
| sympy_str                  | 167 ms                                                      | 165 ms: 1.01x faster                                                        |
| scimark_sor                | 76.2 ms                                                     | 75.9 ms: 1.00x faster                                                       |
| pidigits                   | 146 ms                                                      | 146 ms: 1.00x faster                                                        |
| pprint_safe_repr           | 485 ms                                                      | 489 ms: 1.01x slower                                                        |
| generators                 | 19.0 ms                                                     | 19.2 ms: 1.01x slower                                                       |
| mako                       | 6.56 ms                                                     | 6.63 ms: 1.01x slower                                                       |
| richards                   | 26.3 ms                                                     | 26.6 ms: 1.01x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.91 sec: 1.01x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 55.3 ns: 1.01x slower                                                       |
| sphinx                     | 617 ms                                                      | 626 ms: 1.01x slower                                                        |
| crypto_pyaes               | 45.6 ms                                                     | 46.4 ms: 1.02x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 995 ms: 1.02x slower                                                        |
| xml_etree_iterparse        | 60.5 ms                                                     | 61.6 ms: 1.02x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 133 us: 1.02x slower                                                        |
| connected_components       | 320 ms                                                      | 327 ms: 1.02x slower                                                        |
| logging_simple             | 5.77 us                                                     | 5.91 us: 1.02x slower                                                       |
| richards_super             | 29.8 ms                                                     | 30.5 ms: 1.02x slower                                                       |
| fannkuch                   | 252 ms                                                      | 258 ms: 1.03x slower                                                        |
| chaos                      | 37.9 ms                                                     | 38.9 ms: 1.03x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.39 us: 1.03x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.58 sec: 1.03x slower                                                      |
| comprehensions             | 10.4 us                                                     | 10.8 us: 1.04x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 3.99 ms: 1.04x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.27 ms: 1.04x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 55.6 ms: 1.04x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.06 ms: 1.05x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 88.4 ms: 1.05x slower                                                       |
| async_generators           | 223 ms                                                      | 234 ms: 1.05x slower                                                        |
| regex_dna                  | 115 ms                                                      | 122 ms: 1.06x slower                                                        |
| coverage                   | 45.3 ms                                                     | 48.4 ms: 1.07x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 39.0 ms: 1.07x slower                                                       |
| python_startup             | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 60.5 ms: 1.08x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 206 us: 1.11x slower                                                        |
| django_template            | 20.3 ms                                                     | 23.0 ms: 1.14x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.2 ms: 1.14x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.16 ms: 1.14x slower                                                       |
| raytrace                   | 153 ms                                                      | 177 ms: 1.15x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.16x slower                                                       |
| many_optionals             | 361 us                                                      | 560 us: 1.55x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 31.1 ms: 2.86x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                                |

Benchmark hidden because not significant (8): genshi_xml, genshi_text, sympy_sum, pycparser, shortest_path, 2to3, typing_runtime_protocols, bench_thread_pool
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251019-3.15.0a1+-bedaea0/bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.078x faster

# HPT report

- Reliability score: 87.52% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown