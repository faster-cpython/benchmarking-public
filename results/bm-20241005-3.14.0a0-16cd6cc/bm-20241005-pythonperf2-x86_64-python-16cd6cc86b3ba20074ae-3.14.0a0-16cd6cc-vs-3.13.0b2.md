# Results vs. 3.13.0b2

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-x86_64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.04x slower
- HPT reliability: 99.87%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 283 ms: 1.03x faster                                                        |
| docutils       | 2.98 sec                                                         | 2.88 sec: 1.04x faster                                                      |
| html5lib       | 74.7 ms                                                          | 71.0 ms: 1.05x faster                                                       |
| tornado_http   | 119 ms                                                           | 115 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                            | 1.04x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 460 ms                                                           | 401 ms: 1.15x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 786 ms: 1.14x faster                                                        |
| async_tree_none            | 365 ms                                                           | 319 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 309 ms: 1.10x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 392 ms: 1.07x faster                                                        |
| async_tree_io              | 873 ms                                                           | 821 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 571 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 561 ms: 1.02x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.09x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 78.8 ms: 1.02x faster                                                       |
| pidigits       | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| nbody          | 87.8 ms                                                          | 89.9 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                            | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                          | 25.0 ms: 1.04x faster                                                       |
| regex_dna      | 249 ms                                                           | 242 ms: 1.03x faster                                                        |
| regex_compile  | 144 ms                                                           | 140 ms: 1.03x faster                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.48 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle             | 15.7 us                                                          | 15.1 us: 1.04x faster                                                       |
| unpickle_pure_python | 224 us                                                           | 218 us: 1.03x faster                                                        |
| json_loads           | 25.0 us                                                          | 25.1 us: 1.00x slower                                                       |
| xml_etree_generate   | 85.7 ms                                                          | 86.1 ms: 1.00x slower                                                       |
| json_dumps           | 10.8 ms                                                          | 10.8 ms: 1.00x slower                                                       |
| unpickle_list        | 4.70 us                                                          | 4.76 us: 1.01x slower                                                       |
| pickle               | 10.6 us                                                          | 10.8 us: 1.02x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 315 us: 1.02x slower                                                        |
| xml_etree_process    | 59.7 ms                                                          | 61.4 ms: 1.03x slower                                                       |
| xml_etree_parse      | 144 ms                                                           | 150 ms: 1.04x slower                                                        |
| tomli_loads          | 2.40 sec                                                         | 2.54 sec: 1.06x slower                                                      |
| pickle_list          | 4.44 us                                                          | 4.71 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                            | 1.01x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 8.95 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 54.6 ms: 1.06x faster                                                       |
| genshi_text     | 25.9 ms                                                          | 25.5 ms: 1.02x faster                                                       |
| django_template | 39.0 ms                                                          | 39.9 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 284 us: 1.33x faster                                                        |
| deepcopy_memo              | 37.3 us                                                          | 29.5 us: 1.27x faster                                                       |
| go                         | 165 ms                                                           | 135 ms: 1.22x faster                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 2.90 us: 1.17x faster                                                       |
| generators                 | 33.5 ms                                                          | 29.1 ms: 1.15x faster                                                       |
| async_tree_memoization     | 460 ms                                                           | 401 ms: 1.15x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 786 ms: 1.14x faster                                                        |
| async_tree_none            | 365 ms                                                           | 319 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 309 ms: 1.10x faster                                                        |
| pathlib                    | 17.1 ms                                                          | 15.8 ms: 1.08x faster                                                       |
| async_tree_memoization_tg  | 421 ms                                                           | 392 ms: 1.07x faster                                                        |
| genshi_xml                 | 58.1 ms                                                          | 54.6 ms: 1.06x faster                                                       |
| async_tree_io              | 873 ms                                                           | 821 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 571 ms: 1.06x faster                                                        |
| richards_super             | 61.2 ms                                                          | 57.9 ms: 1.06x faster                                                       |
| html5lib                   | 74.7 ms                                                          | 71.0 ms: 1.05x faster                                                       |
| scimark_fft                | 312 ms                                                           | 297 ms: 1.05x faster                                                        |
| logging_format             | 7.11 us                                                          | 6.80 us: 1.05x faster                                                       |
| richards                   | 53.4 ms                                                          | 51.2 ms: 1.04x faster                                                       |
| scimark_lu                 | 97.5 ms                                                          | 93.5 ms: 1.04x faster                                                       |
| regex_v8                   | 26.0 ms                                                          | 25.0 ms: 1.04x faster                                                       |
| unpickle                   | 15.7 us                                                          | 15.1 us: 1.04x faster                                                       |
| tornado_http               | 119 ms                                                           | 115 ms: 1.04x faster                                                        |
| docutils                   | 2.98 sec                                                         | 2.88 sec: 1.04x faster                                                      |
| bpe_tokeniser              | 5.14 sec                                                         | 4.98 sec: 1.03x faster                                                      |
| 2to3                       | 291 ms                                                           | 283 ms: 1.03x faster                                                        |
| regex_dna                  | 249 ms                                                           | 242 ms: 1.03x faster                                                        |
| sympy_sum                  | 155 ms                                                           | 151 ms: 1.03x faster                                                        |
| unpickle_pure_python       | 224 us                                                           | 218 us: 1.03x faster                                                        |
| thrift                     | 880 us                                                           | 855 us: 1.03x faster                                                        |
| regex_compile              | 144 ms                                                           | 140 ms: 1.03x faster                                                        |
| sqlite_synth               | 2.80 us                                                          | 2.72 us: 1.03x faster                                                       |
| sqlglot_normalize          | 120 ms                                                           | 117 ms: 1.03x faster                                                        |
| telco                      | 8.40 ms                                                          | 8.19 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 561 ms: 1.02x faster                                                        |
| sympy_expand               | 501 ms                                                           | 491 ms: 1.02x faster                                                        |
| sympy_str                  | 295 ms                                                           | 289 ms: 1.02x faster                                                        |
| hexiom                     | 6.35 ms                                                          | 6.23 ms: 1.02x faster                                                       |
| logging_simple             | 6.40 us                                                          | 6.28 us: 1.02x faster                                                       |
| pprint_safe_repr           | 818 ms                                                           | 803 ms: 1.02x faster                                                        |
| float                      | 80.2 ms                                                          | 78.8 ms: 1.02x faster                                                       |
| genshi_text                | 25.9 ms                                                          | 25.5 ms: 1.02x faster                                                       |
| pprint_pformat             | 1.66 sec                                                         | 1.64 sec: 1.01x faster                                                      |
| sqlglot_optimize           | 59.5 ms                                                          | 58.8 ms: 1.01x faster                                                       |
| asyncio_websockets         | 395 ms                                                           | 390 ms: 1.01x faster                                                        |
| async_generators           | 363 ms                                                           | 358 ms: 1.01x faster                                                        |
| dulwich_log                | 67.3 ms                                                          | 66.6 ms: 1.01x faster                                                       |
| meteor_contest             | 128 ms                                                           | 127 ms: 1.01x faster                                                        |
| scimark_sor                | 119 ms                                                           | 118 ms: 1.01x faster                                                        |
| asyncio_tcp                | 378 ms                                                           | 374 ms: 1.01x faster                                                        |
| deltablue                  | 3.37 ms                                                          | 3.35 ms: 1.01x faster                                                       |
| coroutines                 | 22.0 ms                                                          | 21.9 ms: 1.01x faster                                                       |
| pidigits                   | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.58 sec: 1.00x faster                                                      |
| json_loads                 | 25.0 us                                                          | 25.1 us: 1.00x slower                                                       |
| xml_etree_generate         | 85.7 ms                                                          | 86.1 ms: 1.00x slower                                                       |
| json_dumps                 | 10.8 ms                                                          | 10.8 ms: 1.00x slower                                                       |
| nqueens                    | 88.4 ms                                                          | 88.8 ms: 1.00x slower                                                       |
| fannkuch                   | 353 ms                                                           | 355 ms: 1.01x slower                                                        |
| mdp                        | 2.46 sec                                                         | 2.48 sec: 1.01x slower                                                      |
| python_startup             | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                       |
| crypto_pyaes               | 73.6 ms                                                          | 74.2 ms: 1.01x slower                                                       |
| comprehensions             | 17.0 us                                                          | 17.1 us: 1.01x slower                                                       |
| python_startup_no_site     | 8.85 ms                                                          | 8.95 ms: 1.01x slower                                                       |
| typing_runtime_protocols   | 171 us                                                           | 173 us: 1.01x slower                                                        |
| unpickle_list              | 4.70 us                                                          | 4.76 us: 1.01x slower                                                       |
| pickle                     | 10.6 us                                                          | 10.8 us: 1.02x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 1.80 ms: 1.02x slower                                                       |
| pycparser                  | 1.22 sec                                                         | 1.25 sec: 1.02x slower                                                      |
| sqlglot_parse              | 1.39 ms                                                          | 1.42 ms: 1.02x slower                                                       |
| nbody                      | 87.8 ms                                                          | 89.9 ms: 1.02x slower                                                       |
| scimark_monte_carlo        | 65.5 ms                                                          | 67.1 ms: 1.02x slower                                                       |
| regex_effbot               | 3.40 ms                                                          | 3.48 ms: 1.02x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 315 us: 1.02x slower                                                        |
| django_template            | 39.0 ms                                                          | 39.9 ms: 1.03x slower                                                       |
| gc_traversal               | 4.69 ms                                                          | 4.81 ms: 1.03x slower                                                       |
| coverage                   | 83.5 ms                                                          | 85.7 ms: 1.03x slower                                                       |
| xml_etree_process          | 59.7 ms                                                          | 61.4 ms: 1.03x slower                                                       |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.41 ms: 1.03x slower                                                       |
| logging_silent             | 96.3 ns                                                          | 99.3 ns: 1.03x slower                                                       |
| xml_etree_parse            | 144 ms                                                           | 150 ms: 1.04x slower                                                        |
| pyflate                    | 482 ms                                                           | 504 ms: 1.05x slower                                                        |
| raytrace                   | 260 ms                                                           | 273 ms: 1.05x slower                                                        |
| chaos                      | 59.6 ms                                                          | 63.0 ms: 1.06x slower                                                       |
| tomli_loads                | 2.40 sec                                                         | 2.54 sec: 1.06x slower                                                      |
| pickle_list                | 4.44 us                                                          | 4.71 us: 1.06x slower                                                       |
| bench_mp_pool              | 4.91 ms                                                          | 1.33 sec: 270.88x slower                                                    |
| Geometric mean             | (ref)                                                            | 1.04x slower                                                                |

Benchmark hidden because not significant (9): xml_etree_iterparse, json, pickle_dict, spectral_norm, sympy_integrate, mako, bench_thread_pool, create_gc_cycles, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: unpack_sequence

# HPT report

- Reliability score: 99.87% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x