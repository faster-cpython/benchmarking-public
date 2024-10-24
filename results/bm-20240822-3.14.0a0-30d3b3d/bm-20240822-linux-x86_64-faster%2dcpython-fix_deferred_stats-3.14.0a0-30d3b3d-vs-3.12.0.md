# Results vs. 3.12.0

- fork: faster-cpython
- ref: fix_deferred_stats
- machine: linux-x86_64
- commit hash: 30d3b3d
- commit date: 2024-08-22
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 263 ms: 1.04x faster                                                          |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                        |
| tornado_http   | 103 ms                                                 | 90.1 ms: 1.14x faster                                                         |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 391 ms: 1.48x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 308 ms: 1.46x faster                                                          |
| async_tree_none            | 472 ms                                                 | 323 ms: 1.46x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 401 ms: 1.43x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 534 ms: 1.36x faster                                                          |
| async_tree_io_tg           | 1.18 sec                                               | 899 ms: 1.32x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 553 ms: 1.31x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 931 ms: 1.24x faster                                                          |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 85.8 ms: 1.13x faster                                                         |
| float          | 84.7 ms                                                | 79.1 ms: 1.07x faster                                                         |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                                          |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                          |
| regex_v8       | 23.1 ms                                                | 23.7 ms: 1.02x slower                                                         |
| regex_effbot   | 3.61 ms                                                | 3.76 ms: 1.04x slower                                                         |
| regex_dna      | 212 ms                                                 | 225 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.04 sec: 1.14x faster                                                        |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                                          |
| pickle_pure_python   | 324 us                                                 | 304 us: 1.07x faster                                                          |
| xml_etree_parse      | 159 ms                                                 | 154 ms: 1.04x faster                                                          |
| xml_etree_generate   | 89.2 ms                                                | 86.2 ms: 1.03x faster                                                         |
| xml_etree_process    | 61.7 ms                                                | 59.7 ms: 1.03x faster                                                         |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.02x faster                                                          |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                  |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                         |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                         |
| django_template | 34.6 ms                                                | 33.7 ms: 1.03x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 391 ms: 1.48x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 308 ms: 1.46x faster                                                          |
| async_tree_none            | 472 ms                                                 | 323 ms: 1.46x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 401 ms: 1.43x faster                                                          |
| deepcopy                   | 371 us                                                 | 263 us: 1.41x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 534 ms: 1.36x faster                                                          |
| deepcopy_memo              | 40.7 us                                                | 30.1 us: 1.35x faster                                                         |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 899 ms: 1.32x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 553 ms: 1.31x faster                                                          |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 931 ms: 1.24x faster                                                          |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.19x faster                                                         |
| logging_format             | 7.23 us                                                | 6.10 us: 1.19x faster                                                         |
| raytrace                   | 312 ms                                                 | 265 ms: 1.18x faster                                                          |
| logging_simple             | 6.46 us                                                | 5.51 us: 1.17x faster                                                         |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                          |
| deltablue                  | 3.72 ms                                                | 3.23 ms: 1.15x faster                                                         |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                          |
| tomli_loads                | 2.33 sec                                               | 2.04 sec: 1.14x faster                                                        |
| tornado_http               | 103 ms                                                 | 90.1 ms: 1.14x faster                                                         |
| crypto_pyaes               | 81.9 ms                                                | 72.1 ms: 1.13x faster                                                         |
| chaos                      | 67.0 ms                                                | 59.1 ms: 1.13x faster                                                         |
| nbody                      | 97.0 ms                                                | 85.8 ms: 1.13x faster                                                         |
| generators                 | 31.2 ms                                                | 27.6 ms: 1.13x faster                                                         |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 68.3 ms: 1.10x faster                                                         |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.09x faster                                                         |
| scimark_fft                | 382 ms                                                 | 352 ms: 1.09x faster                                                          |
| float                      | 84.7 ms                                                | 79.1 ms: 1.07x faster                                                         |
| bench_thread_pool          | 842 us                                                 | 786 us: 1.07x faster                                                          |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                                          |
| pickle_pure_python         | 324 us                                                 | 304 us: 1.07x faster                                                          |
| async_generators           | 463 ms                                                 | 435 ms: 1.06x faster                                                          |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.06x faster                                                         |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                         |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                                         |
| sympy_expand               | 478 ms                                                 | 456 ms: 1.05x faster                                                          |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                          |
| nqueens                    | 83.3 ms                                                | 79.6 ms: 1.05x faster                                                         |
| fannkuch                   | 417 ms                                                 | 399 ms: 1.04x faster                                                          |
| 2to3                       | 274 ms                                                 | 263 ms: 1.04x faster                                                          |
| gc_traversal               | 3.79 ms                                                | 3.64 ms: 1.04x faster                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.87 ms: 1.04x faster                                                         |
| hexiom                     | 6.41 ms                                                | 6.18 ms: 1.04x faster                                                         |
| xml_etree_parse            | 159 ms                                                 | 154 ms: 1.04x faster                                                          |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.04x faster                                                          |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.04x faster                                                          |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.04x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 86.2 ms: 1.03x faster                                                         |
| xml_etree_process          | 61.7 ms                                                | 59.7 ms: 1.03x faster                                                         |
| pprint_safe_repr           | 776 ms                                                 | 751 ms: 1.03x faster                                                          |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                          |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                        |
| django_template            | 34.6 ms                                                | 33.7 ms: 1.03x faster                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.02x faster                                                        |
| sqlglot_optimize           | 54.8 ms                                                | 53.6 ms: 1.02x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.02x faster                                                          |
| pyflate                    | 482 ms                                                 | 474 ms: 1.02x faster                                                          |
| asyncio_tcp                | 491 ms                                                 | 484 ms: 1.01x faster                                                          |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                                          |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                                          |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                        |
| richards_super             | 51.5 ms                                                | 52.0 ms: 1.01x slower                                                         |
| coroutines                 | 23.2 ms                                                | 23.4 ms: 1.01x slower                                                         |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                          |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                         |
| python_startup_no_site     | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                         |
| regex_v8                   | 23.1 ms                                                | 23.7 ms: 1.02x slower                                                         |
| json                       | 5.26 ms                                                | 5.39 ms: 1.02x slower                                                         |
| go                         | 139 ms                                                 | 143 ms: 1.03x slower                                                          |
| mdp                        | 2.63 sec                                               | 2.73 sec: 1.04x slower                                                        |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                          |
| regex_effbot               | 3.61 ms                                                | 3.76 ms: 1.04x slower                                                         |
| regex_dna                  | 212 ms                                                 | 225 ms: 1.06x slower                                                          |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                         |
| telco                      | 7.10 ms                                                | 8.15 ms: 1.15x slower                                                         |
| coverage                   | 72.7 ms                                                | 85.2 ms: 1.17x slower                                                         |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.19x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                  |

Benchmark hidden because not significant (4): scimark_sor, bench_mp_pool, json_loads, richards
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240822-3.14.0a0-30d3b3d/bm-20240822-linux-x86_64-faster%2dcpython-fix_deferred_stats-3.14.0a0-30d3b3d.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.98x