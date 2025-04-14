# Results vs. 3.12.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-aarch64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.121x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 388 ms: 1.26x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.39 sec: 1.13x slower                                                   |
| html5lib       | 65.1 ms                                                               | 80.6 ms: 1.24x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.21x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 914 ms: 1.54x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 500 ms: 1.48x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 955 ms: 1.48x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 539 ms: 1.44x faster                                                     |
| async_tree_none            | 624 ms                                                                | 444 ms: 1.40x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 414 ms: 1.39x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 716 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 695 ms: 1.27x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.41x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 246 ms: 1.06x slower                                                     |
| float          | 92.1 ms                                                               | 102 ms: 1.11x slower                                                     |
| nbody          | 105 ms                                                                | 183 ms: 1.75x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.27x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.07 ms: 1.14x faster                                                    |
| regex_dna      | 254 ms                                                                | 267 ms: 1.05x slower                                                     |
| regex_v8       | 28.3 ms                                                               | 31.7 ms: 1.12x slower                                                    |
| regex_compile  | 137 ms                                                                | 161 ms: 1.17x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 131 ms: 1.14x faster                                                     |
| xml_etree_parse      | 195 ms                                                                | 180 ms: 1.08x faster                                                     |
| pickle_dict          | 37.3 us                                                               | 41.2 us: 1.10x slower                                                    |
| unpickle             | 18.5 us                                                               | 20.9 us: 1.13x slower                                                    |
| pickle_list          | 5.25 us                                                               | 6.07 us: 1.16x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 7.44 us: 1.21x slower                                                    |
| tomli_loads          | 2.59 sec                                                              | 3.16 sec: 1.22x slower                                                   |
| xml_etree_generate   | 112 ms                                                                | 138 ms: 1.24x slower                                                     |
| pickle               | 13.4 us                                                               | 16.7 us: 1.24x slower                                                    |
| unpickle_pure_python | 260 us                                                                | 333 us: 1.28x slower                                                     |
| json_loads           | 30.7 us                                                               | 39.9 us: 1.30x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 103 ms: 1.30x slower                                                     |
| pickle_pure_python   | 365 us                                                                | 499 us: 1.37x slower                                                     |
| json_dumps           | 12.3 ms                                                               | 17.7 ms: 1.45x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.19x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 12.3 ms: 1.46x slower                                                    |
| python_startup         | 11.4 ms                                                               | 20.1 ms: 1.77x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.61x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 81.1 ms: 1.34x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 37.0 ms: 1.35x slower                                                    |
| django_template | 40.7 ms                                                               | 60.0 ms: 1.47x slower                                                    |
| mako            | 12.9 ms                                                               | 23.4 ms: 1.82x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.48x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| gc_traversal               | 4.40 ms                                                               | 2.75 ms: 1.60x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 914 ms: 1.54x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 500 ms: 1.48x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 955 ms: 1.48x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 539 ms: 1.44x faster                                                     |
| async_tree_none            | 624 ms                                                                | 444 ms: 1.40x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 414 ms: 1.39x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 716 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 695 ms: 1.27x faster                                                     |
| xml_etree_iterparse        | 150 ms                                                                | 131 ms: 1.14x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 4.07 ms: 1.14x faster                                                    |
| xml_etree_parse            | 195 ms                                                                | 180 ms: 1.08x faster                                                     |
| deepcopy                   | 446 us                                                                | 427 us: 1.04x faster                                                     |
| asyncio_websockets         | 658 ms                                                                | 683 ms: 1.04x slower                                                     |
| regex_dna                  | 254 ms                                                                | 267 ms: 1.05x slower                                                     |
| pidigits                   | 233 ms                                                                | 246 ms: 1.06x slower                                                     |
| comprehensions             | 25.4 us                                                               | 27.0 us: 1.06x slower                                                    |
| asyncio_tcp                | 566 ms                                                                | 608 ms: 1.07x slower                                                     |
| spectral_norm              | 131 ms                                                                | 142 ms: 1.08x slower                                                     |
| pylint                     | 355 ms                                                                | 385 ms: 1.08x slower                                                     |
| pickle_dict                | 37.3 us                                                               | 41.2 us: 1.10x slower                                                    |
| async_generators           | 491 ms                                                                | 542 ms: 1.11x slower                                                     |
| go                         | 157 ms                                                                | 174 ms: 1.11x slower                                                     |
| float                      | 92.1 ms                                                               | 102 ms: 1.11x slower                                                     |
| deepcopy_memo              | 49.6 us                                                               | 55.2 us: 1.11x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 31.7 ms: 1.12x slower                                                    |
| mdp                        | 3.41 sec                                                              | 3.83 sec: 1.12x slower                                                   |
| unpickle                   | 18.5 us                                                               | 20.9 us: 1.13x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.39 sec: 1.13x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.20 ms: 1.15x slower                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.72 us: 1.15x slower                                                    |
| scimark_sor                | 150 ms                                                                | 173 ms: 1.16x slower                                                     |
| pickle_list                | 5.25 us                                                               | 6.07 us: 1.16x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 72.0 ms: 1.16x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.54 sec: 1.16x slower                                                   |
| logging_format             | 8.34 us                                                               | 9.73 us: 1.17x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.47 sec: 1.17x slower                                                   |
| scimark_fft                | 418 ms                                                                | 489 ms: 1.17x slower                                                     |
| regex_compile              | 137 ms                                                                | 161 ms: 1.17x slower                                                     |
| logging_simple             | 7.63 us                                                               | 8.97 us: 1.18x slower                                                    |
| raytrace                   | 353 ms                                                                | 423 ms: 1.20x slower                                                     |
| pyflate                    | 559 ms                                                                | 671 ms: 1.20x slower                                                     |
| json                       | 5.54 ms                                                               | 6.66 ms: 1.20x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 7.44 us: 1.21x slower                                                    |
| logging_silent             | 127 ns                                                                | 154 ns: 1.21x slower                                                     |
| tomli_loads                | 2.59 sec                                                              | 3.16 sec: 1.22x slower                                                   |
| sqlglot_normalize          | 126 ms                                                                | 155 ms: 1.23x slower                                                     |
| sympy_sum                  | 154 ms                                                                | 191 ms: 1.23x slower                                                     |
| xml_etree_generate         | 112 ms                                                                | 138 ms: 1.24x slower                                                     |
| html5lib                   | 65.1 ms                                                               | 80.6 ms: 1.24x slower                                                    |
| sqlalchemy_declarative     | 157 ms                                                                | 195 ms: 1.24x slower                                                     |
| pickle                     | 13.4 us                                                               | 16.7 us: 1.24x slower                                                    |
| chaos                      | 71.4 ms                                                               | 88.7 ms: 1.24x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.80 ms: 1.26x slower                                                    |
| 2to3                       | 308 ms                                                                | 388 ms: 1.26x slower                                                     |
| pprint_pformat             | 1.88 sec                                                              | 2.38 sec: 1.27x slower                                                   |
| pprint_safe_repr           | 916 ms                                                                | 1.16 sec: 1.27x slower                                                   |
| sqlglot_optimize           | 61.3 ms                                                               | 77.9 ms: 1.27x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 333 us: 1.28x slower                                                     |
| sympy_integrate            | 21.6 ms                                                               | 28.0 ms: 1.30x slower                                                    |
| json_loads                 | 30.7 us                                                               | 39.9 us: 1.30x slower                                                    |
| sympy_str                  | 280 ms                                                                | 364 ms: 1.30x slower                                                     |
| xml_etree_process          | 79.0 ms                                                               | 103 ms: 1.30x slower                                                     |
| nqueens                    | 99.2 ms                                                               | 130 ms: 1.31x slower                                                     |
| crypto_pyaes               | 86.6 ms                                                               | 114 ms: 1.31x slower                                                     |
| scimark_lu                 | 146 ms                                                                | 193 ms: 1.32x slower                                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 113 ms: 1.33x slower                                                     |
| sqlglot_transpile          | 1.83 ms                                                               | 2.43 ms: 1.33x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 81.1 ms: 1.34x slower                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.96 ms: 1.34x slower                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 22.4 ms: 1.34x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 37.0 ms: 1.35x slower                                                    |
| thrift                     | 937 us                                                                | 1.26 ms: 1.35x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 9.48 ms: 1.36x slower                                                    |
| sympy_expand               | 454 ms                                                                | 616 ms: 1.36x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 499 us: 1.37x slower                                                     |
| telco                      | 8.51 ms                                                               | 11.7 ms: 1.37x slower                                                    |
| meteor_contest             | 112 ms                                                                | 154 ms: 1.38x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 17.7 ms: 1.45x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.90 ms: 1.45x slower                                                    |
| richards                   | 50.9 ms                                                               | 74.5 ms: 1.46x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 12.3 ms: 1.46x slower                                                    |
| richards_super             | 58.5 ms                                                               | 85.9 ms: 1.47x slower                                                    |
| django_template            | 40.7 ms                                                               | 60.0 ms: 1.47x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 6.09 ms: 1.48x slower                                                    |
| coverage                   | 87.3 ms                                                               | 135 ms: 1.54x slower                                                     |
| fannkuch                   | 443 ms                                                                | 688 ms: 1.55x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 281 us: 1.55x slower                                                     |
| nbody                      | 105 ms                                                                | 183 ms: 1.75x slower                                                     |
| python_startup             | 11.4 ms                                                               | 20.1 ms: 1.77x slower                                                    |
| mako                       | 12.9 ms                                                               | 23.4 ms: 1.82x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 58.5 ms: 8.30x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.19x slower                                                             |

Benchmark hidden because not significant (4): generators, pathlib, sqlite_synth, coroutines
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (8) of results/bm-20250208-3.14.0a4+-29f8a67-NOGIL/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.121x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: 1.26x