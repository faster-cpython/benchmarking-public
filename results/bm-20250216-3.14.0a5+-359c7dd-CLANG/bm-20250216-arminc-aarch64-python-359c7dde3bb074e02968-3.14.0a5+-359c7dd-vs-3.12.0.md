# Results vs. 3.12.0

- fork: python
- ref: 359c7dde3bb074e02968
- machine: linux-aarch64
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.046x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| html5lib       | 65.1 ms                                                               | 60.2 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                             |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 394 ms: 1.58x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 497 ms: 1.56x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 485 ms: 1.53x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 927 ms: 1.52x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 930 ms: 1.51x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 390 ms: 1.48x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 755 ms: 1.21x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 755 ms: 1.17x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.44x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 88.0 ms: 1.05x faster                                                    |
| nbody          | 105 ms                                                                | 116 ms: 1.11x slower                                                     |
| pidigits       | 233 ms                                                                | 305 ms: 1.31x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 129 ms: 1.06x faster                                                     |
| regex_effbot   | 4.64 ms                                                               | 4.81 ms: 1.04x slower                                                    |
| regex_v8       | 28.3 ms                                                               | 34.6 ms: 1.22x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|--------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle           | 18.5 us                                                               | 16.8 us: 1.10x faster                                                    |
| unpickle_list      | 6.17 us                                                               | 5.86 us: 1.05x faster                                                    |
| xml_etree_process  | 79.0 ms                                                               | 75.5 ms: 1.05x faster                                                    |
| tomli_loads        | 2.59 sec                                                              | 2.49 sec: 1.04x faster                                                   |
| pickle_list        | 5.25 us                                                               | 5.65 us: 1.08x slower                                                    |
| pickle_pure_python | 365 us                                                                | 397 us: 1.09x slower                                                     |
| xml_etree_parse    | 195 ms                                                                | 212 ms: 1.09x slower                                                     |
| json_loads         | 30.7 us                                                               | 34.7 us: 1.13x slower                                                    |
| pickle             | 13.4 us                                                               | 15.4 us: 1.15x slower                                                    |
| json_dumps         | 12.3 ms                                                               | 14.5 ms: 1.18x slower                                                    |
| Geometric mean     | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (4): xml_etree_generate, pickle_dict, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.12 ms: 1.09x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.5 ms: 1.45x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.26x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 38.4 ms: 1.06x faster                                                    |
| mako            | 12.9 ms                                                               | 14.2 ms: 1.10x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 394 ms: 1.58x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 497 ms: 1.56x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 485 ms: 1.53x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 927 ms: 1.52x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 930 ms: 1.51x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 390 ms: 1.48x faster                                                     |
| deepcopy                   | 446 us                                                                | 320 us: 1.39x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 36.5 us: 1.36x faster                                                    |
| comprehensions             | 25.4 us                                                               | 19.6 us: 1.29x faster                                                    |
| spectral_norm              | 131 ms                                                                | 107 ms: 1.22x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 755 ms: 1.21x faster                                                     |
| generators                 | 43.5 ms                                                               | 36.6 ms: 1.19x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 755 ms: 1.17x faster                                                     |
| async_generators           | 491 ms                                                                | 425 ms: 1.16x faster                                                     |
| go                         | 157 ms                                                                | 136 ms: 1.15x faster                                                     |
| pathlib                    | 24.5 ms                                                               | 21.4 ms: 1.15x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.60 us: 1.14x faster                                                    |
| pylint                     | 355 ms                                                                | 318 ms: 1.12x faster                                                     |
| raytrace                   | 353 ms                                                                | 318 ms: 1.11x faster                                                     |
| logging_simple             | 7.63 us                                                               | 6.93 us: 1.10x faster                                                    |
| sympy_sum                  | 154 ms                                                                | 140 ms: 1.10x faster                                                     |
| unpickle                   | 18.5 us                                                               | 16.8 us: 1.10x faster                                                    |
| logging_format             | 8.34 us                                                               | 7.60 us: 1.10x faster                                                    |
| scimark_fft                | 418 ms                                                                | 383 ms: 1.09x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 145 ms: 1.09x faster                                                     |
| html5lib                   | 65.1 ms                                                               | 60.2 ms: 1.08x faster                                                    |
| logging_silent             | 127 ns                                                                | 118 ns: 1.08x faster                                                     |
| chaos                      | 71.4 ms                                                               | 67.0 ms: 1.07x faster                                                    |
| regex_compile              | 137 ms                                                                | 129 ms: 1.06x faster                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.7 ms: 1.06x faster                                                    |
| django_template            | 40.7 ms                                                               | 38.4 ms: 1.06x faster                                                    |
| scimark_sor                | 150 ms                                                                | 142 ms: 1.06x faster                                                     |
| deltablue                  | 4.12 ms                                                               | 3.91 ms: 1.05x faster                                                    |
| unpickle_list              | 6.17 us                                                               | 5.86 us: 1.05x faster                                                    |
| float                      | 92.1 ms                                                               | 88.0 ms: 1.05x faster                                                    |
| xml_etree_process          | 79.0 ms                                                               | 75.5 ms: 1.05x faster                                                    |
| sympy_integrate            | 21.6 ms                                                               | 20.7 ms: 1.04x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.49 sec: 1.04x faster                                                   |
| mdp                        | 3.41 sec                                                              | 3.28 sec: 1.04x faster                                                   |
| pyflate                    | 559 ms                                                                | 541 ms: 1.03x faster                                                     |
| pycparser                  | 1.26 sec                                                              | 1.28 sec: 1.02x slower                                                   |
| hexiom                     | 6.98 ms                                                               | 7.13 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.26 sec: 1.03x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 1.95 sec: 1.03x slower                                                   |
| regex_effbot               | 4.64 ms                                                               | 4.81 ms: 1.04x slower                                                    |
| meteor_contest             | 112 ms                                                                | 116 ms: 1.04x slower                                                     |
| pprint_safe_repr           | 916 ms                                                                | 966 ms: 1.05x slower                                                     |
| pickle_list                | 5.25 us                                                               | 5.65 us: 1.08x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 4.08 us: 1.08x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 397 us: 1.09x slower                                                     |
| telco                      | 8.51 ms                                                               | 9.25 ms: 1.09x slower                                                    |
| coverage                   | 87.3 ms                                                               | 94.9 ms: 1.09x slower                                                    |
| xml_etree_parse            | 195 ms                                                                | 212 ms: 1.09x slower                                                     |
| json                       | 5.54 ms                                                               | 6.04 ms: 1.09x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.12 ms: 1.09x slower                                                    |
| mako                       | 12.9 ms                                                               | 14.2 ms: 1.10x slower                                                    |
| nbody                      | 105 ms                                                                | 116 ms: 1.11x slower                                                     |
| fannkuch                   | 443 ms                                                                | 497 ms: 1.12x slower                                                     |
| json_loads                 | 30.7 us                                                               | 34.7 us: 1.13x slower                                                    |
| pickle                     | 13.4 us                                                               | 15.4 us: 1.15x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.5 ms: 1.18x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 34.6 ms: 1.22x slower                                                    |
| pidigits                   | 233 ms                                                                | 305 ms: 1.31x slower                                                     |
| python_startup             | 11.4 ms                                                               | 16.5 ms: 1.45x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.76 ms: 1.54x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.86 ms: 2.01x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 4.43 sec: 627.27x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (29): xml_etree_generate, scimark_monte_carlo, sqlglot_transpile, sympy_str, scimark_lu, sqlglot_parse, bench_thread_pool, dulwich_log, 2to3, genshi_text, scimark_sparse_mat_mult, pickle_dict, coroutines, richards, genshi_xml, richards_super, asyncio_tcp, nqueens, sqlglot_normalize, docutils, unpickle_pure_python, sqlglot_optimize, thrift, asyncio_websockets, sympy_expand, typing_runtime_protocols, regex_dna, crypto_pyaes, xml_etree_iterparse
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (8) of results/bm-20250216-3.14.0a5+-359c7dd-CLANG/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.046x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.08x