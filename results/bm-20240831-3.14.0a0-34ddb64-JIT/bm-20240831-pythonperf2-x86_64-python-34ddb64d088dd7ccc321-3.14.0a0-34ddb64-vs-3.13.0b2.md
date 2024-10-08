# Results vs. 3.13.0b2

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-x86_64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.01x faster
- HPT reliability: 82.33%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 310 ms: 1.06x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.16 sec: 1.06x slower                                                      |
| html5lib       | 74.7 ms                                                          | 68.9 ms: 1.08x faster                                                       |
| tornado_http   | 119 ms                                                           | 121 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                            | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 460 ms                                                           | 401 ms: 1.15x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 798 ms: 1.13x faster                                                        |
| async_tree_none            | 365 ms                                                           | 330 ms: 1.11x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 315 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 567 ms: 1.07x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 396 ms: 1.06x faster                                                        |
| async_tree_io              | 873 ms                                                           | 840 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 556 ms: 1.03x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.08x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 75.7 ms: 1.06x faster                                                       |
| pidigits       | 254 ms                                                           | 250 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 234 ms: 1.07x faster                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.33 ms: 1.02x faster                                                       |
| regex_v8       | 26.0 ms                                                          | 25.9 ms: 1.00x faster                                                       |
| regex_compile  | 144 ms                                                           | 147 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.15 sec: 1.12x faster                                                      |
| xml_etree_generate   | 85.7 ms                                                          | 79.0 ms: 1.09x faster                                                       |
| xml_etree_process    | 59.7 ms                                                          | 55.3 ms: 1.08x faster                                                       |
| unpickle_pure_python | 224 us                                                           | 212 us: 1.06x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 98.6 ms: 1.04x faster                                                       |
| json_dumps           | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                       |
| pickle_pure_python   | 307 us                                                           | 320 us: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.04x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.09 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.23 ms: 1.12x faster                                                       |
| genshi_xml      | 58.1 ms                                                          | 61.3 ms: 1.06x slower                                                       |
| django_template | 39.0 ms                                                          | 42.4 ms: 1.09x slower                                                       |
| genshi_text     | 25.9 ms                                                          | 29.4 ms: 1.13x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 37.3 us                                                          | 26.7 us: 1.40x faster                                                       |
| deepcopy                   | 377 us                                                           | 303 us: 1.24x faster                                                        |
| richards                   | 53.4 ms                                                          | 43.7 ms: 1.22x faster                                                       |
| richards_super             | 61.2 ms                                                          | 50.3 ms: 1.22x faster                                                       |
| spectral_norm              | 97.3 ms                                                          | 81.4 ms: 1.20x faster                                                       |
| deepcopy_reduce            | 3.39 us                                                          | 2.94 us: 1.15x faster                                                       |
| async_tree_memoization     | 460 ms                                                           | 401 ms: 1.15x faster                                                        |
| scimark_sor                | 119 ms                                                           | 105 ms: 1.13x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 798 ms: 1.13x faster                                                        |
| mako                       | 10.4 ms                                                          | 9.23 ms: 1.12x faster                                                       |
| tomli_loads                | 2.40 sec                                                         | 2.15 sec: 1.12x faster                                                      |
| async_tree_none            | 365 ms                                                           | 330 ms: 1.11x faster                                                        |
| bpe_tokeniser              | 5.14 sec                                                         | 4.73 sec: 1.09x faster                                                      |
| xml_etree_generate         | 85.7 ms                                                          | 79.0 ms: 1.09x faster                                                       |
| go                         | 165 ms                                                           | 152 ms: 1.08x faster                                                        |
| html5lib                   | 74.7 ms                                                          | 68.9 ms: 1.08x faster                                                       |
| async_tree_none_tg         | 340 ms                                                           | 315 ms: 1.08x faster                                                        |
| xml_etree_process          | 59.7 ms                                                          | 55.3 ms: 1.08x faster                                                       |
| pathlib                    | 17.1 ms                                                          | 15.9 ms: 1.07x faster                                                       |
| scimark_fft                | 312 ms                                                           | 291 ms: 1.07x faster                                                        |
| gc_traversal               | 4.69 ms                                                          | 4.38 ms: 1.07x faster                                                       |
| regex_dna                  | 249 ms                                                           | 234 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 567 ms: 1.07x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 396 ms: 1.06x faster                                                        |
| deltablue                  | 3.37 ms                                                          | 3.18 ms: 1.06x faster                                                       |
| float                      | 80.2 ms                                                          | 75.7 ms: 1.06x faster                                                       |
| unpickle_pure_python       | 224 us                                                           | 212 us: 1.06x faster                                                        |
| crypto_pyaes               | 73.6 ms                                                          | 69.7 ms: 1.06x faster                                                       |
| coverage                   | 83.5 ms                                                          | 79.2 ms: 1.05x faster                                                       |
| create_gc_cycles           | 2.00 ms                                                          | 1.91 ms: 1.05x faster                                                       |
| pprint_safe_repr           | 818 ms                                                           | 780 ms: 1.05x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                           | 98.6 ms: 1.04x faster                                                       |
| async_tree_io              | 873 ms                                                           | 840 ms: 1.04x faster                                                        |
| telco                      | 8.40 ms                                                          | 8.11 ms: 1.04x faster                                                       |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.14 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 556 ms: 1.03x faster                                                        |
| pyflate                    | 482 ms                                                           | 468 ms: 1.03x faster                                                        |
| dulwich_log                | 67.3 ms                                                          | 65.8 ms: 1.02x faster                                                       |
| regex_effbot               | 3.40 ms                                                          | 3.33 ms: 1.02x faster                                                       |
| pprint_pformat             | 1.66 sec                                                         | 1.63 sec: 1.02x faster                                                      |
| logging_format             | 7.11 us                                                          | 7.00 us: 1.02x faster                                                       |
| asyncio_tcp                | 378 ms                                                           | 372 ms: 1.01x faster                                                        |
| pidigits                   | 254 ms                                                           | 250 ms: 1.01x faster                                                        |
| json_dumps                 | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                       |
| scimark_lu                 | 97.5 ms                                                          | 96.7 ms: 1.01x faster                                                       |
| fannkuch                   | 353 ms                                                           | 350 ms: 1.01x faster                                                        |
| logging_simple             | 6.40 us                                                          | 6.36 us: 1.01x faster                                                       |
| regex_v8                   | 26.0 ms                                                          | 25.9 ms: 1.00x faster                                                       |
| meteor_contest             | 128 ms                                                           | 128 ms: 1.00x faster                                                        |
| coroutines                 | 22.0 ms                                                          | 22.1 ms: 1.01x slower                                                       |
| tornado_http               | 119 ms                                                           | 121 ms: 1.01x slower                                                        |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| thrift                     | 880 us                                                           | 894 us: 1.02x slower                                                        |
| bench_thread_pool          | 908 us                                                           | 925 us: 1.02x slower                                                        |
| regex_compile              | 144 ms                                                           | 147 ms: 1.02x slower                                                        |
| pycparser                  | 1.22 sec                                                         | 1.25 sec: 1.03x slower                                                      |
| python_startup_no_site     | 8.85 ms                                                          | 9.09 ms: 1.03x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 320 us: 1.04x slower                                                        |
| logging_silent             | 96.3 ns                                                          | 100 ns: 1.04x slower                                                        |
| scimark_monte_carlo        | 65.5 ms                                                          | 68.6 ms: 1.05x slower                                                       |
| mdp                        | 2.46 sec                                                         | 2.59 sec: 1.05x slower                                                      |
| async_generators           | 363 ms                                                           | 382 ms: 1.05x slower                                                        |
| sympy_expand               | 501 ms                                                           | 528 ms: 1.05x slower                                                        |
| genshi_xml                 | 58.1 ms                                                          | 61.3 ms: 1.06x slower                                                       |
| sympy_str                  | 295 ms                                                           | 311 ms: 1.06x slower                                                        |
| bench_mp_pool              | 4.91 ms                                                          | 5.20 ms: 1.06x slower                                                       |
| docutils                   | 2.98 sec                                                         | 3.16 sec: 1.06x slower                                                      |
| 2to3                       | 291 ms                                                           | 310 ms: 1.06x slower                                                        |
| typing_runtime_protocols   | 171 us                                                           | 182 us: 1.07x slower                                                        |
| sqlglot_parse              | 1.39 ms                                                          | 1.50 ms: 1.08x slower                                                       |
| sqlglot_normalize          | 120 ms                                                           | 130 ms: 1.08x slower                                                        |
| django_template            | 39.0 ms                                                          | 42.4 ms: 1.09x slower                                                       |
| comprehensions             | 17.0 us                                                          | 18.5 us: 1.09x slower                                                       |
| sympy_sum                  | 155 ms                                                           | 170 ms: 1.10x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                          | 1.94 ms: 1.10x slower                                                       |
| hexiom                     | 6.35 ms                                                          | 7.00 ms: 1.10x slower                                                       |
| sqlglot_optimize           | 59.5 ms                                                          | 65.6 ms: 1.10x slower                                                       |
| generators                 | 33.5 ms                                                          | 37.2 ms: 1.11x slower                                                       |
| nqueens                    | 88.4 ms                                                          | 98.2 ms: 1.11x slower                                                       |
| chaos                      | 59.6 ms                                                          | 67.6 ms: 1.13x slower                                                       |
| genshi_text                | 25.9 ms                                                          | 29.4 ms: 1.13x slower                                                       |
| sympy_integrate            | 23.2 ms                                                          | 26.4 ms: 1.14x slower                                                       |
| raytrace                   | 260 ms                                                           | 309 ms: 1.19x slower                                                        |
| pylint                     | 339 ms                                                           | 409 ms: 1.21x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (6): xml_etree_parse, asyncio_tcp_ssl, json_loads, json, asyncio_websockets, nbody
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 82.33% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x