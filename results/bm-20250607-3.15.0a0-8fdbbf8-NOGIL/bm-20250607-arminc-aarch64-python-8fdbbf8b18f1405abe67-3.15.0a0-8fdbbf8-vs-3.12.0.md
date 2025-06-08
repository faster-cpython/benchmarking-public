# Results vs. 3.12.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-aarch64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.265x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x slower
- Memory change: 1.36x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 447 ms: 1.45x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.92 sec: 1.31x slower                                                  |
| html5lib       | 65.1 ms                                                               | 82.9 ms: 1.27x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.34x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 983 ms: 1.43x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 521 ms: 1.42x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.01 sec: 1.39x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 560 ms: 1.39x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 430 ms: 1.34x faster                                                    |
| async_tree_none            | 624 ms                                                                | 466 ms: 1.34x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 812 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 847 ms: 1.08x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.30x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 106 ms: 1.15x slower                                                    |
| pidigits       | 233 ms                                                                | 277 ms: 1.19x slower                                                    |
| nbody          | 105 ms                                                                | 192 ms: 1.83x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.36x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.20 ms: 1.11x faster                                                   |
| regex_dna      | 254 ms                                                                | 233 ms: 1.09x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 30.8 ms: 1.09x slower                                                   |
| regex_compile  | 137 ms                                                                | 196 ms: 1.43x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 158 ms: 1.05x slower                                                    |
| xml_etree_parse      | 195 ms                                                                | 236 ms: 1.21x slower                                                    |
| pickle_dict          | 37.3 us                                                               | 45.5 us: 1.22x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 7.77 us: 1.26x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 3.55 sec: 1.37x slower                                                  |
| pickle_list          | 5.25 us                                                               | 7.26 us: 1.38x slower                                                   |
| unpickle             | 18.5 us                                                               | 26.7 us: 1.45x slower                                                   |
| json_loads           | 30.7 us                                                               | 44.9 us: 1.46x slower                                                   |
| pickle               | 13.4 us                                                               | 20.0 us: 1.49x slower                                                   |
| pickle_pure_python   | 365 us                                                                | 580 us: 1.59x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 19.7 ms: 1.61x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 420 us: 1.61x slower                                                    |
| xml_etree_process    | 79.0 ms                                                               | 129 ms: 1.64x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 192 ms: 1.71x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.42x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 13.8 ms: 1.65x slower                                                   |
| python_startup         | 11.4 ms                                                               | 22.9 ms: 2.01x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.82x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 97.3 ms: 1.61x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 46.0 ms: 1.68x slower                                                   |
| django_template | 40.7 ms                                                               | 73.3 ms: 1.80x slower                                                   |
| mako            | 12.9 ms                                                               | 24.1 ms: 1.87x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.74x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 983 ms: 1.43x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 521 ms: 1.42x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.01 sec: 1.39x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 560 ms: 1.39x faster                                                    |
| mdp                        | 3.41 sec                                                              | 2.54 sec: 1.34x faster                                                  |
| async_tree_none_tg         | 577 ms                                                                | 430 ms: 1.34x faster                                                    |
| async_tree_none            | 624 ms                                                                | 466 ms: 1.34x faster                                                    |
| gc_traversal               | 4.40 ms                                                               | 3.58 ms: 1.23x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.20 ms: 1.11x faster                                                   |
| regex_dna                  | 254 ms                                                                | 233 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 812 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 847 ms: 1.08x faster                                                    |
| asyncio_websockets         | 658 ms                                                                | 671 ms: 1.02x slower                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 158 ms: 1.05x slower                                                    |
| generators                 | 43.5 ms                                                               | 46.9 ms: 1.08x slower                                                   |
| regex_v8                   | 28.3 ms                                                               | 30.8 ms: 1.09x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 627 ms: 1.11x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.50 sec: 1.14x slower                                                  |
| deepcopy_memo              | 49.6 us                                                               | 56.9 us: 1.15x slower                                                   |
| float                      | 92.1 ms                                                               | 106 ms: 1.15x slower                                                    |
| go                         | 157 ms                                                                | 182 ms: 1.16x slower                                                    |
| deepcopy                   | 446 us                                                                | 529 us: 1.19x slower                                                    |
| pidigits                   | 233 ms                                                                | 277 ms: 1.19x slower                                                    |
| comprehensions             | 25.4 us                                                               | 30.2 us: 1.19x slower                                                   |
| sqlite_synth               | 3.77 us                                                               | 4.51 us: 1.20x slower                                                   |
| xml_etree_parse            | 195 ms                                                                | 236 ms: 1.21x slower                                                    |
| pathlib                    | 24.5 ms                                                               | 29.9 ms: 1.22x slower                                                   |
| pickle_dict                | 37.3 us                                                               | 45.5 us: 1.22x slower                                                   |
| pyflate                    | 559 ms                                                                | 685 ms: 1.23x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 7.77 us: 1.26x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 82.9 ms: 1.27x slower                                                   |
| async_generators           | 491 ms                                                                | 626 ms: 1.28x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 79.5 ms: 1.28x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.49 ms: 1.30x slower                                                   |
| docutils                   | 2.98 sec                                                              | 3.92 sec: 1.31x slower                                                  |
| pylint                     | 355 ms                                                                | 468 ms: 1.32x slower                                                    |
| coroutines                 | 29.0 ms                                                               | 38.4 ms: 1.32x slower                                                   |
| scimark_sor                | 150 ms                                                                | 204 ms: 1.36x slower                                                    |
| tomli_loads                | 2.59 sec                                                              | 3.55 sec: 1.37x slower                                                  |
| meteor_contest             | 112 ms                                                                | 154 ms: 1.37x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 5.68 ms: 1.38x slower                                                   |
| pickle_list                | 5.25 us                                                               | 7.26 us: 1.38x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.75 sec: 1.39x slower                                                  |
| scimark_fft                | 418 ms                                                                | 583 ms: 1.39x slower                                                    |
| raytrace                   | 353 ms                                                                | 496 ms: 1.40x slower                                                    |
| chaos                      | 71.4 ms                                                               | 101 ms: 1.41x slower                                                    |
| regex_compile              | 137 ms                                                                | 196 ms: 1.43x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 10.0 ms: 1.44x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 31.3 ms: 1.45x slower                                                   |
| unpickle                   | 18.5 us                                                               | 26.7 us: 1.45x slower                                                   |
| 2to3                       | 308 ms                                                                | 447 ms: 1.45x slower                                                    |
| json                       | 5.54 ms                                                               | 8.06 ms: 1.45x slower                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 5.97 us: 1.46x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 9.05 ms: 1.46x slower                                                   |
| json_loads                 | 30.7 us                                                               | 44.9 us: 1.46x slower                                                   |
| spectral_norm              | 131 ms                                                                | 193 ms: 1.48x slower                                                    |
| pickle                     | 13.4 us                                                               | 20.0 us: 1.49x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.98 ms: 1.51x slower                                                   |
| logging_simple             | 7.63 us                                                               | 11.7 us: 1.53x slower                                                   |
| logging_format             | 8.34 us                                                               | 13.0 us: 1.55x slower                                                   |
| nqueens                    | 99.2 ms                                                               | 156 ms: 1.57x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 580 us: 1.59x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 246 ms: 1.59x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 97.3 ms: 1.61x slower                                                   |
| sympy_str                  | 280 ms                                                                | 449 ms: 1.61x slower                                                    |
| fannkuch                   | 443 ms                                                                | 713 ms: 1.61x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 234 ms: 1.61x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 19.7 ms: 1.61x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 420 us: 1.61x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 139 ms: 1.63x slower                                                    |
| xml_etree_process          | 79.0 ms                                                               | 129 ms: 1.64x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 13.8 ms: 1.65x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 145 ms: 1.67x slower                                                    |
| genshi_text                | 27.4 ms                                                               | 46.0 ms: 1.68x slower                                                   |
| richards                   | 50.9 ms                                                               | 86.8 ms: 1.70x slower                                                   |
| xml_etree_generate         | 112 ms                                                                | 192 ms: 1.71x slower                                                    |
| richards_super             | 58.5 ms                                                               | 101 ms: 1.73x slower                                                    |
| thrift                     | 937 us                                                                | 1.63 ms: 1.74x slower                                                   |
| sympy_expand               | 454 ms                                                                | 790 ms: 1.74x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 3.31 sec: 1.76x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 1.62 sec: 1.77x slower                                                  |
| django_template            | 40.7 ms                                                               | 73.3 ms: 1.80x slower                                                   |
| nbody                      | 105 ms                                                                | 192 ms: 1.83x slower                                                    |
| mako                       | 12.9 ms                                                               | 24.1 ms: 1.87x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 354 us: 1.96x slower                                                    |
| python_startup             | 11.4 ms                                                               | 22.9 ms: 2.01x slower                                                   |
| coverage                   | 87.3 ms                                                               | 184 ms: 2.10x slower                                                    |
| telco                      | 8.51 ms                                                               | 18.1 ms: 2.13x slower                                                   |
| logging_silent             | 127 ns                                                                | 1.13 us: 8.87x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 72.6 ms: 10.30x slower                                                  |
| Geometric mean             | (ref)                                                                 | 1.39x slower                                                            |
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250607-3.15.0a0-8fdbbf8-NOGIL/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.265x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.31x
- 95% likely to have a slowdown of 1.28x
- 99% likely to have a slowdown of 1.24x

# Memory
- memory change: 1.36x