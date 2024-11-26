# Results vs. base

- fork: brandtbucher
- ref: warmup_side_1024
- machine: linux-x86_64
- commit hash: e2daeb7
- commit date: 2024-11-20
- overall geometric mean: 1.002x faster
- HPT reliability: 94.30%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 262 ms                                                                 | 261 ms: 1.00x faster                                                     |
| docutils       | 2.83 sec                                                               | 2.81 sec: 1.01x faster                                                   |
| html5lib       | 66.8 ms                                                                | 67.2 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| coroutines       | 23.4 ms                                                                | 22.8 ms: 1.03x faster                                                    |
| async_generators | 456 ms                                                                 | 451 ms: 1.01x faster                                                     |
| Geometric mean   | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_memoization, async_tree_io, async_tree_none_tg, asyncio_websockets, async_tree_io_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 82.5 ms                                                                | 84.8 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.47 ms                                                                | 3.38 ms: 1.03x faster                                                    |
| regex_compile  | 131 ms                                                                 | 129 ms: 1.02x faster                                                     |
| regex_dna      | 223 ms                                                                 | 220 ms: 1.01x faster                                                     |
| regex_v8       | 25.5 ms                                                                | 25.7 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate   | 83.0 ms                                                                | 79.5 ms: 1.04x faster                                                    |
| xml_etree_process    | 57.5 ms                                                                | 56.2 ms: 1.02x faster                                                    |
| unpickle_pure_python | 193 us                                                                 | 191 us: 1.01x faster                                                     |
| json_dumps           | 11.2 ms                                                                | 11.1 ms: 1.01x faster                                                    |
| tomli_loads          | 1.95 sec                                                               | 1.94 sec: 1.01x faster                                                   |
| json_loads           | 26.3 us                                                                | 26.4 us: 1.00x slower                                                    |
| pickle_pure_python   | 319 us                                                                 | 323 us: 1.01x slower                                                     |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                                    |
| python_startup_no_site | 7.05 ms                                                                | 7.08 ms: 1.01x slower                                                    |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 25.0 ms                                                                | 24.2 ms: 1.03x faster                                                    |
| genshi_xml     | 57.1 ms                                                                | 55.5 ms: 1.03x faster                                                    |
| mako           | 10.1 ms                                                                | 10.2 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20241120-linux-x86_64-python-0af4ec30bd2e3a523503-3.14.0a2+-0af4ec3 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|--------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate       | 83.0 ms                                                                | 79.5 ms: 1.04x faster                                                    |
| pylint                   | 284 ms                                                                 | 274 ms: 1.04x faster                                                     |
| go                       | 134 ms                                                                 | 129 ms: 1.04x faster                                                     |
| genshi_text              | 25.0 ms                                                                | 24.2 ms: 1.03x faster                                                    |
| genshi_xml               | 57.1 ms                                                                | 55.5 ms: 1.03x faster                                                    |
| regex_effbot             | 3.47 ms                                                                | 3.38 ms: 1.03x faster                                                    |
| coroutines               | 23.4 ms                                                                | 22.8 ms: 1.03x faster                                                    |
| xml_etree_process        | 57.5 ms                                                                | 56.2 ms: 1.02x faster                                                    |
| sqlglot_normalize        | 111 ms                                                                 | 109 ms: 1.02x faster                                                     |
| typing_runtime_protocols | 170 us                                                                 | 167 us: 1.02x faster                                                     |
| telco                    | 7.58 ms                                                                | 7.46 ms: 1.02x faster                                                    |
| regex_compile            | 131 ms                                                                 | 129 ms: 1.02x faster                                                     |
| nqueens                  | 90.8 ms                                                                | 89.5 ms: 1.02x faster                                                    |
| comprehensions           | 17.6 us                                                                | 17.3 us: 1.01x faster                                                    |
| fannkuch                 | 389 ms                                                                 | 384 ms: 1.01x faster                                                     |
| shortest_path            | 485 ms                                                                 | 479 ms: 1.01x faster                                                     |
| sympy_sum                | 160 ms                                                                 | 158 ms: 1.01x faster                                                     |
| unpickle_pure_python     | 193 us                                                                 | 191 us: 1.01x faster                                                     |
| dulwich_log              | 68.0 ms                                                                | 67.2 ms: 1.01x faster                                                    |
| sympy_integrate          | 21.0 ms                                                                | 20.8 ms: 1.01x faster                                                    |
| regex_dna                | 223 ms                                                                 | 220 ms: 1.01x faster                                                     |
| many_optionals           | 990 us                                                                 | 978 us: 1.01x faster                                                     |
| pathlib                  | 16.4 ms                                                                | 16.2 ms: 1.01x faster                                                    |
| json_dumps               | 11.2 ms                                                                | 11.1 ms: 1.01x faster                                                    |
| sympy_str                | 287 ms                                                                 | 284 ms: 1.01x faster                                                     |
| logging_simple           | 5.55 us                                                                | 5.49 us: 1.01x faster                                                    |
| sqlalchemy_declarative   | 131 ms                                                                 | 129 ms: 1.01x faster                                                     |
| sqlglot_transpile        | 1.65 ms                                                                | 1.63 ms: 1.01x faster                                                    |
| logging_format           | 6.17 us                                                                | 6.10 us: 1.01x faster                                                    |
| async_generators         | 456 ms                                                                 | 451 ms: 1.01x faster                                                     |
| scimark_fft              | 317 ms                                                                 | 315 ms: 1.01x faster                                                     |
| tomli_loads              | 1.95 sec                                                               | 1.94 sec: 1.01x faster                                                   |
| connected_components     | 440 ms                                                                 | 438 ms: 1.01x faster                                                     |
| sympy_expand             | 482 ms                                                                 | 479 ms: 1.01x faster                                                     |
| docutils                 | 2.83 sec                                                               | 2.81 sec: 1.01x faster                                                   |
| chaos                    | 58.9 ms                                                                | 58.6 ms: 1.01x faster                                                    |
| bench_thread_pool        | 876 us                                                                 | 872 us: 1.00x faster                                                     |
| meteor_contest           | 108 ms                                                                 | 107 ms: 1.00x faster                                                     |
| 2to3                     | 262 ms                                                                 | 261 ms: 1.00x faster                                                     |
| bpe_tokeniser            | 4.50 sec                                                               | 4.51 sec: 1.00x slower                                                   |
| json_loads               | 26.3 us                                                                | 26.4 us: 1.00x slower                                                    |
| python_startup           | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                                    |
| python_startup_no_site   | 7.05 ms                                                                | 7.08 ms: 1.01x slower                                                    |
| bench_mp_pool            | 78.9 ms                                                                | 79.4 ms: 1.01x slower                                                    |
| html5lib                 | 66.8 ms                                                                | 67.2 ms: 1.01x slower                                                    |
| create_gc_cycles         | 2.64 ms                                                                | 2.66 ms: 1.01x slower                                                    |
| subparsers               | 21.0 ms                                                                | 21.1 ms: 1.01x slower                                                    |
| regex_v8                 | 25.5 ms                                                                | 25.7 ms: 1.01x slower                                                    |
| generators               | 35.2 ms                                                                | 35.6 ms: 1.01x slower                                                    |
| sqlalchemy_imperative    | 17.2 ms                                                                | 17.4 ms: 1.01x slower                                                    |
| coverage                 | 83.8 ms                                                                | 84.8 ms: 1.01x slower                                                    |
| pycparser                | 1.13 sec                                                               | 1.14 sec: 1.01x slower                                                   |
| pickle_pure_python       | 319 us                                                                 | 323 us: 1.01x slower                                                     |
| mako                     | 10.1 ms                                                                | 10.2 ms: 1.01x slower                                                    |
| scimark_sparse_mat_mult  | 4.67 ms                                                                | 4.74 ms: 1.01x slower                                                    |
| gc_traversal             | 4.35 ms                                                                | 4.45 ms: 1.02x slower                                                    |
| pprint_pformat           | 1.46 sec                                                               | 1.49 sec: 1.03x slower                                                   |
| raytrace                 | 280 ms                                                                 | 287 ms: 1.03x slower                                                     |
| nbody                    | 82.5 ms                                                                | 84.8 ms: 1.03x slower                                                    |
| logging_silent           | 99.4 ns                                                                | 103 ns: 1.04x slower                                                     |
| mdp                      | 2.59 sec                                                               | 2.71 sec: 1.05x slower                                                   |
| richards_super           | 42.5 ms                                                                | 46.4 ms: 1.09x slower                                                    |
| richards                 | 36.9 ms                                                                | 40.6 ms: 1.10x slower                                                    |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (34): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, k_core, djangocms, sphinx, json, scimark_sor, hexiom, sqlglot_parse, sqlite_synth, xml_etree_iterparse, deepcopy_memo, spectral_norm, scimark_monte_carlo, async_tree_memoization_tg, sqlglot_optimize, pidigits, xml_etree_parse, deepcopy, django_template, deepcopy_reduce, crypto_pyaes, async_tree_memoization, scimark_lu, async_tree_io, async_tree_none_tg, asyncio_websockets, async_tree_io_tg, thrift, pprint_safe_repr, float, async_tree_none, deltablue, pyflate

- Geometric mean (including insignificant results): 1.002x faster
# HPT report

- Reliability score: 94.30% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x