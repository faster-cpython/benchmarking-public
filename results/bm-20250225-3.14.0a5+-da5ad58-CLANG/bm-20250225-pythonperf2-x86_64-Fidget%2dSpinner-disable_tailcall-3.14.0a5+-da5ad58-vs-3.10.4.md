# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: disable_tailcall
- machine: linux-x86_64
- commit hash: da5ad58
- commit date: 2025-02-25
- overall geometric mean: 1.186x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 307 ms: 1.14x faster                                                               |
| docutils       | 3.41 sec                                                     | 2.98 sec: 1.14x faster                                                             |
| html5lib       | 94.6 ms                                                      | 73.0 ms: 1.30x faster                                                              |
| Geometric mean | (ref)                                                        | 1.19x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 713 ms: 2.24x faster                                                               |
| async_tree_none         | 692 ms                                                       | 319 ms: 2.17x faster                                                               |
| async_tree_memoization  | 819 ms                                                       | 390 ms: 2.10x faster                                                               |
| async_tree_cpu_io_mixed | 936 ms                                                       | 586 ms: 1.60x faster                                                               |
| Geometric mean          | (ref)                                                        | 2.01x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 84.7 ms: 1.31x faster                                                              |
| nbody          | 134 ms                                                       | 123 ms: 1.09x faster                                                               |
| pidigits       | 271 ms                                                       | 293 ms: 1.08x slower                                                               |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_dna      | 261 ms                                                       | 226 ms: 1.16x faster                                                               |
| regex_compile  | 190 ms                                                       | 165 ms: 1.15x faster                                                               |
| regex_v8       | 27.2 ms                                                      | 26.4 ms: 1.03x faster                                                              |
| regex_effbot   | 3.09 ms                                                      | 3.01 ms: 1.02x faster                                                              |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| json_dumps           | 14.5 ms                                                      | 12.3 ms: 1.19x faster                                                              |
| json_loads           | 30.3 us                                                      | 26.7 us: 1.13x faster                                                              |
| unpickle_pure_python | 312 us                                                       | 275 us: 1.13x faster                                                               |
| pickle_pure_python   | 455 us                                                       | 404 us: 1.13x faster                                                               |
| xml_etree_process    | 75.9 ms                                                      | 67.8 ms: 1.12x faster                                                              |
| tomli_loads          | 2.92 sec                                                     | 2.75 sec: 1.06x faster                                                             |
| xml_etree_parse      | 160 ms                                                       | 163 ms: 1.02x slower                                                               |
| xml_etree_iterparse  | 110 ms                                                       | 114 ms: 1.03x slower                                                               |
| Geometric mean       | (ref)                                                        | 1.08x faster                                                                       |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.26 ms: 1.26x slower                                                              |
| python_startup         | 11.5 ms                                                      | 16.4 ms: 1.42x slower                                                              |
| Geometric mean         | (ref)                                                        | 1.34x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 42.4 ms: 1.18x faster                                                              |
| mako            | 14.7 ms                                                      | 12.9 ms: 1.14x faster                                                              |
| genshi_text     | 31.4 ms                                                      | 28.5 ms: 1.10x faster                                                              |
| genshi_xml      | 63.3 ms                                                      | 62.7 ms: 1.01x faster                                                              |
| Geometric mean  | (ref)                                                        | 1.11x faster                                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 182 us: 2.94x faster                                                               |
| async_tree_io            | 1.60 sec                                                     | 713 ms: 2.24x faster                                                               |
| async_tree_none          | 692 ms                                                       | 319 ms: 2.17x faster                                                               |
| async_tree_memoization   | 819 ms                                                       | 390 ms: 2.10x faster                                                               |
| deltablue                | 7.50 ms                                                      | 4.36 ms: 1.72x faster                                                              |
| pylint                   | 566 ms                                                       | 336 ms: 1.68x faster                                                               |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 586 ms: 1.60x faster                                                               |
| generators               | 57.3 ms                                                      | 37.0 ms: 1.55x faster                                                              |
| chaos                    | 109 ms                                                       | 72.6 ms: 1.50x faster                                                              |
| go                       | 262 ms                                                       | 175 ms: 1.50x faster                                                               |
| raytrace                 | 489 ms                                                       | 333 ms: 1.47x faster                                                               |
| logging_silent           | 167 ns                                                       | 114 ns: 1.47x faster                                                               |
| deepcopy                 | 468 us                                                       | 320 us: 1.46x faster                                                               |
| pyflate                  | 733 ms                                                       | 517 ms: 1.42x faster                                                               |
| scimark_lu               | 167 ms                                                       | 118 ms: 1.42x faster                                                               |
| spectral_norm            | 139 ms                                                       | 99.0 ms: 1.40x faster                                                              |
| crypto_pyaes             | 119 ms                                                       | 86.4 ms: 1.38x faster                                                              |
| richards_super           | 90.6 ms                                                      | 66.4 ms: 1.36x faster                                                              |
| coroutines               | 30.3 ms                                                      | 22.6 ms: 1.34x faster                                                              |
| sqlglot_parse            | 2.24 ms                                                      | 1.68 ms: 1.33x faster                                                              |
| comprehensions           | 26.7 us                                                      | 20.3 us: 1.31x faster                                                              |
| deepcopy_memo            | 49.8 us                                                      | 37.9 us: 1.31x faster                                                              |
| float                    | 111 ms                                                       | 84.7 ms: 1.31x faster                                                              |
| thrift                   | 1.18 ms                                                      | 899 us: 1.31x faster                                                               |
| scimark_monte_carlo      | 107 ms                                                       | 82.3 ms: 1.31x faster                                                              |
| html5lib                 | 94.6 ms                                                      | 73.0 ms: 1.30x faster                                                              |
| sqlglot_transpile        | 2.68 ms                                                      | 2.07 ms: 1.30x faster                                                              |
| richards                 | 75.1 ms                                                      | 59.9 ms: 1.25x faster                                                              |
| sqlalchemy_declarative   | 190 ms                                                       | 154 ms: 1.23x faster                                                               |
| pathlib                  | 21.4 ms                                                      | 17.4 ms: 1.23x faster                                                              |
| scimark_sor              | 180 ms                                                       | 147 ms: 1.22x faster                                                               |
| pycparser                | 1.67 sec                                                     | 1.37 sec: 1.22x faster                                                             |
| logging_simple           | 8.88 us                                                      | 7.34 us: 1.21x faster                                                              |
| deepcopy_reduce          | 4.01 us                                                      | 3.33 us: 1.20x faster                                                              |
| logging_format           | 9.64 us                                                      | 8.07 us: 1.19x faster                                                              |
| json_dumps               | 14.5 ms                                                      | 12.3 ms: 1.19x faster                                                              |
| django_template          | 50.2 ms                                                      | 42.4 ms: 1.18x faster                                                              |
| sqlalchemy_imperative    | 22.7 ms                                                      | 19.3 ms: 1.17x faster                                                              |
| sympy_sum                | 193 ms                                                       | 164 ms: 1.17x faster                                                               |
| hexiom                   | 9.42 ms                                                      | 8.11 ms: 1.16x faster                                                              |
| regex_dna                | 261 ms                                                       | 226 ms: 1.16x faster                                                               |
| regex_compile            | 190 ms                                                       | 165 ms: 1.15x faster                                                               |
| docutils                 | 3.41 sec                                                     | 2.98 sec: 1.14x faster                                                             |
| mako                     | 14.7 ms                                                      | 12.9 ms: 1.14x faster                                                              |
| sympy_integrate          | 28.2 ms                                                      | 24.7 ms: 1.14x faster                                                              |
| 2to3                     | 350 ms                                                       | 307 ms: 1.14x faster                                                               |
| sympy_str                | 360 ms                                                       | 316 ms: 1.14x faster                                                               |
| dulwich_log              | 81.1 ms                                                      | 71.5 ms: 1.13x faster                                                              |
| json_loads               | 30.3 us                                                      | 26.7 us: 1.13x faster                                                              |
| unpickle_pure_python     | 312 us                                                       | 275 us: 1.13x faster                                                               |
| sympy_expand             | 600 ms                                                       | 532 ms: 1.13x faster                                                               |
| pickle_pure_python       | 455 us                                                       | 404 us: 1.13x faster                                                               |
| xml_etree_process        | 75.9 ms                                                      | 67.8 ms: 1.12x faster                                                              |
| bench_thread_pool        | 1.14 ms                                                      | 1.03 ms: 1.11x faster                                                              |
| genshi_text              | 31.4 ms                                                      | 28.5 ms: 1.10x faster                                                              |
| sqlglot_normalize        | 144 ms                                                       | 131 ms: 1.10x faster                                                               |
| sqlglot_optimize         | 70.1 ms                                                      | 63.9 ms: 1.10x faster                                                              |
| pprint_pformat           | 2.15 sec                                                     | 1.97 sec: 1.09x faster                                                             |
| nbody                    | 134 ms                                                       | 123 ms: 1.09x faster                                                               |
| pprint_safe_repr         | 1.05 sec                                                     | 967 ms: 1.09x faster                                                               |
| json                     | 5.86 ms                                                      | 5.40 ms: 1.09x faster                                                              |
| mdp                      | 3.01 sec                                                     | 2.83 sec: 1.06x faster                                                             |
| tomli_loads              | 2.92 sec                                                     | 2.75 sec: 1.06x faster                                                             |
| nqueens                  | 115 ms                                                       | 110 ms: 1.05x faster                                                               |
| sqlite_synth             | 2.99 us                                                      | 2.88 us: 1.04x faster                                                              |
| scimark_fft              | 361 ms                                                       | 351 ms: 1.03x faster                                                               |
| regex_v8                 | 27.2 ms                                                      | 26.4 ms: 1.03x faster                                                              |
| regex_effbot             | 3.09 ms                                                      | 3.01 ms: 1.02x faster                                                              |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                                               |
| genshi_xml               | 63.3 ms                                                      | 62.7 ms: 1.01x faster                                                              |
| xml_etree_parse          | 160 ms                                                       | 163 ms: 1.02x slower                                                               |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.21 ms: 1.03x slower                                                              |
| fannkuch                 | 483 ms                                                       | 496 ms: 1.03x slower                                                               |
| xml_etree_iterparse      | 110 ms                                                       | 114 ms: 1.03x slower                                                               |
| meteor_contest           | 138 ms                                                       | 143 ms: 1.03x slower                                                               |
| async_generators         | 421 ms                                                       | 445 ms: 1.06x slower                                                               |
| pidigits                 | 271 ms                                                       | 293 ms: 1.08x slower                                                               |
| telco                    | 7.23 ms                                                      | 8.17 ms: 1.13x slower                                                              |
| coverage                 | 63.3 ms                                                      | 79.8 ms: 1.26x slower                                                              |
| python_startup_no_site   | 7.33 ms                                                      | 9.26 ms: 1.26x slower                                                              |
| python_startup           | 11.5 ms                                                      | 16.4 ms: 1.42x slower                                                              |
| gc_traversal             | 3.42 ms                                                      | 5.31 ms: 1.56x slower                                                              |
| create_gc_cycles         | 1.76 ms                                                      | 2.77 ms: 1.57x slower                                                              |
| bench_mp_pool            | 6.37 ms                                                      | 1.09 sec: 170.73x slower                                                           |
| Geometric mean           | (ref)                                                        | 1.12x faster                                                                       |

Benchmark hidden because not significant (1): xml_etree_generate
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250225-3.14.0a5+-da5ad58-CLANG/bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.186x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: 1.35x