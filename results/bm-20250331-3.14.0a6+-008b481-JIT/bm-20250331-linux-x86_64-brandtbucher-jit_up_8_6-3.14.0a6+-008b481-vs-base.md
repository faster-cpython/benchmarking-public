# Results vs. base

- fork: brandtbucher
- ref: jit_up_8_6
- machine: linux-x86_64
- commit hash: 008b481
- commit date: 2025-03-31
- overall geometric mean: 1.007x slower
- HPT reliability: 99.76%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                 | 270 ms: 1.03x slower                                               |
| docutils       | 2.69 sec                                                               | 2.72 sec: 1.01x slower                                             |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|-------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none         | 266 ms                                                                 | 259 ms: 1.02x faster                                               |
| coroutines              | 24.1 ms                                                                | 23.8 ms: 1.01x faster                                              |
| async_tree_none_tg      | 255 ms                                                                 | 253 ms: 1.01x faster                                               |
| async_tree_memoization  | 319 ms                                                                 | 316 ms: 1.01x faster                                               |
| async_generators        | 418 ms                                                                 | 420 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed | 492 ms                                                                 | 495 ms: 1.01x slower                                               |
| Geometric mean          | (ref)                                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_tree_io, async_tree_io_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 89.4 ms                                                                | 88.6 ms: 1.01x faster                                              |
| float          | 64.9 ms                                                                | 66.3 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 23.5 ms                                                                | 22.8 ms: 1.03x faster                                              |
| regex_dna      | 217 ms                                                                 | 213 ms: 1.02x faster                                               |
| regex_compile  | 128 ms                                                                 | 130 ms: 1.02x slower                                               |
| regex_effbot   | 3.16 ms                                                                | 3.23 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|---------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| json_loads          | 30.1 us                                                                | 29.7 us: 1.02x faster                                              |
| xml_etree_iterparse | 97.6 ms                                                                | 98.4 ms: 1.01x slower                                              |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (7): xml_etree_process, xml_etree_parse, json_dumps, pickle_pure_python, xml_etree_generate, tomli_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                              |
| python_startup_no_site | 8.19 ms                                                                | 8.18 ms: 1.00x faster                                              |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 21.4 ms                                                                | 21.3 ms: 1.01x faster                                              |
| mako            | 11.0 ms                                                                | 11.1 ms: 1.00x slower                                              |
| django_template | 32.0 ms                                                                | 32.3 ms: 1.01x slower                                              |
| genshi_xml      | 49.8 ms                                                                | 50.6 ms: 1.02x slower                                              |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                       |

All benchmarks:
===============

| Benchmark                | bm-20250324-linux-x86_64-python-a1232459860235f4fb78-3.14.0a6+-a123245 | bm-20250331-linux-x86_64-brandtbucher-jit_up_8_6-3.14.0a6+-008b481 |
|--------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8                 | 23.5 ms                                                                | 22.8 ms: 1.03x faster                                              |
| crypto_pyaes             | 78.3 ms                                                                | 76.2 ms: 1.03x faster                                              |
| async_tree_none          | 266 ms                                                                 | 259 ms: 1.02x faster                                               |
| comprehensions           | 19.0 us                                                                | 18.6 us: 1.02x faster                                              |
| thrift                   | 783 us                                                                 | 769 us: 1.02x faster                                               |
| regex_dna                | 217 ms                                                                 | 213 ms: 1.02x faster                                               |
| json_loads               | 30.1 us                                                                | 29.7 us: 1.02x faster                                              |
| spectral_norm            | 97.1 ms                                                                | 95.5 ms: 1.02x faster                                              |
| logging_simple           | 5.59 us                                                                | 5.51 us: 1.01x faster                                              |
| chaos                    | 60.3 ms                                                                | 59.7 ms: 1.01x faster                                              |
| gc_traversal             | 5.05 ms                                                                | 5.00 ms: 1.01x faster                                              |
| coroutines               | 24.1 ms                                                                | 23.8 ms: 1.01x faster                                              |
| nbody                    | 89.4 ms                                                                | 88.6 ms: 1.01x faster                                              |
| async_tree_none_tg       | 255 ms                                                                 | 253 ms: 1.01x faster                                               |
| async_tree_memoization   | 319 ms                                                                 | 316 ms: 1.01x faster                                               |
| genshi_text              | 21.4 ms                                                                | 21.3 ms: 1.01x faster                                              |
| dulwich_log              | 60.6 ms                                                                | 60.4 ms: 1.00x faster                                              |
| python_startup           | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                              |
| python_startup_no_site   | 8.19 ms                                                                | 8.18 ms: 1.00x faster                                              |
| meteor_contest           | 108 ms                                                                 | 109 ms: 1.00x slower                                               |
| mako                     | 11.0 ms                                                                | 11.1 ms: 1.00x slower                                              |
| subparsers               | 21.0 ms                                                                | 21.1 ms: 1.00x slower                                              |
| generators               | 29.2 ms                                                                | 29.4 ms: 1.00x slower                                              |
| async_generators         | 418 ms                                                                 | 420 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed  | 492 ms                                                                 | 495 ms: 1.01x slower                                               |
| bench_mp_pool            | 83.3 ms                                                                | 83.8 ms: 1.01x slower                                              |
| deepcopy_memo            | 29.0 us                                                                | 29.2 us: 1.01x slower                                              |
| create_gc_cycles         | 2.48 ms                                                                | 2.50 ms: 1.01x slower                                              |
| coverage                 | 85.5 ms                                                                | 86.1 ms: 1.01x slower                                              |
| go                       | 128 ms                                                                 | 129 ms: 1.01x slower                                               |
| django_template          | 32.0 ms                                                                | 32.3 ms: 1.01x slower                                              |
| xml_etree_iterparse      | 97.6 ms                                                                | 98.4 ms: 1.01x slower                                              |
| typing_runtime_protocols | 167 us                                                                 | 169 us: 1.01x slower                                               |
| fannkuch                 | 423 ms                                                                 | 428 ms: 1.01x slower                                               |
| shortest_path            | 494 ms                                                                 | 499 ms: 1.01x slower                                               |
| scimark_fft              | 312 ms                                                                 | 315 ms: 1.01x slower                                               |
| docutils                 | 2.69 sec                                                               | 2.72 sec: 1.01x slower                                             |
| sympy_expand             | 475 ms                                                                 | 480 ms: 1.01x slower                                               |
| logging_silent           | 95.7 ns                                                                | 96.8 ns: 1.01x slower                                              |
| hexiom                   | 6.86 ms                                                                | 6.94 ms: 1.01x slower                                              |
| scimark_sparse_mat_mult  | 4.61 ms                                                                | 4.66 ms: 1.01x slower                                              |
| pprint_safe_repr         | 756 ms                                                                 | 766 ms: 1.01x slower                                               |
| mdp                      | 2.48 sec                                                               | 2.52 sec: 1.02x slower                                             |
| genshi_xml               | 49.8 ms                                                                | 50.6 ms: 1.02x slower                                              |
| bench_thread_pool        | 882 us                                                                 | 897 us: 1.02x slower                                               |
| scimark_lu               | 118 ms                                                                 | 120 ms: 1.02x slower                                               |
| scimark_sor              | 119 ms                                                                 | 121 ms: 1.02x slower                                               |
| sympy_str                | 274 ms                                                                 | 280 ms: 1.02x slower                                               |
| deepcopy                 | 260 us                                                                 | 265 us: 1.02x slower                                               |
| sqlglot_v2_normalize     | 107 ms                                                                 | 110 ms: 1.02x slower                                               |
| regex_compile            | 128 ms                                                                 | 130 ms: 1.02x slower                                               |
| sqlalchemy_imperative    | 17.1 ms                                                                | 17.4 ms: 1.02x slower                                              |
| float                    | 64.9 ms                                                                | 66.3 ms: 1.02x slower                                              |
| bpe_tokeniser            | 4.57 sec                                                               | 4.67 sec: 1.02x slower                                             |
| sqlglot_v2_parse         | 1.29 ms                                                                | 1.32 ms: 1.02x slower                                              |
| regex_effbot             | 3.16 ms                                                                | 3.23 ms: 1.02x slower                                              |
| sympy_integrate          | 20.0 ms                                                                | 20.5 ms: 1.03x slower                                              |
| sqlglot_v2_optimize      | 54.1 ms                                                                | 55.6 ms: 1.03x slower                                              |
| 2to3                     | 263 ms                                                                 | 270 ms: 1.03x slower                                               |
| sqlglot_v2_transpile     | 1.61 ms                                                                | 1.65 ms: 1.03x slower                                              |
| sympy_sum                | 152 ms                                                                 | 156 ms: 1.03x slower                                               |
| many_optionals           | 970 us                                                                 | 1.00 ms: 1.03x slower                                              |
| pprint_pformat           | 1.55 sec                                                               | 1.61 sec: 1.04x slower                                             |
| pycparser                | 1.13 sec                                                               | 1.18 sec: 1.04x slower                                             |
| richards                 | 35.8 ms                                                                | 37.4 ms: 1.05x slower                                              |
| richards_super           | 41.1 ms                                                                | 43.0 ms: 1.05x slower                                              |
| deepcopy_reduce          | 2.66 us                                                                | 2.79 us: 1.05x slower                                              |
| sqlalchemy_declarative   | 133 ms                                                                 | 141 ms: 1.06x slower                                               |
| pyflate                  | 432 ms                                                                 | 460 ms: 1.07x slower                                               |
| connected_components     | 454 ms                                                                 | 492 ms: 1.08x slower                                               |
| Geometric mean           | (ref)                                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (26): async_tree_memoization_tg, async_tree_io, telco, html5lib, xml_etree_process, async_tree_io_tg, logging_format, raytrace, async_tree_cpu_io_mixed_tg, deltablue, scimark_monte_carlo, json, sqlite_synth, pidigits, xml_etree_parse, nqueens, asyncio_websockets, json_dumps, pickle_pure_python, xml_etree_generate, tomli_loads, pathlib, k_core, sphinx, unpickle_pure_python, pylint

- Geometric mean (including insignificant results): 1.007x slower

# HPT report

- Reliability score: 99.76% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x