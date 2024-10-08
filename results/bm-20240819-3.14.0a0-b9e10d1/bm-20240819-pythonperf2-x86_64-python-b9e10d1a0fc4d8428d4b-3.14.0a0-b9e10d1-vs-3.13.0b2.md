# Results vs. 3.13.0b2

- fork: python
- ref: b9e10d1a0fc4d8428d4b
- machine: linux-x86_64
- commit hash: b9e10d1
- commit date: 2024-08-19
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 284 ms: 1.03x faster                                                        |
| docutils       | 2.98 sec                                                         | 2.97 sec: 1.00x faster                                                      |
| html5lib       | 74.7 ms                                                          | 72.5 ms: 1.03x faster                                                       |
| tornado_http   | 119 ms                                                           | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 762 ms: 1.18x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 402 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 300 ms: 1.14x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 380 ms: 1.11x faster                                                        |
| async_tree_none            | 365 ms                                                           | 334 ms: 1.10x faster                                                        |
| async_tree_io              | 873 ms                                                           | 803 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 539 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 576 ms: 1.05x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.11x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 85.1 ms: 1.03x faster                                                       |
| pidigits       | 254 ms                                                           | 252 ms: 1.00x faster                                                        |
| float          | 80.2 ms                                                          | 80.8 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 238 ms: 1.05x faster                                                        |
| regex_compile  | 144 ms                                                           | 139 ms: 1.03x faster                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.64 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                            | 1.00x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.29 sec: 1.05x faster                                                      |
| unpickle_pure_python | 224 us                                                           | 214 us: 1.05x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 99.7 ms: 1.03x faster                                                       |
| xml_etree_parse      | 144 ms                                                           | 141 ms: 1.02x faster                                                        |
| xml_etree_process    | 59.7 ms                                                          | 58.7 ms: 1.02x faster                                                       |
| xml_etree_generate   | 85.7 ms                                                          | 84.3 ms: 1.02x faster                                                       |
| json_dumps           | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                       |
| pickle_pure_python   | 307 us                                                           | 315 us: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.02x faster                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.05 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 53.4 ms: 1.09x faster                                                       |
| genshi_text     | 25.9 ms                                                          | 25.0 ms: 1.04x faster                                                       |
| django_template | 39.0 ms                                                          | 38.4 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                            | 1.03x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-pythonperf2-x86_64-python-b9e10d1a0fc4d8428d4b-3.14.0a0-b9e10d1 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 288 us: 1.31x faster                                                        |
| deepcopy_memo              | 37.3 us                                                          | 29.4 us: 1.27x faster                                                       |
| generators                 | 33.5 ms                                                          | 28.1 ms: 1.19x faster                                                       |
| async_tree_io_tg           | 900 ms                                                           | 762 ms: 1.18x faster                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 2.89 us: 1.17x faster                                                       |
| async_tree_memoization     | 460 ms                                                           | 402 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 300 ms: 1.14x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 380 ms: 1.11x faster                                                        |
| async_tree_none            | 365 ms                                                           | 334 ms: 1.10x faster                                                        |
| async_tree_io              | 873 ms                                                           | 803 ms: 1.09x faster                                                        |
| genshi_xml                 | 58.1 ms                                                          | 53.4 ms: 1.09x faster                                                       |
| bench_mp_pool              | 4.91 ms                                                          | 4.54 ms: 1.08x faster                                                       |
| coverage                   | 83.5 ms                                                          | 77.3 ms: 1.08x faster                                                       |
| richards_super             | 61.2 ms                                                          | 56.8 ms: 1.08x faster                                                       |
| pathlib                    | 17.1 ms                                                          | 15.9 ms: 1.08x faster                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 539 ms: 1.06x faster                                                        |
| richards                   | 53.4 ms                                                          | 50.4 ms: 1.06x faster                                                       |
| bench_thread_pool          | 908 us                                                           | 860 us: 1.06x faster                                                        |
| logging_format             | 7.11 us                                                          | 6.77 us: 1.05x faster                                                       |
| tomli_loads                | 2.40 sec                                                         | 2.29 sec: 1.05x faster                                                      |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 576 ms: 1.05x faster                                                        |
| go                         | 165 ms                                                           | 157 ms: 1.05x faster                                                        |
| regex_dna                  | 249 ms                                                           | 238 ms: 1.05x faster                                                        |
| gc_traversal               | 4.69 ms                                                          | 4.47 ms: 1.05x faster                                                       |
| unpickle_pure_python       | 224 us                                                           | 214 us: 1.05x faster                                                        |
| genshi_text                | 25.9 ms                                                          | 25.0 ms: 1.04x faster                                                       |
| pyflate                    | 482 ms                                                           | 464 ms: 1.04x faster                                                        |
| logging_simple             | 6.40 us                                                          | 6.18 us: 1.04x faster                                                       |
| bpe_tokeniser              | 5.14 sec                                                         | 4.96 sec: 1.04x faster                                                      |
| regex_compile              | 144 ms                                                           | 139 ms: 1.03x faster                                                        |
| scimark_sor                | 119 ms                                                           | 115 ms: 1.03x faster                                                        |
| tornado_http               | 119 ms                                                           | 116 ms: 1.03x faster                                                        |
| nbody                      | 87.8 ms                                                          | 85.1 ms: 1.03x faster                                                       |
| coroutines                 | 22.0 ms                                                          | 21.3 ms: 1.03x faster                                                       |
| html5lib                   | 74.7 ms                                                          | 72.5 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 99.7 ms: 1.03x faster                                                       |
| telco                      | 8.40 ms                                                          | 8.19 ms: 1.03x faster                                                       |
| 2to3                       | 291 ms                                                           | 284 ms: 1.03x faster                                                        |
| crypto_pyaes               | 73.6 ms                                                          | 72.0 ms: 1.02x faster                                                       |
| xml_etree_parse            | 144 ms                                                           | 141 ms: 1.02x faster                                                        |
| scimark_lu                 | 97.5 ms                                                          | 95.8 ms: 1.02x faster                                                       |
| xml_etree_process          | 59.7 ms                                                          | 58.7 ms: 1.02x faster                                                       |
| xml_etree_generate         | 85.7 ms                                                          | 84.3 ms: 1.02x faster                                                       |
| meteor_contest             | 128 ms                                                           | 126 ms: 1.02x faster                                                        |
| create_gc_cycles           | 2.00 ms                                                          | 1.97 ms: 1.02x faster                                                       |
| django_template            | 39.0 ms                                                          | 38.4 ms: 1.01x faster                                                       |
| thrift                     | 880 us                                                           | 867 us: 1.01x faster                                                        |
| asyncio_tcp                | 378 ms                                                           | 374 ms: 1.01x faster                                                        |
| asyncio_websockets         | 395 ms                                                           | 391 ms: 1.01x faster                                                        |
| json                       | 5.35 ms                                                          | 5.31 ms: 1.01x faster                                                       |
| json_dumps                 | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                       |
| sqlglot_optimize           | 59.5 ms                                                          | 59.1 ms: 1.01x faster                                                       |
| sympy_sum                  | 155 ms                                                           | 154 ms: 1.01x faster                                                        |
| spectral_norm              | 97.3 ms                                                          | 96.6 ms: 1.01x faster                                                       |
| sqlglot_normalize          | 120 ms                                                           | 119 ms: 1.01x faster                                                        |
| deltablue                  | 3.37 ms                                                          | 3.35 ms: 1.01x faster                                                       |
| sympy_str                  | 295 ms                                                           | 293 ms: 1.01x faster                                                        |
| pidigits                   | 254 ms                                                           | 252 ms: 1.00x faster                                                        |
| hexiom                     | 6.35 ms                                                          | 6.33 ms: 1.00x faster                                                       |
| docutils                   | 2.98 sec                                                         | 2.97 sec: 1.00x faster                                                      |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.58 sec: 1.00x faster                                                      |
| sqlglot_transpile          | 1.76 ms                                                          | 1.78 ms: 1.01x slower                                                       |
| float                      | 80.2 ms                                                          | 80.8 ms: 1.01x slower                                                       |
| python_startup             | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                       |
| logging_silent             | 96.3 ns                                                          | 97.3 ns: 1.01x slower                                                       |
| pprint_pformat             | 1.66 sec                                                         | 1.68 sec: 1.01x slower                                                      |
| sqlglot_parse              | 1.39 ms                                                          | 1.41 ms: 1.01x slower                                                       |
| fannkuch                   | 353 ms                                                           | 358 ms: 1.01x slower                                                        |
| nqueens                    | 88.4 ms                                                          | 89.7 ms: 1.02x slower                                                       |
| mdp                        | 2.46 sec                                                         | 2.50 sec: 1.02x slower                                                      |
| raytrace                   | 260 ms                                                           | 265 ms: 1.02x slower                                                        |
| pycparser                  | 1.22 sec                                                         | 1.25 sec: 1.02x slower                                                      |
| typing_runtime_protocols   | 171 us                                                           | 174 us: 1.02x slower                                                        |
| python_startup_no_site     | 8.85 ms                                                          | 9.05 ms: 1.02x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 315 us: 1.02x slower                                                        |
| chaos                      | 59.6 ms                                                          | 61.3 ms: 1.03x slower                                                       |
| scimark_monte_carlo        | 65.5 ms                                                          | 68.0 ms: 1.04x slower                                                       |
| regex_effbot               | 3.40 ms                                                          | 3.64 ms: 1.07x slower                                                       |
| Geometric mean             | (ref)                                                            | 1.03x faster                                                                |

Benchmark hidden because not significant (11): scimark_fft, async_generators, mako, sympy_expand, regex_v8, json_loads, comprehensions, sympy_integrate, pprint_safe_repr, scimark_sparse_mat_mult, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x