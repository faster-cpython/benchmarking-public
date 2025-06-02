# Results vs. 3.12.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-aarch64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.261x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x slower
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 443 ms: 1.44x slower                                                    |
| docutils       | 2.98 sec                                                              | 3.90 sec: 1.31x slower                                                  |
| html5lib       | 65.1 ms                                                               | 82.9 ms: 1.27x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.34x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 992 ms: 1.42x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 523 ms: 1.42x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.01 sec: 1.39x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 560 ms: 1.39x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 430 ms: 1.34x faster                                                    |
| async_tree_none            | 624 ms                                                                | 469 ms: 1.33x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 817 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 863 ms: 1.06x faster                                                    |
| Geometric mean             | (ref)                                                                 | 1.29x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 106 ms: 1.15x slower                                                    |
| pidigits       | 233 ms                                                                | 279 ms: 1.20x slower                                                    |
| nbody          | 105 ms                                                                | 191 ms: 1.82x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.36x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.12 ms: 1.13x faster                                                   |
| regex_dna      | 254 ms                                                                | 231 ms: 1.10x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 30.0 ms: 1.06x slower                                                   |
| regex_compile  | 137 ms                                                                | 197 ms: 1.44x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 156 ms: 1.04x slower                                                    |
| xml_etree_parse      | 195 ms                                                                | 232 ms: 1.19x slower                                                    |
| pickle_dict          | 37.3 us                                                               | 45.7 us: 1.22x slower                                                   |
| unpickle_list        | 6.17 us                                                               | 7.78 us: 1.26x slower                                                   |
| pickle_list          | 5.25 us                                                               | 7.20 us: 1.37x slower                                                   |
| tomli_loads          | 2.59 sec                                                              | 3.61 sec: 1.39x slower                                                  |
| unpickle             | 18.5 us                                                               | 26.5 us: 1.44x slower                                                   |
| json_loads           | 30.7 us                                                               | 44.6 us: 1.45x slower                                                   |
| pickle               | 13.4 us                                                               | 20.3 us: 1.51x slower                                                   |
| unpickle_pure_python | 260 us                                                                | 402 us: 1.55x slower                                                    |
| pickle_pure_python   | 365 us                                                                | 569 us: 1.56x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 19.8 ms: 1.61x slower                                                   |
| xml_etree_process    | 79.0 ms                                                               | 129 ms: 1.63x slower                                                    |
| xml_etree_generate   | 112 ms                                                                | 193 ms: 1.72x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.41x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 13.7 ms: 1.64x slower                                                   |
| python_startup         | 11.4 ms                                                               | 22.9 ms: 2.02x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.82x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                               | 97.2 ms: 1.60x slower                                                   |
| genshi_text     | 27.4 ms                                                               | 45.5 ms: 1.66x slower                                                   |
| django_template | 40.7 ms                                                               | 74.2 ms: 1.82x slower                                                   |
| mako            | 12.9 ms                                                               | 23.7 ms: 1.83x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.73x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 992 ms: 1.42x faster                                                    |
| async_tree_memoization_tg  | 740 ms                                                                | 523 ms: 1.42x faster                                                    |
| async_tree_io              | 1.41 sec                                                              | 1.01 sec: 1.39x faster                                                  |
| async_tree_memoization     | 777 ms                                                                | 560 ms: 1.39x faster                                                    |
| async_tree_none_tg         | 577 ms                                                                | 430 ms: 1.34x faster                                                    |
| mdp                        | 3.41 sec                                                              | 2.55 sec: 1.34x faster                                                  |
| async_tree_none            | 624 ms                                                                | 469 ms: 1.33x faster                                                    |
| gc_traversal               | 4.40 ms                                                               | 3.68 ms: 1.20x faster                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.12 ms: 1.13x faster                                                   |
| regex_dna                  | 254 ms                                                                | 231 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 817 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 863 ms: 1.06x faster                                                    |
| asyncio_websockets         | 658 ms                                                                | 669 ms: 1.02x slower                                                    |
| xml_etree_iterparse        | 150 ms                                                                | 156 ms: 1.04x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 30.0 ms: 1.06x slower                                                   |
| generators                 | 43.5 ms                                                               | 47.8 ms: 1.10x slower                                                   |
| asyncio_tcp                | 566 ms                                                                | 625 ms: 1.10x slower                                                    |
| go                         | 157 ms                                                                | 176 ms: 1.12x slower                                                    |
| float                      | 92.1 ms                                                               | 106 ms: 1.15x slower                                                    |
| deepcopy_memo              | 49.6 us                                                               | 57.2 us: 1.15x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.53 sec: 1.16x slower                                                  |
| sqlite_synth               | 3.77 us                                                               | 4.43 us: 1.18x slower                                                   |
| comprehensions             | 25.4 us                                                               | 30.2 us: 1.19x slower                                                   |
| xml_etree_parse            | 195 ms                                                                | 232 ms: 1.19x slower                                                    |
| deepcopy                   | 446 us                                                                | 530 us: 1.19x slower                                                    |
| pathlib                    | 24.5 ms                                                               | 29.2 ms: 1.19x slower                                                   |
| pidigits                   | 233 ms                                                                | 279 ms: 1.20x slower                                                    |
| pyflate                    | 559 ms                                                                | 682 ms: 1.22x slower                                                    |
| pickle_dict                | 37.3 us                                                               | 45.7 us: 1.22x slower                                                   |
| unpickle_list              | 6.17 us                                                               | 7.78 us: 1.26x slower                                                   |
| html5lib                   | 65.1 ms                                                               | 82.9 ms: 1.27x slower                                                   |
| create_gc_cycles           | 1.92 ms                                                               | 2.45 ms: 1.28x slower                                                   |
| dulwich_log                | 62.0 ms                                                               | 79.3 ms: 1.28x slower                                                   |
| async_generators           | 491 ms                                                                | 632 ms: 1.29x slower                                                    |
| pylint                     | 355 ms                                                                | 459 ms: 1.29x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.90 sec: 1.31x slower                                                  |
| coroutines                 | 29.0 ms                                                               | 38.2 ms: 1.32x slower                                                   |
| scimark_sor                | 150 ms                                                                | 200 ms: 1.34x slower                                                    |
| deltablue                  | 4.12 ms                                                               | 5.57 ms: 1.35x slower                                                   |
| pycparser                  | 1.26 sec                                                              | 1.71 sec: 1.36x slower                                                  |
| pickle_list                | 5.25 us                                                               | 7.20 us: 1.37x slower                                                   |
| tomli_loads                | 2.59 sec                                                              | 3.61 sec: 1.39x slower                                                  |
| meteor_contest             | 112 ms                                                                | 157 ms: 1.40x slower                                                    |
| scimark_fft                | 418 ms                                                                | 590 ms: 1.41x slower                                                    |
| raytrace                   | 353 ms                                                                | 498 ms: 1.41x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 9.83 ms: 1.41x slower                                                   |
| unpickle                   | 18.5 us                                                               | 26.5 us: 1.44x slower                                                   |
| 2to3                       | 308 ms                                                                | 443 ms: 1.44x slower                                                    |
| regex_compile              | 137 ms                                                                | 197 ms: 1.44x slower                                                    |
| chaos                      | 71.4 ms                                                               | 103 ms: 1.44x slower                                                    |
| spectral_norm              | 131 ms                                                                | 190 ms: 1.45x slower                                                    |
| json_loads                 | 30.7 us                                                               | 44.6 us: 1.45x slower                                                   |
| sympy_integrate            | 21.6 ms                                                               | 31.6 ms: 1.46x slower                                                   |
| deepcopy_reduce            | 4.10 us                                                               | 6.01 us: 1.46x slower                                                   |
| json                       | 5.54 ms                                                               | 8.12 ms: 1.47x slower                                                   |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 9.08 ms: 1.47x slower                                                   |
| logging_simple             | 7.63 us                                                               | 11.5 us: 1.51x slower                                                   |
| pickle                     | 13.4 us                                                               | 20.3 us: 1.51x slower                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 2.00 ms: 1.53x slower                                                   |
| logging_format             | 8.34 us                                                               | 12.8 us: 1.53x slower                                                   |
| scimark_lu                 | 146 ms                                                                | 225 ms: 1.54x slower                                                    |
| unpickle_pure_python       | 260 us                                                                | 402 us: 1.55x slower                                                    |
| sympy_sum                  | 154 ms                                                                | 240 ms: 1.55x slower                                                    |
| nqueens                    | 99.2 ms                                                               | 155 ms: 1.56x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 569 us: 1.56x slower                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 133 ms: 1.56x slower                                                    |
| fannkuch                   | 443 ms                                                                | 701 ms: 1.58x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 97.2 ms: 1.60x slower                                                   |
| sympy_str                  | 280 ms                                                                | 450 ms: 1.61x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 19.8 ms: 1.61x slower                                                   |
| xml_etree_process          | 79.0 ms                                                               | 129 ms: 1.63x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 13.7 ms: 1.64x slower                                                   |
| genshi_text                | 27.4 ms                                                               | 45.5 ms: 1.66x slower                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 147 ms: 1.69x slower                                                    |
| richards_super             | 58.5 ms                                                               | 100 ms: 1.71x slower                                                    |
| richards                   | 50.9 ms                                                               | 87.3 ms: 1.71x slower                                                   |
| xml_etree_generate         | 112 ms                                                                | 193 ms: 1.72x slower                                                    |
| sympy_expand               | 454 ms                                                                | 785 ms: 1.73x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 3.27 sec: 1.74x slower                                                  |
| pprint_safe_repr           | 916 ms                                                                | 1.59 sec: 1.74x slower                                                  |
| thrift                     | 937 us                                                                | 1.63 ms: 1.74x slower                                                   |
| nbody                      | 105 ms                                                                | 191 ms: 1.82x slower                                                    |
| django_template            | 40.7 ms                                                               | 74.2 ms: 1.82x slower                                                   |
| mako                       | 12.9 ms                                                               | 23.7 ms: 1.83x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 354 us: 1.96x slower                                                    |
| python_startup             | 11.4 ms                                                               | 22.9 ms: 2.02x slower                                                   |
| telco                      | 8.51 ms                                                               | 17.9 ms: 2.10x slower                                                   |
| coverage                   | 87.3 ms                                                               | 184 ms: 2.11x slower                                                    |
| logging_silent             | 127 ns                                                                | 1.20 us: 9.43x slower                                                   |
| bench_mp_pool              | 7.05 ms                                                               | 72.0 ms: 10.20x slower                                                  |
| Geometric mean             | (ref)                                                                 | 1.39x slower                                                            |
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.261x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.30x
- 95% likely to have a slowdown of 1.28x
- 99% likely to have a slowdown of 1.23x

# Memory
- memory change: 1.37x