# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-x86_64
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.02x faster
- HPT reliability: 79.38%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 288 ms: 1.01x faster                                                                  |
| docutils       | 2.98 sec                                                         | 3.01 sec: 1.01x slower                                                                |
| html5lib       | 74.7 ms                                                          | 74.1 ms: 1.01x faster                                                                 |
| tornado_http   | 119 ms                                                           | 118 ms: 1.01x faster                                                                  |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 781 ms: 1.15x faster                                                                  |
| async_tree_memoization     | 460 ms                                                           | 409 ms: 1.12x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                           | 304 ms: 1.12x faster                                                                  |
| async_tree_none            | 365 ms                                                           | 336 ms: 1.09x faster                                                                  |
| async_tree_memoization_tg  | 421 ms                                                           | 388 ms: 1.08x faster                                                                  |
| async_tree_io              | 873 ms                                                           | 818 ms: 1.07x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 546 ms: 1.05x faster                                                                  |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 582 ms: 1.04x faster                                                                  |
| Geometric mean             | (ref)                                                            | 1.09x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 85.6 ms: 1.03x faster                                                                 |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                          |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 236 ms: 1.06x faster                                                                  |
| regex_v8       | 26.0 ms                                                          | 25.6 ms: 1.02x faster                                                                 |
| regex_compile  | 144 ms                                                           | 143 ms: 1.01x faster                                                                  |
| regex_effbot   | 3.40 ms                                                          | 3.56 ms: 1.05x slower                                                                 |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.21 sec: 1.09x faster                                                                |
| unpickle_pure_python | 224 us                                                           | 210 us: 1.07x faster                                                                  |
| xml_etree_process    | 59.7 ms                                                          | 59.2 ms: 1.01x faster                                                                 |
| xml_etree_generate   | 85.7 ms                                                          | 85.3 ms: 1.01x faster                                                                 |
| xml_etree_iterparse  | 103 ms                                                           | 104 ms: 1.01x slower                                                                  |
| xml_etree_parse      | 144 ms                                                           | 145 ms: 1.01x slower                                                                  |
| json_loads           | 25.0 us                                                          | 25.8 us: 1.03x slower                                                                 |
| pickle_pure_python   | 307 us                                                           | 321 us: 1.04x slower                                                                  |
| Geometric mean       | (ref)                                                            | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.02x slower                                                                 |
| python_startup_no_site | 8.85 ms                                                          | 9.08 ms: 1.03x slower                                                                 |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 54.7 ms: 1.06x faster                                                                 |
| mako            | 10.4 ms                                                          | 10.6 ms: 1.02x slower                                                                 |
| django_template | 39.0 ms                                                          | 40.7 ms: 1.04x slower                                                                 |
| genshi_text     | 25.9 ms                                                          | 27.1 ms: 1.05x slower                                                                 |
| Geometric mean  | (ref)                                                            | 1.01x slower                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf2-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 290 us: 1.30x faster                                                                  |
| deepcopy_memo              | 37.3 us                                                          | 30.5 us: 1.22x faster                                                                 |
| generators                 | 33.5 ms                                                          | 28.7 ms: 1.17x faster                                                                 |
| async_tree_io_tg           | 900 ms                                                           | 781 ms: 1.15x faster                                                                  |
| deepcopy_reduce            | 3.39 us                                                          | 2.95 us: 1.15x faster                                                                 |
| async_tree_memoization     | 460 ms                                                           | 409 ms: 1.12x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                           | 304 ms: 1.12x faster                                                                  |
| async_tree_none            | 365 ms                                                           | 336 ms: 1.09x faster                                                                  |
| tomli_loads                | 2.40 sec                                                         | 2.21 sec: 1.09x faster                                                                |
| async_tree_memoization_tg  | 421 ms                                                           | 388 ms: 1.08x faster                                                                  |
| unpickle_pure_python       | 224 us                                                           | 210 us: 1.07x faster                                                                  |
| richards_super             | 61.2 ms                                                          | 57.3 ms: 1.07x faster                                                                 |
| async_tree_io              | 873 ms                                                           | 818 ms: 1.07x faster                                                                  |
| genshi_xml                 | 58.1 ms                                                          | 54.7 ms: 1.06x faster                                                                 |
| coverage                   | 83.5 ms                                                          | 78.8 ms: 1.06x faster                                                                 |
| pathlib                    | 17.1 ms                                                          | 16.2 ms: 1.06x faster                                                                 |
| regex_dna                  | 249 ms                                                           | 236 ms: 1.06x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 546 ms: 1.05x faster                                                                  |
| bpe_tokeniser              | 5.14 sec                                                         | 4.90 sec: 1.05x faster                                                                |
| richards                   | 53.4 ms                                                          | 51.0 ms: 1.05x faster                                                                 |
| bench_thread_pool          | 908 us                                                           | 874 us: 1.04x faster                                                                  |
| telco                      | 8.40 ms                                                          | 8.09 ms: 1.04x faster                                                                 |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 582 ms: 1.04x faster                                                                  |
| crypto_pyaes               | 73.6 ms                                                          | 71.0 ms: 1.04x faster                                                                 |
| scimark_sor                | 119 ms                                                           | 115 ms: 1.03x faster                                                                  |
| go                         | 165 ms                                                           | 160 ms: 1.03x faster                                                                  |
| logging_format             | 7.11 us                                                          | 6.91 us: 1.03x faster                                                                 |
| nbody                      | 87.8 ms                                                          | 85.6 ms: 1.03x faster                                                                 |
| coroutines                 | 22.0 ms                                                          | 21.5 ms: 1.02x faster                                                                 |
| logging_simple             | 6.40 us                                                          | 6.25 us: 1.02x faster                                                                 |
| regex_v8                   | 26.0 ms                                                          | 25.6 ms: 1.02x faster                                                                 |
| asyncio_websockets         | 395 ms                                                           | 389 ms: 1.01x faster                                                                  |
| tornado_http               | 119 ms                                                           | 118 ms: 1.01x faster                                                                  |
| spectral_norm              | 97.3 ms                                                          | 96.1 ms: 1.01x faster                                                                 |
| 2to3                       | 291 ms                                                           | 288 ms: 1.01x faster                                                                  |
| dask                       | 391 ms                                                           | 386 ms: 1.01x faster                                                                  |
| xml_etree_process          | 59.7 ms                                                          | 59.2 ms: 1.01x faster                                                                 |
| regex_compile              | 144 ms                                                           | 143 ms: 1.01x faster                                                                  |
| html5lib                   | 74.7 ms                                                          | 74.1 ms: 1.01x faster                                                                 |
| asyncio_tcp                | 378 ms                                                           | 375 ms: 1.01x faster                                                                  |
| sqlglot_normalize          | 120 ms                                                           | 120 ms: 1.01x faster                                                                  |
| xml_etree_generate         | 85.7 ms                                                          | 85.3 ms: 1.01x faster                                                                 |
| deltablue                  | 3.37 ms                                                          | 3.36 ms: 1.00x faster                                                                 |
| meteor_contest             | 128 ms                                                           | 128 ms: 1.00x faster                                                                  |
| sqlglot_optimize           | 59.5 ms                                                          | 59.3 ms: 1.00x faster                                                                 |
| async_generators           | 363 ms                                                           | 365 ms: 1.01x slower                                                                  |
| sympy_sum                  | 155 ms                                                           | 156 ms: 1.01x slower                                                                  |
| hexiom                     | 6.35 ms                                                          | 6.39 ms: 1.01x slower                                                                 |
| sqlglot_parse              | 1.39 ms                                                          | 1.40 ms: 1.01x slower                                                                 |
| thrift                     | 880 us                                                           | 886 us: 1.01x slower                                                                  |
| sqlglot_transpile          | 1.76 ms                                                          | 1.78 ms: 1.01x slower                                                                 |
| docutils                   | 2.98 sec                                                         | 3.01 sec: 1.01x slower                                                                |
| xml_etree_iterparse        | 103 ms                                                           | 104 ms: 1.01x slower                                                                  |
| logging_silent             | 96.3 ns                                                          | 97.4 ns: 1.01x slower                                                                 |
| xml_etree_parse            | 144 ms                                                           | 145 ms: 1.01x slower                                                                  |
| gc_traversal               | 4.69 ms                                                          | 4.75 ms: 1.01x slower                                                                 |
| pprint_safe_repr           | 818 ms                                                           | 829 ms: 1.01x slower                                                                  |
| sympy_str                  | 295 ms                                                           | 299 ms: 1.01x slower                                                                  |
| sympy_integrate            | 23.2 ms                                                          | 23.5 ms: 1.01x slower                                                                 |
| scimark_monte_carlo        | 65.5 ms                                                          | 66.5 ms: 1.02x slower                                                                 |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.02x slower                                                                 |
| mdp                        | 2.46 sec                                                         | 2.50 sec: 1.02x slower                                                                |
| create_gc_cycles           | 2.00 ms                                                          | 2.04 ms: 1.02x slower                                                                 |
| scimark_lu                 | 97.5 ms                                                          | 99.2 ms: 1.02x slower                                                                 |
| mako                       | 10.4 ms                                                          | 10.6 ms: 1.02x slower                                                                 |
| sympy_expand               | 501 ms                                                           | 511 ms: 1.02x slower                                                                  |
| fannkuch                   | 353 ms                                                           | 360 ms: 1.02x slower                                                                  |
| pyflate                    | 482 ms                                                           | 491 ms: 1.02x slower                                                                  |
| raytrace                   | 260 ms                                                           | 266 ms: 1.02x slower                                                                  |
| json                       | 5.35 ms                                                          | 5.48 ms: 1.02x slower                                                                 |
| pprint_pformat             | 1.66 sec                                                         | 1.70 sec: 1.02x slower                                                                |
| python_startup_no_site     | 8.85 ms                                                          | 9.08 ms: 1.03x slower                                                                 |
| nqueens                    | 88.4 ms                                                          | 90.7 ms: 1.03x slower                                                                 |
| typing_runtime_protocols   | 171 us                                                           | 176 us: 1.03x slower                                                                  |
| json_loads                 | 25.0 us                                                          | 25.8 us: 1.03x slower                                                                 |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.44 ms: 1.04x slower                                                                 |
| comprehensions             | 17.0 us                                                          | 17.6 us: 1.04x slower                                                                 |
| pickle_pure_python         | 307 us                                                           | 321 us: 1.04x slower                                                                  |
| django_template            | 39.0 ms                                                          | 40.7 ms: 1.04x slower                                                                 |
| pycparser                  | 1.22 sec                                                         | 1.28 sec: 1.04x slower                                                                |
| regex_effbot               | 3.40 ms                                                          | 3.56 ms: 1.05x slower                                                                 |
| genshi_text                | 25.9 ms                                                          | 27.1 ms: 1.05x slower                                                                 |
| chaos                      | 59.6 ms                                                          | 62.5 ms: 1.05x slower                                                                 |
| Geometric mean             | (ref)                                                            | 1.02x faster                                                                          |

Benchmark hidden because not significant (7): bench_mp_pool, scimark_fft, json_dumps, asyncio_tcp_ssl, float, pidigits, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 79.38% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x