# Results vs. 3.12.0

- fork: brandtbucher
- ref: main
- machine: linux-aarch64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 380 ms: 1.23x slower                                          |
| docutils       | 2.98 sec                                                              | 4.02 sec: 1.35x slower                                        |
| html5lib       | 65.1 ms                                                               | 72.5 ms: 1.12x slower                                         |
| tornado_http   | 136 ms                                                                | 150 ms: 1.11x slower                                          |
| Geometric mean | (ref)                                                                 | 1.20x slower                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 445 ms: 1.40x faster                                          |
| async_tree_none_tg         | 577 ms                                                                | 432 ms: 1.33x faster                                          |
| async_tree_memoization     | 777 ms                                                                | 588 ms: 1.32x faster                                          |
| async_tree_memoization_tg  | 740 ms                                                                | 568 ms: 1.30x faster                                          |
| async_tree_io              | 1.41 sec                                                              | 1.14 sec: 1.23x faster                                        |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 754 ms: 1.21x faster                                          |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 737 ms: 1.20x faster                                          |
| async_tree_io_tg           | 1.40 sec                                                              | 1.19 sec: 1.18x faster                                        |
| Geometric mean             | (ref)                                                                 | 1.27x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 88.5 ms: 1.04x faster                                         |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                          |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                          |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 255 ms: 1.01x slower                                          |
| regex_effbot   | 4.64 ms                                                               | 4.96 ms: 1.07x slower                                         |
| regex_v8       | 28.3 ms                                                               | 30.5 ms: 1.08x slower                                         |
| regex_compile  | 137 ms                                                                | 197 ms: 1.44x slower                                          |
| Geometric mean | (ref)                                                                 | 1.14x slower                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 187 ms: 1.04x faster                                          |
| xml_etree_generate   | 112 ms                                                                | 110 ms: 1.02x faster                                          |
| xml_etree_iterparse  | 150 ms                                                                | 148 ms: 1.02x faster                                          |
| tomli_loads          | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                        |
| pickle_dict          | 37.3 us                                                               | 38.2 us: 1.02x slower                                         |
| unpickle_pure_python | 260 us                                                                | 266 us: 1.02x slower                                          |
| xml_etree_process    | 79.0 ms                                                               | 81.1 ms: 1.03x slower                                         |
| pickle               | 13.4 us                                                               | 13.8 us: 1.03x slower                                         |
| unpickle_list        | 6.17 us                                                               | 6.37 us: 1.03x slower                                         |
| json_loads           | 30.7 us                                                               | 31.7 us: 1.03x slower                                         |
| unpickle             | 18.5 us                                                               | 19.5 us: 1.05x slower                                         |
| pickle_pure_python   | 365 us                                                                | 399 us: 1.09x slower                                          |
| json_dumps           | 12.3 ms                                                               | 13.4 ms: 1.10x slower                                         |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                  |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.69 ms: 1.04x slower                                         |
| python_startup         | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                         |
| Geometric mean         | (ref)                                                                 | 1.09x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.1 ms: 1.01x slower                                         |
| django_template | 40.7 ms                                                               | 51.0 ms: 1.25x slower                                         |
| genshi_text     | 27.4 ms                                                               | 34.6 ms: 1.26x slower                                         |
| genshi_xml      | 60.6 ms                                                               | 80.5 ms: 1.33x slower                                         |
| Geometric mean  | (ref)                                                                 | 1.21x slower                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 445 ms: 1.40x faster                                          |
| async_tree_none_tg         | 577 ms                                                                | 432 ms: 1.33x faster                                          |
| deepcopy_memo              | 49.6 us                                                               | 37.5 us: 1.32x faster                                         |
| async_tree_memoization     | 777 ms                                                                | 588 ms: 1.32x faster                                          |
| async_tree_memoization_tg  | 740 ms                                                                | 568 ms: 1.30x faster                                          |
| async_tree_io              | 1.41 sec                                                              | 1.14 sec: 1.23x faster                                        |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 754 ms: 1.21x faster                                          |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 737 ms: 1.20x faster                                          |
| async_tree_io_tg           | 1.40 sec                                                              | 1.19 sec: 1.18x faster                                        |
| pathlib                    | 24.5 ms                                                               | 21.8 ms: 1.12x faster                                         |
| deepcopy                   | 446 us                                                                | 398 us: 1.12x faster                                          |
| deepcopy_reduce            | 4.10 us                                                               | 3.90 us: 1.05x faster                                         |
| xml_etree_parse            | 195 ms                                                                | 187 ms: 1.04x faster                                          |
| comprehensions             | 25.4 us                                                               | 24.3 us: 1.04x faster                                         |
| float                      | 92.1 ms                                                               | 88.5 ms: 1.04x faster                                         |
| logging_format             | 8.34 us                                                               | 8.16 us: 1.02x faster                                         |
| coroutines                 | 29.0 ms                                                               | 28.4 ms: 1.02x faster                                         |
| xml_etree_generate         | 112 ms                                                                | 110 ms: 1.02x faster                                          |
| logging_simple             | 7.63 us                                                               | 7.49 us: 1.02x faster                                         |
| xml_etree_iterparse        | 150 ms                                                                | 148 ms: 1.02x faster                                          |
| raytrace                   | 353 ms                                                                | 347 ms: 1.02x faster                                          |
| regex_dna                  | 254 ms                                                                | 255 ms: 1.01x slower                                          |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                          |
| asyncio_websockets         | 658 ms                                                                | 663 ms: 1.01x slower                                          |
| scimark_sor                | 150 ms                                                                | 151 ms: 1.01x slower                                          |
| tomli_loads                | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                        |
| mako                       | 12.9 ms                                                               | 13.1 ms: 1.01x slower                                         |
| thrift                     | 937 us                                                                | 953 us: 1.02x slower                                          |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.22 sec: 1.02x slower                                        |
| pickle_dict                | 37.3 us                                                               | 38.2 us: 1.02x slower                                         |
| unpickle_pure_python       | 260 us                                                                | 266 us: 1.02x slower                                          |
| mdp                        | 3.41 sec                                                              | 3.49 sec: 1.02x slower                                        |
| json                       | 5.54 ms                                                               | 5.68 ms: 1.03x slower                                         |
| scimark_lu                 | 146 ms                                                                | 149 ms: 1.03x slower                                          |
| xml_etree_process          | 79.0 ms                                                               | 81.1 ms: 1.03x slower                                         |
| pickle                     | 13.4 us                                                               | 13.8 us: 1.03x slower                                         |
| sqlite_synth               | 3.77 us                                                               | 3.89 us: 1.03x slower                                         |
| unpickle_list              | 6.17 us                                                               | 6.37 us: 1.03x slower                                         |
| async_generators           | 491 ms                                                                | 507 ms: 1.03x slower                                          |
| json_loads                 | 30.7 us                                                               | 31.7 us: 1.03x slower                                         |
| crypto_pyaes               | 86.6 ms                                                               | 89.9 ms: 1.04x slower                                         |
| python_startup_no_site     | 8.37 ms                                                               | 8.69 ms: 1.04x slower                                         |
| bench_thread_pool          | 1.31 ms                                                               | 1.36 ms: 1.04x slower                                         |
| bench_mp_pool              | 7.05 ms                                                               | 7.35 ms: 1.04x slower                                         |
| unpickle                   | 18.5 us                                                               | 19.5 us: 1.05x slower                                         |
| deltablue                  | 4.12 ms                                                               | 4.36 ms: 1.06x slower                                         |
| regex_effbot               | 4.64 ms                                                               | 4.96 ms: 1.07x slower                                         |
| logging_silent             | 127 ns                                                                | 136 ns: 1.08x slower                                          |
| regex_v8                   | 28.3 ms                                                               | 30.5 ms: 1.08x slower                                         |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                          |
| pickle_pure_python         | 365 us                                                                | 399 us: 1.09x slower                                          |
| scimark_monte_carlo        | 85.1 ms                                                               | 93.0 ms: 1.09x slower                                         |
| json_dumps                 | 12.3 ms                                                               | 13.4 ms: 1.10x slower                                         |
| scimark_fft                | 418 ms                                                                | 459 ms: 1.10x slower                                          |
| asyncio_tcp                | 566 ms                                                                | 623 ms: 1.10x slower                                          |
| meteor_contest             | 112 ms                                                                | 124 ms: 1.11x slower                                          |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.86 ms: 1.11x slower                                         |
| tornado_http               | 136 ms                                                                | 150 ms: 1.11x slower                                          |
| html5lib                   | 65.1 ms                                                               | 72.5 ms: 1.12x slower                                         |
| spectral_norm              | 131 ms                                                                | 146 ms: 1.12x slower                                          |
| pyflate                    | 559 ms                                                                | 628 ms: 1.12x slower                                          |
| fannkuch                   | 443 ms                                                                | 510 ms: 1.15x slower                                          |
| python_startup             | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                         |
| gc_traversal               | 4.40 ms                                                               | 5.12 ms: 1.17x slower                                         |
| coverage                   | 87.3 ms                                                               | 103 ms: 1.18x slower                                          |
| go                         | 157 ms                                                                | 186 ms: 1.18x slower                                          |
| typing_runtime_protocols   | 181 us                                                                | 215 us: 1.19x slower                                          |
| sqlglot_parse              | 1.46 ms                                                               | 1.75 ms: 1.19x slower                                         |
| pycparser                  | 1.26 sec                                                              | 1.51 sec: 1.20x slower                                        |
| sqlglot_transpile          | 1.83 ms                                                               | 2.21 ms: 1.21x slower                                         |
| create_gc_cycles           | 1.92 ms                                                               | 2.33 ms: 1.22x slower                                         |
| sqlglot_normalize          | 126 ms                                                                | 154 ms: 1.22x slower                                          |
| 2to3                       | 308 ms                                                                | 380 ms: 1.23x slower                                          |
| django_template            | 40.7 ms                                                               | 51.0 ms: 1.25x slower                                         |
| genshi_text                | 27.4 ms                                                               | 34.6 ms: 1.26x slower                                         |
| telco                      | 8.51 ms                                                               | 10.7 ms: 1.26x slower                                         |
| chaos                      | 71.4 ms                                                               | 90.8 ms: 1.27x slower                                         |
| nqueens                    | 99.2 ms                                                               | 127 ms: 1.28x slower                                          |
| sqlglot_optimize           | 61.3 ms                                                               | 79.1 ms: 1.29x slower                                         |
| generators                 | 43.5 ms                                                               | 56.5 ms: 1.30x slower                                         |
| richards_super             | 58.5 ms                                                               | 76.3 ms: 1.31x slower                                         |
| dulwich_log                | 62.0 ms                                                               | 81.1 ms: 1.31x slower                                         |
| richards                   | 50.9 ms                                                               | 66.6 ms: 1.31x slower                                         |
| sympy_str                  | 280 ms                                                                | 366 ms: 1.31x slower                                          |
| sympy_integrate            | 21.6 ms                                                               | 28.4 ms: 1.31x slower                                         |
| genshi_xml                 | 60.6 ms                                                               | 80.5 ms: 1.33x slower                                         |
| pylint                     | 355 ms                                                                | 476 ms: 1.34x slower                                          |
| docutils                   | 2.98 sec                                                              | 4.02 sec: 1.35x slower                                        |
| sympy_expand               | 454 ms                                                                | 613 ms: 1.35x slower                                          |
| sympy_sum                  | 154 ms                                                                | 209 ms: 1.35x slower                                          |
| pprint_safe_repr           | 916 ms                                                                | 1.26 sec: 1.37x slower                                        |
| pprint_pformat             | 1.88 sec                                                              | 2.61 sec: 1.39x slower                                        |
| regex_compile              | 137 ms                                                                | 197 ms: 1.44x slower                                          |
| hexiom                     | 6.98 ms                                                               | 10.2 ms: 1.47x slower                                         |
| Geometric mean             | (ref)                                                                 | 1.08x slower                                                  |

Benchmark hidden because not significant (1): pickle_list
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240924-3.14.0a0-e256a75-JIT/bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75.json: bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.01x