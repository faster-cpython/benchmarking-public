# Results vs. 3.12.0

- fork: mdboom
- ref: unicode_check_exact
- machine: linux-x86_64
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.089x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.08x faster                                                 |
| docutils       | 2.77 sec                                               | 2.66 sec: 1.04x faster                                               |
| tornado_http   | 103 ms                                                 | 90.4 ms: 1.14x faster                                                |
| Geometric mean | (ref)                                                  | 1.08x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 313 ms: 1.51x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 387 ms: 1.48x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 391 ms: 1.48x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 305 ms: 1.47x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 871 ms: 1.36x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 861 ms: 1.34x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 546 ms: 1.33x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 559 ms: 1.30x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.41x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 77.7 ms: 1.09x faster                                                |
| nbody          | 97.0 ms                                                | 89.4 ms: 1.08x faster                                                |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                 |
| regex_effbot   | 3.61 ms                                                | 3.53 ms: 1.02x faster                                                |
| regex_dna      | 212 ms                                                 | 217 ms: 1.02x slower                                                 |
| regex_v8       | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                  | 1.02x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.08 sec: 1.12x faster                                               |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 301 us: 1.07x faster                                                 |
| json_loads           | 28.5 us                                                | 26.7 us: 1.07x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 59.3 ms: 1.04x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 85.6 ms: 1.04x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 154 ms: 1.04x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 104 ms: 1.03x faster                                                 |
| pickle_dict          | 35.5 us                                                | 34.9 us: 1.02x faster                                                |
| pickle               | 11.6 us                                                | 11.4 us: 1.01x faster                                                |
| pickle_list          | 5.08 us                                                | 5.06 us: 1.00x faster                                                |
| unpickle_list        | 5.29 us                                                | 5.44 us: 1.03x slower                                                |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                         |

Benchmark hidden because not significant (2): unpickle, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.97 ms: 1.00x slower                                                |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako           | 11.9 ms                                                | 11.2 ms: 1.07x faster                                                |
| Geometric mean | (ref)                                                  | 1.03x faster                                                         |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 313 ms: 1.51x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 387 ms: 1.48x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 391 ms: 1.48x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 305 ms: 1.47x faster                                                 |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 871 ms: 1.36x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 861 ms: 1.34x faster                                                 |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 546 ms: 1.33x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 30.8 us: 1.32x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 559 ms: 1.30x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.25x faster                                                |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                |
| raytrace                   | 312 ms                                                 | 259 ms: 1.20x faster                                                 |
| go                         | 139 ms                                                 | 117 ms: 1.19x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.19 ms: 1.17x faster                                                |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                 |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 71.8 ms: 1.14x faster                                                |
| chaos                      | 67.0 ms                                                | 58.9 ms: 1.14x faster                                                |
| tornado_http               | 103 ms                                                 | 90.4 ms: 1.14x faster                                                |
| logging_format             | 7.23 us                                                | 6.38 us: 1.13x faster                                                |
| logging_simple             | 6.46 us                                                | 5.74 us: 1.13x faster                                                |
| tomli_loads                | 2.33 sec                                               | 2.08 sec: 1.12x faster                                               |
| generators                 | 31.2 ms                                                | 27.9 ms: 1.12x faster                                                |
| sympy_str                  | 300 ms                                                 | 270 ms: 1.11x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 67.8 ms: 1.11x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.09x faster                                                |
| float                      | 84.7 ms                                                | 77.7 ms: 1.09x faster                                                |
| async_generators           | 463 ms                                                 | 427 ms: 1.09x faster                                                 |
| nbody                      | 97.0 ms                                                | 89.4 ms: 1.08x faster                                                |
| pprint_safe_repr           | 776 ms                                                 | 718 ms: 1.08x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                                 |
| 2to3                       | 274 ms                                                 | 255 ms: 1.08x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 301 us: 1.07x faster                                                 |
| unpack_sequence            | 54.0 ns                                                | 50.5 ns: 1.07x faster                                                |
| json                       | 5.26 ms                                                | 4.92 ms: 1.07x faster                                                |
| json_loads                 | 28.5 us                                                | 26.7 us: 1.07x faster                                                |
| bench_thread_pool          | 842 us                                                 | 789 us: 1.07x faster                                                 |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.07x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.06x faster                                               |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.06x faster                                                |
| dulwich_log                | 68.5 ms                                                | 64.5 ms: 1.06x faster                                                |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                                |
| nqueens                    | 83.3 ms                                                | 79.3 ms: 1.05x faster                                                |
| docutils                   | 2.77 sec                                               | 2.66 sec: 1.04x faster                                               |
| xml_etree_process          | 61.7 ms                                                | 59.3 ms: 1.04x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 85.6 ms: 1.04x faster                                                |
| logging_silent             | 104 ns                                                 | 100 ns: 1.04x faster                                                 |
| sympy_expand               | 478 ms                                                 | 460 ms: 1.04x faster                                                 |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                 |
| gc_traversal               | 3.79 ms                                                | 3.66 ms: 1.04x faster                                                |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.04x faster                                               |
| xml_etree_parse            | 159 ms                                                 | 154 ms: 1.04x faster                                                 |
| fannkuch                   | 417 ms                                                 | 403 ms: 1.03x faster                                                 |
| asyncio_tcp                | 491 ms                                                 | 475 ms: 1.03x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.03x faster                                                 |
| hexiom                     | 6.41 ms                                                | 6.22 ms: 1.03x faster                                                |
| scimark_fft                | 382 ms                                                 | 371 ms: 1.03x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 104 ms: 1.03x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.53 ms: 1.02x faster                                                |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.02x faster                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 53.7 ms: 1.02x faster                                                |
| scimark_sor                | 129 ms                                                 | 127 ms: 1.02x faster                                                 |
| mdp                        | 2.63 sec                                               | 2.58 sec: 1.02x faster                                               |
| pyflate                    | 482 ms                                                 | 474 ms: 1.02x faster                                                 |
| pickle_dict                | 35.5 us                                                | 34.9 us: 1.02x faster                                                |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.02x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.98 ms: 1.02x faster                                                |
| pickle                     | 11.6 us                                                | 11.4 us: 1.01x faster                                                |
| pickle_list                | 5.08 us                                                | 5.06 us: 1.00x faster                                                |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                               |
| python_startup_no_site     | 6.94 ms                                                | 6.97 ms: 1.00x slower                                                |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                 |
| sqlite_synth               | 2.83 us                                                | 2.85 us: 1.01x slower                                                |
| richards_super             | 51.5 ms                                                | 51.9 ms: 1.01x slower                                                |
| coroutines                 | 23.2 ms                                                | 23.6 ms: 1.02x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 161 us: 1.02x slower                                                 |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.02x slower                                                 |
| unpickle_list              | 5.29 us                                                | 5.44 us: 1.03x slower                                                |
| regex_v8                   | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 1.71 ms: 1.16x slower                                                |
| telco                      | 7.10 ms                                                | 8.42 ms: 1.19x slower                                                |
| coverage                   | 72.7 ms                                                | 86.5 ms: 1.19x slower                                                |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                         |

Benchmark hidden because not significant (5): unpickle, bench_mp_pool, json_dumps, richards, django_template
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240911-3.14.0a0-76aa43c/bm-20240911-linux-x86_64-mdboom-unicode_check_exact-3.14.0a0-76aa43c.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.089x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.97x