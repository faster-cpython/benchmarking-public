# Results vs. base

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-aarch64
- commit hash: 64b198a
- commit date: 2024-10-25
- overall geometric mean: 1.009x slower
- HPT reliability: 98.85%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 384 ms                                                                   | 390 ms: 1.01x slower                                                        |
| sphinx         | 1.47 sec                                                                 | 1.45 sec: 1.01x faster                                                      |
| tornado_http   | 145 ms                                                                   | 148 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                    | 1.00x slower                                                                |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg | 1.26 sec                                                                 | 1.25 sec: 1.01x faster                                                      |
| Geometric mean   | (ref)                                                                    | 1.01x faster                                                                |

Benchmark hidden because not significant (10): async_tree_none_tg, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_cpu_io_mixed, coroutines, async_tree_memoization_tg, async_generators, asyncio_websockets, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 96.4 ms                                                                  | 95.9 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                    | 1.00x slower                                                                |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 32.1 ms                                                                  | 30.7 ms: 1.05x faster                                                       |
| regex_dna      | 249 ms                                                                   | 251 ms: 1.01x slower                                                        |
| regex_compile  | 173 ms                                                                   | 177 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                    | 1.00x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark      | bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads    | 2.62 sec                                                                 | 2.71 sec: 1.03x slower                                                      |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                                |

Benchmark hidden because not significant (8): pickle_pure_python, unpickle_pure_python, xml_etree_generate, xml_etree_process, json_loads, json_dumps, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.5 ms                                                                  | 14.6 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.68 ms                                                                  | 8.78 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                                    | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|-----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 13.3 ms                                                                  | 13.3 ms: 1.01x slower                                                       |
| genshi_xml      | 81.8 ms                                                                  | 84.8 ms: 1.04x slower                                                       |
| django_template | 50.9 ms                                                                  | 53.3 ms: 1.05x slower                                                       |
| Geometric mean  | (ref)                                                                    | 1.02x slower                                                                |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark              | bm-20241022-arminc-aarch64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8               | 32.1 ms                                                                  | 30.7 ms: 1.05x faster                                                       |
| gc_traversal           | 6.39 ms                                                                  | 6.12 ms: 1.04x faster                                                       |
| logging_format         | 8.24 us                                                                  | 8.04 us: 1.02x faster                                                       |
| thrift                 | 979 us                                                                   | 965 us: 1.01x faster                                                        |
| logging_simple         | 7.51 us                                                                  | 7.42 us: 1.01x faster                                                       |
| sphinx                 | 1.47 sec                                                                 | 1.45 sec: 1.01x faster                                                      |
| async_tree_io_tg       | 1.26 sec                                                                 | 1.25 sec: 1.01x faster                                                      |
| float                  | 96.4 ms                                                                  | 95.9 ms: 1.01x faster                                                       |
| mako                   | 13.3 ms                                                                  | 13.3 ms: 1.01x slower                                                       |
| regex_dna              | 249 ms                                                                   | 251 ms: 1.01x slower                                                        |
| sqlglot_optimize       | 81.4 ms                                                                  | 82.0 ms: 1.01x slower                                                       |
| python_startup         | 14.5 ms                                                                  | 14.6 ms: 1.01x slower                                                       |
| scimark_fft            | 455 ms                                                                   | 459 ms: 1.01x slower                                                        |
| deltablue              | 4.47 ms                                                                  | 4.51 ms: 1.01x slower                                                       |
| logging_silent         | 147 ns                                                                   | 149 ns: 1.01x slower                                                        |
| python_startup_no_site | 8.68 ms                                                                  | 8.78 ms: 1.01x slower                                                       |
| sqlglot_normalize      | 155 ms                                                                   | 157 ms: 1.01x slower                                                        |
| 2to3                   | 384 ms                                                                   | 390 ms: 1.01x slower                                                        |
| bpe_tokeniser          | 5.95 sec                                                                 | 6.06 sec: 1.02x slower                                                      |
| deepcopy               | 378 us                                                                   | 386 us: 1.02x slower                                                        |
| dulwich_log            | 76.7 ms                                                                  | 78.4 ms: 1.02x slower                                                       |
| regex_compile          | 173 ms                                                                   | 177 ms: 1.02x slower                                                        |
| sympy_expand           | 584 ms                                                                   | 597 ms: 1.02x slower                                                        |
| hexiom                 | 10.2 ms                                                                  | 10.4 ms: 1.02x slower                                                       |
| tornado_http           | 145 ms                                                                   | 148 ms: 1.02x slower                                                        |
| scimark_sor            | 157 ms                                                                   | 161 ms: 1.02x slower                                                        |
| nqueens                | 126 ms                                                                   | 130 ms: 1.03x slower                                                        |
| sqlglot_parse          | 1.70 ms                                                                  | 1.75 ms: 1.03x slower                                                       |
| crypto_pyaes           | 88.7 ms                                                                  | 91.2 ms: 1.03x slower                                                       |
| telco                  | 9.29 ms                                                                  | 9.55 ms: 1.03x slower                                                       |
| spectral_norm          | 156 ms                                                                   | 161 ms: 1.03x slower                                                        |
| tomli_loads            | 2.62 sec                                                                 | 2.71 sec: 1.03x slower                                                      |
| go                     | 182 ms                                                                   | 189 ms: 1.04x slower                                                        |
| genshi_xml             | 81.8 ms                                                                  | 84.8 ms: 1.04x slower                                                       |
| fannkuch               | 503 ms                                                                   | 522 ms: 1.04x slower                                                        |
| richards_super         | 71.7 ms                                                                  | 74.4 ms: 1.04x slower                                                       |
| pprint_pformat         | 2.52 sec                                                                 | 2.62 sec: 1.04x slower                                                      |
| pprint_safe_repr       | 1.21 sec                                                                 | 1.26 sec: 1.04x slower                                                      |
| scimark_monte_carlo    | 90.3 ms                                                                  | 94.3 ms: 1.04x slower                                                       |
| django_template        | 50.9 ms                                                                  | 53.3 ms: 1.05x slower                                                       |
| chaos                  | 85.4 ms                                                                  | 89.8 ms: 1.05x slower                                                       |
| richards               | 67.7 ms                                                                  | 71.9 ms: 1.06x slower                                                       |
| pyflate                | 612 ms                                                                   | 652 ms: 1.06x slower                                                        |
| Geometric mean         | (ref)                                                                    | 1.01x slower                                                                |

Benchmark hidden because not significant (48): pathlib, async_tree_none_tg, async_tree_io, pickle_pure_python, async_tree_cpu_io_mixed_tg, typing_runtime_protocols, async_tree_none, async_tree_cpu_io_mixed, coroutines, json, unpickle_pure_python, genshi_text, pycparser, sympy_str, bench_thread_pool, async_tree_memoization_tg, docutils, xml_etree_generate, async_generators, regex_effbot, xml_etree_process, html5lib, asyncio_websockets, async_tree_memoization, scimark_lu, meteor_contest, coverage, generators, pidigits, comprehensions, sqlalchemy_declarative, sympy_sum, json_loads, deepcopy_reduce, mdp, sqlalchemy_imperative, json_dumps, sympy_integrate, create_gc_cycles, deepcopy_memo, xml_etree_iterparse, sqlglot_transpile, nbody, xml_etree_parse, raytrace, pylint, scimark_sparse_mat_mult, bench_mp_pool

- Geometric mean (including insignificant results): 1.009x slower
# HPT report

- Reliability score: 98.85% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x