# Results vs. base

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-aarch64
- commit hash: 0442576
- commit date: 2024-10-07
- overall geometric mean: 1.01x faster
- HPT reliability: 99.44%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 385 ms                                                                  | 365 ms: 1.05x faster                                                 |
| docutils       | 3.74 sec                                                                | 3.56 sec: 1.05x faster                                               |
| html5lib       | 71.5 ms                                                                 | 70.6 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                   | 1.03x faster                                                         |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| asyncio_tcp_ssl  | 2.27 sec                                                                | 2.28 sec: 1.01x slower                                               |
| async_generators | 503 ms                                                                  | 517 ms: 1.03x slower                                                 |
| Geometric mean   | (ref)                                                                   | 1.00x slower                                                         |

Benchmark hidden because not significant (11): coroutines, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_memoization_tg, asyncio_tcp, async_tree_none_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 185 ms                                                                  | 174 ms: 1.06x faster                                                 |
| regex_effbot   | 4.92 ms                                                                 | 5.00 ms: 1.01x slower                                                |
| regex_dna      | 253 ms                                                                  | 263 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|--------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_process  | 81.3 ms                                                                 | 79.4 ms: 1.02x faster                                                |
| xml_etree_generate | 111 ms                                                                  | 109 ms: 1.02x faster                                                 |
| pickle_list        | 5.22 us                                                                 | 5.19 us: 1.01x faster                                                |
| tomli_loads        | 2.62 sec                                                                | 2.64 sec: 1.01x slower                                               |
| pickle_pure_python | 388 us                                                                  | 395 us: 1.02x slower                                                 |
| json_dumps         | 12.9 ms                                                                 | 13.1 ms: 1.02x slower                                                |
| Geometric mean     | (ref)                                                                   | 1.00x faster                                                         |

Benchmark hidden because not significant (8): unpickle_list, unpickle_pure_python, json_loads, unpickle, xml_etree_iterparse, pickle_dict, pickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup | 13.0 ms                                                                 | 13.1 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                         |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml     | 82.9 ms                                                                 | 78.1 ms: 1.06x faster                                                |
| genshi_text    | 34.8 ms                                                                 | 33.1 ms: 1.05x faster                                                |
| mako           | 13.0 ms                                                                 | 13.2 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                   | 1.03x faster                                                         |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|--------------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| richards                 | 65.2 ms                                                                 | 56.9 ms: 1.15x faster                                                |
| sqlglot_optimize         | 82.0 ms                                                                 | 76.1 ms: 1.08x faster                                                |
| richards_super           | 71.7 ms                                                                 | 67.3 ms: 1.07x faster                                                |
| regex_compile            | 185 ms                                                                  | 174 ms: 1.06x faster                                                 |
| sympy_str                | 368 ms                                                                  | 346 ms: 1.06x faster                                                 |
| genshi_xml               | 82.9 ms                                                                 | 78.1 ms: 1.06x faster                                                |
| 2to3                     | 385 ms                                                                  | 365 ms: 1.05x faster                                                 |
| genshi_text              | 34.8 ms                                                                 | 33.1 ms: 1.05x faster                                                |
| chaos                    | 90.8 ms                                                                 | 86.4 ms: 1.05x faster                                                |
| docutils                 | 3.74 sec                                                                | 3.56 sec: 1.05x faster                                               |
| sqlglot_normalize        | 155 ms                                                                  | 149 ms: 1.04x faster                                                 |
| sympy_sum                | 218 ms                                                                  | 210 ms: 1.04x faster                                                 |
| pprint_pformat           | 2.64 sec                                                                | 2.54 sec: 1.04x faster                                               |
| typing_runtime_protocols | 213 us                                                                  | 205 us: 1.04x faster                                                 |
| sympy_expand             | 593 ms                                                                  | 573 ms: 1.03x faster                                                 |
| sympy_integrate          | 29.3 ms                                                                 | 28.5 ms: 1.03x faster                                                |
| xml_etree_process        | 81.3 ms                                                                 | 79.4 ms: 1.02x faster                                                |
| deepcopy_memo            | 38.3 us                                                                 | 37.4 us: 1.02x faster                                                |
| pprint_safe_repr         | 1.25 sec                                                                | 1.22 sec: 1.02x faster                                               |
| telco                    | 9.58 ms                                                                 | 9.37 ms: 1.02x faster                                                |
| sqlglot_parse            | 1.71 ms                                                                 | 1.68 ms: 1.02x faster                                                |
| hexiom                   | 10.1 ms                                                                 | 9.90 ms: 1.02x faster                                                |
| go                       | 186 ms                                                                  | 182 ms: 1.02x faster                                                 |
| xml_etree_generate       | 111 ms                                                                  | 109 ms: 1.02x faster                                                 |
| crypto_pyaes             | 90.1 ms                                                                 | 88.6 ms: 1.02x faster                                                |
| raytrace                 | 350 ms                                                                  | 345 ms: 1.01x faster                                                 |
| mdp                      | 3.50 sec                                                                | 3.45 sec: 1.01x faster                                               |
| html5lib                 | 71.5 ms                                                                 | 70.6 ms: 1.01x faster                                                |
| pickle_list              | 5.22 us                                                                 | 5.19 us: 1.01x faster                                                |
| asyncio_tcp_ssl          | 2.27 sec                                                                | 2.28 sec: 1.01x slower                                               |
| python_startup           | 13.0 ms                                                                 | 13.1 ms: 1.01x slower                                                |
| scimark_fft              | 443 ms                                                                  | 446 ms: 1.01x slower                                                 |
| tomli_loads              | 2.62 sec                                                                | 2.64 sec: 1.01x slower                                               |
| mako                     | 13.0 ms                                                                 | 13.2 ms: 1.01x slower                                                |
| scimark_lu               | 149 ms                                                                  | 151 ms: 1.01x slower                                                 |
| regex_effbot             | 4.92 ms                                                                 | 5.00 ms: 1.01x slower                                                |
| pickle_pure_python       | 388 us                                                                  | 395 us: 1.02x slower                                                 |
| json_dumps               | 12.9 ms                                                                 | 13.1 ms: 1.02x slower                                                |
| async_generators         | 503 ms                                                                  | 517 ms: 1.03x slower                                                 |
| gc_traversal             | 5.06 ms                                                                 | 5.21 ms: 1.03x slower                                                |
| dulwich_log              | 78.7 ms                                                                 | 81.3 ms: 1.03x slower                                                |
| regex_dna                | 253 ms                                                                  | 263 ms: 1.04x slower                                                 |
| bench_mp_pool            | 2.04 sec                                                                | 2.94 sec: 1.44x slower                                               |
| Geometric mean           | (ref)                                                                   | 1.01x faster                                                         |

Benchmark hidden because not significant (54): pylint, unpack_sequence, meteor_contest, unpickle_list, deltablue, logging_format, unpickle_pure_python, scimark_sor, pycparser, scimark_monte_carlo, logging_silent, coroutines, async_tree_memoization, generators, pathlib, async_tree_none, logging_simple, pyflate, json, regex_v8, coverage, bpe_tokeniser, json_loads, unpickle, create_gc_cycles, nbody, comprehensions, thrift, async_tree_cpu_io_mixed_tg, python_startup_no_site, async_tree_io, scimark_sparse_mat_mult, async_tree_io_tg, bench_thread_pool, django_template, sqlglot_transpile, deepcopy, pidigits, async_tree_cpu_io_mixed, asyncio_websockets, xml_etree_iterparse, tornado_http, pickle_dict, fannkuch, pickle, nqueens, float, async_tree_memoization_tg, asyncio_tcp, xml_etree_parse, spectral_norm, deepcopy_reduce, async_tree_none_tg, sqlite_synth

# HPT report

- Reliability score: 99.44% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x