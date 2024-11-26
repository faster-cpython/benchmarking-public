# Results vs. base

- fork: nick-arm
- ref: codecache
- machine: linux-aarch64
- commit hash: c2fad93
- commit date: 2024-10-17
- overall geometric mean: 1.005x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 386 ms                                                                  | 375 ms: 1.03x faster                                             |
| docutils       | 3.71 sec                                                                | 3.67 sec: 1.01x faster                                           |
| html5lib       | 71.9 ms                                                                 | 71.1 ms: 1.01x faster                                            |
| sphinx         | 1.46 sec                                                                | 1.42 sec: 1.03x faster                                           |
| Geometric mean | (ref)                                                                   | 1.02x faster                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| asyncio_tcp_ssl | 2.24 sec                                                                | 2.28 sec: 1.02x slower                                           |
| asyncio_tcp     | 603 ms                                                                  | 623 ms: 1.03x slower                                             |
| Geometric mean  | (ref)                                                                   | 1.00x faster                                                     |

Benchmark hidden because not significant (11): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, coroutines, async_tree_none, async_tree_io_tg, async_tree_none_tg, asyncio_websockets, async_tree_io, async_tree_memoization, async_tree_memoization_tg, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 111 ms                                                                  | 110 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                     |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 255 ms                                                                  | 247 ms: 1.03x faster                                             |
| regex_effbot   | 5.00 ms                                                                 | 4.90 ms: 1.02x faster                                            |
| regex_compile  | 180 ms                                                                  | 176 ms: 1.02x faster                                             |
| regex_v8       | 30.9 ms                                                                 | 31.5 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|---------------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| json_dumps          | 13.6 ms                                                                 | 13.4 ms: 1.02x faster                                            |
| pickle_list         | 5.29 us                                                                 | 5.21 us: 1.02x faster                                            |
| xml_etree_process   | 81.3 ms                                                                 | 80.5 ms: 1.01x faster                                            |
| xml_etree_iterparse | 152 ms                                                                  | 151 ms: 1.01x faster                                             |
| pickle              | 13.7 us                                                                 | 13.8 us: 1.01x slower                                            |
| Geometric mean      | (ref)                                                                   | 1.00x faster                                                     |

Benchmark hidden because not significant (9): pickle_pure_python, json_loads, xml_etree_generate, xml_etree_parse, unpickle, tomli_loads, unpickle_pure_python, unpickle_list, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup | 14.6 ms                                                                 | 14.7 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako           | 13.0 ms                                                                 | 12.9 ms: 1.00x faster                                            |
| genshi_text    | 34.4 ms                                                                 | 35.0 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                     |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241017-arminc-aarch64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|--------------------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| sqlglot_optimize         | 82.8 ms                                                                 | 79.2 ms: 1.04x faster                                            |
| nqueens                  | 125 ms                                                                  | 121 ms: 1.04x faster                                             |
| dulwich_log              | 80.1 ms                                                                 | 77.3 ms: 1.04x faster                                            |
| json                     | 5.72 ms                                                                 | 5.53 ms: 1.03x faster                                            |
| regex_dna                | 255 ms                                                                  | 247 ms: 1.03x faster                                             |
| deepcopy_reduce          | 3.94 us                                                                 | 3.83 us: 1.03x faster                                            |
| sphinx                   | 1.46 sec                                                                | 1.42 sec: 1.03x faster                                           |
| 2to3                     | 386 ms                                                                  | 375 ms: 1.03x faster                                             |
| telco                    | 9.78 ms                                                                 | 9.53 ms: 1.03x faster                                            |
| deepcopy                 | 407 us                                                                  | 397 us: 1.03x faster                                             |
| regex_effbot             | 5.00 ms                                                                 | 4.90 ms: 1.02x faster                                            |
| regex_compile            | 180 ms                                                                  | 176 ms: 1.02x faster                                             |
| json_dumps               | 13.6 ms                                                                 | 13.4 ms: 1.02x faster                                            |
| sympy_sum                | 214 ms                                                                  | 210 ms: 1.02x faster                                             |
| typing_runtime_protocols | 211 us                                                                  | 207 us: 1.02x faster                                             |
| pycparser                | 1.51 sec                                                                | 1.48 sec: 1.02x faster                                           |
| scimark_sparse_mat_mult  | 6.91 ms                                                                 | 6.80 ms: 1.02x faster                                            |
| pickle_list              | 5.29 us                                                                 | 5.21 us: 1.02x faster                                            |
| scimark_lu               | 151 ms                                                                  | 149 ms: 1.02x faster                                             |
| sqlglot_normalize        | 157 ms                                                                  | 154 ms: 1.02x faster                                             |
| sqlite_synth             | 3.89 us                                                                 | 3.83 us: 1.02x faster                                            |
| crypto_pyaes             | 89.8 ms                                                                 | 88.5 ms: 1.01x faster                                            |
| logging_format           | 8.34 us                                                                 | 8.22 us: 1.01x faster                                            |
| pathlib                  | 21.9 ms                                                                 | 21.6 ms: 1.01x faster                                            |
| pprint_safe_repr         | 1.24 sec                                                                | 1.22 sec: 1.01x faster                                           |
| docutils                 | 3.71 sec                                                                | 3.67 sec: 1.01x faster                                           |
| html5lib                 | 71.9 ms                                                                 | 71.1 ms: 1.01x faster                                            |
| chaos                    | 87.0 ms                                                                 | 86.0 ms: 1.01x faster                                            |
| pprint_pformat           | 2.63 sec                                                                | 2.60 sec: 1.01x faster                                           |
| xml_etree_process        | 81.3 ms                                                                 | 80.5 ms: 1.01x faster                                            |
| sympy_integrate          | 29.2 ms                                                                 | 28.9 ms: 1.01x faster                                            |
| nbody                    | 111 ms                                                                  | 110 ms: 1.01x faster                                             |
| scimark_sor              | 153 ms                                                                  | 152 ms: 1.01x faster                                             |
| xml_etree_iterparse      | 152 ms                                                                  | 151 ms: 1.01x faster                                             |
| scimark_fft              | 446 ms                                                                  | 443 ms: 1.01x faster                                             |
| mako                     | 13.0 ms                                                                 | 12.9 ms: 1.00x faster                                            |
| sqlglot_parse            | 1.69 ms                                                                 | 1.69 ms: 1.00x faster                                            |
| logging_silent           | 134 ns                                                                  | 135 ns: 1.01x slower                                             |
| python_startup           | 14.6 ms                                                                 | 14.7 ms: 1.01x slower                                            |
| bpe_tokeniser            | 6.07 sec                                                                | 6.13 sec: 1.01x slower                                           |
| pickle                   | 13.7 us                                                                 | 13.8 us: 1.01x slower                                            |
| scimark_monte_carlo      | 89.5 ms                                                                 | 90.9 ms: 1.02x slower                                            |
| genshi_text              | 34.4 ms                                                                 | 35.0 ms: 1.02x slower                                            |
| asyncio_tcp_ssl          | 2.24 sec                                                                | 2.28 sec: 1.02x slower                                           |
| richards_super           | 74.9 ms                                                                 | 76.3 ms: 1.02x slower                                            |
| regex_v8                 | 30.9 ms                                                                 | 31.5 ms: 1.02x slower                                            |
| go                       | 184 ms                                                                  | 189 ms: 1.02x slower                                             |
| fannkuch                 | 503 ms                                                                  | 519 ms: 1.03x slower                                             |
| asyncio_tcp              | 603 ms                                                                  | 623 ms: 1.03x slower                                             |
| coverage                 | 99.7 ms                                                                 | 103 ms: 1.03x slower                                             |
| richards                 | 66.2 ms                                                                 | 68.8 ms: 1.04x slower                                            |
| bench_mp_pool            | 1.43 sec                                                                | 3.29 sec: 2.29x slower                                           |
| Geometric mean           | (ref)                                                                   | 1.00x slower                                                     |

Benchmark hidden because not significant (46): pylint, async_tree_cpu_io_mixed_tg, pickle_pure_python, raytrace, logging_simple, async_tree_cpu_io_mixed, tornado_http, sympy_str, coroutines, json_loads, async_tree_none, async_tree_io_tg, sympy_expand, float, async_tree_none_tg, spectral_norm, meteor_contest, mdp, asyncio_websockets, xml_etree_generate, xml_etree_parse, async_tree_io, unpickle, comprehensions, tomli_loads, async_tree_memoization, unpickle_pure_python, django_template, pidigits, create_gc_cycles, async_tree_memoization_tg, deepcopy_memo, thrift, generators, python_startup_no_site, async_generators, unpack_sequence, unpickle_list, pyflate, bench_thread_pool, genshi_xml, gc_traversal, pickle_dict, sqlglot_transpile, deltablue, hexiom

- Geometric mean (including insignificant results): 1.005x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x