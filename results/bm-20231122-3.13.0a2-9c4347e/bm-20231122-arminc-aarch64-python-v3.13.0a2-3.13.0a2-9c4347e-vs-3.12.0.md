# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a2
- machine: linux-aarch64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.01x faster
- HPT reliability: 90.29%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.87x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 303 ms: 1.02x faster                                         |
| chameleon      | 8.81 ms                                                               | 8.96 ms: 1.02x slower                                        |
| docutils       | 2.98 sec                                                              | 2.88 sec: 1.04x faster                                       |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                 |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 572 ms: 1.09x faster                                         |
| async_tree_memoization     | 777 ms                                                                | 736 ms: 1.06x faster                                         |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 882 ms: 1.03x faster                                         |
| async_tree_io              | 1.41 sec                                                              | 1.44 sec: 1.02x slower                                       |
| async_tree_none_tg         | 577 ms                                                                | 590 ms: 1.02x slower                                         |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 907 ms: 1.03x slower                                         |
| async_tree_memoization_tg  | 740 ms                                                                | 763 ms: 1.03x slower                                         |
| async_tree_io_tg           | 1.40 sec                                                              | 1.47 sec: 1.05x slower                                       |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 90.6 ms: 1.02x faster                                        |
| nbody          | 105 ms                                                                | 105 ms: 1.00x slower                                         |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 129 ms: 1.06x faster                                         |
| regex_dna      | 254 ms                                                                | 246 ms: 1.03x faster                                         |
| regex_effbot   | 4.64 ms                                                               | 4.61 ms: 1.01x faster                                        |
| regex_v8       | 28.3 ms                                                               | 30.0 ms: 1.06x slower                                        |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 365 us                                                                | 346 us: 1.05x faster                                         |
| unpickle_pure_python | 260 us                                                                | 253 us: 1.03x faster                                         |
| pickle_list          | 5.25 us                                                               | 5.19 us: 1.01x faster                                        |
| unpickle_list        | 6.17 us                                                               | 6.12 us: 1.01x faster                                        |
| tomli_loads          | 2.59 sec                                                              | 2.57 sec: 1.01x faster                                       |
| xml_etree_iterparse  | 150 ms                                                                | 149 ms: 1.01x faster                                         |
| pickle               | 13.4 us                                                               | 13.5 us: 1.00x slower                                        |
| json_loads           | 30.7 us                                                               | 30.8 us: 1.00x slower                                        |
| pickle_dict          | 37.3 us                                                               | 37.5 us: 1.00x slower                                        |
| xml_etree_process    | 79.0 ms                                                               | 79.5 ms: 1.01x slower                                        |
| xml_etree_generate   | 112 ms                                                                | 113 ms: 1.01x slower                                         |
| xml_etree_parse      | 195 ms                                                                | 196 ms: 1.01x slower                                         |
| json_dumps           | 12.3 ms                                                               | 12.4 ms: 1.01x slower                                        |
| unpickle             | 18.5 us                                                               | 18.7 us: 1.01x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                               | 12.6 ms: 1.11x slower                                        |
| python_startup_no_site | 8.37 ms                                                               | 10.9 ms: 1.30x slower                                        |
| Geometric mean         | (ref)                                                                 | 1.20x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 12.8 ms: 1.00x faster                                        |
| django_template | 40.7 ms                                                               | 40.9 ms: 1.00x slower                                        |
| genshi_text     | 27.4 ms                                                               | 27.9 ms: 1.02x slower                                        |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                 |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols   | 181 us                                                                | 138 us: 1.30x faster                                         |
| comprehensions             | 25.4 us                                                               | 19.7 us: 1.29x faster                                        |
| raytrace                   | 353 ms                                                                | 299 ms: 1.18x faster                                         |
| crypto_pyaes               | 86.6 ms                                                               | 77.5 ms: 1.12x faster                                        |
| sympy_sum                  | 154 ms                                                                | 140 ms: 1.10x faster                                         |
| generators                 | 43.5 ms                                                               | 39.5 ms: 1.10x faster                                        |
| async_tree_none            | 624 ms                                                                | 572 ms: 1.09x faster                                         |
| logging_format             | 8.34 us                                                               | 7.74 us: 1.08x faster                                        |
| sympy_str                  | 280 ms                                                                | 260 ms: 1.08x faster                                         |
| logging_simple             | 7.63 us                                                               | 7.12 us: 1.07x faster                                        |
| sqlglot_parse              | 1.46 ms                                                               | 1.37 ms: 1.07x faster                                        |
| chaos                      | 71.4 ms                                                               | 66.9 ms: 1.07x faster                                        |
| sqlglot_transpile          | 1.83 ms                                                               | 1.72 ms: 1.06x faster                                        |
| regex_compile              | 137 ms                                                                | 129 ms: 1.06x faster                                         |
| sympy_integrate            | 21.6 ms                                                               | 20.4 ms: 1.06x faster                                        |
| pylint                     | 355 ms                                                                | 336 ms: 1.06x faster                                         |
| async_tree_memoization     | 777 ms                                                                | 736 ms: 1.06x faster                                         |
| pickle_pure_python         | 365 us                                                                | 346 us: 1.05x faster                                         |
| scimark_monte_carlo        | 85.1 ms                                                               | 81.1 ms: 1.05x faster                                        |
| deepcopy_reduce            | 4.10 us                                                               | 3.93 us: 1.04x faster                                        |
| dulwich_log                | 62.0 ms                                                               | 59.4 ms: 1.04x faster                                        |
| aiohttp                    | 1.16 ms                                                               | 1.11 ms: 1.04x faster                                        |
| docutils                   | 2.98 sec                                                              | 2.88 sec: 1.04x faster                                       |
| scimark_lu                 | 146 ms                                                                | 141 ms: 1.04x faster                                         |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 882 ms: 1.03x faster                                         |
| regex_dna                  | 254 ms                                                                | 246 ms: 1.03x faster                                         |
| deltablue                  | 4.12 ms                                                               | 4.00 ms: 1.03x faster                                        |
| deepcopy_memo              | 49.6 us                                                               | 48.2 us: 1.03x faster                                        |
| deepcopy                   | 446 us                                                                | 433 us: 1.03x faster                                         |
| unpickle_pure_python       | 260 us                                                                | 253 us: 1.03x faster                                         |
| asyncio_tcp                | 566 ms                                                                | 551 ms: 1.03x faster                                         |
| mdp                        | 3.41 sec                                                              | 3.33 sec: 1.03x faster                                       |
| pathlib                    | 24.5 ms                                                               | 23.9 ms: 1.03x faster                                        |
| async_generators           | 491 ms                                                                | 480 ms: 1.02x faster                                         |
| bench_mp_pool              | 7.05 ms                                                               | 6.91 ms: 1.02x faster                                        |
| sqlglot_normalize          | 126 ms                                                                | 123 ms: 1.02x faster                                         |
| 2to3                       | 308 ms                                                                | 303 ms: 1.02x faster                                         |
| float                      | 92.1 ms                                                               | 90.6 ms: 1.02x faster                                        |
| nqueens                    | 99.2 ms                                                               | 97.6 ms: 1.02x faster                                        |
| thrift                     | 937 us                                                                | 923 us: 1.02x faster                                         |
| spectral_norm              | 131 ms                                                                | 129 ms: 1.02x faster                                         |
| create_gc_cycles           | 1.92 ms                                                               | 1.89 ms: 1.01x faster                                        |
| sqlglot_optimize           | 61.3 ms                                                               | 60.6 ms: 1.01x faster                                        |
| sympy_expand               | 454 ms                                                                | 448 ms: 1.01x faster                                         |
| pickle_list                | 5.25 us                                                               | 5.19 us: 1.01x faster                                        |
| json                       | 5.54 ms                                                               | 5.49 ms: 1.01x faster                                        |
| unpickle_list              | 6.17 us                                                               | 6.12 us: 1.01x faster                                        |
| tomli_loads                | 2.59 sec                                                              | 2.57 sec: 1.01x faster                                       |
| xml_etree_iterparse        | 150 ms                                                                | 149 ms: 1.01x faster                                         |
| regex_effbot               | 4.64 ms                                                               | 4.61 ms: 1.01x faster                                        |
| mako                       | 12.9 ms                                                               | 12.8 ms: 1.00x faster                                        |
| pprint_pformat             | 1.88 sec                                                              | 1.88 sec: 1.00x faster                                       |
| pickle                     | 13.4 us                                                               | 13.5 us: 1.00x slower                                        |
| nbody                      | 105 ms                                                                | 105 ms: 1.00x slower                                         |
| json_loads                 | 30.7 us                                                               | 30.8 us: 1.00x slower                                        |
| pickle_dict                | 37.3 us                                                               | 37.5 us: 1.00x slower                                        |
| django_template            | 40.7 ms                                                               | 40.9 ms: 1.00x slower                                        |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                         |
| xml_etree_process          | 79.0 ms                                                               | 79.5 ms: 1.01x slower                                        |
| xml_etree_generate         | 112 ms                                                                | 113 ms: 1.01x slower                                         |
| xml_etree_parse            | 195 ms                                                                | 196 ms: 1.01x slower                                         |
| hexiom                     | 6.98 ms                                                               | 7.03 ms: 1.01x slower                                        |
| coroutines                 | 29.0 ms                                                               | 29.2 ms: 1.01x slower                                        |
| gc_traversal               | 4.40 ms                                                               | 4.44 ms: 1.01x slower                                        |
| pyflate                    | 559 ms                                                                | 565 ms: 1.01x slower                                         |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.21 sec: 1.01x slower                                       |
| json_dumps                 | 12.3 ms                                                               | 12.4 ms: 1.01x slower                                        |
| unpickle                   | 18.5 us                                                               | 18.7 us: 1.01x slower                                        |
| chameleon                  | 8.81 ms                                                               | 8.96 ms: 1.02x slower                                        |
| genshi_text                | 27.4 ms                                                               | 27.9 ms: 1.02x slower                                        |
| go                         | 157 ms                                                                | 160 ms: 1.02x slower                                         |
| meteor_contest             | 112 ms                                                                | 114 ms: 1.02x slower                                         |
| async_tree_io              | 1.41 sec                                                              | 1.44 sec: 1.02x slower                                       |
| async_tree_none_tg         | 577 ms                                                                | 590 ms: 1.02x slower                                         |
| logging_silent             | 127 ns                                                                | 130 ns: 1.02x slower                                         |
| scimark_fft                | 418 ms                                                                | 428 ms: 1.02x slower                                         |
| richards                   | 50.9 ms                                                               | 52.2 ms: 1.02x slower                                        |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.34 ms: 1.02x slower                                        |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 907 ms: 1.03x slower                                         |
| async_tree_memoization_tg  | 740 ms                                                                | 763 ms: 1.03x slower                                         |
| fannkuch                   | 443 ms                                                                | 458 ms: 1.03x slower                                         |
| richards_super             | 58.5 ms                                                               | 60.7 ms: 1.04x slower                                        |
| async_tree_io_tg           | 1.40 sec                                                              | 1.47 sec: 1.05x slower                                       |
| gunicorn                   | 1.14 ms                                                               | 1.19 ms: 1.05x slower                                        |
| regex_v8                   | 28.3 ms                                                               | 30.0 ms: 1.06x slower                                        |
| scimark_sor                | 150 ms                                                                | 162 ms: 1.08x slower                                         |
| python_startup             | 11.4 ms                                                               | 12.6 ms: 1.11x slower                                        |
| telco                      | 8.51 ms                                                               | 9.69 ms: 1.14x slower                                        |
| coverage                   | 87.3 ms                                                               | 99.8 ms: 1.14x slower                                        |
| python_startup_no_site     | 8.37 ms                                                               | 10.9 ms: 1.30x slower                                        |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                 |

Benchmark hidden because not significant (9): bench_thread_pool, asyncio_websockets, sqlite_synth, tornado_http, pprint_safe_repr, genshi_xml, pycparser, html5lib, mypy2
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e.json: flaskblogging

# HPT report

- Reliability score: 90.29% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.87x