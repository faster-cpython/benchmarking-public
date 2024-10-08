# Results vs. 3.12.0

- fork: python
- ref: v3.13.0b1
- machine: linux-aarch64
- commit hash: 2268289
- commit date: 2024-05-08
- overall geometric mean: 1.03x slower
- HPT reliability: 77.53%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| chameleon      | 8.81 ms                                                               | 9.23 ms: 1.05x slower                                        |
| docutils       | 2.98 sec                                                              | 3.12 sec: 1.04x slower                                       |
| html5lib       | 65.1 ms                                                               | 66.6 ms: 1.02x slower                                        |
| tornado_http   | 136 ms                                                                | 130 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                 |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 491 ms: 1.27x faster                                         |
| async_tree_none_tg         | 577 ms                                                                | 472 ms: 1.22x faster                                         |
| async_tree_memoization     | 777 ms                                                                | 645 ms: 1.20x faster                                         |
| async_tree_memoization_tg  | 740 ms                                                                | 628 ms: 1.18x faster                                         |
| async_tree_io              | 1.41 sec                                                              | 1.21 sec: 1.17x faster                                       |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 799 ms: 1.14x faster                                         |
| async_tree_io_tg           | 1.40 sec                                                              | 1.23 sec: 1.14x faster                                       |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 795 ms: 1.11x faster                                         |
| Geometric mean             | (ref)                                                                 | 1.18x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 90.7 ms: 1.02x faster                                        |
| pidigits       | 233 ms                                                                | 236 ms: 1.01x slower                                         |
| nbody          | 105 ms                                                                | 110 ms: 1.06x slower                                         |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 130 ms: 1.06x faster                                         |
| regex_dna      | 254 ms                                                                | 257 ms: 1.01x slower                                         |
| regex_effbot   | 4.64 ms                                                               | 4.93 ms: 1.06x slower                                        |
| regex_v8       | 28.3 ms                                                               | 31.5 ms: 1.11x slower                                        |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 260 us                                                                | 255 us: 1.02x faster                                         |
| tomli_loads          | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                       |
| pickle_dict          | 37.3 us                                                               | 38.0 us: 1.02x slower                                        |
| pickle               | 13.4 us                                                               | 13.7 us: 1.02x slower                                        |
| unpickle_list        | 6.17 us                                                               | 6.31 us: 1.02x slower                                        |
| xml_etree_process    | 79.0 ms                                                               | 82.2 ms: 1.04x slower                                        |
| json_loads           | 30.7 us                                                               | 32.3 us: 1.05x slower                                        |
| xml_etree_generate   | 112 ms                                                                | 118 ms: 1.05x slower                                         |
| unpickle             | 18.5 us                                                               | 19.5 us: 1.06x slower                                        |
| json_dumps           | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                 |

Benchmark hidden because not significant (4): pickle_pure_python, xml_etree_iterparse, pickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup | 11.4 ms                                                               | 12.6 ms: 1.11x slower                                        |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                 |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                        |
| genshi_text     | 27.4 ms                                                               | 28.0 ms: 1.02x slower                                        |
| django_template | 40.7 ms                                                               | 42.6 ms: 1.05x slower                                        |
| Geometric mean  | (ref)                                                                 | 1.03x slower                                                 |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 491 ms: 1.27x faster                                         |
| comprehensions             | 25.4 us                                                               | 20.3 us: 1.25x faster                                        |
| async_tree_none_tg         | 577 ms                                                                | 472 ms: 1.22x faster                                         |
| async_tree_memoization     | 777 ms                                                                | 645 ms: 1.20x faster                                         |
| raytrace                   | 353 ms                                                                | 297 ms: 1.19x faster                                         |
| async_tree_memoization_tg  | 740 ms                                                                | 628 ms: 1.18x faster                                         |
| generators                 | 43.5 ms                                                               | 37.3 ms: 1.17x faster                                        |
| async_tree_io              | 1.41 sec                                                              | 1.21 sec: 1.17x faster                                       |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 799 ms: 1.14x faster                                         |
| async_tree_io_tg           | 1.40 sec                                                              | 1.23 sec: 1.14x faster                                       |
| mypy2                      | 873 ms                                                                | 771 ms: 1.13x faster                                         |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 795 ms: 1.11x faster                                         |
| chaos                      | 71.4 ms                                                               | 66.5 ms: 1.07x faster                                        |
| logging_format             | 8.34 us                                                               | 7.78 us: 1.07x faster                                        |
| logging_simple             | 7.63 us                                                               | 7.15 us: 1.07x faster                                        |
| pathlib                    | 24.5 ms                                                               | 23.1 ms: 1.06x faster                                        |
| sympy_sum                  | 154 ms                                                                | 146 ms: 1.06x faster                                         |
| regex_compile              | 137 ms                                                                | 130 ms: 1.06x faster                                         |
| deltablue                  | 4.12 ms                                                               | 3.90 ms: 1.06x faster                                        |
| sqlglot_transpile          | 1.83 ms                                                               | 1.73 ms: 1.05x faster                                        |
| crypto_pyaes               | 86.6 ms                                                               | 82.4 ms: 1.05x faster                                        |
| scimark_lu                 | 146 ms                                                                | 139 ms: 1.04x faster                                         |
| dulwich_log                | 62.0 ms                                                               | 59.5 ms: 1.04x faster                                        |
| asyncio_tcp                | 566 ms                                                                | 545 ms: 1.04x faster                                         |
| tornado_http               | 136 ms                                                                | 130 ms: 1.04x faster                                         |
| sympy_str                  | 280 ms                                                                | 270 ms: 1.03x faster                                         |
| sqlglot_parse              | 1.46 ms                                                               | 1.42 ms: 1.03x faster                                        |
| scimark_monte_carlo        | 85.1 ms                                                               | 83.1 ms: 1.02x faster                                        |
| bench_thread_pool          | 1.31 ms                                                               | 1.28 ms: 1.02x faster                                        |
| mdp                        | 3.41 sec                                                              | 3.34 sec: 1.02x faster                                       |
| unpickle_pure_python       | 260 us                                                                | 255 us: 1.02x faster                                         |
| pycparser                  | 1.26 sec                                                              | 1.23 sec: 1.02x faster                                       |
| float                      | 92.1 ms                                                               | 90.7 ms: 1.02x faster                                        |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.17 sec: 1.01x faster                                       |
| thrift                     | 937 us                                                                | 946 us: 1.01x slower                                         |
| regex_dna                  | 254 ms                                                                | 257 ms: 1.01x slower                                         |
| asyncio_websockets         | 658 ms                                                                | 666 ms: 1.01x slower                                         |
| pidigits                   | 233 ms                                                                | 236 ms: 1.01x slower                                         |
| hexiom                     | 6.98 ms                                                               | 7.07 ms: 1.01x slower                                        |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                         |
| go                         | 157 ms                                                                | 160 ms: 1.02x slower                                         |
| tomli_loads                | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                       |
| deepcopy                   | 446 us                                                                | 453 us: 1.02x slower                                         |
| nqueens                    | 99.2 ms                                                               | 101 ms: 1.02x slower                                         |
| pickle_dict                | 37.3 us                                                               | 38.0 us: 1.02x slower                                        |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                        |
| json                       | 5.54 ms                                                               | 5.65 ms: 1.02x slower                                        |
| pickle                     | 13.4 us                                                               | 13.7 us: 1.02x slower                                        |
| coroutines                 | 29.0 ms                                                               | 29.7 ms: 1.02x slower                                        |
| genshi_text                | 27.4 ms                                                               | 28.0 ms: 1.02x slower                                        |
| unpickle_list              | 6.17 us                                                               | 6.31 us: 1.02x slower                                        |
| html5lib                   | 65.1 ms                                                               | 66.6 ms: 1.02x slower                                        |
| sqlglot_normalize          | 126 ms                                                                | 129 ms: 1.03x slower                                         |
| deepcopy_memo              | 49.6 us                                                               | 51.0 us: 1.03x slower                                        |
| pprint_pformat             | 1.88 sec                                                              | 1.94 sec: 1.03x slower                                       |
| aiohttp                    | 1.16 ms                                                               | 1.20 ms: 1.03x slower                                        |
| sqlite_synth               | 3.77 us                                                               | 3.89 us: 1.03x slower                                        |
| pprint_safe_repr           | 916 ms                                                                | 948 ms: 1.03x slower                                         |
| sympy_expand               | 454 ms                                                                | 470 ms: 1.04x slower                                         |
| sqlglot_optimize           | 61.3 ms                                                               | 63.6 ms: 1.04x slower                                        |
| xml_etree_process          | 79.0 ms                                                               | 82.2 ms: 1.04x slower                                        |
| docutils                   | 2.98 sec                                                              | 3.12 sec: 1.04x slower                                       |
| django_template            | 40.7 ms                                                               | 42.6 ms: 1.05x slower                                        |
| chameleon                  | 8.81 ms                                                               | 9.23 ms: 1.05x slower                                        |
| fannkuch                   | 443 ms                                                                | 465 ms: 1.05x slower                                         |
| json_loads                 | 30.7 us                                                               | 32.3 us: 1.05x slower                                        |
| xml_etree_generate         | 112 ms                                                                | 118 ms: 1.05x slower                                         |
| nbody                      | 105 ms                                                                | 110 ms: 1.06x slower                                         |
| unpickle                   | 18.5 us                                                               | 19.5 us: 1.06x slower                                        |
| scimark_fft                | 418 ms                                                                | 442 ms: 1.06x slower                                         |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.56 ms: 1.06x slower                                        |
| logging_silent             | 127 ns                                                                | 135 ns: 1.06x slower                                         |
| regex_effbot               | 4.64 ms                                                               | 4.93 ms: 1.06x slower                                        |
| pyflate                    | 559 ms                                                                | 595 ms: 1.06x slower                                         |
| spectral_norm              | 131 ms                                                                | 139 ms: 1.07x slower                                         |
| gunicorn                   | 1.14 ms                                                               | 1.21 ms: 1.07x slower                                        |
| scimark_sor                | 150 ms                                                                | 160 ms: 1.07x slower                                         |
| richards_super             | 58.5 ms                                                               | 62.8 ms: 1.07x slower                                        |
| json_dumps                 | 12.3 ms                                                               | 13.4 ms: 1.09x slower                                        |
| richards                   | 50.9 ms                                                               | 56.3 ms: 1.11x slower                                        |
| python_startup             | 11.4 ms                                                               | 12.6 ms: 1.11x slower                                        |
| regex_v8                   | 28.3 ms                                                               | 31.5 ms: 1.11x slower                                        |
| typing_runtime_protocols   | 181 us                                                                | 203 us: 1.13x slower                                         |
| coverage                   | 87.3 ms                                                               | 98.6 ms: 1.13x slower                                        |
| gc_traversal               | 4.40 ms                                                               | 5.09 ms: 1.16x slower                                        |
| create_gc_cycles           | 1.92 ms                                                               | 2.43 ms: 1.27x slower                                        |
| telco                      | 8.51 ms                                                               | 167 ms: 19.68x slower                                        |
| Geometric mean             | (ref)                                                                 | 1.03x slower                                                 |

Benchmark hidden because not significant (13): pylint, sympy_integrate, 2to3, async_generators, pickle_pure_python, deepcopy_reduce, bench_mp_pool, xml_etree_iterparse, pickle_list, dask, python_startup_no_site, genshi_xml, xml_etree_parse
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240508-3.13.0b1-2268289/bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289.json: flaskblogging

# HPT report

- Reliability score: 77.53% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.92x