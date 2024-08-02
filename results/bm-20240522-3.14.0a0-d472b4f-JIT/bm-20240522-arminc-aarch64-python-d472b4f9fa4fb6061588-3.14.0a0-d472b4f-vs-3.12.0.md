# Results vs. 3.12.0

- fork: python
- ref: d472b4f9fa4fb6061588
- machine: linux-aarch64
- commit hash: d472b4f
- commit date: 2024-05-22
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 361 ms: 1.17x slower                                                    |
| chameleon      | 8.81 ms                                                               | 9.28 ms: 1.05x slower                                                   |
| docutils       | 2.98 sec                                                              | 3.56 sec: 1.19x slower                                                  |
| html5lib       | 65.1 ms                                                               | 71.4 ms: 1.10x slower                                                   |
| tornado_http   | 136 ms                                                                | 139 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 517 ms: 1.20x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 489 ms: 1.18x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 633 ms: 1.17x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 684 ms: 1.14x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.24 sec: 1.13x faster                                                  |
| async_tree_io              | 1.41 sec                                                              | 1.26 sec: 1.12x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 825 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 801 ms: 1.10x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.14x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 91.4 ms: 1.01x faster                                                   |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 116 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.91 ms: 1.06x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.5 ms: 1.08x slower                                                   |
| regex_compile  | 137 ms                                                                | 172 ms: 1.25x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.09x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 189 ms: 1.03x faster                                                    |
| xml_etree_generate   | 112 ms                                                                | 113 ms: 1.01x slower                                                    |
| pickle_dict          | 37.3 us                                                               | 37.8 us: 1.01x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.63 sec: 1.02x slower                                                  |
| xml_etree_process    | 79.0 ms                                                               | 80.4 ms: 1.02x slower                                                   |
| pickle               | 13.4 us                                                               | 13.8 us: 1.03x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.41 us: 1.04x slower                                                   |
| json_loads           | 30.7 us                                                               | 32.3 us: 1.05x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.7 us: 1.07x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 278 us: 1.07x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 398 us: 1.09x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (2): pickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.8 ms: 1.29x slower                                                   |
| python_startup         | 11.4 ms                                                               | 14.8 ms: 1.31x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 51.5 ms: 1.27x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 35.3 ms: 1.29x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 83.8 ms: 1.38x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.23x slower                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 517 ms: 1.20x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 489 ms: 1.18x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 633 ms: 1.17x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 684 ms: 1.14x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.6 ms: 1.13x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.24 sec: 1.13x faster                                                  |
| generators                 | 43.5 ms                                                               | 38.6 ms: 1.13x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.26 sec: 1.12x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 825 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 801 ms: 1.10x faster                                                    |
| comprehensions             | 25.4 us                                                               | 23.1 us: 1.10x faster                                                   |
| raytrace                   | 353 ms                                                                | 324 ms: 1.09x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.99 us: 1.04x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.32 us: 1.04x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 189 ms: 1.03x faster                                                    |
| float                      | 92.1 ms                                                               | 91.4 ms: 1.01x faster                                                   |
| coroutines                 | 29.0 ms                                                               | 28.9 ms: 1.00x faster                                                   |
| xml_etree_generate         | 112 ms                                                                | 113 ms: 1.01x slower                                                    |
| deepcopy_memo              | 49.6 us                                                               | 50.0 us: 1.01x slower                                                   |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 664 ms: 1.01x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 37.8 us: 1.01x slower                                                   |
| mdp                        | 3.41 sec                                                              | 3.46 sec: 1.01x slower                                                  |
| tomli_loads                | 2.59 sec                                                              | 2.63 sec: 1.02x slower                                                  |
| bench_thread_pool          | 1.31 ms                                                               | 1.33 ms: 1.02x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 80.4 ms: 1.02x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.86 us: 1.02x slower                                                   |
| tornado_http               | 136 ms                                                                | 139 ms: 1.02x slower                                                    |
| pickle                     | 13.4 us                                                               | 13.8 us: 1.03x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.26 sec: 1.03x slower                                                  |
| dask                       | 376 ms                                                                | 389 ms: 1.03x slower                                                    |
| json                       | 5.54 ms                                                               | 5.72 ms: 1.03x slower                                                   |
| thrift                     | 937 us                                                                | 972 us: 1.04x slower                                                    |
| fannkuch                   | 443 ms                                                                | 460 ms: 1.04x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.41 us: 1.04x slower                                                   |
| async_generators           | 491 ms                                                                | 511 ms: 1.04x slower                                                    |
| meteor_contest             | 112 ms                                                                | 117 ms: 1.04x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 90.7 ms: 1.05x slower                                                   |
| richards_super             | 58.5 ms                                                               | 61.4 ms: 1.05x slower                                                   |
| chameleon                  | 8.81 ms                                                               | 9.28 ms: 1.05x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.3 us: 1.05x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.91 ms: 1.06x slower                                                   |
| unpickle                   | 18.5 us                                                               | 19.7 us: 1.07x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 278 us: 1.07x slower                                                    |
| richards                   | 50.9 ms                                                               | 54.7 ms: 1.07x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.5 ms: 1.08x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.36 sec: 1.08x slower                                                  |
| asyncio_tcp                | 566 ms                                                                | 617 ms: 1.09x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 398 us: 1.09x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 92.8 ms: 1.09x slower                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.60 ms: 1.09x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 71.4 ms: 1.10x slower                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 2.01 ms: 1.10x slower                                                   |
| scimark_fft                | 418 ms                                                                | 461 ms: 1.10x slower                                                    |
| nbody                      | 105 ms                                                                | 116 ms: 1.11x slower                                                    |
| logging_silent             | 127 ns                                                                | 140 ns: 1.11x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.91 ms: 1.12x slower                                                   |
| deltablue                  | 4.12 ms                                                               | 4.62 ms: 1.12x slower                                                   |
| spectral_norm              | 131 ms                                                                | 147 ms: 1.12x slower                                                    |
| deepcopy                   | 446 us                                                                | 503 us: 1.13x slower                                                    |
| pyflate                    | 559 ms                                                                | 633 ms: 1.13x slower                                                    |
| go                         | 157 ms                                                                | 179 ms: 1.14x slower                                                    |
| coverage                   | 87.3 ms                                                               | 99.6 ms: 1.14x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 70.3 ms: 1.15x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 144 ms: 1.15x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 8.11 ms: 1.15x slower                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 4.72 us: 1.15x slower                                                   |
| sympy_str                  | 280 ms                                                                | 323 ms: 1.15x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 208 us: 1.15x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 71.9 ms: 1.16x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 5.10 ms: 1.16x slower                                                   |
| pylint                     | 355 ms                                                                | 413 ms: 1.16x slower                                                    |
| scimark_sor                | 150 ms                                                                | 175 ms: 1.17x slower                                                    |
| 2to3                       | 308 ms                                                                | 361 ms: 1.17x slower                                                    |
| sympy_expand               | 454 ms                                                                | 541 ms: 1.19x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 184 ms: 1.19x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.56 sec: 1.19x slower                                                  |
| nqueens                    | 99.2 ms                                                               | 119 ms: 1.20x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 26.0 ms: 1.20x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.10 sec: 1.20x slower                                                  |
| telco                      | 8.51 ms                                                               | 10.3 ms: 1.21x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.30 sec: 1.22x slower                                                  |
| chaos                      | 71.4 ms                                                               | 88.8 ms: 1.24x slower                                                   |
| regex_compile              | 137 ms                                                                | 172 ms: 1.25x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 183 ms: 1.25x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 2.42 ms: 1.26x slower                                                   |
| django_template            | 40.7 ms                                                               | 51.5 ms: 1.27x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 35.3 ms: 1.29x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 10.8 ms: 1.29x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 9.07 ms: 1.30x slower                                                   |
| python_startup             | 11.4 ms                                                               | 14.8 ms: 1.31x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 83.8 ms: 1.38x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.07x slower                                                            |

Benchmark hidden because not significant (4): pickle_list, regex_dna, mako, xml_etree_iterparse
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240522-3.14.0a0-d472b4f-JIT/bm-20240522-arminc-aarch64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f.json: flaskblogging

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.00x