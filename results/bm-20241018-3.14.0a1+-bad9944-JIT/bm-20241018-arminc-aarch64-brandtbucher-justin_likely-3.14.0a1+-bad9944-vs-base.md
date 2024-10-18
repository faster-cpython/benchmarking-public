# Results vs. base

- fork: brandtbucher
- ref: justin_likely
- machine: linux-aarch64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.00x slower
- HPT reliability: 83.38%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 3.61 sec                                                                 | 3.58 sec: 1.01x faster                                                  |
| tornado_http   | 154 ms                                                                   | 147 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|---------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg | 545 ms                                                                   | 536 ms: 1.02x faster                                                    |
| asyncio_tcp               | 630 ms                                                                   | 621 ms: 1.02x faster                                                    |
| async_tree_none           | 461 ms                                                                   | 457 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl           | 2.25 sec                                                                 | 2.26 sec: 1.00x slower                                                  |
| async_generators          | 507 ms                                                                   | 515 ms: 1.02x slower                                                    |
| Geometric mean            | (ref)                                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_io, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                                   | 115 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 178 ms                                                                   | 179 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (3): regex_v8, regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|---------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse | 152 ms                                                                   | 150 ms: 1.01x faster                                                    |
| pickle              | 14.1 us                                                                  | 13.9 us: 1.01x faster                                                   |
| xml_etree_generate  | 111 ms                                                                   | 112 ms: 1.01x slower                                                    |
| unpickle            | 18.9 us                                                                  | 19.6 us: 1.04x slower                                                   |
| Geometric mean      | (ref)                                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (10): unpickle_list, pickle_list, tomli_loads, json_loads, xml_etree_process, pickle_dict, pickle_pure_python, unpickle_pure_python, xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.9 ms                                                                  | 14.5 ms: 1.02x faster                                                   |
| python_startup_no_site | 8.81 ms                                                                  | 8.73 ms: 1.01x faster                                                   |
| Geometric mean         | (ref)                                                                    | 1.01x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 51.6 ms                                                                  | 52.6 ms: 1.02x slower                                                   |
| mako            | 13.1 ms                                                                  | 13.6 ms: 1.03x slower                                                   |
| Geometric mean  | (ref)                                                                    | 1.02x slower                                                            |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|---------------------------|:------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tornado_http              | 154 ms                                                                   | 147 ms: 1.05x faster                                                    |
| deepcopy_reduce           | 4.07 us                                                                  | 3.98 us: 1.02x faster                                                   |
| python_startup            | 14.9 ms                                                                  | 14.5 ms: 1.02x faster                                                   |
| async_tree_memoization_tg | 545 ms                                                                   | 536 ms: 1.02x faster                                                    |
| asyncio_tcp               | 630 ms                                                                   | 621 ms: 1.02x faster                                                    |
| xml_etree_iterparse       | 152 ms                                                                   | 150 ms: 1.01x faster                                                    |
| telco                     | 9.75 ms                                                                  | 9.64 ms: 1.01x faster                                                   |
| pickle                    | 14.1 us                                                                  | 13.9 us: 1.01x faster                                                   |
| docutils                  | 3.61 sec                                                                 | 3.58 sec: 1.01x faster                                                  |
| python_startup_no_site    | 8.81 ms                                                                  | 8.73 ms: 1.01x faster                                                   |
| scimark_lu                | 149 ms                                                                   | 148 ms: 1.01x faster                                                    |
| async_tree_none           | 461 ms                                                                   | 457 ms: 1.01x faster                                                    |
| sympy_sum                 | 216 ms                                                                   | 214 ms: 1.01x faster                                                    |
| scimark_monte_carlo       | 89.3 ms                                                                  | 88.7 ms: 1.01x faster                                                   |
| pathlib                   | 21.7 ms                                                                  | 21.8 ms: 1.00x slower                                                   |
| asyncio_tcp_ssl           | 2.25 sec                                                                 | 2.26 sec: 1.00x slower                                                  |
| comprehensions            | 24.7 us                                                                  | 24.8 us: 1.00x slower                                                   |
| generators                | 58.8 ms                                                                  | 59.1 ms: 1.01x slower                                                   |
| xml_etree_generate        | 111 ms                                                                   | 112 ms: 1.01x slower                                                    |
| regex_compile             | 178 ms                                                                   | 179 ms: 1.01x slower                                                    |
| nbody                     | 114 ms                                                                   | 115 ms: 1.01x slower                                                    |
| sqlglot_normalize         | 157 ms                                                                   | 159 ms: 1.01x slower                                                    |
| sqlglot_optimize          | 82.1 ms                                                                  | 83.1 ms: 1.01x slower                                                   |
| fannkuch                  | 505 ms                                                                   | 512 ms: 1.01x slower                                                    |
| meteor_contest            | 122 ms                                                                   | 124 ms: 1.01x slower                                                    |
| async_generators          | 507 ms                                                                   | 515 ms: 1.02x slower                                                    |
| richards_super            | 71.0 ms                                                                  | 72.2 ms: 1.02x slower                                                   |
| chaos                     | 84.2 ms                                                                  | 85.7 ms: 1.02x slower                                                   |
| django_template           | 51.6 ms                                                                  | 52.6 ms: 1.02x slower                                                   |
| pprint_safe_repr          | 1.21 sec                                                                 | 1.23 sec: 1.02x slower                                                  |
| scimark_sparse_mat_mult   | 7.07 ms                                                                  | 7.23 ms: 1.02x slower                                                   |
| hexiom                    | 10.1 ms                                                                  | 10.3 ms: 1.02x slower                                                   |
| dulwich_log               | 78.2 ms                                                                  | 79.9 ms: 1.02x slower                                                   |
| pprint_pformat            | 2.56 sec                                                                 | 2.62 sec: 1.02x slower                                                  |
| mako                      | 13.1 ms                                                                  | 13.6 ms: 1.03x slower                                                   |
| unpickle                  | 18.9 us                                                                  | 19.6 us: 1.04x slower                                                   |
| pyflate                   | 617 ms                                                                   | 642 ms: 1.04x slower                                                    |
| sqlite_synth              | 3.81 us                                                                  | 4.00 us: 1.05x slower                                                   |
| Geometric mean            | (ref)                                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (60): sqlglot_parse, async_tree_memoization, coverage, sympy_str, regex_v8, logging_simple, logging_format, deepcopy, async_tree_cpu_io_mixed, sympy_expand, gc_traversal, unpickle_list, sympy_integrate, thrift, typing_runtime_protocols, async_tree_none_tg, pickle_list, 2to3, html5lib, spectral_norm, bench_thread_pool, tomli_loads, json_loads, mdp, go, logging_silent, sphinx, asyncio_websockets, xml_etree_process, genshi_text, pickle_dict, crypto_pyaes, async_tree_cpu_io_mixed_tg, unpack_sequence, float, scimark_fft, async_tree_io_tg, pycparser, json, pidigits, nqueens, deltablue, deepcopy_memo, pickle_pure_python, regex_effbot, async_tree_io, scimark_sor, bpe_tokeniser, raytrace, unpickle_pure_python, coroutines, richards, regex_dna, genshi_xml, pylint, xml_etree_parse, create_gc_cycles, sqlglot_transpile, json_dumps, bench_mp_pool

# HPT report

- Reliability score: 83.38% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x