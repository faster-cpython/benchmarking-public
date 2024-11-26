# Results vs. base

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-aarch64
- commit hash: 0442576
- commit date: 2024-10-07
- overall geometric mean: 1.025x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.90x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 386 ms                                                                  | 365 ms: 1.06x faster                                                 |
| docutils       | 3.71 sec                                                                | 3.56 sec: 1.04x faster                                               |
| html5lib       | 71.9 ms                                                                 | 70.6 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                                   | 1.03x faster                                                         |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|---------------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io             | 1.20 sec                                                                | 1.15 sec: 1.05x faster                                               |
| async_tree_none           | 459 ms                                                                  | 442 ms: 1.04x faster                                                 |
| async_tree_io_tg          | 1.20 sec                                                                | 1.17 sec: 1.02x faster                                               |
| async_generators          | 508 ms                                                                  | 517 ms: 1.02x slower                                                 |
| asyncio_tcp_ssl           | 2.24 sec                                                                | 2.28 sec: 1.02x slower                                               |
| asyncio_tcp               | 603 ms                                                                  | 622 ms: 1.03x slower                                                 |
| async_tree_memoization_tg | 543 ms                                                                  | 561 ms: 1.03x slower                                                 |
| Geometric mean            | (ref)                                                                   | 1.00x faster                                                         |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, coroutines, asyncio_websockets, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 94.3 ms                                                                 | 90.2 ms: 1.05x faster                                                |
| Geometric mean | (ref)                                                                   | 1.02x faster                                                         |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 180 ms                                                                  | 174 ms: 1.04x faster                                                 |
| regex_dna      | 255 ms                                                                  | 263 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                         |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|--------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| json_dumps         | 13.6 ms                                                                 | 13.1 ms: 1.04x faster                                                |
| unpickle_list      | 6.56 us                                                                 | 6.37 us: 1.03x faster                                                |
| xml_etree_generate | 112 ms                                                                  | 109 ms: 1.03x faster                                                 |
| xml_etree_process  | 81.3 ms                                                                 | 79.4 ms: 1.02x faster                                                |
| pickle_list        | 5.29 us                                                                 | 5.19 us: 1.02x faster                                                |
| json_loads         | 31.6 us                                                                 | 31.1 us: 1.02x faster                                                |
| Geometric mean     | (ref)                                                                   | 1.01x faster                                                         |

Benchmark hidden because not significant (8): unpickle, xml_etree_iterparse, unpickle_pure_python, tomli_loads, pickle_dict, pickle, pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup | 14.6 ms                                                                 | 13.1 ms: 1.11x faster                                                |
| Geometric mean | (ref)                                                                   | 1.05x faster                                                         |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml      | 84.4 ms                                                                 | 78.1 ms: 1.08x faster                                                |
| genshi_text     | 34.4 ms                                                                 | 33.1 ms: 1.04x faster                                                |
| django_template | 52.2 ms                                                                 | 51.2 ms: 1.02x faster                                                |
| mako            | 13.0 ms                                                                 | 13.2 ms: 1.01x slower                                                |
| Geometric mean  | (ref)                                                                   | 1.03x faster                                                         |

All benchmarks:
===============

| Benchmark                 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|---------------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| create_gc_cycles          | 3.57 ms                                                                 | 2.28 ms: 1.57x faster                                                |
| gc_traversal              | 6.11 ms                                                                 | 5.21 ms: 1.17x faster                                                |
| richards                  | 66.2 ms                                                                 | 56.9 ms: 1.16x faster                                                |
| richards_super            | 74.9 ms                                                                 | 67.3 ms: 1.11x faster                                                |
| python_startup            | 14.6 ms                                                                 | 13.1 ms: 1.11x faster                                                |
| sqlglot_optimize          | 82.8 ms                                                                 | 76.1 ms: 1.09x faster                                                |
| genshi_xml                | 84.4 ms                                                                 | 78.1 ms: 1.08x faster                                                |
| 2to3                      | 386 ms                                                                  | 365 ms: 1.06x faster                                                 |
| sqlglot_normalize         | 157 ms                                                                  | 149 ms: 1.05x faster                                                 |
| async_tree_io             | 1.20 sec                                                                | 1.15 sec: 1.05x faster                                               |
| float                     | 94.3 ms                                                                 | 90.2 ms: 1.05x faster                                                |
| telco                     | 9.78 ms                                                                 | 9.37 ms: 1.04x faster                                                |
| docutils                  | 3.71 sec                                                                | 3.56 sec: 1.04x faster                                               |
| sympy_expand              | 597 ms                                                                  | 573 ms: 1.04x faster                                                 |
| genshi_text               | 34.4 ms                                                                 | 33.1 ms: 1.04x faster                                                |
| async_tree_none           | 459 ms                                                                  | 442 ms: 1.04x faster                                                 |
| regex_compile             | 180 ms                                                                  | 174 ms: 1.04x faster                                                 |
| sympy_str                 | 359 ms                                                                  | 346 ms: 1.04x faster                                                 |
| json_dumps                | 13.6 ms                                                                 | 13.1 ms: 1.04x faster                                                |
| pprint_pformat            | 2.63 sec                                                                | 2.54 sec: 1.03x faster                                               |
| spectral_norm             | 152 ms                                                                  | 147 ms: 1.03x faster                                                 |
| json                      | 5.72 ms                                                                 | 5.54 ms: 1.03x faster                                                |
| unpickle_list             | 6.56 us                                                                 | 6.37 us: 1.03x faster                                                |
| logging_format            | 8.34 us                                                                 | 8.10 us: 1.03x faster                                                |
| logging_simple            | 7.70 us                                                                 | 7.49 us: 1.03x faster                                                |
| xml_etree_generate        | 112 ms                                                                  | 109 ms: 1.03x faster                                                 |
| hexiom                    | 10.2 ms                                                                 | 9.90 ms: 1.03x faster                                                |
| typing_runtime_protocols  | 211 us                                                                  | 205 us: 1.03x faster                                                 |
| xml_etree_process         | 81.3 ms                                                                 | 79.4 ms: 1.02x faster                                                |
| nqueens                   | 125 ms                                                                  | 123 ms: 1.02x faster                                                 |
| pycparser                 | 1.51 sec                                                                | 1.47 sec: 1.02x faster                                               |
| async_tree_io_tg          | 1.20 sec                                                                | 1.17 sec: 1.02x faster                                               |
| sympy_sum                 | 214 ms                                                                  | 210 ms: 1.02x faster                                                 |
| bench_thread_pool         | 1.39 ms                                                                 | 1.37 ms: 1.02x faster                                                |
| pickle_list               | 5.29 us                                                                 | 5.19 us: 1.02x faster                                                |
| html5lib                  | 71.9 ms                                                                 | 70.6 ms: 1.02x faster                                                |
| django_template           | 52.2 ms                                                                 | 51.2 ms: 1.02x faster                                                |
| meteor_contest            | 125 ms                                                                  | 123 ms: 1.02x faster                                                 |
| bpe_tokeniser             | 6.07 sec                                                                | 5.96 sec: 1.02x faster                                               |
| mdp                       | 3.51 sec                                                                | 3.45 sec: 1.02x faster                                               |
| raytrace                  | 351 ms                                                                  | 345 ms: 1.02x faster                                                 |
| logging_silent            | 134 ns                                                                  | 132 ns: 1.02x faster                                                 |
| scimark_sor               | 153 ms                                                                  | 151 ms: 1.02x faster                                                 |
| json_loads                | 31.6 us                                                                 | 31.1 us: 1.02x faster                                                |
| deltablue                 | 4.40 ms                                                                 | 4.34 ms: 1.01x faster                                                |
| scimark_monte_carlo       | 89.5 ms                                                                 | 88.2 ms: 1.01x faster                                                |
| crypto_pyaes              | 89.8 ms                                                                 | 88.6 ms: 1.01x faster                                                |
| deepcopy                  | 407 us                                                                  | 402 us: 1.01x faster                                                 |
| pprint_safe_repr          | 1.24 sec                                                                | 1.22 sec: 1.01x faster                                               |
| sqlglot_parse             | 1.69 ms                                                                 | 1.68 ms: 1.01x faster                                                |
| chaos                     | 87.0 ms                                                                 | 86.4 ms: 1.01x faster                                                |
| generators                | 59.1 ms                                                                 | 58.8 ms: 1.00x faster                                                |
| mako                      | 13.0 ms                                                                 | 13.2 ms: 1.01x slower                                                |
| async_generators          | 508 ms                                                                  | 517 ms: 1.02x slower                                                 |
| asyncio_tcp_ssl           | 2.24 sec                                                                | 2.28 sec: 1.02x slower                                               |
| asyncio_tcp               | 603 ms                                                                  | 622 ms: 1.03x slower                                                 |
| regex_dna                 | 255 ms                                                                  | 263 ms: 1.03x slower                                                 |
| async_tree_memoization_tg | 543 ms                                                                  | 561 ms: 1.03x slower                                                 |
| bench_mp_pool             | 1.43 sec                                                                | 2.94 sec: 2.05x slower                                               |
| Geometric mean            | (ref)                                                                   | 1.02x faster                                                         |

Benchmark hidden because not significant (38): pylint, sympy_integrate, comprehensions, coverage, async_tree_cpu_io_mixed, scimark_sparse_mat_mult, go, coroutines, unpickle, sqlite_synth, xml_etree_iterparse, unpickle_pure_python, deepcopy_memo, pidigits, tomli_loads, regex_effbot, deepcopy_reduce, asyncio_websockets, scimark_lu, nbody, scimark_fft, fannkuch, pickle_dict, pathlib, python_startup_no_site, pickle, thrift, async_tree_memoization, pickle_pure_python, pyflate, async_tree_cpu_io_mixed_tg, tornado_http, unpack_sequence, async_tree_none_tg, xml_etree_parse, regex_v8, dulwich_log, sqlglot_transpile
Ignored benchmarks (1) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: sphinx

- Geometric mean (including insignificant results): 1.025x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.90x