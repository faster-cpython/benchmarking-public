# Results vs. 3.12.0

- fork: python
- ref: 71da68d5887b6c058907
- machine: linux-aarch64
- commit hash: 71da68d
- commit date: 2025-04-19
- overall geometric mean: 1.075x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 289 ms: 1.07x faster                                                     |
| docutils       | 2.98 sec                                                              | 2.90 sec: 1.03x faster                                                   |
| html5lib       | 65.1 ms                                                               | 58.6 ms: 1.11x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 455 ms: 1.71x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 861 ms: 1.64x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 452 ms: 1.64x faster                                                     |
| async_tree_none            | 624 ms                                                                | 381 ms: 1.64x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 871 ms: 1.61x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 368 ms: 1.57x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 727 ms: 1.26x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 704 ms: 1.26x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.53x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 84.0 ms: 1.10x faster                                                    |
| nbody          | 105 ms                                                                | 126 ms: 1.21x slower                                                     |
| pidigits       | 233 ms                                                                | 291 ms: 1.25x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.02 ms: 1.15x faster                                                    |
| regex_compile  | 137 ms                                                                | 123 ms: 1.12x faster                                                     |
| regex_dna      | 254 ms                                                                | 232 ms: 1.09x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|--------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle           | 18.5 us                                                               | 16.4 us: 1.12x faster                                                    |
| tomli_loads        | 2.59 sec                                                              | 2.35 sec: 1.10x faster                                                   |
| unpickle_list      | 6.17 us                                                               | 5.72 us: 1.08x faster                                                    |
| xml_etree_generate | 112 ms                                                                | 104 ms: 1.08x faster                                                     |
| xml_etree_process  | 79.0 ms                                                               | 74.9 ms: 1.05x faster                                                    |
| pickle_pure_python | 365 us                                                                | 367 us: 1.01x slower                                                     |
| pickle_list        | 5.25 us                                                               | 5.32 us: 1.01x slower                                                    |
| xml_etree_parse    | 195 ms                                                                | 207 ms: 1.06x slower                                                     |
| json_loads         | 30.7 us                                                               | 33.5 us: 1.09x slower                                                    |
| pickle             | 13.4 us                                                               | 15.4 us: 1.15x slower                                                    |
| json_dumps         | 12.3 ms                                                               | 14.5 ms: 1.18x slower                                                    |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (3): pickle_dict, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.3 ms: 1.44x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.32x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 26.1 ms: 1.05x faster                                                    |
| mako           | 12.9 ms                                                               | 14.0 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.61 sec: 2.12x faster                                                   |
| async_tree_memoization     | 777 ms                                                                | 455 ms: 1.71x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 861 ms: 1.64x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 452 ms: 1.64x faster                                                     |
| async_tree_none            | 624 ms                                                                | 381 ms: 1.64x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 871 ms: 1.61x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 368 ms: 1.57x faster                                                     |
| deepcopy                   | 446 us                                                                | 308 us: 1.44x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 35.6 us: 1.39x faster                                                    |
| comprehensions             | 25.4 us                                                               | 20.0 us: 1.27x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 727 ms: 1.26x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 704 ms: 1.26x faster                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 3.27 us: 1.25x faster                                                    |
| generators                 | 43.5 ms                                                               | 35.2 ms: 1.23x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 50.7 ms: 1.22x faster                                                    |
| go                         | 157 ms                                                                | 129 ms: 1.22x faster                                                     |
| async_generators           | 491 ms                                                                | 416 ms: 1.18x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 21.2 ms: 1.16x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.02 ms: 1.15x faster                                                    |
| pylint                     | 355 ms                                                                | 310 ms: 1.15x faster                                                     |
| sympy_sum                  | 154 ms                                                                | 136 ms: 1.13x faster                                                     |
| unpickle                   | 18.5 us                                                               | 16.4 us: 1.12x faster                                                    |
| regex_compile              | 137 ms                                                                | 123 ms: 1.12x faster                                                     |
| sympy_integrate            | 21.6 ms                                                               | 19.4 ms: 1.12x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 58.6 ms: 1.11x faster                                                    |
| raytrace                   | 353 ms                                                                | 318 ms: 1.11x faster                                                     |
| logging_silent             | 127 ns                                                                | 114 ns: 1.11x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.56 us: 1.10x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.35 sec: 1.10x faster                                                   |
| spectral_norm              | 131 ms                                                                | 119 ms: 1.10x faster                                                     |
| logging_simple             | 7.63 us                                                               | 6.96 us: 1.10x faster                                                    |
| chaos                      | 71.4 ms                                                               | 65.1 ms: 1.10x faster                                                    |
| float                      | 92.1 ms                                                               | 84.0 ms: 1.10x faster                                                    |
| regex_dna                  | 254 ms                                                                | 232 ms: 1.09x faster                                                     |
| sympy_str                  | 280 ms                                                                | 257 ms: 1.09x faster                                                     |
| unpickle_list              | 6.17 us                                                               | 5.72 us: 1.08x faster                                                    |
| xml_etree_generate         | 112 ms                                                                | 104 ms: 1.08x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 146 ms: 1.07x faster                                                     |
| deltablue                  | 4.12 ms                                                               | 3.85 ms: 1.07x faster                                                    |
| 2to3                       | 308 ms                                                                | 289 ms: 1.07x faster                                                     |
| asyncio_tcp                | 566 ms                                                                | 533 ms: 1.06x faster                                                     |
| pyflate                    | 559 ms                                                                | 527 ms: 1.06x faster                                                     |
| xml_etree_process          | 79.0 ms                                                               | 74.9 ms: 1.05x faster                                                    |
| genshi_text                | 27.4 ms                                                               | 26.1 ms: 1.05x faster                                                    |
| richards                   | 50.9 ms                                                               | 48.7 ms: 1.05x faster                                                    |
| scimark_sor                | 150 ms                                                                | 144 ms: 1.04x faster                                                     |
| docutils                   | 2.98 sec                                                              | 2.90 sec: 1.03x faster                                                   |
| crypto_pyaes               | 86.6 ms                                                               | 84.3 ms: 1.03x faster                                                    |
| pycparser                  | 1.26 sec                                                              | 1.23 sec: 1.02x faster                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.16 sec: 1.01x faster                                                   |
| hexiom                     | 6.98 ms                                                               | 6.94 ms: 1.01x faster                                                    |
| pickle_pure_python         | 365 us                                                                | 367 us: 1.01x slower                                                     |
| pickle_list                | 5.25 us                                                               | 5.32 us: 1.01x slower                                                    |
| asyncio_websockets         | 658 ms                                                                | 670 ms: 1.02x slower                                                     |
| typing_runtime_protocols   | 181 us                                                                | 188 us: 1.04x slower                                                     |
| json                       | 5.54 ms                                                               | 5.84 ms: 1.05x slower                                                    |
| xml_etree_parse            | 195 ms                                                                | 207 ms: 1.06x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 30.3 ms: 1.07x slower                                                    |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.62 ms: 1.07x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.18 ms: 1.08x slower                                                    |
| mako                       | 12.9 ms                                                               | 14.0 ms: 1.08x slower                                                    |
| json_loads                 | 30.7 us                                                               | 33.5 us: 1.09x slower                                                    |
| fannkuch                   | 443 ms                                                                | 495 ms: 1.12x slower                                                     |
| pickle                     | 13.4 us                                                               | 15.4 us: 1.15x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.5 ms: 1.18x slower                                                    |
| nbody                      | 105 ms                                                                | 126 ms: 1.21x slower                                                     |
| coverage                   | 87.3 ms                                                               | 106 ms: 1.22x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 10.2 ms: 1.22x slower                                                    |
| pidigits                   | 233 ms                                                                | 291 ms: 1.25x slower                                                     |
| python_startup             | 11.4 ms                                                               | 16.3 ms: 1.44x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.64 ms: 1.51x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.73 ms: 1.94x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 1.85 sec: 262.27x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (18): django_template, genshi_xml, sqlalchemy_imperative, richards_super, pickle_dict, scimark_monte_carlo, unpickle_pure_python, nqueens, coroutines, sympy_expand, scimark_lu, pprint_safe_repr, xml_etree_iterparse, pprint_pformat, scimark_fft, bench_thread_pool, sqlite_synth, meteor_contest
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250419-3.14.0a7+-71da68d-CLANG/bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.075x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.09x