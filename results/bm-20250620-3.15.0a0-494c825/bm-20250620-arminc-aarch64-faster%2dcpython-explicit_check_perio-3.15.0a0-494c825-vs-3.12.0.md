# Results vs. 3.12.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-aarch64
- commit hash: 494c825
- commit date: 2025-06-20
- overall geometric mean: 1.049x faster
- HPT reliability: 99.78%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 301 ms: 1.02x faster                                                              |
| html5lib       | 65.1 ms                                                               | 62.2 ms: 1.05x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                                      |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 472 ms: 1.65x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 891 ms: 1.58x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 469 ms: 1.58x faster                                                              |
| async_tree_none            | 624 ms                                                                | 398 ms: 1.57x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 925 ms: 1.52x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 380 ms: 1.52x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 667 ms: 1.37x faster                                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 658 ms: 1.34x faster                                                              |
| Geometric mean             | (ref)                                                                 | 1.51x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 87.2 ms: 1.06x faster                                                             |
| pidigits       | 233 ms                                                                | 240 ms: 1.03x slower                                                              |
| nbody          | 105 ms                                                                | 129 ms: 1.23x slower                                                              |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.86 ms: 1.20x faster                                                             |
| regex_dna      | 254 ms                                                                | 219 ms: 1.16x faster                                                              |
| regex_compile  | 137 ms                                                                | 124 ms: 1.11x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.11x faster                                                                      |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 179 ms: 1.09x faster                                                              |
| xml_etree_iterparse  | 150 ms                                                                | 143 ms: 1.05x faster                                                              |
| tomli_loads          | 2.59 sec                                                              | 2.47 sec: 1.05x faster                                                            |
| xml_etree_process    | 79.0 ms                                                               | 81.1 ms: 1.03x slower                                                             |
| unpickle_pure_python | 260 us                                                                | 270 us: 1.04x slower                                                              |
| json_loads           | 30.7 us                                                               | 32.4 us: 1.06x slower                                                             |
| pickle_pure_python   | 365 us                                                                | 412 us: 1.13x slower                                                              |
| json_dumps           | 12.3 ms                                                               | 13.8 ms: 1.13x slower                                                             |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                                      |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.63 ms: 1.03x slower                                                             |
| python_startup         | 11.4 ms                                                               | 15.0 ms: 1.32x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml     | 60.6 ms                                                               | 63.8 ms: 1.05x slower                                                             |
| mako           | 12.9 ms                                                               | 14.4 ms: 1.12x slower                                                             |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                                      |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mdp                        | 3.41 sec                                                              | 1.68 sec: 2.03x faster                                                            |
| async_tree_memoization     | 777 ms                                                                | 472 ms: 1.65x faster                                                              |
| async_tree_io              | 1.41 sec                                                              | 891 ms: 1.58x faster                                                              |
| async_tree_memoization_tg  | 740 ms                                                                | 469 ms: 1.58x faster                                                              |
| async_tree_none            | 624 ms                                                                | 398 ms: 1.57x faster                                                              |
| async_tree_io_tg           | 1.40 sec                                                              | 925 ms: 1.52x faster                                                              |
| async_tree_none_tg         | 577 ms                                                                | 380 ms: 1.52x faster                                                              |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 667 ms: 1.37x faster                                                              |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 658 ms: 1.34x faster                                                              |
| deepcopy                   | 446 us                                                                | 341 us: 1.31x faster                                                              |
| deepcopy_memo              | 49.6 us                                                               | 40.0 us: 1.24x faster                                                             |
| comprehensions             | 25.4 us                                                               | 20.5 us: 1.24x faster                                                             |
| generators                 | 43.5 ms                                                               | 35.1 ms: 1.24x faster                                                             |
| go                         | 157 ms                                                                | 130 ms: 1.21x faster                                                              |
| regex_effbot               | 4.64 ms                                                               | 3.86 ms: 1.20x faster                                                             |
| regex_dna                  | 254 ms                                                                | 219 ms: 1.16x faster                                                              |
| dulwich_log                | 62.0 ms                                                               | 54.9 ms: 1.13x faster                                                             |
| pylint                     | 355 ms                                                                | 318 ms: 1.11x faster                                                              |
| regex_compile              | 137 ms                                                                | 124 ms: 1.11x faster                                                              |
| deepcopy_reduce            | 4.10 us                                                               | 3.70 us: 1.11x faster                                                             |
| xml_etree_parse            | 195 ms                                                                | 179 ms: 1.09x faster                                                              |
| async_generators           | 491 ms                                                                | 456 ms: 1.08x faster                                                              |
| pathlib                    | 24.5 ms                                                               | 22.9 ms: 1.07x faster                                                             |
| spectral_norm              | 131 ms                                                                | 122 ms: 1.07x faster                                                              |
| pyflate                    | 559 ms                                                                | 526 ms: 1.06x faster                                                              |
| scimark_monte_carlo        | 85.1 ms                                                               | 80.3 ms: 1.06x faster                                                             |
| float                      | 92.1 ms                                                               | 87.2 ms: 1.06x faster                                                             |
| xml_etree_iterparse        | 150 ms                                                                | 143 ms: 1.05x faster                                                              |
| raytrace                   | 353 ms                                                                | 336 ms: 1.05x faster                                                              |
| tomli_loads                | 2.59 sec                                                              | 2.47 sec: 1.05x faster                                                            |
| sympy_str                  | 280 ms                                                                | 267 ms: 1.05x faster                                                              |
| html5lib                   | 65.1 ms                                                               | 62.2 ms: 1.05x faster                                                             |
| crypto_pyaes               | 86.6 ms                                                               | 83.3 ms: 1.04x faster                                                             |
| scimark_sor                | 150 ms                                                                | 145 ms: 1.03x faster                                                              |
| 2to3                       | 308 ms                                                                | 301 ms: 1.02x faster                                                              |
| deltablue                  | 4.12 ms                                                               | 4.07 ms: 1.01x faster                                                             |
| hexiom                     | 6.98 ms                                                               | 6.99 ms: 1.00x slower                                                             |
| asyncio_websockets         | 658 ms                                                                | 668 ms: 1.02x slower                                                              |
| logging_format             | 8.34 us                                                               | 8.57 us: 1.03x slower                                                             |
| xml_etree_process          | 79.0 ms                                                               | 81.1 ms: 1.03x slower                                                             |
| python_startup_no_site     | 8.37 ms                                                               | 8.63 ms: 1.03x slower                                                             |
| pidigits                   | 233 ms                                                                | 240 ms: 1.03x slower                                                              |
| scimark_fft                | 418 ms                                                                | 433 ms: 1.04x slower                                                              |
| coroutines                 | 29.0 ms                                                               | 30.1 ms: 1.04x slower                                                             |
| sympy_expand               | 454 ms                                                                | 471 ms: 1.04x slower                                                              |
| logging_simple             | 7.63 us                                                               | 7.93 us: 1.04x slower                                                             |
| unpickle_pure_python       | 260 us                                                                | 270 us: 1.04x slower                                                              |
| json                       | 5.54 ms                                                               | 5.77 ms: 1.04x slower                                                             |
| scimark_lu                 | 146 ms                                                                | 152 ms: 1.05x slower                                                              |
| genshi_xml                 | 60.6 ms                                                               | 63.8 ms: 1.05x slower                                                             |
| json_loads                 | 30.7 us                                                               | 32.4 us: 1.06x slower                                                             |
| richards                   | 50.9 ms                                                               | 54.8 ms: 1.08x slower                                                             |
| richards_super             | 58.5 ms                                                               | 62.9 ms: 1.08x slower                                                             |
| thrift                     | 937 us                                                                | 1.01 ms: 1.08x slower                                                             |
| fannkuch                   | 443 ms                                                                | 485 ms: 1.09x slower                                                              |
| typing_runtime_protocols   | 181 us                                                                | 200 us: 1.11x slower                                                              |
| telco                      | 8.51 ms                                                               | 9.50 ms: 1.12x slower                                                             |
| mako                       | 12.9 ms                                                               | 14.4 ms: 1.12x slower                                                             |
| pprint_pformat             | 1.88 sec                                                              | 2.11 sec: 1.12x slower                                                            |
| pprint_safe_repr           | 916 ms                                                                | 1.03 sec: 1.12x slower                                                            |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.95 ms: 1.12x slower                                                             |
| pickle_pure_python         | 365 us                                                                | 412 us: 1.13x slower                                                              |
| json_dumps                 | 12.3 ms                                                               | 13.8 ms: 1.13x slower                                                             |
| coverage                   | 87.3 ms                                                               | 102 ms: 1.16x slower                                                              |
| nbody                      | 105 ms                                                                | 129 ms: 1.23x slower                                                              |
| python_startup             | 11.4 ms                                                               | 15.0 ms: 1.32x slower                                                             |
| gc_traversal               | 4.40 ms                                                               | 6.72 ms: 1.53x slower                                                             |
| create_gc_cycles           | 1.92 ms                                                               | 3.75 ms: 1.96x slower                                                             |
| logging_silent             | 127 ns                                                                | 643 ns: 5.07x slower                                                              |
| Geometric mean             | (ref)                                                                 | 1.02x faster                                                                      |

Benchmark hidden because not significant (12): sympy_integrate, sympy_sum, chaos, docutils, pycparser, django_template, sqlite_synth, nqueens, regex_v8, genshi_text, meteor_contest, xml_etree_generate
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250620-3.15.0a0-494c825/bm-20250620-arminc-aarch64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.049x faster

# HPT report

- Reliability score: 99.78% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x