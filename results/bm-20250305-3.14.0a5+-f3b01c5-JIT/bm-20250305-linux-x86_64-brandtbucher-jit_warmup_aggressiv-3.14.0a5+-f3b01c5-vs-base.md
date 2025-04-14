# Results vs. base

- fork: brandtbucher
- ref: jit_warmup_aggressiv
- machine: linux-x86_64
- commit hash: f3b01c5
- commit date: 2025-03-05
- overall geometric mean: 1.006x slower
- HPT reliability: 98.84%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 262 ms                                                                 | 273 ms: 1.04x slower                                                         |
| docutils       | 2.68 sec                                                               | 2.70 sec: 1.01x slower                                                       |
| html5lib       | 61.0 ms                                                                | 62.5 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 485 ms                                                                 | 475 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed    | 497 ms                                                                 | 488 ms: 1.02x faster                                                         |
| async_tree_none_tg         | 255 ms                                                                 | 252 ms: 1.01x faster                                                         |
| async_generators           | 408 ms                                                                 | 411 ms: 1.01x slower                                                         |
| coroutines                 | 24.5 ms                                                                | 24.9 ms: 1.02x slower                                                        |
| async_tree_io_tg           | 615 ms                                                                 | 628 ms: 1.02x slower                                                         |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (5): async_tree_memoization, async_tree_memoization_tg, asyncio_websockets, async_tree_io, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 71.1 ms                                                                | 69.7 ms: 1.02x faster                                                        |
| pidigits       | 186 ms                                                                 | 190 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 213 ms                                                                 | 210 ms: 1.02x faster                                                         |
| regex_effbot   | 3.37 ms                                                                | 3.34 ms: 1.01x faster                                                        |
| regex_v8       | 25.2 ms                                                                | 25.1 ms: 1.01x faster                                                        |
| regex_compile  | 128 ms                                                                 | 132 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                                 | 99.6 ms: 1.01x faster                                                        |
| xml_etree_parse      | 148 ms                                                                 | 147 ms: 1.01x faster                                                         |
| json_loads           | 30.0 us                                                                | 29.8 us: 1.01x faster                                                        |
| pickle_pure_python   | 320 us                                                                 | 322 us: 1.01x slower                                                         |
| unpickle_pure_python | 208 us                                                                 | 210 us: 1.01x slower                                                         |
| json_dumps           | 11.2 ms                                                                | 11.4 ms: 1.01x slower                                                        |
| tomli_loads          | 1.85 sec                                                               | 1.89 sec: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                                | 13.0 ms: 1.00x faster                                                        |
| python_startup_no_site | 7.16 ms                                                                | 7.15 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 31.9 ms                                                                | 32.1 ms: 1.00x slower                                                        |
| genshi_text     | 21.3 ms                                                                | 21.6 ms: 1.02x slower                                                        |
| mako            | 10.2 ms                                                                | 10.6 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal               | 4.96 ms                                                                | 4.73 ms: 1.05x faster                                                        |
| logging_silent             | 109 ns                                                                 | 107 ns: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg | 485 ms                                                                 | 475 ms: 1.02x faster                                                         |
| float                      | 71.1 ms                                                                | 69.7 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed    | 497 ms                                                                 | 488 ms: 1.02x faster                                                         |
| deepcopy_reduce            | 2.71 us                                                                | 2.66 us: 1.02x faster                                                        |
| richards                   | 45.0 ms                                                                | 44.2 ms: 1.02x faster                                                        |
| telco                      | 7.68 ms                                                                | 7.54 ms: 1.02x faster                                                        |
| regex_dna                  | 213 ms                                                                 | 210 ms: 1.02x faster                                                         |
| scimark_lu                 | 119 ms                                                                 | 117 ms: 1.02x faster                                                         |
| logging_simple             | 5.61 us                                                                | 5.52 us: 1.02x faster                                                        |
| scimark_sparse_mat_mult    | 4.54 ms                                                                | 4.48 ms: 1.01x faster                                                        |
| deltablue                  | 3.38 ms                                                                | 3.34 ms: 1.01x faster                                                        |
| richards_super             | 51.2 ms                                                                | 50.6 ms: 1.01x faster                                                        |
| deepcopy                   | 263 us                                                                 | 259 us: 1.01x faster                                                         |
| logging_format             | 6.18 us                                                                | 6.11 us: 1.01x faster                                                        |
| async_tree_none_tg         | 255 ms                                                                 | 252 ms: 1.01x faster                                                         |
| raytrace                   | 277 ms                                                                 | 274 ms: 1.01x faster                                                         |
| xml_etree_iterparse        | 101 ms                                                                 | 99.6 ms: 1.01x faster                                                        |
| chaos                      | 60.3 ms                                                                | 59.7 ms: 1.01x faster                                                        |
| xml_etree_parse            | 148 ms                                                                 | 147 ms: 1.01x faster                                                         |
| meteor_contest             | 108 ms                                                                 | 107 ms: 1.01x faster                                                         |
| regex_effbot               | 3.37 ms                                                                | 3.34 ms: 1.01x faster                                                        |
| coverage                   | 85.0 ms                                                                | 84.4 ms: 1.01x faster                                                        |
| connected_components       | 442 ms                                                                 | 439 ms: 1.01x faster                                                         |
| json_loads                 | 30.0 us                                                                | 29.8 us: 1.01x faster                                                        |
| regex_v8                   | 25.2 ms                                                                | 25.1 ms: 1.01x faster                                                        |
| deepcopy_memo              | 29.2 us                                                                | 29.0 us: 1.00x faster                                                        |
| thrift                     | 756 us                                                                 | 753 us: 1.00x faster                                                         |
| python_startup             | 13.0 ms                                                                | 13.0 ms: 1.00x faster                                                        |
| python_startup_no_site     | 7.16 ms                                                                | 7.15 ms: 1.00x faster                                                        |
| shortest_path              | 480 ms                                                                 | 481 ms: 1.00x slower                                                         |
| dulwich_log                | 67.0 ms                                                                | 67.3 ms: 1.00x slower                                                        |
| django_template            | 31.9 ms                                                                | 32.1 ms: 1.00x slower                                                        |
| bpe_tokeniser              | 4.48 sec                                                               | 4.50 sec: 1.00x slower                                                       |
| pathlib                    | 16.8 ms                                                                | 16.9 ms: 1.01x slower                                                        |
| async_generators           | 408 ms                                                                 | 411 ms: 1.01x slower                                                         |
| pickle_pure_python         | 320 us                                                                 | 322 us: 1.01x slower                                                         |
| hexiom                     | 6.39 ms                                                                | 6.43 ms: 1.01x slower                                                        |
| sympy_expand               | 471 ms                                                                 | 474 ms: 1.01x slower                                                         |
| create_gc_cycles           | 2.44 ms                                                                | 2.45 ms: 1.01x slower                                                        |
| scimark_fft                | 311 ms                                                                 | 314 ms: 1.01x slower                                                         |
| go                         | 121 ms                                                                 | 122 ms: 1.01x slower                                                         |
| docutils                   | 2.68 sec                                                               | 2.70 sec: 1.01x slower                                                       |
| unpickle_pure_python       | 208 us                                                                 | 210 us: 1.01x slower                                                         |
| json_dumps                 | 11.2 ms                                                                | 11.4 ms: 1.01x slower                                                        |
| crypto_pyaes               | 74.3 ms                                                                | 75.2 ms: 1.01x slower                                                        |
| sympy_str                  | 274 ms                                                                 | 278 ms: 1.01x slower                                                         |
| sqlglot_normalize          | 107 ms                                                                 | 109 ms: 1.02x slower                                                         |
| genshi_text                | 21.3 ms                                                                | 21.6 ms: 1.02x slower                                                        |
| coroutines                 | 24.5 ms                                                                | 24.9 ms: 1.02x slower                                                        |
| comprehensions             | 17.8 us                                                                | 18.1 us: 1.02x slower                                                        |
| bench_thread_pool          | 875 us                                                                 | 890 us: 1.02x slower                                                         |
| sqlglot_transpile          | 1.60 ms                                                                | 1.63 ms: 1.02x slower                                                        |
| pidigits                   | 186 ms                                                                 | 190 ms: 1.02x slower                                                         |
| async_tree_io_tg           | 615 ms                                                                 | 628 ms: 1.02x slower                                                         |
| tomli_loads                | 1.85 sec                                                               | 1.89 sec: 1.02x slower                                                       |
| sqlite_synth               | 2.70 us                                                                | 2.76 us: 1.02x slower                                                        |
| html5lib                   | 61.0 ms                                                                | 62.5 ms: 1.02x slower                                                        |
| sqlalchemy_imperative      | 16.8 ms                                                                | 17.3 ms: 1.03x slower                                                        |
| sqlglot_optimize           | 53.7 ms                                                                | 55.3 ms: 1.03x slower                                                        |
| nqueens                    | 80.5 ms                                                                | 82.9 ms: 1.03x slower                                                        |
| pylint                     | 281 ms                                                                 | 289 ms: 1.03x slower                                                         |
| mako                       | 10.2 ms                                                                | 10.6 ms: 1.03x slower                                                        |
| many_optionals             | 963 us                                                                 | 993 us: 1.03x slower                                                         |
| sympy_integrate            | 20.2 ms                                                                | 20.8 ms: 1.03x slower                                                        |
| generators                 | 28.0 ms                                                                | 28.9 ms: 1.03x slower                                                        |
| scimark_sor                | 120 ms                                                                 | 124 ms: 1.03x slower                                                         |
| regex_compile              | 128 ms                                                                 | 132 ms: 1.03x slower                                                         |
| typing_runtime_protocols   | 161 us                                                                 | 167 us: 1.03x slower                                                         |
| fannkuch                   | 398 ms                                                                 | 412 ms: 1.04x slower                                                         |
| pprint_pformat             | 1.50 sec                                                               | 1.56 sec: 1.04x slower                                                       |
| 2to3                       | 262 ms                                                                 | 273 ms: 1.04x slower                                                         |
| pyflate                    | 429 ms                                                                 | 447 ms: 1.04x slower                                                         |
| sympy_sum                  | 150 ms                                                                 | 158 ms: 1.06x slower                                                         |
| spectral_norm              | 96.0 ms                                                                | 102 ms: 1.06x slower                                                         |
| bench_mp_pool              | 82.1 ms                                                                | 87.3 ms: 1.06x slower                                                        |
| sqlalchemy_declarative     | 131 ms                                                                 | 140 ms: 1.07x slower                                                         |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (18): k_core, nbody, pycparser, async_tree_memoization, async_tree_memoization_tg, mdp, scimark_monte_carlo, json, subparsers, asyncio_websockets, xml_etree_generate, xml_etree_process, sqlglot_parse, async_tree_io, pprint_safe_repr, genshi_xml, sphinx, async_tree_none

- Geometric mean (including insignificant results): 1.006x slower

# HPT report

- Reliability score: 98.84% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.04x