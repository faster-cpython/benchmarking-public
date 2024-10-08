# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a1
- machine: linux-x86_64
- commit hash: ad056f0
- commit date: 2023-10-13
- overall geometric mean: 1.02x slower
- HPT reliability: 65.71%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.55x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 276 ms: 1.01x slower                                       |
| chameleon      | 7.41 ms                                                | 7.13 ms: 1.04x faster                                      |
| docutils       | 2.77 sec                                               | 2.71 sec: 1.02x faster                                     |
| tornado_http   | 103 ms                                                 | 99.1 ms: 1.04x faster                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 446 ms: 1.06x faster                                       |
| async_tree_none_tg         | 450 ms                                                 | 463 ms: 1.03x slower                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 759 ms: 1.05x slower                                       |
| async_tree_io              | 1.16 sec                                               | 1.21 sec: 1.05x slower                                     |
| async_tree_io_tg           | 1.18 sec                                               | 1.25 sec: 1.05x slower                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 610 ms: 1.06x slower                                       |
| Geometric mean             | (ref)                                                  | 1.02x slower                                               |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 84.7 ms                                                | 83.4 ms: 1.02x faster                                      |
| nbody          | 97.0 ms                                                | 95.7 ms: 1.01x faster                                      |
| pidigits       | 187 ms                                                 | 190 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                  | 1.00x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 142 ms: 1.04x faster                                       |
| regex_dna      | 212 ms                                                 | 209 ms: 1.02x faster                                       |
| regex_effbot   | 3.61 ms                                                | 3.56 ms: 1.01x faster                                      |
| regex_v8       | 23.1 ms                                                | 25.3 ms: 1.09x slower                                      |
| Geometric mean | (ref)                                                  | 1.00x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| unpickle             | 15.9 us                                                | 14.9 us: 1.06x faster                                      |
| pickle_pure_python   | 324 us                                                 | 307 us: 1.06x faster                                       |
| unpickle_list        | 5.29 us                                                | 5.08 us: 1.04x faster                                      |
| tomli_loads          | 2.33 sec                                               | 2.25 sec: 1.04x faster                                     |
| json_loads           | 28.5 us                                                | 27.9 us: 1.02x faster                                      |
| xml_etree_process    | 61.7 ms                                                | 60.5 ms: 1.02x faster                                      |
| unpickle_pure_python | 230 us                                                 | 226 us: 1.02x faster                                       |
| xml_etree_generate   | 89.2 ms                                                | 87.7 ms: 1.02x faster                                      |
| pickle_dict          | 35.5 us                                                | 35.4 us: 1.00x faster                                      |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                      |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                      |
| pickle_list          | 5.08 us                                                | 5.21 us: 1.03x slower                                      |
| Geometric mean       | (ref)                                                  | 1.02x faster                                               |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                      |
| python_startup         | 9.55 ms                                                | 10.4 ms: 1.09x slower                                      |
| Geometric mean         | (ref)                                                  | 1.05x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako           | 11.9 ms                                                | 11.7 ms: 1.01x faster                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| raytrace                   | 312 ms                                                 | 285 ms: 1.09x faster                                       |
| deltablue                  | 3.72 ms                                                | 3.40 ms: 1.09x faster                                      |
| crypto_pyaes               | 81.9 ms                                                | 75.1 ms: 1.09x faster                                      |
| logging_format             | 7.23 us                                                | 6.71 us: 1.08x faster                                      |
| logging_simple             | 6.46 us                                                | 6.02 us: 1.07x faster                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 70.2 ms: 1.07x faster                                      |
| unpickle                   | 15.9 us                                                | 14.9 us: 1.06x faster                                      |
| async_tree_none            | 472 ms                                                 | 446 ms: 1.06x faster                                       |
| generators                 | 31.2 ms                                                | 29.5 ms: 1.06x faster                                      |
| pickle_pure_python         | 324 us                                                 | 307 us: 1.06x faster                                       |
| sympy_sum                  | 169 ms                                                 | 160 ms: 1.06x faster                                       |
| sympy_str                  | 300 ms                                                 | 286 ms: 1.05x faster                                       |
| chaos                      | 67.0 ms                                                | 64.0 ms: 1.05x faster                                      |
| deepcopy_reduce            | 3.35 us                                                | 3.20 us: 1.04x faster                                      |
| regex_compile              | 148 ms                                                 | 142 ms: 1.04x faster                                       |
| unpickle_list              | 5.29 us                                                | 5.08 us: 1.04x faster                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                      |
| chameleon                  | 7.41 ms                                                | 7.13 ms: 1.04x faster                                      |
| tomli_loads                | 2.33 sec                                               | 2.25 sec: 1.04x faster                                     |
| tornado_http               | 103 ms                                                 | 99.1 ms: 1.04x faster                                      |
| sympy_expand               | 478 ms                                                 | 463 ms: 1.03x faster                                       |
| sympy_integrate            | 21.4 ms                                                | 20.8 ms: 1.03x faster                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.03x faster                                      |
| pprint_safe_repr           | 776 ms                                                 | 752 ms: 1.03x faster                                       |
| deepcopy                   | 371 us                                                 | 361 us: 1.03x faster                                       |
| deepcopy_memo              | 40.7 us                                                | 39.6 us: 1.03x faster                                      |
| nqueens                    | 83.3 ms                                                | 81.0 ms: 1.03x faster                                      |
| typing_runtime_protocols   | 158 us                                                 | 153 us: 1.03x faster                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.93 ms: 1.03x faster                                      |
| docutils                   | 2.77 sec                                               | 2.71 sec: 1.02x faster                                     |
| json_loads                 | 28.5 us                                                | 27.9 us: 1.02x faster                                      |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                       |
| xml_etree_process          | 61.7 ms                                                | 60.5 ms: 1.02x faster                                      |
| mdp                        | 2.63 sec                                               | 2.58 sec: 1.02x faster                                     |
| scimark_fft                | 382 ms                                                 | 375 ms: 1.02x faster                                       |
| unpickle_pure_python       | 230 us                                                 | 226 us: 1.02x faster                                       |
| meteor_contest             | 112 ms                                                 | 111 ms: 1.02x faster                                       |
| scimark_sor                | 129 ms                                                 | 127 ms: 1.02x faster                                       |
| xml_etree_generate         | 89.2 ms                                                | 87.7 ms: 1.02x faster                                      |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                     |
| float                      | 84.7 ms                                                | 83.4 ms: 1.02x faster                                      |
| regex_dna                  | 212 ms                                                 | 209 ms: 1.02x faster                                       |
| mako                       | 11.9 ms                                                | 11.7 ms: 1.01x faster                                      |
| nbody                      | 97.0 ms                                                | 95.7 ms: 1.01x faster                                      |
| regex_effbot               | 3.61 ms                                                | 3.56 ms: 1.01x faster                                      |
| comprehensions             | 21.8 us                                                | 21.5 us: 1.01x faster                                      |
| bench_thread_pool          | 842 us                                                 | 833 us: 1.01x faster                                       |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                       |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.01x faster                                      |
| sqlglot_optimize           | 54.8 ms                                                | 54.5 ms: 1.01x faster                                      |
| pickle_dict                | 35.5 us                                                | 35.4 us: 1.00x faster                                      |
| hexiom                     | 6.41 ms                                                | 6.40 ms: 1.00x faster                                      |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                      |
| 2to3                       | 274 ms                                                 | 276 ms: 1.01x slower                                       |
| fannkuch                   | 417 ms                                                 | 420 ms: 1.01x slower                                       |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                      |
| pathlib                    | 19.3 ms                                                | 19.6 ms: 1.01x slower                                      |
| spectral_norm              | 115 ms                                                 | 116 ms: 1.01x slower                                       |
| pidigits                   | 187 ms                                                 | 190 ms: 1.01x slower                                       |
| asyncio_tcp                | 491 ms                                                 | 498 ms: 1.02x slower                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                      |
| create_gc_cycles           | 1.48 ms                                                | 1.50 ms: 1.02x slower                                      |
| async_generators           | 463 ms                                                 | 472 ms: 1.02x slower                                       |
| asyncio_websockets         | 551 ms                                                 | 563 ms: 1.02x slower                                       |
| coroutines                 | 23.2 ms                                                | 23.7 ms: 1.02x slower                                      |
| aiohttp                    | 1.15 ms                                                | 1.18 ms: 1.02x slower                                      |
| pickle_list                | 5.08 us                                                | 5.21 us: 1.03x slower                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.83 sec: 1.03x slower                                     |
| gunicorn                   | 1.24 ms                                                | 1.27 ms: 1.03x slower                                      |
| async_tree_none_tg         | 450 ms                                                 | 463 ms: 1.03x slower                                       |
| logging_silent             | 104 ns                                                 | 109 ns: 1.04x slower                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 759 ms: 1.05x slower                                       |
| async_tree_io              | 1.16 sec                                               | 1.21 sec: 1.05x slower                                     |
| go                         | 139 ms                                                 | 146 ms: 1.05x slower                                       |
| async_tree_io_tg           | 1.18 sec                                               | 1.25 sec: 1.05x slower                                     |
| pycparser                  | 1.18 sec                                               | 1.24 sec: 1.06x slower                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 610 ms: 1.06x slower                                       |
| richards_super             | 51.5 ms                                                | 56.0 ms: 1.09x slower                                      |
| python_startup             | 9.55 ms                                                | 10.4 ms: 1.09x slower                                      |
| richards                   | 45.8 ms                                                | 49.9 ms: 1.09x slower                                      |
| regex_v8                   | 23.1 ms                                                | 25.3 ms: 1.09x slower                                      |
| gc_traversal               | 3.79 ms                                                | 4.15 ms: 1.09x slower                                      |
| sqlite_synth               | 2.83 us                                                | 3.11 us: 1.10x slower                                      |
| telco                      | 7.10 ms                                                | 8.41 ms: 1.18x slower                                      |
| dask                       | 372 ms                                                 | 544 ms: 1.46x slower                                       |
| coverage                   | 72.7 ms                                                | 700 ms: 9.63x slower                                       |
| Geometric mean             | (ref)                                                  | 1.02x slower                                               |

Benchmark hidden because not significant (9): async_tree_memoization, pyflate, dulwich_log, async_tree_cpu_io_mixed, json, xml_etree_iterparse, xml_etree_parse, django_template, mypy2
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20231013-3.13.0a1-ad056f0-NOGIL/bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 65.71% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.55x