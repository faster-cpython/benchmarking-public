# Results vs. 3.12.0

- fork: python
- ref: e83ce850f433fd8bbf8f
- machine: linux-aarch64
- commit hash: e83ce85
- commit date: 2024-06-05
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 356 ms: 1.16x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.50 sec: 1.17x slower                                                  |
| html5lib       | 65.1 ms                                                               | 72.2 ms: 1.11x slower                                                   |
| tornado_http   | 136 ms                                                                | 138 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 504 ms: 1.24x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 607 ms: 1.22x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 478 ms: 1.21x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 663 ms: 1.17x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 771 ms: 1.15x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 811 ms: 1.12x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.25 sec: 1.12x faster                                                  |
| async_tree_io_tg           | 1.40 sec                                                              | 1.27 sec: 1.10x faster                                                  |
| Geometric mean             | (ref)                                                                 | 1.17x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 90.4 ms: 1.02x faster                                                   |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| nbody          | 105 ms                                                                | 115 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 250 ms: 1.01x faster                                                    |
| regex_effbot   | 4.64 ms                                                               | 4.87 ms: 1.05x slower                                                   |
| regex_v8       | 28.3 ms                                                               | 30.1 ms: 1.06x slower                                                   |
| regex_compile  | 137 ms                                                                | 175 ms: 1.27x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.09x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 189 ms: 1.03x faster                                                    |
| xml_etree_iterparse  | 150 ms                                                                | 149 ms: 1.01x faster                                                    |
| pickle_list          | 5.25 us                                                               | 5.27 us: 1.00x slower                                                   |
| xml_etree_process    | 79.0 ms                                                               | 79.7 ms: 1.01x slower                                                   |
| pickle_dict          | 37.3 us                                                               | 37.8 us: 1.01x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                  |
| pickle               | 13.4 us                                                               | 13.7 us: 1.02x slower                                                   |
| xml_etree_generate   | 112 ms                                                                | 115 ms: 1.03x slower                                                    |
| json_loads           | 30.7 us                                                               | 32.1 us: 1.05x slower                                                   |
| unpickle             | 18.5 us                                                               | 19.4 us: 1.05x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 277 us: 1.07x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 13.1 ms: 1.07x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 6.63 us: 1.07x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 413 us: 1.13x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 11.0 ms: 1.32x slower                                                   |
| python_startup         | 11.4 ms                                                               | 15.2 ms: 1.33x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.33x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.0 ms: 1.01x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 33.8 ms: 1.23x slower                                                   |
| django_template | 40.7 ms                                                               | 51.2 ms: 1.26x slower                                                   |
| genshi_xml      | 60.6 ms                                                               | 83.0 ms: 1.37x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.21x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 504 ms: 1.24x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 607 ms: 1.22x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 478 ms: 1.21x faster                                                    |
| async_tree_memoization     | 777 ms                                                                | 663 ms: 1.17x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 771 ms: 1.15x faster                                                    |
| generators                 | 43.5 ms                                                               | 38.6 ms: 1.13x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 811 ms: 1.12x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.25 sec: 1.12x faster                                                  |
| pathlib                    | 24.5 ms                                                               | 21.9 ms: 1.12x faster                                                   |
| async_tree_io_tg           | 1.40 sec                                                              | 1.27 sec: 1.10x faster                                                  |
| comprehensions             | 25.4 us                                                               | 23.4 us: 1.08x faster                                                   |
| raytrace                   | 353 ms                                                                | 326 ms: 1.08x faster                                                    |
| logging_simple             | 7.63 us                                                               | 7.38 us: 1.03x faster                                                   |
| xml_etree_parse            | 195 ms                                                                | 189 ms: 1.03x faster                                                    |
| logging_format             | 8.34 us                                                               | 8.09 us: 1.03x faster                                                   |
| float                      | 92.1 ms                                                               | 90.4 ms: 1.02x faster                                                   |
| regex_dna                  | 254 ms                                                                | 250 ms: 1.01x faster                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 149 ms: 1.01x faster                                                    |
| pickle_list                | 5.25 us                                                               | 5.27 us: 1.00x slower                                                   |
| mako                       | 12.9 ms                                                               | 13.0 ms: 1.01x slower                                                   |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 79.7 ms: 1.01x slower                                                   |
| pickle_dict                | 37.3 us                                                               | 37.8 us: 1.01x slower                                                   |
| tornado_http               | 136 ms                                                                | 138 ms: 1.02x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.64 sec: 1.02x slower                                                  |
| pickle                     | 13.4 us                                                               | 13.7 us: 1.02x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.23 sec: 1.02x slower                                                  |
| bench_thread_pool          | 1.31 ms                                                               | 1.34 ms: 1.02x slower                                                   |
| xml_etree_generate         | 112 ms                                                                | 115 ms: 1.03x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 89.1 ms: 1.03x slower                                                   |
| thrift                     | 937 us                                                                | 964 us: 1.03x slower                                                    |
| json                       | 5.54 ms                                                               | 5.71 ms: 1.03x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 3.90 us: 1.03x slower                                                   |
| meteor_contest             | 112 ms                                                                | 117 ms: 1.05x slower                                                    |
| json_loads                 | 30.7 us                                                               | 32.1 us: 1.05x slower                                                   |
| unpickle                   | 18.5 us                                                               | 19.4 us: 1.05x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.87 ms: 1.05x slower                                                   |
| async_generators           | 491 ms                                                                | 516 ms: 1.05x slower                                                    |
| dask                       | 376 ms                                                                | 397 ms: 1.05x slower                                                    |
| fannkuch                   | 443 ms                                                                | 468 ms: 1.05x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.1 ms: 1.06x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 277 us: 1.07x slower                                                    |
| richards_super             | 58.5 ms                                                               | 62.4 ms: 1.07x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 13.1 ms: 1.07x slower                                                   |
| scimark_monte_carlo        | 85.1 ms                                                               | 91.3 ms: 1.07x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.63 us: 1.07x slower                                                   |
| pyflate                    | 559 ms                                                                | 603 ms: 1.08x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.36 sec: 1.08x slower                                                  |
| asyncio_tcp                | 566 ms                                                                | 614 ms: 1.08x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.59 ms: 1.09x slower                                                   |
| logging_silent             | 127 ns                                                                | 138 ns: 1.09x slower                                                    |
| scimark_fft                | 418 ms                                                                | 459 ms: 1.10x slower                                                    |
| nbody                      | 105 ms                                                                | 115 ms: 1.10x slower                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 2.02 ms: 1.11x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 72.2 ms: 1.11x slower                                                   |
| deepcopy                   | 446 us                                                                | 494 us: 1.11x slower                                                    |
| richards                   | 50.9 ms                                                               | 56.7 ms: 1.11x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.90 ms: 1.11x slower                                                   |
| deltablue                  | 4.12 ms                                                               | 4.60 ms: 1.12x slower                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 4.61 us: 1.13x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 413 us: 1.13x slower                                                    |
| go                         | 157 ms                                                                | 179 ms: 1.14x slower                                                    |
| sqlglot_normalize          | 126 ms                                                                | 144 ms: 1.14x slower                                                    |
| spectral_norm              | 131 ms                                                                | 149 ms: 1.14x slower                                                    |
| sqlglot_optimize           | 61.3 ms                                                               | 70.0 ms: 1.14x slower                                                   |
| coverage                   | 87.3 ms                                                               | 100 ms: 1.15x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 207 us: 1.15x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 71.2 ms: 1.15x slower                                                   |
| pylint                     | 355 ms                                                                | 408 ms: 1.15x slower                                                    |
| sympy_str                  | 280 ms                                                                | 322 ms: 1.15x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 5.07 ms: 1.15x slower                                                   |
| 2to3                       | 308 ms                                                                | 356 ms: 1.16x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 8.23 ms: 1.17x slower                                                   |
| scimark_sor                | 150 ms                                                                | 175 ms: 1.17x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.50 sec: 1.17x slower                                                  |
| sympy_integrate            | 21.6 ms                                                               | 25.8 ms: 1.19x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 118 ms: 1.19x slower                                                    |
| sympy_expand               | 454 ms                                                                | 546 ms: 1.20x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 187 ms: 1.21x slower                                                    |
| telco                      | 8.51 ms                                                               | 10.4 ms: 1.22x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.12 sec: 1.22x slower                                                  |
| create_gc_cycles           | 1.92 ms                                                               | 2.35 ms: 1.23x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 33.8 ms: 1.23x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.32 sec: 1.23x slower                                                  |
| django_template            | 40.7 ms                                                               | 51.2 ms: 1.26x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 184 ms: 1.26x slower                                                    |
| chaos                      | 71.4 ms                                                               | 90.4 ms: 1.27x slower                                                   |
| regex_compile              | 137 ms                                                                | 175 ms: 1.27x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 8.99 ms: 1.29x slower                                                   |
| python_startup_no_site     | 8.37 ms                                                               | 11.0 ms: 1.32x slower                                                   |
| python_startup             | 11.4 ms                                                               | 15.2 ms: 1.33x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 83.0 ms: 1.37x slower                                                   |
| Geometric mean             | (ref)                                                                 | 1.07x slower                                                            |

Benchmark hidden because not significant (4): coroutines, mdp, asyncio_websockets, deepcopy_memo
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.00x