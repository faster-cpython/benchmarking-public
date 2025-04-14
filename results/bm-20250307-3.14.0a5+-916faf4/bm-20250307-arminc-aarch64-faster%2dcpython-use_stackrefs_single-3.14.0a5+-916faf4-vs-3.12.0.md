# Results vs. 3.12.0

- fork: faster-cpython
- ref: use_stackrefs_single
- machine: linux-aarch64
- commit hash: 916faf4
- commit date: 2025-03-07
- overall geometric mean: 1.014x faster
- HPT reliability: 70.43%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.06 sec: 1.03x slower                                                             |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                       |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 486 ms: 1.60x faster                                                               |
| async_tree_none            | 624 ms                                                                | 394 ms: 1.58x faster                                                               |
| async_tree_memoization_tg  | 740 ms                                                                | 486 ms: 1.52x faster                                                               |
| async_tree_io              | 1.41 sec                                                              | 933 ms: 1.51x faster                                                               |
| async_tree_io_tg           | 1.40 sec                                                              | 941 ms: 1.49x faster                                                               |
| async_tree_none_tg         | 577 ms                                                                | 393 ms: 1.47x faster                                                               |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 695 ms: 1.31x faster                                                               |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 679 ms: 1.30x faster                                                               |
| Geometric mean             | (ref)                                                                 | 1.47x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 105 ms                                                                | 128 ms: 1.23x slower                                                               |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                                       |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.04 ms: 1.15x faster                                                              |
| regex_v8       | 28.3 ms                                                               | 32.6 ms: 1.15x slower                                                              |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                       |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| xml_etree_generate   | 112 ms                                                                | 118 ms: 1.05x slower                                                               |
| xml_etree_process    | 79.0 ms                                                               | 83.9 ms: 1.06x slower                                                              |
| unpickle_pure_python | 260 us                                                                | 284 us: 1.09x slower                                                               |
| pickle_pure_python   | 365 us                                                                | 405 us: 1.11x slower                                                               |
| json_loads           | 30.7 us                                                               | 34.5 us: 1.13x slower                                                              |
| json_dumps           | 12.3 ms                                                               | 14.6 ms: 1.19x slower                                                              |
| Geometric mean       | (ref)                                                                 | 1.06x slower                                                                       |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_iterparse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.10 ms: 1.09x slower                                                              |
| python_startup         | 11.4 ms                                                               | 16.5 ms: 1.45x slower                                                              |
| Geometric mean         | (ref)                                                                 | 1.26x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 63.4 ms: 1.05x slower                                                              |
| mako           | 12.9 ms                                                               | 14.9 ms: 1.15x slower                                                              |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                                       |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 486 ms: 1.60x faster                                                               |
| async_tree_none            | 624 ms                                                                | 394 ms: 1.58x faster                                                               |
| async_tree_memoization_tg  | 740 ms                                                                | 486 ms: 1.52x faster                                                               |
| async_tree_io              | 1.41 sec                                                              | 933 ms: 1.51x faster                                                               |
| async_tree_io_tg           | 1.40 sec                                                              | 941 ms: 1.49x faster                                                               |
| async_tree_none_tg         | 577 ms                                                                | 393 ms: 1.47x faster                                                               |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 695 ms: 1.31x faster                                                               |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 679 ms: 1.30x faster                                                               |
| deepcopy                   | 446 us                                                                | 347 us: 1.28x faster                                                               |
| deepcopy_memo              | 49.6 us                                                               | 40.4 us: 1.23x faster                                                              |
| generators                 | 43.5 ms                                                               | 37.4 ms: 1.16x faster                                                              |
| regex_effbot               | 4.64 ms                                                               | 4.04 ms: 1.15x faster                                                              |
| comprehensions             | 25.4 us                                                               | 22.4 us: 1.13x faster                                                              |
| deepcopy_reduce            | 4.10 us                                                               | 3.62 us: 1.13x faster                                                              |
| pylint                     | 355 ms                                                                | 326 ms: 1.09x faster                                                               |
| sympy_sum                  | 154 ms                                                                | 144 ms: 1.07x faster                                                               |
| raytrace                   | 353 ms                                                                | 329 ms: 1.07x faster                                                               |
| go                         | 157 ms                                                                | 147 ms: 1.07x faster                                                               |
| pathlib                    | 24.5 ms                                                               | 23.2 ms: 1.06x faster                                                              |
| async_generators           | 491 ms                                                                | 467 ms: 1.05x faster                                                               |
| spectral_norm              | 131 ms                                                                | 125 ms: 1.05x faster                                                               |
| logging_format             | 8.34 us                                                               | 8.03 us: 1.04x faster                                                              |
| docutils                   | 2.98 sec                                                              | 3.06 sec: 1.03x slower                                                             |
| asyncio_websockets         | 658 ms                                                                | 678 ms: 1.03x slower                                                               |
| scimark_fft                | 418 ms                                                                | 435 ms: 1.04x slower                                                               |
| sympy_expand               | 454 ms                                                                | 474 ms: 1.05x slower                                                               |
| genshi_xml                 | 60.6 ms                                                               | 63.4 ms: 1.05x slower                                                              |
| xml_etree_generate         | 112 ms                                                                | 118 ms: 1.05x slower                                                               |
| bench_thread_pool          | 1.31 ms                                                               | 1.38 ms: 1.06x slower                                                              |
| thrift                     | 937 us                                                                | 995 us: 1.06x slower                                                               |
| xml_etree_process          | 79.0 ms                                                               | 83.9 ms: 1.06x slower                                                              |
| pycparser                  | 1.26 sec                                                              | 1.33 sec: 1.06x slower                                                             |
| coroutines                 | 29.0 ms                                                               | 30.9 ms: 1.06x slower                                                              |
| nqueens                    | 99.2 ms                                                               | 107 ms: 1.07x slower                                                               |
| richards                   | 50.9 ms                                                               | 54.8 ms: 1.08x slower                                                              |
| crypto_pyaes               | 86.6 ms                                                               | 93.4 ms: 1.08x slower                                                              |
| richards_super             | 58.5 ms                                                               | 63.1 ms: 1.08x slower                                                              |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.69 ms: 1.08x slower                                                              |
| scimark_lu                 | 146 ms                                                                | 157 ms: 1.08x slower                                                               |
| meteor_contest             | 112 ms                                                                | 121 ms: 1.08x slower                                                               |
| scimark_sor                | 150 ms                                                                | 162 ms: 1.09x slower                                                               |
| pyflate                    | 559 ms                                                                | 607 ms: 1.09x slower                                                               |
| python_startup_no_site     | 8.37 ms                                                               | 9.10 ms: 1.09x slower                                                              |
| pprint_pformat             | 1.88 sec                                                              | 2.05 sec: 1.09x slower                                                             |
| logging_silent             | 127 ns                                                                | 138 ns: 1.09x slower                                                               |
| unpickle_pure_python       | 260 us                                                                | 284 us: 1.09x slower                                                               |
| pprint_safe_repr           | 916 ms                                                                | 1.00 sec: 1.10x slower                                                             |
| json                       | 5.54 ms                                                               | 6.08 ms: 1.10x slower                                                              |
| hexiom                     | 6.98 ms                                                               | 7.68 ms: 1.10x slower                                                              |
| sqlite_synth               | 3.77 us                                                               | 4.16 us: 1.10x slower                                                              |
| pickle_pure_python         | 365 us                                                                | 405 us: 1.11x slower                                                               |
| json_loads                 | 30.7 us                                                               | 34.5 us: 1.13x slower                                                              |
| typing_runtime_protocols   | 181 us                                                                | 203 us: 1.13x slower                                                               |
| regex_v8                   | 28.3 ms                                                               | 32.6 ms: 1.15x slower                                                              |
| telco                      | 8.51 ms                                                               | 9.79 ms: 1.15x slower                                                              |
| mako                       | 12.9 ms                                                               | 14.9 ms: 1.15x slower                                                              |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.17x slower                                                               |
| json_dumps                 | 12.3 ms                                                               | 14.6 ms: 1.19x slower                                                              |
| fannkuch                   | 443 ms                                                                | 528 ms: 1.19x slower                                                               |
| nbody                      | 105 ms                                                                | 128 ms: 1.23x slower                                                               |
| python_startup             | 11.4 ms                                                               | 16.5 ms: 1.45x slower                                                              |
| gc_traversal               | 4.40 ms                                                               | 7.13 ms: 1.62x slower                                                              |
| create_gc_cycles           | 1.92 ms                                                               | 3.60 ms: 1.87x slower                                                              |
| bench_mp_pool              | 7.05 ms                                                               | 4.66 sec: 660.19x slower                                                           |
| Geometric mean             | (ref)                                                                 | 1.08x slower                                                                       |

Benchmark hidden because not significant (25): sqlalchemy_declarative, xml_etree_parse, regex_compile, xml_etree_iterparse, sympy_str, tomli_loads, sqlalchemy_imperative, float, logging_simple, django_template, mdp, 2to3, sqlglot_transpile, pidigits, dulwich_log, html5lib, deltablue, regex_dna, sympy_integrate, sqlglot_optimize, chaos, scimark_monte_carlo, sqlglot_parse, genshi_text, sqlglot_normalize
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20250307-3.14.0a5+-916faf4/bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.014x faster

# HPT report

- Reliability score: 70.43% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x