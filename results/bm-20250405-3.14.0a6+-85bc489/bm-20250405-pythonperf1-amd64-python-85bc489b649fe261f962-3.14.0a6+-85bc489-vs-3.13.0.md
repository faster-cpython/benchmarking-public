# Results vs. 3.13.0

- fork: python
- ref: 85bc489b649fe261f962
- machine: windows-amd64
- commit hash: 85bc489
- commit date: 2025-04-05
- overall geometric mean: 1.040x faster
- HPT reliability: 61.13%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 220 ms: 1.02x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                                      |
| sphinx         | 617 ms                                                      | 638 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 203 ms: 1.30x faster                                                        |
| async_tree_io              | 513 ms                                                      | 404 ms: 1.27x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 391 ms: 1.27x faster                                                        |
| async_tree_none            | 219 ms                                                      | 179 ms: 1.23x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.18x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 334 ms: 1.15x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.23x faster                                                                |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 42.2 ms: 1.21x faster                                                       |
| nbody          | 66.3 ms                                                     | 62.6 ms: 1.06x faster                                                       |
| pidigits       | 146 ms                                                      | 147 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.3 ms: 1.67x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 79.4 ms: 1.02x faster                                                       |
| regex_dna      | 115 ms                                                      | 118 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 88.5 ms: 1.04x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.6 us: 1.03x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.33 sec: 1.03x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 134 us: 1.03x slower                                                        |
| xml_etree_generate   | 53.5 ms                                                     | 55.3 ms: 1.04x slower                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.7 ms: 1.04x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.49 ms: 1.05x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 39.1 ms: 1.07x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 207 us: 1.11x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.0 ms: 1.07x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 20.6 ms: 1.22x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.47 ms: 1.01x faster                                                       |
| genshi_text     | 15.2 ms                                                     | 15.1 ms: 1.01x faster                                                       |
| django_template | 20.3 ms                                                     | 25.0 ms: 1.23x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 32.0 ms: 2.36x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                                        |
| mdp                        | 1.43 sec                                                    | 793 ms: 1.81x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 14.3 ms: 1.67x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                        |
| deepcopy                   | 223 us                                                      | 171 us: 1.31x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 203 ms: 1.30x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 18.1 us: 1.28x faster                                                       |
| async_tree_io              | 513 ms                                                      | 404 ms: 1.27x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 391 ms: 1.27x faster                                                        |
| async_tree_none            | 219 ms                                                      | 179 ms: 1.23x faster                                                        |
| float                      | 50.8 ms                                                     | 42.2 ms: 1.21x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.18x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 334 ms: 1.15x faster                                                        |
| spectral_norm              | 63.4 ms                                                     | 55.5 ms: 1.14x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.79 us: 1.13x faster                                                       |
| go                         | 84.7 ms                                                     | 76.3 ms: 1.11x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.44 ms: 1.07x faster                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 38.2 ms: 1.07x faster                                                       |
| nbody                      | 66.3 ms                                                     | 62.6 ms: 1.06x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.62 ms: 1.05x faster                                                       |
| pylint                     | 205 ms                                                      | 196 ms: 1.05x faster                                                        |
| json                       | 3.30 ms                                                     | 3.15 ms: 1.05x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 88.5 ms: 1.04x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 73.8 ms: 1.03x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.6 us: 1.03x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.33 sec: 1.03x faster                                                      |
| scimark_fft                | 175 ms                                                      | 171 ms: 1.02x faster                                                        |
| regex_compile              | 80.7 ms                                                     | 79.4 ms: 1.02x faster                                                       |
| mako                       | 6.56 ms                                                     | 6.47 ms: 1.01x faster                                                       |
| genshi_text                | 15.2 ms                                                     | 15.1 ms: 1.01x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.57 us: 1.01x faster                                                       |
| fannkuch                   | 252 ms                                                      | 250 ms: 1.01x faster                                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 2.88 sec: 1.00x slower                                                      |
| pidigits                   | 146 ms                                                      | 147 ms: 1.01x slower                                                        |
| typing_runtime_protocols   | 103 us                                                      | 104 us: 1.01x slower                                                        |
| crypto_pyaes               | 45.6 ms                                                     | 46.0 ms: 1.01x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 55.0 ns: 1.01x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.4 ms: 1.01x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 57.5 ms: 1.01x slower                                                       |
| connected_components       | 320 ms                                                      | 324 ms: 1.01x slower                                                        |
| create_gc_cycles           | 1.22 ms                                                     | 1.24 ms: 1.02x slower                                                       |
| sympy_expand               | 286 ms                                                      | 291 ms: 1.02x slower                                                        |
| sympy_str                  | 167 ms                                                      | 170 ms: 1.02x slower                                                        |
| chaos                      | 37.9 ms                                                     | 38.7 ms: 1.02x slower                                                       |
| 2to3                       | 215 ms                                                      | 220 ms: 1.02x slower                                                        |
| meteor_contest             | 72.0 ms                                                     | 73.7 ms: 1.02x slower                                                       |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.03x slower                                                        |
| unpickle_pure_python       | 130 us                                                      | 134 us: 1.03x slower                                                        |
| hexiom                     | 3.84 ms                                                     | 3.96 ms: 1.03x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.6 ms: 1.03x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.01 sec: 1.03x slower                                                      |
| sphinx                     | 617 ms                                                      | 638 ms: 1.03x slower                                                        |
| xml_etree_generate         | 53.5 ms                                                     | 55.3 ms: 1.04x slower                                                       |
| richards                   | 26.3 ms                                                     | 27.2 ms: 1.04x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.7 ms: 1.04x slower                                                       |
| richards_super             | 29.8 ms                                                     | 30.9 ms: 1.04x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.04 ms: 1.04x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 88.8 ms: 1.04x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 41.9 ms: 1.05x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 88.3 ms: 1.05x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.49 ms: 1.05x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 850 us: 1.05x slower                                                        |
| python_startup             | 24.4 ms                                                     | 26.0 ms: 1.07x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 39.1 ms: 1.07x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                                      |
| coverage                   | 45.3 ms                                                     | 48.6 ms: 1.07x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 60.5 ms: 1.08x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.23 us: 1.08x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.3 us: 1.09x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.74 us: 1.09x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 207 us: 1.11x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.13 ms: 1.13x slower                                                       |
| raytrace                   | 153 ms                                                      | 173 ms: 1.13x slower                                                        |
| many_optionals             | 361 us                                                      | 427 us: 1.18x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 20.6 ms: 1.22x slower                                                       |
| django_template            | 20.3 ms                                                     | 25.0 ms: 1.23x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 15.9 ms: 1.47x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (8): genshi_xml, k_core, pyflate, html5lib, async_generators, shortest_path, pprint_safe_repr, pycparser
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250405-3.14.0a6+-85bc489/bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 61.13% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown