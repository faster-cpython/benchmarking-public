# Results vs. 3.13.0b2

- fork: nohlson
- ref: enable_no_impact_def
- machine: linux-x86_64
- commit hash: 98d9ea0
- commit date: 2024-06-20
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 265 ms: 1.03x faster                                                   |
| docutils       | 2.83 sec                                                   | 2.71 sec: 1.04x faster                                                 |
| tornado_http   | 94.6 ms                                                    | 91.6 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                      | 1.03x faster                                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 936 ms                                                     | 877 ms: 1.07x faster                                                   |
| async_tree_none            | 378 ms                                                     | 366 ms: 1.03x faster                                                   |
| async_tree_none_tg         | 336 ms                                                     | 327 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 572 ms: 1.03x faster                                                   |
| async_tree_io              | 939 ms                                                     | 974 ms: 1.04x slower                                                   |
| Geometric mean             | (ref)                                                      | 1.02x faster                                                           |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 76.6 ms: 1.03x faster                                                  |
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                   |
| nbody          | 88.3 ms                                                    | 91.9 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                      | 1.00x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 132 ms: 1.04x faster                                                   |
| regex_effbot   | 3.67 ms                                                    | 3.55 ms: 1.03x faster                                                  |
| regex_v8       | 25.1 ms                                                    | 24.6 ms: 1.02x faster                                                  |
| regex_dna      | 221 ms                                                     | 224 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                      | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                  |
| xml_etree_parse      | 162 ms                                                     | 157 ms: 1.03x faster                                                   |
| xml_etree_process    | 61.2 ms                                                    | 59.3 ms: 1.03x faster                                                  |
| xml_etree_generate   | 87.4 ms                                                    | 84.9 ms: 1.03x faster                                                  |
| pickle               | 11.5 us                                                    | 11.3 us: 1.02x faster                                                  |
| json_loads           | 28.9 us                                                    | 28.5 us: 1.02x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                     | 106 ms: 1.01x faster                                                   |
| pickle_pure_python   | 305 us                                                     | 301 us: 1.01x faster                                                   |
| unpickle_pure_python | 218 us                                                     | 217 us: 1.00x faster                                                   |
| unpickle_list        | 5.34 us                                                    | 5.37 us: 1.00x slower                                                  |
| tomli_loads          | 2.12 sec                                                   | 2.14 sec: 1.01x slower                                                 |
| unpickle             | 15.1 us                                                    | 15.7 us: 1.04x slower                                                  |
| pickle_dict          | 34.8 us                                                    | 36.6 us: 1.05x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.01x faster                                                           |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.4 ms: 1.03x faster                                                  |
| python_startup_no_site | 7.11 ms                                                    | 6.93 ms: 1.03x faster                                                  |
| Geometric mean         | (ref)                                                      | 1.03x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 23.1 ms: 1.02x faster                                                  |
| genshi_xml      | 51.6 ms                                                    | 50.5 ms: 1.02x faster                                                  |
| django_template | 34.8 ms                                                    | 34.2 ms: 1.02x faster                                                  |
| mako            | 11.2 ms                                                    | 11.2 ms: 1.00x faster                                                  |
| Geometric mean  | (ref)                                                      | 1.02x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-linux-x86_64-nohlson-enable_no_impact_def-3.14.0a0-98d9ea0 |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 265 us: 1.39x faster                                                   |
| deepcopy_memo              | 39.7 us                                                    | 29.9 us: 1.33x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                    | 2.68 us: 1.25x faster                                                  |
| gc_traversal               | 3.98 ms                                                    | 3.60 ms: 1.10x faster                                                  |
| pathlib                    | 17.3 ms                                                    | 15.9 ms: 1.09x faster                                                  |
| logging_format             | 6.47 us                                                    | 6.03 us: 1.07x faster                                                  |
| scimark_fft                | 392 ms                                                     | 367 ms: 1.07x faster                                                   |
| async_tree_io_tg           | 936 ms                                                     | 877 ms: 1.07x faster                                                   |
| richards                   | 50.9 ms                                                    | 48.0 ms: 1.06x faster                                                  |
| bench_thread_pool          | 834 us                                                     | 789 us: 1.06x faster                                                   |
| richards_super             | 57.4 ms                                                    | 54.3 ms: 1.06x faster                                                  |
| scimark_lu                 | 122 ms                                                     | 115 ms: 1.06x faster                                                   |
| asyncio_tcp                | 508 ms                                                     | 482 ms: 1.05x faster                                                   |
| create_gc_cycles           | 1.82 ms                                                    | 1.73 ms: 1.05x faster                                                  |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 5.02 ms: 1.05x faster                                                  |
| docutils                   | 2.83 sec                                                   | 2.71 sec: 1.04x faster                                                 |
| logging_simple             | 5.74 us                                                    | 5.51 us: 1.04x faster                                                  |
| dulwich_log                | 67.2 ms                                                    | 64.5 ms: 1.04x faster                                                  |
| crypto_pyaes               | 77.5 ms                                                    | 74.5 ms: 1.04x faster                                                  |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.77 sec: 1.04x faster                                                 |
| regex_compile              | 137 ms                                                     | 132 ms: 1.04x faster                                                   |
| nqueens                    | 81.4 ms                                                    | 78.5 ms: 1.04x faster                                                  |
| generators                 | 29.6 ms                                                    | 28.6 ms: 1.04x faster                                                  |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                  |
| async_tree_none            | 378 ms                                                     | 366 ms: 1.03x faster                                                   |
| tornado_http               | 94.6 ms                                                    | 91.6 ms: 1.03x faster                                                  |
| regex_effbot               | 3.67 ms                                                    | 3.55 ms: 1.03x faster                                                  |
| 2to3                       | 274 ms                                                     | 265 ms: 1.03x faster                                                   |
| xml_etree_parse            | 162 ms                                                     | 157 ms: 1.03x faster                                                   |
| python_startup             | 10.8 ms                                                    | 10.4 ms: 1.03x faster                                                  |
| xml_etree_process          | 61.2 ms                                                    | 59.3 ms: 1.03x faster                                                  |
| sympy_str                  | 282 ms                                                     | 274 ms: 1.03x faster                                                   |
| dask                       | 369 ms                                                     | 358 ms: 1.03x faster                                                   |
| float                      | 78.9 ms                                                    | 76.6 ms: 1.03x faster                                                  |
| xml_etree_generate         | 87.4 ms                                                    | 84.9 ms: 1.03x faster                                                  |
| thrift                     | 823 us                                                     | 799 us: 1.03x faster                                                   |
| chaos                      | 61.3 ms                                                    | 59.6 ms: 1.03x faster                                                  |
| sqlite_synth               | 2.99 us                                                    | 2.90 us: 1.03x faster                                                  |
| async_tree_none_tg         | 336 ms                                                     | 327 ms: 1.03x faster                                                   |
| pycparser                  | 1.16 sec                                                   | 1.13 sec: 1.03x faster                                                 |
| sqlglot_transpile          | 1.63 ms                                                    | 1.59 ms: 1.03x faster                                                  |
| sqlglot_optimize           | 55.5 ms                                                    | 54.0 ms: 1.03x faster                                                  |
| sympy_sum                  | 156 ms                                                     | 152 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 572 ms: 1.03x faster                                                   |
| bpe_tokeniser              | 5.02 sec                                                   | 4.89 sec: 1.03x faster                                                 |
| sympy_integrate            | 20.5 ms                                                    | 20.0 ms: 1.03x faster                                                  |
| pprint_safe_repr           | 758 ms                                                     | 739 ms: 1.03x faster                                                   |
| fannkuch                   | 402 ms                                                     | 392 ms: 1.03x faster                                                   |
| python_startup_no_site     | 7.11 ms                                                    | 6.93 ms: 1.03x faster                                                  |
| pprint_pformat             | 1.56 sec                                                   | 1.52 sec: 1.02x faster                                                 |
| coroutines                 | 23.2 ms                                                    | 22.6 ms: 1.02x faster                                                  |
| asyncio_websockets         | 567 ms                                                     | 554 ms: 1.02x faster                                                   |
| genshi_text                | 23.7 ms                                                    | 23.1 ms: 1.02x faster                                                  |
| genshi_xml                 | 51.6 ms                                                    | 50.5 ms: 1.02x faster                                                  |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                   |
| spectral_norm              | 116 ms                                                     | 114 ms: 1.02x faster                                                   |
| pickle                     | 11.5 us                                                    | 11.3 us: 1.02x faster                                                  |
| regex_v8                   | 25.1 ms                                                    | 24.6 ms: 1.02x faster                                                  |
| sqlglot_normalize          | 110 ms                                                     | 108 ms: 1.02x faster                                                   |
| mdp                        | 2.79 sec                                                   | 2.73 sec: 1.02x faster                                                 |
| hexiom                     | 6.30 ms                                                    | 6.19 ms: 1.02x faster                                                  |
| django_template            | 34.8 ms                                                    | 34.2 ms: 1.02x faster                                                  |
| sqlglot_parse              | 1.32 ms                                                    | 1.30 ms: 1.02x faster                                                  |
| meteor_contest             | 110 ms                                                     | 108 ms: 1.02x faster                                                   |
| json_loads                 | 28.9 us                                                    | 28.5 us: 1.02x faster                                                  |
| telco                      | 8.41 ms                                                    | 8.29 ms: 1.02x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                     | 106 ms: 1.01x faster                                                   |
| async_generators           | 442 ms                                                     | 436 ms: 1.01x faster                                                   |
| pickle_pure_python         | 305 us                                                     | 301 us: 1.01x faster                                                   |
| sympy_expand               | 473 ms                                                     | 466 ms: 1.01x faster                                                   |
| scimark_sor                | 127 ms                                                     | 126 ms: 1.01x faster                                                   |
| coverage                   | 93.1 ms                                                    | 92.1 ms: 1.01x faster                                                  |
| go                         | 145 ms                                                     | 143 ms: 1.01x faster                                                   |
| json                       | 5.31 ms                                                    | 5.27 ms: 1.01x faster                                                  |
| unpickle_pure_python       | 218 us                                                     | 217 us: 1.00x faster                                                   |
| mako                       | 11.2 ms                                                    | 11.2 ms: 1.00x faster                                                  |
| raytrace                   | 267 ms                                                     | 266 ms: 1.00x faster                                                   |
| logging_silent             | 105 ns                                                     | 105 ns: 1.00x slower                                                   |
| unpickle_list              | 5.34 us                                                    | 5.37 us: 1.00x slower                                                  |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                  |
| deltablue                  | 3.25 ms                                                    | 3.28 ms: 1.01x slower                                                  |
| scimark_monte_carlo        | 69.2 ms                                                    | 69.8 ms: 1.01x slower                                                  |
| tomli_loads                | 2.12 sec                                                   | 2.14 sec: 1.01x slower                                                 |
| regex_dna                  | 221 ms                                                     | 224 ms: 1.01x slower                                                   |
| comprehensions             | 16.6 us                                                    | 16.9 us: 1.02x slower                                                  |
| async_tree_io              | 939 ms                                                     | 974 ms: 1.04x slower                                                   |
| unpickle                   | 15.1 us                                                    | 15.7 us: 1.04x slower                                                  |
| nbody                      | 88.3 ms                                                    | 91.9 ms: 1.04x slower                                                  |
| pickle_dict                | 34.8 us                                                    | 36.6 us: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                      | 1.03x faster                                                           |

Benchmark hidden because not significant (8): pylint, async_tree_memoization, typing_runtime_protocols, async_tree_memoization_tg, pyflate, pickle_list, async_tree_cpu_io_mixed, html5lib
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.01x