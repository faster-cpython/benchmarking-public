# Results vs. 3.13.0b2

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: linux-x86_64
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 281 ms: 1.04x faster                                                        |
| docutils       | 2.98 sec                                                         | 2.90 sec: 1.03x faster                                                      |
| html5lib       | 74.7 ms                                                          | 71.5 ms: 1.04x faster                                                       |
| tornado_http   | 119 ms                                                           | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                            | 1.04x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 460 ms                                                           | 400 ms: 1.15x faster                                                        |
| async_tree_none            | 365 ms                                                           | 322 ms: 1.14x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 795 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 310 ms: 1.10x faster                                                        |
| async_tree_io              | 873 ms                                                           | 803 ms: 1.09x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 391 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 545 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 575 ms: 1.05x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 78.3 ms: 1.02x faster                                                       |
| pidigits       | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 241 ms: 1.03x faster                                                        |
| regex_compile  | 144 ms                                                           | 140 ms: 1.03x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 25.5 ms: 1.02x faster                                                       |
| regex_effbot   | 3.40 ms                                                          | 3.64 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                            | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_list        | 4.70 us                                                          | 4.56 us: 1.03x faster                                                       |
| unpickle_pure_python | 224 us                                                           | 220 us: 1.02x faster                                                        |
| pickle_dict          | 32.8 us                                                          | 32.4 us: 1.01x faster                                                       |
| unpickle             | 15.7 us                                                          | 15.5 us: 1.01x faster                                                       |
| pickle               | 10.6 us                                                          | 10.5 us: 1.01x faster                                                       |
| xml_etree_generate   | 85.7 ms                                                          | 85.6 ms: 1.00x faster                                                       |
| xml_etree_process    | 59.7 ms                                                          | 59.9 ms: 1.00x slower                                                       |
| json_dumps           | 10.8 ms                                                          | 10.8 ms: 1.00x slower                                                       |
| pickle_list          | 4.44 us                                                          | 4.50 us: 1.01x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 317 us: 1.03x slower                                                        |
| tomli_loads          | 2.40 sec                                                         | 2.53 sec: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                            | 1.00x slower                                                                |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.85 ms                                                          | 8.94 ms: 1.01x slower                                                       |
| python_startup         | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 54.6 ms: 1.06x faster                                                       |
| genshi_text     | 25.9 ms                                                          | 24.9 ms: 1.04x faster                                                       |
| django_template | 39.0 ms                                                          | 38.3 ms: 1.02x faster                                                       |
| Geometric mean  | (ref)                                                            | 1.03x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 286 us: 1.32x faster                                                        |
| deepcopy_memo              | 37.3 us                                                          | 30.2 us: 1.24x faster                                                       |
| go                         | 165 ms                                                           | 134 ms: 1.23x faster                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 2.90 us: 1.17x faster                                                       |
| async_tree_memoization     | 460 ms                                                           | 400 ms: 1.15x faster                                                        |
| generators                 | 33.5 ms                                                          | 29.3 ms: 1.14x faster                                                       |
| async_tree_none            | 365 ms                                                           | 322 ms: 1.14x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 795 ms: 1.13x faster                                                        |
| pathlib                    | 17.1 ms                                                          | 15.6 ms: 1.10x faster                                                       |
| async_tree_none_tg         | 340 ms                                                           | 310 ms: 1.10x faster                                                        |
| async_tree_io              | 873 ms                                                           | 803 ms: 1.09x faster                                                        |
| richards_super             | 61.2 ms                                                          | 56.5 ms: 1.08x faster                                                       |
| async_tree_memoization_tg  | 421 ms                                                           | 391 ms: 1.08x faster                                                        |
| genshi_xml                 | 58.1 ms                                                          | 54.6 ms: 1.06x faster                                                       |
| richards                   | 53.4 ms                                                          | 50.3 ms: 1.06x faster                                                       |
| gc_traversal               | 4.69 ms                                                          | 4.45 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 545 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 575 ms: 1.05x faster                                                        |
| bench_thread_pool          | 908 us                                                           | 865 us: 1.05x faster                                                        |
| html5lib                   | 74.7 ms                                                          | 71.5 ms: 1.04x faster                                                       |
| create_gc_cycles           | 2.00 ms                                                          | 1.92 ms: 1.04x faster                                                       |
| scimark_fft                | 312 ms                                                           | 300 ms: 1.04x faster                                                        |
| genshi_text                | 25.9 ms                                                          | 24.9 ms: 1.04x faster                                                       |
| 2to3                       | 291 ms                                                           | 281 ms: 1.04x faster                                                        |
| logging_format             | 7.11 us                                                          | 6.87 us: 1.03x faster                                                       |
| regex_dna                  | 249 ms                                                           | 241 ms: 1.03x faster                                                        |
| bpe_tokeniser              | 5.14 sec                                                         | 4.97 sec: 1.03x faster                                                      |
| tornado_http               | 119 ms                                                           | 116 ms: 1.03x faster                                                        |
| unpickle_list              | 4.70 us                                                          | 4.56 us: 1.03x faster                                                       |
| docutils                   | 2.98 sec                                                         | 2.90 sec: 1.03x faster                                                      |
| regex_compile              | 144 ms                                                           | 140 ms: 1.03x faster                                                        |
| coroutines                 | 22.0 ms                                                          | 21.4 ms: 1.03x faster                                                       |
| thrift                     | 880 us                                                           | 859 us: 1.02x faster                                                        |
| float                      | 80.2 ms                                                          | 78.3 ms: 1.02x faster                                                       |
| hexiom                     | 6.35 ms                                                          | 6.21 ms: 1.02x faster                                                       |
| sqlite_synth               | 2.80 us                                                          | 2.73 us: 1.02x faster                                                       |
| json                       | 5.35 ms                                                          | 5.24 ms: 1.02x faster                                                       |
| sympy_sum                  | 155 ms                                                           | 152 ms: 1.02x faster                                                        |
| unpickle_pure_python       | 224 us                                                           | 220 us: 1.02x faster                                                        |
| regex_v8                   | 26.0 ms                                                          | 25.5 ms: 1.02x faster                                                       |
| scimark_lu                 | 97.5 ms                                                          | 95.7 ms: 1.02x faster                                                       |
| sqlglot_normalize          | 120 ms                                                           | 118 ms: 1.02x faster                                                        |
| django_template            | 39.0 ms                                                          | 38.3 ms: 1.02x faster                                                       |
| asyncio_tcp                | 378 ms                                                           | 372 ms: 1.02x faster                                                        |
| pickle_dict                | 32.8 us                                                          | 32.4 us: 1.01x faster                                                       |
| unpickle                   | 15.7 us                                                          | 15.5 us: 1.01x faster                                                       |
| sympy_str                  | 295 ms                                                           | 291 ms: 1.01x faster                                                        |
| meteor_contest             | 128 ms                                                           | 127 ms: 1.01x faster                                                        |
| scimark_sor                | 119 ms                                                           | 117 ms: 1.01x faster                                                        |
| pycparser                  | 1.22 sec                                                         | 1.21 sec: 1.01x faster                                                      |
| sqlglot_optimize           | 59.5 ms                                                          | 59.0 ms: 1.01x faster                                                       |
| pickle                     | 10.6 us                                                          | 10.5 us: 1.01x faster                                                       |
| coverage                   | 83.5 ms                                                          | 82.8 ms: 1.01x faster                                                       |
| sympy_integrate            | 23.2 ms                                                          | 23.0 ms: 1.01x faster                                                       |
| spectral_norm              | 97.3 ms                                                          | 96.6 ms: 1.01x faster                                                       |
| async_generators           | 363 ms                                                           | 361 ms: 1.01x faster                                                        |
| pprint_safe_repr           | 818 ms                                                           | 815 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.57 sec: 1.00x faster                                                      |
| pidigits                   | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| xml_etree_generate         | 85.7 ms                                                          | 85.6 ms: 1.00x faster                                                       |
| crypto_pyaes               | 73.6 ms                                                          | 73.8 ms: 1.00x slower                                                       |
| xml_etree_process          | 59.7 ms                                                          | 59.9 ms: 1.00x slower                                                       |
| json_dumps                 | 10.8 ms                                                          | 10.8 ms: 1.00x slower                                                       |
| python_startup_no_site     | 8.85 ms                                                          | 8.94 ms: 1.01x slower                                                       |
| fannkuch                   | 353 ms                                                           | 356 ms: 1.01x slower                                                        |
| python_startup             | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 1.79 ms: 1.01x slower                                                       |
| pickle_list                | 4.44 us                                                          | 4.50 us: 1.01x slower                                                       |
| sqlglot_parse              | 1.39 ms                                                          | 1.41 ms: 1.01x slower                                                       |
| mdp                        | 2.46 sec                                                         | 2.50 sec: 1.02x slower                                                      |
| scimark_monte_carlo        | 65.5 ms                                                          | 66.8 ms: 1.02x slower                                                       |
| pyflate                    | 482 ms                                                           | 492 ms: 1.02x slower                                                        |
| typing_runtime_protocols   | 171 us                                                           | 175 us: 1.03x slower                                                        |
| pickle_pure_python         | 307 us                                                           | 317 us: 1.03x slower                                                        |
| logging_silent             | 96.3 ns                                                          | 99.3 ns: 1.03x slower                                                       |
| raytrace                   | 260 ms                                                           | 272 ms: 1.05x slower                                                        |
| chaos                      | 59.6 ms                                                          | 62.7 ms: 1.05x slower                                                       |
| tomli_loads                | 2.40 sec                                                         | 2.53 sec: 1.05x slower                                                      |
| regex_effbot               | 3.40 ms                                                          | 3.64 ms: 1.07x slower                                                       |
| Geometric mean             | (ref)                                                            | 1.03x faster                                                                |

Benchmark hidden because not significant (17): bench_mp_pool, telco, nbody, logging_simple, xml_etree_iterparse, xml_etree_parse, mako, sympy_expand, dulwich_log, comprehensions, scimark_sparse_mat_mult, deltablue, json_loads, nqueens, pprint_pformat, asyncio_websockets, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x