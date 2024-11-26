# Results vs. base

- fork: brandtbucher
- ref: warmup_side_65536
- machine: linux-x86_64
- commit hash: 41565b0
- commit date: 2024-11-21
- overall geometric mean: 1.000x faster
- HPT reliability: 83.05%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_65536-3.14.0a2+-41565b0 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 262 ms                                                                 | 260 ms: 1.01x faster                                                      |
| docutils       | 2.83 sec                                                               | 2.71 sec: 1.04x faster                                                    |
| html5lib       | 66.8 ms                                                                | 67.4 ms: 1.01x slower                                                     |
| sphinx         | 1.10 sec                                                               | 1.08 sec: 1.02x faster                                                    |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_65536-3.14.0a2+-41565b0 |
|------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_generators | 456 ms                                                                 | 457 ms: 1.00x slower                                                      |
| Geometric mean   | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (10): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_memoization, async_tree_none, coroutines, async_tree_io_tg, asyncio_websockets, async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_65536-3.14.0a2+-41565b0 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 187 ms: 1.01x slower                                                      |
| nbody          | 82.5 ms                                                                | 84.8 ms: 1.03x slower                                                     |
| float          | 77.8 ms                                                                | 82.3 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_65536-3.14.0a2+-41565b0 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.47 ms                                                                | 3.40 ms: 1.02x faster                                                     |
| regex_dna      | 223 ms                                                                 | 219 ms: 1.02x faster                                                      |
| regex_v8       | 25.5 ms                                                                | 25.0 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_65536-3.14.0a2+-41565b0 |
|--------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_generate | 83.0 ms                                                                | 78.8 ms: 1.05x faster                                                     |
| json_dumps         | 11.2 ms                                                                | 11.1 ms: 1.01x faster                                                     |
| xml_etree_parse    | 148 ms                                                                 | 149 ms: 1.01x slower                                                      |
| pickle_pure_python | 319 us                                                                 | 323 us: 1.01x slower                                                      |
| tomli_loads        | 1.95 sec                                                               | 1.99 sec: 1.02x slower                                                    |
| Geometric mean     | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (4): xml_etree_process, json_loads, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_65536-3.14.0a2+-41565b0 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                                     |
| python_startup_no_site | 7.05 ms                                                                | 7.07 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_65536-3.14.0a2+-41565b0 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml     | 57.1 ms                                                                | 56.2 ms: 1.02x faster                                                     |
| mako           | 10.1 ms                                                                | 10.2 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_65536-3.14.0a2+-41565b0 |
|--------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| go                       | 134 ms                                                                 | 126 ms: 1.06x faster                                                      |
| pylint                   | 284 ms                                                                 | 269 ms: 1.06x faster                                                      |
| xml_etree_generate       | 83.0 ms                                                                | 78.8 ms: 1.05x faster                                                     |
| hexiom                   | 7.15 ms                                                                | 6.83 ms: 1.05x faster                                                     |
| docutils                 | 2.83 sec                                                               | 2.71 sec: 1.04x faster                                                    |
| sympy_sum                | 160 ms                                                                 | 153 ms: 1.04x faster                                                      |
| many_optionals           | 990 us                                                                 | 965 us: 1.03x faster                                                      |
| sympy_str                | 287 ms                                                                 | 280 ms: 1.03x faster                                                      |
| typing_runtime_protocols | 170 us                                                                 | 165 us: 1.03x faster                                                      |
| scimark_lu               | 115 ms                                                                 | 112 ms: 1.02x faster                                                      |
| regex_effbot             | 3.47 ms                                                                | 3.40 ms: 1.02x faster                                                     |
| regex_dna                | 223 ms                                                                 | 219 ms: 1.02x faster                                                      |
| sphinx                   | 1.10 sec                                                               | 1.08 sec: 1.02x faster                                                    |
| regex_v8                 | 25.5 ms                                                                | 25.0 ms: 1.02x faster                                                     |
| sqlglot_parse            | 1.33 ms                                                                | 1.31 ms: 1.02x faster                                                     |
| dulwich_log              | 68.0 ms                                                                | 66.8 ms: 1.02x faster                                                     |
| nqueens                  | 90.8 ms                                                                | 89.2 ms: 1.02x faster                                                     |
| sympy_integrate          | 21.0 ms                                                                | 20.7 ms: 1.02x faster                                                     |
| genshi_xml               | 57.1 ms                                                                | 56.2 ms: 1.02x faster                                                     |
| deltablue                | 3.19 ms                                                                | 3.14 ms: 1.02x faster                                                     |
| sqlglot_transpile        | 1.65 ms                                                                | 1.62 ms: 1.01x faster                                                     |
| pathlib                  | 16.4 ms                                                                | 16.2 ms: 1.01x faster                                                     |
| sqlite_synth             | 2.79 us                                                                | 2.76 us: 1.01x faster                                                     |
| sqlalchemy_declarative   | 131 ms                                                                 | 129 ms: 1.01x faster                                                      |
| scimark_sparse_mat_mult  | 4.67 ms                                                                | 4.62 ms: 1.01x faster                                                     |
| sympy_expand             | 482 ms                                                                 | 477 ms: 1.01x faster                                                      |
| json_dumps               | 11.2 ms                                                                | 11.1 ms: 1.01x faster                                                     |
| sqlglot_optimize         | 55.5 ms                                                                | 55.1 ms: 1.01x faster                                                     |
| 2to3                     | 262 ms                                                                 | 260 ms: 1.01x faster                                                      |
| shortest_path            | 485 ms                                                                 | 482 ms: 1.01x faster                                                      |
| scimark_fft              | 317 ms                                                                 | 315 ms: 1.01x faster                                                      |
| bpe_tokeniser            | 4.50 sec                                                               | 4.47 sec: 1.01x faster                                                    |
| bench_thread_pool        | 876 us                                                                 | 872 us: 1.00x faster                                                      |
| mdp                      | 2.59 sec                                                               | 2.58 sec: 1.00x faster                                                    |
| async_generators         | 456 ms                                                                 | 457 ms: 1.00x slower                                                      |
| python_startup           | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                                     |
| python_startup_no_site   | 7.05 ms                                                                | 7.07 ms: 1.00x slower                                                     |
| pidigits                 | 186 ms                                                                 | 187 ms: 1.01x slower                                                      |
| pyflate                  | 452 ms                                                                 | 455 ms: 1.01x slower                                                      |
| html5lib                 | 66.8 ms                                                                | 67.4 ms: 1.01x slower                                                     |
| create_gc_cycles         | 2.64 ms                                                                | 2.67 ms: 1.01x slower                                                     |
| mako                     | 10.1 ms                                                                | 10.2 ms: 1.01x slower                                                     |
| generators               | 35.2 ms                                                                | 35.6 ms: 1.01x slower                                                     |
| logging_silent           | 99.4 ns                                                                | 100 ns: 1.01x slower                                                      |
| logging_simple           | 5.55 us                                                                | 5.61 us: 1.01x slower                                                     |
| xml_etree_parse          | 148 ms                                                                 | 149 ms: 1.01x slower                                                      |
| meteor_contest           | 108 ms                                                                 | 109 ms: 1.01x slower                                                      |
| pickle_pure_python       | 319 us                                                                 | 323 us: 1.01x slower                                                      |
| logging_format           | 6.17 us                                                                | 6.25 us: 1.01x slower                                                     |
| crypto_pyaes             | 67.6 ms                                                                | 68.6 ms: 1.01x slower                                                     |
| subparsers               | 21.0 ms                                                                | 21.3 ms: 1.02x slower                                                     |
| tomli_loads              | 1.95 sec                                                               | 1.99 sec: 1.02x slower                                                    |
| coverage                 | 83.8 ms                                                                | 85.4 ms: 1.02x slower                                                     |
| thrift                   | 776 us                                                                 | 791 us: 1.02x slower                                                      |
| spectral_norm            | 112 ms                                                                 | 115 ms: 1.02x slower                                                      |
| pprint_safe_repr         | 720 ms                                                                 | 736 ms: 1.02x slower                                                      |
| json                     | 4.85 ms                                                                | 4.97 ms: 1.03x slower                                                     |
| chaos                    | 58.9 ms                                                                | 60.4 ms: 1.03x slower                                                     |
| nbody                    | 82.5 ms                                                                | 84.8 ms: 1.03x slower                                                     |
| pycparser                | 1.13 sec                                                               | 1.17 sec: 1.04x slower                                                    |
| pprint_pformat           | 1.46 sec                                                               | 1.52 sec: 1.05x slower                                                    |
| float                    | 77.8 ms                                                                | 82.3 ms: 1.06x slower                                                     |
| richards                 | 36.9 ms                                                                | 39.3 ms: 1.06x slower                                                     |
| richards_super           | 42.5 ms                                                                | 45.6 ms: 1.07x slower                                                     |
| gc_traversal             | 4.35 ms                                                                | 4.73 ms: 1.09x slower                                                     |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (32): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, xml_etree_process, djangocms, deepcopy_memo, async_tree_io, async_tree_memoization, deepcopy, sqlglot_normalize, fannkuch, scimark_sor, genshi_text, async_tree_none, coroutines, async_tree_io_tg, deepcopy_reduce, sqlalchemy_imperative, k_core, comprehensions, json_loads, raytrace, regex_compile, connected_components, scimark_monte_carlo, unpickle_pure_python, asyncio_websockets, bench_mp_pool, xml_etree_iterparse, django_template, async_tree_memoization_tg, telco, async_tree_none_tg

- Geometric mean (including insignificant results): 1.000x faster
# HPT report

- Reliability score: 83.05% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x