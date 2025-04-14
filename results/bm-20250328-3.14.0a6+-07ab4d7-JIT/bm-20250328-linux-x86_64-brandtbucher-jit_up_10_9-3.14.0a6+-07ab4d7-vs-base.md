# Results vs. base

- fork: brandtbucher
- ref: jit_up_10_9
- machine: linux-x86_64
- commit hash: 07ab4d7
- commit date: 2025-03-28
- overall geometric mean: 1.007x slower
- HPT reliability: 98.64%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_9-3.14.0a6+-07ab4d7 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                 | 266 ms: 1.01x slower                                                |
| docutils       | 2.69 sec                                                               | 2.70 sec: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_9-3.14.0a6+-07ab4d7 |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coroutines              | 24.1 ms                                                                | 23.7 ms: 1.02x faster                                               |
| async_tree_none         | 266 ms                                                                 | 262 ms: 1.01x faster                                                |
| async_generators        | 418 ms                                                                 | 414 ms: 1.01x faster                                                |
| async_tree_cpu_io_mixed | 492 ms                                                                 | 495 ms: 1.01x slower                                                |
| async_tree_memoization  | 319 ms                                                                 | 323 ms: 1.01x slower                                                |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (6): async_tree_io, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_9-3.14.0a6+-07ab4d7 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 89.4 ms                                                                | 88.0 ms: 1.02x faster                                               |
| pidigits       | 186 ms                                                                 | 185 ms: 1.00x faster                                                |
| float          | 64.9 ms                                                                | 66.1 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_9-3.14.0a6+-07ab4d7 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 217 ms                                                                 | 214 ms: 1.01x faster                                                |
| regex_compile  | 128 ms                                                                 | 129 ms: 1.01x slower                                                |
| regex_effbot   | 3.16 ms                                                                | 3.40 ms: 1.08x slower                                               |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                        |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_9-3.14.0a6+-07ab4d7 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_loads           | 30.1 us                                                                | 29.6 us: 1.02x faster                                               |
| unpickle_pure_python | 214 us                                                                 | 212 us: 1.01x faster                                                |
| xml_etree_generate   | 80.8 ms                                                                | 80.4 ms: 1.01x faster                                               |
| xml_etree_iterparse  | 97.6 ms                                                                | 98.0 ms: 1.00x slower                                               |
| json_dumps           | 11.6 ms                                                                | 11.7 ms: 1.01x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (4): xml_etree_process, xml_etree_parse, tomli_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_9-3.14.0a6+-07ab4d7 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                               |
| python_startup_no_site | 8.19 ms                                                                | 8.21 ms: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_9-3.14.0a6+-07ab4d7 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 32.0 ms                                                                | 31.7 ms: 1.01x faster                                               |
| genshi_text     | 21.4 ms                                                                | 21.3 ms: 1.01x faster                                               |
| mako            | 11.0 ms                                                                | 11.0 ms: 1.00x faster                                               |
| genshi_xml      | 49.8 ms                                                                | 50.6 ms: 1.02x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250328-linux-x86_64-brandtbucher-jit_up_10_9-3.14.0a6+-07ab4d7 |
|--------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| spectral_norm            | 97.1 ms                                                                | 91.9 ms: 1.06x faster                                               |
| gc_traversal             | 5.05 ms                                                                | 4.82 ms: 1.05x faster                                               |
| crypto_pyaes             | 78.3 ms                                                                | 75.5 ms: 1.04x faster                                               |
| json_loads               | 30.1 us                                                                | 29.6 us: 1.02x faster                                               |
| coroutines               | 24.1 ms                                                                | 23.7 ms: 1.02x faster                                               |
| nbody                    | 89.4 ms                                                                | 88.0 ms: 1.02x faster                                               |
| async_tree_none          | 266 ms                                                                 | 262 ms: 1.01x faster                                                |
| generators               | 29.2 ms                                                                | 28.9 ms: 1.01x faster                                               |
| scimark_lu               | 118 ms                                                                 | 116 ms: 1.01x faster                                                |
| django_template          | 32.0 ms                                                                | 31.7 ms: 1.01x faster                                               |
| regex_dna                | 217 ms                                                                 | 214 ms: 1.01x faster                                                |
| async_generators         | 418 ms                                                                 | 414 ms: 1.01x faster                                                |
| unpickle_pure_python     | 214 us                                                                 | 212 us: 1.01x faster                                                |
| shortest_path            | 494 ms                                                                 | 490 ms: 1.01x faster                                                |
| chaos                    | 60.3 ms                                                                | 60.0 ms: 1.01x faster                                               |
| genshi_text              | 21.4 ms                                                                | 21.3 ms: 1.01x faster                                               |
| subparsers               | 21.0 ms                                                                | 20.9 ms: 1.01x faster                                               |
| xml_etree_generate       | 80.8 ms                                                                | 80.4 ms: 1.01x faster                                               |
| scimark_monte_carlo      | 68.6 ms                                                                | 68.3 ms: 1.01x faster                                               |
| deepcopy_memo            | 29.0 us                                                                | 28.8 us: 1.00x faster                                               |
| mako                     | 11.0 ms                                                                | 11.0 ms: 1.00x faster                                               |
| pidigits                 | 186 ms                                                                 | 185 ms: 1.00x faster                                                |
| python_startup           | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                               |
| python_startup_no_site   | 8.19 ms                                                                | 8.21 ms: 1.00x slower                                               |
| create_gc_cycles         | 2.48 ms                                                                | 2.49 ms: 1.00x slower                                               |
| scimark_fft              | 312 ms                                                                 | 313 ms: 1.00x slower                                                |
| xml_etree_iterparse      | 97.6 ms                                                                | 98.0 ms: 1.00x slower                                               |
| mdp                      | 2.48 sec                                                               | 2.49 sec: 1.00x slower                                              |
| sqlite_synth             | 2.72 us                                                                | 2.73 us: 1.00x slower                                               |
| pathlib                  | 16.8 ms                                                                | 16.8 ms: 1.01x slower                                               |
| docutils                 | 2.69 sec                                                               | 2.70 sec: 1.01x slower                                              |
| async_tree_cpu_io_mixed  | 492 ms                                                                 | 495 ms: 1.01x slower                                                |
| bench_thread_pool        | 882 us                                                                 | 888 us: 1.01x slower                                                |
| regex_compile            | 128 ms                                                                 | 129 ms: 1.01x slower                                                |
| sqlglot_v2_parse         | 1.29 ms                                                                | 1.30 ms: 1.01x slower                                               |
| fannkuch                 | 423 ms                                                                 | 427 ms: 1.01x slower                                                |
| sympy_expand             | 475 ms                                                                 | 479 ms: 1.01x slower                                                |
| json_dumps               | 11.6 ms                                                                | 11.7 ms: 1.01x slower                                               |
| coverage                 | 85.5 ms                                                                | 86.5 ms: 1.01x slower                                               |
| nqueens                  | 84.9 ms                                                                | 85.8 ms: 1.01x slower                                               |
| 2to3                     | 263 ms                                                                 | 266 ms: 1.01x slower                                                |
| sqlglot_v2_optimize      | 54.1 ms                                                                | 54.8 ms: 1.01x slower                                               |
| meteor_contest           | 108 ms                                                                 | 110 ms: 1.01x slower                                                |
| async_tree_memoization   | 319 ms                                                                 | 323 ms: 1.01x slower                                                |
| many_optionals           | 970 us                                                                 | 985 us: 1.01x slower                                                |
| sympy_str                | 274 ms                                                                 | 279 ms: 1.02x slower                                                |
| genshi_xml               | 49.8 ms                                                                | 50.6 ms: 1.02x slower                                               |
| sqlglot_v2_transpile     | 1.61 ms                                                                | 1.63 ms: 1.02x slower                                               |
| float                    | 64.9 ms                                                                | 66.1 ms: 1.02x slower                                               |
| sqlalchemy_imperative    | 17.1 ms                                                                | 17.4 ms: 1.02x slower                                               |
| sympy_integrate          | 20.0 ms                                                                | 20.4 ms: 1.02x slower                                               |
| bpe_tokeniser            | 4.57 sec                                                               | 4.66 sec: 1.02x slower                                              |
| sqlalchemy_declarative   | 133 ms                                                                 | 136 ms: 1.02x slower                                                |
| sympy_sum                | 152 ms                                                                 | 155 ms: 1.02x slower                                                |
| sqlglot_v2_normalize     | 107 ms                                                                 | 110 ms: 1.02x slower                                                |
| deepcopy_reduce          | 2.66 us                                                                | 2.73 us: 1.02x slower                                               |
| scimark_sor              | 119 ms                                                                 | 122 ms: 1.03x slower                                                |
| hexiom                   | 6.86 ms                                                                | 7.10 ms: 1.03x slower                                               |
| typing_runtime_protocols | 167 us                                                                 | 173 us: 1.04x slower                                                |
| pycparser                | 1.13 sec                                                               | 1.17 sec: 1.04x slower                                              |
| scimark_sparse_mat_mult  | 4.61 ms                                                                | 4.81 ms: 1.04x slower                                               |
| pyflate                  | 432 ms                                                                 | 461 ms: 1.07x slower                                                |
| regex_effbot             | 3.16 ms                                                                | 3.40 ms: 1.08x slower                                               |
| connected_components     | 454 ms                                                                 | 494 ms: 1.09x slower                                                |
| logging_silent           | 95.7 ns                                                                | 105 ns: 1.09x slower                                                |
| richards_super           | 41.1 ms                                                                | 45.6 ms: 1.11x slower                                               |
| richards                 | 35.8 ms                                                                | 40.8 ms: 1.14x slower                                               |
| Geometric mean           | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (29): telco, async_tree_io, xml_etree_process, async_tree_none_tg, go, xml_etree_parse, pprint_pformat, thrift, async_tree_memoization_tg, bench_mp_pool, tomli_loads, async_tree_cpu_io_mixed_tg, raytrace, pickle_pure_python, deltablue, regex_v8, asyncio_websockets, logging_format, dulwich_log, k_core, logging_simple, json, async_tree_io_tg, sphinx, comprehensions, html5lib, deepcopy, pylint, pprint_safe_repr

- Geometric mean (including insignificant results): 1.007x slower

# HPT report

- Reliability score: 98.64% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x