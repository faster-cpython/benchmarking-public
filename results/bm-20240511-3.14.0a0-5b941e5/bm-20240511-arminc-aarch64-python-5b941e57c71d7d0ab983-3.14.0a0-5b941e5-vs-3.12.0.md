# Results vs. 3.12.0

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: linux-aarch64
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.03x slower
- HPT reliability: 67.81%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 306 ms: 1.01x faster                                                    |
| chameleon      | 8.81 ms                                                               | 8.99 ms: 1.02x slower                                                   |
| docutils       | 2.98 sec                                                              | 3.09 sec: 1.04x slower                                                  |
| html5lib       | 65.1 ms                                                               | 67.1 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 487 ms: 1.28x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 465 ms: 1.24x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 644 ms: 1.21x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 624 ms: 1.19x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 792 ms: 1.15x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.23 sec: 1.15x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.23 sec: 1.14x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 789 ms: 1.12x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.18x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 90.2 ms: 1.02x faster                                                   |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 112 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 130 ms: 1.06x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.93 ms: 1.06x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.7 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 260 us                                                                | 252 us: 1.03x faster                                                    |
| pickle_pure_python   | 365 us                                                                | 360 us: 1.01x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 149 ms: 1.01x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.58 sec: 1.00x faster                                                  |
| xml_etree_process    | 79.0 ms                                                               | 79.3 ms: 1.00x slower                                                   |
| pickle               | 13.4 us                                                               | 13.8 us: 1.03x slower                                                   |
| json_loads           | 30.7 us                                                               | 32.3 us: 1.05x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.6 us: 1.06x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.59 us: 1.07x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (4): pickle_list, xml_etree_parse, xml_etree_generate, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.55 ms: 1.02x slower                                                   |
| python_startup         | 11.4 ms                                                               | 12.5 ms: 1.10x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.06x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 28.0 ms: 1.02x slower                                                   |
| mako            | 12.9 ms                                                               | 13.2 ms: 1.03x slower                                                   |
| django_template | 40.7 ms                                                               | 41.9 ms: 1.03x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 487 ms: 1.28x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 465 ms: 1.24x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.9 us: 1.22x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 644 ms: 1.21x faster                                                    |
| raytrace                   | 353 ms                                                                | 296 ms: 1.19x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 624 ms: 1.19x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 792 ms: 1.15x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.23 sec: 1.15x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.23 sec: 1.14x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 789 ms: 1.12x faster                                                    |
| generators                 | 43.5 ms                                                               | 39.3 ms: 1.11x faster                                                   |
| logging_format             | 8.34 us                                                               | 7.76 us: 1.07x faster                                                   |
| deltablue                  | 4.12 ms                                                               | 3.85 ms: 1.07x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.15 us: 1.07x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 23.1 ms: 1.06x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 81.9 ms: 1.06x faster                                                   |
| regex_compile              | 137 ms                                                                | 130 ms: 1.06x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 138 ms: 1.06x faster                                                    |
| chaos                      | 71.4 ms                                                               | 67.8 ms: 1.05x faster                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.40 ms: 1.05x faster                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 1.75 ms: 1.05x faster                                                   |
| sympy_str                  | 280 ms                                                                | 269 ms: 1.04x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 149 ms: 1.04x faster                                                    |
| unpickle_pure_python       | 260 us                                                                | 252 us: 1.03x faster                                                    |
| pycparser                  | 1.26 sec                                                              | 1.22 sec: 1.03x faster                                                  |
| bench_thread_pool          | 1.31 ms                                                               | 1.28 ms: 1.02x faster                                                   |
| float                      | 92.1 ms                                                               | 90.2 ms: 1.02x faster                                                   |
| mdp                        | 3.41 sec                                                              | 3.35 sec: 1.02x faster                                                  |
| pickle_pure_python         | 365 us                                                                | 360 us: 1.01x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 83.9 ms: 1.01x faster                                                   |
| nqueens                    | 99.2 ms                                                               | 98.0 ms: 1.01x faster                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 149 ms: 1.01x faster                                                    |
| 2to3                       | 308 ms                                                                | 306 ms: 1.01x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.58 sec: 1.00x faster                                                  |
| xml_etree_process          | 79.0 ms                                                               | 79.3 ms: 1.00x slower                                                   |
| asyncio_websockets         | 658 ms                                                                | 663 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.21 sec: 1.01x slower                                                  |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| meteor_contest             | 112 ms                                                                | 113 ms: 1.01x slower                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.15 us: 1.01x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 7.14 ms: 1.01x slower                                                   |
| sympy_expand               | 454 ms                                                                | 459 ms: 1.01x slower                                                    |
| thrift                     | 937 us                                                                | 952 us: 1.02x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 576 ms: 1.02x slower                                                    |
| deepcopy                   | 446 us                                                                | 454 us: 1.02x slower                                                    |
| chameleon                  | 8.81 ms                                                               | 8.99 ms: 1.02x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 7.11 ms: 1.02x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 1.92 sec: 1.02x slower                                                  |
| python_startup_no_site     | 8.37 ms                                                               | 8.55 ms: 1.02x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 62.6 ms: 1.02x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 28.0 ms: 1.02x slower                                                   |
| json                       | 5.54 ms                                                               | 5.67 ms: 1.02x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.03x slower                                                   |
| pickle                     | 13.4 us                                                               | 13.8 us: 1.03x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 129 ms: 1.03x slower                                                    |
| go                         | 157 ms                                                                | 161 ms: 1.03x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 941 ms: 1.03x slower                                                    |
| django_template            | 40.7 ms                                                               | 41.9 ms: 1.03x slower                                                   |
| richards_super             | 58.5 ms                                                               | 60.3 ms: 1.03x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 67.1 ms: 1.03x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.90 us: 1.03x slower                                                   |
| deepcopy_memo              | 49.6 us                                                               | 51.4 us: 1.04x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.09 sec: 1.04x slower                                                  |
| pyflate                    | 559 ms                                                                | 581 ms: 1.04x slower                                                    |
| fannkuch                   | 443 ms                                                                | 461 ms: 1.04x slower                                                    |
| richards                   | 50.9 ms                                                               | 53.4 ms: 1.05x slower                                                   |
| logging_silent             | 127 ns                                                                | 134 ns: 1.05x slower                                                    |
| scimark_sor                | 150 ms                                                                | 158 ms: 1.05x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.3 us: 1.05x slower                                                   |
| unpickle                   | 18.5 us                                                               | 19.6 us: 1.06x slower                                                   |
| scimark_fft                | 418 ms                                                                | 444 ms: 1.06x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.93 ms: 1.06x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.58 ms: 1.06x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.59 us: 1.07x slower                                                   |
| nbody                      | 105 ms                                                                | 112 ms: 1.07x slower                                                    |
| spectral_norm              | 131 ms                                                                | 141 ms: 1.08x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 13.3 ms: 1.08x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.7 ms: 1.08x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 196 us: 1.09x slower                                                    |
| python_startup             | 11.4 ms                                                               | 12.5 ms: 1.10x slower                                                   |
| coverage                   | 87.3 ms                                                               | 97.5 ms: 1.12x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 5.14 ms: 1.17x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.40 ms: 1.25x slower                                                   |
| telco                      | 8.51 ms                                                               | 164 ms: 19.25x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (13): pylint, tornado_http, pickle_list, dulwich_log, xml_etree_parse, xml_etree_generate, async_generators, sympy_integrate, pickle_dict, regex_dna, coroutines, genshi_xml, dask
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240511-3.14.0a0-5b941e5/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json: flaskblogging

# HPT report

- Reliability score: 67.81% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x