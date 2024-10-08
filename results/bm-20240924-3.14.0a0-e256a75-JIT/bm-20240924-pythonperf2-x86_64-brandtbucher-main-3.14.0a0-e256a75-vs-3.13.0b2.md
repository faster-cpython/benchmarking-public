# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: main
- machine: linux-x86_64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.01x faster
- HPT reliability: 84.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 311 ms: 1.07x slower                                              |
| docutils       | 2.98 sec                                                         | 3.17 sec: 1.06x slower                                            |
| html5lib       | 74.7 ms                                                          | 69.7 ms: 1.07x faster                                             |
| tornado_http   | 119 ms                                                           | 122 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                            | 1.02x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization     | 460 ms                                                           | 403 ms: 1.14x faster                                              |
| async_tree_none            | 365 ms                                                           | 323 ms: 1.13x faster                                              |
| async_tree_io_tg           | 900 ms                                                           | 813 ms: 1.11x faster                                              |
| async_tree_none_tg         | 340 ms                                                           | 309 ms: 1.10x faster                                              |
| async_tree_io              | 873 ms                                                           | 802 ms: 1.09x faster                                              |
| async_tree_memoization_tg  | 421 ms                                                           | 390 ms: 1.08x faster                                              |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 574 ms: 1.05x faster                                              |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 546 ms: 1.05x faster                                              |
| Geometric mean             | (ref)                                                            | 1.09x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 73.8 ms: 1.09x faster                                             |
| nbody          | 87.8 ms                                                          | 81.5 ms: 1.08x faster                                             |
| pidigits       | 254 ms                                                           | 251 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                            | 1.06x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 233 ms: 1.07x faster                                              |
| regex_v8       | 26.0 ms                                                          | 25.5 ms: 1.02x faster                                             |
| regex_effbot   | 3.40 ms                                                          | 3.39 ms: 1.00x faster                                             |
| regex_compile  | 144 ms                                                           | 149 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                            | 1.01x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.12 sec: 1.14x faster                                            |
| xml_etree_generate   | 85.7 ms                                                          | 79.1 ms: 1.08x faster                                             |
| xml_etree_process    | 59.7 ms                                                          | 55.9 ms: 1.07x faster                                             |
| xml_etree_iterparse  | 103 ms                                                           | 98.3 ms: 1.04x faster                                             |
| unpickle_pure_python | 224 us                                                           | 217 us: 1.04x faster                                              |
| unpickle             | 15.7 us                                                          | 15.2 us: 1.03x faster                                             |
| json_loads           | 25.0 us                                                          | 24.2 us: 1.03x faster                                             |
| json_dumps           | 10.8 ms                                                          | 10.6 ms: 1.01x faster                                             |
| pickle_dict          | 32.8 us                                                          | 32.6 us: 1.01x faster                                             |
| pickle               | 10.6 us                                                          | 10.7 us: 1.01x slower                                             |
| pickle_list          | 4.44 us                                                          | 4.55 us: 1.02x slower                                             |
| pickle_pure_python   | 307 us                                                           | 331 us: 1.08x slower                                              |
| Geometric mean       | (ref)                                                            | 1.02x faster                                                      |

Benchmark hidden because not significant (2): unpickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                             |
| python_startup_no_site | 8.85 ms                                                          | 8.99 ms: 1.02x slower                                             |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|-----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.15 ms: 1.13x faster                                             |
| django_template | 39.0 ms                                                          | 43.3 ms: 1.11x slower                                             |
| genshi_xml      | 58.1 ms                                                          | 66.8 ms: 1.15x slower                                             |
| genshi_text     | 25.9 ms                                                          | 31.1 ms: 1.20x slower                                             |
| Geometric mean  | (ref)                                                            | 1.08x slower                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------:|
| deepcopy_memo              | 37.3 us                                                          | 26.6 us: 1.40x faster                                             |
| deepcopy                   | 377 us                                                           | 297 us: 1.27x faster                                              |
| richards                   | 53.4 ms                                                          | 44.8 ms: 1.19x faster                                             |
| spectral_norm              | 97.3 ms                                                          | 81.9 ms: 1.19x faster                                             |
| richards_super             | 61.2 ms                                                          | 52.3 ms: 1.17x faster                                             |
| deepcopy_reduce            | 3.39 us                                                          | 2.97 us: 1.14x faster                                             |
| async_tree_memoization     | 460 ms                                                           | 403 ms: 1.14x faster                                              |
| tomli_loads                | 2.40 sec                                                         | 2.12 sec: 1.14x faster                                            |
| mako                       | 10.4 ms                                                          | 9.15 ms: 1.13x faster                                             |
| async_tree_none            | 365 ms                                                           | 323 ms: 1.13x faster                                              |
| scimark_sor                | 119 ms                                                           | 105 ms: 1.13x faster                                              |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 3.81 ms: 1.12x faster                                             |
| async_tree_io_tg           | 900 ms                                                           | 813 ms: 1.11x faster                                              |
| go                         | 165 ms                                                           | 149 ms: 1.11x faster                                              |
| async_tree_none_tg         | 340 ms                                                           | 309 ms: 1.10x faster                                              |
| pathlib                    | 17.1 ms                                                          | 15.7 ms: 1.09x faster                                             |
| async_tree_io              | 873 ms                                                           | 802 ms: 1.09x faster                                              |
| float                      | 80.2 ms                                                          | 73.8 ms: 1.09x faster                                             |
| scimark_fft                | 312 ms                                                           | 288 ms: 1.08x faster                                              |
| xml_etree_generate         | 85.7 ms                                                          | 79.1 ms: 1.08x faster                                             |
| bpe_tokeniser              | 5.14 sec                                                         | 4.76 sec: 1.08x faster                                            |
| async_tree_memoization_tg  | 421 ms                                                           | 390 ms: 1.08x faster                                              |
| nbody                      | 87.8 ms                                                          | 81.5 ms: 1.08x faster                                             |
| html5lib                   | 74.7 ms                                                          | 69.7 ms: 1.07x faster                                             |
| xml_etree_process          | 59.7 ms                                                          | 55.9 ms: 1.07x faster                                             |
| regex_dna                  | 249 ms                                                           | 233 ms: 1.07x faster                                              |
| gc_traversal               | 4.69 ms                                                          | 4.41 ms: 1.06x faster                                             |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 574 ms: 1.05x faster                                              |
| deltablue                  | 3.37 ms                                                          | 3.21 ms: 1.05x faster                                             |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 546 ms: 1.05x faster                                              |
| dulwich_log                | 67.3 ms                                                          | 64.2 ms: 1.05x faster                                             |
| create_gc_cycles           | 2.00 ms                                                          | 1.92 ms: 1.05x faster                                             |
| xml_etree_iterparse        | 103 ms                                                           | 98.3 ms: 1.04x faster                                             |
| unpickle_pure_python       | 224 us                                                           | 217 us: 1.04x faster                                              |
| unpickle                   | 15.7 us                                                          | 15.2 us: 1.03x faster                                             |
| json_loads                 | 25.0 us                                                          | 24.2 us: 1.03x faster                                             |
| sqlite_synth               | 2.80 us                                                          | 2.71 us: 1.03x faster                                             |
| pprint_safe_repr           | 818 ms                                                           | 792 ms: 1.03x faster                                              |
| crypto_pyaes               | 73.6 ms                                                          | 71.3 ms: 1.03x faster                                             |
| regex_v8                   | 26.0 ms                                                          | 25.5 ms: 1.02x faster                                             |
| json                       | 5.35 ms                                                          | 5.26 ms: 1.02x faster                                             |
| coverage                   | 83.5 ms                                                          | 82.0 ms: 1.02x faster                                             |
| pyflate                    | 482 ms                                                           | 474 ms: 1.02x faster                                              |
| asyncio_tcp                | 378 ms                                                           | 372 ms: 1.01x faster                                              |
| json_dumps                 | 10.8 ms                                                          | 10.6 ms: 1.01x faster                                             |
| pidigits                   | 254 ms                                                           | 251 ms: 1.01x faster                                              |
| pickle_dict                | 32.8 us                                                          | 32.6 us: 1.01x faster                                             |
| pprint_pformat             | 1.66 sec                                                         | 1.65 sec: 1.00x faster                                            |
| regex_effbot               | 3.40 ms                                                          | 3.39 ms: 1.00x faster                                             |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.58 sec: 1.00x slower                                            |
| meteor_contest             | 128 ms                                                           | 129 ms: 1.01x slower                                              |
| logging_format             | 7.11 us                                                          | 7.17 us: 1.01x slower                                             |
| thrift                     | 880 us                                                           | 887 us: 1.01x slower                                              |
| pickle                     | 10.6 us                                                          | 10.7 us: 1.01x slower                                             |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                             |
| python_startup_no_site     | 8.85 ms                                                          | 8.99 ms: 1.02x slower                                             |
| fannkuch                   | 353 ms                                                           | 360 ms: 1.02x slower                                              |
| tornado_http               | 119 ms                                                           | 122 ms: 1.02x slower                                              |
| pickle_list                | 4.44 us                                                          | 4.55 us: 1.02x slower                                             |
| logging_simple             | 6.40 us                                                          | 6.61 us: 1.03x slower                                             |
| regex_compile              | 144 ms                                                           | 149 ms: 1.03x slower                                              |
| logging_silent             | 96.3 ns                                                          | 100 ns: 1.04x slower                                              |
| scimark_monte_carlo        | 65.5 ms                                                          | 68.2 ms: 1.04x slower                                             |
| sympy_str                  | 295 ms                                                           | 308 ms: 1.04x slower                                              |
| pycparser                  | 1.22 sec                                                         | 1.29 sec: 1.05x slower                                            |
| sympy_expand               | 501 ms                                                           | 528 ms: 1.05x slower                                              |
| mdp                        | 2.46 sec                                                         | 2.60 sec: 1.06x slower                                            |
| async_generators           | 363 ms                                                           | 384 ms: 1.06x slower                                              |
| bench_mp_pool              | 4.91 ms                                                          | 5.21 ms: 1.06x slower                                             |
| docutils                   | 2.98 sec                                                         | 3.17 sec: 1.06x slower                                            |
| 2to3                       | 291 ms                                                           | 311 ms: 1.07x slower                                              |
| sqlglot_parse              | 1.39 ms                                                          | 1.49 ms: 1.07x slower                                             |
| pickle_pure_python         | 307 us                                                           | 331 us: 1.08x slower                                              |
| comprehensions             | 17.0 us                                                          | 18.3 us: 1.08x slower                                             |
| sympy_sum                  | 155 ms                                                           | 168 ms: 1.08x slower                                              |
| sqlglot_normalize          | 120 ms                                                           | 131 ms: 1.09x slower                                              |
| hexiom                     | 6.35 ms                                                          | 6.92 ms: 1.09x slower                                             |
| typing_runtime_protocols   | 171 us                                                           | 186 us: 1.09x slower                                              |
| sqlglot_optimize           | 59.5 ms                                                          | 65.7 ms: 1.10x slower                                             |
| sqlglot_transpile          | 1.76 ms                                                          | 1.95 ms: 1.10x slower                                             |
| chaos                      | 59.6 ms                                                          | 66.1 ms: 1.11x slower                                             |
| nqueens                    | 88.4 ms                                                          | 98.3 ms: 1.11x slower                                             |
| django_template            | 39.0 ms                                                          | 43.3 ms: 1.11x slower                                             |
| sympy_integrate            | 23.2 ms                                                          | 26.4 ms: 1.14x slower                                             |
| genshi_xml                 | 58.1 ms                                                          | 66.8 ms: 1.15x slower                                             |
| genshi_text                | 25.9 ms                                                          | 31.1 ms: 1.20x slower                                             |
| pylint                     | 339 ms                                                           | 410 ms: 1.21x slower                                              |
| raytrace                   | 260 ms                                                           | 318 ms: 1.22x slower                                              |
| generators                 | 33.5 ms                                                          | 42.5 ms: 1.27x slower                                             |
| Geometric mean             | (ref)                                                            | 1.01x faster                                                      |

Benchmark hidden because not significant (7): telco, unpickle_list, asyncio_websockets, xml_etree_parse, scimark_lu, coroutines, bench_thread_pool
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240924-3.14.0a0-e256a75-JIT/bm-20240924-pythonperf2-x86_64-brandtbucher-main-3.14.0a0-e256a75.json: unpack_sequence

# HPT report

- Reliability score: 84.95% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x