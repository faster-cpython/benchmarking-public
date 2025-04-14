# Results vs. base

- fork: brandtbucher
- ref: jit_up_12_10
- machine: linux-x86_64
- commit hash: f2d447f
- commit date: 2025-03-26
- overall geometric mean: 1.003x slower
- HPT reliability: 98.91%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_10-3.14.0a6+-f2d447f |
|-------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization  | 319 ms                                                                 | 315 ms: 1.01x faster                                                 |
| async_tree_none_tg      | 255 ms                                                                 | 253 ms: 1.01x faster                                                 |
| async_tree_cpu_io_mixed | 492 ms                                                                 | 495 ms: 1.01x slower                                                 |
| async_generators        | 418 ms                                                                 | 421 ms: 1.01x slower                                                 |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (7): async_tree_io_tg, async_tree_memoization_tg, async_tree_none, async_tree_cpu_io_mixed_tg, asyncio_websockets, coroutines, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_10-3.14.0a6+-f2d447f |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 89.4 ms                                                                | 87.7 ms: 1.02x faster                                                |
| float          | 64.9 ms                                                                | 65.9 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_10-3.14.0a6+-f2d447f |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_dna      | 217 ms                                                                 | 209 ms: 1.04x faster                                                 |
| regex_v8       | 23.5 ms                                                                | 23.0 ms: 1.02x faster                                                |
| regex_effbot   | 3.16 ms                                                                | 3.13 ms: 1.01x faster                                                |
| regex_compile  | 128 ms                                                                 | 129 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_10-3.14.0a6+-f2d447f |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_process    | 57.1 ms                                                                | 56.6 ms: 1.01x faster                                                |
| unpickle_pure_python | 214 us                                                                 | 212 us: 1.01x faster                                                 |
| xml_etree_iterparse  | 97.6 ms                                                                | 98.8 ms: 1.01x slower                                                |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (6): json_loads, xml_etree_generate, pickle_pure_python, tomli_loads, json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_10-3.14.0a6+-f2d447f |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 8.19 ms                                                                | 8.20 ms: 1.00x slower                                                |
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                                |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_10-3.14.0a6+-f2d447f |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 32.0 ms                                                                | 31.8 ms: 1.01x faster                                                |
| genshi_xml      | 49.8 ms                                                                | 50.1 ms: 1.01x slower                                                |
| mako            | 11.0 ms                                                                | 11.1 ms: 1.01x slower                                                |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_10-3.14.0a6+-f2d447f |
|--------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| gc_traversal             | 5.05 ms                                                                | 4.81 ms: 1.05x faster                                                |
| regex_dna                | 217 ms                                                                 | 209 ms: 1.04x faster                                                 |
| regex_v8                 | 23.5 ms                                                                | 23.0 ms: 1.02x faster                                                |
| nbody                    | 89.4 ms                                                                | 87.7 ms: 1.02x faster                                                |
| telco                    | 7.93 ms                                                                | 7.80 ms: 1.02x faster                                                |
| spectral_norm            | 97.1 ms                                                                | 95.8 ms: 1.01x faster                                                |
| async_tree_memoization   | 319 ms                                                                 | 315 ms: 1.01x faster                                                 |
| scimark_lu               | 118 ms                                                                 | 116 ms: 1.01x faster                                                 |
| async_tree_none_tg       | 255 ms                                                                 | 253 ms: 1.01x faster                                                 |
| regex_effbot             | 3.16 ms                                                                | 3.13 ms: 1.01x faster                                                |
| thrift                   | 783 us                                                                 | 775 us: 1.01x faster                                                 |
| comprehensions           | 19.0 us                                                                | 18.8 us: 1.01x faster                                                |
| xml_etree_process        | 57.1 ms                                                                | 56.6 ms: 1.01x faster                                                |
| generators               | 29.2 ms                                                                | 29.0 ms: 1.01x faster                                                |
| sqlite_synth             | 2.72 us                                                                | 2.70 us: 1.01x faster                                                |
| django_template          | 32.0 ms                                                                | 31.8 ms: 1.01x faster                                                |
| unpickle_pure_python     | 214 us                                                                 | 212 us: 1.01x faster                                                 |
| subparsers               | 21.0 ms                                                                | 20.9 ms: 1.01x faster                                                |
| create_gc_cycles         | 2.48 ms                                                                | 2.47 ms: 1.00x faster                                                |
| python_startup_no_site   | 8.19 ms                                                                | 8.20 ms: 1.00x slower                                                |
| python_startup           | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                                |
| sympy_integrate          | 20.0 ms                                                                | 20.1 ms: 1.00x slower                                                |
| sympy_str                | 274 ms                                                                 | 276 ms: 1.00x slower                                                 |
| deltablue                | 3.06 ms                                                                | 3.07 ms: 1.00x slower                                                |
| logging_format           | 6.16 us                                                                | 6.19 us: 1.01x slower                                                |
| genshi_xml               | 49.8 ms                                                                | 50.1 ms: 1.01x slower                                                |
| regex_compile            | 128 ms                                                                 | 129 ms: 1.01x slower                                                 |
| async_tree_cpu_io_mixed  | 492 ms                                                                 | 495 ms: 1.01x slower                                                 |
| scimark_fft              | 312 ms                                                                 | 314 ms: 1.01x slower                                                 |
| connected_components     | 454 ms                                                                 | 457 ms: 1.01x slower                                                 |
| sympy_sum                | 152 ms                                                                 | 153 ms: 1.01x slower                                                 |
| shortest_path            | 494 ms                                                                 | 498 ms: 1.01x slower                                                 |
| async_generators         | 418 ms                                                                 | 421 ms: 1.01x slower                                                 |
| sqlglot_v2_transpile     | 1.61 ms                                                                | 1.62 ms: 1.01x slower                                                |
| typing_runtime_protocols | 167 us                                                                 | 169 us: 1.01x slower                                                 |
| json                     | 5.29 ms                                                                | 5.34 ms: 1.01x slower                                                |
| mako                     | 11.0 ms                                                                | 11.1 ms: 1.01x slower                                                |
| sqlglot_v2_optimize      | 54.1 ms                                                                | 54.7 ms: 1.01x slower                                                |
| nqueens                  | 84.9 ms                                                                | 85.8 ms: 1.01x slower                                                |
| sqlglot_v2_normalize     | 107 ms                                                                 | 109 ms: 1.01x slower                                                 |
| scimark_monte_carlo      | 68.6 ms                                                                | 69.5 ms: 1.01x slower                                                |
| xml_etree_iterparse      | 97.6 ms                                                                | 98.8 ms: 1.01x slower                                                |
| bpe_tokeniser            | 4.57 sec                                                               | 4.63 sec: 1.01x slower                                               |
| pprint_safe_repr         | 756 ms                                                                 | 767 ms: 1.01x slower                                                 |
| sqlalchemy_imperative    | 17.1 ms                                                                | 17.3 ms: 1.01x slower                                                |
| float                    | 64.9 ms                                                                | 65.9 ms: 1.01x slower                                                |
| sqlglot_v2_parse         | 1.29 ms                                                                | 1.31 ms: 1.02x slower                                                |
| mdp                      | 2.48 sec                                                               | 2.52 sec: 1.02x slower                                               |
| logging_silent           | 95.7 ns                                                                | 97.5 ns: 1.02x slower                                                |
| coverage                 | 85.5 ms                                                                | 87.3 ms: 1.02x slower                                                |
| go                       | 128 ms                                                                 | 132 ms: 1.03x slower                                                 |
| pprint_pformat           | 1.55 sec                                                               | 1.59 sec: 1.03x slower                                               |
| richards                 | 35.8 ms                                                                | 36.9 ms: 1.03x slower                                                |
| richards_super           | 41.1 ms                                                                | 42.5 ms: 1.03x slower                                                |
| deepcopy_reduce          | 2.66 us                                                                | 2.76 us: 1.04x slower                                                |
| deepcopy_memo            | 29.0 us                                                                | 30.1 us: 1.04x slower                                                |
| scimark_sparse_mat_mult  | 4.61 ms                                                                | 4.79 ms: 1.04x slower                                                |
| pyflate                  | 432 ms                                                                 | 459 ms: 1.06x slower                                                 |
| Geometric mean           | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (38): async_tree_io_tg, async_tree_memoization_tg, json_loads, async_tree_none, sympy_expand, bench_mp_pool, xml_etree_generate, crypto_pyaes, pylint, html5lib, raytrace, logging_simple, async_tree_cpu_io_mixed_tg, asyncio_websockets, genshi_text, coroutines, 2to3, bench_thread_pool, pickle_pure_python, deepcopy, pidigits, meteor_contest, dulwich_log, pathlib, docutils, chaos, hexiom, async_tree_io, sqlalchemy_declarative, many_optionals, scimark_sor, sphinx, tomli_loads, json_dumps, k_core, fannkuch, xml_etree_parse, pycparser

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 98.91% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x