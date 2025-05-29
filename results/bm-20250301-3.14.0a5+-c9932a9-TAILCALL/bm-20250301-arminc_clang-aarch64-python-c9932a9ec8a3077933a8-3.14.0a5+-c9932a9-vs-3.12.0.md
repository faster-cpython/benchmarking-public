# Results vs. 3.12.0

- fork: python
- ref: c9932a9ec8a3077933a8
- machine: linux-aarch64
- commit hash: c9932a9
- commit date: 2025-03-01
- overall geometric mean: 1.060x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| html5lib       | 65.1 ms                                                               | 60.4 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                             |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 371 ms: 1.68x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 478 ms: 1.62x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 883 ms: 1.59x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 470 ms: 1.57x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 900 ms: 1.57x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 381 ms: 1.51x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 749 ms: 1.22x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 727 ms: 1.22x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.49x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 105 ms                                                                | 116 ms: 1.11x slower                                                     |
| pidigits       | 233 ms                                                                | 293 ms: 1.26x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                             |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 125 ms: 1.10x faster                                                     |
| regex_effbot   | 4.64 ms                                                               | 4.32 ms: 1.07x faster                                                    |
| regex_v8       | 28.3 ms                                                               | 34.4 ms: 1.21x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|--------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle           | 18.5 us                                                               | 17.5 us: 1.06x faster                                                    |
| tomli_loads        | 2.59 sec                                                              | 2.45 sec: 1.06x faster                                                   |
| xml_etree_generate | 112 ms                                                                | 106 ms: 1.05x faster                                                     |
| unpickle_list      | 6.17 us                                                               | 5.89 us: 1.05x faster                                                    |
| pickle_list        | 5.25 us                                                               | 5.56 us: 1.06x slower                                                    |
| xml_etree_parse    | 195 ms                                                                | 212 ms: 1.09x slower                                                     |
| pickle_pure_python | 365 us                                                                | 399 us: 1.09x slower                                                     |
| json_loads         | 30.7 us                                                               | 33.6 us: 1.10x slower                                                    |
| pickle             | 13.4 us                                                               | 15.0 us: 1.12x slower                                                    |
| json_dumps         | 12.3 ms                                                               | 14.7 ms: 1.20x slower                                                    |
| Geometric mean     | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (4): xml_etree_process, pickle_dict, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.29 ms: 1.11x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.5 ms: 1.45x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.27x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 37.7 ms: 1.08x faster                                                    |
| mako            | 12.9 ms                                                               | 14.0 ms: 1.08x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 371 ms: 1.68x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 478 ms: 1.62x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 883 ms: 1.59x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 470 ms: 1.57x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 900 ms: 1.57x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 381 ms: 1.51x faster                                                     |
| deepcopy                   | 446 us                                                                | 313 us: 1.43x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 37.0 us: 1.34x faster                                                    |
| comprehensions             | 25.4 us                                                               | 19.7 us: 1.29x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.35 us: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 749 ms: 1.22x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 727 ms: 1.22x faster                                                     |
| pylint                     | 355 ms                                                                | 297 ms: 1.20x faster                                                     |
| async_generators           | 491 ms                                                                | 417 ms: 1.18x faster                                                     |
| go                         | 157 ms                                                                | 135 ms: 1.17x faster                                                     |
| generators                 | 43.5 ms                                                               | 37.4 ms: 1.16x faster                                                    |
| spectral_norm              | 131 ms                                                                | 112 ms: 1.16x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 21.3 ms: 1.15x faster                                                    |
| raytrace                   | 353 ms                                                                | 311 ms: 1.13x faster                                                     |
| sympy_sum                  | 154 ms                                                                | 138 ms: 1.12x faster                                                     |
| logging_simple             | 7.63 us                                                               | 6.90 us: 1.11x faster                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.1 ms: 1.10x faster                                                    |
| regex_compile              | 137 ms                                                                | 125 ms: 1.10x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.69 us: 1.09x faster                                                    |
| sqlalchemy_declarative     | 157 ms                                                                | 146 ms: 1.08x faster                                                     |
| django_template            | 40.7 ms                                                               | 37.7 ms: 1.08x faster                                                    |
| scimark_fft                | 418 ms                                                                | 388 ms: 1.08x faster                                                     |
| html5lib                   | 65.1 ms                                                               | 60.4 ms: 1.08x faster                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 1.70 ms: 1.07x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.32 ms: 1.07x faster                                                    |
| logging_silent             | 127 ns                                                                | 119 ns: 1.07x faster                                                     |
| sympy_integrate            | 21.6 ms                                                               | 20.3 ms: 1.07x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 80.3 ms: 1.06x faster                                                    |
| unpickle                   | 18.5 us                                                               | 17.5 us: 1.06x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.45 sec: 1.06x faster                                                   |
| chaos                      | 71.4 ms                                                               | 67.7 ms: 1.06x faster                                                    |
| xml_etree_generate         | 112 ms                                                                | 106 ms: 1.05x faster                                                     |
| scimark_sor                | 150 ms                                                                | 142 ms: 1.05x faster                                                     |
| mdp                        | 3.41 sec                                                              | 3.24 sec: 1.05x faster                                                   |
| scimark_lu                 | 146 ms                                                                | 138 ms: 1.05x faster                                                     |
| sqlglot_parse              | 1.46 ms                                                               | 1.39 ms: 1.05x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.93 ms: 1.05x faster                                                    |
| unpickle_list              | 6.17 us                                                               | 5.89 us: 1.05x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 59.2 ms: 1.05x faster                                                    |
| richards                   | 50.9 ms                                                               | 48.9 ms: 1.04x faster                                                    |
| pyflate                    | 559 ms                                                                | 537 ms: 1.04x faster                                                     |
| pprint_safe_repr           | 916 ms                                                                | 937 ms: 1.02x slower                                                     |
| asyncio_websockets         | 658 ms                                                                | 676 ms: 1.03x slower                                                     |
| pprint_pformat             | 1.88 sec                                                              | 1.95 sec: 1.04x slower                                                   |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.29 sec: 1.05x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 190 us: 1.05x slower                                                     |
| pickle_list                | 5.25 us                                                               | 5.56 us: 1.06x slower                                                    |
| hexiom                     | 6.98 ms                                                               | 7.41 ms: 1.06x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.13 ms: 1.07x slower                                                    |
| mako                       | 12.9 ms                                                               | 14.0 ms: 1.08x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 4.08 us: 1.08x slower                                                    |
| xml_etree_parse            | 195 ms                                                                | 212 ms: 1.09x slower                                                     |
| json                       | 5.54 ms                                                               | 6.05 ms: 1.09x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 399 us: 1.09x slower                                                     |
| meteor_contest             | 112 ms                                                                | 122 ms: 1.09x slower                                                     |
| json_loads                 | 30.7 us                                                               | 33.6 us: 1.10x slower                                                    |
| coverage                   | 87.3 ms                                                               | 96.4 ms: 1.10x slower                                                    |
| nbody                      | 105 ms                                                                | 116 ms: 1.11x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 9.29 ms: 1.11x slower                                                    |
| fannkuch                   | 443 ms                                                                | 495 ms: 1.12x slower                                                     |
| pickle                     | 13.4 us                                                               | 15.0 us: 1.12x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.7 ms: 1.20x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 34.4 ms: 1.21x slower                                                    |
| pidigits                   | 233 ms                                                                | 293 ms: 1.26x slower                                                     |
| python_startup             | 11.4 ms                                                               | 16.5 ms: 1.45x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.72 ms: 1.53x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.69 ms: 1.92x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 3.26 sec: 462.38x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (23): xml_etree_process, sympy_str, bench_thread_pool, genshi_text, scimark_sparse_mat_mult, 2to3, thrift, float, coroutines, crypto_pyaes, pickle_dict, nqueens, richards_super, sqlglot_normalize, sympy_expand, pycparser, genshi_xml, docutils, sqlglot_optimize, regex_dna, unpickle_pure_python, xml_etree_iterparse, asyncio_tcp
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (8) of results/bm-20250301-3.14.0a5+-c9932a9-CLANG/bm-20250301-arminc-aarch64-python-c9932a9ec8a3077933a8-3.14.0a5+-c9932a9.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.060x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.08x