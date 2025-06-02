# Results vs. 3.12.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-aarch64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.233x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 356 ms: 1.16x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.45 sec: 1.16x slower                                                  |
| html5lib       | 65.1 ms                                                               | 67.3 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 525 ms: 1.48x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 987 ms: 1.43x faster                                                    |
| async_tree_none            | 624 ms                                                                | 441 ms: 1.41x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 524 ms: 1.41x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.02 sec: 1.37x faster                                                  |
| async_tree_none_tg         | 577 ms                                                                | 427 ms: 1.35x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 808 ms: 1.13x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 822 ms: 1.08x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.32x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 96.5 ms: 1.05x slower                                                   |
| pidigits       | 233 ms                                                                | 277 ms: 1.19x slower                                                    |
| nbody          | 105 ms                                                                | 144 ms: 1.37x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.20x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.08 ms: 1.14x faster                                                   |
| regex_dna      | 254 ms                                                                | 226 ms: 1.12x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 30.1 ms: 1.06x slower                                                   |
| regex_compile  | 137 ms                                                                | 158 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 167 ms: 1.11x slower                                                    |
| unpickle_list        | 6.17 us                                                               | 6.91 us: 1.12x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 2.93 sec: 1.13x slower                                                  |
| pickle_dict          | 37.3 us                                                               | 42.6 us: 1.14x slower                                                   |
| xml_etree_parse      | 195 ms                                                                | 229 ms: 1.17x slower                                                    |
| unpickle             | 18.5 us                                                               | 22.6 us: 1.23x slower                                                   |
| json_loads           | 30.7 us                                                               | 38.0 us: 1.24x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 328 us: 1.26x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 474 us: 1.30x slower                                                    |
| pickle_list          | 5.25 us                                                               | 7.06 us: 1.34x slower                                                   |
| xml_etree_process    | 79.0 ms                                                               | 108 ms: 1.36x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 17.2 ms: 1.40x slower                                                   |
| xml_etree_generate   | 112 ms                                                                | 161 ms: 1.43x slower                                                    |
| pickle               | 13.4 us                                                               | 19.7 us: 1.46x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.26x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.71 ms: 1.16x slower                                                   |
| python_startup         | 11.4 ms                                                               | 17.2 ms: 1.51x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.32x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 74.7 ms: 1.23x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 34.4 ms: 1.25x slower                                                   |
| django_template | 40.7 ms                                                               | 52.5 ms: 1.29x slower                                                   |
| mako            | 12.9 ms                                                               | 17.9 ms: 1.39x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.29x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 2.01 sec: 1.70x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 525 ms: 1.48x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 987 ms: 1.43x faster                                                    |
| async_tree_none            | 624 ms                                                                | 441 ms: 1.41x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 524 ms: 1.41x faster                                                    |
| async_tree_io_tg           | 1.40 sec                                                              | 1.02 sec: 1.37x faster                                                  |
| async_tree_none_tg         | 577 ms                                                                | 427 ms: 1.35x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.08 ms: 1.14x faster                                                   |
| deepcopy_memo              | 49.6 us                                                               | 43.7 us: 1.14x faster                                                   |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 808 ms: 1.13x faster                                                    |
| regex_dna                  | 254 ms                                                                | 226 ms: 1.12x faster                                                    |
| go                         | 157 ms                                                                | 141 ms: 1.12x faster                                                    |
| deepcopy                   | 446 us                                                                | 401 us: 1.11x faster                                                    |
| generators                 | 43.5 ms                                                               | 39.6 ms: 1.10x faster                                                   |
| comprehensions             | 25.4 us                                                               | 23.1 us: 1.10x faster                                                   |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 822 ms: 1.08x faster                                                    |
| asyncio_tcp                | 566 ms                                                                | 556 ms: 1.02x faster                                                    |
| asyncio_websockets         | 658 ms                                                                | 670 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.25 sec: 1.03x slower                                                  |
| html5lib                   | 65.1 ms                                                               | 67.3 ms: 1.03x slower                                                   |
| float                      | 92.1 ms                                                               | 96.5 ms: 1.05x slower                                                   |
| pylint                     | 355 ms                                                                | 374 ms: 1.05x slower                                                    |
| pyflate                    | 559 ms                                                                | 590 ms: 1.06x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 65.6 ms: 1.06x slower                                                   |
| async_generators           | 491 ms                                                                | 521 ms: 1.06x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.1 ms: 1.06x slower                                                   |
| pathlib                    | 24.5 ms                                                               | 26.9 ms: 1.10x slower                                                   |
| deltablue                  | 4.12 ms                                                               | 4.54 ms: 1.10x slower                                                   |
| raytrace                   | 353 ms                                                                | 390 ms: 1.11x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 23.9 ms: 1.11x slower                                                   |
| xml_etree_iterparse        | 150 ms                                                                | 167 ms: 1.11x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 94.8 ms: 1.11x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 6.91 us: 1.12x slower                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 4.61 us: 1.13x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.48 ms: 1.13x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.93 sec: 1.13x slower                                                  |
| meteor_contest             | 112 ms                                                                | 127 ms: 1.14x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 42.6 us: 1.14x slower                                                   |
| coroutines                 | 29.0 ms                                                               | 33.1 ms: 1.14x slower                                                   |
| sympy_sum                  | 154 ms                                                                | 178 ms: 1.15x slower                                                    |
| spectral_norm              | 131 ms                                                                | 151 ms: 1.15x slower                                                    |
| regex_compile              | 137 ms                                                                | 158 ms: 1.15x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.45 sec: 1.16x slower                                                  |
| 2to3                       | 308 ms                                                                | 356 ms: 1.16x slower                                                    |
| scimark_sor                | 150 ms                                                                | 173 ms: 1.16x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.71 ms: 1.16x slower                                                   |
| chaos                      | 71.4 ms                                                               | 83.8 ms: 1.17x slower                                                   |
| xml_etree_parse            | 195 ms                                                                | 229 ms: 1.17x slower                                                    |
| pidigits                   | 233 ms                                                                | 277 ms: 1.19x slower                                                    |
| pycparser                  | 1.26 sec                                                              | 1.49 sec: 1.19x slower                                                  |
| scimark_fft                | 418 ms                                                                | 500 ms: 1.19x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 8.37 ms: 1.20x slower                                                   |
| sympy_str                  | 280 ms                                                                | 339 ms: 1.21x slower                                                    |
| crypto_pyaes               | 86.6 ms                                                               | 105 ms: 1.22x slower                                                    |
| richards_super             | 58.5 ms                                                               | 71.2 ms: 1.22x slower                                                   |
| logging_simple             | 7.63 us                                                               | 9.31 us: 1.22x slower                                                   |
| unpickle                   | 18.5 us                                                               | 22.6 us: 1.23x slower                                                   |
| genshi_xml                 | 60.6 ms                                                               | 74.7 ms: 1.23x slower                                                   |
| logging_format             | 8.34 us                                                               | 10.3 us: 1.23x slower                                                   |
| richards                   | 50.9 ms                                                               | 62.9 ms: 1.24x slower                                                   |
| json_loads                 | 30.7 us                                                               | 38.0 us: 1.24x slower                                                   |
| json                       | 5.54 ms                                                               | 6.95 ms: 1.25x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 34.4 ms: 1.25x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.78 ms: 1.26x slower                                                   |
| unpickle_pure_python       | 260 us                                                                | 328 us: 1.26x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 125 ms: 1.26x slower                                                    |
| scimark_lu                 | 146 ms                                                                | 184 ms: 1.27x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 4.81 us: 1.28x slower                                                   |
| django_template            | 40.7 ms                                                               | 52.5 ms: 1.29x slower                                                   |
| pickle_pure_python         | 365 us                                                                | 474 us: 1.30x slower                                                    |
| sympy_expand               | 454 ms                                                                | 599 ms: 1.32x slower                                                    |
| fannkuch                   | 443 ms                                                                | 596 ms: 1.34x slower                                                    |
| pickle_list                | 5.25 us                                                               | 7.06 us: 1.34x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 108 ms: 1.36x slower                                                    |
| nbody                      | 105 ms                                                                | 144 ms: 1.37x slower                                                    |
| mako                       | 12.9 ms                                                               | 17.9 ms: 1.39x slower                                                   |
| json_dumps                 | 12.3 ms                                                               | 17.2 ms: 1.40x slower                                                   |
| xml_etree_generate         | 112 ms                                                                | 161 ms: 1.43x slower                                                    |
| typing_runtime_protocols   | 181 us                                                                | 260 us: 1.44x slower                                                    |
| pickle                     | 13.4 us                                                               | 19.7 us: 1.46x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 2.76 sec: 1.47x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 1.35 sec: 1.47x slower                                                  |
| python_startup             | 11.4 ms                                                               | 17.2 ms: 1.51x slower                                                   |
| telco                      | 8.51 ms                                                               | 13.2 ms: 1.55x slower                                                   |
| gc_traversal               | 4.40 ms                                                               | 7.69 ms: 1.75x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 3.97 ms: 2.07x slower                                                   |
| logging_silent             | 127 ns                                                                | 914 ns: 7.21x slower                                                    |
| coverage                   | 87.3 ms                                                               | 739 ms: 8.47x slower                                                    |
| thrift                     | 937 us                                                                | 199 ms: 212.61x slower                                                  |
| bench_mp_pool              | 7.05 ms                                                               | 5.59 sec: 792.00x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.34x slower                                                            |
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.233x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: 1.11x