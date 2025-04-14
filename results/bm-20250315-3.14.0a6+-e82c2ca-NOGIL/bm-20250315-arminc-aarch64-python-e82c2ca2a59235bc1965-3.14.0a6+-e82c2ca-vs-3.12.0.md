# Results vs. 3.12.0

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: linux-aarch64
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.088x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.06x slower
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 357 ms: 1.16x slower                                                     |
| docutils       | 2.98 sec                                                              | 3.18 sec: 1.07x slower                                                   |
| html5lib       | 65.1 ms                                                               | 73.5 ms: 1.13x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 863 ms: 1.63x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 469 ms: 1.58x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 902 ms: 1.56x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 376 ms: 1.53x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 511 ms: 1.52x faster                                                     |
| async_tree_none            | 624 ms                                                                | 428 ms: 1.46x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 652 ms: 1.36x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 689 ms: 1.32x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.49x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 231 ms: 1.01x faster                                                     |
| float          | 92.1 ms                                                               | 102 ms: 1.11x slower                                                     |
| nbody          | 105 ms                                                                | 181 ms: 1.73x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.24x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.04 ms: 1.15x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 27.4 ms: 1.03x faster                                                    |
| regex_dna      | 254 ms                                                                | 248 ms: 1.02x faster                                                     |
| regex_compile  | 137 ms                                                                | 159 ms: 1.16x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 127 ms: 1.19x faster                                                     |
| xml_etree_parse      | 195 ms                                                                | 176 ms: 1.11x faster                                                     |
| pickle_dict          | 37.3 us                                                               | 39.2 us: 1.05x slower                                                    |
| pickle_list          | 5.25 us                                                               | 5.74 us: 1.09x slower                                                    |
| unpickle             | 18.5 us                                                               | 20.3 us: 1.10x slower                                                    |
| pickle               | 13.4 us                                                               | 15.0 us: 1.12x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 7.27 us: 1.18x slower                                                    |
| tomli_loads          | 2.59 sec                                                              | 3.06 sec: 1.18x slower                                                   |
| xml_etree_generate   | 112 ms                                                                | 134 ms: 1.19x slower                                                     |
| unpickle_pure_python | 260 us                                                                | 310 us: 1.19x slower                                                     |
| pickle_pure_python   | 365 us                                                                | 440 us: 1.21x slower                                                     |
| json_loads           | 30.7 us                                                               | 38.2 us: 1.25x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 98.6 ms: 1.25x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 16.4 ms: 1.33x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.13x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 14.0 ms: 1.67x slower                                                    |
| python_startup         | 11.4 ms                                                               | 19.6 ms: 1.72x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.70x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 74.0 ms: 1.22x slower                                                    |
| django_template | 40.7 ms                                                               | 53.5 ms: 1.32x slower                                                    |
| genshi_text     | 27.4 ms                                                               | 37.4 ms: 1.36x slower                                                    |
| mako            | 12.9 ms                                                               | 21.9 ms: 1.70x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.39x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 863 ms: 1.63x faster                                                     |
| gc_traversal               | 4.40 ms                                                               | 2.71 ms: 1.62x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 469 ms: 1.58x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 902 ms: 1.56x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 376 ms: 1.53x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 511 ms: 1.52x faster                                                     |
| async_tree_none            | 624 ms                                                                | 428 ms: 1.46x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 652 ms: 1.36x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 689 ms: 1.32x faster                                                     |
| xml_etree_iterparse        | 150 ms                                                                | 127 ms: 1.19x faster                                                     |
| regex_effbot               | 4.64 ms                                                               | 4.04 ms: 1.15x faster                                                    |
| deepcopy                   | 446 us                                                                | 399 us: 1.12x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 176 ms: 1.11x faster                                                     |
| sqlite_synth               | 3.77 us                                                               | 3.44 us: 1.10x faster                                                    |
| generators                 | 43.5 ms                                                               | 40.0 ms: 1.09x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 59.2 ms: 1.05x faster                                                    |
| regex_v8                   | 28.3 ms                                                               | 27.4 ms: 1.03x faster                                                    |
| regex_dna                  | 254 ms                                                                | 248 ms: 1.02x faster                                                     |
| pidigits                   | 233 ms                                                                | 231 ms: 1.01x faster                                                     |
| coroutines                 | 29.0 ms                                                               | 28.9 ms: 1.00x faster                                                    |
| asyncio_websockets         | 658 ms                                                                | 670 ms: 1.02x slower                                                     |
| asyncio_tcp                | 566 ms                                                                | 589 ms: 1.04x slower                                                     |
| async_generators           | 491 ms                                                                | 514 ms: 1.05x slower                                                     |
| pickle_dict                | 37.3 us                                                               | 39.2 us: 1.05x slower                                                    |
| pylint                     | 355 ms                                                                | 373 ms: 1.05x slower                                                     |
| comprehensions             | 25.4 us                                                               | 26.9 us: 1.06x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.18 sec: 1.07x slower                                                   |
| go                         | 157 ms                                                                | 169 ms: 1.08x slower                                                     |
| create_gc_cycles           | 1.92 ms                                                               | 2.08 ms: 1.08x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.37 sec: 1.09x slower                                                   |
| mdp                        | 3.41 sec                                                              | 3.71 sec: 1.09x slower                                                   |
| spectral_norm              | 131 ms                                                                | 143 ms: 1.09x slower                                                     |
| pickle_list                | 5.25 us                                                               | 5.74 us: 1.09x slower                                                    |
| unpickle                   | 18.5 us                                                               | 20.3 us: 1.10x slower                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 4.52 us: 1.10x slower                                                    |
| float                      | 92.1 ms                                                               | 102 ms: 1.11x slower                                                     |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.43 sec: 1.11x slower                                                   |
| logging_simple             | 7.63 us                                                               | 8.53 us: 1.12x slower                                                    |
| pyflate                    | 559 ms                                                                | 625 ms: 1.12x slower                                                     |
| pickle                     | 13.4 us                                                               | 15.0 us: 1.12x slower                                                    |
| logging_silent             | 127 ns                                                                | 143 ns: 1.13x slower                                                     |
| logging_format             | 8.34 us                                                               | 9.42 us: 1.13x slower                                                    |
| scimark_sor                | 150 ms                                                                | 169 ms: 1.13x slower                                                     |
| html5lib                   | 65.1 ms                                                               | 73.5 ms: 1.13x slower                                                    |
| scimark_fft                | 418 ms                                                                | 481 ms: 1.15x slower                                                     |
| raytrace                   | 353 ms                                                                | 407 ms: 1.15x slower                                                     |
| 2to3                       | 308 ms                                                                | 357 ms: 1.16x slower                                                     |
| regex_compile              | 137 ms                                                                | 159 ms: 1.16x slower                                                     |
| json                       | 5.54 ms                                                               | 6.47 ms: 1.17x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 7.27 us: 1.18x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 3.06 sec: 1.18x slower                                                   |
| sqlalchemy_declarative     | 157 ms                                                                | 187 ms: 1.19x slower                                                     |
| xml_etree_generate         | 112 ms                                                                | 134 ms: 1.19x slower                                                     |
| unpickle_pure_python       | 260 us                                                                | 310 us: 1.19x slower                                                     |
| pickle_pure_python         | 365 us                                                                | 440 us: 1.21x slower                                                     |
| deltablue                  | 4.12 ms                                                               | 4.97 ms: 1.21x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 1.11 sec: 1.21x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.28 sec: 1.21x slower                                                   |
| chaos                      | 71.4 ms                                                               | 87.2 ms: 1.22x slower                                                    |
| thrift                     | 937 us                                                                | 1.14 ms: 1.22x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 74.0 ms: 1.22x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 192 ms: 1.24x slower                                                     |
| json_loads                 | 30.7 us                                                               | 38.2 us: 1.25x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 98.6 ms: 1.25x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 108 ms: 1.25x slower                                                     |
| sympy_integrate            | 21.6 ms                                                               | 27.1 ms: 1.25x slower                                                    |
| sympy_str                  | 280 ms                                                                | 352 ms: 1.26x slower                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 21.1 ms: 1.27x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 127 ms: 1.28x slower                                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 110 ms: 1.29x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 9.08 ms: 1.30x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 189 ms: 1.30x slower                                                     |
| sympy_expand               | 454 ms                                                                | 595 ms: 1.31x slower                                                     |
| django_template            | 40.7 ms                                                               | 53.5 ms: 1.32x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 8.24 ms: 1.33x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 16.4 ms: 1.33x slower                                                    |
| telco                      | 8.51 ms                                                               | 11.5 ms: 1.35x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 37.4 ms: 1.36x slower                                                    |
| richards                   | 50.9 ms                                                               | 69.8 ms: 1.37x slower                                                    |
| meteor_contest             | 112 ms                                                                | 155 ms: 1.38x slower                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.82 ms: 1.39x slower                                                    |
| richards_super             | 58.5 ms                                                               | 81.7 ms: 1.40x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 263 us: 1.46x slower                                                     |
| coverage                   | 87.3 ms                                                               | 128 ms: 1.47x slower                                                     |
| fannkuch                   | 443 ms                                                                | 652 ms: 1.47x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 14.0 ms: 1.67x slower                                                    |
| mako                       | 12.9 ms                                                               | 21.9 ms: 1.70x slower                                                    |
| python_startup             | 11.4 ms                                                               | 19.6 ms: 1.72x slower                                                    |
| nbody                      | 105 ms                                                                | 181 ms: 1.73x slower                                                     |
| bench_mp_pool              | 7.05 ms                                                               | 57.7 ms: 8.18x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.13x slower                                                             |

Benchmark hidden because not significant (2): pathlib, deepcopy_memo
Ignored benchmarks (10) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250315-3.14.0a6+-e82c2ca-NOGIL/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.088x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 1.27x