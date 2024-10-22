# Results vs. 3.12.0

- fork: python
- ref: 52caaef6d01a94962576
- machine: linux-aarch64
- commit hash: 52caaef
- commit date: 2024-08-24
- overall geometric mean: 1.56x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.37x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 521 ms: 1.69x slower                                                    |
| docutils       | 2.98 sec                                                              | 4.04 sec: 1.35x slower                                                  |
| html5lib       | 65.1 ms                                                               | 122 ms: 1.87x slower                                                    |
| tornado_http   | 136 ms                                                                | 204 ms: 1.51x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.59x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 695 ms: 1.07x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 738 ms: 1.05x faster                                                    |
| async_tree_none            | 624 ms                                                                | 606 ms: 1.03x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.37 sec: 1.03x faster                                                  |
| async_tree_none_tg         | 577 ms                                                                | 570 ms: 1.01x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 877 ms: 1.01x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.02x faster                                                            |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| float          | 92.1 ms                                                               | 209 ms: 2.27x slower                                                    |
| nbody          | 105 ms                                                                | 282 ms: 2.69x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.83x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.48 ms: 1.04x faster                                                   |
| regex_dna      | 254 ms                                                                | 258 ms: 1.01x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 32.8 ms: 1.16x slower                                                   |
| regex_compile  | 137 ms                                                                | 260 ms: 1.89x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.21x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 184 ms: 1.06x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 160 ms: 1.06x slower                                                    |
| json_loads           | 30.7 us                                                               | 39.5 us: 1.29x slower                                                   |
| xml_etree_generate   | 112 ms                                                                | 162 ms: 1.44x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 18.3 ms: 1.49x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 4.20 sec: 1.62x slower                                                  |
| xml_etree_process    | 79.0 ms                                                               | 131 ms: 1.66x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 548 us: 2.11x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 776 us: 2.12x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.48x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.1 ms: 1.44x slower                                                   |
| python_startup         | 11.4 ms                                                               | 18.0 ms: 1.58x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.51x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 105 ms: 1.74x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 53.4 ms: 1.95x slower                                                   |
| django_template | 40.7 ms                                                               | 84.2 ms: 2.07x slower                                                   |
| mako            | 12.9 ms                                                               | 28.9 ms: 2.24x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.99x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 4.40 ms                                                               | 3.50 ms: 1.26x faster                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 1.64 ms: 1.17x faster                                                   |
| async_tree_memoization_tg  | 740 ms                                                                | 695 ms: 1.07x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 184 ms: 1.06x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 738 ms: 1.05x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.48 ms: 1.04x faster                                                   |
| async_tree_none            | 624 ms                                                                | 606 ms: 1.03x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.37 sec: 1.03x faster                                                  |
| bench_mp_pool              | 7.05 ms                                                               | 6.96 ms: 1.01x faster                                                   |
| async_tree_none_tg         | 577 ms                                                                | 570 ms: 1.01x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 877 ms: 1.01x faster                                                    |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| regex_dna                  | 254 ms                                                                | 258 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 672 ms: 1.02x slower                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 160 ms: 1.06x slower                                                    |
| pathlib                    | 24.5 ms                                                               | 26.8 ms: 1.09x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.46 sec: 1.12x slower                                                  |
| asyncio_tcp                | 566 ms                                                                | 642 ms: 1.13x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 32.8 ms: 1.16x slower                                                   |
| mdp                        | 3.41 sec                                                              | 4.34 sec: 1.27x slower                                                  |
| deepcopy                   | 446 us                                                                | 566 us: 1.27x slower                                                    |
| json                       | 5.54 ms                                                               | 7.12 ms: 1.29x slower                                                   |
| json_loads                 | 30.7 us                                                               | 39.5 us: 1.29x slower                                                   |
| generators                 | 43.5 ms                                                               | 57.4 ms: 1.32x slower                                                   |
| docutils                   | 2.98 sec                                                              | 4.04 sec: 1.35x slower                                                  |
| async_generators           | 491 ms                                                                | 665 ms: 1.36x slower                                                    |
| scimark_fft                | 418 ms                                                                | 576 ms: 1.38x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 41.3 ms: 1.42x slower                                                   |
| pylint                     | 355 ms                                                                | 509 ms: 1.44x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 162 ms: 1.44x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 12.1 ms: 1.44x slower                                                   |
| deepcopy_memo              | 49.6 us                                                               | 72.2 us: 1.46x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 9.03 ms: 1.46x slower                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 6.08 us: 1.48x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 18.3 ms: 1.49x slower                                                   |
| meteor_contest             | 112 ms                                                                | 167 ms: 1.49x slower                                                    |
| tornado_http               | 136 ms                                                                | 204 ms: 1.51x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 153 ms: 1.54x slower                                                    |
| telco                      | 8.51 ms                                                               | 13.2 ms: 1.55x slower                                                   |
| coverage                   | 87.3 ms                                                               | 136 ms: 1.55x slower                                                    |
| python_startup             | 11.4 ms                                                               | 18.0 ms: 1.58x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 137 ms: 1.59x slower                                                    |
| comprehensions             | 25.4 us                                                               | 40.7 us: 1.60x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 2.10 ms: 1.61x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 34.7 ms: 1.61x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 2.03 sec: 1.61x slower                                                  |
| tomli_loads                | 2.59 sec                                                              | 4.20 sec: 1.62x slower                                                  |
| xml_etree_process          | 79.0 ms                                                               | 131 ms: 1.66x slower                                                    |
| fannkuch                   | 443 ms                                                                | 740 ms: 1.67x slower                                                    |
| 2to3                       | 308 ms                                                                | 521 ms: 1.69x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 105 ms: 1.74x slower                                                    |
| thrift                     | 937 us                                                                | 1.66 ms: 1.77x slower                                                   |
| spectral_norm              | 131 ms                                                                | 233 ms: 1.78x slower                                                    |
| pyflate                    | 559 ms                                                                | 1.01 sec: 1.81x slower                                                  |
| sympy_str                  | 280 ms                                                                | 514 ms: 1.84x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 234 ms: 1.86x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 122 ms: 1.87x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 339 us: 1.88x slower                                                    |
| logging_format             | 8.34 us                                                               | 15.7 us: 1.88x slower                                                   |
| regex_compile              | 137 ms                                                                | 260 ms: 1.89x slower                                                    |
| logging_simple             | 7.63 us                                                               | 14.5 us: 1.89x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 117 ms: 1.90x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.78 sec: 1.94x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 3.66 sec: 1.94x slower                                                  |
| genshi_text                | 27.4 ms                                                               | 53.4 ms: 1.95x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 315 ms: 2.04x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 174 ms: 2.04x slower                                                    |
| django_template            | 40.7 ms                                                               | 84.2 ms: 2.07x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 548 us: 2.11x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 776 us: 2.12x slower                                                    |
| sympy_expand               | 454 ms                                                                | 969 ms: 2.14x slower                                                    |
| chaos                      | 71.4 ms                                                               | 159 ms: 2.23x slower                                                    |
| mako                       | 12.9 ms                                                               | 28.9 ms: 2.24x slower                                                   |
| logging_silent             | 127 ns                                                                | 287 ns: 2.26x slower                                                    |
| float                      | 92.1 ms                                                               | 209 ms: 2.27x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 15.9 ms: 2.28x slower                                                   |
| scimark_sor                | 150 ms                                                                | 342 ms: 2.29x slower                                                    |
| richards                   | 50.9 ms                                                               | 118 ms: 2.31x slower                                                    |
| raytrace                   | 353 ms                                                                | 817 ms: 2.31x slower                                                    |
| richards_super             | 58.5 ms                                                               | 138 ms: 2.35x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 4.30 ms: 2.35x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 355 ms: 2.44x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 3.70 ms: 2.52x slower                                                   |
| nbody                      | 105 ms                                                                | 282 ms: 2.69x slower                                                    |
| go                         | 157 ms                                                                | 443 ms: 2.82x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 12.8 ms: 3.12x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.56x slower                                                            |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_io
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240824-3.14.0a0-52caaef-NOGIL/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.47x
- 95% likely to have a slowdown of 1.44x
- 99% likely to have a slowdown of 1.37x

# Memory
- memory change: 1.08x