# Results vs. 3.12.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: linux-aarch64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.037x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (3): 2to3, docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 402 ms: 1.55x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 481 ms: 1.54x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 505 ms: 1.54x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 924 ms: 1.53x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 931 ms: 1.51x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 395 ms: 1.46x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 671 ms: 1.32x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 694 ms: 1.31x faster                                                     |
| Geometric mean             | (ref)                                                                 | 1.47x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 105 ms                                                                | 123 ms: 1.17x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                             |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.06 ms: 1.14x faster                                                    |
| regex_compile  | 137 ms                                                                | 127 ms: 1.08x faster                                                     |
| regex_dna      | 254 ms                                                                | 247 ms: 1.03x faster                                                     |
| regex_v8       | 28.3 ms                                                               | 33.4 ms: 1.18x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|--------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse    | 195 ms                                                                | 182 ms: 1.07x faster                                                     |
| pickle_dict        | 37.3 us                                                               | 40.2 us: 1.08x slower                                                    |
| unpickle_list      | 6.17 us                                                               | 6.68 us: 1.08x slower                                                    |
| pickle_pure_python | 365 us                                                                | 398 us: 1.09x slower                                                     |
| json_loads         | 30.7 us                                                               | 34.5 us: 1.12x slower                                                    |
| pickle_list        | 5.25 us                                                               | 6.13 us: 1.17x slower                                                    |
| json_dumps         | 12.3 ms                                                               | 14.7 ms: 1.20x slower                                                    |
| pickle             | 13.4 us                                                               | 16.5 us: 1.23x slower                                                    |
| Geometric mean     | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (6): xml_etree_iterparse, tomli_loads, unpickle, unpickle_pure_python, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.05 ms: 1.08x slower                                                    |
| python_startup         | 11.4 ms                                                               | 16.4 ms: 1.44x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.25x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako           | 12.9 ms                                                               | 14.5 ms: 1.12x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (3): django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 402 ms: 1.55x faster                                                     |
| async_tree_memoization_tg  | 740 ms                                                                | 481 ms: 1.54x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 505 ms: 1.54x faster                                                     |
| async_tree_io              | 1.41 sec                                                              | 924 ms: 1.53x faster                                                     |
| async_tree_io_tg           | 1.40 sec                                                              | 931 ms: 1.51x faster                                                     |
| async_tree_none_tg         | 577 ms                                                                | 395 ms: 1.46x faster                                                     |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 671 ms: 1.32x faster                                                     |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 694 ms: 1.31x faster                                                     |
| deepcopy                   | 446 us                                                                | 344 us: 1.29x faster                                                     |
| comprehensions             | 25.4 us                                                               | 21.3 us: 1.19x faster                                                    |
| deepcopy_memo              | 49.6 us                                                               | 41.7 us: 1.19x faster                                                    |
| pathlib                    | 24.5 ms                                                               | 21.1 ms: 1.16x faster                                                    |
| generators                 | 43.5 ms                                                               | 37.8 ms: 1.15x faster                                                    |
| regex_effbot               | 4.64 ms                                                               | 4.06 ms: 1.14x faster                                                    |
| raytrace                   | 353 ms                                                                | 315 ms: 1.12x faster                                                     |
| pylint                     | 355 ms                                                                | 322 ms: 1.10x faster                                                     |
| go                         | 157 ms                                                                | 144 ms: 1.09x faster                                                     |
| sqlalchemy_imperative      | 16.7 ms                                                               | 15.3 ms: 1.09x faster                                                    |
| async_generators           | 491 ms                                                                | 450 ms: 1.09x faster                                                     |
| regex_compile              | 137 ms                                                                | 127 ms: 1.08x faster                                                     |
| xml_etree_parse            | 195 ms                                                                | 182 ms: 1.07x faster                                                     |
| deltablue                  | 4.12 ms                                                               | 3.86 ms: 1.07x faster                                                    |
| spectral_norm              | 131 ms                                                                | 123 ms: 1.06x faster                                                     |
| sqlalchemy_declarative     | 157 ms                                                                | 148 ms: 1.06x faster                                                     |
| scimark_lu                 | 146 ms                                                                | 139 ms: 1.05x faster                                                     |
| chaos                      | 71.4 ms                                                               | 68.4 ms: 1.04x faster                                                    |
| sympy_str                  | 280 ms                                                                | 268 ms: 1.04x faster                                                     |
| asyncio_tcp                | 566 ms                                                                | 546 ms: 1.04x faster                                                     |
| regex_dna                  | 254 ms                                                                | 247 ms: 1.03x faster                                                     |
| bench_thread_pool          | 1.31 ms                                                               | 1.29 ms: 1.02x faster                                                    |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.26 sec: 1.03x slower                                                   |
| thrift                     | 937 us                                                                | 982 us: 1.05x slower                                                     |
| sympy_expand               | 454 ms                                                                | 476 ms: 1.05x slower                                                     |
| hexiom                     | 6.98 ms                                                               | 7.38 ms: 1.06x slower                                                    |
| pprint_pformat             | 1.88 sec                                                              | 1.99 sec: 1.06x slower                                                   |
| typing_runtime_protocols   | 181 us                                                                | 193 us: 1.07x slower                                                     |
| logging_silent             | 127 ns                                                                | 136 ns: 1.07x slower                                                     |
| fannkuch                   | 443 ms                                                                | 477 ms: 1.08x slower                                                     |
| pickle_dict                | 37.3 us                                                               | 40.2 us: 1.08x slower                                                    |
| pprint_safe_repr           | 916 ms                                                                | 988 ms: 1.08x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 9.05 ms: 1.08x slower                                                    |
| sqlite_synth               | 3.77 us                                                               | 4.08 us: 1.08x slower                                                    |
| unpickle_list              | 6.17 us                                                               | 6.68 us: 1.08x slower                                                    |
| json                       | 5.54 ms                                                               | 6.03 ms: 1.09x slower                                                    |
| pickle_pure_python         | 365 us                                                                | 398 us: 1.09x slower                                                     |
| telco                      | 8.51 ms                                                               | 9.52 ms: 1.12x slower                                                    |
| mako                       | 12.9 ms                                                               | 14.5 ms: 1.12x slower                                                    |
| json_loads                 | 30.7 us                                                               | 34.5 us: 1.12x slower                                                    |
| coverage                   | 87.3 ms                                                               | 100 ms: 1.15x slower                                                     |
| pickle_list                | 5.25 us                                                               | 6.13 us: 1.17x slower                                                    |
| nbody                      | 105 ms                                                                | 123 ms: 1.17x slower                                                     |
| regex_v8                   | 28.3 ms                                                               | 33.4 ms: 1.18x slower                                                    |
| json_dumps                 | 12.3 ms                                                               | 14.7 ms: 1.20x slower                                                    |
| pickle                     | 13.4 us                                                               | 16.5 us: 1.23x slower                                                    |
| python_startup             | 11.4 ms                                                               | 16.4 ms: 1.44x slower                                                    |
| gc_traversal               | 4.40 ms                                                               | 6.50 ms: 1.48x slower                                                    |
| create_gc_cycles           | 1.92 ms                                                               | 3.65 ms: 1.90x slower                                                    |
| bench_mp_pool              | 7.05 ms                                                               | 5.94 sec: 842.62x slower                                                 |
| Geometric mean             | (ref)                                                                 | 1.06x slower                                                             |

Benchmark hidden because not significant (38): deepcopy_reduce, float, logging_format, logging_simple, sympy_sum, xml_etree_iterparse, dulwich_log, 2to3, django_template, sqlglot_parse, genshi_text, docutils, sympy_integrate, mdp, tomli_loads, scimark_fft, sqlglot_transpile, sqlglot_optimize, unpickle, unpickle_pure_python, scimark_sparse_mat_mult, pycparser, html5lib, nqueens, scimark_sor, coroutines, pyflate, richards_super, xml_etree_process, asyncio_websockets, pidigits, crypto_pyaes, meteor_contest, scimark_monte_carlo, genshi_xml, xml_etree_generate, richards, sqlglot_normalize
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (8) of results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.037x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x