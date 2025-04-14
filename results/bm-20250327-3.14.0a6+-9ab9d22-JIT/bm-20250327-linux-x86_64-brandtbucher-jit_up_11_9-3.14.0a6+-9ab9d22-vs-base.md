# Results vs. base

- fork: brandtbucher
- ref: jit_up_11_9
- machine: linux-x86_64
- commit hash: 9ab9d22
- commit date: 2025-03-27
- overall geometric mean: 1.003x slower
- HPT reliability: 82.60%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_9-3.14.0a6+-9ab9d22 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                 | 266 ms: 1.01x slower                                                |
| docutils       | 2.69 sec                                                               | 2.71 sec: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_9-3.14.0a6+-9ab9d22 |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coroutines              | 24.1 ms                                                                | 23.6 ms: 1.02x faster                                               |
| async_tree_none         | 266 ms                                                                 | 262 ms: 1.02x faster                                                |
| async_tree_memoization  | 319 ms                                                                 | 315 ms: 1.01x faster                                                |
| async_tree_none_tg      | 255 ms                                                                 | 253 ms: 1.01x faster                                                |
| async_generators        | 418 ms                                                                 | 416 ms: 1.00x faster                                                |
| async_tree_cpu_io_mixed | 492 ms                                                                 | 494 ms: 1.00x slower                                                |
| Geometric mean          | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_tree_io, async_tree_io_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_9-3.14.0a6+-9ab9d22 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 89.4 ms                                                                | 88.0 ms: 1.02x faster                                               |
| pidigits       | 186 ms                                                                 | 185 ms: 1.00x faster                                                |
| float          | 64.9 ms                                                                | 65.2 ms: 1.00x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_9-3.14.0a6+-9ab9d22 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 217 ms                                                                 | 215 ms: 1.01x faster                                                |
| regex_compile  | 128 ms                                                                 | 129 ms: 1.01x slower                                                |
| regex_effbot   | 3.16 ms                                                                | 3.26 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_9-3.14.0a6+-9ab9d22 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_loads           | 30.1 us                                                                | 29.8 us: 1.01x faster                                               |
| unpickle_pure_python | 214 us                                                                 | 212 us: 1.01x faster                                                |
| json_dumps           | 11.6 ms                                                                | 11.6 ms: 1.01x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (6): pickle_pure_python, xml_etree_process, xml_etree_parse, xml_etree_generate, xml_etree_iterparse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_9-3.14.0a6+-9ab9d22 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                               |
| python_startup_no_site | 8.19 ms                                                                | 8.18 ms: 1.00x faster                                               |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_9-3.14.0a6+-9ab9d22 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 49.8 ms                                                                | 49.3 ms: 1.01x faster                                               |
| django_template | 32.0 ms                                                                | 32.4 ms: 1.01x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark                | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_9-3.14.0a6+-9ab9d22 |
|--------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| gc_traversal             | 5.05 ms                                                                | 4.85 ms: 1.04x faster                                               |
| crypto_pyaes             | 78.3 ms                                                                | 75.4 ms: 1.04x faster                                               |
| scimark_lu               | 118 ms                                                                 | 114 ms: 1.03x faster                                                |
| coroutines               | 24.1 ms                                                                | 23.6 ms: 1.02x faster                                               |
| comprehensions           | 19.0 us                                                                | 18.6 us: 1.02x faster                                               |
| nbody                    | 89.4 ms                                                                | 88.0 ms: 1.02x faster                                               |
| async_tree_none          | 266 ms                                                                 | 262 ms: 1.02x faster                                                |
| raytrace                 | 269 ms                                                                 | 265 ms: 1.01x faster                                                |
| async_tree_memoization   | 319 ms                                                                 | 315 ms: 1.01x faster                                                |
| async_tree_none_tg       | 255 ms                                                                 | 253 ms: 1.01x faster                                                |
| json_loads               | 30.1 us                                                                | 29.8 us: 1.01x faster                                               |
| chaos                    | 60.3 ms                                                                | 59.7 ms: 1.01x faster                                               |
| genshi_xml               | 49.8 ms                                                                | 49.3 ms: 1.01x faster                                               |
| generators               | 29.2 ms                                                                | 29.0 ms: 1.01x faster                                               |
| scimark_sor              | 119 ms                                                                 | 117 ms: 1.01x faster                                                |
| go                       | 128 ms                                                                 | 127 ms: 1.01x faster                                                |
| scimark_monte_carlo      | 68.6 ms                                                                | 68.1 ms: 1.01x faster                                               |
| unpickle_pure_python     | 214 us                                                                 | 212 us: 1.01x faster                                                |
| regex_dna                | 217 ms                                                                 | 215 ms: 1.01x faster                                                |
| dulwich_log              | 60.6 ms                                                                | 60.3 ms: 1.01x faster                                               |
| deltablue                | 3.06 ms                                                                | 3.04 ms: 1.01x faster                                               |
| bench_mp_pool            | 83.3 ms                                                                | 82.9 ms: 1.01x faster                                               |
| deepcopy_memo            | 29.0 us                                                                | 28.8 us: 1.01x faster                                               |
| pathlib                  | 16.8 ms                                                                | 16.7 ms: 1.00x faster                                               |
| async_generators         | 418 ms                                                                 | 416 ms: 1.00x faster                                                |
| bench_thread_pool        | 882 us                                                                 | 879 us: 1.00x faster                                                |
| python_startup           | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                               |
| pidigits                 | 186 ms                                                                 | 185 ms: 1.00x faster                                                |
| python_startup_no_site   | 8.19 ms                                                                | 8.18 ms: 1.00x faster                                               |
| create_gc_cycles         | 2.48 ms                                                                | 2.49 ms: 1.00x slower                                               |
| async_tree_cpu_io_mixed  | 492 ms                                                                 | 494 ms: 1.00x slower                                                |
| float                    | 64.9 ms                                                                | 65.2 ms: 1.00x slower                                               |
| sqlglot_v2_parse         | 1.29 ms                                                                | 1.29 ms: 1.00x slower                                               |
| subparsers               | 21.0 ms                                                                | 21.2 ms: 1.01x slower                                               |
| sympy_expand             | 475 ms                                                                 | 477 ms: 1.01x slower                                                |
| json_dumps               | 11.6 ms                                                                | 11.6 ms: 1.01x slower                                               |
| sqlglot_v2_optimize      | 54.1 ms                                                                | 54.5 ms: 1.01x slower                                               |
| regex_compile            | 128 ms                                                                 | 129 ms: 1.01x slower                                                |
| sympy_str                | 274 ms                                                                 | 276 ms: 1.01x slower                                                |
| docutils                 | 2.69 sec                                                               | 2.71 sec: 1.01x slower                                              |
| pyflate                  | 432 ms                                                                 | 435 ms: 1.01x slower                                                |
| pprint_safe_repr         | 756 ms                                                                 | 764 ms: 1.01x slower                                                |
| sympy_integrate          | 20.0 ms                                                                | 20.3 ms: 1.01x slower                                               |
| django_template          | 32.0 ms                                                                | 32.4 ms: 1.01x slower                                               |
| sqlglot_v2_transpile     | 1.61 ms                                                                | 1.62 ms: 1.01x slower                                               |
| json                     | 5.29 ms                                                                | 5.35 ms: 1.01x slower                                               |
| typing_runtime_protocols | 167 us                                                                 | 169 us: 1.01x slower                                                |
| pprint_pformat           | 1.55 sec                                                               | 1.57 sec: 1.01x slower                                              |
| telco                    | 7.93 ms                                                                | 8.04 ms: 1.01x slower                                               |
| 2to3                     | 263 ms                                                                 | 266 ms: 1.01x slower                                                |
| scimark_sparse_mat_mult  | 4.61 ms                                                                | 4.67 ms: 1.01x slower                                               |
| sqlglot_v2_normalize     | 107 ms                                                                 | 109 ms: 1.02x slower                                                |
| sqlalchemy_declarative   | 133 ms                                                                 | 135 ms: 1.02x slower                                                |
| sympy_sum                | 152 ms                                                                 | 154 ms: 1.02x slower                                                |
| nqueens                  | 84.9 ms                                                                | 86.4 ms: 1.02x slower                                               |
| connected_components     | 454 ms                                                                 | 462 ms: 1.02x slower                                                |
| many_optionals           | 970 us                                                                 | 991 us: 1.02x slower                                                |
| mdp                      | 2.48 sec                                                               | 2.53 sec: 1.02x slower                                              |
| deepcopy                 | 260 us                                                                 | 266 us: 1.02x slower                                                |
| sqlalchemy_imperative    | 17.1 ms                                                                | 17.5 ms: 1.03x slower                                               |
| regex_effbot             | 3.16 ms                                                                | 3.26 ms: 1.03x slower                                               |
| deepcopy_reduce          | 2.66 us                                                                | 2.77 us: 1.04x slower                                               |
| pycparser                | 1.13 sec                                                               | 1.19 sec: 1.05x slower                                              |
| richards                 | 35.8 ms                                                                | 37.8 ms: 1.06x slower                                               |
| richards_super           | 41.1 ms                                                                | 43.8 ms: 1.07x slower                                               |
| Geometric mean           | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (31): spectral_norm, async_tree_memoization_tg, async_tree_io, pickle_pure_python, xml_etree_process, regex_v8, async_tree_io_tg, logging_format, logging_silent, asyncio_websockets, scimark_fft, k_core, async_tree_cpu_io_mixed_tg, logging_simple, xml_etree_parse, hexiom, shortest_path, html5lib, meteor_contest, xml_etree_generate, genshi_text, fannkuch, sqlite_synth, xml_etree_iterparse, tomli_loads, mako, bpe_tokeniser, pylint, coverage, thrift, sphinx

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 82.60% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x