# Results vs. base

- fork: brandtbucher
- ref: justin_compact
- machine: linux-aarch64
- commit hash: 34e6994
- commit date: 2024-06-20
- overall geometric mean: 1.00x faster
- HPT reliability: 99.63%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240618-arminc-aarch64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 359 ms                                                                  | 370 ms: 1.03x slower                                                    |
| docutils       | 3.50 sec                                                                | 3.58 sec: 1.02x slower                                                  |
| tornado_http   | 139 ms                                                                  | 147 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                                   | 1.03x slower                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240618-arminc-aarch64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|---------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg | 625 ms                                                                  | 605 ms: 1.03x faster                                                    |
| async_tree_none           | 512 ms                                                                  | 500 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed   | 814 ms                                                                  | 799 ms: 1.02x faster                                                    |
| Geometric mean            | (ref)                                                                   | 1.02x faster                                                            |

Benchmark hidden because not significant (5): async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240618-arminc-aarch64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 89.6 ms                                                                 | 88.2 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240618-arminc-aarch64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 251 ms                                                                  | 248 ms: 1.01x faster                                                    |
| regex_compile  | 172 ms                                                                  | 175 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                            |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark      | bm-20240618-arminc-aarch64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_list    | 5.27 us                                                                 | 5.28 us: 1.00x slower                                                   |
| json_loads     | 32.7 us                                                                 | 33.2 us: 1.01x slower                                                   |
| pickle         | 13.6 us                                                                 | 13.8 us: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                            |

Benchmark hidden because not significant (11): xml_etree_process, unpickle_list, tomli_loads, unpickle_pure_python, unpickle, json_dumps, xml_etree_iterparse, xml_etree_generate, pickle_pure_python, pickle_dict, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240618-arminc-aarch64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 11.0 ms                                                                 | 11.2 ms: 1.02x slower                                                   |
| python_startup         | 15.4 ms                                                                 | 15.8 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                                   | 1.02x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240618-arminc-aarch64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 51.2 ms                                                                 | 49.0 ms: 1.05x faster                                                   |
| genshi_xml      | 81.8 ms                                                                 | 79.0 ms: 1.04x faster                                                   |
| genshi_text     | 34.5 ms                                                                 | 33.5 ms: 1.03x faster                                                   |
| Geometric mean  | (ref)                                                                   | 1.03x faster                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                 | bm-20240618-arminc-aarch64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|---------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| bench_mp_pool             | 8.17 ms                                                                 | 7.50 ms: 1.09x faster                                                   |
| gc_traversal              | 5.28 ms                                                                 | 5.01 ms: 1.05x faster                                                   |
| asyncio_tcp               | 641 ms                                                                  | 611 ms: 1.05x faster                                                    |
| typing_runtime_protocols  | 216 us                                                                  | 206 us: 1.05x faster                                                    |
| django_template           | 51.2 ms                                                                 | 49.0 ms: 1.05x faster                                                   |
| telco                     | 10.4 ms                                                                 | 9.97 ms: 1.04x faster                                                   |
| genshi_xml                | 81.8 ms                                                                 | 79.0 ms: 1.04x faster                                                   |
| async_tree_memoization_tg | 625 ms                                                                  | 605 ms: 1.03x faster                                                    |
| pyflate                   | 611 ms                                                                  | 592 ms: 1.03x faster                                                    |
| genshi_text               | 34.5 ms                                                                 | 33.5 ms: 1.03x faster                                                   |
| sqlite_synth              | 3.91 us                                                                 | 3.80 us: 1.03x faster                                                   |
| deepcopy_reduce           | 4.14 us                                                                 | 4.03 us: 1.03x faster                                                   |
| scimark_monte_carlo       | 87.1 ms                                                                 | 85.1 ms: 1.02x faster                                                   |
| pprint_safe_repr          | 1.13 sec                                                                | 1.10 sec: 1.02x faster                                                  |
| async_tree_none           | 512 ms                                                                  | 500 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed   | 814 ms                                                                  | 799 ms: 1.02x faster                                                    |
| richards                  | 55.9 ms                                                                 | 54.8 ms: 1.02x faster                                                   |
| logging_silent            | 140 ns                                                                  | 138 ns: 1.02x faster                                                    |
| richards_super            | 62.5 ms                                                                 | 61.5 ms: 1.02x faster                                                   |
| chaos                     | 88.1 ms                                                                 | 86.7 ms: 1.02x faster                                                   |
| float                     | 89.6 ms                                                                 | 88.2 ms: 1.02x faster                                                   |
| async_generators          | 515 ms                                                                  | 507 ms: 1.01x faster                                                    |
| pprint_pformat            | 2.33 sec                                                                | 2.30 sec: 1.01x faster                                                  |
| crypto_pyaes              | 86.7 ms                                                                 | 85.5 ms: 1.01x faster                                                   |
| deepcopy                  | 383 us                                                                  | 378 us: 1.01x faster                                                    |
| logging_format            | 7.99 us                                                                 | 7.88 us: 1.01x faster                                                   |
| scimark_fft               | 462 ms                                                                  | 456 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl           | 2.28 sec                                                                | 2.25 sec: 1.01x faster                                                  |
| scimark_lu                | 183 ms                                                                  | 181 ms: 1.01x faster                                                    |
| go                        | 178 ms                                                                  | 176 ms: 1.01x faster                                                    |
| regex_dna                 | 251 ms                                                                  | 248 ms: 1.01x faster                                                    |
| bench_thread_pool         | 1.34 ms                                                                 | 1.33 ms: 1.01x faster                                                   |
| scimark_sparse_mat_mult   | 6.95 ms                                                                 | 6.89 ms: 1.01x faster                                                   |
| deltablue                 | 4.45 ms                                                                 | 4.41 ms: 1.01x faster                                                   |
| bpe_tokeniser             | 6.07 sec                                                                | 6.03 sec: 1.01x faster                                                  |
| mdp                       | 3.46 sec                                                                | 3.44 sec: 1.01x faster                                                  |
| sqlglot_transpile         | 2.00 ms                                                                 | 2.01 ms: 1.00x slower                                                   |
| pickle_list               | 5.27 us                                                                 | 5.28 us: 1.00x slower                                                   |
| sympy_integrate           | 26.0 ms                                                                 | 26.2 ms: 1.01x slower                                                   |
| json_loads                | 32.7 us                                                                 | 33.2 us: 1.01x slower                                                   |
| python_startup_no_site    | 11.0 ms                                                                 | 11.2 ms: 1.02x slower                                                   |
| pickle                    | 13.6 us                                                                 | 13.8 us: 1.02x slower                                                   |
| regex_compile             | 172 ms                                                                  | 175 ms: 1.02x slower                                                    |
| fannkuch                  | 459 ms                                                                  | 468 ms: 1.02x slower                                                    |
| python_startup            | 15.4 ms                                                                 | 15.8 ms: 1.02x slower                                                   |
| docutils                  | 3.50 sec                                                                | 3.58 sec: 1.02x slower                                                  |
| meteor_contest            | 116 ms                                                                  | 119 ms: 1.03x slower                                                    |
| nqueens                   | 118 ms                                                                  | 122 ms: 1.03x slower                                                    |
| 2to3                      | 359 ms                                                                  | 370 ms: 1.03x slower                                                    |
| sympy_str                 | 321 ms                                                                  | 332 ms: 1.03x slower                                                    |
| sympy_sum                 | 182 ms                                                                  | 188 ms: 1.04x slower                                                    |
| dulwich_log               | 72.3 ms                                                                 | 76.2 ms: 1.05x slower                                                   |
| tornado_http              | 139 ms                                                                  | 147 ms: 1.06x slower                                                    |
| Geometric mean            | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (44): xml_etree_process, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_none_tg, unpickle_list, regex_effbot, comprehensions, sqlglot_normalize, spectral_norm, async_tree_cpu_io_mixed_tg, html5lib, tomli_loads, scimark_sor, unpickle_pure_python, asyncio_websockets, coroutines, pidigits, unpickle, dask, json_dumps, generators, raytrace, logging_simple, xml_etree_iterparse, mako, regex_v8, pathlib, create_gc_cycles, xml_etree_generate, thrift, sqlglot_parse, deepcopy_memo, hexiom, coverage, sqlglot_optimize, sympy_expand, pycparser, pickle_pure_python, pickle_dict, xml_etree_parse, nbody, json, pylint

# HPT report

- Reliability score: 99.63% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x