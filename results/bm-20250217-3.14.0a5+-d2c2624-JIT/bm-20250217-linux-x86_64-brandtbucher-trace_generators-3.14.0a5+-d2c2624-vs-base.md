# Results vs. base

- fork: brandtbucher
- ref: trace_generators
- machine: linux-x86_64
- commit hash: d2c2624
- commit date: 2025-02-17
- overall geometric mean: 1.013x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d2c2624 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 258 ms                                                                 | 265 ms: 1.03x slower                                                     |
| docutils       | 2.65 sec                                                               | 2.67 sec: 1.01x slower                                                   |
| html5lib       | 60.6 ms                                                                | 62.5 ms: 1.03x slower                                                    |
| sphinx         | 1.00 sec                                                               | 1.02 sec: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d2c2624 |
|-------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 489 ms                                                                 | 493 ms: 1.01x slower                                                     |
| async_tree_memoization  | 323 ms                                                                 | 326 ms: 1.01x slower                                                     |
| coroutines              | 23.4 ms                                                                | 23.7 ms: 1.01x slower                                                    |
| async_generators        | 403 ms                                                                 | 411 ms: 1.02x slower                                                     |
| Geometric mean          | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (7): async_tree_io_tg, async_tree_none_tg, asyncio_websockets, async_tree_memoization_tg, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d2c2624 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 188 ms                                                                 | 186 ms: 1.01x faster                                                     |
| nbody          | 90.0 ms                                                                | 99.2 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                             |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d2c2624 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 126 ms                                                                 | 125 ms: 1.01x faster                                                     |
| regex_v8       | 24.0 ms                                                                | 23.9 ms: 1.00x faster                                                    |
| regex_dna      | 202 ms                                                                 | 207 ms: 1.02x slower                                                     |
| regex_effbot   | 3.01 ms                                                                | 3.09 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d2c2624 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 11.8 ms                                                                | 11.7 ms: 1.01x faster                                                    |
| tomli_loads          | 1.84 sec                                                               | 1.85 sec: 1.01x slower                                                   |
| json_loads           | 28.5 us                                                                | 28.7 us: 1.01x slower                                                    |
| xml_etree_iterparse  | 96.2 ms                                                                | 97.0 ms: 1.01x slower                                                    |
| xml_etree_generate   | 78.2 ms                                                                | 79.1 ms: 1.01x slower                                                    |
| unpickle_pure_python | 205 us                                                                 | 211 us: 1.03x slower                                                     |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d2c2624 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 7.08 ms                                                                | 7.05 ms: 1.00x faster                                                    |
| python_startup         | 12.9 ms                                                                | 12.8 ms: 1.00x faster                                                    |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d2c2624 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 31.6 ms                                                                | 31.8 ms: 1.01x slower                                                    |
| mako            | 9.92 ms                                                                | 10.3 ms: 1.04x slower                                                    |
| genshi_xml      | 48.8 ms                                                                | 52.2 ms: 1.07x slower                                                    |
| genshi_text     | 21.3 ms                                                                | 23.7 ms: 1.11x slower                                                    |
| Geometric mean  | (ref)                                                                  | 1.06x slower                                                             |

All benchmarks:
===============

| Benchmark                | bm-20250213-linux-x86_64-python-05e89c34bd8389f87bd6-3.14.0a5+-05e89c3 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d2c2624 |
|--------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nqueens                  | 83.3 ms                                                                | 81.3 ms: 1.02x faster                                                    |
| deepcopy                 | 261 us                                                                 | 257 us: 1.01x faster                                                     |
| pyflate                  | 467 ms                                                                 | 462 ms: 1.01x faster                                                     |
| logging_format           | 6.15 us                                                                | 6.09 us: 1.01x faster                                                    |
| pidigits                 | 188 ms                                                                 | 186 ms: 1.01x faster                                                     |
| gc_traversal             | 4.80 ms                                                                | 4.77 ms: 1.01x faster                                                    |
| bpe_tokeniser            | 4.41 sec                                                               | 4.39 sec: 1.01x faster                                                   |
| regex_compile            | 126 ms                                                                 | 125 ms: 1.01x faster                                                     |
| meteor_contest           | 108 ms                                                                 | 107 ms: 1.01x faster                                                     |
| json_dumps               | 11.8 ms                                                                | 11.7 ms: 1.01x faster                                                    |
| regex_v8                 | 24.0 ms                                                                | 23.9 ms: 1.00x faster                                                    |
| create_gc_cycles         | 2.48 ms                                                                | 2.47 ms: 1.00x faster                                                    |
| many_optionals           | 954 us                                                                 | 950 us: 1.00x faster                                                     |
| sympy_str                | 273 ms                                                                 | 272 ms: 1.00x faster                                                     |
| python_startup_no_site   | 7.08 ms                                                                | 7.05 ms: 1.00x faster                                                    |
| python_startup           | 12.9 ms                                                                | 12.8 ms: 1.00x faster                                                    |
| chaos                    | 58.7 ms                                                                | 58.9 ms: 1.00x slower                                                    |
| sympy_expand             | 466 ms                                                                 | 468 ms: 1.00x slower                                                     |
| connected_components     | 440 ms                                                                 | 441 ms: 1.00x slower                                                     |
| mdp                      | 2.48 sec                                                               | 2.49 sec: 1.00x slower                                                   |
| crypto_pyaes             | 71.4 ms                                                                | 71.7 ms: 1.00x slower                                                    |
| hexiom                   | 6.67 ms                                                                | 6.71 ms: 1.01x slower                                                    |
| sqlalchemy_declarative   | 130 ms                                                                 | 131 ms: 1.01x slower                                                     |
| tomli_loads              | 1.84 sec                                                               | 1.85 sec: 1.01x slower                                                   |
| sqlglot_parse            | 1.29 ms                                                                | 1.30 ms: 1.01x slower                                                    |
| coverage                 | 88.6 ms                                                                | 89.2 ms: 1.01x slower                                                    |
| sqlglot_optimize         | 53.2 ms                                                                | 53.5 ms: 1.01x slower                                                    |
| go                       | 125 ms                                                                 | 125 ms: 1.01x slower                                                     |
| json_loads               | 28.5 us                                                                | 28.7 us: 1.01x slower                                                    |
| shortest_path            | 480 ms                                                                 | 483 ms: 1.01x slower                                                     |
| django_template          | 31.6 ms                                                                | 31.8 ms: 1.01x slower                                                    |
| async_tree_cpu_io_mixed  | 489 ms                                                                 | 493 ms: 1.01x slower                                                     |
| async_tree_memoization   | 323 ms                                                                 | 326 ms: 1.01x slower                                                     |
| xml_etree_iterparse      | 96.2 ms                                                                | 97.0 ms: 1.01x slower                                                    |
| docutils                 | 2.65 sec                                                               | 2.67 sec: 1.01x slower                                                   |
| sqlite_synth             | 2.72 us                                                                | 2.74 us: 1.01x slower                                                    |
| thrift                   | 751 us                                                                 | 759 us: 1.01x slower                                                     |
| richards                 | 43.6 ms                                                                | 44.1 ms: 1.01x slower                                                    |
| xml_etree_generate       | 78.2 ms                                                                | 79.1 ms: 1.01x slower                                                    |
| coroutines               | 23.4 ms                                                                | 23.7 ms: 1.01x slower                                                    |
| pprint_safe_repr         | 727 ms                                                                 | 737 ms: 1.01x slower                                                     |
| typing_runtime_protocols | 162 us                                                                 | 164 us: 1.01x slower                                                     |
| sphinx                   | 1.00 sec                                                               | 1.02 sec: 1.02x slower                                                   |
| bench_thread_pool        | 872 us                                                                 | 888 us: 1.02x slower                                                     |
| pathlib                  | 16.1 ms                                                                | 16.4 ms: 1.02x slower                                                    |
| scimark_fft              | 313 ms                                                                 | 319 ms: 1.02x slower                                                     |
| scimark_lu               | 116 ms                                                                 | 118 ms: 1.02x slower                                                     |
| async_generators         | 403 ms                                                                 | 411 ms: 1.02x slower                                                     |
| regex_dna                | 202 ms                                                                 | 207 ms: 1.02x slower                                                     |
| sqlglot_normalize        | 105 ms                                                                 | 107 ms: 1.02x slower                                                     |
| dulwich_log              | 66.5 ms                                                                | 68.0 ms: 1.02x slower                                                    |
| logging_silent           | 102 ns                                                                 | 104 ns: 1.02x slower                                                     |
| raytrace                 | 272 ms                                                                 | 279 ms: 1.02x slower                                                     |
| regex_effbot             | 3.01 ms                                                                | 3.09 ms: 1.03x slower                                                    |
| scimark_sparse_mat_mult  | 4.49 ms                                                                | 4.60 ms: 1.03x slower                                                    |
| unpickle_pure_python     | 205 us                                                                 | 211 us: 1.03x slower                                                     |
| 2to3                     | 258 ms                                                                 | 265 ms: 1.03x slower                                                     |
| html5lib                 | 60.6 ms                                                                | 62.5 ms: 1.03x slower                                                    |
| deltablue                | 3.28 ms                                                                | 3.39 ms: 1.03x slower                                                    |
| spectral_norm            | 94.6 ms                                                                | 98.0 ms: 1.04x slower                                                    |
| mako                     | 9.92 ms                                                                | 10.3 ms: 1.04x slower                                                    |
| pprint_pformat           | 1.49 sec                                                               | 1.56 sec: 1.04x slower                                                   |
| genshi_xml               | 48.8 ms                                                                | 52.2 ms: 1.07x slower                                                    |
| nbody                    | 90.0 ms                                                                | 99.2 ms: 1.10x slower                                                    |
| genshi_text              | 21.3 ms                                                                | 23.7 ms: 1.11x slower                                                    |
| generators               | 27.7 ms                                                                | 40.7 ms: 1.47x slower                                                    |
| Geometric mean           | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (30): pycparser, async_tree_io_tg, scimark_sor, deepcopy_memo, sqlglot_transpile, subparsers, logging_simple, deepcopy_reduce, fannkuch, sqlalchemy_imperative, async_tree_none_tg, sympy_integrate, json, asyncio_websockets, async_tree_memoization_tg, bench_mp_pool, xml_etree_process, comprehensions, k_core, telco, sympy_sum, richards_super, async_tree_none, scimark_monte_carlo, xml_etree_parse, float, async_tree_cpu_io_mixed_tg, async_tree_io, pickle_pure_python, pylint

- Geometric mean (including insignificant results): 1.013x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x