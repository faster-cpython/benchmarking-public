# Results vs. base

- fork: brandtbucher
- ref: warmup_side_16384
- machine: linux-x86_64
- commit hash: 5092a50
- commit date: 2024-11-21
- overall geometric mean: 1.002x faster
- HPT reliability: 82.85%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 262 ms                                                                 | 260 ms: 1.01x faster                                                      |
| docutils       | 2.83 sec                                                               | 2.75 sec: 1.03x faster                                                    |
| html5lib       | 66.8 ms                                                                | 65.8 ms: 1.02x faster                                                     |
| sphinx         | 1.10 sec                                                               | 1.08 sec: 1.02x faster                                                    |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| coroutines       | 23.4 ms                                                                | 22.5 ms: 1.04x faster                                                     |
| async_generators | 456 ms                                                                 | 453 ms: 1.01x faster                                                      |
| Geometric mean   | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_io, async_tree_none, async_tree_memoization, asyncio_websockets, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                                      |
| nbody          | 82.5 ms                                                                | 83.4 ms: 1.01x slower                                                     |
| float          | 77.8 ms                                                                | 78.9 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 25.5 ms                                                                | 24.9 ms: 1.02x faster                                                     |
| regex_effbot   | 3.47 ms                                                                | 3.42 ms: 1.02x faster                                                     |
| regex_compile  | 131 ms                                                                 | 130 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|--------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_generate | 83.0 ms                                                                | 78.7 ms: 1.05x faster                                                     |
| xml_etree_process  | 57.5 ms                                                                | 55.7 ms: 1.03x faster                                                     |
| tomli_loads        | 1.95 sec                                                               | 1.96 sec: 1.00x slower                                                    |
| pickle_pure_python | 319 us                                                                 | 324 us: 1.02x slower                                                      |
| Geometric mean     | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (5): xml_etree_parse, xml_etree_iterparse, json_dumps, json_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.9 ms: 1.01x slower                                                     |
| python_startup_no_site | 7.05 ms                                                                | 7.11 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 10.1 ms                                                                | 10.1 ms: 1.00x slower                                                     |
| genshi_text     | 25.0 ms                                                                | 25.1 ms: 1.01x slower                                                     |
| django_template | 33.0 ms                                                                | 33.4 ms: 1.01x slower                                                     |
| genshi_xml      | 57.1 ms                                                                | 60.5 ms: 1.06x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.02x slower                                                              |

All benchmarks:
===============

| Benchmark                | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|--------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| hexiom                   | 7.15 ms                                                                | 6.73 ms: 1.06x faster                                                     |
| pylint                   | 284 ms                                                                 | 268 ms: 1.06x faster                                                      |
| go                       | 134 ms                                                                 | 126 ms: 1.06x faster                                                      |
| xml_etree_generate       | 83.0 ms                                                                | 78.7 ms: 1.05x faster                                                     |
| coroutines               | 23.4 ms                                                                | 22.5 ms: 1.04x faster                                                     |
| sympy_sum                | 160 ms                                                                 | 153 ms: 1.04x faster                                                      |
| scimark_lu               | 115 ms                                                                 | 111 ms: 1.04x faster                                                      |
| djangocms                | 22.8 us                                                                | 22.0 us: 1.03x faster                                                     |
| nqueens                  | 90.8 ms                                                                | 87.8 ms: 1.03x faster                                                     |
| xml_etree_process        | 57.5 ms                                                                | 55.7 ms: 1.03x faster                                                     |
| sympy_str                | 287 ms                                                                 | 279 ms: 1.03x faster                                                      |
| docutils                 | 2.83 sec                                                               | 2.75 sec: 1.03x faster                                                    |
| many_optionals           | 990 us                                                                 | 964 us: 1.03x faster                                                      |
| sqlglot_parse            | 1.33 ms                                                                | 1.30 ms: 1.02x faster                                                     |
| regex_v8                 | 25.5 ms                                                                | 24.9 ms: 1.02x faster                                                     |
| sqlglot_transpile        | 1.65 ms                                                                | 1.61 ms: 1.02x faster                                                     |
| sphinx                   | 1.10 sec                                                               | 1.08 sec: 1.02x faster                                                    |
| sympy_integrate          | 21.0 ms                                                                | 20.6 ms: 1.02x faster                                                     |
| regex_effbot             | 3.47 ms                                                                | 3.42 ms: 1.02x faster                                                     |
| typing_runtime_protocols | 170 us                                                                 | 167 us: 1.02x faster                                                      |
| html5lib                 | 66.8 ms                                                                | 65.8 ms: 1.02x faster                                                     |
| telco                    | 7.58 ms                                                                | 7.49 ms: 1.01x faster                                                     |
| logging_format           | 6.17 us                                                                | 6.09 us: 1.01x faster                                                     |
| scimark_sor              | 120 ms                                                                 | 119 ms: 1.01x faster                                                      |
| logging_simple           | 5.55 us                                                                | 5.49 us: 1.01x faster                                                     |
| sympy_expand             | 482 ms                                                                 | 477 ms: 1.01x faster                                                      |
| shortest_path            | 485 ms                                                                 | 481 ms: 1.01x faster                                                      |
| sqlalchemy_declarative   | 131 ms                                                                 | 130 ms: 1.01x faster                                                      |
| scimark_sparse_mat_mult  | 4.67 ms                                                                | 4.64 ms: 1.01x faster                                                     |
| dulwich_log              | 68.0 ms                                                                | 67.5 ms: 1.01x faster                                                     |
| fannkuch                 | 389 ms                                                                 | 386 ms: 1.01x faster                                                      |
| deltablue                | 3.19 ms                                                                | 3.16 ms: 1.01x faster                                                     |
| 2to3                     | 262 ms                                                                 | 260 ms: 1.01x faster                                                      |
| async_generators         | 456 ms                                                                 | 453 ms: 1.01x faster                                                      |
| regex_compile            | 131 ms                                                                 | 130 ms: 1.01x faster                                                      |
| logging_silent           | 99.4 ns                                                                | 98.9 ns: 1.01x faster                                                     |
| connected_components     | 440 ms                                                                 | 438 ms: 1.00x faster                                                      |
| sqlglot_optimize         | 55.5 ms                                                                | 55.3 ms: 1.00x faster                                                     |
| pidigits                 | 186 ms                                                                 | 186 ms: 1.00x slower                                                      |
| mako                     | 10.1 ms                                                                | 10.1 ms: 1.00x slower                                                     |
| tomli_loads              | 1.95 sec                                                               | 1.96 sec: 1.00x slower                                                    |
| thrift                   | 776 us                                                                 | 781 us: 1.01x slower                                                      |
| python_startup           | 12.8 ms                                                                | 12.9 ms: 1.01x slower                                                     |
| genshi_text              | 25.0 ms                                                                | 25.1 ms: 1.01x slower                                                     |
| subparsers               | 21.0 ms                                                                | 21.1 ms: 1.01x slower                                                     |
| python_startup_no_site   | 7.05 ms                                                                | 7.11 ms: 1.01x slower                                                     |
| raytrace                 | 280 ms                                                                 | 283 ms: 1.01x slower                                                      |
| meteor_contest           | 108 ms                                                                 | 109 ms: 1.01x slower                                                      |
| scimark_fft              | 317 ms                                                                 | 320 ms: 1.01x slower                                                      |
| create_gc_cycles         | 2.64 ms                                                                | 2.67 ms: 1.01x slower                                                     |
| nbody                    | 82.5 ms                                                                | 83.4 ms: 1.01x slower                                                     |
| crypto_pyaes             | 67.6 ms                                                                | 68.4 ms: 1.01x slower                                                     |
| django_template          | 33.0 ms                                                                | 33.4 ms: 1.01x slower                                                     |
| chaos                    | 58.9 ms                                                                | 59.7 ms: 1.01x slower                                                     |
| float                    | 77.8 ms                                                                | 78.9 ms: 1.02x slower                                                     |
| pickle_pure_python       | 319 us                                                                 | 324 us: 1.02x slower                                                      |
| pprint_pformat           | 1.46 sec                                                               | 1.50 sec: 1.03x slower                                                    |
| deepcopy_reduce          | 2.69 us                                                                | 2.78 us: 1.03x slower                                                     |
| comprehensions           | 17.6 us                                                                | 18.2 us: 1.03x slower                                                     |
| pycparser                | 1.13 sec                                                               | 1.18 sec: 1.04x slower                                                    |
| spectral_norm            | 112 ms                                                                 | 119 ms: 1.05x slower                                                      |
| genshi_xml               | 57.1 ms                                                                | 60.5 ms: 1.06x slower                                                     |
| mdp                      | 2.59 sec                                                               | 2.75 sec: 1.06x slower                                                    |
| gc_traversal             | 4.35 ms                                                                | 4.68 ms: 1.08x slower                                                     |
| richards_super           | 42.5 ms                                                                | 46.2 ms: 1.09x slower                                                     |
| richards                 | 36.9 ms                                                                | 40.2 ms: 1.09x slower                                                     |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (31): async_tree_cpu_io_mixed_tg, scimark_monte_carlo, json, sqlalchemy_imperative, async_tree_io_tg, async_tree_cpu_io_mixed, xml_etree_parse, sqlglot_normalize, async_tree_none_tg, async_tree_io, regex_dna, deepcopy_memo, bench_thread_pool, generators, async_tree_none, xml_etree_iterparse, async_tree_memoization, json_dumps, json_loads, k_core, asyncio_websockets, pyflate, async_tree_memoization_tg, bpe_tokeniser, sqlite_synth, pathlib, bench_mp_pool, deepcopy, coverage, unpickle_pure_python, pprint_safe_repr

- Geometric mean (including insignificant results): 1.002x faster
# HPT report

- Reliability score: 82.85% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x