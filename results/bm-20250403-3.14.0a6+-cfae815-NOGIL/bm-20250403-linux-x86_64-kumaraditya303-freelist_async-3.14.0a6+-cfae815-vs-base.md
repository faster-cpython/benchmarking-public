# Results vs. base

- fork: kumaraditya303
- ref: freelist_async
- machine: linux-x86_64
- commit hash: cfae815
- commit date: 2025-04-03
- overall geometric mean: 1.005x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 287 ms                                                                 | 287 ms: 1.00x faster                                                     |
| html5lib       | 67.2 ms                                                                | 66.5 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_generators | 423 ms                                                                 | 419 ms: 1.01x faster                                                     |
| async_tree_io    | 547 ms                                                                 | 542 ms: 1.01x faster                                                     |
| async_tree_io_tg | 508 ms                                                                 | 504 ms: 1.01x faster                                                     |
| coroutines       | 23.9 ms                                                                | 24.2 ms: 1.01x slower                                                    |
| Geometric mean   | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (7): async_tree_none, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 184 ms                                                                 | 189 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 23.9 ms                                                                | 22.0 ms: 1.09x faster                                                    |
| regex_dna      | 218 ms                                                                 | 211 ms: 1.04x faster                                                     |
| regex_compile  | 145 ms                                                                 | 143 ms: 1.01x faster                                                     |
| regex_effbot   | 3.23 ms                                                                | 3.32 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 345 us                                                                 | 336 us: 1.03x faster                                                     |
| unpickle_pure_python | 240 us                                                                 | 236 us: 1.01x faster                                                     |
| tomli_loads          | 2.17 sec                                                               | 2.15 sec: 1.01x faster                                                   |
| json_dumps           | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                    |
| xml_etree_parse      | 147 ms                                                                 | 148 ms: 1.01x slower                                                     |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (4): xml_etree_iterparse, xml_etree_generate, xml_etree_process, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                                | 15.6 ms: 1.00x slower                                                    |
| python_startup_no_site | 10.9 ms                                                                | 10.9 ms: 1.00x slower                                                    |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 38.5 ms                                                                | 38.2 ms: 1.01x faster                                                    |
| mako            | 15.6 ms                                                                | 15.7 ms: 1.01x slower                                                    |
| genshi_xml      | 57.5 ms                                                                | 58.0 ms: 1.01x slower                                                    |
| genshi_text     | 26.7 ms                                                                | 27.1 ms: 1.02x slower                                                    |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                             |

All benchmarks:
===============

| Benchmark                | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|--------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8                 | 23.9 ms                                                                | 22.0 ms: 1.09x faster                                                    |
| pyflate                  | 501 ms                                                                 | 469 ms: 1.07x faster                                                     |
| scimark_sparse_mat_mult  | 5.60 ms                                                                | 5.28 ms: 1.06x faster                                                    |
| logging_silent           | 108 ns                                                                 | 103 ns: 1.04x faster                                                     |
| regex_dna                | 218 ms                                                                 | 211 ms: 1.04x faster                                                     |
| pprint_safe_repr         | 826 ms                                                                 | 801 ms: 1.03x faster                                                     |
| pprint_pformat           | 1.70 sec                                                               | 1.66 sec: 1.03x faster                                                   |
| pickle_pure_python       | 345 us                                                                 | 336 us: 1.03x faster                                                     |
| deltablue                | 3.69 ms                                                                | 3.60 ms: 1.02x faster                                                    |
| logging_simple           | 6.57 us                                                                | 6.41 us: 1.02x faster                                                    |
| scimark_lu               | 135 ms                                                                 | 132 ms: 1.02x faster                                                     |
| pathlib                  | 17.0 ms                                                                | 16.7 ms: 1.02x faster                                                    |
| deepcopy_memo            | 35.8 us                                                                | 35.2 us: 1.02x faster                                                    |
| logging_format           | 7.36 us                                                                | 7.26 us: 1.01x faster                                                    |
| bpe_tokeniser            | 4.85 sec                                                               | 4.79 sec: 1.01x faster                                                   |
| unpickle_pure_python     | 240 us                                                                 | 236 us: 1.01x faster                                                     |
| scimark_monte_carlo      | 79.8 ms                                                                | 78.7 ms: 1.01x faster                                                    |
| go                       | 130 ms                                                                 | 129 ms: 1.01x faster                                                     |
| typing_runtime_protocols | 197 us                                                                 | 195 us: 1.01x faster                                                     |
| regex_compile            | 145 ms                                                                 | 143 ms: 1.01x faster                                                     |
| comprehensions           | 19.4 us                                                                | 19.2 us: 1.01x faster                                                    |
| scimark_sor              | 128 ms                                                                 | 127 ms: 1.01x faster                                                     |
| html5lib                 | 67.2 ms                                                                | 66.5 ms: 1.01x faster                                                    |
| fannkuch                 | 487 ms                                                                 | 482 ms: 1.01x faster                                                     |
| raytrace                 | 312 ms                                                                 | 308 ms: 1.01x faster                                                     |
| tomli_loads              | 2.17 sec                                                               | 2.15 sec: 1.01x faster                                                   |
| async_generators         | 423 ms                                                                 | 419 ms: 1.01x faster                                                     |
| async_tree_io            | 547 ms                                                                 | 542 ms: 1.01x faster                                                     |
| scimark_fft              | 374 ms                                                                 | 371 ms: 1.01x faster                                                     |
| mdp                      | 1.38 sec                                                               | 1.37 sec: 1.01x faster                                                   |
| django_template          | 38.5 ms                                                                | 38.2 ms: 1.01x faster                                                    |
| async_tree_io_tg         | 508 ms                                                                 | 504 ms: 1.01x faster                                                     |
| nqueens                  | 89.8 ms                                                                | 89.3 ms: 1.01x faster                                                    |
| crypto_pyaes             | 86.5 ms                                                                | 86.1 ms: 1.01x faster                                                    |
| chaos                    | 65.3 ms                                                                | 65.0 ms: 1.00x faster                                                    |
| sqlalchemy_declarative   | 158 ms                                                                 | 158 ms: 1.00x faster                                                     |
| sqlglot_v2_normalize     | 115 ms                                                                 | 115 ms: 1.00x faster                                                     |
| many_optionals           | 1.04 ms                                                                | 1.04 ms: 1.00x faster                                                    |
| hexiom                   | 7.20 ms                                                                | 7.17 ms: 1.00x faster                                                    |
| json_dumps               | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                    |
| 2to3                     | 287 ms                                                                 | 287 ms: 1.00x faster                                                     |
| python_startup           | 15.6 ms                                                                | 15.6 ms: 1.00x slower                                                    |
| python_startup_no_site   | 10.9 ms                                                                | 10.9 ms: 1.00x slower                                                    |
| connected_components     | 523 ms                                                                 | 525 ms: 1.00x slower                                                     |
| k_core                   | 2.40 sec                                                               | 2.41 sec: 1.01x slower                                                   |
| shortest_path            | 560 ms                                                                 | 563 ms: 1.01x slower                                                     |
| deepcopy                 | 290 us                                                                 | 292 us: 1.01x slower                                                     |
| mako                     | 15.6 ms                                                                | 15.7 ms: 1.01x slower                                                    |
| create_gc_cycles         | 1.68 ms                                                                | 1.69 ms: 1.01x slower                                                    |
| sqlite_synth             | 2.75 us                                                                | 2.78 us: 1.01x slower                                                    |
| genshi_xml               | 57.5 ms                                                                | 58.0 ms: 1.01x slower                                                    |
| xml_etree_parse          | 147 ms                                                                 | 148 ms: 1.01x slower                                                     |
| coroutines               | 23.9 ms                                                                | 24.2 ms: 1.01x slower                                                    |
| genshi_text              | 26.7 ms                                                                | 27.1 ms: 1.02x slower                                                    |
| richards                 | 50.7 ms                                                                | 51.5 ms: 1.02x slower                                                    |
| meteor_contest           | 130 ms                                                                 | 133 ms: 1.02x slower                                                     |
| telco                    | 8.99 ms                                                                | 9.18 ms: 1.02x slower                                                    |
| deepcopy_reduce          | 3.02 us                                                                | 3.10 us: 1.03x slower                                                    |
| regex_effbot             | 3.23 ms                                                                | 3.32 ms: 1.03x slower                                                    |
| pidigits                 | 184 ms                                                                 | 189 ms: 1.03x slower                                                     |
| pycparser                | 1.12 sec                                                               | 1.16 sec: 1.04x slower                                                   |
| Geometric mean           | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (34): async_tree_none, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed, sqlalchemy_imperative, coverage, docutils, sphinx, async_tree_none_tg, sqlglot_v2_parse, pylint, xml_etree_iterparse, bench_mp_pool, sympy_integrate, sqlglot_v2_optimize, nbody, sympy_expand, sympy_sum, richards_super, xml_etree_generate, async_tree_cpu_io_mixed_tg, bench_thread_pool, asyncio_websockets, xml_etree_process, generators, gc_traversal, sqlglot_v2_transpile, dulwich_log, sympy_str, float, subparsers, spectral_norm, json_loads, json

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x