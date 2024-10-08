# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: nojit
- machine: linux-x86_64
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.02x faster
- HPT reliability: 99.75%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 282 ms: 1.03x faster                                               |
| docutils       | 2.98 sec                                                         | 2.91 sec: 1.02x faster                                             |
| html5lib       | 74.7 ms                                                          | 70.9 ms: 1.05x faster                                              |
| tornado_http   | 119 ms                                                           | 116 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                            | 1.04x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 774 ms: 1.16x faster                                               |
| async_tree_memoization     | 460 ms                                                           | 397 ms: 1.16x faster                                               |
| async_tree_none            | 365 ms                                                           | 319 ms: 1.14x faster                                               |
| async_tree_none_tg         | 340 ms                                                           | 307 ms: 1.11x faster                                               |
| async_tree_memoization_tg  | 421 ms                                                           | 389 ms: 1.08x faster                                               |
| async_tree_io              | 873 ms                                                           | 818 ms: 1.07x faster                                               |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 569 ms: 1.06x faster                                               |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 559 ms: 1.02x faster                                               |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 79.6 ms: 1.01x faster                                              |
| pidigits       | 254 ms                                                           | 253 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                            | 1.00x slower                                                       |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 237 ms: 1.05x faster                                               |
| regex_v8       | 26.0 ms                                                          | 25.0 ms: 1.04x faster                                              |
| regex_compile  | 144 ms                                                           | 139 ms: 1.04x faster                                               |
| regex_effbot   | 3.40 ms                                                          | 3.51 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                            | 1.02x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_dict          | 32.8 us                                                          | 30.3 us: 1.08x faster                                              |
| pickle_list          | 4.44 us                                                          | 4.18 us: 1.06x faster                                              |
| unpickle_pure_python | 224 us                                                           | 216 us: 1.04x faster                                               |
| pickle               | 10.6 us                                                          | 10.3 us: 1.03x faster                                              |
| unpickle             | 15.7 us                                                          | 15.5 us: 1.01x faster                                              |
| json_loads           | 25.0 us                                                          | 24.8 us: 1.01x faster                                              |
| xml_etree_generate   | 85.7 ms                                                          | 84.8 ms: 1.01x faster                                              |
| xml_etree_iterparse  | 103 ms                                                           | 101 ms: 1.01x faster                                               |
| xml_etree_process    | 59.7 ms                                                          | 59.2 ms: 1.01x faster                                              |
| xml_etree_parse      | 144 ms                                                           | 145 ms: 1.01x slower                                               |
| json_dumps           | 10.8 ms                                                          | 10.9 ms: 1.01x slower                                              |
| unpickle_list        | 4.70 us                                                          | 4.81 us: 1.02x slower                                              |
| pickle_pure_python   | 307 us                                                           | 323 us: 1.05x slower                                               |
| tomli_loads          | 2.40 sec                                                         | 2.58 sec: 1.07x slower                                             |
| Geometric mean       | (ref)                                                            | 1.01x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                              |
| python_startup_no_site | 8.85 ms                                                          | 8.98 ms: 1.01x slower                                              |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 55.4 ms: 1.05x faster                                              |
| genshi_text     | 25.9 ms                                                          | 24.8 ms: 1.05x faster                                              |
| django_template | 39.0 ms                                                          | 39.6 ms: 1.02x slower                                              |
| mako            | 10.4 ms                                                          | 10.6 ms: 1.02x slower                                              |
| Geometric mean  | (ref)                                                            | 1.01x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 291 us: 1.30x faster                                               |
| deepcopy_memo              | 37.3 us                                                          | 30.1 us: 1.24x faster                                              |
| go                         | 165 ms                                                           | 135 ms: 1.22x faster                                               |
| generators                 | 33.5 ms                                                          | 28.8 ms: 1.16x faster                                              |
| async_tree_io_tg           | 900 ms                                                           | 774 ms: 1.16x faster                                               |
| async_tree_memoization     | 460 ms                                                           | 397 ms: 1.16x faster                                               |
| async_tree_none            | 365 ms                                                           | 319 ms: 1.14x faster                                               |
| deepcopy_reduce            | 3.39 us                                                          | 2.97 us: 1.14x faster                                              |
| async_tree_none_tg         | 340 ms                                                           | 307 ms: 1.11x faster                                               |
| richards_super             | 61.2 ms                                                          | 55.8 ms: 1.10x faster                                              |
| pickle_dict                | 32.8 us                                                          | 30.3 us: 1.08x faster                                              |
| pathlib                    | 17.1 ms                                                          | 15.8 ms: 1.08x faster                                              |
| async_tree_memoization_tg  | 421 ms                                                           | 389 ms: 1.08x faster                                               |
| richards                   | 53.4 ms                                                          | 50.0 ms: 1.07x faster                                              |
| async_tree_io              | 873 ms                                                           | 818 ms: 1.07x faster                                               |
| pickle_list                | 4.44 us                                                          | 4.18 us: 1.06x faster                                              |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 569 ms: 1.06x faster                                               |
| bench_mp_pool              | 4.91 ms                                                          | 4.63 ms: 1.06x faster                                              |
| regex_dna                  | 249 ms                                                           | 237 ms: 1.05x faster                                               |
| html5lib                   | 74.7 ms                                                          | 70.9 ms: 1.05x faster                                              |
| genshi_xml                 | 58.1 ms                                                          | 55.4 ms: 1.05x faster                                              |
| genshi_text                | 25.9 ms                                                          | 24.8 ms: 1.05x faster                                              |
| bpe_tokeniser              | 5.14 sec                                                         | 4.94 sec: 1.04x faster                                             |
| regex_v8                   | 26.0 ms                                                          | 25.0 ms: 1.04x faster                                              |
| unpickle_pure_python       | 224 us                                                           | 216 us: 1.04x faster                                               |
| regex_compile              | 144 ms                                                           | 139 ms: 1.04x faster                                               |
| 2to3                       | 291 ms                                                           | 282 ms: 1.03x faster                                               |
| tornado_http               | 119 ms                                                           | 116 ms: 1.03x faster                                               |
| pickle                     | 10.6 us                                                          | 10.3 us: 1.03x faster                                              |
| docutils                   | 2.98 sec                                                         | 2.91 sec: 1.02x faster                                             |
| json                       | 5.35 ms                                                          | 5.23 ms: 1.02x faster                                              |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 559 ms: 1.02x faster                                               |
| sympy_sum                  | 155 ms                                                           | 152 ms: 1.02x faster                                               |
| sqlite_synth               | 2.80 us                                                          | 2.75 us: 1.02x faster                                              |
| asyncio_tcp                | 378 ms                                                           | 371 ms: 1.02x faster                                               |
| hexiom                     | 6.35 ms                                                          | 6.26 ms: 1.01x faster                                              |
| unpickle                   | 15.7 us                                                          | 15.5 us: 1.01x faster                                              |
| dulwich_log                | 67.3 ms                                                          | 66.5 ms: 1.01x faster                                              |
| sympy_str                  | 295 ms                                                           | 291 ms: 1.01x faster                                               |
| json_loads                 | 25.0 us                                                          | 24.8 us: 1.01x faster                                              |
| xml_etree_generate         | 85.7 ms                                                          | 84.8 ms: 1.01x faster                                              |
| xml_etree_iterparse        | 103 ms                                                           | 101 ms: 1.01x faster                                               |
| meteor_contest             | 128 ms                                                           | 127 ms: 1.01x faster                                               |
| xml_etree_process          | 59.7 ms                                                          | 59.2 ms: 1.01x faster                                              |
| asyncio_websockets         | 395 ms                                                           | 391 ms: 1.01x faster                                               |
| sympy_expand               | 501 ms                                                           | 497 ms: 1.01x faster                                               |
| sqlglot_optimize           | 59.5 ms                                                          | 59.1 ms: 1.01x faster                                              |
| sqlglot_normalize          | 120 ms                                                           | 119 ms: 1.01x faster                                               |
| float                      | 80.2 ms                                                          | 79.6 ms: 1.01x faster                                              |
| sympy_integrate            | 23.2 ms                                                          | 23.1 ms: 1.00x faster                                              |
| pprint_safe_repr           | 818 ms                                                           | 815 ms: 1.00x faster                                               |
| pidigits                   | 254 ms                                                           | 253 ms: 1.00x faster                                               |
| spectral_norm              | 97.3 ms                                                          | 97.6 ms: 1.00x slower                                              |
| pyflate                    | 482 ms                                                           | 483 ms: 1.00x slower                                               |
| gc_traversal               | 4.69 ms                                                          | 4.70 ms: 1.00x slower                                              |
| typing_runtime_protocols   | 171 us                                                           | 172 us: 1.01x slower                                               |
| pprint_pformat             | 1.66 sec                                                         | 1.68 sec: 1.01x slower                                             |
| xml_etree_parse            | 144 ms                                                           | 145 ms: 1.01x slower                                               |
| deltablue                  | 3.37 ms                                                          | 3.42 ms: 1.01x slower                                              |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                              |
| python_startup_no_site     | 8.85 ms                                                          | 8.98 ms: 1.01x slower                                              |
| json_dumps                 | 10.8 ms                                                          | 10.9 ms: 1.01x slower                                              |
| django_template            | 39.0 ms                                                          | 39.6 ms: 1.02x slower                                              |
| scimark_lu                 | 97.5 ms                                                          | 99.2 ms: 1.02x slower                                              |
| mako                       | 10.4 ms                                                          | 10.6 ms: 1.02x slower                                              |
| mdp                        | 2.46 sec                                                         | 2.51 sec: 1.02x slower                                             |
| unpickle_list              | 4.70 us                                                          | 4.81 us: 1.02x slower                                              |
| sqlglot_parse              | 1.39 ms                                                          | 1.43 ms: 1.03x slower                                              |
| logging_simple             | 6.40 us                                                          | 6.58 us: 1.03x slower                                              |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.40 ms: 1.03x slower                                              |
| sqlglot_transpile          | 1.76 ms                                                          | 1.81 ms: 1.03x slower                                              |
| scimark_monte_carlo        | 65.5 ms                                                          | 67.4 ms: 1.03x slower                                              |
| coverage                   | 83.5 ms                                                          | 86.1 ms: 1.03x slower                                              |
| regex_effbot               | 3.40 ms                                                          | 3.51 ms: 1.03x slower                                              |
| fannkuch                   | 353 ms                                                           | 365 ms: 1.03x slower                                               |
| nqueens                    | 88.4 ms                                                          | 91.4 ms: 1.03x slower                                              |
| logging_silent             | 96.3 ns                                                          | 100 ns: 1.04x slower                                               |
| comprehensions             | 17.0 us                                                          | 17.7 us: 1.04x slower                                              |
| chaos                      | 59.6 ms                                                          | 62.5 ms: 1.05x slower                                              |
| pickle_pure_python         | 307 us                                                           | 323 us: 1.05x slower                                               |
| raytrace                   | 260 ms                                                           | 275 ms: 1.06x slower                                               |
| tomli_loads                | 2.40 sec                                                         | 2.58 sec: 1.07x slower                                             |
| scimark_sor                | 119 ms                                                           | 129 ms: 1.09x slower                                               |
| Geometric mean             | (ref)                                                            | 1.02x faster                                                       |

Benchmark hidden because not significant (13): scimark_fft, bench_thread_pool, create_gc_cycles, thrift, crypto_pyaes, coroutines, async_generators, asyncio_tcp_ssl, pycparser, logging_format, telco, nbody, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240921-3.14.0a0-a6f1035/bm-20240921-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a0-a6f1035.json: unpack_sequence

# HPT report

- Reliability score: 99.75% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x