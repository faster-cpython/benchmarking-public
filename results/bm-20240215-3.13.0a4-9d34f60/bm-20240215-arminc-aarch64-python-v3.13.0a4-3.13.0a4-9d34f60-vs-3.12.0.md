# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a4
- machine: linux-aarch64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.01x faster
- HPT reliability: 94.81%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.88x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 306 ms: 1.01x faster                                         |
| chameleon      | 8.81 ms                                                               | 8.93 ms: 1.01x slower                                        |
| docutils       | 2.98 sec                                                              | 2.91 sec: 1.03x faster                                       |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                 |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|---------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none           | 624 ms                                                                | 564 ms: 1.11x faster                                         |
| async_tree_memoization    | 777 ms                                                                | 737 ms: 1.05x faster                                         |
| async_tree_cpu_io_mixed   | 912 ms                                                                | 880 ms: 1.04x faster                                         |
| async_tree_none_tg        | 577 ms                                                                | 567 ms: 1.02x faster                                         |
| async_tree_memoization_tg | 740 ms                                                                | 728 ms: 1.02x faster                                         |
| async_tree_io             | 1.41 sec                                                              | 1.42 sec: 1.01x slower                                       |
| async_tree_io_tg          | 1.40 sec                                                              | 1.43 sec: 1.01x slower                                       |
| Geometric mean            | (ref)                                                                 | 1.02x faster                                                 |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                         |
| float          | 92.1 ms                                                               | 93.1 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 125 ms: 1.10x faster                                         |
| regex_effbot   | 4.64 ms                                                               | 4.90 ms: 1.06x slower                                        |
| regex_v8       | 28.3 ms                                                               | 30.2 ms: 1.06x slower                                        |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 365 us                                                                | 351 us: 1.04x faster                                         |
| unpickle_pure_python | 260 us                                                                | 255 us: 1.02x faster                                         |
| xml_etree_iterparse  | 150 ms                                                                | 149 ms: 1.01x faster                                         |
| tomli_loads          | 2.59 sec                                                              | 2.58 sec: 1.01x faster                                       |
| pickle_list          | 5.25 us                                                               | 5.22 us: 1.00x faster                                        |
| xml_etree_generate   | 112 ms                                                                | 113 ms: 1.01x slower                                         |
| unpickle_list        | 6.17 us                                                               | 6.46 us: 1.05x slower                                        |
| json_loads           | 30.7 us                                                               | 32.2 us: 1.05x slower                                        |
| unpickle             | 18.5 us                                                               | 19.7 us: 1.07x slower                                        |
| json_dumps           | 12.3 ms                                                               | 13.2 ms: 1.07x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                 |

Benchmark hidden because not significant (4): xml_etree_process, pickle_dict, pickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                               | 12.1 ms: 1.07x slower                                        |
| python_startup_no_site | 8.37 ms                                                               | 10.5 ms: 1.26x slower                                        |
| Geometric mean         | (ref)                                                                 | 1.16x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 59.7 ms: 1.02x faster                                        |
| genshi_text     | 27.4 ms                                                               | 27.1 ms: 1.01x faster                                        |
| django_template | 40.7 ms                                                               | 40.3 ms: 1.01x faster                                        |
| mako            | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                        |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                 |

All benchmarks:
===============

| Benchmark                 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|---------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols  | 181 us                                                                | 133 us: 1.36x faster                                         |
| comprehensions            | 25.4 us                                                               | 20.3 us: 1.25x faster                                        |
| generators                | 43.5 ms                                                               | 36.2 ms: 1.20x faster                                        |
| raytrace                  | 353 ms                                                                | 295 ms: 1.20x faster                                         |
| sympy_sum                 | 154 ms                                                                | 139 ms: 1.11x faster                                         |
| async_tree_none           | 624 ms                                                                | 564 ms: 1.11x faster                                         |
| crypto_pyaes              | 86.6 ms                                                               | 78.8 ms: 1.10x faster                                        |
| regex_compile             | 137 ms                                                                | 125 ms: 1.10x faster                                         |
| sympy_str                 | 280 ms                                                                | 257 ms: 1.09x faster                                         |
| sqlglot_parse             | 1.46 ms                                                               | 1.36 ms: 1.07x faster                                        |
| chaos                     | 71.4 ms                                                               | 67.1 ms: 1.06x faster                                        |
| pylint                    | 355 ms                                                                | 334 ms: 1.06x faster                                         |
| sqlglot_transpile         | 1.83 ms                                                               | 1.72 ms: 1.06x faster                                        |
| scimark_lu                | 146 ms                                                                | 138 ms: 1.06x faster                                         |
| async_tree_memoization    | 777 ms                                                                | 737 ms: 1.05x faster                                         |
| logging_format            | 8.34 us                                                               | 7.92 us: 1.05x faster                                        |
| logging_simple            | 7.63 us                                                               | 7.26 us: 1.05x faster                                        |
| sympy_integrate           | 21.6 ms                                                               | 20.7 ms: 1.05x faster                                        |
| dulwich_log               | 62.0 ms                                                               | 59.4 ms: 1.04x faster                                        |
| pickle_pure_python        | 365 us                                                                | 351 us: 1.04x faster                                         |
| deepcopy_reduce           | 4.10 us                                                               | 3.94 us: 1.04x faster                                        |
| async_tree_cpu_io_mixed   | 912 ms                                                                | 880 ms: 1.04x faster                                         |
| pathlib                   | 24.5 ms                                                               | 23.7 ms: 1.04x faster                                        |
| deepcopy                  | 446 us                                                                | 434 us: 1.03x faster                                         |
| nqueens                   | 99.2 ms                                                               | 96.6 ms: 1.03x faster                                        |
| docutils                  | 2.98 sec                                                              | 2.91 sec: 1.03x faster                                       |
| deepcopy_memo             | 49.6 us                                                               | 48.5 us: 1.02x faster                                        |
| asyncio_tcp               | 566 ms                                                                | 553 ms: 1.02x faster                                         |
| mdp                       | 3.41 sec                                                              | 3.34 sec: 1.02x faster                                       |
| deltablue                 | 4.12 ms                                                               | 4.03 ms: 1.02x faster                                        |
| unpickle_pure_python      | 260 us                                                                | 255 us: 1.02x faster                                         |
| async_tree_none_tg        | 577 ms                                                                | 567 ms: 1.02x faster                                         |
| async_tree_memoization_tg | 740 ms                                                                | 728 ms: 1.02x faster                                         |
| genshi_xml                | 60.6 ms                                                               | 59.7 ms: 1.02x faster                                        |
| pprint_safe_repr          | 916 ms                                                                | 903 ms: 1.01x faster                                         |
| bench_mp_pool             | 7.05 ms                                                               | 6.96 ms: 1.01x faster                                        |
| scimark_monte_carlo       | 85.1 ms                                                               | 84.0 ms: 1.01x faster                                        |
| sympy_expand              | 454 ms                                                                | 448 ms: 1.01x faster                                         |
| pprint_pformat            | 1.88 sec                                                              | 1.86 sec: 1.01x faster                                       |
| thrift                    | 937 us                                                                | 926 us: 1.01x faster                                         |
| genshi_text               | 27.4 ms                                                               | 27.1 ms: 1.01x faster                                        |
| xml_etree_iterparse       | 150 ms                                                                | 149 ms: 1.01x faster                                         |
| bench_thread_pool         | 1.31 ms                                                               | 1.30 ms: 1.01x faster                                        |
| django_template           | 40.7 ms                                                               | 40.3 ms: 1.01x faster                                        |
| 2to3                      | 308 ms                                                                | 306 ms: 1.01x faster                                         |
| logging_silent            | 127 ns                                                                | 126 ns: 1.01x faster                                         |
| tomli_loads               | 2.59 sec                                                              | 2.58 sec: 1.01x faster                                       |
| pickle_list               | 5.25 us                                                               | 5.22 us: 1.00x faster                                        |
| pidigits                  | 233 ms                                                                | 234 ms: 1.01x slower                                         |
| asyncio_tcp_ssl           | 2.19 sec                                                              | 2.20 sec: 1.01x slower                                       |
| async_tree_io             | 1.41 sec                                                              | 1.42 sec: 1.01x slower                                       |
| xml_etree_generate        | 112 ms                                                                | 113 ms: 1.01x slower                                         |
| float                     | 92.1 ms                                                               | 93.1 ms: 1.01x slower                                        |
| chameleon                 | 8.81 ms                                                               | 8.93 ms: 1.01x slower                                        |
| async_tree_io_tg          | 1.40 sec                                                              | 1.43 sec: 1.01x slower                                       |
| sqlite_synth              | 3.77 us                                                               | 3.84 us: 1.02x slower                                        |
| pycparser                 | 1.26 sec                                                              | 1.28 sec: 1.02x slower                                       |
| go                        | 157 ms                                                                | 160 ms: 1.02x slower                                         |
| mako                      | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                        |
| create_gc_cycles          | 1.92 ms                                                               | 1.96 ms: 1.02x slower                                        |
| meteor_contest            | 112 ms                                                                | 114 ms: 1.02x slower                                         |
| aiohttp                   | 1.16 ms                                                               | 1.19 ms: 1.03x slower                                        |
| json                      | 5.54 ms                                                               | 5.69 ms: 1.03x slower                                        |
| spectral_norm             | 131 ms                                                                | 135 ms: 1.04x slower                                         |
| richards_super            | 58.5 ms                                                               | 60.6 ms: 1.04x slower                                        |
| fannkuch                  | 443 ms                                                                | 461 ms: 1.04x slower                                         |
| unpickle_list             | 6.17 us                                                               | 6.46 us: 1.05x slower                                        |
| json_loads                | 30.7 us                                                               | 32.2 us: 1.05x slower                                        |
| scimark_sparse_mat_mult   | 6.19 ms                                                               | 6.53 ms: 1.05x slower                                        |
| regex_effbot              | 4.64 ms                                                               | 4.90 ms: 1.06x slower                                        |
| scimark_fft               | 418 ms                                                                | 442 ms: 1.06x slower                                         |
| richards                  | 50.9 ms                                                               | 54.2 ms: 1.06x slower                                        |
| regex_v8                  | 28.3 ms                                                               | 30.2 ms: 1.06x slower                                        |
| unpickle                  | 18.5 us                                                               | 19.7 us: 1.07x slower                                        |
| python_startup            | 11.4 ms                                                               | 12.1 ms: 1.07x slower                                        |
| pyflate                   | 559 ms                                                                | 597 ms: 1.07x slower                                         |
| gunicorn                  | 1.14 ms                                                               | 1.22 ms: 1.07x slower                                        |
| json_dumps                | 12.3 ms                                                               | 13.2 ms: 1.07x slower                                        |
| scimark_sor               | 150 ms                                                                | 166 ms: 1.11x slower                                         |
| telco                     | 8.51 ms                                                               | 9.57 ms: 1.12x slower                                        |
| coverage                  | 87.3 ms                                                               | 102 ms: 1.16x slower                                         |
| python_startup_no_site    | 8.37 ms                                                               | 10.5 ms: 1.26x slower                                        |
| Geometric mean            | (ref)                                                                 | 1.01x faster                                                 |

Benchmark hidden because not significant (17): tornado_http, async_generators, sqlglot_normalize, sqlglot_optimize, regex_dna, gc_traversal, hexiom, xml_etree_process, async_tree_cpu_io_mixed_tg, asyncio_websockets, coroutines, pickle_dict, pickle, nbody, xml_etree_parse, html5lib, mypy2
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-arminc-aarch64-python-v3.13.0a4-3.13.0a4-9d34f60.json: flaskblogging

# HPT report

- Reliability score: 94.81% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.88x