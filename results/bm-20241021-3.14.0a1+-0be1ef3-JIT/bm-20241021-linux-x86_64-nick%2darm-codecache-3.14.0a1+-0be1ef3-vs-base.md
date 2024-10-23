# Results vs. base

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.00x faster
- HPT reliability: 86.09%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 278 ms                                                                 | 276 ms: 1.01x faster                                            |
| docutils       | 2.93 sec                                                               | 2.91 sec: 1.01x faster                                          |
| html5lib       | 65.5 ms                                                                | 67.1 ms: 1.02x slower                                           |
| tornado_http   | 94.2 ms                                                                | 94.8 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                    |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_generators | 455 ms                                                                 | 457 ms: 1.01x slower                                            |
| async_tree_io_tg | 965 ms                                                                 | 976 ms: 1.01x slower                                            |
| coroutines       | 23.1 ms                                                                | 23.7 ms: 1.02x slower                                           |
| Geometric mean   | (ref)                                                                  | 1.01x slower                                                    |

Benchmark hidden because not significant (8): async_tree_none_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 83.7 ms                                                                | 82.3 ms: 1.02x faster                                           |
| float          | 76.1 ms                                                                | 75.6 ms: 1.01x faster                                           |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                            |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_dna      | 220 ms                                                                 | 214 ms: 1.03x faster                                            |
| regex_effbot   | 3.76 ms                                                                | 3.72 ms: 1.01x faster                                           |
| regex_v8       | 24.8 ms                                                                | 24.7 ms: 1.00x faster                                           |
| regex_compile  | 137 ms                                                                 | 139 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 11.2 ms                                                                | 10.8 ms: 1.04x faster                                           |
| xml_etree_process    | 55.6 ms                                                                | 54.8 ms: 1.01x faster                                           |
| pickle_pure_python   | 314 us                                                                 | 311 us: 1.01x faster                                            |
| unpickle_pure_python | 217 us                                                                 | 215 us: 1.01x faster                                            |
| tomli_loads          | 1.91 sec                                                               | 1.90 sec: 1.01x faster                                          |
| xml_etree_iterparse  | 101 ms                                                                 | 101 ms: 1.01x slower                                            |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                    |

Benchmark hidden because not significant (3): xml_etree_generate, json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 7.09 ms                                                                | 7.07 ms: 1.00x faster                                           |
| python_startup         | 11.9 ms                                                                | 11.8 ms: 1.00x faster                                           |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 36.1 ms                                                                | 35.8 ms: 1.01x faster                                           |
| mako            | 10.1 ms                                                                | 10.2 ms: 1.01x slower                                           |
| genshi_xml      | 58.4 ms                                                                | 60.4 ms: 1.03x slower                                           |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                    |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark              | bm-20241021-linux-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-linux-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| gc_traversal           | 4.79 ms                                                                | 4.37 ms: 1.10x faster                                           |
| logging_silent         | 102 ns                                                                 | 97.1 ns: 1.05x faster                                           |
| richards               | 42.7 ms                                                                | 40.8 ms: 1.05x faster                                           |
| pprint_safe_repr       | 724 ms                                                                 | 696 ms: 1.04x faster                                            |
| json_dumps             | 11.2 ms                                                                | 10.8 ms: 1.04x faster                                           |
| coverage               | 87.7 ms                                                                | 84.4 ms: 1.04x faster                                           |
| richards_super         | 49.3 ms                                                                | 47.6 ms: 1.04x faster                                           |
| regex_dna              | 220 ms                                                                 | 214 ms: 1.03x faster                                            |
| scimark_fft            | 322 ms                                                                 | 315 ms: 1.02x faster                                            |
| thrift                 | 796 us                                                                 | 779 us: 1.02x faster                                            |
| nbody                  | 83.7 ms                                                                | 82.3 ms: 1.02x faster                                           |
| xml_etree_process      | 55.6 ms                                                                | 54.8 ms: 1.01x faster                                           |
| pycparser              | 1.15 sec                                                               | 1.14 sec: 1.01x faster                                          |
| pyflate                | 454 ms                                                                 | 447 ms: 1.01x faster                                            |
| telco                  | 7.69 ms                                                                | 7.58 ms: 1.01x faster                                           |
| scimark_lu             | 114 ms                                                                 | 113 ms: 1.01x faster                                            |
| create_gc_cycles       | 2.69 ms                                                                | 2.66 ms: 1.01x faster                                           |
| regex_effbot           | 3.76 ms                                                                | 3.72 ms: 1.01x faster                                           |
| pickle_pure_python     | 314 us                                                                 | 311 us: 1.01x faster                                            |
| django_template        | 36.1 ms                                                                | 35.8 ms: 1.01x faster                                           |
| 2to3                   | 278 ms                                                                 | 276 ms: 1.01x faster                                            |
| docutils               | 2.93 sec                                                               | 2.91 sec: 1.01x faster                                          |
| unpickle_pure_python   | 217 us                                                                 | 215 us: 1.01x faster                                            |
| float                  | 76.1 ms                                                                | 75.6 ms: 1.01x faster                                           |
| tomli_loads            | 1.91 sec                                                               | 1.90 sec: 1.01x faster                                          |
| sqlglot_normalize      | 114 ms                                                                 | 113 ms: 1.01x faster                                            |
| raytrace               | 275 ms                                                                 | 273 ms: 1.01x faster                                            |
| sympy_str              | 301 ms                                                                 | 299 ms: 1.01x faster                                            |
| sqlglot_optimize       | 59.7 ms                                                                | 59.3 ms: 1.01x faster                                           |
| bench_mp_pool          | 84.3 ms                                                                | 83.8 ms: 1.01x faster                                           |
| regex_v8               | 24.8 ms                                                                | 24.7 ms: 1.00x faster                                           |
| python_startup_no_site | 7.09 ms                                                                | 7.07 ms: 1.00x faster                                           |
| python_startup         | 11.9 ms                                                                | 11.8 ms: 1.00x faster                                           |
| meteor_contest         | 107 ms                                                                 | 107 ms: 1.00x faster                                            |
| pidigits               | 186 ms                                                                 | 186 ms: 1.00x faster                                            |
| spectral_norm          | 114 ms                                                                 | 115 ms: 1.00x slower                                            |
| dulwich_log            | 66.7 ms                                                                | 66.9 ms: 1.00x slower                                           |
| generators             | 35.3 ms                                                                | 35.5 ms: 1.00x slower                                           |
| async_generators       | 455 ms                                                                 | 457 ms: 1.01x slower                                            |
| logging_simple         | 5.53 us                                                                | 5.57 us: 1.01x slower                                           |
| tornado_http           | 94.2 ms                                                                | 94.8 ms: 1.01x slower                                           |
| bpe_tokeniser          | 4.43 sec                                                               | 4.46 sec: 1.01x slower                                          |
| xml_etree_iterparse    | 101 ms                                                                 | 101 ms: 1.01x slower                                            |
| go                     | 132 ms                                                                 | 133 ms: 1.01x slower                                            |
| pathlib                | 15.8 ms                                                                | 16.0 ms: 1.01x slower                                           |
| regex_compile          | 137 ms                                                                 | 139 ms: 1.01x slower                                            |
| async_tree_io_tg       | 965 ms                                                                 | 976 ms: 1.01x slower                                            |
| mako                   | 10.1 ms                                                                | 10.2 ms: 1.01x slower                                           |
| coroutines             | 23.1 ms                                                                | 23.7 ms: 1.02x slower                                           |
| html5lib               | 65.5 ms                                                                | 67.1 ms: 1.02x slower                                           |
| genshi_xml             | 58.4 ms                                                                | 60.4 ms: 1.03x slower                                           |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                    |

Benchmark hidden because not significant (38): pprint_pformat, sphinx, scimark_monte_carlo, pylint, typing_runtime_protocols, deltablue, chaos, scimark_sor, json, sympy_sum, xml_etree_generate, deepcopy, logging_format, sqlglot_parse, async_tree_none_tg, nqueens, sympy_integrate, deepcopy_memo, asyncio_websockets, json_loads, mdp, sqlglot_transpile, comprehensions, bench_thread_pool, hexiom, sympy_expand, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, xml_etree_parse, deepcopy_reduce, genshi_text, async_tree_cpu_io_mixed, fannkuch, crypto_pyaes, async_tree_none, async_tree_io, async_tree_memoization, scimark_sparse_mat_mult

# HPT report

- Reliability score: 86.09% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x