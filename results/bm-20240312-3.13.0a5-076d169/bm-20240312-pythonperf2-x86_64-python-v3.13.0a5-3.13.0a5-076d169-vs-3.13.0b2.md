# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a5
- machine: linux-x86_64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.01x slower
- HPT reliability: 74.83%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 292 ms: 1.00x slower                                             |
| chameleon      | 7.40 ms                                                          | 7.28 ms: 1.02x faster                                            |
| docutils       | 2.98 sec                                                         | 2.83 sec: 1.06x faster                                           |
| html5lib       | 74.7 ms                                                          | 76.2 ms: 1.02x slower                                            |
| tornado_http   | 119 ms                                                           | 123 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                            | 1.00x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 604 ms                                                           | 697 ms: 1.15x slower                                             |
| async_tree_memoization     | 460 ms                                                           | 543 ms: 1.18x slower                                             |
| async_tree_none            | 365 ms                                                           | 433 ms: 1.18x slower                                             |
| async_tree_io_tg           | 900 ms                                                           | 1.07 sec: 1.19x slower                                           |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 703 ms: 1.23x slower                                             |
| async_tree_io              | 873 ms                                                           | 1.07 sec: 1.23x slower                                           |
| async_tree_none_tg         | 340 ms                                                           | 434 ms: 1.28x slower                                             |
| async_tree_memoization_tg  | 421 ms                                                           | 546 ms: 1.30x slower                                             |
| Geometric mean             | (ref)                                                            | 1.22x slower                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 78.8 ms: 1.02x faster                                            |
| pidigits       | 254 ms                                                           | 262 ms: 1.03x slower                                             |
| nbody          | 87.8 ms                                                          | 91.5 ms: 1.04x slower                                            |
| Geometric mean | (ref)                                                            | 1.02x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 237 ms: 1.05x faster                                             |
| regex_compile  | 144 ms                                                           | 143 ms: 1.01x faster                                             |
| regex_v8       | 26.0 ms                                                          | 26.0 ms: 1.00x faster                                            |
| regex_effbot   | 3.40 ms                                                          | 3.57 ms: 1.05x slower                                            |
| Geometric mean | (ref)                                                            | 1.00x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 224 us                                                           | 211 us: 1.06x faster                                             |
| pickle_dict          | 32.8 us                                                          | 31.0 us: 1.06x faster                                            |
| tomli_loads          | 2.40 sec                                                         | 2.29 sec: 1.05x faster                                           |
| pickle               | 10.6 us                                                          | 10.2 us: 1.04x faster                                            |
| json_dumps           | 10.8 ms                                                          | 10.3 ms: 1.04x faster                                            |
| unpickle_list        | 4.70 us                                                          | 4.56 us: 1.03x faster                                            |
| unpickle             | 15.7 us                                                          | 15.3 us: 1.03x faster                                            |
| json_loads           | 25.0 us                                                          | 24.5 us: 1.02x faster                                            |
| pickle_pure_python   | 307 us                                                           | 305 us: 1.01x faster                                             |
| xml_etree_process    | 59.7 ms                                                          | 60.2 ms: 1.01x slower                                            |
| xml_etree_parse      | 144 ms                                                           | 145 ms: 1.01x slower                                             |
| pickle_list          | 4.44 us                                                          | 4.51 us: 1.01x slower                                            |
| xml_etree_generate   | 85.7 ms                                                          | 87.7 ms: 1.02x slower                                            |
| xml_etree_iterparse  | 103 ms                                                           | 105 ms: 1.03x slower                                             |
| Geometric mean       | (ref)                                                            | 1.02x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 12.7 ms: 1.04x faster                                            |
| python_startup_no_site | 8.85 ms                                                          | 11.1 ms: 1.25x slower                                            |
| Geometric mean         | (ref)                                                            | 1.10x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 54.9 ms: 1.06x faster                                            |
| django_template | 39.0 ms                                                          | 37.7 ms: 1.03x faster                                            |
| mako            | 10.4 ms                                                          | 10.1 ms: 1.02x faster                                            |
| genshi_text     | 25.9 ms                                                          | 25.7 ms: 1.01x faster                                            |
| Geometric mean  | (ref)                                                            | 1.03x faster                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-pythonperf2-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols   | 171 us                                                           | 116 us: 1.47x faster                                             |
| gc_traversal               | 4.69 ms                                                          | 3.55 ms: 1.32x faster                                            |
| create_gc_cycles           | 2.00 ms                                                          | 1.61 ms: 1.25x faster                                            |
| bench_mp_pool              | 4.91 ms                                                          | 4.49 ms: 1.09x faster                                            |
| richards_super             | 61.2 ms                                                          | 57.5 ms: 1.06x faster                                            |
| coverage                   | 83.5 ms                                                          | 78.5 ms: 1.06x faster                                            |
| unpickle_pure_python       | 224 us                                                           | 211 us: 1.06x faster                                             |
| pickle_dict                | 32.8 us                                                          | 31.0 us: 1.06x faster                                            |
| genshi_xml                 | 58.1 ms                                                          | 54.9 ms: 1.06x faster                                            |
| docutils                   | 2.98 sec                                                         | 2.83 sec: 1.06x faster                                           |
| spectral_norm              | 97.3 ms                                                          | 92.4 ms: 1.05x faster                                            |
| regex_dna                  | 249 ms                                                           | 237 ms: 1.05x faster                                             |
| tomli_loads                | 2.40 sec                                                         | 2.29 sec: 1.05x faster                                           |
| pickle                     | 10.6 us                                                          | 10.2 us: 1.04x faster                                            |
| richards                   | 53.4 ms                                                          | 51.2 ms: 1.04x faster                                            |
| json_dumps                 | 10.8 ms                                                          | 10.3 ms: 1.04x faster                                            |
| python_startup             | 13.2 ms                                                          | 12.7 ms: 1.04x faster                                            |
| sqlite_synth               | 2.80 us                                                          | 2.69 us: 1.04x faster                                            |
| telco                      | 8.40 ms                                                          | 8.09 ms: 1.04x faster                                            |
| django_template            | 39.0 ms                                                          | 37.7 ms: 1.03x faster                                            |
| sqlglot_normalize          | 120 ms                                                           | 117 ms: 1.03x faster                                             |
| unpickle_list              | 4.70 us                                                          | 4.56 us: 1.03x faster                                            |
| scimark_lu                 | 97.5 ms                                                          | 94.6 ms: 1.03x faster                                            |
| deepcopy_reduce            | 3.39 us                                                          | 3.29 us: 1.03x faster                                            |
| asyncio_websockets         | 395 ms                                                           | 384 ms: 1.03x faster                                             |
| raytrace                   | 260 ms                                                           | 253 ms: 1.03x faster                                             |
| unpickle                   | 15.7 us                                                          | 15.3 us: 1.03x faster                                            |
| json_loads                 | 25.0 us                                                          | 24.5 us: 1.02x faster                                            |
| mako                       | 10.4 ms                                                          | 10.1 ms: 1.02x faster                                            |
| pprint_safe_repr           | 818 ms                                                           | 800 ms: 1.02x faster                                             |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.20 ms: 1.02x faster                                            |
| comprehensions             | 17.0 us                                                          | 16.7 us: 1.02x faster                                            |
| float                      | 80.2 ms                                                          | 78.8 ms: 1.02x faster                                            |
| pprint_pformat             | 1.66 sec                                                         | 1.63 sec: 1.02x faster                                           |
| sympy_sum                  | 155 ms                                                           | 152 ms: 1.02x faster                                             |
| chameleon                  | 7.40 ms                                                          | 7.28 ms: 1.02x faster                                            |
| crypto_pyaes               | 73.6 ms                                                          | 72.5 ms: 1.01x faster                                            |
| generators                 | 33.5 ms                                                          | 33.1 ms: 1.01x faster                                            |
| deepcopy                   | 377 us                                                           | 373 us: 1.01x faster                                             |
| regex_compile              | 144 ms                                                           | 143 ms: 1.01x faster                                             |
| thrift                     | 880 us                                                           | 870 us: 1.01x faster                                             |
| logging_silent             | 96.3 ns                                                          | 95.3 ns: 1.01x faster                                            |
| genshi_text                | 25.9 ms                                                          | 25.7 ms: 1.01x faster                                            |
| deepcopy_memo              | 37.3 us                                                          | 37.0 us: 1.01x faster                                            |
| sqlglot_optimize           | 59.5 ms                                                          | 59.1 ms: 1.01x faster                                            |
| sympy_str                  | 295 ms                                                           | 293 ms: 1.01x faster                                             |
| pickle_pure_python         | 307 us                                                           | 305 us: 1.01x faster                                             |
| hexiom                     | 6.35 ms                                                          | 6.32 ms: 1.01x faster                                            |
| regex_v8                   | 26.0 ms                                                          | 26.0 ms: 1.00x faster                                            |
| 2to3                       | 291 ms                                                           | 292 ms: 1.00x slower                                             |
| sympy_integrate            | 23.2 ms                                                          | 23.2 ms: 1.00x slower                                            |
| meteor_contest             | 128 ms                                                           | 129 ms: 1.01x slower                                             |
| sympy_expand               | 501 ms                                                           | 504 ms: 1.01x slower                                             |
| logging_simple             | 6.40 us                                                          | 6.44 us: 1.01x slower                                            |
| xml_etree_process          | 59.7 ms                                                          | 60.2 ms: 1.01x slower                                            |
| xml_etree_parse            | 144 ms                                                           | 145 ms: 1.01x slower                                             |
| async_generators           | 363 ms                                                           | 366 ms: 1.01x slower                                             |
| go                         | 165 ms                                                           | 167 ms: 1.01x slower                                             |
| coroutines                 | 22.0 ms                                                          | 22.2 ms: 1.01x slower                                            |
| mdp                        | 2.46 sec                                                         | 2.49 sec: 1.01x slower                                           |
| pickle_list                | 4.44 us                                                          | 4.51 us: 1.01x slower                                            |
| aiohttp                    | 1.07 ms                                                          | 1.09 ms: 1.01x slower                                            |
| dask                       | 391 ms                                                           | 397 ms: 1.02x slower                                             |
| sqlglot_transpile          | 1.76 ms                                                          | 1.80 ms: 1.02x slower                                            |
| html5lib                   | 74.7 ms                                                          | 76.2 ms: 1.02x slower                                            |
| xml_etree_generate         | 85.7 ms                                                          | 87.7 ms: 1.02x slower                                            |
| dulwich_log                | 67.3 ms                                                          | 68.8 ms: 1.02x slower                                            |
| chaos                      | 59.6 ms                                                          | 61.1 ms: 1.03x slower                                            |
| xml_etree_iterparse        | 103 ms                                                           | 105 ms: 1.03x slower                                             |
| tornado_http               | 119 ms                                                           | 123 ms: 1.03x slower                                             |
| pidigits                   | 254 ms                                                           | 262 ms: 1.03x slower                                             |
| nbody                      | 87.8 ms                                                          | 91.5 ms: 1.04x slower                                            |
| regex_effbot               | 3.40 ms                                                          | 3.57 ms: 1.05x slower                                            |
| deltablue                  | 3.37 ms                                                          | 3.56 ms: 1.06x slower                                            |
| pyflate                    | 482 ms                                                           | 509 ms: 1.06x slower                                             |
| pycparser                  | 1.22 sec                                                         | 1.31 sec: 1.07x slower                                           |
| scimark_monte_carlo        | 65.5 ms                                                          | 70.6 ms: 1.08x slower                                            |
| bench_thread_pool          | 908 us                                                           | 979 us: 1.08x slower                                             |
| pathlib                    | 17.1 ms                                                          | 18.9 ms: 1.10x slower                                            |
| mypy2                      | 764 ms                                                           | 864 ms: 1.13x slower                                             |
| fannkuch                   | 353 ms                                                           | 406 ms: 1.15x slower                                             |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 697 ms: 1.15x slower                                             |
| async_tree_memoization     | 460 ms                                                           | 543 ms: 1.18x slower                                             |
| async_tree_none            | 365 ms                                                           | 433 ms: 1.18x slower                                             |
| async_tree_io_tg           | 900 ms                                                           | 1.07 sec: 1.19x slower                                           |
| scimark_sor                | 119 ms                                                           | 143 ms: 1.20x slower                                             |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 703 ms: 1.23x slower                                             |
| async_tree_io              | 873 ms                                                           | 1.07 sec: 1.23x slower                                           |
| python_startup_no_site     | 8.85 ms                                                          | 11.1 ms: 1.25x slower                                            |
| async_tree_none_tg         | 340 ms                                                           | 434 ms: 1.28x slower                                             |
| async_tree_memoization_tg  | 421 ms                                                           | 546 ms: 1.30x slower                                             |
| Geometric mean             | (ref)                                                            | 1.01x slower                                                     |

Benchmark hidden because not significant (10): scimark_fft, flaskblogging, gunicorn, json, asyncio_tcp, asyncio_tcp_ssl, sqlglot_parse, logging_format, nqueens, pylint
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 74.83% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.96x