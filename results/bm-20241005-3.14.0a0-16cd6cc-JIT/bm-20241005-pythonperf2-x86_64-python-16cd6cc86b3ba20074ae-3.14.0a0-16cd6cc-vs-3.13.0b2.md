# Results vs. 3.13.0b2

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-x86_64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.06x slower
- HPT reliability: 69.17%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 317 ms: 1.09x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.22 sec: 1.08x slower                                                      |
| html5lib       | 74.7 ms                                                          | 71.2 ms: 1.05x faster                                                       |
| tornado_http   | 119 ms                                                           | 123 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                            | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 779 ms: 1.15x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 406 ms: 1.13x faster                                                        |
| async_tree_none            | 365 ms                                                           | 324 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 307 ms: 1.11x faster                                                        |
| async_tree_io              | 873 ms                                                           | 813 ms: 1.07x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 392 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 544 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 575 ms: 1.05x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 75.5 ms: 1.06x faster                                                       |
| nbody          | 87.8 ms                                                          | 83.6 ms: 1.05x faster                                                       |
| pidigits       | 254 ms                                                           | 254 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                            | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 252 ms: 1.01x slower                                                        |
| regex_v8       | 26.0 ms                                                          | 26.6 ms: 1.02x slower                                                       |
| regex_compile  | 144 ms                                                           | 153 ms: 1.06x slower                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.75 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                            | 1.05x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.18 sec: 1.10x faster                                                      |
| xml_etree_generate   | 85.7 ms                                                          | 78.4 ms: 1.09x faster                                                       |
| pickle_dict          | 32.8 us                                                          | 30.4 us: 1.08x faster                                                       |
| xml_etree_process    | 59.7 ms                                                          | 55.9 ms: 1.07x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                           | 97.5 ms: 1.05x faster                                                       |
| pickle_list          | 4.44 us                                                          | 4.23 us: 1.05x faster                                                       |
| json_loads           | 25.0 us                                                          | 24.0 us: 1.04x faster                                                       |
| pickle               | 10.6 us                                                          | 10.3 us: 1.03x faster                                                       |
| unpickle             | 15.7 us                                                          | 15.2 us: 1.03x faster                                                       |
| xml_etree_parse      | 144 ms                                                           | 140 ms: 1.03x faster                                                        |
| unpickle_list        | 4.70 us                                                          | 4.58 us: 1.03x faster                                                       |
| unpickle_pure_python | 224 us                                                           | 220 us: 1.02x faster                                                        |
| json_dumps           | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                       |
| pickle_pure_python   | 307 us                                                           | 330 us: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.04x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 8.98 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.15 ms: 1.13x faster                                                       |
| django_template | 39.0 ms                                                          | 41.8 ms: 1.07x slower                                                       |
| genshi_xml      | 58.1 ms                                                          | 63.6 ms: 1.10x slower                                                       |
| genshi_text     | 25.9 ms                                                          | 29.0 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 37.3 us                                                          | 28.2 us: 1.32x faster                                                       |
| deepcopy                   | 377 us                                                           | 300 us: 1.26x faster                                                        |
| richards                   | 53.4 ms                                                          | 44.7 ms: 1.20x faster                                                       |
| richards_super             | 61.2 ms                                                          | 51.8 ms: 1.18x faster                                                       |
| spectral_norm              | 97.3 ms                                                          | 82.9 ms: 1.17x faster                                                       |
| async_tree_io_tg           | 900 ms                                                           | 779 ms: 1.15x faster                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 2.95 us: 1.15x faster                                                       |
| mako                       | 10.4 ms                                                          | 9.15 ms: 1.13x faster                                                       |
| async_tree_memoization     | 460 ms                                                           | 406 ms: 1.13x faster                                                        |
| async_tree_none            | 365 ms                                                           | 324 ms: 1.13x faster                                                        |
| scimark_fft                | 312 ms                                                           | 280 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 307 ms: 1.11x faster                                                        |
| scimark_sor                | 119 ms                                                           | 107 ms: 1.11x faster                                                        |
| telco                      | 8.40 ms                                                          | 7.61 ms: 1.10x faster                                                       |
| tomli_loads                | 2.40 sec                                                         | 2.18 sec: 1.10x faster                                                      |
| xml_etree_generate         | 85.7 ms                                                          | 78.4 ms: 1.09x faster                                                       |
| gc_traversal               | 4.69 ms                                                          | 4.30 ms: 1.09x faster                                                       |
| pathlib                    | 17.1 ms                                                          | 15.7 ms: 1.09x faster                                                       |
| pprint_safe_repr           | 818 ms                                                           | 755 ms: 1.08x faster                                                        |
| pickle_dict                | 32.8 us                                                          | 30.4 us: 1.08x faster                                                       |
| async_tree_io              | 873 ms                                                           | 813 ms: 1.07x faster                                                        |
| go                         | 165 ms                                                           | 154 ms: 1.07x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 392 ms: 1.07x faster                                                        |
| create_gc_cycles           | 2.00 ms                                                          | 1.87 ms: 1.07x faster                                                       |
| bpe_tokeniser              | 5.14 sec                                                         | 4.80 sec: 1.07x faster                                                      |
| xml_etree_process          | 59.7 ms                                                          | 55.9 ms: 1.07x faster                                                       |
| float                      | 80.2 ms                                                          | 75.5 ms: 1.06x faster                                                       |
| deltablue                  | 3.37 ms                                                          | 3.21 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 544 ms: 1.05x faster                                                        |
| pprint_pformat             | 1.66 sec                                                         | 1.58 sec: 1.05x faster                                                      |
| xml_etree_iterparse        | 103 ms                                                           | 97.5 ms: 1.05x faster                                                       |
| nbody                      | 87.8 ms                                                          | 83.6 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 575 ms: 1.05x faster                                                        |
| pickle_list                | 4.44 us                                                          | 4.23 us: 1.05x faster                                                       |
| html5lib                   | 74.7 ms                                                          | 71.2 ms: 1.05x faster                                                       |
| dulwich_log                | 67.3 ms                                                          | 64.3 ms: 1.05x faster                                                       |
| json_loads                 | 25.0 us                                                          | 24.0 us: 1.04x faster                                                       |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.12 ms: 1.04x faster                                                       |
| coroutines                 | 22.0 ms                                                          | 21.2 ms: 1.04x faster                                                       |
| crypto_pyaes               | 73.6 ms                                                          | 71.1 ms: 1.03x faster                                                       |
| pickle                     | 10.6 us                                                          | 10.3 us: 1.03x faster                                                       |
| scimark_lu                 | 97.5 ms                                                          | 94.4 ms: 1.03x faster                                                       |
| unpickle                   | 15.7 us                                                          | 15.2 us: 1.03x faster                                                       |
| xml_etree_parse            | 144 ms                                                           | 140 ms: 1.03x faster                                                        |
| unpickle_list              | 4.70 us                                                          | 4.58 us: 1.03x faster                                                       |
| sqlite_synth               | 2.80 us                                                          | 2.73 us: 1.02x faster                                                       |
| unpickle_pure_python       | 224 us                                                           | 220 us: 1.02x faster                                                        |
| json                       | 5.35 ms                                                          | 5.26 ms: 1.02x faster                                                       |
| asyncio_websockets         | 395 ms                                                           | 390 ms: 1.01x faster                                                        |
| asyncio_tcp                | 378 ms                                                           | 374 ms: 1.01x faster                                                        |
| json_dumps                 | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                       |
| pyflate                    | 482 ms                                                           | 478 ms: 1.01x faster                                                        |
| pidigits                   | 254 ms                                                           | 254 ms: 1.00x slower                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.58 sec: 1.00x slower                                                      |
| coverage                   | 83.5 ms                                                          | 84.0 ms: 1.01x slower                                                       |
| regex_dna                  | 249 ms                                                           | 252 ms: 1.01x slower                                                        |
| logging_silent             | 96.3 ns                                                          | 97.3 ns: 1.01x slower                                                       |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site     | 8.85 ms                                                          | 8.98 ms: 1.01x slower                                                       |
| fannkuch                   | 353 ms                                                           | 359 ms: 1.02x slower                                                        |
| logging_format             | 7.11 us                                                          | 7.26 us: 1.02x slower                                                       |
| thrift                     | 880 us                                                           | 899 us: 1.02x slower                                                        |
| regex_v8                   | 26.0 ms                                                          | 26.6 ms: 1.02x slower                                                       |
| tornado_http               | 119 ms                                                           | 123 ms: 1.03x slower                                                        |
| meteor_contest             | 128 ms                                                           | 132 ms: 1.03x slower                                                        |
| logging_simple             | 6.40 us                                                          | 6.62 us: 1.03x slower                                                       |
| scimark_monte_carlo        | 65.5 ms                                                          | 68.2 ms: 1.04x slower                                                       |
| pycparser                  | 1.22 sec                                                         | 1.28 sec: 1.05x slower                                                      |
| bench_thread_pool          | 908 us                                                           | 952 us: 1.05x slower                                                        |
| mdp                        | 2.46 sec                                                         | 2.60 sec: 1.06x slower                                                      |
| regex_compile              | 144 ms                                                           | 153 ms: 1.06x slower                                                        |
| sympy_expand               | 501 ms                                                           | 532 ms: 1.06x slower                                                        |
| django_template            | 39.0 ms                                                          | 41.8 ms: 1.07x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 330 us: 1.07x slower                                                        |
| docutils                   | 2.98 sec                                                         | 3.22 sec: 1.08x slower                                                      |
| async_generators           | 363 ms                                                           | 392 ms: 1.08x slower                                                        |
| typing_runtime_protocols   | 171 us                                                           | 185 us: 1.08x slower                                                        |
| 2to3                       | 291 ms                                                           | 317 ms: 1.09x slower                                                        |
| sympy_str                  | 295 ms                                                           | 322 ms: 1.09x slower                                                        |
| genshi_xml                 | 58.1 ms                                                          | 63.6 ms: 1.10x slower                                                       |
| regex_effbot               | 3.40 ms                                                          | 3.75 ms: 1.10x slower                                                       |
| sqlglot_parse              | 1.39 ms                                                          | 1.54 ms: 1.11x slower                                                       |
| comprehensions             | 17.0 us                                                          | 18.8 us: 1.11x slower                                                       |
| hexiom                     | 6.35 ms                                                          | 7.08 ms: 1.11x slower                                                       |
| genshi_text                | 25.9 ms                                                          | 29.0 ms: 1.12x slower                                                       |
| sqlglot_normalize          | 120 ms                                                           | 135 ms: 1.12x slower                                                        |
| sympy_sum                  | 155 ms                                                           | 174 ms: 1.12x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                          | 1.98 ms: 1.12x slower                                                       |
| chaos                      | 59.6 ms                                                          | 67.3 ms: 1.13x slower                                                       |
| nqueens                    | 88.4 ms                                                          | 101 ms: 1.14x slower                                                        |
| generators                 | 33.5 ms                                                          | 38.4 ms: 1.15x slower                                                       |
| sympy_integrate            | 23.2 ms                                                          | 27.3 ms: 1.18x slower                                                       |
| sqlglot_optimize           | 59.5 ms                                                          | 70.2 ms: 1.18x slower                                                       |
| raytrace                   | 260 ms                                                           | 320 ms: 1.23x slower                                                        |
| pylint                     | 339 ms                                                           | 419 ms: 1.23x slower                                                        |
| bench_mp_pool              | 4.91 ms                                                          | 1.87 sec: 381.05x slower                                                    |
| Geometric mean             | (ref)                                                            | 1.06x slower                                                                |
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241005-3.14.0a0-16cd6cc-JIT/bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: unpack_sequence

# HPT report

- Reliability score: 69.17% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x