# Results vs. base

- fork: fluhus
- ref: amit
- machine: linux-x86_64
- commit hash: 138f037
- commit date: 2025-03-29
- overall geometric mean: 1.002x faster
- HPT reliability: 97.54%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250327-linux-x86_64-python-8a00c9a4d2ce9d373b13-3.14.0a6+-8a00c9a | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 263 ms                                                                 | 262 ms: 1.00x faster                                   |
| docutils       | 2.68 sec                                                               | 2.69 sec: 1.00x slower                                 |
| Geometric mean | (ref)                                                                  | 1.00x faster                                           |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250327-linux-x86_64-python-8a00c9a4d2ce9d373b13-3.14.0a6+-8a00c9a | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|------------------|:----------------------------------------------------------------------:|:------------------------------------------------------:|
| coroutines       | 23.3 ms                                                                | 23.0 ms: 1.01x faster                                  |
| async_generators | 414 ms                                                                 | 412 ms: 1.00x faster                                   |
| Geometric mean   | (ref)                                                                  | 1.00x faster                                           |

Benchmark hidden because not significant (9): async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_io, async_tree_memoization, async_tree_none, async_tree_none_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250327-linux-x86_64-python-8a00c9a4d2ce9d373b13-3.14.0a6+-8a00c9a | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------:|
| float          | 63.8 ms                                                                | 63.0 ms: 1.01x faster                                  |
| nbody          | 85.5 ms                                                                | 84.9 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                                  | 1.01x faster                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250327-linux-x86_64-python-8a00c9a4d2ce9d373b13-3.14.0a6+-8a00c9a | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------:|
| regex_v8       | 24.0 ms                                                                | 23.1 ms: 1.04x faster                                  |
| regex_dna      | 228 ms                                                                 | 223 ms: 1.02x faster                                   |
| regex_effbot   | 3.51 ms                                                                | 3.47 ms: 1.01x faster                                  |
| regex_compile  | 128 ms                                                                 | 128 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                                  | 1.02x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250327-linux-x86_64-python-8a00c9a4d2ce9d373b13-3.14.0a6+-8a00c9a | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|---------------------|:----------------------------------------------------------------------:|:------------------------------------------------------:|
| xml_etree_process   | 56.3 ms                                                                | 55.7 ms: 1.01x faster                                  |
| tomli_loads         | 1.87 sec                                                               | 1.85 sec: 1.01x faster                                 |
| xml_etree_iterparse | 98.1 ms                                                                | 97.7 ms: 1.00x faster                                  |
| json_loads          | 29.9 us                                                                | 30.0 us: 1.00x slower                                  |
| xml_etree_generate  | 79.3 ms                                                                | 80.2 ms: 1.01x slower                                  |
| xml_etree_parse     | 139 ms                                                                 | 141 ms: 1.01x slower                                   |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (3): json_dumps, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250327-linux-x86_64-python-8a00c9a4d2ce9d373b13-3.14.0a6+-8a00c9a | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 8.22 ms                                                                | 8.20 ms: 1.00x faster                                  |
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                  |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250327-linux-x86_64-python-8a00c9a4d2ce9d373b13-3.14.0a6+-8a00c9a | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------:|
| django_template | 32.2 ms                                                                | 32.3 ms: 1.01x slower                                  |
| mako            | 11.0 ms                                                                | 11.1 ms: 1.01x slower                                  |
| genshi_xml      | 49.4 ms                                                                | 49.9 ms: 1.01x slower                                  |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20250327-linux-x86_64-python-8a00c9a4d2ce9d373b13-3.14.0a6+-8a00c9a | bm-20250329-linux-x86_64-fluhus-amit-3.14.0a6+-138f037 |
|--------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------:|
| gc_traversal             | 5.05 ms                                                                | 4.76 ms: 1.06x faster                                  |
| regex_v8                 | 24.0 ms                                                                | 23.1 ms: 1.04x faster                                  |
| regex_dna                | 228 ms                                                                 | 223 ms: 1.02x faster                                   |
| scimark_sor              | 121 ms                                                                 | 119 ms: 1.02x faster                                   |
| logging_silent           | 99.4 ns                                                                | 97.6 ns: 1.02x faster                                  |
| typing_runtime_protocols | 169 us                                                                 | 166 us: 1.02x faster                                   |
| pprint_safe_repr         | 777 ms                                                                 | 764 ms: 1.02x faster                                   |
| pathlib                  | 16.8 ms                                                                | 16.5 ms: 1.02x faster                                  |
| scimark_fft              | 314 ms                                                                 | 309 ms: 1.02x faster                                   |
| telco                    | 7.87 ms                                                                | 7.76 ms: 1.01x faster                                  |
| regex_effbot             | 3.51 ms                                                                | 3.47 ms: 1.01x faster                                  |
| coroutines               | 23.3 ms                                                                | 23.0 ms: 1.01x faster                                  |
| float                    | 63.8 ms                                                                | 63.0 ms: 1.01x faster                                  |
| richards                 | 35.6 ms                                                                | 35.2 ms: 1.01x faster                                  |
| sqlite_synth             | 2.74 us                                                                | 2.71 us: 1.01x faster                                  |
| xml_etree_process        | 56.3 ms                                                                | 55.7 ms: 1.01x faster                                  |
| tomli_loads              | 1.87 sec                                                               | 1.85 sec: 1.01x faster                                 |
| bench_mp_pool            | 83.8 ms                                                                | 83.0 ms: 1.01x faster                                  |
| sqlalchemy_imperative    | 17.2 ms                                                                | 17.0 ms: 1.01x faster                                  |
| raytrace                 | 267 ms                                                                 | 266 ms: 1.01x faster                                   |
| nbody                    | 85.5 ms                                                                | 84.9 ms: 1.01x faster                                  |
| scimark_sparse_mat_mult  | 4.66 ms                                                                | 4.63 ms: 1.01x faster                                  |
| create_gc_cycles         | 2.49 ms                                                                | 2.48 ms: 1.01x faster                                  |
| deltablue                | 3.03 ms                                                                | 3.01 ms: 1.01x faster                                  |
| chaos                    | 59.1 ms                                                                | 58.8 ms: 1.01x faster                                  |
| coverage                 | 85.1 ms                                                                | 84.6 ms: 1.01x faster                                  |
| regex_compile            | 128 ms                                                                 | 128 ms: 1.01x faster                                   |
| sqlalchemy_declarative   | 132 ms                                                                 | 131 ms: 1.00x faster                                   |
| xml_etree_iterparse      | 98.1 ms                                                                | 97.7 ms: 1.00x faster                                  |
| async_generators         | 414 ms                                                                 | 412 ms: 1.00x faster                                   |
| 2to3                     | 263 ms                                                                 | 262 ms: 1.00x faster                                   |
| dulwich_log              | 60.6 ms                                                                | 60.4 ms: 1.00x faster                                  |
| python_startup_no_site   | 8.22 ms                                                                | 8.20 ms: 1.00x faster                                  |
| sqlglot_v2_optimize      | 54.2 ms                                                                | 54.1 ms: 1.00x faster                                  |
| bench_thread_pool        | 884 us                                                                 | 882 us: 1.00x faster                                   |
| python_startup           | 13.1 ms                                                                | 13.1 ms: 1.00x faster                                  |
| sympy_expand             | 474 ms                                                                 | 476 ms: 1.00x slower                                   |
| sympy_str                | 274 ms                                                                 | 275 ms: 1.00x slower                                   |
| json_loads               | 29.9 us                                                                | 30.0 us: 1.00x slower                                  |
| docutils                 | 2.68 sec                                                               | 2.69 sec: 1.00x slower                                 |
| fannkuch                 | 417 ms                                                                 | 419 ms: 1.00x slower                                   |
| sympy_integrate          | 19.9 ms                                                                | 20.0 ms: 1.01x slower                                  |
| crypto_pyaes             | 75.3 ms                                                                | 75.7 ms: 1.01x slower                                  |
| django_template          | 32.2 ms                                                                | 32.3 ms: 1.01x slower                                  |
| sympy_sum                | 152 ms                                                                 | 153 ms: 1.01x slower                                   |
| spectral_norm            | 92.3 ms                                                                | 92.9 ms: 1.01x slower                                  |
| meteor_contest           | 108 ms                                                                 | 109 ms: 1.01x slower                                   |
| json                     | 5.29 ms                                                                | 5.33 ms: 1.01x slower                                  |
| subparsers               | 21.0 ms                                                                | 21.2 ms: 1.01x slower                                  |
| mako                     | 11.0 ms                                                                | 11.1 ms: 1.01x slower                                  |
| genshi_xml               | 49.4 ms                                                                | 49.9 ms: 1.01x slower                                  |
| deepcopy_reduce          | 2.68 us                                                                | 2.71 us: 1.01x slower                                  |
| hexiom                   | 6.70 ms                                                                | 6.78 ms: 1.01x slower                                  |
| xml_etree_generate       | 79.3 ms                                                                | 80.2 ms: 1.01x slower                                  |
| xml_etree_parse          | 139 ms                                                                 | 141 ms: 1.01x slower                                   |
| scimark_lu               | 115 ms                                                                 | 117 ms: 1.01x slower                                   |
| comprehensions           | 18.5 us                                                                | 18.8 us: 1.02x slower                                  |
| scimark_monte_carlo      | 66.9 ms                                                                | 68.0 ms: 1.02x slower                                  |
| shortest_path            | 492 ms                                                                 | 501 ms: 1.02x slower                                   |
| pyflate                  | 433 ms                                                                 | 443 ms: 1.02x slower                                   |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                           |

Benchmark hidden because not significant (35): async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, html5lib, pylint, generators, sphinx, mdp, k_core, json_dumps, nqueens, connected_components, sqlglot_v2_transpile, sqlglot_v2_parse, pycparser, async_tree_cpu_io_mixed, genshi_text, asyncio_websockets, async_tree_io, go, pidigits, pprint_pformat, sqlglot_v2_normalize, async_tree_memoization, unpickle_pure_python, deepcopy, bpe_tokeniser, async_tree_none, logging_simple, pickle_pure_python, async_tree_none_tg, richards_super, logging_format, async_tree_io_tg, deepcopy_memo, many_optionals

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 97.54% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x