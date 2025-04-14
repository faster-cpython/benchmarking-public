# Results vs. base

- fork: iritkatriel
- ref: binaryops
- machine: linux-x86_64
- commit hash: c57fe46
- commit date: 2025-01-16
- overall geometric mean: 1.004x slower
- HPT reliability: 99.89%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4+-27494dd | bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-c57fe46 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 254 ms: 1.00x slower                                             |
| docutils       | 2.58 sec                                                               | 2.60 sec: 1.01x slower                                           |
| html5lib       | 61.1 ms                                                                | 61.7 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                     |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4+-27494dd | bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-c57fe46 |
|------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_generators | 389 ms                                                                 | 384 ms: 1.01x faster                                             |
| coroutines       | 23.3 ms                                                                | 23.5 ms: 1.01x slower                                            |
| Geometric mean   | (ref)                                                                  | 1.00x slower                                                     |

Benchmark hidden because not significant (9): async_tree_none, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4+-27494dd | bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-c57fe46 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                             |
| float          | 70.1 ms                                                                | 72.0 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                     |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4+-27494dd | bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-c57fe46 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 216 ms                                                                 | 218 ms: 1.01x slower                                             |
| regex_effbot   | 3.25 ms                                                                | 3.29 ms: 1.01x slower                                            |
| regex_compile  | 125 ms                                                                 | 127 ms: 1.01x slower                                             |
| regex_v8       | 25.2 ms                                                                | 25.7 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4+-27494dd | bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-c57fe46 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 221 us                                                                 | 217 us: 1.02x faster                                             |
| json_dumps           | 12.0 ms                                                                | 11.8 ms: 1.01x faster                                            |
| pickle_pure_python   | 323 us                                                                 | 320 us: 1.01x faster                                             |
| tomli_loads          | 1.96 sec                                                               | 1.97 sec: 1.01x slower                                           |
| xml_etree_generate   | 84.4 ms                                                                | 85.3 ms: 1.01x slower                                            |
| xml_etree_process    | 59.6 ms                                                                | 60.6 ms: 1.02x slower                                            |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                     |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4+-27494dd | bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-c57fe46 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 7.05 ms                                                                | 7.08 ms: 1.00x slower                                            |
| python_startup         | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                            |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4+-27494dd | bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-c57fe46 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| django_template | 31.8 ms                                                                | 32.1 ms: 1.01x slower                                            |
| genshi_xml      | 47.6 ms                                                                | 48.2 ms: 1.01x slower                                            |
| genshi_text     | 21.1 ms                                                                | 21.7 ms: 1.03x slower                                            |
| mako            | 11.2 ms                                                                | 11.8 ms: 1.05x slower                                            |
| Geometric mean  | (ref)                                                                  | 1.03x slower                                                     |

All benchmarks:
===============

| Benchmark               | bm-20250116-linux-x86_64-python-27494dd9ad6032c29e27-3.14.0a4+-27494dd | bm-20250116-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-c57fe46 |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| telco                   | 8.04 ms                                                                | 7.76 ms: 1.04x faster                                            |
| scimark_lu              | 119 ms                                                                 | 116 ms: 1.03x faster                                             |
| scimark_monte_carlo     | 68.6 ms                                                                | 67.1 ms: 1.02x faster                                            |
| unpickle_pure_python    | 221 us                                                                 | 217 us: 1.02x faster                                             |
| scimark_sor             | 124 ms                                                                 | 121 ms: 1.02x faster                                             |
| scimark_fft             | 349 ms                                                                 | 343 ms: 1.02x faster                                             |
| json_dumps              | 12.0 ms                                                                | 11.8 ms: 1.01x faster                                            |
| async_generators        | 389 ms                                                                 | 384 ms: 1.01x faster                                             |
| fannkuch                | 407 ms                                                                 | 403 ms: 1.01x faster                                             |
| meteor_contest          | 107 ms                                                                 | 106 ms: 1.01x faster                                             |
| pickle_pure_python      | 323 us                                                                 | 320 us: 1.01x faster                                             |
| subparsers              | 20.5 ms                                                                | 20.4 ms: 1.01x faster                                            |
| nqueens                 | 81.0 ms                                                                | 80.6 ms: 1.01x faster                                            |
| pidigits                | 186 ms                                                                 | 186 ms: 1.00x slower                                             |
| hexiom                  | 6.23 ms                                                                | 6.24 ms: 1.00x slower                                            |
| sqlglot_optimize        | 52.7 ms                                                                | 52.8 ms: 1.00x slower                                            |
| 2to3                    | 253 ms                                                                 | 254 ms: 1.00x slower                                             |
| python_startup_no_site  | 7.05 ms                                                                | 7.08 ms: 1.00x slower                                            |
| python_startup          | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                            |
| go                      | 118 ms                                                                 | 118 ms: 1.00x slower                                             |
| sqlglot_parse           | 1.26 ms                                                                | 1.27 ms: 1.00x slower                                            |
| bench_thread_pool       | 863 us                                                                 | 867 us: 1.00x slower                                             |
| sqlglot_normalize       | 105 ms                                                                 | 105 ms: 1.00x slower                                             |
| chaos                   | 57.8 ms                                                                | 58.1 ms: 1.00x slower                                            |
| scimark_sparse_mat_mult | 4.69 ms                                                                | 4.71 ms: 1.01x slower                                            |
| thrift                  | 756 us                                                                 | 759 us: 1.01x slower                                             |
| docutils                | 2.58 sec                                                               | 2.60 sec: 1.01x slower                                           |
| tomli_loads             | 1.96 sec                                                               | 1.97 sec: 1.01x slower                                           |
| richards                | 44.3 ms                                                                | 44.6 ms: 1.01x slower                                            |
| create_gc_cycles        | 2.46 ms                                                                | 2.47 ms: 1.01x slower                                            |
| pprint_pformat          | 1.49 sec                                                               | 1.50 sec: 1.01x slower                                           |
| regex_dna               | 216 ms                                                                 | 218 ms: 1.01x slower                                             |
| coroutines              | 23.3 ms                                                                | 23.5 ms: 1.01x slower                                            |
| pprint_safe_repr        | 725 ms                                                                 | 731 ms: 1.01x slower                                             |
| richards_super          | 50.7 ms                                                                | 51.2 ms: 1.01x slower                                            |
| django_template         | 31.8 ms                                                                | 32.1 ms: 1.01x slower                                            |
| sympy_integrate         | 19.7 ms                                                                | 19.8 ms: 1.01x slower                                            |
| html5lib                | 61.1 ms                                                                | 61.7 ms: 1.01x slower                                            |
| sympy_str               | 265 ms                                                                 | 267 ms: 1.01x slower                                             |
| shortest_path           | 476 ms                                                                 | 481 ms: 1.01x slower                                             |
| sympy_expand            | 450 ms                                                                 | 455 ms: 1.01x slower                                             |
| regex_effbot            | 3.25 ms                                                                | 3.29 ms: 1.01x slower                                            |
| xml_etree_generate      | 84.4 ms                                                                | 85.3 ms: 1.01x slower                                            |
| sqlalchemy_declarative  | 129 ms                                                                 | 130 ms: 1.01x slower                                             |
| deepcopy                | 255 us                                                                 | 258 us: 1.01x slower                                             |
| mdp                     | 2.46 sec                                                               | 2.49 sec: 1.01x slower                                           |
| pathlib                 | 16.1 ms                                                                | 16.4 ms: 1.01x slower                                            |
| sqlalchemy_imperative   | 16.3 ms                                                                | 16.5 ms: 1.01x slower                                            |
| genshi_xml              | 47.6 ms                                                                | 48.2 ms: 1.01x slower                                            |
| raytrace                | 270 ms                                                                 | 274 ms: 1.01x slower                                             |
| many_optionals          | 933 us                                                                 | 946 us: 1.01x slower                                             |
| regex_compile           | 125 ms                                                                 | 127 ms: 1.01x slower                                             |
| logging_format          | 5.93 us                                                                | 6.03 us: 1.02x slower                                            |
| xml_etree_process       | 59.6 ms                                                                | 60.6 ms: 1.02x slower                                            |
| logging_simple          | 5.36 us                                                                | 5.45 us: 1.02x slower                                            |
| deepcopy_memo           | 30.7 us                                                                | 31.3 us: 1.02x slower                                            |
| regex_v8                | 25.2 ms                                                                | 25.7 ms: 1.02x slower                                            |
| deepcopy_reduce         | 2.60 us                                                                | 2.65 us: 1.02x slower                                            |
| deltablue               | 3.18 ms                                                                | 3.25 ms: 1.02x slower                                            |
| float                   | 70.1 ms                                                                | 72.0 ms: 1.03x slower                                            |
| genshi_text             | 21.1 ms                                                                | 21.7 ms: 1.03x slower                                            |
| gc_traversal            | 4.78 ms                                                                | 4.93 ms: 1.03x slower                                            |
| crypto_pyaes            | 71.3 ms                                                                | 74.0 ms: 1.04x slower                                            |
| logging_silent          | 105 ns                                                                 | 111 ns: 1.05x slower                                             |
| mako                    | 11.2 ms                                                                | 11.8 ms: 1.05x slower                                            |
| Geometric mean          | (ref)                                                                  | 1.01x slower                                                     |

Benchmark hidden because not significant (31): nbody, sqlite_synth, xml_etree_iterparse, typing_runtime_protocols, bench_mp_pool, async_tree_none, pyflate, async_tree_cpu_io_mixed, xml_etree_parse, asyncio_websockets, spectral_norm, pycparser, async_tree_io, coverage, dulwich_log, comprehensions, bpe_tokeniser, generators, json_loads, sympy_sum, async_tree_cpu_io_mixed_tg, json, sqlglot_transpile, async_tree_none_tg, async_tree_io_tg, async_tree_memoization_tg, sphinx, async_tree_memoization, connected_components, pylint, k_core

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 99.89% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x