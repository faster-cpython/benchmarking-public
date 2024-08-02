# Results vs. 3.12.0

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: linux-aarch64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 365 ms: 1.19x slower                                                     |
| chameleon      | 8.81 ms                                                               | 9.29 ms: 1.05x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.62 sec: 1.21x slower                                                   |
| html5lib       | 65.1 ms                                                               | 71.7 ms: 1.10x slower                                                    |
| tornado_http   | 136 ms                                                                | 150 ms: 1.10x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.13x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 504 ms: 1.24x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 623 ms: 1.19x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 489 ms: 1.18x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 666 ms: 1.17x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.23 sec: 1.14x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.25 sec: 1.13x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 817 ms: 1.12x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 801 ms: 1.10x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.16x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 89.2 ms: 1.03x faster                                                    |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 260 ms: 1.02x slower                                                     |
| regex_effbot   | 4.64 ms                                                               | 4.94 ms: 1.07x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                    |
| regex_compile  | 137 ms                                                                | 176 ms: 1.28x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 190 ms: 1.03x faster                                                     |
| tomli_loads          | 2.59 sec                                                              | 2.62 sec: 1.01x slower                                                   |
| pickle_dict          | 37.3 us                                                               | 37.8 us: 1.01x slower                                                    |
| pickle               | 13.4 us                                                               | 13.6 us: 1.01x slower                                                    |
| json_loads           | 30.7 us                                                               | 32.0 us: 1.04x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 117 ms: 1.04x slower                                                     |
| xml_etree_process    | 79.0 ms                                                               | 83.1 ms: 1.05x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 277 us: 1.07x slower                                                     |
| json_dumps           | 12.3 ms                                                               | 13.2 ms: 1.07x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 6.63 us: 1.07x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 396 us: 1.08x slower                                                     |
| unpickle             | 18.5 us                                                               | 20.0 us: 1.09x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 11.2 ms: 1.34x slower                                                    |
| python_startup         | 11.4 ms                                                               | 15.9 ms: 1.40x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.37x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 49.8 ms: 1.23x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 34.3 ms: 1.25x slower                                                    |
| genshi_xml      | 60.6 ms                                                               | 83.0 ms: 1.37x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.20x slower                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 504 ms: 1.24x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 623 ms: 1.19x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 489 ms: 1.18x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 666 ms: 1.17x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 1.23 sec: 1.14x faster                                                   |
| async_tree_io              | 1.41 sec                                                              | 1.25 sec: 1.13x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 817 ms: 1.12x faster                                                     |
| raytrace                   | 353 ms                                                                | 318 ms: 1.11x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 801 ms: 1.10x faster                                                     |
| generators                 | 43.5 ms                                                               | 39.5 ms: 1.10x faster                                                    |
| comprehensions             | 25.4 us                                                               | 23.1 us: 1.10x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 23.3 ms: 1.05x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.27 us: 1.05x faster                                                    |
| logging_format             | 8.34 us                                                               | 8.02 us: 1.04x faster                                                    |
| float                      | 92.1 ms                                                               | 89.2 ms: 1.03x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 190 ms: 1.03x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 49.4 us: 1.00x faster                                                    |
| asyncio_websockets         | 658 ms                                                                | 661 ms: 1.01x slower                                                     |
| mdp                        | 3.41 sec                                                              | 3.44 sec: 1.01x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.62 sec: 1.01x slower                                                   |
| pickle_dict                | 37.3 us                                                               | 37.8 us: 1.01x slower                                                    |
| pickle                     | 13.4 us                                                               | 13.6 us: 1.01x slower                                                    |
| regex_dna                  | 254 ms                                                                | 260 ms: 1.02x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 3.87 us: 1.03x slower                                                    |
| json                       | 5.54 ms                                                               | 5.71 ms: 1.03x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.35 ms: 1.03x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 88.1 ms: 1.04x slower                                                    |
| thrift                     | 937 us                                                                | 971 us: 1.04x slower                                                     |
| async_generators           | 491 ms                                                                | 509 ms: 1.04x slower                                                     |
| json_loads                 | 30.7 us                                                               | 32.0 us: 1.04x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 117 ms: 1.04x slower                                                     |
| meteor_contest             | 112 ms                                                                | 117 ms: 1.04x slower                                                     |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.28 sec: 1.04x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 83.1 ms: 1.05x slower                                                    |
| chameleon                  | 8.81 ms                                                               | 9.29 ms: 1.05x slower                                                    |
| fannkuch                   | 443 ms                                                                | 469 ms: 1.06x slower                                                     |
| regex_effbot               | 4.64 ms                                                               | 4.94 ms: 1.07x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 277 us: 1.07x slower                                                     |
| dask                       | 376 ms                                                                | 403 ms: 1.07x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.34 sec: 1.07x slower                                                   |
| pyflate                    | 559 ms                                                                | 599 ms: 1.07x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 13.2 ms: 1.07x slower                                                    |
| mypy2                      | 873 ms                                                                | 938 ms: 1.07x slower                                                     |
| unpickle_list              | 6.17 us                                                               | 6.63 us: 1.07x slower                                                    |
| richards_super             | 58.5 ms                                                               | 63.0 ms: 1.08x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 396 us: 1.08x slower                                                     |
| unpickle                   | 18.5 us                                                               | 20.0 us: 1.09x slower                                                    |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                                     |
| sqlglot_parse              | 1.46 ms                                                               | 1.60 ms: 1.09x slower                                                    |
| logging_silent             | 127 ns                                                                | 138 ns: 1.09x slower                                                     |
| sqlglot_transpile          | 1.83 ms                                                               | 2.00 ms: 1.10x slower                                                    |
| scimark_fft                | 418 ms                                                                | 460 ms: 1.10x slower                                                     |
| html5lib                   | 65.1 ms                                                               | 71.7 ms: 1.10x slower                                                    |
| tornado_http               | 136 ms                                                                | 150 ms: 1.10x slower                                                     |
| richards                   | 50.9 ms                                                               | 56.5 ms: 1.11x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 4.58 ms: 1.11x slower                                                    |
| spectral_norm              | 131 ms                                                                | 146 ms: 1.11x slower                                                     |
| deepcopy                   | 446 us                                                                | 497 us: 1.12x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.95 ms: 1.12x slower                                                    |
| coverage                   | 87.3 ms                                                               | 98.4 ms: 1.13x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 142 ms: 1.13x slower                                                     |
| sqlglot_optimize           | 61.3 ms                                                               | 69.3 ms: 1.13x slower                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.64 us: 1.13x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 645 ms: 1.14x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 207 us: 1.15x slower                                                     |
| go                         | 157 ms                                                                | 180 ms: 1.15x slower                                                     |
| scimark_sor                | 150 ms                                                                | 173 ms: 1.16x slower                                                     |
| aiohttp                    | 1.16 ms                                                               | 1.35 ms: 1.16x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 116 ms: 1.16x slower                                                     |
| pylint                     | 355 ms                                                                | 417 ms: 1.17x slower                                                     |
| gc_traversal               | 4.40 ms                                                               | 5.19 ms: 1.18x slower                                                    |
| 2to3                       | 308 ms                                                                | 365 ms: 1.19x slower                                                     |
| sympy_str                  | 280 ms                                                                | 332 ms: 1.19x slower                                                     |
| bench_mp_pool              | 7.05 ms                                                               | 8.50 ms: 1.20x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.10 sec: 1.21x slower                                                   |
| chaos                      | 71.4 ms                                                               | 86.1 ms: 1.21x slower                                                    |
| gunicorn                   | 1.14 ms                                                               | 1.37 ms: 1.21x slower                                                    |
| telco                      | 8.51 ms                                                               | 10.3 ms: 1.21x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.62 sec: 1.21x slower                                                   |
| django_template            | 40.7 ms                                                               | 49.8 ms: 1.23x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 2.32 sec: 1.23x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 26.7 ms: 1.23x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 191 ms: 1.24x slower                                                     |
| sympy_expand               | 454 ms                                                                | 561 ms: 1.24x slower                                                     |
| dulwich_log                | 62.0 ms                                                               | 77.4 ms: 1.25x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 34.3 ms: 1.25x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 183 ms: 1.26x slower                                                     |
| create_gc_cycles           | 1.92 ms                                                               | 2.42 ms: 1.26x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 8.91 ms: 1.28x slower                                                    |
| regex_compile              | 137 ms                                                                | 176 ms: 1.28x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 11.2 ms: 1.34x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 83.0 ms: 1.37x slower                                                    |
| python_startup             | 11.4 ms                                                               | 15.9 ms: 1.40x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.08x slower                                                             |

Benchmark hidden because not significant (6): xml_etree_iterparse, mako, coroutines, crypto_pyaes, pidigits, pickle_list
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240604-3.13.0b1+-6725c78-JIT/bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json: flaskblogging

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.01x