# Results vs. base

- fork: faster-cpython
- ref: better_instrument_fo
- machine: linux-x86_64
- commit hash: 182c512
- commit date: 2024-12-31
- overall geometric mean: 1.001x faster
- HPT reliability: 92.59%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241231-linux-x86_64-python-e389d6c650ddacb55b08-3.14.0a3+-e389d6c | bm-20241231-linux-x86_64-faster%2dcpython-better_instrument_fo-3.14.0a3+-182c512 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                                 | 255 ms: 1.00x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241231-linux-x86_64-python-e389d6c650ddacb55b08-3.14.0a3+-e389d6c | bm-20241231-linux-x86_64-faster%2dcpython-better_instrument_fo-3.14.0a3+-182c512 |
|------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| coroutines       | 23.6 ms                                                                | 23.2 ms: 1.02x faster                                                            |
| async_generators | 423 ms                                                                 | 421 ms: 1.00x faster                                                             |
| Geometric mean   | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (9): async_tree_memoization_tg, asyncio_websockets, async_tree_none_tg, async_tree_io_tg, async_tree_none, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241231-linux-x86_64-python-e389d6c650ddacb55b08-3.14.0a3+-e389d6c | bm-20241231-linux-x86_64-faster%2dcpython-better_instrument_fo-3.14.0a3+-182c512 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                                             |
| nbody          | 92.4 ms                                                                | 95.9 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241231-linux-x86_64-python-e389d6c650ddacb55b08-3.14.0a3+-e389d6c | bm-20241231-linux-x86_64-faster%2dcpython-better_instrument_fo-3.14.0a3+-182c512 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.48 ms                                                                | 3.28 ms: 1.06x faster                                                            |
| regex_compile  | 128 ms                                                                 | 128 ms: 1.00x faster                                                             |
| regex_dna      | 218 ms                                                                 | 221 ms: 1.01x slower                                                             |
| regex_v8       | 24.7 ms                                                                | 25.4 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241231-linux-x86_64-python-e389d6c650ddacb55b08-3.14.0a3+-e389d6c | bm-20241231-linux-x86_64-faster%2dcpython-better_instrument_fo-3.14.0a3+-182c512 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 324 us                                                                 | 320 us: 1.01x faster                                                             |
| xml_etree_parse      | 138 ms                                                                 | 137 ms: 1.01x faster                                                             |
| unpickle_pure_python | 217 us                                                                 | 218 us: 1.00x slower                                                             |
| tomli_loads          | 1.99 sec                                                               | 2.01 sec: 1.01x slower                                                           |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (5): xml_etree_process, xml_etree_generate, json_dumps, xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241231-linux-x86_64-python-e389d6c650ddacb55b08-3.14.0a3+-e389d6c | bm-20241231-linux-x86_64-faster%2dcpython-better_instrument_fo-3.14.0a3+-182c512 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 12.9 ms                                                                | 12.8 ms: 1.00x faster                                                            |
| python_startup_no_site | 7.07 ms                                                                | 7.07 ms: 1.00x slower                                                            |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241231-linux-x86_64-python-e389d6c650ddacb55b08-3.14.0a3+-e389d6c | bm-20241231-linux-x86_64-faster%2dcpython-better_instrument_fo-3.14.0a3+-182c512 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 11.7 ms                                                                | 11.4 ms: 1.02x faster                                                            |
| genshi_text     | 22.7 ms                                                                | 22.4 ms: 1.02x faster                                                            |
| genshi_xml      | 50.2 ms                                                                | 49.8 ms: 1.01x faster                                                            |
| django_template | 31.4 ms                                                                | 32.0 ms: 1.02x slower                                                            |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20241231-linux-x86_64-python-e389d6c650ddacb55b08-3.14.0a3+-e389d6c | bm-20241231-linux-x86_64-faster%2dcpython-better_instrument_fo-3.14.0a3+-182c512 |
|--------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot             | 3.48 ms                                                                | 3.28 ms: 1.06x faster                                                            |
| scimark_sparse_mat_mult  | 4.82 ms                                                                | 4.64 ms: 1.04x faster                                                            |
| mdp                      | 2.63 sec                                                               | 2.54 sec: 1.03x faster                                                           |
| mako                     | 11.7 ms                                                                | 11.4 ms: 1.02x faster                                                            |
| comprehensions           | 17.1 us                                                                | 16.7 us: 1.02x faster                                                            |
| coverage                 | 85.0 ms                                                                | 83.4 ms: 1.02x faster                                                            |
| deltablue                | 3.32 ms                                                                | 3.26 ms: 1.02x faster                                                            |
| generators               | 28.1 ms                                                                | 27.6 ms: 1.02x faster                                                            |
| gc_traversal             | 5.03 ms                                                                | 4.95 ms: 1.02x faster                                                            |
| meteor_contest           | 109 ms                                                                 | 107 ms: 1.02x faster                                                             |
| deepcopy_memo            | 31.2 us                                                                | 30.7 us: 1.02x faster                                                            |
| spectral_norm            | 107 ms                                                                 | 105 ms: 1.02x faster                                                             |
| coroutines               | 23.6 ms                                                                | 23.2 ms: 1.02x faster                                                            |
| genshi_text              | 22.7 ms                                                                | 22.4 ms: 1.02x faster                                                            |
| pickle_pure_python       | 324 us                                                                 | 320 us: 1.01x faster                                                             |
| scimark_fft              | 350 ms                                                                 | 346 ms: 1.01x faster                                                             |
| xml_etree_parse          | 138 ms                                                                 | 137 ms: 1.01x faster                                                             |
| go                       | 119 ms                                                                 | 117 ms: 1.01x faster                                                             |
| sqlite_synth             | 2.82 us                                                                | 2.80 us: 1.01x faster                                                            |
| telco                    | 7.82 ms                                                                | 7.74 ms: 1.01x faster                                                            |
| deepcopy                 | 261 us                                                                 | 258 us: 1.01x faster                                                             |
| chaos                    | 61.0 ms                                                                | 60.5 ms: 1.01x faster                                                            |
| genshi_xml               | 50.2 ms                                                                | 49.8 ms: 1.01x faster                                                            |
| richards                 | 43.9 ms                                                                | 43.6 ms: 1.01x faster                                                            |
| sympy_expand             | 458 ms                                                                 | 455 ms: 1.01x faster                                                             |
| richards_super           | 50.8 ms                                                                | 50.5 ms: 1.00x faster                                                            |
| async_generators         | 423 ms                                                                 | 421 ms: 1.00x faster                                                             |
| regex_compile            | 128 ms                                                                 | 128 ms: 1.00x faster                                                             |
| python_startup           | 12.9 ms                                                                | 12.8 ms: 1.00x faster                                                            |
| python_startup_no_site   | 7.07 ms                                                                | 7.07 ms: 1.00x slower                                                            |
| 2to3                     | 255 ms                                                                 | 255 ms: 1.00x slower                                                             |
| pidigits                 | 186 ms                                                                 | 186 ms: 1.00x slower                                                             |
| sqlalchemy_declarative   | 129 ms                                                                 | 129 ms: 1.00x slower                                                             |
| sqlglot_optimize         | 52.6 ms                                                                | 52.7 ms: 1.00x slower                                                            |
| unpickle_pure_python     | 217 us                                                                 | 218 us: 1.00x slower                                                             |
| dulwich_log              | 63.9 ms                                                                | 64.1 ms: 1.00x slower                                                            |
| pprint_pformat           | 1.48 sec                                                               | 1.48 sec: 1.00x slower                                                           |
| sqlglot_transpile        | 1.58 ms                                                                | 1.59 ms: 1.01x slower                                                            |
| bpe_tokeniser            | 4.52 sec                                                               | 4.55 sec: 1.01x slower                                                           |
| sqlglot_normalize        | 104 ms                                                                 | 104 ms: 1.01x slower                                                             |
| scimark_monte_carlo      | 67.3 ms                                                                | 67.7 ms: 1.01x slower                                                            |
| subparsers               | 20.6 ms                                                                | 20.7 ms: 1.01x slower                                                            |
| logging_simple           | 5.56 us                                                                | 5.61 us: 1.01x slower                                                            |
| tomli_loads              | 1.99 sec                                                               | 2.01 sec: 1.01x slower                                                           |
| regex_dna                | 218 ms                                                                 | 221 ms: 1.01x slower                                                             |
| typing_runtime_protocols | 160 us                                                                 | 162 us: 1.01x slower                                                             |
| hexiom                   | 6.21 ms                                                                | 6.28 ms: 1.01x slower                                                            |
| scimark_sor              | 122 ms                                                                 | 123 ms: 1.01x slower                                                             |
| pprint_safe_repr         | 723 ms                                                                 | 733 ms: 1.02x slower                                                             |
| nqueens                  | 80.1 ms                                                                | 81.3 ms: 1.02x slower                                                            |
| django_template          | 31.4 ms                                                                | 32.0 ms: 1.02x slower                                                            |
| pyflate                  | 450 ms                                                                 | 459 ms: 1.02x slower                                                             |
| logging_silent           | 105 ns                                                                 | 108 ns: 1.02x slower                                                             |
| regex_v8                 | 24.7 ms                                                                | 25.4 ms: 1.03x slower                                                            |
| fannkuch                 | 399 ms                                                                 | 410 ms: 1.03x slower                                                             |
| pathlib                  | 15.6 ms                                                                | 16.1 ms: 1.03x slower                                                            |
| crypto_pyaes             | 69.3 ms                                                                | 71.4 ms: 1.03x slower                                                            |
| pycparser                | 1.13 sec                                                               | 1.17 sec: 1.03x slower                                                           |
| nbody                    | 92.4 ms                                                                | 95.9 ms: 1.04x slower                                                            |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (39): djangocms, k_core, async_tree_memoization_tg, connected_components, xml_etree_process, xml_etree_generate, docutils, logging_format, sympy_str, json, sympy_sum, mypy2, pylint, sympy_integrate, many_optionals, bench_thread_pool, raytrace, sqlalchemy_imperative, create_gc_cycles, shortest_path, float, json_dumps, asyncio_websockets, thrift, async_tree_none_tg, bench_mp_pool, async_tree_io_tg, async_tree_none, xml_etree_iterparse, sqlglot_parse, async_tree_io, deepcopy_reduce, json_loads, async_tree_cpu_io_mixed_tg, async_tree_memoization, scimark_lu, async_tree_cpu_io_mixed, sphinx, html5lib

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 92.59% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x