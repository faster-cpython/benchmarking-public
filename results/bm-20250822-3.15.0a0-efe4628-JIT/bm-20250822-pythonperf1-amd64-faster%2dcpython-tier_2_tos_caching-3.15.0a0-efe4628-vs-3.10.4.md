# Results vs. 3.10.4

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: windows-amd64
- commit hash: efe4628
- commit date: 2025-08-22
- overall geometric mean: 1.324x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                                               |
| docutils       | 1.92 sec                                                    | 1.66 sec: 1.15x faster                                                             |
| html5lib       | 51.0 ms                                                     | 38.8 ms: 1.32x faster                                                              |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|-------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 392 ms: 2.83x faster                                                               |
| async_tree_memoization  | 526 ms                                                      | 206 ms: 2.56x faster                                                               |
| async_tree_none         | 435 ms                                                      | 175 ms: 2.48x faster                                                               |
| async_tree_cpu_io_mixed | 638 ms                                                      | 332 ms: 1.92x faster                                                               |
| Geometric mean          | (ref)                                                       | 2.42x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 43.6 ms: 1.64x faster                                                              |
| float          | 61.7 ms                                                     | 45.1 ms: 1.37x faster                                                              |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                               |
| Geometric mean | (ref)                                                       | 1.31x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.6 ms: 1.33x faster                                                              |
| regex_dna      | 136 ms                                                      | 120 ms: 1.14x faster                                                               |
| regex_v8       | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                                              |
| regex_effbot   | 1.66 ms                                                     | 1.52 ms: 1.09x faster                                                              |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 106 us: 1.72x faster                                                               |
| json_dumps           | 9.16 ms                                                     | 5.50 ms: 1.67x faster                                                              |
| tomli_loads          | 1.67 sec                                                    | 1.12 sec: 1.49x faster                                                             |
| pickle_pure_python   | 270 us                                                      | 206 us: 1.31x faster                                                               |
| xml_etree_process    | 44.5 ms                                                     | 35.5 ms: 1.25x faster                                                              |
| xml_etree_parse      | 96.8 ms                                                     | 88.4 ms: 1.10x faster                                                              |
| xml_etree_generate   | 55.5 ms                                                     | 51.0 ms: 1.09x faster                                                              |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                                              |
| Geometric mean       | (ref)                                                       | 1.27x faster                                                                       |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                              |
| python_startup         | 20.6 ms                                                     | 26.5 ms: 1.28x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.43 ms: 1.66x faster                                                              |
| genshi_text     | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                              |
| django_template | 28.9 ms                                                     | 24.3 ms: 1.19x faster                                                              |
| genshi_xml      | 41.0 ms                                                     | 34.8 ms: 1.18x faster                                                              |
| Geometric mean  | (ref)                                                       | 1.31x faster                                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 106 us: 3.18x faster                                                               |
| async_tree_io            | 1.11 sec                                                    | 392 ms: 2.83x faster                                                               |
| pathlib                  | 75.7 ms                                                     | 29.5 ms: 2.56x faster                                                              |
| async_tree_memoization   | 526 ms                                                      | 206 ms: 2.56x faster                                                               |
| async_tree_none          | 435 ms                                                      | 175 ms: 2.48x faster                                                               |
| mdp                      | 1.78 sec                                                    | 810 ms: 2.20x faster                                                               |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 332 ms: 1.92x faster                                                               |
| deltablue                | 4.19 ms                                                     | 2.25 ms: 1.86x faster                                                              |
| go                       | 139 ms                                                      | 78.4 ms: 1.77x faster                                                              |
| pylint                   | 350 ms                                                      | 199 ms: 1.76x faster                                                               |
| unpickle_pure_python     | 183 us                                                      | 106 us: 1.72x faster                                                               |
| richards_super           | 52.2 ms                                                     | 30.9 ms: 1.69x faster                                                              |
| logging_silent           | 94.6 ns                                                     | 56.7 ns: 1.67x faster                                                              |
| json_dumps               | 9.16 ms                                                     | 5.50 ms: 1.67x faster                                                              |
| mako                     | 9.03 ms                                                     | 5.43 ms: 1.66x faster                                                              |
| nbody                    | 71.3 ms                                                     | 43.6 ms: 1.64x faster                                                              |
| generators               | 32.4 ms                                                     | 20.2 ms: 1.60x faster                                                              |
| pyflate                  | 409 ms                                                      | 260 ms: 1.57x faster                                                               |
| comprehensions           | 16.5 us                                                     | 10.6 us: 1.55x faster                                                              |
| raytrace                 | 273 ms                                                      | 176 ms: 1.55x faster                                                               |
| richards                 | 42.4 ms                                                     | 27.4 ms: 1.55x faster                                                              |
| deepcopy_memo            | 28.8 us                                                     | 18.7 us: 1.54x faster                                                              |
| chaos                    | 61.7 ms                                                     | 40.8 ms: 1.51x faster                                                              |
| tomli_loads              | 1.67 sec                                                    | 1.12 sec: 1.49x faster                                                             |
| deepcopy                 | 255 us                                                      | 175 us: 1.46x faster                                                               |
| pprint_pformat           | 1.22 sec                                                    | 845 ms: 1.44x faster                                                               |
| scimark_lu               | 85.8 ms                                                     | 60.1 ms: 1.43x faster                                                              |
| hexiom                   | 5.74 ms                                                     | 4.07 ms: 1.41x faster                                                              |
| pprint_safe_repr         | 592 ms                                                      | 421 ms: 1.41x faster                                                               |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.4 ms: 1.38x faster                                                              |
| crypto_pyaes             | 62.5 ms                                                     | 45.4 ms: 1.38x faster                                                              |
| float                    | 61.7 ms                                                     | 45.1 ms: 1.37x faster                                                              |
| scimark_sor              | 106 ms                                                      | 79.3 ms: 1.34x faster                                                              |
| regex_compile            | 106 ms                                                      | 79.6 ms: 1.33x faster                                                              |
| html5lib                 | 51.0 ms                                                     | 38.8 ms: 1.32x faster                                                              |
| pickle_pure_python       | 270 us                                                      | 206 us: 1.31x faster                                                               |
| scimark_fft              | 187 ms                                                      | 146 ms: 1.29x faster                                                               |
| genshi_text              | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                              |
| thrift                   | 617 us                                                      | 493 us: 1.25x faster                                                               |
| xml_etree_process        | 44.5 ms                                                     | 35.5 ms: 1.25x faster                                                              |
| sqlite_synth             | 1.91 us                                                     | 1.54 us: 1.24x faster                                                              |
| dulwich_log              | 50.5 ms                                                     | 40.6 ms: 1.24x faster                                                              |
| fannkuch                 | 256 ms                                                      | 206 ms: 1.24x faster                                                               |
| sympy_sum                | 107 ms                                                      | 87.9 ms: 1.22x faster                                                              |
| sympy_integrate          | 15.3 ms                                                     | 12.8 ms: 1.20x faster                                                              |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.28 ms: 1.20x faster                                                              |
| django_template          | 28.9 ms                                                     | 24.3 ms: 1.19x faster                                                              |
| genshi_xml               | 41.0 ms                                                     | 34.8 ms: 1.18x faster                                                              |
| deepcopy_reduce          | 2.20 us                                                     | 1.89 us: 1.17x faster                                                              |
| docutils                 | 1.92 sec                                                    | 1.66 sec: 1.15x faster                                                             |
| spectral_norm            | 77.3 ms                                                     | 67.5 ms: 1.14x faster                                                              |
| regex_dna                | 136 ms                                                      | 120 ms: 1.14x faster                                                               |
| sympy_str                | 194 ms                                                      | 171 ms: 1.14x faster                                                               |
| nqueens                  | 66.6 ms                                                     | 58.9 ms: 1.13x faster                                                              |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                                               |
| regex_v8                 | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                                              |
| xml_etree_parse          | 96.8 ms                                                     | 88.4 ms: 1.10x faster                                                              |
| regex_effbot             | 1.66 ms                                                     | 1.52 ms: 1.09x faster                                                              |
| coroutines               | 16.0 ms                                                     | 14.6 ms: 1.09x faster                                                              |
| xml_etree_generate       | 55.5 ms                                                     | 51.0 ms: 1.09x faster                                                              |
| json                     | 3.14 ms                                                     | 2.94 ms: 1.06x faster                                                              |
| sympy_expand             | 314 ms                                                      | 296 ms: 1.06x faster                                                               |
| logging_format           | 6.76 us                                                     | 6.51 us: 1.04x faster                                                              |
| logging_simple           | 6.22 us                                                     | 5.99 us: 1.04x faster                                                              |
| meteor_contest           | 75.9 ms                                                     | 73.4 ms: 1.03x faster                                                              |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                               |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                                              |
| telco                    | 3.94 ms                                                     | 4.01 ms: 1.02x slower                                                              |
| async_generators         | 222 ms                                                      | 243 ms: 1.10x slower                                                               |
| python_startup_no_site   | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                              |
| python_startup           | 20.6 ms                                                     | 26.5 ms: 1.28x slower                                                              |
| coverage                 | 39.0 ms                                                     | 50.5 ms: 1.29x slower                                                              |
| gc_traversal             | 1.41 ms                                                     | 2.11 ms: 1.49x slower                                                              |
| create_gc_cycles         | 800 us                                                      | 1.30 ms: 1.62x slower                                                              |
| Geometric mean           | (ref)                                                       | 1.32x faster                                                                       |

Benchmark hidden because not significant (1): xml_etree_iterparse
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, pycparser, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250822-3.15.0a0-efe4628-JIT/bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.324x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown