# Results vs. base

- fork: brandtbucher
- ref: jit_warmup_1024
- machine: linux-x86_64
- commit hash: 39791ef
- commit date: 2025-03-04
- overall geometric mean: 1.001x faster
- HPT reliability: 97.45%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| html5lib       | 61.0 ms                                                                | 62.3 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (3): 2to3, docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|-------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| coroutines              | 24.5 ms                                                                | 24.0 ms: 1.02x faster                                                   |
| async_tree_none_tg      | 255 ms                                                                 | 250 ms: 1.02x faster                                                    |
| async_generators        | 408 ms                                                                 | 404 ms: 1.01x faster                                                    |
| async_tree_cpu_io_mixed | 497 ms                                                                 | 494 ms: 1.01x faster                                                    |
| Geometric mean          | (ref)                                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (7): async_tree_io, async_tree_none, async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 71.1 ms                                                                | 69.9 ms: 1.02x faster                                                   |
| pidigits       | 186 ms                                                                 | 187 ms: 1.00x slower                                                    |
| nbody          | 89.7 ms                                                                | 91.4 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                                 | 126 ms: 1.01x faster                                                    |
| regex_effbot   | 3.37 ms                                                                | 3.46 ms: 1.03x slower                                                   |
| regex_dna      | 213 ms                                                                 | 221 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 208 us                                                                 | 203 us: 1.02x faster                                                    |
| xml_etree_process    | 56.0 ms                                                                | 55.5 ms: 1.01x faster                                                   |
| xml_etree_parse      | 148 ms                                                                 | 147 ms: 1.01x faster                                                    |
| json_dumps           | 11.2 ms                                                                | 11.4 ms: 1.01x slower                                                   |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (5): xml_etree_generate, xml_etree_iterparse, pickle_pure_python, tomli_loads, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                                | 13.0 ms: 1.00x faster                                                   |
| python_startup_no_site | 7.16 ms                                                                | 7.14 ms: 1.00x faster                                                   |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 10.2 ms                                                                | 10.1 ms: 1.02x faster                                                   |
| django_template | 31.9 ms                                                                | 31.5 ms: 1.01x faster                                                   |
| genshi_xml      | 49.8 ms                                                                | 50.6 ms: 1.02x slower                                                   |
| genshi_text     | 21.3 ms                                                                | 21.7 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                            |

All benchmarks:
===============

| Benchmark                | bm-20250303-linux-x86_64-python-813bc5694bd8aa431654-3.14.0a5+-813bc56 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|--------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal             | 4.96 ms                                                                | 4.58 ms: 1.08x faster                                                   |
| logging_silent           | 109 ns                                                                 | 105 ns: 1.04x faster                                                    |
| crypto_pyaes             | 74.3 ms                                                                | 71.8 ms: 1.03x faster                                                   |
| deltablue                | 3.38 ms                                                                | 3.27 ms: 1.03x faster                                                   |
| raytrace                 | 277 ms                                                                 | 270 ms: 1.02x faster                                                    |
| unpickle_pure_python     | 208 us                                                                 | 203 us: 1.02x faster                                                    |
| hexiom                   | 6.39 ms                                                                | 6.24 ms: 1.02x faster                                                   |
| richards                 | 45.0 ms                                                                | 44.0 ms: 1.02x faster                                                   |
| coroutines               | 24.5 ms                                                                | 24.0 ms: 1.02x faster                                                   |
| mako                     | 10.2 ms                                                                | 10.1 ms: 1.02x faster                                                   |
| float                    | 71.1 ms                                                                | 69.9 ms: 1.02x faster                                                   |
| async_tree_none_tg       | 255 ms                                                                 | 250 ms: 1.02x faster                                                    |
| richards_super           | 51.2 ms                                                                | 50.4 ms: 1.02x faster                                                   |
| django_template          | 31.9 ms                                                                | 31.5 ms: 1.01x faster                                                   |
| deepcopy_memo            | 29.2 us                                                                | 28.8 us: 1.01x faster                                                   |
| chaos                    | 60.3 ms                                                                | 59.5 ms: 1.01x faster                                                   |
| regex_compile            | 128 ms                                                                 | 126 ms: 1.01x faster                                                    |
| logging_simple           | 5.61 us                                                                | 5.56 us: 1.01x faster                                                   |
| async_generators         | 408 ms                                                                 | 404 ms: 1.01x faster                                                    |
| go                       | 121 ms                                                                 | 120 ms: 1.01x faster                                                    |
| xml_etree_process        | 56.0 ms                                                                | 55.5 ms: 1.01x faster                                                   |
| xml_etree_parse          | 148 ms                                                                 | 147 ms: 1.01x faster                                                    |
| scimark_monte_carlo      | 68.9 ms                                                                | 68.4 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed  | 497 ms                                                                 | 494 ms: 1.01x faster                                                    |
| sqlglot_normalize        | 107 ms                                                                 | 107 ms: 1.01x faster                                                    |
| create_gc_cycles         | 2.44 ms                                                                | 2.42 ms: 1.01x faster                                                   |
| mdp                      | 2.51 sec                                                               | 2.49 sec: 1.01x faster                                                  |
| dulwich_log              | 67.0 ms                                                                | 66.7 ms: 1.00x faster                                                   |
| shortest_path            | 480 ms                                                                 | 478 ms: 1.00x faster                                                    |
| python_startup           | 13.0 ms                                                                | 13.0 ms: 1.00x faster                                                   |
| meteor_contest           | 108 ms                                                                 | 108 ms: 1.00x faster                                                    |
| python_startup_no_site   | 7.16 ms                                                                | 7.14 ms: 1.00x faster                                                   |
| generators               | 28.0 ms                                                                | 28.1 ms: 1.00x slower                                                   |
| pidigits                 | 186 ms                                                                 | 187 ms: 1.00x slower                                                    |
| sympy_integrate          | 20.2 ms                                                                | 20.3 ms: 1.00x slower                                                   |
| many_optionals           | 963 us                                                                 | 968 us: 1.00x slower                                                    |
| bench_thread_pool        | 875 us                                                                 | 880 us: 1.01x slower                                                    |
| sqlglot_parse            | 1.30 ms                                                                | 1.31 ms: 1.01x slower                                                   |
| sympy_str                | 274 ms                                                                 | 276 ms: 1.01x slower                                                    |
| subparsers               | 20.7 ms                                                                | 20.8 ms: 1.01x slower                                                   |
| sympy_expand             | 471 ms                                                                 | 475 ms: 1.01x slower                                                    |
| pathlib                  | 16.8 ms                                                                | 16.9 ms: 1.01x slower                                                   |
| sqlglot_transpile        | 1.60 ms                                                                | 1.62 ms: 1.01x slower                                                   |
| json_dumps               | 11.2 ms                                                                | 11.4 ms: 1.01x slower                                                   |
| thrift                   | 756 us                                                                 | 764 us: 1.01x slower                                                    |
| sympy_sum                | 150 ms                                                                 | 151 ms: 1.01x slower                                                    |
| genshi_xml               | 49.8 ms                                                                | 50.6 ms: 1.02x slower                                                   |
| sqlalchemy_declarative   | 131 ms                                                                 | 133 ms: 1.02x slower                                                    |
| sqlalchemy_imperative    | 16.8 ms                                                                | 17.1 ms: 1.02x slower                                                   |
| sqlite_synth             | 2.70 us                                                                | 2.75 us: 1.02x slower                                                   |
| nbody                    | 89.7 ms                                                                | 91.4 ms: 1.02x slower                                                   |
| scimark_sor              | 120 ms                                                                 | 123 ms: 1.02x slower                                                    |
| genshi_text              | 21.3 ms                                                                | 21.7 ms: 1.02x slower                                                   |
| html5lib                 | 61.0 ms                                                                | 62.3 ms: 1.02x slower                                                   |
| regex_effbot             | 3.37 ms                                                                | 3.46 ms: 1.03x slower                                                   |
| typing_runtime_protocols | 161 us                                                                 | 166 us: 1.03x slower                                                    |
| regex_dna                | 213 ms                                                                 | 221 ms: 1.03x slower                                                    |
| connected_components     | 442 ms                                                                 | 467 ms: 1.06x slower                                                    |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (38): async_tree_io, async_tree_none, async_tree_memoization, deepcopy_reduce, async_tree_memoization_tg, pylint, scimark_lu, xml_etree_generate, scimark_fft, xml_etree_iterparse, bench_mp_pool, pickle_pure_python, regex_v8, pprint_pformat, coverage, pycparser, k_core, async_tree_cpu_io_mixed_tg, asyncio_websockets, comprehensions, sqlglot_optimize, tomli_loads, logging_format, spectral_norm, deepcopy, 2to3, json, bpe_tokeniser, fannkuch, docutils, sphinx, json_loads, telco, nqueens, pyflate, scimark_sparse_mat_mult, pprint_safe_repr, async_tree_io_tg

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 97.45% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x