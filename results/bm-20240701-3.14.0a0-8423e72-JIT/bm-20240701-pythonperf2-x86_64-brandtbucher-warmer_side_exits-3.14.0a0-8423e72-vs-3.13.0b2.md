# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: warmer_side_exits
- machine: linux-x86_64
- commit hash: 8423e72
- commit date: 2024-07-01
- overall geometric mean: 1.01x faster
- HPT reliability: 54.80%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 309 ms: 1.06x slower                                                           |
| docutils       | 2.98 sec                                                         | 3.14 sec: 1.05x slower                                                         |
| html5lib       | 74.7 ms                                                          | 73.0 ms: 1.02x faster                                                          |
| tornado_http   | 119 ms                                                           | 121 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                            | 1.03x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 796 ms: 1.13x faster                                                           |
| async_tree_memoization     | 460 ms                                                           | 410 ms: 1.12x faster                                                           |
| async_tree_none_tg         | 340 ms                                                           | 307 ms: 1.11x faster                                                           |
| async_tree_memoization_tg  | 421 ms                                                           | 389 ms: 1.08x faster                                                           |
| async_tree_io              | 873 ms                                                           | 808 ms: 1.08x faster                                                           |
| async_tree_none            | 365 ms                                                           | 343 ms: 1.06x faster                                                           |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 543 ms: 1.05x faster                                                           |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 584 ms: 1.04x faster                                                           |
| Geometric mean             | (ref)                                                            | 1.08x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 75.2 ms: 1.07x faster                                                          |
| nbody          | 87.8 ms                                                          | 83.1 ms: 1.06x faster                                                          |
| pidigits       | 254 ms                                                           | 250 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                            | 1.04x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 138 ms: 1.04x faster                                                           |
| regex_dna      | 249 ms                                                           | 240 ms: 1.04x faster                                                           |
| regex_v8       | 26.0 ms                                                          | 25.5 ms: 1.02x faster                                                          |
| regex_effbot   | 3.40 ms                                                          | 3.66 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.10 sec: 1.15x faster                                                         |
| unpickle_pure_python | 224 us                                                           | 202 us: 1.11x faster                                                           |
| xml_etree_generate   | 85.7 ms                                                          | 82.5 ms: 1.04x faster                                                          |
| xml_etree_iterparse  | 103 ms                                                           | 98.9 ms: 1.04x faster                                                          |
| xml_etree_process    | 59.7 ms                                                          | 58.3 ms: 1.02x faster                                                          |
| xml_etree_parse      | 144 ms                                                           | 143 ms: 1.00x faster                                                           |
| json_loads           | 25.0 us                                                          | 25.2 us: 1.01x slower                                                          |
| pickle_pure_python   | 307 us                                                           | 317 us: 1.03x slower                                                           |
| Geometric mean       | (ref)                                                            | 1.03x faster                                                                   |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.02x slower                                                          |
| python_startup_no_site | 8.85 ms                                                          | 9.11 ms: 1.03x slower                                                          |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|-----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 8.97 ms: 1.16x faster                                                          |
| genshi_text     | 25.9 ms                                                          | 27.2 ms: 1.05x slower                                                          |
| genshi_xml      | 58.1 ms                                                          | 62.0 ms: 1.07x slower                                                          |
| django_template | 39.0 ms                                                          | 42.2 ms: 1.08x slower                                                          |
| Geometric mean  | (ref)                                                            | 1.01x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf2-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 37.3 us                                                          | 29.1 us: 1.28x faster                                                          |
| deepcopy                   | 377 us                                                           | 307 us: 1.23x faster                                                           |
| spectral_norm              | 97.3 ms                                                          | 83.2 ms: 1.17x faster                                                          |
| richards                   | 53.4 ms                                                          | 45.8 ms: 1.17x faster                                                          |
| mako                       | 10.4 ms                                                          | 8.97 ms: 1.16x faster                                                          |
| richards_super             | 61.2 ms                                                          | 53.1 ms: 1.15x faster                                                          |
| tomli_loads                | 2.40 sec                                                         | 2.10 sec: 1.15x faster                                                         |
| async_tree_io_tg           | 900 ms                                                           | 796 ms: 1.13x faster                                                           |
| async_tree_memoization     | 460 ms                                                           | 410 ms: 1.12x faster                                                           |
| deepcopy_reduce            | 3.39 us                                                          | 3.06 us: 1.11x faster                                                          |
| unpickle_pure_python       | 224 us                                                           | 202 us: 1.11x faster                                                           |
| async_tree_none_tg         | 340 ms                                                           | 307 ms: 1.11x faster                                                           |
| pyflate                    | 482 ms                                                           | 443 ms: 1.09x faster                                                           |
| async_tree_memoization_tg  | 421 ms                                                           | 389 ms: 1.08x faster                                                           |
| async_tree_io              | 873 ms                                                           | 808 ms: 1.08x faster                                                           |
| float                      | 80.2 ms                                                          | 75.2 ms: 1.07x faster                                                          |
| async_tree_none            | 365 ms                                                           | 343 ms: 1.06x faster                                                           |
| scimark_fft                | 312 ms                                                           | 293 ms: 1.06x faster                                                           |
| pathlib                    | 17.1 ms                                                          | 16.1 ms: 1.06x faster                                                          |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.05 ms: 1.06x faster                                                          |
| nbody                      | 87.8 ms                                                          | 83.1 ms: 1.06x faster                                                          |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 543 ms: 1.05x faster                                                           |
| regex_compile              | 144 ms                                                           | 138 ms: 1.04x faster                                                           |
| gc_traversal               | 4.69 ms                                                          | 4.49 ms: 1.04x faster                                                          |
| regex_dna                  | 249 ms                                                           | 240 ms: 1.04x faster                                                           |
| xml_etree_generate         | 85.7 ms                                                          | 82.5 ms: 1.04x faster                                                          |
| coroutines                 | 22.0 ms                                                          | 21.2 ms: 1.04x faster                                                          |
| telco                      | 8.40 ms                                                          | 8.10 ms: 1.04x faster                                                          |
| xml_etree_iterparse        | 103 ms                                                           | 98.9 ms: 1.04x faster                                                          |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 584 ms: 1.04x faster                                                           |
| crypto_pyaes               | 73.6 ms                                                          | 71.2 ms: 1.03x faster                                                          |
| create_gc_cycles           | 2.00 ms                                                          | 1.95 ms: 1.03x faster                                                          |
| pprint_safe_repr           | 818 ms                                                           | 797 ms: 1.03x faster                                                           |
| xml_etree_process          | 59.7 ms                                                          | 58.3 ms: 1.02x faster                                                          |
| html5lib                   | 74.7 ms                                                          | 73.0 ms: 1.02x faster                                                          |
| regex_v8                   | 26.0 ms                                                          | 25.5 ms: 1.02x faster                                                          |
| coverage                   | 83.5 ms                                                          | 82.0 ms: 1.02x faster                                                          |
| pprint_pformat             | 1.66 sec                                                         | 1.64 sec: 1.01x faster                                                         |
| dulwich_log                | 67.3 ms                                                          | 66.4 ms: 1.01x faster                                                          |
| pidigits                   | 254 ms                                                           | 250 ms: 1.01x faster                                                           |
| xml_etree_parse            | 144 ms                                                           | 143 ms: 1.00x faster                                                           |
| bpe_tokeniser              | 5.14 sec                                                         | 5.15 sec: 1.00x slower                                                         |
| go                         | 165 ms                                                           | 165 ms: 1.00x slower                                                           |
| asyncio_tcp                | 378 ms                                                           | 380 ms: 1.01x slower                                                           |
| json_loads                 | 25.0 us                                                          | 25.2 us: 1.01x slower                                                          |
| scimark_monte_carlo        | 65.5 ms                                                          | 65.9 ms: 1.01x slower                                                          |
| thrift                     | 880 us                                                           | 889 us: 1.01x slower                                                           |
| tornado_http               | 119 ms                                                           | 121 ms: 1.01x slower                                                           |
| asyncio_websockets         | 395 ms                                                           | 401 ms: 1.01x slower                                                           |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.02x slower                                                          |
| meteor_contest             | 128 ms                                                           | 131 ms: 1.02x slower                                                           |
| bench_thread_pool          | 908 us                                                           | 926 us: 1.02x slower                                                           |
| dask                       | 391 ms                                                           | 399 ms: 1.02x slower                                                           |
| sqlglot_parse              | 1.39 ms                                                          | 1.42 ms: 1.02x slower                                                          |
| json                       | 5.35 ms                                                          | 5.47 ms: 1.02x slower                                                          |
| python_startup_no_site     | 8.85 ms                                                          | 9.11 ms: 1.03x slower                                                          |
| mdp                        | 2.46 sec                                                         | 2.54 sec: 1.03x slower                                                         |
| pickle_pure_python         | 307 us                                                           | 317 us: 1.03x slower                                                           |
| sqlglot_transpile          | 1.76 ms                                                          | 1.82 ms: 1.03x slower                                                          |
| generators                 | 33.5 ms                                                          | 35.2 ms: 1.05x slower                                                          |
| genshi_text                | 25.9 ms                                                          | 27.2 ms: 1.05x slower                                                          |
| logging_silent             | 96.3 ns                                                          | 101 ns: 1.05x slower                                                           |
| docutils                   | 2.98 sec                                                         | 3.14 sec: 1.05x slower                                                         |
| sympy_expand               | 501 ms                                                           | 528 ms: 1.05x slower                                                           |
| pycparser                  | 1.22 sec                                                         | 1.29 sec: 1.05x slower                                                         |
| hexiom                     | 6.35 ms                                                          | 6.70 ms: 1.05x slower                                                          |
| sympy_str                  | 295 ms                                                           | 311 ms: 1.06x slower                                                           |
| sqlglot_optimize           | 59.5 ms                                                          | 63.1 ms: 1.06x slower                                                          |
| 2to3                       | 291 ms                                                           | 309 ms: 1.06x slower                                                           |
| sqlglot_normalize          | 120 ms                                                           | 128 ms: 1.06x slower                                                           |
| async_generators           | 363 ms                                                           | 385 ms: 1.06x slower                                                           |
| genshi_xml                 | 58.1 ms                                                          | 62.0 ms: 1.07x slower                                                          |
| regex_effbot               | 3.40 ms                                                          | 3.66 ms: 1.08x slower                                                          |
| sympy_sum                  | 155 ms                                                           | 167 ms: 1.08x slower                                                           |
| typing_runtime_protocols   | 171 us                                                           | 184 us: 1.08x slower                                                           |
| nqueens                    | 88.4 ms                                                          | 95.5 ms: 1.08x slower                                                          |
| django_template            | 39.0 ms                                                          | 42.2 ms: 1.08x slower                                                          |
| comprehensions             | 17.0 us                                                          | 18.5 us: 1.09x slower                                                          |
| scimark_sor                | 119 ms                                                           | 132 ms: 1.11x slower                                                           |
| sympy_integrate            | 23.2 ms                                                          | 26.0 ms: 1.12x slower                                                          |
| chaos                      | 59.6 ms                                                          | 67.0 ms: 1.12x slower                                                          |
| deltablue                  | 3.37 ms                                                          | 3.80 ms: 1.13x slower                                                          |
| pylint                     | 339 ms                                                           | 385 ms: 1.13x slower                                                           |
| raytrace                   | 260 ms                                                           | 300 ms: 1.15x slower                                                           |
| scimark_lu                 | 97.5 ms                                                          | 115 ms: 1.18x slower                                                           |
| Geometric mean             | (ref)                                                            | 1.01x faster                                                                   |

Benchmark hidden because not significant (6): bench_mp_pool, fannkuch, json_dumps, asyncio_tcp_ssl, logging_simple, logging_format
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 54.80% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x