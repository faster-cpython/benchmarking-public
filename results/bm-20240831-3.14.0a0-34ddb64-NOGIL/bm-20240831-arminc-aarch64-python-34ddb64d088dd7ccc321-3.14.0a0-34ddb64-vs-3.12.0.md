# Results vs. 3.12.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-aarch64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.55x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.36x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 518 ms: 1.68x slower                                                    |
| docutils       | 2.98 sec                                                              | 4.08 sec: 1.37x slower                                                  |
| html5lib       | 65.1 ms                                                               | 121 ms: 1.86x slower                                                    |
| tornado_http   | 136 ms                                                                | 208 ms: 1.54x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.60x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 695 ms: 1.07x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 731 ms: 1.06x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.36 sec: 1.04x faster                                                  |
| async_tree_none            | 624 ms                                                                | 606 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 869 ms: 1.02x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.39 sec: 1.02x faster                                                  |
| async_tree_none_tg         | 577 ms                                                                | 570 ms: 1.01x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.03x faster                                                            |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| float          | 92.1 ms                                                               | 206 ms: 2.24x slower                                                    |
| nbody          | 105 ms                                                                | 281 ms: 2.69x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.82x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.46 ms: 1.04x faster                                                   |
| regex_v8       | 28.3 ms                                                               | 33.0 ms: 1.16x slower                                                   |
| regex_compile  | 137 ms                                                                | 257 ms: 1.87x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.20x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 185 ms: 1.05x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 156 ms: 1.04x slower                                                    |
| json_loads           | 30.7 us                                                               | 38.6 us: 1.26x slower                                                   |
| xml_etree_generate   | 112 ms                                                                | 163 ms: 1.45x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 18.2 ms: 1.49x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 4.22 sec: 1.63x slower                                                  |
| xml_etree_process    | 79.0 ms                                                               | 132 ms: 1.67x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 546 us: 2.10x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 773 us: 2.12x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.47x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.3 ms: 1.46x slower                                                   |
| python_startup         | 11.4 ms                                                               | 18.2 ms: 1.60x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.53x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 104 ms: 1.71x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 52.9 ms: 1.93x slower                                                   |
| django_template | 40.7 ms                                                               | 82.7 ms: 2.03x slower                                                   |
| mako            | 12.9 ms                                                               | 28.7 ms: 2.23x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.97x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 4.40 ms                                                               | 3.50 ms: 1.26x faster                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 1.62 ms: 1.18x faster                                                   |
| async_tree_memoization_tg  | 740 ms                                                                | 695 ms: 1.07x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 731 ms: 1.06x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 185 ms: 1.05x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.46 ms: 1.04x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.36 sec: 1.04x faster                                                  |
| async_tree_none            | 624 ms                                                                | 606 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 869 ms: 1.02x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.39 sec: 1.02x faster                                                  |
| async_tree_none_tg         | 577 ms                                                                | 570 ms: 1.01x faster                                                    |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 675 ms: 1.03x slower                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 156 ms: 1.04x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 7.51 ms: 1.07x slower                                                   |
| pathlib                    | 24.5 ms                                                               | 26.4 ms: 1.07x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 33.0 ms: 1.16x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.56 sec: 1.17x slower                                                  |
| asyncio_tcp                | 566 ms                                                                | 673 ms: 1.19x slower                                                    |
| json                       | 5.54 ms                                                               | 6.93 ms: 1.25x slower                                                   |
| deepcopy                   | 446 us                                                                | 557 us: 1.25x slower                                                    |
| json_loads                 | 30.7 us                                                               | 38.6 us: 1.26x slower                                                   |
| mdp                        | 3.41 sec                                                              | 4.33 sec: 1.27x slower                                                  |
| async_generators           | 491 ms                                                                | 652 ms: 1.33x slower                                                    |
| generators                 | 43.5 ms                                                               | 58.4 ms: 1.34x slower                                                   |
| docutils                   | 2.98 sec                                                              | 4.08 sec: 1.37x slower                                                  |
| scimark_fft                | 418 ms                                                                | 576 ms: 1.38x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 40.6 ms: 1.40x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.94 ms: 1.44x slower                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 5.94 us: 1.45x slower                                                   |
| pylint                     | 355 ms                                                                | 514 ms: 1.45x slower                                                    |
| xml_etree_generate         | 112 ms                                                                | 163 ms: 1.45x slower                                                    |
| deepcopy_memo              | 49.6 us                                                               | 72.3 us: 1.46x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 12.3 ms: 1.46x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 18.2 ms: 1.49x slower                                                   |
| telco                      | 8.51 ms                                                               | 12.8 ms: 1.50x slower                                                   |
| meteor_contest             | 112 ms                                                                | 168 ms: 1.50x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 151 ms: 1.52x slower                                                    |
| tornado_http               | 136 ms                                                                | 208 ms: 1.54x slower                                                    |
| coverage                   | 87.3 ms                                                               | 135 ms: 1.54x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 97.1 ms: 1.57x slower                                                   |
| python_startup             | 11.4 ms                                                               | 18.2 ms: 1.60x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 139 ms: 1.60x slower                                                    |
| comprehensions             | 25.4 us                                                               | 40.9 us: 1.61x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 34.8 ms: 1.61x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 2.03 sec: 1.62x slower                                                  |
| tomli_loads                | 2.59 sec                                                              | 4.22 sec: 1.63x slower                                                  |
| bench_thread_pool          | 1.31 ms                                                               | 2.13 ms: 1.63x slower                                                   |
| fannkuch                   | 443 ms                                                                | 736 ms: 1.66x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 132 ms: 1.67x slower                                                    |
| 2to3                       | 308 ms                                                                | 518 ms: 1.68x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 104 ms: 1.71x slower                                                    |
| spectral_norm              | 131 ms                                                                | 231 ms: 1.77x slower                                                    |
| thrift                     | 937 us                                                                | 1.67 ms: 1.78x slower                                                   |
| pyflate                    | 559 ms                                                                | 1.02 sec: 1.83x slower                                                  |
| sympy_str                  | 280 ms                                                                | 516 ms: 1.84x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 234 ms: 1.86x slower                                                    |
| html5lib                   | 65.1 ms                                                               | 121 ms: 1.86x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 337 us: 1.87x slower                                                    |
| regex_compile              | 137 ms                                                                | 257 ms: 1.87x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 116 ms: 1.89x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.76 sec: 1.92x slower                                                  |
| logging_format             | 8.34 us                                                               | 16.1 us: 1.92x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 3.63 sec: 1.93x slower                                                  |
| genshi_text                | 27.4 ms                                                               | 52.9 ms: 1.93x slower                                                   |
| logging_simple             | 7.63 us                                                               | 14.9 us: 1.95x slower                                                   |
| django_template            | 40.7 ms                                                               | 82.7 ms: 2.03x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 174 ms: 2.04x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 317 ms: 2.05x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 546 us: 2.10x slower                                                    |
| sympy_expand               | 454 ms                                                                | 959 ms: 2.11x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 773 us: 2.12x slower                                                    |
| chaos                      | 71.4 ms                                                               | 159 ms: 2.23x slower                                                    |
| mako                       | 12.9 ms                                                               | 28.7 ms: 2.23x slower                                                   |
| float                      | 92.1 ms                                                               | 206 ms: 2.24x slower                                                    |
| logging_silent             | 127 ns                                                                | 287 ns: 2.27x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 15.8 ms: 2.27x slower                                                   |
| scimark_sor                | 150 ms                                                                | 342 ms: 2.29x slower                                                    |
| richards                   | 50.9 ms                                                               | 117 ms: 2.29x slower                                                    |
| raytrace                   | 353 ms                                                                | 812 ms: 2.30x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 4.27 ms: 2.34x slower                                                   |
| richards_super             | 58.5 ms                                                               | 138 ms: 2.35x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 353 ms: 2.43x slower                                                    |
| go                         | 157 ms                                                                | 389 ms: 2.47x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 3.65 ms: 2.49x slower                                                   |
| nbody                      | 105 ms                                                                | 281 ms: 2.69x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 12.8 ms: 3.11x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.55x slower                                                            |

Benchmark hidden because not significant (2): regex_dna, async_tree_cpu_io_mixed
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240831-3.14.0a0-34ddb64-NOGIL/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.44x
- 95% likely to have a slowdown of 1.40x
- 99% likely to have a slowdown of 1.36x

# Memory
- memory change: 1.08x