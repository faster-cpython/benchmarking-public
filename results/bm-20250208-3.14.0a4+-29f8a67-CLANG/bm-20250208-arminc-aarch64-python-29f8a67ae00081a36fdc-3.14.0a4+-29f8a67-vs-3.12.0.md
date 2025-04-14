# Results vs. 3.12.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-aarch64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.066x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 294 ms: 1.05x faster                                                     |
| html5lib       | 65.1 ms                                                               | 59.3 ms: 1.10x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                             |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 480 ms: 1.62x faster                                                     |
| async_tree_none            | 624 ms                                                                | 387 ms: 1.61x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 472 ms: 1.57x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 904 ms: 1.55x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 908 ms: 1.55x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 376 ms: 1.53x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 758 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 739 ms: 1.20x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.47x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 82.9 ms: 1.11x faster                                                    |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                                     |
| pidigits       | 233 ms                                                                | 303 ms: 1.30x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 120 ms: 1.14x faster                                                     |
| regex_dna      | 254 ms                                                                | 250 ms: 1.02x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 34.5 ms: 1.22x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate   | 112 ms                                                                | 103 ms: 1.09x faster                                                     |
| xml_etree_process    | 79.0 ms                                                               | 74.6 ms: 1.06x faster                                                    |
| tomli_loads          | 2.59 sec                                                              | 2.46 sec: 1.06x faster                                                   |
| unpickle_pure_python | 260 us                                                                | 252 us: 1.03x faster                                                     |
| xml_etree_parse      | 195 ms                                                                | 209 ms: 1.07x slower                                                     |
| json_loads           | 30.7 us                                                               | 36.5 us: 1.19x slower                                                    |
| json_dumps           | 12.3 ms                                                               | 14.8 ms: 1.21x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.30 ms: 1.11x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.5 ms: 1.45x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.27x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                               | 25.7 ms: 1.07x faster                                                    |
| genshi_xml     | 60.6 ms                                                               | 58.8 ms: 1.03x faster                                                    |
| mako           | 12.9 ms                                                               | 13.9 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 480 ms: 1.62x faster                                                     |
| async_tree_none            | 624 ms                                                                | 387 ms: 1.61x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 472 ms: 1.57x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 904 ms: 1.55x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 908 ms: 1.55x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 376 ms: 1.53x faster                                                     |
| deepcopy                   | 446 us                                                                | 316 us: 1.41x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 35.4 us: 1.40x faster                                                    |
| comprehensions             | 25.4 us                                                               | 19.4 us: 1.31x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.39 us: 1.21x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 758 ms: 1.20x faster                                                     |
| spectral_norm              | 131 ms                                                                | 109 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 739 ms: 1.20x faster                                                     |
| go                         | 157 ms                                                                | 133 ms: 1.18x faster                                                     |
| generators                 | 43.5 ms                                                               | 37.0 ms: 1.18x faster                                                    |
| async_generators           | 491 ms                                                                | 419 ms: 1.17x faster                                                     |
| pylint                     | 355 ms                                                                | 306 ms: 1.16x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 21.2 ms: 1.16x faster                                                    |
| regex_compile              | 137 ms                                                                | 120 ms: 1.14x faster                                                     |
| raytrace                   | 353 ms                                                                | 312 ms: 1.13x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.37 us: 1.13x faster                                                    |
| logging_simple             | 7.63 us                                                               | 6.81 us: 1.12x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 138 ms: 1.12x faster                                                     |
| scimark_fft                | 418 ms                                                                | 375 ms: 1.12x faster                                                     |
| float                      | 92.1 ms                                                               | 82.9 ms: 1.11x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 77.1 ms: 1.10x faster                                                    |
| html5lib                   | 65.1 ms                                                               | 59.3 ms: 1.10x faster                                                    |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.3 ms: 1.09x faster                                                    |
| xml_etree_generate         | 112 ms                                                                | 103 ms: 1.09x faster                                                     |
| sqlglot_parse              | 1.46 ms                                                               | 1.35 ms: 1.09x faster                                                    |
| sqlglot_transpile          | 1.83 ms                                                               | 1.69 ms: 1.08x faster                                                    |
| logging_silent             | 127 ns                                                                | 118 ns: 1.08x faster                                                     |
| genshi_text                | 27.4 ms                                                               | 25.7 ms: 1.07x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.86 ms: 1.07x faster                                                    |
| sqlalchemy_declarative     | 157 ms                                                                | 148 ms: 1.06x faster                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 5.83 ms: 1.06x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 58.5 ms: 1.06x faster                                                    |
| xml_etree_process          | 79.0 ms                                                               | 74.6 ms: 1.06x faster                                                    |
| mdp                        | 3.41 sec                                                              | 3.23 sec: 1.06x faster                                                   |
| tomli_loads                | 2.59 sec                                                              | 2.46 sec: 1.06x faster                                                   |
| pyflate                    | 559 ms                                                                | 532 ms: 1.05x faster                                                     |
| richards_super             | 58.5 ms                                                               | 55.7 ms: 1.05x faster                                                    |
| scimark_lu                 | 146 ms                                                                | 139 ms: 1.05x faster                                                     |
| 2to3                       | 308 ms                                                                | 294 ms: 1.05x faster                                                     |
| sympy_str                  | 280 ms                                                                | 268 ms: 1.04x faster                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.26 ms: 1.04x faster                                                    |
| unpickle_pure_python       | 260 us                                                                | 252 us: 1.03x faster                                                     |
| genshi_xml                 | 60.6 ms                                                               | 58.8 ms: 1.03x faster                                                    |
| regex_dna                  | 254 ms                                                                | 250 ms: 1.02x faster                                                     |
| pprint_safe_repr           | 916 ms                                                                | 939 ms: 1.03x slower                                                     |
| asyncio_websockets         | 658 ms                                                                | 676 ms: 1.03x slower                                                     |
| xml_etree_parse            | 195 ms                                                                | 209 ms: 1.07x slower                                                     |
| mako                       | 12.9 ms                                                               | 13.9 ms: 1.08x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 4.07 us: 1.08x slower                                                    |
| coverage                   | 87.3 ms                                                               | 94.4 ms: 1.08x slower                                                    |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                                     |
| json                       | 5.54 ms                                                               | 6.15 ms: 1.11x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.30 ms: 1.11x slower                                                    |
| fannkuch                   | 443 ms                                                                | 494 ms: 1.11x slower                                                     |
| telco                      | 8.51 ms                                                               | 9.57 ms: 1.12x slower                                                    |
| json_loads                 | 30.7 us                                                               | 36.5 us: 1.19x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.8 ms: 1.21x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 34.5 ms: 1.22x slower                                                    |
| pidigits                   | 233 ms                                                                | 303 ms: 1.30x slower                                                     |
| python_startup             | 11.4 ms                                                               | 16.5 ms: 1.45x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.82 ms: 1.55x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.70 ms: 1.93x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 7.51 sec: 1064.06x slower                                                |
| Geometric mean             | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (21): chaos, django_template, sympy_integrate, richards, scimark_sor, sqlglot_optimize, nqueens, sqlglot_normalize, coroutines, regex_effbot, docutils, pycparser, pprint_pformat, sympy_expand, typing_runtime_protocols, xml_etree_iterparse, thrift, crypto_pyaes, hexiom, meteor_contest, pickle_pure_python
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20250208-3.14.0a4+-29f8a67-CLANG/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.066x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.08x