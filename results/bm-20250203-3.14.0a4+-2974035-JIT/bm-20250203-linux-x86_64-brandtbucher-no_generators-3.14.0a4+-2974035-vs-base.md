# Results vs. base

- fork: brandtbucher
- ref: no_generators
- machine: linux-x86_64
- commit hash: 2974035
- commit date: 2025-02-03
- overall geometric mean: 1.006x faster
- HPT reliability: 83.58%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250203-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-2974035 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 261 ms                                                                 | 257 ms: 1.01x faster                                                  |
| docutils       | 2.67 sec                                                               | 2.73 sec: 1.02x slower                                                |
| html5lib       | 63.3 ms                                                                | 62.2 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250203-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-2974035 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_generators       | 411 ms                                                                 | 383 ms: 1.07x faster                                                  |
| coroutines             | 23.0 ms                                                                | 23.2 ms: 1.01x slower                                                 |
| async_tree_memoization | 327 ms                                                                 | 331 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250203-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-2974035 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 90.4 ms                                                                | 92.5 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250203-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-2974035 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 211 ms                                                                 | 207 ms: 1.02x faster                                                  |
| regex_v8       | 24.0 ms                                                                | 23.7 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250203-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-2974035 |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 138 ms                                                                 | 137 ms: 1.01x faster                                                  |
| pickle_pure_python   | 317 us                                                                 | 315 us: 1.01x faster                                                  |
| unpickle_pure_python | 200 us                                                                 | 201 us: 1.00x slower                                                  |
| xml_etree_iterparse  | 94.7 ms                                                                | 95.3 ms: 1.01x slower                                                 |
| json_dumps           | 11.1 ms                                                                | 11.4 ms: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (4): xml_etree_generate, json_loads, xml_etree_process, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250203-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-2974035 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.9 ms                                                                | 12.9 ms: 1.00x slower                                                 |
| python_startup_no_site | 7.06 ms                                                                | 7.07 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250203-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-2974035 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 57.7 ms                                                                | 47.5 ms: 1.22x faster                                                 |
| genshi_text     | 23.0 ms                                                                | 20.9 ms: 1.10x faster                                                 |
| mako            | 10.3 ms                                                                | 9.89 ms: 1.04x faster                                                 |
| django_template | 33.1 ms                                                                | 32.2 ms: 1.03x faster                                                 |
| Geometric mean  | (ref)                                                                  | 1.09x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20250203-linux-x86_64-python-bb5c6875d6e84bf2b4e1-3.14.0a4+-bb5c687 | bm-20250203-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-2974035 |
|--------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml               | 57.7 ms                                                                | 47.5 ms: 1.22x faster                                                 |
| nqueens                  | 89.5 ms                                                                | 78.2 ms: 1.14x faster                                                 |
| genshi_text              | 23.0 ms                                                                | 20.9 ms: 1.10x faster                                                 |
| async_generators         | 411 ms                                                                 | 383 ms: 1.07x faster                                                  |
| comprehensions           | 17.1 us                                                                | 16.5 us: 1.04x faster                                                 |
| mako                     | 10.3 ms                                                                | 9.89 ms: 1.04x faster                                                 |
| hexiom                   | 7.46 ms                                                                | 7.19 ms: 1.04x faster                                                 |
| sqlglot_normalize        | 108 ms                                                                 | 105 ms: 1.03x faster                                                  |
| pyflate                  | 463 ms                                                                 | 451 ms: 1.03x faster                                                  |
| django_template          | 33.1 ms                                                                | 32.2 ms: 1.03x faster                                                 |
| sqlglot_optimize         | 54.1 ms                                                                | 52.8 ms: 1.02x faster                                                 |
| mdp                      | 2.54 sec                                                               | 2.48 sec: 1.02x faster                                                |
| scimark_sparse_mat_mult  | 4.63 ms                                                                | 4.54 ms: 1.02x faster                                                 |
| shortest_path            | 481 ms                                                                 | 473 ms: 1.02x faster                                                  |
| telco                    | 7.70 ms                                                                | 7.56 ms: 1.02x faster                                                 |
| regex_dna                | 211 ms                                                                 | 207 ms: 1.02x faster                                                  |
| html5lib                 | 63.3 ms                                                                | 62.2 ms: 1.02x faster                                                 |
| bench_thread_pool        | 894 us                                                                 | 881 us: 1.02x faster                                                  |
| scimark_fft              | 314 ms                                                                 | 309 ms: 1.01x faster                                                  |
| scimark_monte_carlo      | 63.9 ms                                                                | 63.0 ms: 1.01x faster                                                 |
| sympy_sum                | 154 ms                                                                 | 152 ms: 1.01x faster                                                  |
| 2to3                     | 261 ms                                                                 | 257 ms: 1.01x faster                                                  |
| typing_runtime_protocols | 165 us                                                                 | 163 us: 1.01x faster                                                  |
| generators               | 37.5 ms                                                                | 37.1 ms: 1.01x faster                                                 |
| go                       | 128 ms                                                                 | 127 ms: 1.01x faster                                                  |
| bench_mp_pool            | 81.0 ms                                                                | 80.1 ms: 1.01x faster                                                 |
| regex_v8                 | 24.0 ms                                                                | 23.7 ms: 1.01x faster                                                 |
| spectral_norm            | 95.6 ms                                                                | 94.7 ms: 1.01x faster                                                 |
| xml_etree_parse          | 138 ms                                                                 | 137 ms: 1.01x faster                                                  |
| sympy_integrate          | 20.5 ms                                                                | 20.4 ms: 1.01x faster                                                 |
| pickle_pure_python       | 317 us                                                                 | 315 us: 1.01x faster                                                  |
| sympy_str                | 279 ms                                                                 | 277 ms: 1.01x faster                                                  |
| crypto_pyaes             | 71.3 ms                                                                | 70.9 ms: 1.01x faster                                                 |
| connected_components     | 440 ms                                                                 | 438 ms: 1.00x faster                                                  |
| sqlalchemy_declarative   | 131 ms                                                                 | 131 ms: 1.00x faster                                                  |
| python_startup           | 12.9 ms                                                                | 12.9 ms: 1.00x slower                                                 |
| python_startup_no_site   | 7.06 ms                                                                | 7.07 ms: 1.00x slower                                                 |
| unpickle_pure_python     | 200 us                                                                 | 201 us: 1.00x slower                                                  |
| create_gc_cycles         | 2.45 ms                                                                | 2.46 ms: 1.00x slower                                                 |
| xml_etree_iterparse      | 94.7 ms                                                                | 95.3 ms: 1.01x slower                                                 |
| many_optionals           | 958 us                                                                 | 964 us: 1.01x slower                                                  |
| sqlglot_transpile        | 1.58 ms                                                                | 1.60 ms: 1.01x slower                                                 |
| thrift                   | 771 us                                                                 | 778 us: 1.01x slower                                                  |
| deltablue                | 3.49 ms                                                                | 3.52 ms: 1.01x slower                                                 |
| richards_super           | 49.7 ms                                                                | 50.2 ms: 1.01x slower                                                 |
| chaos                    | 58.8 ms                                                                | 59.5 ms: 1.01x slower                                                 |
| coroutines               | 23.0 ms                                                                | 23.2 ms: 1.01x slower                                                 |
| sqlglot_parse            | 1.28 ms                                                                | 1.29 ms: 1.01x slower                                                 |
| deepcopy_memo            | 30.2 us                                                                | 30.6 us: 1.01x slower                                                 |
| async_tree_memoization   | 327 ms                                                                 | 331 ms: 1.01x slower                                                  |
| pathlib                  | 16.1 ms                                                                | 16.3 ms: 1.01x slower                                                 |
| richards                 | 43.5 ms                                                                | 44.3 ms: 1.02x slower                                                 |
| pprint_pformat           | 1.50 sec                                                               | 1.53 sec: 1.02x slower                                                |
| coverage                 | 89.7 ms                                                                | 91.5 ms: 1.02x slower                                                 |
| docutils                 | 2.67 sec                                                               | 2.73 sec: 1.02x slower                                                |
| logging_format           | 6.17 us                                                                | 6.31 us: 1.02x slower                                                 |
| json_dumps               | 11.1 ms                                                                | 11.4 ms: 1.02x slower                                                 |
| nbody                    | 90.4 ms                                                                | 92.5 ms: 1.02x slower                                                 |
| fannkuch                 | 392 ms                                                                 | 402 ms: 1.03x slower                                                  |
| scimark_lu               | 113 ms                                                                 | 116 ms: 1.03x slower                                                  |
| pprint_safe_repr         | 728 ms                                                                 | 750 ms: 1.03x slower                                                  |
| deepcopy                 | 265 us                                                                 | 274 us: 1.03x slower                                                  |
| logging_simple           | 5.63 us                                                                | 5.82 us: 1.03x slower                                                 |
| gc_traversal             | 4.77 ms                                                                | 4.94 ms: 1.04x slower                                                 |
| logging_silent           | 108 ns                                                                 | 112 ns: 1.04x slower                                                  |
| deepcopy_reduce          | 2.73 us                                                                | 2.88 us: 1.05x slower                                                 |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (30): pylint, sphinx, sqlalchemy_imperative, async_tree_none_tg, xml_etree_generate, sqlite_synth, json_loads, bpe_tokeniser, regex_compile, scimark_sor, pidigits, regex_effbot, meteor_contest, subparsers, pycparser, k_core, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, asyncio_websockets, sympy_expand, dulwich_log, raytrace, async_tree_cpu_io_mixed, float, xml_etree_process, async_tree_none, tomli_loads, async_tree_memoization_tg, json

- Geometric mean (including insignificant results): 1.006x faster

# HPT report

- Reliability score: 83.58% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x