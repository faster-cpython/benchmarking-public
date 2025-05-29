# Results vs. 3.12.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: linux-aarch64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.059x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 300 ms: 1.03x faster                                                     |
| docutils       | 2.98 sec                                                              | 3.01 sec: 1.01x slower                                                   |
| html5lib       | 65.1 ms                                                               | 59.9 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 475 ms: 1.64x faster                                                     |
| async_tree_none            | 624 ms                                                                | 383 ms: 1.63x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 467 ms: 1.58x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 904 ms: 1.56x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 912 ms: 1.54x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 377 ms: 1.53x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 745 ms: 1.22x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 735 ms: 1.20x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.48x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 86.3 ms: 1.07x faster                                                    |
| nbody          | 105 ms                                                                | 118 ms: 1.12x slower                                                     |
| pidigits       | 233 ms                                                                | 306 ms: 1.31x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                                | 123 ms: 1.12x faster                                                     |
| regex_effbot   | 4.64 ms                                                               | 4.35 ms: 1.07x faster                                                    |
| regex_dna      | 254 ms                                                                | 250 ms: 1.01x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 34.2 ms: 1.21x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|--------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle           | 18.5 us                                                               | 16.6 us: 1.11x faster                                                    |
| unpickle_list      | 6.17 us                                                               | 5.83 us: 1.06x faster                                                    |
| xml_etree_process  | 79.0 ms                                                               | 74.8 ms: 1.06x faster                                                    |
| tomli_loads        | 2.59 sec                                                              | 2.47 sec: 1.05x faster                                                   |
| pickle_list        | 5.25 us                                                               | 5.52 us: 1.05x slower                                                    |
| pickle_pure_python | 365 us                                                                | 385 us: 1.06x slower                                                     |
| xml_etree_parse    | 195 ms                                                                | 212 ms: 1.09x slower                                                     |
| json_loads         | 30.7 us                                                               | 35.4 us: 1.15x slower                                                    |
| pickle             | 13.4 us                                                               | 15.8 us: 1.17x slower                                                    |
| json_dumps         | 12.3 ms                                                               | 14.5 ms: 1.18x slower                                                    |
| Geometric mean     | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (4): xml_etree_generate, unpickle_pure_python, pickle_dict, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.09 ms: 1.09x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.4 ms: 1.44x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.25x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 38.4 ms: 1.06x faster                                                    |
| mako            | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                             |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 475 ms: 1.64x faster                                                     |
| async_tree_none            | 624 ms                                                                | 383 ms: 1.63x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 467 ms: 1.58x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 904 ms: 1.56x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 912 ms: 1.54x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 377 ms: 1.53x faster                                                     |
| deepcopy                   | 446 us                                                                | 318 us: 1.40x faster                                                     |
| deepcopy_memo              | 49.6 us                                                               | 35.6 us: 1.39x faster                                                    |
| comprehensions             | 25.4 us                                                               | 19.5 us: 1.30x faster                                                    |
| deepcopy_reduce            | 4.10 us                                                               | 3.28 us: 1.25x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 745 ms: 1.22x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 735 ms: 1.20x faster                                                     |
| async_generators           | 491 ms                                                                | 415 ms: 1.18x faster                                                     |
| spectral_norm              | 131 ms                                                                | 111 ms: 1.18x faster                                                     |
| generators                 | 43.5 ms                                                               | 37.5 ms: 1.16x faster                                                    |
| raytrace                   | 353 ms                                                                | 308 ms: 1.15x faster                                                     |
| go                         | 157 ms                                                                | 138 ms: 1.14x faster                                                     |
| pylint                     | 355 ms                                                                | 311 ms: 1.14x faster                                                     |
| logging_silent             | 127 ns                                                                | 112 ns: 1.13x faster                                                     |
| regex_compile              | 137 ms                                                                | 123 ms: 1.12x faster                                                     |
| sympy_sum                  | 154 ms                                                                | 139 ms: 1.11x faster                                                     |
| logging_format             | 8.34 us                                                               | 7.49 us: 1.11x faster                                                    |
| unpickle                   | 18.5 us                                                               | 16.6 us: 1.11x faster                                                    |
| scimark_monte_carlo        | 85.1 ms                                                               | 76.8 ms: 1.11x faster                                                    |
| logging_simple             | 7.63 us                                                               | 6.94 us: 1.10x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 22.4 ms: 1.10x faster                                                    |
| sqlalchemy_declarative     | 157 ms                                                                | 145 ms: 1.09x faster                                                     |
| html5lib                   | 65.1 ms                                                               | 59.9 ms: 1.09x faster                                                    |
| scimark_fft                | 418 ms                                                                | 386 ms: 1.08x faster                                                     |
| sqlglot_transpile          | 1.83 ms                                                               | 1.69 ms: 1.08x faster                                                    |
| chaos                      | 71.4 ms                                                               | 66.8 ms: 1.07x faster                                                    |
| float                      | 92.1 ms                                                               | 86.3 ms: 1.07x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.35 ms: 1.07x faster                                                    |
| richards_super             | 58.5 ms                                                               | 55.0 ms: 1.06x faster                                                    |
| pyflate                    | 559 ms                                                                | 527 ms: 1.06x faster                                                     |
| django_template            | 40.7 ms                                                               | 38.4 ms: 1.06x faster                                                    |
| unpickle_list              | 6.17 us                                                               | 5.83 us: 1.06x faster                                                    |
| sqlglot_parse              | 1.46 ms                                                               | 1.38 ms: 1.06x faster                                                    |
| dulwich_log                | 62.0 ms                                                               | 58.7 ms: 1.06x faster                                                    |
| xml_etree_process          | 79.0 ms                                                               | 74.8 ms: 1.06x faster                                                    |
| deltablue                  | 4.12 ms                                                               | 3.91 ms: 1.05x faster                                                    |
| richards                   | 50.9 ms                                                               | 48.5 ms: 1.05x faster                                                    |
| tomli_loads                | 2.59 sec                                                              | 2.47 sec: 1.05x faster                                                   |
| mdp                        | 3.41 sec                                                              | 3.27 sec: 1.04x faster                                                   |
| bench_thread_pool          | 1.31 ms                                                               | 1.27 ms: 1.03x faster                                                    |
| 2to3                       | 308 ms                                                                | 300 ms: 1.03x faster                                                     |
| regex_dna                  | 254 ms                                                                | 250 ms: 1.01x faster                                                     |
| hexiom                     | 6.98 ms                                                               | 7.04 ms: 1.01x slower                                                    |
| docutils                   | 2.98 sec                                                              | 3.01 sec: 1.01x slower                                                   |
| pprint_pformat             | 1.88 sec                                                              | 1.92 sec: 1.02x slower                                                   |
| asyncio_websockets         | 658 ms                                                                | 672 ms: 1.02x slower                                                     |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.28 sec: 1.05x slower                                                   |
| pickle_list                | 5.25 us                                                               | 5.52 us: 1.05x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 385 us: 1.06x slower                                                     |
| mako                       | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                                    |
| meteor_contest             | 112 ms                                                                | 120 ms: 1.07x slower                                                     |
| coverage                   | 87.3 ms                                                               | 94.0 ms: 1.08x slower                                                    |
| telco                      | 8.51 ms                                                               | 9.22 ms: 1.08x slower                                                    |
| python_startup_no_site     | 8.37 ms                                                               | 9.09 ms: 1.09x slower                                                    |
| xml_etree_parse            | 195 ms                                                                | 212 ms: 1.09x slower                                                     |
| sqlite_synth               | 3.77 us                                                               | 4.14 us: 1.10x slower                                                    |
| json                       | 5.54 ms                                                               | 6.11 ms: 1.10x slower                                                    |
| fannkuch                   | 443 ms                                                                | 492 ms: 1.11x slower                                                     |
| nbody                      | 105 ms                                                                | 118 ms: 1.12x slower                                                     |
| json_loads                 | 30.7 us                                                               | 35.4 us: 1.15x slower                                                    |
| pickle                     | 13.4 us                                                               | 15.8 us: 1.17x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.5 ms: 1.18x slower                                                    |
| regex_v8                   | 28.3 ms                                                               | 34.2 ms: 1.21x slower                                                    |
| pidigits                   | 233 ms                                                                | 306 ms: 1.31x slower                                                     |
| python_startup             | 11.4 ms                                                               | 16.4 ms: 1.44x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.87 ms: 1.56x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.88 ms: 2.02x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 6.84 sec: 970.28x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (23): sympy_integrate, scimark_sor, sqlalchemy_imperative, sympy_str, genshi_text, xml_etree_generate, unpickle_pure_python, coroutines, pickle_dict, scimark_sparse_mat_mult, genshi_xml, nqueens, scimark_lu, sqlglot_normalize, thrift, sqlglot_optimize, crypto_pyaes, asyncio_tcp, sympy_expand, pycparser, pprint_safe_repr, xml_etree_iterparse, typing_runtime_protocols
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (8) of results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.059x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.08x