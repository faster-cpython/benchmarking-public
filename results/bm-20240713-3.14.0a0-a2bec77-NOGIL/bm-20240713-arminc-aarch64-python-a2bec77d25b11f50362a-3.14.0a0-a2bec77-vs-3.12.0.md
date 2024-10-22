# Results vs. 3.12.0

- fork: python
- ref: a2bec77d25b11f50362a
- machine: linux-aarch64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.55x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.38x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 517 ms: 1.68x slower                                                    |
| docutils       | 2.98 sec                                                              | 4.10 sec: 1.38x slower                                                  |
| html5lib       | 65.1 ms                                                               | 121 ms: 1.86x slower                                                    |
| tornado_http   | 136 ms                                                                | 202 ms: 1.49x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.59x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 702 ms: 1.05x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.35 sec: 1.04x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 748 ms: 1.04x faster                                                    |
| async_tree_none            | 624 ms                                                                | 611 ms: 1.02x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 566 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 869 ms: 1.02x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.40 sec: 1.01x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| float          | 92.1 ms                                                               | 210 ms: 2.28x slower                                                    |
| nbody          | 105 ms                                                                | 289 ms: 2.76x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.85x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.30 ms: 1.08x faster                                                   |
| regex_dna      | 254 ms                                                                | 245 ms: 1.04x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 32.5 ms: 1.15x slower                                                   |
| regex_compile  | 137 ms                                                                | 256 ms: 1.86x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.18x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 182 ms: 1.07x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 156 ms: 1.04x slower                                                    |
| json_loads           | 30.7 us                                                               | 38.7 us: 1.26x slower                                                   |
| xml_etree_generate   | 112 ms                                                                | 160 ms: 1.43x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 17.6 ms: 1.44x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 4.20 sec: 1.62x slower                                                  |
| xml_etree_process    | 79.0 ms                                                               | 129 ms: 1.64x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 542 us: 2.08x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 774 us: 2.12x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.46x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 11.7 ms: 1.40x slower                                                   |
| python_startup         | 11.4 ms                                                               | 17.6 ms: 1.55x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.47x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 104 ms: 1.71x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 53.2 ms: 1.94x slower                                                   |
| django_template | 40.7 ms                                                               | 83.2 ms: 2.05x slower                                                   |
| mako            | 12.9 ms                                                               | 28.8 ms: 2.23x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.97x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 4.40 ms                                                               | 3.42 ms: 1.28x faster                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 1.58 ms: 1.21x faster                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 6.25 ms: 1.13x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.30 ms: 1.08x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 182 ms: 1.07x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 702 ms: 1.05x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.35 sec: 1.04x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 748 ms: 1.04x faster                                                    |
| regex_dna                  | 254 ms                                                                | 245 ms: 1.04x faster                                                    |
| async_tree_none            | 624 ms                                                                | 611 ms: 1.02x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 566 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 869 ms: 1.02x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.40 sec: 1.01x faster                                                  |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 671 ms: 1.02x slower                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 156 ms: 1.04x slower                                                    |
| pathlib                    | 24.5 ms                                                               | 26.3 ms: 1.07x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.47 sec: 1.13x slower                                                  |
| regex_v8                   | 28.3 ms                                                               | 32.5 ms: 1.15x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 684 ms: 1.21x slower                                                    |
| deepcopy                   | 446 us                                                                | 559 us: 1.26x slower                                                    |
| json_loads                 | 30.7 us                                                               | 38.7 us: 1.26x slower                                                   |
| json                       | 5.54 ms                                                               | 7.01 ms: 1.26x slower                                                   |
| mdp                        | 3.41 sec                                                              | 4.37 sec: 1.28x slower                                                  |
| generators                 | 43.5 ms                                                               | 58.4 ms: 1.34x slower                                                   |
| coroutines                 | 29.0 ms                                                               | 39.2 ms: 1.35x slower                                                   |
| docutils                   | 2.98 sec                                                              | 4.10 sec: 1.38x slower                                                  |
| async_generators           | 491 ms                                                                | 678 ms: 1.38x slower                                                    |
| telco                      | 8.51 ms                                                               | 11.8 ms: 1.39x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 11.7 ms: 1.40x slower                                                   |
| pylint                     | 355 ms                                                                | 504 ms: 1.42x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 160 ms: 1.43x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 17.6 ms: 1.44x slower                                                   |
| scimark_fft                | 418 ms                                                                | 601 ms: 1.44x slower                                                    |
| deepcopy_memo              | 49.6 us                                                               | 72.0 us: 1.45x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.91 ms: 1.46x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 9.05 ms: 1.46x slower                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 6.02 us: 1.47x slower                                                   |
| tornado_http               | 136 ms                                                                | 202 ms: 1.49x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 151 ms: 1.52x slower                                                    |
| coverage                   | 87.3 ms                                                               | 134 ms: 1.53x slower                                                    |
| meteor_contest             | 112 ms                                                                | 174 ms: 1.55x slower                                                    |
| python_startup             | 11.4 ms                                                               | 17.6 ms: 1.55x slower                                                   |
| dulwich_log                | 62.0 ms                                                               | 97.3 ms: 1.57x slower                                                   |
| comprehensions             | 25.4 us                                                               | 40.7 us: 1.60x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 140 ms: 1.61x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 35.0 ms: 1.62x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 4.20 sec: 1.62x slower                                                  |
| xml_etree_process          | 79.0 ms                                                               | 129 ms: 1.64x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 2.06 sec: 1.64x slower                                                  |
| 2to3                       | 308 ms                                                                | 517 ms: 1.68x slower                                                    |
| fannkuch                   | 443 ms                                                                | 750 ms: 1.69x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 104 ms: 1.71x slower                                                    |
| thrift                     | 937 us                                                                | 1.67 ms: 1.78x slower                                                   |
| spectral_norm              | 131 ms                                                                | 237 ms: 1.81x slower                                                    |
| pyflate                    | 559 ms                                                                | 1.02 sec: 1.82x slower                                                  |
| sqlglot_normalize          | 126 ms                                                                | 230 ms: 1.83x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 331 us: 1.83x slower                                                    |
| sympy_str                  | 280 ms                                                                | 519 ms: 1.85x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 121 ms: 1.86x slower                                                    |
| regex_compile              | 137 ms                                                                | 256 ms: 1.86x slower                                                    |
| logging_format             | 8.34 us                                                               | 15.6 us: 1.87x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 116 ms: 1.89x slower                                                    |
| logging_simple             | 7.63 us                                                               | 14.6 us: 1.91x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 3.64 sec: 1.93x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 1.77 sec: 1.94x slower                                                  |
| genshi_text                | 27.4 ms                                                               | 53.2 ms: 1.94x slower                                                   |
| django_template            | 40.7 ms                                                               | 83.2 ms: 2.05x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 318 ms: 2.06x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 175 ms: 2.06x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 542 us: 2.08x slower                                                    |
| sympy_expand               | 454 ms                                                                | 956 ms: 2.11x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 774 us: 2.12x slower                                                    |
| mako                       | 12.9 ms                                                               | 28.8 ms: 2.23x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 15.6 ms: 2.24x slower                                                   |
| chaos                      | 71.4 ms                                                               | 161 ms: 2.26x slower                                                    |
| logging_silent             | 127 ns                                                                | 287 ns: 2.26x slower                                                    |
| float                      | 92.1 ms                                                               | 210 ms: 2.28x slower                                                    |
| scimark_sor                | 150 ms                                                                | 343 ms: 2.29x slower                                                    |
| raytrace                   | 353 ms                                                                | 825 ms: 2.34x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 4.38 ms: 2.40x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 355 ms: 2.44x slower                                                    |
| richards_super             | 58.5 ms                                                               | 145 ms: 2.49x slower                                                    |
| richards                   | 50.9 ms                                                               | 127 ms: 2.50x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 3.78 ms: 2.58x slower                                                   |
| nbody                      | 105 ms                                                                | 289 ms: 2.76x slower                                                    |
| go                         | 157 ms                                                                | 448 ms: 2.85x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 12.9 ms: 3.13x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.55x slower                                                            |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240713-3.14.0a0-a2bec77-NOGIL/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.47x
- 95% likely to have a slowdown of 1.44x
- 99% likely to have a slowdown of 1.38x

# Memory
- memory change: 1.07x