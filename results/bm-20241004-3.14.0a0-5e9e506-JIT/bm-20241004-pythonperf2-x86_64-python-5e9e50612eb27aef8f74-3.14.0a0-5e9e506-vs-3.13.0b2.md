# Results vs. 3.13.0b2

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: linux-x86_64
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.05x slower
- HPT reliability: 72.06%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 317 ms: 1.09x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.22 sec: 1.08x slower                                                      |
| html5lib       | 74.7 ms                                                          | 70.5 ms: 1.06x faster                                                       |
| tornado_http   | 119 ms                                                           | 122 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                            | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 777 ms: 1.16x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 402 ms: 1.14x faster                                                        |
| async_tree_none            | 365 ms                                                           | 324 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 308 ms: 1.10x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 391 ms: 1.08x faster                                                        |
| async_tree_io              | 873 ms                                                           | 820 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 575 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 546 ms: 1.05x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 75.7 ms: 1.06x faster                                                       |
| nbody          | 87.8 ms                                                          | 84.3 ms: 1.04x faster                                                       |
| pidigits       | 254 ms                                                           | 251 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                            | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                          | 25.8 ms: 1.01x faster                                                       |
| regex_dna      | 249 ms                                                           | 249 ms: 1.00x faster                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.52 ms: 1.03x slower                                                       |
| regex_compile  | 144 ms                                                           | 153 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.17 sec: 1.11x faster                                                      |
| xml_etree_generate   | 85.7 ms                                                          | 79.1 ms: 1.08x faster                                                       |
| pickle_dict          | 32.8 us                                                          | 30.9 us: 1.06x faster                                                       |
| xml_etree_process    | 59.7 ms                                                          | 56.7 ms: 1.05x faster                                                       |
| pickle_list          | 4.44 us                                                          | 4.24 us: 1.05x faster                                                       |
| pickle               | 10.6 us                                                          | 10.2 us: 1.04x faster                                                       |
| json_dumps           | 10.8 ms                                                          | 10.5 ms: 1.02x faster                                                       |
| unpickle_pure_python | 224 us                                                           | 220 us: 1.02x faster                                                        |
| unpickle_list        | 4.70 us                                                          | 4.60 us: 1.02x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                           | 101 ms: 1.02x faster                                                        |
| unpickle             | 15.7 us                                                          | 15.5 us: 1.01x faster                                                       |
| xml_etree_parse      | 144 ms                                                           | 148 ms: 1.03x slower                                                        |
| pickle_pure_python   | 307 us                                                           | 324 us: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.03x faster                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.85 ms                                                          | 8.97 ms: 1.01x slower                                                       |
| python_startup         | 13.2 ms                                                          | 13.5 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.16 ms: 1.13x faster                                                       |
| django_template | 39.0 ms                                                          | 42.9 ms: 1.10x slower                                                       |
| genshi_xml      | 58.1 ms                                                          | 64.9 ms: 1.12x slower                                                       |
| genshi_text     | 25.9 ms                                                          | 29.7 ms: 1.15x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.06x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 37.3 us                                                          | 27.4 us: 1.36x faster                                                       |
| deepcopy                   | 377 us                                                           | 294 us: 1.28x faster                                                        |
| richards                   | 53.4 ms                                                          | 44.3 ms: 1.21x faster                                                       |
| richards_super             | 61.2 ms                                                          | 51.5 ms: 1.19x faster                                                       |
| spectral_norm              | 97.3 ms                                                          | 82.6 ms: 1.18x faster                                                       |
| async_tree_io_tg           | 900 ms                                                           | 777 ms: 1.16x faster                                                        |
| scimark_sor                | 119 ms                                                           | 104 ms: 1.14x faster                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 2.97 us: 1.14x faster                                                       |
| async_tree_memoization     | 460 ms                                                           | 402 ms: 1.14x faster                                                        |
| mako                       | 10.4 ms                                                          | 9.16 ms: 1.13x faster                                                       |
| async_tree_none            | 365 ms                                                           | 324 ms: 1.13x faster                                                        |
| scimark_fft                | 312 ms                                                           | 278 ms: 1.12x faster                                                        |
| tomli_loads                | 2.40 sec                                                         | 2.17 sec: 1.11x faster                                                      |
| async_tree_none_tg         | 340 ms                                                           | 308 ms: 1.10x faster                                                        |
| telco                      | 8.40 ms                                                          | 7.65 ms: 1.10x faster                                                       |
| pathlib                    | 17.1 ms                                                          | 15.7 ms: 1.09x faster                                                       |
| xml_etree_generate         | 85.7 ms                                                          | 79.1 ms: 1.08x faster                                                       |
| bpe_tokeniser              | 5.14 sec                                                         | 4.76 sec: 1.08x faster                                                      |
| async_tree_memoization_tg  | 421 ms                                                           | 391 ms: 1.08x faster                                                        |
| go                         | 165 ms                                                           | 154 ms: 1.07x faster                                                        |
| create_gc_cycles           | 2.00 ms                                                          | 1.87 ms: 1.07x faster                                                       |
| pyflate                    | 482 ms                                                           | 452 ms: 1.07x faster                                                        |
| async_tree_io              | 873 ms                                                           | 820 ms: 1.06x faster                                                        |
| pprint_safe_repr           | 818 ms                                                           | 768 ms: 1.06x faster                                                        |
| pickle_dict                | 32.8 us                                                          | 30.9 us: 1.06x faster                                                       |
| float                      | 80.2 ms                                                          | 75.7 ms: 1.06x faster                                                       |
| html5lib                   | 74.7 ms                                                          | 70.5 ms: 1.06x faster                                                       |
| xml_etree_process          | 59.7 ms                                                          | 56.7 ms: 1.05x faster                                                       |
| deltablue                  | 3.37 ms                                                          | 3.21 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 575 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 546 ms: 1.05x faster                                                        |
| crypto_pyaes               | 73.6 ms                                                          | 70.2 ms: 1.05x faster                                                       |
| pickle_list                | 4.44 us                                                          | 4.24 us: 1.05x faster                                                       |
| dulwich_log                | 67.3 ms                                                          | 64.3 ms: 1.05x faster                                                       |
| nbody                      | 87.8 ms                                                          | 84.3 ms: 1.04x faster                                                       |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.13 ms: 1.04x faster                                                       |
| pickle                     | 10.6 us                                                          | 10.2 us: 1.04x faster                                                       |
| pprint_pformat             | 1.66 sec                                                         | 1.61 sec: 1.03x faster                                                      |
| sqlite_synth               | 2.80 us                                                          | 2.72 us: 1.03x faster                                                       |
| json                       | 5.35 ms                                                          | 5.22 ms: 1.03x faster                                                       |
| asyncio_tcp                | 378 ms                                                           | 368 ms: 1.03x faster                                                        |
| coroutines                 | 22.0 ms                                                          | 21.4 ms: 1.03x faster                                                       |
| json_dumps                 | 10.8 ms                                                          | 10.5 ms: 1.02x faster                                                       |
| unpickle_pure_python       | 224 us                                                           | 220 us: 1.02x faster                                                        |
| unpickle_list              | 4.70 us                                                          | 4.60 us: 1.02x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 101 ms: 1.02x faster                                                        |
| gc_traversal               | 4.69 ms                                                          | 4.62 ms: 1.01x faster                                                       |
| pidigits                   | 254 ms                                                           | 251 ms: 1.01x faster                                                        |
| asyncio_websockets         | 395 ms                                                           | 390 ms: 1.01x faster                                                        |
| unpickle                   | 15.7 us                                                          | 15.5 us: 1.01x faster                                                       |
| regex_v8                   | 26.0 ms                                                          | 25.8 ms: 1.01x faster                                                       |
| regex_dna                  | 249 ms                                                           | 249 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.58 sec: 1.00x slower                                                      |
| coverage                   | 83.5 ms                                                          | 84.0 ms: 1.01x slower                                                       |
| fannkuch                   | 353 ms                                                           | 356 ms: 1.01x slower                                                        |
| logging_format             | 7.11 us                                                          | 7.17 us: 1.01x slower                                                       |
| logging_silent             | 96.3 ns                                                          | 97.5 ns: 1.01x slower                                                       |
| scimark_lu                 | 97.5 ms                                                          | 98.7 ms: 1.01x slower                                                       |
| python_startup_no_site     | 8.85 ms                                                          | 8.97 ms: 1.01x slower                                                       |
| python_startup             | 13.2 ms                                                          | 13.5 ms: 1.02x slower                                                       |
| logging_simple             | 6.40 us                                                          | 6.53 us: 1.02x slower                                                       |
| tornado_http               | 119 ms                                                           | 122 ms: 1.02x slower                                                        |
| thrift                     | 880 us                                                           | 905 us: 1.03x slower                                                        |
| xml_etree_parse            | 144 ms                                                           | 148 ms: 1.03x slower                                                        |
| regex_effbot               | 3.40 ms                                                          | 3.52 ms: 1.03x slower                                                       |
| mdp                        | 2.46 sec                                                         | 2.56 sec: 1.04x slower                                                      |
| pycparser                  | 1.22 sec                                                         | 1.28 sec: 1.04x slower                                                      |
| meteor_contest             | 128 ms                                                           | 134 ms: 1.04x slower                                                        |
| scimark_monte_carlo        | 65.5 ms                                                          | 68.8 ms: 1.05x slower                                                       |
| bench_thread_pool          | 908 us                                                           | 954 us: 1.05x slower                                                        |
| pickle_pure_python         | 307 us                                                           | 324 us: 1.06x slower                                                        |
| sympy_expand               | 501 ms                                                           | 529 ms: 1.06x slower                                                        |
| regex_compile              | 144 ms                                                           | 153 ms: 1.06x slower                                                        |
| async_generators           | 363 ms                                                           | 385 ms: 1.06x slower                                                        |
| typing_runtime_protocols   | 171 us                                                           | 181 us: 1.06x slower                                                        |
| docutils                   | 2.98 sec                                                         | 3.22 sec: 1.08x slower                                                      |
| sympy_str                  | 295 ms                                                           | 319 ms: 1.08x slower                                                        |
| sqlglot_normalize          | 120 ms                                                           | 131 ms: 1.09x slower                                                        |
| 2to3                       | 291 ms                                                           | 317 ms: 1.09x slower                                                        |
| sqlglot_parse              | 1.39 ms                                                          | 1.53 ms: 1.10x slower                                                       |
| django_template            | 39.0 ms                                                          | 42.9 ms: 1.10x slower                                                       |
| comprehensions             | 17.0 us                                                          | 18.8 us: 1.11x slower                                                       |
| chaos                      | 59.6 ms                                                          | 66.4 ms: 1.11x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 1.97 ms: 1.11x slower                                                       |
| sympy_sum                  | 155 ms                                                           | 173 ms: 1.12x slower                                                        |
| hexiom                     | 6.35 ms                                                          | 7.09 ms: 1.12x slower                                                       |
| genshi_xml                 | 58.1 ms                                                          | 64.9 ms: 1.12x slower                                                       |
| nqueens                    | 88.4 ms                                                          | 99.7 ms: 1.13x slower                                                       |
| genshi_text                | 25.9 ms                                                          | 29.7 ms: 1.15x slower                                                       |
| generators                 | 33.5 ms                                                          | 38.8 ms: 1.16x slower                                                       |
| sqlglot_optimize           | 59.5 ms                                                          | 69.4 ms: 1.16x slower                                                       |
| sympy_integrate            | 23.2 ms                                                          | 27.2 ms: 1.17x slower                                                       |
| raytrace                   | 260 ms                                                           | 312 ms: 1.20x slower                                                        |
| pylint                     | 339 ms                                                           | 418 ms: 1.23x slower                                                        |
| bench_mp_pool              | 4.91 ms                                                          | 1.57 sec: 320.43x slower                                                    |
| Geometric mean             | (ref)                                                            | 1.05x slower                                                                |

Benchmark hidden because not significant (1): json_loads
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: unpack_sequence

# HPT report

- Reliability score: 72.06% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x