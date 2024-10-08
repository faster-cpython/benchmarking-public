# Results vs. 3.13.0b2

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-x86_64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.02x faster
- HPT reliability: 89.76%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 309 ms: 1.06x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.16 sec: 1.06x slower                                                      |
| html5lib       | 74.7 ms                                                          | 71.3 ms: 1.05x faster                                                       |
| tornado_http   | 119 ms                                                           | 121 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 365 ms                                                           | 319 ms: 1.15x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 401 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 309 ms: 1.10x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 818 ms: 1.10x faster                                                        |
| async_tree_io              | 873 ms                                                           | 805 ms: 1.09x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 389 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 571 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 544 ms: 1.05x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 78.7 ms: 1.12x faster                                                       |
| float          | 80.2 ms                                                          | 74.2 ms: 1.08x faster                                                       |
| pidigits       | 254 ms                                                           | 250 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                            | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 237 ms: 1.05x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 25.8 ms: 1.01x faster                                                       |
| regex_compile  | 144 ms                                                           | 146 ms: 1.01x slower                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.61 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                            | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.09 sec: 1.15x faster                                                      |
| xml_etree_generate   | 85.7 ms                                                          | 78.5 ms: 1.09x faster                                                       |
| xml_etree_process    | 59.7 ms                                                          | 55.8 ms: 1.07x faster                                                       |
| pickle_dict          | 32.8 us                                                          | 30.7 us: 1.07x faster                                                       |
| pickle_list          | 4.44 us                                                          | 4.22 us: 1.05x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                           | 97.4 ms: 1.05x faster                                                       |
| unpickle_pure_python | 224 us                                                           | 214 us: 1.05x faster                                                        |
| unpickle             | 15.7 us                                                          | 15.2 us: 1.03x faster                                                       |
| pickle               | 10.6 us                                                          | 10.4 us: 1.02x faster                                                       |
| json_loads           | 25.0 us                                                          | 24.5 us: 1.02x faster                                                       |
| xml_etree_parse      | 144 ms                                                           | 142 ms: 1.01x faster                                                        |
| pickle_pure_python   | 307 us                                                           | 326 us: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.04x faster                                                                |

Benchmark hidden because not significant (2): unpickle_list, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.85 ms                                                          | 8.93 ms: 1.01x slower                                                       |
| python_startup         | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.18 ms: 1.13x faster                                                       |
| django_template | 39.0 ms                                                          | 41.6 ms: 1.07x slower                                                       |
| genshi_text     | 25.9 ms                                                          | 29.3 ms: 1.13x slower                                                       |
| genshi_xml      | 58.1 ms                                                          | 66.1 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.05x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 37.3 us                                                          | 26.5 us: 1.41x faster                                                       |
| deepcopy                   | 377 us                                                           | 292 us: 1.29x faster                                                        |
| spectral_norm              | 97.3 ms                                                          | 81.4 ms: 1.20x faster                                                       |
| richards                   | 53.4 ms                                                          | 44.7 ms: 1.19x faster                                                       |
| richards_super             | 61.2 ms                                                          | 52.4 ms: 1.17x faster                                                       |
| deepcopy_reduce            | 3.39 us                                                          | 2.90 us: 1.17x faster                                                       |
| tomli_loads                | 2.40 sec                                                         | 2.09 sec: 1.15x faster                                                      |
| scimark_sor                | 119 ms                                                           | 103 ms: 1.15x faster                                                        |
| async_tree_none            | 365 ms                                                           | 319 ms: 1.15x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 401 ms: 1.15x faster                                                        |
| mako                       | 10.4 ms                                                          | 9.18 ms: 1.13x faster                                                       |
| nbody                      | 87.8 ms                                                          | 78.7 ms: 1.12x faster                                                       |
| async_tree_none_tg         | 340 ms                                                           | 309 ms: 1.10x faster                                                        |
| go                         | 165 ms                                                           | 150 ms: 1.10x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 818 ms: 1.10x faster                                                        |
| xml_etree_generate         | 85.7 ms                                                          | 78.5 ms: 1.09x faster                                                       |
| pathlib                    | 17.1 ms                                                          | 15.7 ms: 1.09x faster                                                       |
| async_tree_io              | 873 ms                                                           | 805 ms: 1.09x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 389 ms: 1.08x faster                                                        |
| float                      | 80.2 ms                                                          | 74.2 ms: 1.08x faster                                                       |
| bpe_tokeniser              | 5.14 sec                                                         | 4.76 sec: 1.08x faster                                                      |
| scimark_fft                | 312 ms                                                           | 290 ms: 1.08x faster                                                        |
| gc_traversal               | 4.69 ms                                                          | 4.36 ms: 1.07x faster                                                       |
| xml_etree_process          | 59.7 ms                                                          | 55.8 ms: 1.07x faster                                                       |
| pickle_dict                | 32.8 us                                                          | 30.7 us: 1.07x faster                                                       |
| pyflate                    | 482 ms                                                           | 454 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 571 ms: 1.06x faster                                                        |
| crypto_pyaes               | 73.6 ms                                                          | 69.7 ms: 1.06x faster                                                       |
| pickle_list                | 4.44 us                                                          | 4.22 us: 1.05x faster                                                       |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.06 ms: 1.05x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 97.4 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 544 ms: 1.05x faster                                                        |
| coverage                   | 83.5 ms                                                          | 79.4 ms: 1.05x faster                                                       |
| regex_dna                  | 249 ms                                                           | 237 ms: 1.05x faster                                                        |
| create_gc_cycles           | 2.00 ms                                                          | 1.91 ms: 1.05x faster                                                       |
| unpickle_pure_python       | 224 us                                                           | 214 us: 1.05x faster                                                        |
| html5lib                   | 74.7 ms                                                          | 71.3 ms: 1.05x faster                                                       |
| pprint_safe_repr           | 818 ms                                                           | 783 ms: 1.04x faster                                                        |
| deltablue                  | 3.37 ms                                                          | 3.23 ms: 1.04x faster                                                       |
| dulwich_log                | 67.3 ms                                                          | 64.6 ms: 1.04x faster                                                       |
| telco                      | 8.40 ms                                                          | 8.08 ms: 1.04x faster                                                       |
| sqlite_synth               | 2.80 us                                                          | 2.71 us: 1.03x faster                                                       |
| unpickle                   | 15.7 us                                                          | 15.2 us: 1.03x faster                                                       |
| json                       | 5.35 ms                                                          | 5.20 ms: 1.03x faster                                                       |
| pickle                     | 10.6 us                                                          | 10.4 us: 1.02x faster                                                       |
| json_loads                 | 25.0 us                                                          | 24.5 us: 1.02x faster                                                       |
| pprint_pformat             | 1.66 sec                                                         | 1.63 sec: 1.02x faster                                                      |
| pidigits                   | 254 ms                                                           | 250 ms: 1.01x faster                                                        |
| coroutines                 | 22.0 ms                                                          | 21.7 ms: 1.01x faster                                                       |
| regex_v8                   | 26.0 ms                                                          | 25.8 ms: 1.01x faster                                                       |
| xml_etree_parse            | 144 ms                                                           | 142 ms: 1.01x faster                                                        |
| meteor_contest             | 128 ms                                                           | 128 ms: 1.00x faster                                                        |
| thrift                     | 880 us                                                           | 885 us: 1.01x slower                                                        |
| python_startup_no_site     | 8.85 ms                                                          | 8.93 ms: 1.01x slower                                                       |
| tornado_http               | 119 ms                                                           | 121 ms: 1.01x slower                                                        |
| python_startup             | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                       |
| logging_format             | 7.11 us                                                          | 7.20 us: 1.01x slower                                                       |
| regex_compile              | 144 ms                                                           | 146 ms: 1.01x slower                                                        |
| fannkuch                   | 353 ms                                                           | 358 ms: 1.02x slower                                                        |
| logging_simple             | 6.40 us                                                          | 6.53 us: 1.02x slower                                                       |
| scimark_monte_carlo        | 65.5 ms                                                          | 67.1 ms: 1.02x slower                                                       |
| sympy_str                  | 295 ms                                                           | 308 ms: 1.05x slower                                                        |
| sympy_expand               | 501 ms                                                           | 525 ms: 1.05x slower                                                        |
| logging_silent             | 96.3 ns                                                          | 101 ns: 1.05x slower                                                        |
| mdp                        | 2.46 sec                                                         | 2.61 sec: 1.06x slower                                                      |
| sqlglot_normalize          | 120 ms                                                           | 128 ms: 1.06x slower                                                        |
| docutils                   | 2.98 sec                                                         | 3.16 sec: 1.06x slower                                                      |
| pickle_pure_python         | 307 us                                                           | 326 us: 1.06x slower                                                        |
| regex_effbot               | 3.40 ms                                                          | 3.61 ms: 1.06x slower                                                       |
| 2to3                       | 291 ms                                                           | 309 ms: 1.06x slower                                                        |
| pycparser                  | 1.22 sec                                                         | 1.30 sec: 1.06x slower                                                      |
| sqlglot_parse              | 1.39 ms                                                          | 1.48 ms: 1.06x slower                                                       |
| async_generators           | 363 ms                                                           | 386 ms: 1.07x slower                                                        |
| django_template            | 39.0 ms                                                          | 41.6 ms: 1.07x slower                                                       |
| sympy_sum                  | 155 ms                                                           | 167 ms: 1.08x slower                                                        |
| comprehensions             | 17.0 us                                                          | 18.3 us: 1.08x slower                                                       |
| generators                 | 33.5 ms                                                          | 36.5 ms: 1.09x slower                                                       |
| typing_runtime_protocols   | 171 us                                                           | 186 us: 1.09x slower                                                        |
| sqlglot_optimize           | 59.5 ms                                                          | 65.0 ms: 1.09x slower                                                       |
| hexiom                     | 6.35 ms                                                          | 6.95 ms: 1.09x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 1.93 ms: 1.09x slower                                                       |
| nqueens                    | 88.4 ms                                                          | 97.0 ms: 1.10x slower                                                       |
| chaos                      | 59.6 ms                                                          | 65.6 ms: 1.10x slower                                                       |
| genshi_text                | 25.9 ms                                                          | 29.3 ms: 1.13x slower                                                       |
| sympy_integrate            | 23.2 ms                                                          | 26.3 ms: 1.14x slower                                                       |
| genshi_xml                 | 58.1 ms                                                          | 66.1 ms: 1.14x slower                                                       |
| raytrace                   | 260 ms                                                           | 313 ms: 1.20x slower                                                        |
| pylint                     | 339 ms                                                           | 408 ms: 1.20x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.02x faster                                                                |

Benchmark hidden because not significant (8): asyncio_tcp, unpickle_list, asyncio_tcp_ssl, scimark_lu, json_dumps, asyncio_websockets, bench_thread_pool, bench_mp_pool
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: unpack_sequence

# HPT report

- Reliability score: 89.76% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x