# Results vs. 3.12.0

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-aarch64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 360 ms: 1.17x slower                                                    |
| chameleon      | 8.81 ms                                                               | 9.19 ms: 1.04x slower                                                   |
| docutils       | 2.98 sec                                                              | 3.58 sec: 1.20x slower                                                  |
| html5lib       | 65.1 ms                                                               | 71.3 ms: 1.10x slower                                                   |
| tornado_http   | 136 ms                                                                | 140 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 508 ms: 1.23x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 630 ms: 1.18x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 491 ms: 1.17x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.23 sec: 1.14x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 685 ms: 1.13x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 788 ms: 1.12x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.27 sec: 1.11x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 822 ms: 1.11x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.15x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 89.3 ms: 1.03x faster                                                   |
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 115 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 251 ms: 1.01x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.90 ms: 1.06x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.2 ms: 1.07x slower                                                   |
| regex_compile  | 137 ms                                                                | 174 ms: 1.27x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.09x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_list          | 5.25 us                                                               | 5.27 us: 1.00x slower                                                   |
| pickle_dict          | 37.3 us                                                               | 37.7 us: 1.01x slower                                                   |
| pickle               | 13.4 us                                                               | 13.7 us: 1.02x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.66 sec: 1.03x slower                                                  |
| xml_etree_process    | 79.0 ms                                                               | 81.0 ms: 1.03x slower                                                   |
| xml_etree_generate   | 112 ms                                                                | 115 ms: 1.03x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 6.43 us: 1.04x slower                                                   |
| json_loads           | 30.7 us                                                               | 32.0 us: 1.04x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 275 us: 1.06x slower                                                    |
| unpickle             | 18.5 us                                                               | 19.5 us: 1.06x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 405 us: 1.11x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.04x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.7 ms: 1.28x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.2 ms: 1.33x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.31x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 50.4 ms: 1.24x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 34.8 ms: 1.27x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 81.7 ms: 1.35x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.21x slower                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 508 ms: 1.23x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 630 ms: 1.18x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 491 ms: 1.17x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.23 sec: 1.14x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 685 ms: 1.13x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.9 ms: 1.12x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 788 ms: 1.12x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.27 sec: 1.11x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 822 ms: 1.11x faster                                                    |
| comprehensions             | 25.4 us                                                               | 22.9 us: 1.11x faster                                                   |
| generators                 | 43.5 ms                                                               | 39.9 ms: 1.09x faster                                                   |
| raytrace                   | 353 ms                                                                | 325 ms: 1.09x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.38 us: 1.03x faster                                                   |
| float                      | 92.1 ms                                                               | 89.3 ms: 1.03x faster                                                   |
| logging_format             | 8.34 us                                                               | 8.13 us: 1.03x faster                                                   |
| regex_dna                  | 254 ms                                                                | 251 ms: 1.01x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 49.7 us: 1.00x slower                                                   |
| pickle_list                | 5.25 us                                                               | 5.27 us: 1.00x slower                                                   |
| mdp                        | 3.41 sec                                                              | 3.43 sec: 1.01x slower                                                  |
| asyncio_websockets         | 658 ms                                                                | 663 ms: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 37.7 us: 1.01x slower                                                   |
| json                       | 5.54 ms                                                               | 5.62 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.23 sec: 1.02x slower                                                  |
| pickle                     | 13.4 us                                                               | 13.7 us: 1.02x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.66 sec: 1.03x slower                                                  |
| xml_etree_process          | 79.0 ms                                                               | 81.0 ms: 1.03x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.34 ms: 1.03x slower                                                   |
| thrift                     | 937 us                                                                | 962 us: 1.03x slower                                                    |
| async_generators           | 491 ms                                                                | 505 ms: 1.03x slower                                                    |
| tornado_http               | 136 ms                                                                | 140 ms: 1.03x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 115 ms: 1.03x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.89 us: 1.03x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 89.5 ms: 1.03x slower                                                   |
| dask                       | 376 ms                                                                | 391 ms: 1.04x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 88.6 ms: 1.04x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.43 us: 1.04x slower                                                   |
| chameleon                  | 8.81 ms                                                               | 9.19 ms: 1.04x slower                                                   |
| json_loads                 | 30.7 us                                                               | 32.0 us: 1.04x slower                                                   |
| meteor_contest             | 112 ms                                                                | 118 ms: 1.05x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.90 ms: 1.06x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 275 us: 1.06x slower                                                    |
| unpickle                   | 18.5 us                                                               | 19.5 us: 1.06x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.2 ms: 1.07x slower                                                   |
| richards_super             | 58.5 ms                                                               | 62.4 ms: 1.07x slower                                                   |
| fannkuch                   | 443 ms                                                                | 475 ms: 1.07x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.57 ms: 1.07x slower                                                   |
| richards                   | 50.9 ms                                                               | 54.7 ms: 1.07x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.2 ms: 1.08x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 611 ms: 1.08x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.36 sec: 1.08x slower                                                  |
| sqlglot_transpile          | 1.83 ms                                                               | 1.98 ms: 1.09x slower                                                   |
| logging_silent             | 127 ns                                                                | 138 ns: 1.09x slower                                                    |
| nbody                      | 105 ms                                                                | 115 ms: 1.10x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 71.3 ms: 1.10x slower                                                   |
| pyflate                    | 559 ms                                                                | 616 ms: 1.10x slower                                                    |
| scimark_fft                | 418 ms                                                                | 462 ms: 1.10x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 405 us: 1.11x slower                                                    |
| spectral_norm              | 131 ms                                                                | 146 ms: 1.12x slower                                                    |
| deepcopy                   | 446 us                                                                | 499 us: 1.12x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.95 ms: 1.12x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 69.5 ms: 1.13x slower                                                   |
| deltablue                  | 4.12 ms                                                               | 4.69 ms: 1.14x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 143 ms: 1.14x slower                                                    |
| coverage                   | 87.3 ms                                                               | 99.5 ms: 1.14x slower                                                   |
| dulwich_log                | 62.0 ms                                                               | 70.8 ms: 1.14x slower                                                   |
| go                         | 157 ms                                                                | 179 ms: 1.14x slower                                                    |
| scimark_sor                | 150 ms                                                                | 173 ms: 1.16x slower                                                    |
| sympy_str                  | 280 ms                                                                | 323 ms: 1.16x slower                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.74 us: 1.16x slower                                                   |
| 2to3                       | 308 ms                                                                | 360 ms: 1.17x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 212 us: 1.18x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 8.41 ms: 1.19x slower                                                   |
| pylint                     | 355 ms                                                                | 423 ms: 1.19x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 5.25 ms: 1.20x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.58 sec: 1.20x slower                                                  |
| telco                      | 8.51 ms                                                               | 10.2 ms: 1.20x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 120 ms: 1.21x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 187 ms: 1.21x slower                                                    |
| sympy_expand               | 454 ms                                                                | 548 ms: 1.21x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.11 sec: 1.22x slower                                                  |
| pprint_pformat             | 1.88 sec                                                              | 2.30 sec: 1.22x slower                                                  |
| sympy_integrate            | 21.6 ms                                                               | 26.4 ms: 1.22x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.36 ms: 1.23x slower                                                   |
| chaos                      | 71.4 ms                                                               | 88.2 ms: 1.24x slower                                                   |
| django_template            | 40.7 ms                                                               | 50.4 ms: 1.24x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 181 ms: 1.24x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 34.8 ms: 1.27x slower                                                   |
| regex_compile              | 137 ms                                                                | 174 ms: 1.27x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 10.7 ms: 1.28x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 8.96 ms: 1.28x slower                                                   |
| python_startup             | 11.4 ms                                                               | 15.2 ms: 1.33x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 81.7 ms: 1.35x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.07x slower                                                            |

Benchmark hidden because not significant (4): coroutines, mako, xml_etree_iterparse, xml_etree_parse
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: flaskblogging

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.00x