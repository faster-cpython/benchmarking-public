# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a3
- machine: linux-aarch64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.01x faster
- HPT reliability: 58.16%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.88x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 305 ms: 1.01x faster                                         |
| chameleon      | 8.81 ms                                                               | 8.98 ms: 1.02x slower                                        |
| docutils       | 2.98 sec                                                              | 2.90 sec: 1.03x faster                                       |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                 |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 582 ms: 1.07x faster                                         |
| async_tree_memoization     | 777 ms                                                                | 745 ms: 1.04x faster                                         |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 888 ms: 1.03x faster                                         |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 895 ms: 1.01x slower                                         |
| async_tree_io_tg           | 1.40 sec                                                              | 1.44 sec: 1.02x slower                                       |
| async_tree_io              | 1.41 sec                                                              | 1.45 sec: 1.03x slower                                       |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                 |

Benchmark hidden because not significant (2): async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 91.0 ms: 1.01x faster                                        |
| nbody          | 105 ms                                                                | 104 ms: 1.01x faster                                         |
| pidigits       | 233 ms                                                                | 233 ms: 1.00x slower                                         |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 125 ms: 1.10x faster                                         |
| regex_dna      | 254 ms                                                                | 255 ms: 1.01x slower                                         |
| regex_v8       | 28.3 ms                                                               | 30.1 ms: 1.06x slower                                        |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 365 us                                                                | 347 us: 1.05x faster                                         |
| unpickle_pure_python | 260 us                                                                | 256 us: 1.02x faster                                         |
| pickle_list          | 5.25 us                                                               | 5.28 us: 1.01x slower                                        |
| xml_etree_iterparse  | 150 ms                                                                | 152 ms: 1.01x slower                                         |
| json_loads           | 30.7 us                                                               | 31.1 us: 1.01x slower                                        |
| json_dumps           | 12.3 ms                                                               | 12.5 ms: 1.02x slower                                        |
| xml_etree_process    | 79.0 ms                                                               | 80.2 ms: 1.02x slower                                        |
| xml_etree_generate   | 112 ms                                                                | 114 ms: 1.02x slower                                         |
| unpickle_list        | 6.17 us                                                               | 6.45 us: 1.05x slower                                        |
| xml_etree_parse      | 195 ms                                                                | 206 ms: 1.06x slower                                         |
| unpickle             | 18.5 us                                                               | 19.6 us: 1.06x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                 |

Benchmark hidden because not significant (3): pickle, tomli_loads, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                               | 12.1 ms: 1.06x slower                                        |
| python_startup_no_site | 8.37 ms                                                               | 10.3 ms: 1.23x slower                                        |
| Geometric mean         | (ref)                                                                 | 1.14x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 27.3 ms: 1.00x faster                                        |
| genshi_xml     | 60.6 ms                                                               | 60.8 ms: 1.00x slower                                        |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                 |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols   | 181 us                                                                | 135 us: 1.34x faster                                         |
| comprehensions             | 25.4 us                                                               | 19.8 us: 1.28x faster                                        |
| generators                 | 43.5 ms                                                               | 36.0 ms: 1.21x faster                                        |
| raytrace                   | 353 ms                                                                | 296 ms: 1.19x faster                                         |
| crypto_pyaes               | 86.6 ms                                                               | 77.3 ms: 1.12x faster                                        |
| sympy_sum                  | 154 ms                                                                | 139 ms: 1.11x faster                                         |
| regex_compile              | 137 ms                                                                | 125 ms: 1.10x faster                                         |
| sympy_str                  | 280 ms                                                                | 259 ms: 1.08x faster                                         |
| sqlglot_parse              | 1.46 ms                                                               | 1.36 ms: 1.07x faster                                        |
| async_tree_none            | 624 ms                                                                | 582 ms: 1.07x faster                                         |
| chaos                      | 71.4 ms                                                               | 66.7 ms: 1.07x faster                                        |
| sqlglot_transpile          | 1.83 ms                                                               | 1.72 ms: 1.07x faster                                        |
| scimark_lu                 | 146 ms                                                                | 137 ms: 1.06x faster                                         |
| pylint                     | 355 ms                                                                | 333 ms: 1.06x faster                                         |
| sympy_integrate            | 21.6 ms                                                               | 20.5 ms: 1.06x faster                                        |
| pickle_pure_python         | 365 us                                                                | 347 us: 1.05x faster                                         |
| logging_simple             | 7.63 us                                                               | 7.26 us: 1.05x faster                                        |
| logging_format             | 8.34 us                                                               | 8.00 us: 1.04x faster                                        |
| async_tree_memoization     | 777 ms                                                                | 745 ms: 1.04x faster                                         |
| deltablue                  | 4.12 ms                                                               | 3.98 ms: 1.03x faster                                        |
| nqueens                    | 99.2 ms                                                               | 96.4 ms: 1.03x faster                                        |
| docutils                   | 2.98 sec                                                              | 2.90 sec: 1.03x faster                                       |
| mdp                        | 3.41 sec                                                              | 3.32 sec: 1.03x faster                                       |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 888 ms: 1.03x faster                                         |
| sqlglot_normalize          | 126 ms                                                                | 123 ms: 1.02x faster                                         |
| async_generators           | 491 ms                                                                | 480 ms: 1.02x faster                                         |
| scimark_monte_carlo        | 85.1 ms                                                               | 83.5 ms: 1.02x faster                                        |
| pathlib                    | 24.5 ms                                                               | 24.1 ms: 1.02x faster                                        |
| unpickle_pure_python       | 260 us                                                                | 256 us: 1.02x faster                                         |
| deepcopy_reduce            | 4.10 us                                                               | 4.04 us: 1.01x faster                                        |
| spectral_norm              | 131 ms                                                                | 129 ms: 1.01x faster                                         |
| sympy_expand               | 454 ms                                                                | 448 ms: 1.01x faster                                         |
| thrift                     | 937 us                                                                | 925 us: 1.01x faster                                         |
| dulwich_log                | 62.0 ms                                                               | 61.3 ms: 1.01x faster                                        |
| float                      | 92.1 ms                                                               | 91.0 ms: 1.01x faster                                        |
| sqlglot_optimize           | 61.3 ms                                                               | 60.7 ms: 1.01x faster                                        |
| bench_mp_pool              | 7.05 ms                                                               | 6.98 ms: 1.01x faster                                        |
| 2to3                       | 308 ms                                                                | 305 ms: 1.01x faster                                         |
| gc_traversal               | 4.40 ms                                                               | 4.36 ms: 1.01x faster                                        |
| nbody                      | 105 ms                                                                | 104 ms: 1.01x faster                                         |
| deepcopy_memo              | 49.6 us                                                               | 49.3 us: 1.01x faster                                        |
| sqlite_synth               | 3.77 us                                                               | 3.75 us: 1.00x faster                                        |
| genshi_text                | 27.4 ms                                                               | 27.3 ms: 1.00x faster                                        |
| pidigits                   | 233 ms                                                                | 233 ms: 1.00x slower                                         |
| genshi_xml                 | 60.6 ms                                                               | 60.8 ms: 1.00x slower                                        |
| pyflate                    | 559 ms                                                                | 562 ms: 1.00x slower                                         |
| regex_dna                  | 254 ms                                                                | 255 ms: 1.01x slower                                         |
| pickle_list                | 5.25 us                                                               | 5.28 us: 1.01x slower                                        |
| json                       | 5.54 ms                                                               | 5.59 ms: 1.01x slower                                        |
| xml_etree_iterparse        | 150 ms                                                                | 152 ms: 1.01x slower                                         |
| coroutines                 | 29.0 ms                                                               | 29.4 ms: 1.01x slower                                        |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 895 ms: 1.01x slower                                         |
| json_loads                 | 30.7 us                                                               | 31.1 us: 1.01x slower                                        |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                         |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.22 sec: 1.01x slower                                       |
| json_dumps                 | 12.3 ms                                                               | 12.5 ms: 1.02x slower                                        |
| xml_etree_process          | 79.0 ms                                                               | 80.2 ms: 1.02x slower                                        |
| pprint_pformat             | 1.88 sec                                                              | 1.91 sec: 1.02x slower                                       |
| xml_etree_generate         | 112 ms                                                                | 114 ms: 1.02x slower                                         |
| chameleon                  | 8.81 ms                                                               | 8.98 ms: 1.02x slower                                        |
| pprint_safe_repr           | 916 ms                                                                | 936 ms: 1.02x slower                                         |
| hexiom                     | 6.98 ms                                                               | 7.14 ms: 1.02x slower                                        |
| async_tree_io_tg           | 1.40 sec                                                              | 1.44 sec: 1.02x slower                                       |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.34 ms: 1.02x slower                                        |
| go                         | 157 ms                                                                | 161 ms: 1.02x slower                                         |
| async_tree_io              | 1.41 sec                                                              | 1.45 sec: 1.03x slower                                       |
| fannkuch                   | 443 ms                                                                | 456 ms: 1.03x slower                                         |
| scimark_fft                | 418 ms                                                                | 430 ms: 1.03x slower                                         |
| richards_super             | 58.5 ms                                                               | 60.9 ms: 1.04x slower                                        |
| unpickle_list              | 6.17 us                                                               | 6.45 us: 1.05x slower                                        |
| gunicorn                   | 1.14 ms                                                               | 1.19 ms: 1.05x slower                                        |
| xml_etree_parse            | 195 ms                                                                | 206 ms: 1.06x slower                                         |
| unpickle                   | 18.5 us                                                               | 19.6 us: 1.06x slower                                        |
| logging_silent             | 127 ns                                                                | 134 ns: 1.06x slower                                         |
| python_startup             | 11.4 ms                                                               | 12.1 ms: 1.06x slower                                        |
| regex_v8                   | 28.3 ms                                                               | 30.1 ms: 1.06x slower                                        |
| richards                   | 50.9 ms                                                               | 55.0 ms: 1.08x slower                                        |
| scimark_sor                | 150 ms                                                                | 163 ms: 1.09x slower                                         |
| telco                      | 8.51 ms                                                               | 9.69 ms: 1.14x slower                                        |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.17x slower                                         |
| python_startup_no_site     | 8.37 ms                                                               | 10.3 ms: 1.23x slower                                        |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                 |

Benchmark hidden because not significant (18): asyncio_tcp, create_gc_cycles, async_tree_memoization_tg, async_tree_none_tg, deepcopy, bench_thread_pool, pickle, tomli_loads, mako, pickle_dict, django_template, asyncio_websockets, regex_effbot, aiohttp, pycparser, tornado_http, html5lib, mypy2
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240117-3.13.0a3-f009305/bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305.json: flaskblogging

# HPT report

- Reliability score: 58.16% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.88x