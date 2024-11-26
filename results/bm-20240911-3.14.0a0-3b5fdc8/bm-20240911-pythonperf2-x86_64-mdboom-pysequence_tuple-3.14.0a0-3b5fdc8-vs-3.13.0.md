# Results vs. 3.13.0

- fork: mdboom
- ref: pysequence_tuple
- machine: linux-x86_64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.028x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 287 ms: 1.02x faster                                                    |
| docutils       | 2.81 sec                                                     | 2.91 sec: 1.04x slower                                                  |
| Geometric mean | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 392 ms: 1.17x faster                                                    |
| async_tree_none            | 370 ms                                                       | 326 ms: 1.14x faster                                                    |
| async_tree_memoization     | 447 ms                                                       | 403 ms: 1.11x faster                                                    |
| async_tree_none_tg         | 342 ms                                                       | 312 ms: 1.10x faster                                                    |
| async_tree_io_tg           | 823 ms                                                       | 784 ms: 1.05x faster                                                    |
| async_tree_io              | 832 ms                                                       | 807 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 580 ms: 1.03x faster                                                    |
| async_generators           | 364 ms                                                       | 360 ms: 1.01x faster                                                    |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 570 ms: 1.01x faster                                                    |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 85.3 ms: 1.08x faster                                                   |
| float          | 81.6 ms                                                      | 80.4 ms: 1.02x faster                                                   |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                        | 1.03x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 140 ms: 1.02x faster                                                    |
| regex_effbot   | 3.51 ms                                                      | 3.46 ms: 1.01x faster                                                   |
| regex_dna      | 238 ms                                                       | 240 ms: 1.01x slower                                                    |
| regex_v8       | 24.9 ms                                                      | 25.8 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                        | 1.00x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_process    | 60.7 ms                                                      | 59.2 ms: 1.03x faster                                                   |
| pickle_pure_python   | 322 us                                                       | 315 us: 1.02x faster                                                    |
| json_loads           | 24.7 us                                                      | 24.9 us: 1.01x slower                                                   |
| xml_etree_iterparse  | 99.8 ms                                                      | 101 ms: 1.02x slower                                                    |
| json_dumps           | 10.8 ms                                                      | 11.1 ms: 1.03x slower                                                   |
| unpickle_pure_python | 216 us                                                       | 226 us: 1.04x slower                                                    |
| tomli_loads          | 2.43 sec                                                     | 2.56 sec: 1.05x slower                                                  |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                   |
| python_startup_no_site | 8.93 ms                                                      | 8.95 ms: 1.00x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.08x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                                   |
| genshi_xml      | 58.0 ms                                                      | 54.2 ms: 1.07x faster                                                   |
| django_template | 38.9 ms                                                      | 41.3 ms: 1.06x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 2.65 ms                                                      | 1.95 ms: 1.36x faster                                                   |
| deepcopy                   | 388 us                                                       | 287 us: 1.35x faster                                                    |
| deepcopy_memo              | 38.9 us                                                      | 29.7 us: 1.31x faster                                                   |
| deepcopy_reduce            | 3.49 us                                                      | 2.87 us: 1.22x faster                                                   |
| go                         | 167 ms                                                       | 139 ms: 1.20x faster                                                    |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                   |
| async_tree_memoization_tg  | 458 ms                                                       | 392 ms: 1.17x faster                                                    |
| generators                 | 33.9 ms                                                      | 29.7 ms: 1.14x faster                                                   |
| async_tree_none            | 370 ms                                                       | 326 ms: 1.14x faster                                                    |
| pathlib                    | 17.4 ms                                                      | 15.6 ms: 1.11x faster                                                   |
| async_tree_memoization     | 447 ms                                                       | 403 ms: 1.11x faster                                                    |
| async_tree_none_tg         | 342 ms                                                       | 312 ms: 1.10x faster                                                    |
| coverage                   | 84.5 ms                                                      | 77.4 ms: 1.09x faster                                                   |
| bench_thread_pool          | 929 us                                                       | 859 us: 1.08x faster                                                    |
| nbody                      | 92.1 ms                                                      | 85.3 ms: 1.08x faster                                                   |
| genshi_text                | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                                   |
| genshi_xml                 | 58.0 ms                                                      | 54.2 ms: 1.07x faster                                                   |
| json                       | 5.62 ms                                                      | 5.26 ms: 1.07x faster                                                   |
| scimark_sor                | 125 ms                                                       | 118 ms: 1.06x faster                                                    |
| thrift                     | 918 us                                                       | 868 us: 1.06x faster                                                    |
| telco                      | 8.77 ms                                                      | 8.35 ms: 1.05x faster                                                   |
| async_tree_io_tg           | 823 ms                                                       | 784 ms: 1.05x faster                                                    |
| richards_super             | 60.2 ms                                                      | 57.9 ms: 1.04x faster                                                   |
| async_tree_io              | 832 ms                                                       | 807 ms: 1.03x faster                                                    |
| hexiom                     | 6.47 ms                                                      | 6.29 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 580 ms: 1.03x faster                                                    |
| meteor_contest             | 130 ms                                                       | 127 ms: 1.03x faster                                                    |
| xml_etree_process          | 60.7 ms                                                      | 59.2 ms: 1.03x faster                                                   |
| bpe_tokeniser              | 5.09 sec                                                     | 4.97 sec: 1.03x faster                                                  |
| pprint_safe_repr           | 835 ms                                                       | 816 ms: 1.02x faster                                                    |
| pickle_pure_python         | 322 us                                                       | 315 us: 1.02x faster                                                    |
| 2to3                       | 293 ms                                                       | 287 ms: 1.02x faster                                                    |
| pprint_pformat             | 1.70 sec                                                     | 1.67 sec: 1.02x faster                                                  |
| regex_compile              | 143 ms                                                       | 140 ms: 1.02x faster                                                    |
| nqueens                    | 92.3 ms                                                      | 90.5 ms: 1.02x faster                                                   |
| typing_runtime_protocols   | 176 us                                                       | 172 us: 1.02x faster                                                    |
| pycparser                  | 1.28 sec                                                     | 1.26 sec: 1.02x faster                                                  |
| pyflate                    | 493 ms                                                       | 484 ms: 1.02x faster                                                    |
| float                      | 81.6 ms                                                      | 80.4 ms: 1.02x faster                                                   |
| regex_effbot               | 3.51 ms                                                      | 3.46 ms: 1.01x faster                                                   |
| gc_traversal               | 4.48 ms                                                      | 4.42 ms: 1.01x faster                                                   |
| sympy_str                  | 297 ms                                                       | 293 ms: 1.01x faster                                                    |
| crypto_pyaes               | 73.5 ms                                                      | 72.6 ms: 1.01x faster                                                   |
| async_generators           | 364 ms                                                       | 360 ms: 1.01x faster                                                    |
| richards                   | 52.5 ms                                                      | 52.0 ms: 1.01x faster                                                   |
| sympy_integrate            | 23.4 ms                                                      | 23.2 ms: 1.01x faster                                                   |
| mdp                        | 2.53 sec                                                     | 2.51 sec: 1.01x faster                                                  |
| sqlglot_normalize          | 119 ms                                                       | 118 ms: 1.01x faster                                                    |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 570 ms: 1.01x faster                                                    |
| sympy_expand               | 506 ms                                                       | 504 ms: 1.01x faster                                                    |
| spectral_norm              | 97.4 ms                                                      | 97.1 ms: 1.00x faster                                                   |
| sqlglot_optimize           | 58.7 ms                                                      | 58.5 ms: 1.00x faster                                                   |
| python_startup_no_site     | 8.93 ms                                                      | 8.95 ms: 1.00x slower                                                   |
| scimark_lu                 | 97.4 ms                                                      | 98.1 ms: 1.01x slower                                                   |
| comprehensions             | 17.3 us                                                      | 17.4 us: 1.01x slower                                                   |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                    |
| regex_dna                  | 238 ms                                                       | 240 ms: 1.01x slower                                                    |
| json_loads                 | 24.7 us                                                      | 24.9 us: 1.01x slower                                                   |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.25 ms: 1.01x slower                                                   |
| logging_silent             | 97.5 ns                                                      | 98.8 ns: 1.01x slower                                                   |
| xml_etree_iterparse        | 99.8 ms                                                      | 101 ms: 1.02x slower                                                    |
| scimark_fft                | 298 ms                                                       | 305 ms: 1.02x slower                                                    |
| logging_format             | 6.95 us                                                      | 7.12 us: 1.02x slower                                                   |
| dulwich_log                | 65.5 ms                                                      | 67.2 ms: 1.03x slower                                                   |
| json_dumps                 | 10.8 ms                                                      | 11.1 ms: 1.03x slower                                                   |
| logging_simple             | 6.28 us                                                      | 6.47 us: 1.03x slower                                                   |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                                   |
| docutils                   | 2.81 sec                                                     | 2.91 sec: 1.04x slower                                                  |
| regex_v8                   | 24.9 ms                                                      | 25.8 ms: 1.04x slower                                                   |
| deltablue                  | 3.38 ms                                                      | 3.51 ms: 1.04x slower                                                   |
| raytrace                   | 267 ms                                                       | 278 ms: 1.04x slower                                                    |
| unpickle_pure_python       | 216 us                                                       | 226 us: 1.04x slower                                                    |
| sqlglot_transpile          | 1.76 ms                                                      | 1.84 ms: 1.04x slower                                                   |
| chaos                      | 60.6 ms                                                      | 63.2 ms: 1.04x slower                                                   |
| scimark_monte_carlo        | 65.2 ms                                                      | 68.3 ms: 1.05x slower                                                   |
| tomli_loads                | 2.43 sec                                                     | 2.56 sec: 1.05x slower                                                  |
| django_template            | 38.9 ms                                                      | 41.3 ms: 1.06x slower                                                   |
| sqlglot_parse              | 1.37 ms                                                      | 1.46 ms: 1.07x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                            |

Benchmark hidden because not significant (10): bench_mp_pool, fannkuch, asyncio_websockets, tornado_http, xml_etree_parse, sympy_sum, html5lib, xml_etree_generate, mako, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240911-3.14.0a0-3b5fdc8/bm-20240911-pythonperf2-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.028x faster
# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x