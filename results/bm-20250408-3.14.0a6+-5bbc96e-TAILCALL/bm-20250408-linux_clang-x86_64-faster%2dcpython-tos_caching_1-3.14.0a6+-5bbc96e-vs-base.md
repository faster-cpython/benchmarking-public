# Results vs. base

- fork: faster-cpython
- ref: tos_caching_1
- machine: linux-x86_64
- commit hash: 5bbc96e
- commit date: 2025-04-08
- overall geometric mean: 1.009x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 243 ms                                                                 | 245 ms: 1.01x slower                                                      |
| docutils       | 2.57 sec                                                               | 2.58 sec: 1.00x slower                                                    |
| html5lib       | 57.1 ms                                                                | 58.5 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_generators       | 381 ms                                                                 | 386 ms: 1.01x slower                                                      |
| async_tree_none_tg     | 244 ms                                                                 | 247 ms: 1.01x slower                                                      |
| async_tree_io          | 596 ms                                                                 | 605 ms: 1.01x slower                                                      |
| async_tree_none        | 252 ms                                                                 | 257 ms: 1.02x slower                                                      |
| async_tree_memoization | 303 ms                                                                 | 309 ms: 1.02x slower                                                      |
| coroutines             | 21.7 ms                                                                | 23.2 ms: 1.07x slower                                                     |
| Geometric mean         | (ref)                                                                  | 1.02x slower                                                              |

Benchmark hidden because not significant (5): asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 83.5 ms                                                                | 82.1 ms: 1.02x faster                                                     |
| pidigits       | 202 ms                                                                 | 202 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 22.6 ms                                                                | 22.3 ms: 1.01x faster                                                     |
| regex_dna      | 187 ms                                                                 | 191 ms: 1.02x slower                                                      |
| regex_compile  | 123 ms                                                                 | 126 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                                | 12.3 ms: 1.02x faster                                                     |
| json_loads           | 28.2 us                                                                | 28.3 us: 1.00x slower                                                     |
| xml_etree_iterparse  | 102 ms                                                                 | 103 ms: 1.01x slower                                                      |
| xml_etree_parse      | 161 ms                                                                 | 162 ms: 1.01x slower                                                      |
| tomli_loads          | 1.82 sec                                                               | 1.84 sec: 1.01x slower                                                    |
| xml_etree_process    | 59.3 ms                                                                | 60.7 ms: 1.02x slower                                                     |
| xml_etree_generate   | 85.7 ms                                                                | 87.9 ms: 1.03x slower                                                     |
| pickle_pure_python   | 300 us                                                                 | 309 us: 1.03x slower                                                      |
| unpickle_pure_python | 212 us                                                                 | 220 us: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                                | 13.0 ms: 1.00x slower                                                     |
| python_startup_no_site | 8.09 ms                                                                | 8.12 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 31.4 ms                                                                | 31.9 ms: 1.02x slower                                                     |
| genshi_text     | 20.5 ms                                                                | 21.0 ms: 1.02x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|--------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| scimark_sparse_mat_mult  | 4.31 ms                                                                | 3.81 ms: 1.13x faster                                                     |
| json_dumps               | 12.6 ms                                                                | 12.3 ms: 1.02x faster                                                     |
| comprehensions           | 15.9 us                                                                | 15.6 us: 1.02x faster                                                     |
| nbody                    | 83.5 ms                                                                | 82.1 ms: 1.02x faster                                                     |
| pycparser                | 1.11 sec                                                               | 1.09 sec: 1.02x faster                                                    |
| scimark_monte_carlo      | 59.5 ms                                                                | 58.6 ms: 1.01x faster                                                     |
| regex_v8                 | 22.6 ms                                                                | 22.3 ms: 1.01x faster                                                     |
| json                     | 5.30 ms                                                                | 5.24 ms: 1.01x faster                                                     |
| generators               | 28.3 ms                                                                | 28.0 ms: 1.01x faster                                                     |
| scimark_sor              | 110 ms                                                                 | 109 ms: 1.01x faster                                                      |
| meteor_contest           | 108 ms                                                                 | 108 ms: 1.00x faster                                                      |
| pidigits                 | 202 ms                                                                 | 202 ms: 1.00x faster                                                      |
| gc_traversal             | 4.94 ms                                                                | 4.94 ms: 1.00x slower                                                     |
| create_gc_cycles         | 2.50 ms                                                                | 2.51 ms: 1.00x slower                                                     |
| fannkuch                 | 395 ms                                                                 | 396 ms: 1.00x slower                                                      |
| sqlglot_v2_transpile     | 1.49 ms                                                                | 1.50 ms: 1.00x slower                                                     |
| python_startup           | 13.0 ms                                                                | 13.0 ms: 1.00x slower                                                     |
| python_startup_no_site   | 8.09 ms                                                                | 8.12 ms: 1.00x slower                                                     |
| bench_thread_pool        | 845 us                                                                 | 848 us: 1.00x slower                                                      |
| json_loads               | 28.2 us                                                                | 28.3 us: 1.00x slower                                                     |
| docutils                 | 2.57 sec                                                               | 2.58 sec: 1.00x slower                                                    |
| dulwich_log              | 57.8 ms                                                                | 58.2 ms: 1.01x slower                                                     |
| bpe_tokeniser            | 4.32 sec                                                               | 4.35 sec: 1.01x slower                                                    |
| 2to3                     | 243 ms                                                                 | 245 ms: 1.01x slower                                                      |
| sqlalchemy_declarative   | 127 ms                                                                 | 128 ms: 1.01x slower                                                      |
| xml_etree_iterparse      | 102 ms                                                                 | 103 ms: 1.01x slower                                                      |
| xml_etree_parse          | 161 ms                                                                 | 162 ms: 1.01x slower                                                      |
| coverage                 | 81.3 ms                                                                | 82.1 ms: 1.01x slower                                                     |
| hexiom                   | 5.80 ms                                                                | 5.86 ms: 1.01x slower                                                     |
| tomli_loads              | 1.82 sec                                                               | 1.84 sec: 1.01x slower                                                    |
| chaos                    | 54.0 ms                                                                | 54.6 ms: 1.01x slower                                                     |
| async_generators         | 381 ms                                                                 | 386 ms: 1.01x slower                                                      |
| sympy_sum                | 144 ms                                                                 | 146 ms: 1.01x slower                                                      |
| nqueens                  | 77.8 ms                                                                | 78.8 ms: 1.01x slower                                                     |
| async_tree_none_tg       | 244 ms                                                                 | 247 ms: 1.01x slower                                                      |
| mdp                      | 1.20 sec                                                               | 1.21 sec: 1.01x slower                                                    |
| sqlalchemy_imperative    | 16.3 ms                                                                | 16.5 ms: 1.01x slower                                                     |
| sympy_integrate          | 18.3 ms                                                                | 18.6 ms: 1.01x slower                                                     |
| async_tree_io            | 596 ms                                                                 | 605 ms: 1.01x slower                                                      |
| django_template          | 31.4 ms                                                                | 31.9 ms: 1.02x slower                                                     |
| sqlglot_v2_optimize      | 52.6 ms                                                                | 53.4 ms: 1.02x slower                                                     |
| sympy_expand             | 448 ms                                                                 | 455 ms: 1.02x slower                                                      |
| many_optionals           | 906 us                                                                 | 921 us: 1.02x slower                                                      |
| go                       | 106 ms                                                                 | 108 ms: 1.02x slower                                                      |
| async_tree_none          | 252 ms                                                                 | 257 ms: 1.02x slower                                                      |
| sqlglot_v2_normalize     | 104 ms                                                                 | 106 ms: 1.02x slower                                                      |
| sympy_str                | 260 ms                                                                 | 265 ms: 1.02x slower                                                      |
| deepcopy_reduce          | 2.53 us                                                                | 2.57 us: 1.02x slower                                                     |
| subparsers               | 20.2 ms                                                                | 20.6 ms: 1.02x slower                                                     |
| async_tree_memoization   | 303 ms                                                                 | 309 ms: 1.02x slower                                                      |
| raytrace                 | 247 ms                                                                 | 252 ms: 1.02x slower                                                      |
| deepcopy                 | 241 us                                                                 | 247 us: 1.02x slower                                                      |
| regex_dna                | 187 ms                                                                 | 191 ms: 1.02x slower                                                      |
| richards_super           | 46.0 ms                                                                | 47.0 ms: 1.02x slower                                                     |
| regex_compile            | 123 ms                                                                 | 126 ms: 1.02x slower                                                      |
| genshi_text              | 20.5 ms                                                                | 21.0 ms: 1.02x slower                                                     |
| deltablue                | 2.93 ms                                                                | 3.01 ms: 1.02x slower                                                     |
| pprint_safe_repr         | 740 ms                                                                 | 758 ms: 1.02x slower                                                      |
| xml_etree_process        | 59.3 ms                                                                | 60.7 ms: 1.02x slower                                                     |
| xml_etree_generate       | 85.7 ms                                                                | 87.9 ms: 1.03x slower                                                     |
| html5lib                 | 57.1 ms                                                                | 58.5 ms: 1.03x slower                                                     |
| scimark_lu               | 110 ms                                                                 | 113 ms: 1.03x slower                                                      |
| pickle_pure_python       | 300 us                                                                 | 309 us: 1.03x slower                                                      |
| richards                 | 39.8 ms                                                                | 41.1 ms: 1.03x slower                                                     |
| logging_format           | 5.92 us                                                                | 6.11 us: 1.03x slower                                                     |
| logging_simple           | 5.35 us                                                                | 5.53 us: 1.03x slower                                                     |
| pprint_pformat           | 1.50 sec                                                               | 1.56 sec: 1.03x slower                                                    |
| unpickle_pure_python     | 212 us                                                                 | 220 us: 1.04x slower                                                      |
| typing_runtime_protocols | 151 us                                                                 | 157 us: 1.04x slower                                                      |
| logging_silent           | 84.7 ns                                                                | 88.7 ns: 1.05x slower                                                     |
| deepcopy_memo            | 27.7 us                                                                | 29.1 us: 1.05x slower                                                     |
| spectral_norm            | 88.2 ms                                                                | 93.5 ms: 1.06x slower                                                     |
| coroutines               | 21.7 ms                                                                | 23.2 ms: 1.07x slower                                                     |
| Geometric mean           | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (22): k_core, regex_effbot, shortest_path, telco, pyflate, scimark_fft, pathlib, asyncio_websockets, mako, sqlite_synth, float, crypto_pyaes, sqlglot_v2_parse, bench_mp_pool, genshi_xml, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, sphinx, connected_components, pylint, async_tree_memoization_tg, async_tree_io_tg

- Geometric mean (including insignificant results): 1.009x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x