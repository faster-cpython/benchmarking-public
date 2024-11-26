# Results vs. base

- fork: mdboom
- ref: remove_redundant_typ
- machine: linux-aarch64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.002x slower
- HPT reliability: 67.96%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_tcp_ssl | 2.20 sec                                                                | 2.19 sec: 1.01x faster                                                  |
| coroutines      | 28.3 ms                                                                 | 28.6 ms: 1.01x slower                                                   |
| Geometric mean  | (ref)                                                                   | 1.00x slower                                                            |

Benchmark hidden because not significant (11): async_generators, async_tree_memoization, async_tree_none_tg, async_tree_io, async_tree_memoization_tg, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_io_tg, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.9 ms                                                                 | 93.3 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 247 ms                                                                  | 252 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                            |

Benchmark hidden because not significant (3): regex_v8, regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 193 ms                                                                  | 186 ms: 1.04x faster                                                    |
| unpickle_list        | 6.63 us                                                                 | 6.54 us: 1.01x faster                                                   |
| unpickle_pure_python | 255 us                                                                  | 256 us: 1.01x slower                                                    |
| json_dumps           | 13.1 ms                                                                 | 13.3 ms: 1.02x slower                                                   |
| Geometric mean       | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (10): pickle_list, xml_etree_process, tomli_loads, pickle_dict, pickle_pure_python, pickle, json_loads, xml_etree_iterparse, unpickle, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.57 ms                                                                 | 8.69 ms: 1.01x slower                                                   |
| python_startup         | 12.9 ms                                                                 | 13.1 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                                   | 1.01x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.5 ms                                                                 | 13.3 ms: 1.02x faster                                                   |
| genshi_text    | 26.9 ms                                                                 | 27.2 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                            |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark              | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse        | 193 ms                                                                  | 186 ms: 1.04x faster                                                    |
| unpack_sequence        | 60.0 ns                                                                 | 58.5 ns: 1.03x faster                                                   |
| mako                   | 13.5 ms                                                                 | 13.3 ms: 1.02x faster                                                   |
| spectral_norm          | 142 ms                                                                  | 140 ms: 1.02x faster                                                    |
| mdp                    | 3.35 sec                                                                | 3.31 sec: 1.01x faster                                                  |
| unpickle_list          | 6.63 us                                                                 | 6.54 us: 1.01x faster                                                   |
| pprint_safe_repr       | 923 ms                                                                  | 914 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl        | 2.20 sec                                                                | 2.19 sec: 1.01x faster                                                  |
| pprint_pformat         | 1.89 sec                                                                | 1.88 sec: 1.01x faster                                                  |
| richards_super         | 58.9 ms                                                                 | 59.1 ms: 1.00x slower                                                   |
| float                  | 92.9 ms                                                                 | 93.3 ms: 1.00x slower                                                   |
| unpickle_pure_python   | 255 us                                                                  | 256 us: 1.01x slower                                                    |
| richards               | 52.4 ms                                                                 | 52.7 ms: 1.01x slower                                                   |
| meteor_contest         | 111 ms                                                                  | 113 ms: 1.01x slower                                                    |
| deepcopy_memo          | 37.6 us                                                                 | 38.0 us: 1.01x slower                                                   |
| coroutines             | 28.3 ms                                                                 | 28.6 ms: 1.01x slower                                                   |
| genshi_text            | 26.9 ms                                                                 | 27.2 ms: 1.01x slower                                                   |
| scimark_lu             | 134 ms                                                                  | 136 ms: 1.01x slower                                                    |
| pathlib                | 20.9 ms                                                                 | 21.2 ms: 1.01x slower                                                   |
| python_startup_no_site | 8.57 ms                                                                 | 8.69 ms: 1.01x slower                                                   |
| python_startup         | 12.9 ms                                                                 | 13.1 ms: 1.01x slower                                                   |
| scimark_monte_carlo    | 82.2 ms                                                                 | 83.6 ms: 1.02x slower                                                   |
| json_dumps             | 13.1 ms                                                                 | 13.3 ms: 1.02x slower                                                   |
| logging_simple         | 6.89 us                                                                 | 7.02 us: 1.02x slower                                                   |
| regex_dna              | 247 ms                                                                  | 252 ms: 1.02x slower                                                    |
| pyflate                | 564 ms                                                                  | 580 ms: 1.03x slower                                                    |
| telco                  | 9.97 ms                                                                 | 10.3 ms: 1.03x slower                                                   |
| Geometric mean         | (ref)                                                                   | 1.00x slower                                                            |

Benchmark hidden because not significant (70): sqlglot_parse, sqlglot_optimize, html5lib, bench_mp_pool, crypto_pyaes, sympy_integrate, pickle_list, logging_silent, xml_etree_process, gc_traversal, scimark_sor, typing_runtime_protocols, json, sympy_sum, tornado_http, regex_v8, scimark_sparse_mat_mult, deepcopy, pylint, comprehensions, async_generators, async_tree_memoization, async_tree_none_tg, sympy_str, raytrace, sympy_expand, pycparser, tomli_loads, pickle_dict, docutils, create_gc_cycles, pickle_pure_python, generators, async_tree_io, 2to3, async_tree_memoization_tg, scimark_fft, hexiom, bpe_tokeniser, asyncio_websockets, async_tree_cpu_io_mixed, pidigits, bench_thread_pool, fannkuch, pickle, async_tree_cpu_io_mixed_tg, chaos, async_tree_none, thrift, sqlite_synth, json_loads, nbody, deepcopy_reduce, xml_etree_iterparse, regex_effbot, nqueens, go, coverage, sqlglot_transpile, django_template, unpickle, async_tree_io_tg, dulwich_log, asyncio_tcp, regex_compile, xml_etree_generate, logging_format, deltablue, sqlglot_normalize, genshi_xml

- Geometric mean (including insignificant results): 1.002x slower
# HPT report

- Reliability score: 67.96% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x