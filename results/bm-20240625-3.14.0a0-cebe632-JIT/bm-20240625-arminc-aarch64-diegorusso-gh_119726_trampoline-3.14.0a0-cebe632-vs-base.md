# Results vs. base

- fork: diegorusso
- ref: gh_119726_trampoline
- machine: linux-aarch64
- commit hash: cebe632
- commit date: 2024-06-25
- overall geometric mean: 1.00x faster
- HPT reliability: 86.26%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240625-arminc-aarch64-python-42b2c9d78da7ebd6bd59-3.14.0a0-42b2c9d | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 358 ms                                                                  | 364 ms: 1.02x slower                                                        |
| html5lib       | 71.8 ms                                                                 | 70.5 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                                |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240625-arminc-aarch64-python-42b2c9d78da7ebd6bd59-3.14.0a0-42b2c9d | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|---------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg | 547 ms                                                                  | 538 ms: 1.02x faster                                                        |
| Geometric mean            | (ref)                                                                   | 1.01x faster                                                                |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_io, async_tree_io_tg, async_tree_none_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240625-arminc-aarch64-python-42b2c9d78da7ebd6bd59-3.14.0a0-42b2c9d | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 115 ms                                                                  | 114 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                                |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240625-arminc-aarch64-python-42b2c9d78da7ebd6bd59-3.14.0a0-42b2c9d | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 262 ms                                                                  | 251 ms: 1.04x faster                                                        |
| regex_v8       | 30.2 ms                                                                 | 30.4 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                                |

Benchmark hidden because not significant (2): regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240625-arminc-aarch64-python-42b2c9d78da7ebd6bd59-3.14.0a0-42b2c9d | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|---------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse     | 192 ms                                                                  | 187 ms: 1.02x faster                                                        |
| xml_etree_generate  | 112 ms                                                                  | 110 ms: 1.01x faster                                                        |
| xml_etree_iterparse | 149 ms                                                                  | 147 ms: 1.01x faster                                                        |
| json_dumps          | 13.6 ms                                                                 | 13.5 ms: 1.01x faster                                                       |
| pickle_pure_python  | 393 us                                                                  | 396 us: 1.01x slower                                                        |
| pickle              | 13.8 us                                                                 | 14.0 us: 1.02x slower                                                       |
| Geometric mean      | (ref)                                                                   | 1.00x faster                                                                |

Benchmark hidden because not significant (8): xml_etree_process, json_loads, pickle_list, unpickle, pickle_dict, unpickle_list, tomli_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): django_template, genshi_xml, mako, genshi_text

All benchmarks:
===============

| Benchmark                 | bm-20240625-arminc-aarch64-python-42b2c9d78da7ebd6bd59-3.14.0a0-42b2c9d | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|---------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal              | 5.11 ms                                                                 | 4.82 ms: 1.06x faster                                                       |
| regex_dna                 | 262 ms                                                                  | 251 ms: 1.04x faster                                                        |
| telco                     | 10.5 ms                                                                 | 10.1 ms: 1.04x faster                                                       |
| create_gc_cycles          | 2.39 ms                                                                 | 2.33 ms: 1.03x faster                                                       |
| typing_runtime_protocols  | 212 us                                                                  | 207 us: 1.02x faster                                                        |
| scimark_sparse_mat_mult   | 6.87 ms                                                                 | 6.71 ms: 1.02x faster                                                       |
| xml_etree_parse           | 192 ms                                                                  | 187 ms: 1.02x faster                                                        |
| async_generators          | 517 ms                                                                  | 507 ms: 1.02x faster                                                        |
| dulwich_log               | 70.0 ms                                                                 | 68.7 ms: 1.02x faster                                                       |
| deepcopy_memo             | 39.7 us                                                                 | 38.9 us: 1.02x faster                                                       |
| spectral_norm             | 149 ms                                                                  | 146 ms: 1.02x faster                                                        |
| html5lib                  | 71.8 ms                                                                 | 70.5 ms: 1.02x faster                                                       |
| pycparser                 | 1.36 sec                                                                | 1.34 sec: 1.02x faster                                                      |
| async_tree_memoization_tg | 547 ms                                                                  | 538 ms: 1.02x faster                                                        |
| fannkuch                  | 472 ms                                                                  | 464 ms: 1.02x faster                                                        |
| scimark_sor               | 176 ms                                                                  | 174 ms: 1.01x faster                                                        |
| xml_etree_generate        | 112 ms                                                                  | 110 ms: 1.01x faster                                                        |
| bpe_tokeniser             | 6.08 sec                                                                | 6.01 sec: 1.01x faster                                                      |
| xml_etree_iterparse       | 149 ms                                                                  | 147 ms: 1.01x faster                                                        |
| meteor_contest            | 116 ms                                                                  | 115 ms: 1.01x faster                                                        |
| json_dumps                | 13.6 ms                                                                 | 13.5 ms: 1.01x faster                                                       |
| nbody                     | 115 ms                                                                  | 114 ms: 1.01x faster                                                        |
| hexiom                    | 8.91 ms                                                                 | 8.97 ms: 1.01x slower                                                       |
| pickle_pure_python        | 393 us                                                                  | 396 us: 1.01x slower                                                        |
| regex_v8                  | 30.2 ms                                                                 | 30.4 ms: 1.01x slower                                                       |
| pyflate                   | 613 ms                                                                  | 619 ms: 1.01x slower                                                        |
| comprehensions            | 23.3 us                                                                 | 23.5 us: 1.01x slower                                                       |
| nqueens                   | 117 ms                                                                  | 119 ms: 1.01x slower                                                        |
| richards                  | 55.1 ms                                                                 | 55.8 ms: 1.01x slower                                                       |
| 2to3                      | 358 ms                                                                  | 364 ms: 1.02x slower                                                        |
| pprint_safe_repr          | 1.12 sec                                                                | 1.14 sec: 1.02x slower                                                      |
| pickle                    | 13.8 us                                                                 | 14.0 us: 1.02x slower                                                       |
| pathlib                   | 22.1 ms                                                                 | 22.5 ms: 1.02x slower                                                       |
| sympy_sum                 | 179 ms                                                                  | 183 ms: 1.02x slower                                                        |
| scimark_monte_carlo       | 85.5 ms                                                                 | 87.5 ms: 1.02x slower                                                       |
| sympy_integrate           | 25.6 ms                                                                 | 26.2 ms: 1.02x slower                                                       |
| deepcopy                  | 377 us                                                                  | 386 us: 1.03x slower                                                        |
| pprint_pformat            | 2.31 sec                                                                | 2.38 sec: 1.03x slower                                                      |
| asyncio_tcp               | 622 ms                                                                  | 647 ms: 1.04x slower                                                        |
| sqlglot_parse             | 1.57 ms                                                                 | 1.64 ms: 1.04x slower                                                       |
| Geometric mean            | (ref)                                                                   | 1.00x faster                                                                |

Benchmark hidden because not significant (57): regex_effbot, xml_etree_process, async_tree_cpu_io_mixed, dask, sympy_expand, async_tree_cpu_io_mixed_tg, python_startup, json, async_tree_memoization, coroutines, tornado_http, sqlglot_optimize, bench_mp_pool, async_tree_io, json_loads, logging_simple, regex_compile, scimark_lu, float, crypto_pyaes, pidigits, pickle_list, go, async_tree_io_tg, unpickle, django_template, python_startup_no_site, thrift, pylint, docutils, generators, sympy_str, genshi_xml, async_tree_none_tg, mdp, logging_silent, mako, pickle_dict, raytrace, asyncio_tcp_ssl, sqlglot_normalize, unpickle_list, asyncio_websockets, tomli_loads, chaos, deltablue, sqlite_synth, genshi_text, scimark_fft, unpickle_pure_python, async_tree_none, sqlglot_transpile, deepcopy_reduce, logging_format, richards_super, bench_thread_pool, coverage

# HPT report

- Reliability score: 86.26% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x