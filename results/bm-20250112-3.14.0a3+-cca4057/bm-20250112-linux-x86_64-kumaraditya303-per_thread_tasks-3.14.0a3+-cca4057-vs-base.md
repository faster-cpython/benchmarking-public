# Results vs. base

- fork: kumaraditya303
- ref: per_thread_tasks
- machine: linux-x86_64
- commit hash: cca4057
- commit date: 2025-01-12
- overall geometric mean: 1.002x slower
- HPT reliability: 99.86%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250111-linux-x86_64-python-3a570c6d58bd5ad7d7c1-3.14.0a3+-3a570c6 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 255 ms: 1.01x slower                                                       |
| docutils       | 2.60 sec                                                               | 2.61 sec: 1.01x slower                                                     |
| html5lib       | 60.3 ms                                                                | 61.9 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250111-linux-x86_64-python-3a570c6d58bd5ad7d7c1-3.14.0a3+-3a570c6 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_generators | 420 ms                                                                 | 426 ms: 1.01x slower                                                       |
| coroutines       | 23.0 ms                                                                | 23.7 ms: 1.03x slower                                                      |
| Geometric mean   | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (9): async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_none, async_tree_none_tg, async_tree_io_tg, async_tree_io, asyncio_websockets, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250111-linux-x86_64-python-3a570c6d58bd5ad7d7c1-3.14.0a3+-3a570c6 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 96.6 ms                                                                | 96.0 ms: 1.01x faster                                                      |
| pidigits       | 186 ms                                                                 | 190 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250111-linux-x86_64-python-3a570c6d58bd5ad7d7c1-3.14.0a3+-3a570c6 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 216 ms                                                                 | 210 ms: 1.03x faster                                                       |
| regex_v8       | 25.6 ms                                                                | 25.0 ms: 1.02x faster                                                      |
| regex_effbot   | 3.39 ms                                                                | 3.34 ms: 1.02x faster                                                      |
| regex_compile  | 127 ms                                                                 | 128 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250111-linux-x86_64-python-3a570c6d58bd5ad7d7c1-3.14.0a3+-3a570c6 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 26.5 us                                                                | 26.3 us: 1.01x faster                                                      |
| xml_etree_parse      | 137 ms                                                                 | 137 ms: 1.00x slower                                                       |
| pickle_pure_python   | 320 us                                                                 | 324 us: 1.01x slower                                                       |
| xml_etree_generate   | 84.3 ms                                                                | 85.8 ms: 1.02x slower                                                      |
| xml_etree_process    | 58.5 ms                                                                | 59.6 ms: 1.02x slower                                                      |
| unpickle_pure_python | 215 us                                                                 | 220 us: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (3): json_dumps, xml_etree_iterparse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250111-linux-x86_64-python-3a570c6d58bd5ad7d7c1-3.14.0a3+-3a570c6 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.02 ms                                                                | 7.05 ms: 1.00x slower                                                      |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                      |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250111-linux-x86_64-python-3a570c6d58bd5ad7d7c1-3.14.0a3+-3a570c6 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 31.6 ms                                                                | 31.5 ms: 1.00x faster                                                      |
| mako            | 11.4 ms                                                                | 11.5 ms: 1.00x slower                                                      |
| genshi_xml      | 49.3 ms                                                                | 49.8 ms: 1.01x slower                                                      |
| genshi_text     | 22.1 ms                                                                | 22.3 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20250111-linux-x86_64-python-3a570c6d58bd5ad7d7c1-3.14.0a3+-3a570c6 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|--------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| gc_traversal             | 5.01 ms                                                                | 4.62 ms: 1.09x faster                                                      |
| scimark_sparse_mat_mult  | 4.85 ms                                                                | 4.69 ms: 1.03x faster                                                      |
| regex_dna                | 216 ms                                                                 | 210 ms: 1.03x faster                                                       |
| deepcopy_memo            | 31.3 us                                                                | 30.6 us: 1.02x faster                                                      |
| regex_v8                 | 25.6 ms                                                                | 25.0 ms: 1.02x faster                                                      |
| scimark_fft              | 351 ms                                                                 | 346 ms: 1.02x faster                                                       |
| regex_effbot             | 3.39 ms                                                                | 3.34 ms: 1.02x faster                                                      |
| logging_silent           | 109 ns                                                                 | 107 ns: 1.01x faster                                                       |
| dulwich_log              | 64.0 ms                                                                | 63.1 ms: 1.01x faster                                                      |
| logging_format           | 6.23 us                                                                | 6.15 us: 1.01x faster                                                      |
| sympy_expand             | 460 ms                                                                 | 455 ms: 1.01x faster                                                       |
| pathlib                  | 16.1 ms                                                                | 15.9 ms: 1.01x faster                                                      |
| logging_simple           | 5.65 us                                                                | 5.59 us: 1.01x faster                                                      |
| nbody                    | 96.6 ms                                                                | 96.0 ms: 1.01x faster                                                      |
| json_loads               | 26.5 us                                                                | 26.3 us: 1.01x faster                                                      |
| create_gc_cycles         | 2.46 ms                                                                | 2.45 ms: 1.01x faster                                                      |
| django_template          | 31.6 ms                                                                | 31.5 ms: 1.00x faster                                                      |
| hexiom                   | 6.24 ms                                                                | 6.22 ms: 1.00x faster                                                      |
| bpe_tokeniser            | 4.54 sec                                                               | 4.52 sec: 1.00x faster                                                     |
| mako                     | 11.4 ms                                                                | 11.5 ms: 1.00x slower                                                      |
| bench_thread_pool        | 861 us                                                                 | 863 us: 1.00x slower                                                       |
| meteor_contest           | 106 ms                                                                 | 107 ms: 1.00x slower                                                       |
| sqlalchemy_declarative   | 129 ms                                                                 | 129 ms: 1.00x slower                                                       |
| sympy_integrate          | 19.8 ms                                                                | 19.9 ms: 1.00x slower                                                      |
| generators               | 27.2 ms                                                                | 27.3 ms: 1.00x slower                                                      |
| python_startup_no_site   | 7.02 ms                                                                | 7.05 ms: 1.00x slower                                                      |
| python_startup           | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                      |
| xml_etree_parse          | 137 ms                                                                 | 137 ms: 1.00x slower                                                       |
| crypto_pyaes             | 71.6 ms                                                                | 71.9 ms: 1.00x slower                                                      |
| docutils                 | 2.60 sec                                                               | 2.61 sec: 1.01x slower                                                     |
| pprint_pformat           | 1.49 sec                                                               | 1.50 sec: 1.01x slower                                                     |
| coverage                 | 83.6 ms                                                                | 84.0 ms: 1.01x slower                                                      |
| 2to3                     | 254 ms                                                                 | 255 ms: 1.01x slower                                                       |
| scimark_monte_carlo      | 67.0 ms                                                                | 67.4 ms: 1.01x slower                                                      |
| many_optionals           | 941 us                                                                 | 947 us: 1.01x slower                                                       |
| deepcopy                 | 258 us                                                                 | 260 us: 1.01x slower                                                       |
| deepcopy_reduce          | 2.65 us                                                                | 2.67 us: 1.01x slower                                                      |
| bench_mp_pool            | 81.4 ms                                                                | 82.1 ms: 1.01x slower                                                      |
| genshi_xml               | 49.3 ms                                                                | 49.8 ms: 1.01x slower                                                      |
| subparsers               | 20.5 ms                                                                | 20.7 ms: 1.01x slower                                                      |
| regex_compile            | 127 ms                                                                 | 128 ms: 1.01x slower                                                       |
| deltablue                | 3.26 ms                                                                | 3.29 ms: 1.01x slower                                                      |
| sqlite_synth             | 2.80 us                                                                | 2.83 us: 1.01x slower                                                      |
| shortest_path            | 477 ms                                                                 | 482 ms: 1.01x slower                                                       |
| genshi_text              | 22.1 ms                                                                | 22.3 ms: 1.01x slower                                                      |
| spectral_norm            | 106 ms                                                                 | 107 ms: 1.01x slower                                                       |
| pickle_pure_python       | 320 us                                                                 | 324 us: 1.01x slower                                                       |
| chaos                    | 60.3 ms                                                                | 61.0 ms: 1.01x slower                                                      |
| async_generators         | 420 ms                                                                 | 426 ms: 1.01x slower                                                       |
| fannkuch                 | 400 ms                                                                 | 406 ms: 1.01x slower                                                       |
| pyflate                  | 453 ms                                                                 | 460 ms: 1.02x slower                                                       |
| xml_etree_generate       | 84.3 ms                                                                | 85.8 ms: 1.02x slower                                                      |
| xml_etree_process        | 58.5 ms                                                                | 59.6 ms: 1.02x slower                                                      |
| raytrace                 | 270 ms                                                                 | 275 ms: 1.02x slower                                                       |
| typing_runtime_protocols | 160 us                                                                 | 163 us: 1.02x slower                                                       |
| unpickle_pure_python     | 215 us                                                                 | 220 us: 1.02x slower                                                       |
| pidigits                 | 186 ms                                                                 | 190 ms: 1.02x slower                                                       |
| html5lib                 | 60.3 ms                                                                | 61.9 ms: 1.03x slower                                                      |
| coroutines               | 23.0 ms                                                                | 23.7 ms: 1.03x slower                                                      |
| go                       | 116 ms                                                                 | 119 ms: 1.03x slower                                                       |
| mdp                      | 2.53 sec                                                               | 2.67 sec: 1.06x slower                                                     |
| Geometric mean           | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (35): scimark_lu, k_core, json_dumps, async_tree_memoization_tg, telco, xml_etree_iterparse, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_none, async_tree_none_tg, richards, async_tree_io_tg, pycparser, sqlglot_optimize, async_tree_io, comprehensions, sympy_sum, sphinx, sympy_str, sqlglot_parse, sqlalchemy_imperative, sqlglot_normalize, richards_super, nqueens, asyncio_websockets, scimark_sor, tomli_loads, pylint, thrift, sqlglot_transpile, pprint_safe_repr, float, async_tree_cpu_io_mixed, json, connected_components

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 99.86% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x