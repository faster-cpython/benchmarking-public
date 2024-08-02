# Results vs. 3.12.0

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: linux-aarch64
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.16x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 354 ms: 1.15x slower                                                    |
| chameleon      | 8.81 ms                                                               | 9.96 ms: 1.13x slower                                                   |
| docutils       | 2.98 sec                                                              | 3.54 sec: 1.19x slower                                                  |
| html5lib       | 65.1 ms                                                               | 74.8 ms: 1.15x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 478 ms: 1.21x faster                                                    |
| async_tree_none            | 624 ms                                                                | 517 ms: 1.20x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 629 ms: 1.18x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 670 ms: 1.16x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.25 sec: 1.13x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 816 ms: 1.12x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.26 sec: 1.11x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 802 ms: 1.10x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.15x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 237 ms: 1.02x slower                                                    |
| float          | 92.1 ms                                                               | 114 ms: 1.23x slower                                                    |
| nbody          | 105 ms                                                                | 138 ms: 1.32x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.18x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 261 ms: 1.03x slower                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.96 ms: 1.07x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 31.1 ms: 1.10x slower                                                   |
| regex_compile  | 137 ms                                                                | 167 ms: 1.21x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_list          | 5.25 us                                                               | 5.23 us: 1.00x faster                                                   |
| pickle               | 13.4 us                                                               | 13.9 us: 1.03x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.51 us: 1.06x slower                                                   |
| json_loads           | 30.7 us                                                               | 32.6 us: 1.06x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.6 us: 1.06x slower                                                   |
| xml_etree_iterparse  | 150 ms                                                                | 162 ms: 1.08x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 125 ms: 1.11x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 88.5 ms: 1.12x slower                                                   |
| json_dumps           | 12.3 ms                                                               | 14.0 ms: 1.14x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 3.08 sec: 1.19x slower                                                  |
| pickle_pure_python   | 365 us                                                                | 449 us: 1.23x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 349 us: 1.34x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.10x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_parse, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.47 ms: 1.01x slower                                                   |
| python_startup         | 11.4 ms                                                               | 12.5 ms: 1.10x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.06x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 49.9 ms: 1.23x slower                                                   |
| mako            | 12.9 ms                                                               | 16.5 ms: 1.28x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 77.7 ms: 1.28x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 36.6 ms: 1.34x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.28x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 478 ms: 1.21x faster                                                    |
| async_tree_none            | 624 ms                                                                | 517 ms: 1.20x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 629 ms: 1.18x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 670 ms: 1.16x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.25 sec: 1.13x faster                                                  |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 816 ms: 1.12x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.26 sec: 1.11x faster                                                  |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 802 ms: 1.10x faster                                                    |
| generators                 | 43.5 ms                                                               | 39.7 ms: 1.10x faster                                                   |
| logging_simple             | 7.63 us                                                               | 7.28 us: 1.05x faster                                                   |
| raytrace                   | 353 ms                                                                | 342 ms: 1.03x faster                                                    |
| logging_format             | 8.34 us                                                               | 8.09 us: 1.03x faster                                                   |
| pathlib                    | 24.5 ms                                                               | 24.3 ms: 1.01x faster                                                   |
| pickle_list                | 5.25 us                                                               | 5.23 us: 1.00x faster                                                   |
| asyncio_websockets         | 658 ms                                                                | 662 ms: 1.01x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 8.47 ms: 1.01x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 575 ms: 1.01x slower                                                    |
| pidigits                   | 233 ms                                                                | 237 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.24 sec: 1.02x slower                                                  |
| regex_dna                  | 254 ms                                                                | 261 ms: 1.03x slower                                                    |
| dask                       | 376 ms                                                                | 387 ms: 1.03x slower                                                    |
| pickle                     | 13.4 us                                                               | 13.9 us: 1.03x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.36 ms: 1.04x slower                                                   |
| json                       | 5.54 ms                                                               | 5.79 ms: 1.05x slower                                                   |
| dulwich_log                | 62.0 ms                                                               | 64.9 ms: 1.05x slower                                                   |
| coroutines                 | 29.0 ms                                                               | 30.4 ms: 1.05x slower                                                   |
| thrift                     | 937 us                                                                | 985 us: 1.05x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 3.96 us: 1.05x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.51 us: 1.06x slower                                                   |
| mdp                        | 3.41 sec                                                              | 3.60 sec: 1.06x slower                                                  |
| json_loads                 | 30.7 us                                                               | 32.6 us: 1.06x slower                                                   |
| unpickle                   | 18.5 us                                                               | 19.6 us: 1.06x slower                                                   |
| async_generators           | 491 ms                                                                | 523 ms: 1.07x slower                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.96 ms: 1.07x slower                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 162 ms: 1.08x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.37 sec: 1.09x slower                                                  |
| regex_v8                   | 28.3 ms                                                               | 31.1 ms: 1.10x slower                                                   |
| python_startup             | 11.4 ms                                                               | 12.5 ms: 1.10x slower                                                   |
| pylint                     | 355 ms                                                                | 392 ms: 1.11x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 125 ms: 1.11x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 172 ms: 1.11x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 88.5 ms: 1.12x slower                                                   |
| chameleon                  | 8.81 ms                                                               | 9.96 ms: 1.13x slower                                                   |
| sympy_str                  | 280 ms                                                                | 317 ms: 1.13x slower                                                    |
| coverage                   | 87.3 ms                                                               | 99.1 ms: 1.14x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 14.0 ms: 1.14x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 74.8 ms: 1.15x slower                                                   |
| 2to3                       | 308 ms                                                                | 354 ms: 1.15x slower                                                    |
| sympy_expand               | 454 ms                                                                | 522 ms: 1.15x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 5.15 ms: 1.17x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 102 ms: 1.18x slower                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.84 us: 1.18x slower                                                   |
| comprehensions             | 25.4 us                                                               | 30.0 us: 1.18x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 72.4 ms: 1.18x slower                                                   |
| meteor_contest             | 112 ms                                                                | 132 ms: 1.18x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 149 ms: 1.19x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.54 sec: 1.19x slower                                                  |
| tomli_loads                | 2.59 sec                                                              | 3.08 sec: 1.19x slower                                                  |
| chaos                      | 71.4 ms                                                               | 85.1 ms: 1.19x slower                                                   |
| sqlglot_parse              | 1.46 ms                                                               | 1.75 ms: 1.20x slower                                                   |
| sqlglot_transpile          | 1.83 ms                                                               | 2.21 ms: 1.21x slower                                                   |
| deepcopy                   | 446 us                                                                | 541 us: 1.21x slower                                                    |
| regex_compile              | 137 ms                                                                | 167 ms: 1.21x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 26.3 ms: 1.22x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 8.60 ms: 1.22x slower                                                   |
| django_template            | 40.7 ms                                                               | 49.9 ms: 1.23x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 449 us: 1.23x slower                                                    |
| richards_super             | 58.5 ms                                                               | 71.9 ms: 1.23x slower                                                   |
| float                      | 92.1 ms                                                               | 114 ms: 1.23x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 5.19 ms: 1.26x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 227 us: 1.26x slower                                                    |
| go                         | 157 ms                                                                | 198 ms: 1.26x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.37 sec: 1.26x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 1.16 sec: 1.27x slower                                                  |
| create_gc_cycles           | 1.92 ms                                                               | 2.43 ms: 1.27x slower                                                   |
| mako                       | 12.9 ms                                                               | 16.5 ms: 1.28x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 77.7 ms: 1.28x slower                                                   |
| richards                   | 50.9 ms                                                               | 65.4 ms: 1.28x slower                                                   |
| scimark_fft                | 418 ms                                                                | 537 ms: 1.28x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.98 ms: 1.29x slower                                                   |
| fannkuch                   | 443 ms                                                                | 575 ms: 1.30x slower                                                    |
| pyflate                    | 559 ms                                                                | 726 ms: 1.30x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 130 ms: 1.31x slower                                                    |
| nbody                      | 105 ms                                                                | 138 ms: 1.32x slower                                                    |
| scimark_sor                | 150 ms                                                                | 198 ms: 1.32x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 36.6 ms: 1.34x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 114 ms: 1.34x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 349 us: 1.34x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 207 ms: 1.42x slower                                                    |
| spectral_norm              | 131 ms                                                                | 186 ms: 1.43x slower                                                    |
| deepcopy_memo              | 49.6 us                                                               | 71.6 us: 1.44x slower                                                   |
| logging_silent             | 127 ns                                                                | 188 ns: 1.48x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 10.5 ms: 1.51x slower                                                   |
| telco                      | 8.51 ms                                                               | 166 ms: 19.46x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.16x slower                                                            |

Benchmark hidden because not significant (3): tornado_http, xml_etree_parse, pickle_dict
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240511-3.14.0a0-5b941e5-PYTHON_UOPS/bm-20240511-arminc-aarch64-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json: flaskblogging

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 0.93x