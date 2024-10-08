# Results vs. base

- fork: mdboom
- ref: remove_redundant_typ
- machine: darwin-arm64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.00x slower
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 160 ms                                                                | 162 ms: 1.01x slower                                                  |
| docutils       | 1.42 sec                                                              | 1.45 sec: 1.02x slower                                                |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                          |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines       | 16.0 ms                                                               | 16.0 ms: 1.00x faster                                                 |
| async_generators | 278 ms                                                                | 278 ms: 1.00x slower                                                  |
| async_tree_eager | 60.6 ms                                                               | 60.8 ms: 1.00x slower                                                 |
| Geometric mean   | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (18): asyncio_tcp, async_tree_io_tg, async_tree_eager_io_tg, async_tree_eager_tg, async_tree_eager_memoization, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_eager_memoization_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed, async_tree_none, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, async_tree_eager_io, async_tree_none_tg, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 60.2 ms                                                               | 60.0 ms: 1.00x faster                                                 |
| pidigits       | 282 ms                                                                | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 66.8 ms                                                               | 67.0 ms: 1.00x slower                                                 |
| regex_effbot   | 2.45 ms                                                               | 2.46 ms: 1.00x slower                                                 |
| regex_dna      | 144 ms                                                                | 145 ms: 1.00x slower                                                  |
| regex_v8       | 16.4 ms                                                               | 16.6 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_list        | 2.98 us                                                               | 2.90 us: 1.03x faster                                                 |
| pickle_pure_python   | 183 us                                                                | 180 us: 1.02x faster                                                  |
| pickle_list          | 2.98 us                                                               | 2.96 us: 1.01x faster                                                 |
| pickle               | 7.39 us                                                               | 7.34 us: 1.01x faster                                                 |
| pickle_dict          | 18.2 us                                                               | 18.1 us: 1.00x faster                                                 |
| unpickle_pure_python | 141 us                                                                | 140 us: 1.00x faster                                                  |
| xml_etree_process    | 37.4 ms                                                               | 37.5 ms: 1.00x slower                                                 |
| json_dumps           | 6.26 ms                                                               | 6.30 ms: 1.01x slower                                                 |
| xml_etree_generate   | 52.3 ms                                                               | 52.9 ms: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (5): tomli_loads, unpickle, json_loads, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.7 ms                                                               | 16.0 ms: 1.02x slower                                                 |
| python_startup_no_site | 12.8 ms                                                               | 13.1 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.02x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.21 ms                                                               | 7.12 ms: 1.01x faster                                                 |
| django_template | 20.0 ms                                                               | 20.0 ms: 1.00x slower                                                 |
| genshi_text     | 13.7 ms                                                               | 13.8 ms: 1.00x slower                                                 |
| genshi_xml      | 30.2 ms                                                               | 30.3 ms: 1.00x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20240924-darwin-arm64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 | bm-20240923-darwin-arm64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_list            | 2.98 us                                                               | 2.90 us: 1.03x faster                                                 |
| pickle_pure_python       | 183 us                                                                | 180 us: 1.02x faster                                                  |
| bench_thread_pool        | 454 us                                                                | 448 us: 1.01x faster                                                  |
| mako                     | 7.21 ms                                                               | 7.12 ms: 1.01x faster                                                 |
| logging_format           | 3.30 us                                                               | 3.28 us: 1.01x faster                                                 |
| sympy_sum                | 69.2 ms                                                               | 68.7 ms: 1.01x faster                                                 |
| pickle_list              | 2.98 us                                                               | 2.96 us: 1.01x faster                                                 |
| json                     | 2.92 ms                                                               | 2.91 ms: 1.01x faster                                                 |
| pickle                   | 7.39 us                                                               | 7.34 us: 1.01x faster                                                 |
| sqlglot_parse            | 740 us                                                                | 736 us: 1.01x faster                                                  |
| dulwich_log              | 27.4 ms                                                               | 27.3 ms: 1.01x faster                                                 |
| pickle_dict              | 18.2 us                                                               | 18.1 us: 1.00x faster                                                 |
| meteor_contest           | 71.6 ms                                                               | 71.3 ms: 1.00x faster                                                 |
| hexiom                   | 4.06 ms                                                               | 4.04 ms: 1.00x faster                                                 |
| logging_simple           | 3.01 us                                                               | 3.00 us: 1.00x faster                                                 |
| unpickle_pure_python     | 141 us                                                                | 140 us: 1.00x faster                                                  |
| nbody                    | 60.2 ms                                                               | 60.0 ms: 1.00x faster                                                 |
| pidigits                 | 282 ms                                                                | 281 ms: 1.00x faster                                                  |
| coroutines               | 16.0 ms                                                               | 16.0 ms: 1.00x faster                                                 |
| chaos                    | 35.6 ms                                                               | 35.6 ms: 1.00x slower                                                 |
| scimark_sor              | 92.6 ms                                                               | 92.7 ms: 1.00x slower                                                 |
| xml_etree_process        | 37.4 ms                                                               | 37.5 ms: 1.00x slower                                                 |
| regex_compile            | 66.8 ms                                                               | 67.0 ms: 1.00x slower                                                 |
| bpe_tokeniser            | 3.12 sec                                                              | 3.13 sec: 1.00x slower                                                |
| sympy_expand             | 227 ms                                                                | 227 ms: 1.00x slower                                                  |
| django_template          | 20.0 ms                                                               | 20.0 ms: 1.00x slower                                                 |
| create_gc_cycles         | 889 us                                                                | 892 us: 1.00x slower                                                  |
| async_generators         | 278 ms                                                                | 278 ms: 1.00x slower                                                  |
| pprint_safe_repr         | 455 ms                                                                | 457 ms: 1.00x slower                                                  |
| pyflate                  | 319 ms                                                                | 320 ms: 1.00x slower                                                  |
| genshi_text              | 13.7 ms                                                               | 13.8 ms: 1.00x slower                                                 |
| regex_effbot             | 2.45 ms                                                               | 2.46 ms: 1.00x slower                                                 |
| genshi_xml               | 30.2 ms                                                               | 30.3 ms: 1.00x slower                                                 |
| async_tree_eager         | 60.6 ms                                                               | 60.8 ms: 1.00x slower                                                 |
| regex_dna                | 144 ms                                                                | 145 ms: 1.00x slower                                                  |
| sympy_str                | 131 ms                                                                | 132 ms: 1.00x slower                                                  |
| nqueens                  | 53.0 ms                                                               | 53.2 ms: 1.00x slower                                                 |
| thrift                   | 424 us                                                                | 426 us: 1.01x slower                                                  |
| sqlglot_optimize         | 30.9 ms                                                               | 31.1 ms: 1.01x slower                                                 |
| deltablue                | 2.12 ms                                                               | 2.13 ms: 1.01x slower                                                 |
| sqlglot_normalize        | 166 ms                                                                | 167 ms: 1.01x slower                                                  |
| deepcopy                 | 143 us                                                                | 144 us: 1.01x slower                                                  |
| json_dumps               | 6.26 ms                                                               | 6.30 ms: 1.01x slower                                                 |
| coverage                 | 44.1 ms                                                               | 44.4 ms: 1.01x slower                                                 |
| fannkuch                 | 259 ms                                                                | 261 ms: 1.01x slower                                                  |
| logging_silent           | 60.3 ns                                                               | 60.8 ns: 1.01x slower                                                 |
| mdp                      | 1.42 sec                                                              | 1.44 sec: 1.01x slower                                                |
| typing_runtime_protocols | 92.6 us                                                               | 93.6 us: 1.01x slower                                                 |
| 2to3                     | 160 ms                                                                | 162 ms: 1.01x slower                                                  |
| xml_etree_generate       | 52.3 ms                                                               | 52.9 ms: 1.01x slower                                                 |
| regex_v8                 | 16.4 ms                                                               | 16.6 ms: 1.01x slower                                                 |
| docutils                 | 1.42 sec                                                              | 1.45 sec: 1.02x slower                                                |
| python_startup           | 15.7 ms                                                               | 16.0 ms: 1.02x slower                                                 |
| generators               | 20.7 ms                                                               | 21.1 ms: 1.02x slower                                                 |
| python_startup_no_site   | 12.8 ms                                                               | 13.1 ms: 1.02x slower                                                 |
| telco                    | 4.63 ms                                                               | 4.81 ms: 1.04x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (49): asyncio_tcp, pylint, async_tree_io_tg, async_tree_eager_io_tg, unpack_sequence, scimark_lu, bench_mp_pool, sqlglot_transpile, spectral_norm, sqlite_synth, raytrace, tomli_loads, async_tree_eager_tg, gc_traversal, crypto_pyaes, async_tree_eager_memoization, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_eager_memoization_tg, sympy_integrate, async_tree_eager_cpu_io_mixed_tg, scimark_monte_carlo, richards_super, go, scimark_sparse_mat_mult, deepcopy_reduce, pprint_pformat, richards, async_tree_eager_cpu_io_mixed, html5lib, async_tree_none, scimark_fft, comprehensions, deepcopy_memo, unpickle, async_tree_cpu_io_mixed_tg, float, pycparser, asyncio_tcp_ssl, json_loads, async_tree_eager_io, async_tree_none_tg, async_tree_memoization_tg, xml_etree_iterparse, async_tree_io, xml_etree_parse, pathlib, tornado_http

# HPT report

- Reliability score: 99.95% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown