# Results vs. base

- fork: nick-arm
- ref: codecache
- machine: linux-aarch64
- commit hash: aa18ec3
- commit date: 2024-10-07
- overall geometric mean: 1.01x faster
- HPT reliability: 98.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 385 ms                                                                  | 374 ms: 1.03x faster                                             |
| docutils       | 3.72 sec                                                                | 3.63 sec: 1.02x faster                                           |
| html5lib       | 71.9 ms                                                                 | 71.3 ms: 1.01x faster                                            |
| tornado_http   | 145 ms                                                                  | 142 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                                   | 1.02x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (13): async_tree_cpu_io_mixed, asyncio_tcp, asyncio_tcp_ssl, async_tree_io, asyncio_websockets, async_generators, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, coroutines, async_tree_memoization, async_tree_none_tg, async_tree_io_tg, async_tree_none

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 253 ms                                                                  | 247 ms: 1.03x faster                                             |
| regex_compile  | 185 ms                                                                  | 181 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                     |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|---------------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python  | 397 us                                                                  | 384 us: 1.03x faster                                             |
| xml_etree_process   | 82.5 ms                                                                 | 80.0 ms: 1.03x faster                                            |
| xml_etree_generate  | 113 ms                                                                  | 110 ms: 1.02x faster                                             |
| tomli_loads         | 2.64 sec                                                                | 2.61 sec: 1.01x faster                                           |
| unpickle_list       | 6.33 us                                                                 | 6.40 us: 1.01x slower                                            |
| xml_etree_iterparse | 148 ms                                                                  | 152 ms: 1.03x slower                                             |
| xml_etree_parse     | 187 ms                                                                  | 192 ms: 1.03x slower                                             |
| Geometric mean      | (ref)                                                                   | 1.00x faster                                                     |

Benchmark hidden because not significant (7): unpickle, json_loads, pickle, pickle_list, pickle_dict, json_dumps, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|------------------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                                 | 13.1 ms: 1.01x slower                                            |
| python_startup_no_site | 8.73 ms                                                                 | 8.81 ms: 1.01x slower                                            |
| Geometric mean         | (ref)                                                                   | 1.01x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|-----------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 13.0 ms                                                                 | 13.2 ms: 1.01x slower                                            |
| django_template | 51.0 ms                                                                 | 51.9 ms: 1.02x slower                                            |
| Geometric mean  | (ref)                                                                   | 1.00x slower                                                     |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|-------------------------|:-----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| dulwich_log             | 80.8 ms                                                                 | 76.0 ms: 1.06x faster                                            |
| richards                | 64.1 ms                                                                 | 60.3 ms: 1.06x faster                                            |
| pprint_pformat          | 2.61 sec                                                                | 2.50 sec: 1.04x faster                                           |
| deepcopy_reduce         | 4.01 us                                                                 | 3.85 us: 1.04x faster                                            |
| pprint_safe_repr        | 1.25 sec                                                                | 1.20 sec: 1.04x faster                                           |
| pyflate                 | 638 ms                                                                  | 617 ms: 1.03x faster                                             |
| pickle_pure_python      | 397 us                                                                  | 384 us: 1.03x faster                                             |
| logging_format          | 8.27 us                                                                 | 8.02 us: 1.03x faster                                            |
| xml_etree_process       | 82.5 ms                                                                 | 80.0 ms: 1.03x faster                                            |
| 2to3                    | 385 ms                                                                  | 374 ms: 1.03x faster                                             |
| scimark_monte_carlo     | 89.9 ms                                                                 | 87.5 ms: 1.03x faster                                            |
| nqueens                 | 125 ms                                                                  | 122 ms: 1.03x faster                                             |
| regex_dna               | 253 ms                                                                  | 247 ms: 1.03x faster                                             |
| docutils                | 3.72 sec                                                                | 3.63 sec: 1.02x faster                                           |
| tornado_http            | 145 ms                                                                  | 142 ms: 1.02x faster                                             |
| deepcopy_memo           | 38.3 us                                                                 | 37.4 us: 1.02x faster                                            |
| regex_compile           | 185 ms                                                                  | 181 ms: 1.02x faster                                             |
| sqlglot_optimize        | 82.1 ms                                                                 | 80.2 ms: 1.02x faster                                            |
| crypto_pyaes            | 90.1 ms                                                                 | 88.1 ms: 1.02x faster                                            |
| xml_etree_generate      | 113 ms                                                                  | 110 ms: 1.02x faster                                             |
| scimark_sparse_mat_mult | 6.91 ms                                                                 | 6.79 ms: 1.02x faster                                            |
| sqlglot_parse           | 1.71 ms                                                                 | 1.68 ms: 1.02x faster                                            |
| pathlib                 | 21.9 ms                                                                 | 21.5 ms: 1.02x faster                                            |
| logging_simple          | 7.51 us                                                                 | 7.40 us: 1.02x faster                                            |
| sympy_str               | 363 ms                                                                  | 358 ms: 1.01x faster                                             |
| sympy_integrate         | 29.2 ms                                                                 | 28.8 ms: 1.01x faster                                            |
| tomli_loads             | 2.64 sec                                                                | 2.61 sec: 1.01x faster                                           |
| scimark_fft             | 449 ms                                                                  | 444 ms: 1.01x faster                                             |
| pycparser               | 1.49 sec                                                                | 1.47 sec: 1.01x faster                                           |
| html5lib                | 71.9 ms                                                                 | 71.3 ms: 1.01x faster                                            |
| sqlglot_normalize       | 156 ms                                                                  | 155 ms: 1.01x faster                                             |
| python_startup          | 13.0 ms                                                                 | 13.1 ms: 1.01x slower                                            |
| python_startup_no_site  | 8.73 ms                                                                 | 8.81 ms: 1.01x slower                                            |
| mako                    | 13.0 ms                                                                 | 13.2 ms: 1.01x slower                                            |
| unpickle_list           | 6.33 us                                                                 | 6.40 us: 1.01x slower                                            |
| create_gc_cycles        | 2.28 ms                                                                 | 2.31 ms: 1.01x slower                                            |
| coverage                | 97.8 ms                                                                 | 99.2 ms: 1.01x slower                                            |
| go                      | 186 ms                                                                  | 189 ms: 1.02x slower                                             |
| logging_silent          | 131 ns                                                                  | 133 ns: 1.02x slower                                             |
| django_template         | 51.0 ms                                                                 | 51.9 ms: 1.02x slower                                            |
| xml_etree_iterparse     | 148 ms                                                                  | 152 ms: 1.03x slower                                             |
| xml_etree_parse         | 187 ms                                                                  | 192 ms: 1.03x slower                                             |
| gc_traversal            | 5.02 ms                                                                 | 5.21 ms: 1.04x slower                                            |
| telco                   | 9.41 ms                                                                 | 9.86 ms: 1.05x slower                                            |
| scimark_sor             | 152 ms                                                                  | 167 ms: 1.10x slower                                             |
| Geometric mean          | (ref)                                                                   | 1.01x faster                                                     |

Benchmark hidden because not significant (52): bench_mp_pool, pylint, richards_super, async_tree_cpu_io_mixed, genshi_xml, asyncio_tcp, spectral_norm, thrift, sympy_sum, chaos, unpack_sequence, fannkuch, raytrace, generators, regex_effbot, asyncio_tcp_ssl, async_tree_io, genshi_text, comprehensions, bench_thread_pool, unpickle, regex_v8, json_loads, bpe_tokeniser, pickle, asyncio_websockets, async_generators, async_tree_memoization_tg, pickle_list, pidigits, scimark_lu, async_tree_cpu_io_mixed_tg, float, coroutines, async_tree_memoization, hexiom, meteor_contest, async_tree_none_tg, sqlite_synth, sympy_expand, mdp, pickle_dict, deltablue, async_tree_io_tg, deepcopy, json_dumps, sqlglot_transpile, async_tree_none, unpickle_pure_python, typing_runtime_protocols, json, nbody

# HPT report

- Reliability score: 98.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x