# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_targets
- machine: windows-amd64
- commit hash: 997a858
- commit date: 2025-07-08
- overall geometric mean: 1.476x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.37x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 216 ms: 1.23x faster                                                          |
| docutils       | 1.95 sec                                                        | 1.64 sec: 1.19x faster                                                        |
| html5lib       | 52.1 ms                                                         | 38.0 ms: 1.37x faster                                                         |
| Geometric mean | (ref)                                                           | 1.26x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|-------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 328 ms: 2.81x faster                                                          |
| async_tree_io           | 940 ms                                                          | 392 ms: 2.40x faster                                                          |
| async_tree_none         | 394 ms                                                          | 165 ms: 2.38x faster                                                          |
| async_tree_memoization  | 467 ms                                                          | 202 ms: 2.31x faster                                                          |
| Geometric mean          | (ref)                                                           | 2.47x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 149 ms: 3.37x faster                                                          |
| float          | 69.6 ms                                                         | 43.3 ms: 1.61x faster                                                         |
| nbody          | 79.1 ms                                                         | 55.4 ms: 1.43x faster                                                         |
| Geometric mean | (ref)                                                           | 1.98x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 80.2 ms: 1.45x faster                                                         |
| regex_v8       | 15.8 ms                                                         | 14.4 ms: 1.10x faster                                                         |
| regex_dna      | 131 ms                                                          | 122 ms: 1.07x faster                                                          |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                  |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.12 sec: 1.70x faster                                                        |
| unpickle_pure_python | 189 us                                                          | 112 us: 1.69x faster                                                          |
| json_dumps           | 9.82 ms                                                         | 6.17 ms: 1.59x faster                                                         |
| json_loads           | 22.4 us                                                         | 14.4 us: 1.55x faster                                                         |
| xml_etree_parse      | 120 ms                                                          | 88.5 ms: 1.36x faster                                                         |
| pickle_pure_python   | 280 us                                                          | 207 us: 1.35x faster                                                          |
| xml_etree_process    | 48.1 ms                                                         | 36.2 ms: 1.33x faster                                                         |
| xml_etree_generate   | 61.6 ms                                                         | 51.1 ms: 1.21x faster                                                         |
| xml_etree_iterparse  | 70.8 ms                                                         | 65.4 ms: 1.08x faster                                                         |
| Geometric mean       | (ref)                                                           | 1.41x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.6 ms: 1.08x slower                                                         |
| python_startup         | 22.9 ms                                                         | 25.7 ms: 1.12x slower                                                         |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.49 ms: 1.66x faster                                                         |
| django_template | 36.0 ms                                                         | 23.7 ms: 1.52x faster                                                         |
| genshi_text     | 21.0 ms                                                         | 15.1 ms: 1.39x faster                                                         |
| genshi_xml      | 46.6 ms                                                         | 33.9 ms: 1.38x faster                                                         |
| Geometric mean  | (ref)                                                           | 1.48x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|--------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 104 us: 3.82x faster                                                          |
| pidigits                 | 502 ms                                                          | 149 ms: 3.37x faster                                                          |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 328 ms: 2.81x faster                                                          |
| pathlib                  | 81.2 ms                                                         | 30.2 ms: 2.69x faster                                                         |
| async_tree_io            | 940 ms                                                          | 392 ms: 2.40x faster                                                          |
| async_tree_none          | 394 ms                                                          | 165 ms: 2.38x faster                                                          |
| async_tree_memoization   | 467 ms                                                          | 202 ms: 2.31x faster                                                          |
| mdp                      | 1.83 sec                                                        | 794 ms: 2.30x faster                                                          |
| go                       | 146 ms                                                          | 75.3 ms: 1.93x faster                                                         |
| deltablue                | 4.04 ms                                                         | 2.16 ms: 1.87x faster                                                         |
| pylint                   | 384 ms                                                          | 205 ms: 1.87x faster                                                          |
| chaos                    | 74.4 ms                                                         | 39.9 ms: 1.86x faster                                                         |
| deepcopy                 | 310 us                                                          | 168 us: 1.85x faster                                                          |
| thrift                   | 902 us                                                          | 495 us: 1.82x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 45.4 ms: 1.79x faster                                                         |
| logging_silent           | 97.9 ns                                                         | 54.9 ns: 1.78x faster                                                         |
| comprehensions           | 17.7 us                                                         | 10.3 us: 1.71x faster                                                         |
| deepcopy_memo            | 29.6 us                                                         | 17.3 us: 1.71x faster                                                         |
| tomli_loads              | 1.91 sec                                                        | 1.12 sec: 1.70x faster                                                        |
| unpickle_pure_python     | 189 us                                                          | 112 us: 1.69x faster                                                          |
| pyflate                  | 422 ms                                                          | 253 ms: 1.67x faster                                                          |
| raytrace                 | 303 ms                                                          | 182 ms: 1.66x faster                                                          |
| mako                     | 9.10 ms                                                         | 5.49 ms: 1.66x faster                                                         |
| generators               | 31.6 ms                                                         | 19.6 ms: 1.61x faster                                                         |
| float                    | 69.6 ms                                                         | 43.3 ms: 1.61x faster                                                         |
| richards_super           | 49.9 ms                                                         | 31.0 ms: 1.61x faster                                                         |
| json                     | 4.76 ms                                                         | 2.96 ms: 1.61x faster                                                         |
| json_dumps               | 9.82 ms                                                         | 6.17 ms: 1.59x faster                                                         |
| json_loads               | 22.4 us                                                         | 14.4 us: 1.55x faster                                                         |
| django_template          | 36.0 ms                                                         | 23.7 ms: 1.52x faster                                                         |
| hexiom                   | 6.13 ms                                                         | 4.04 ms: 1.52x faster                                                         |
| scimark_sor              | 115 ms                                                          | 76.0 ms: 1.52x faster                                                         |
| pprint_pformat           | 1.37 sec                                                        | 908 ms: 1.51x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 41.1 ms: 1.51x faster                                                         |
| richards                 | 40.3 ms                                                         | 27.1 ms: 1.49x faster                                                         |
| nqueens                  | 87.1 ms                                                         | 59.2 ms: 1.47x faster                                                         |
| pycparser                | 1.04 sec                                                        | 711 ms: 1.46x faster                                                          |
| sqlite_synth             | 2.29 us                                                         | 1.57 us: 1.46x faster                                                         |
| regex_compile            | 117 ms                                                          | 80.2 ms: 1.45x faster                                                         |
| scimark_lu               | 89.8 ms                                                         | 61.7 ms: 1.45x faster                                                         |
| pprint_safe_repr         | 658 ms                                                          | 454 ms: 1.45x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 1.86 us: 1.44x faster                                                         |
| dulwich_log              | 58.5 ms                                                         | 40.7 ms: 1.44x faster                                                         |
| nbody                    | 79.1 ms                                                         | 55.4 ms: 1.43x faster                                                         |
| fannkuch                 | 317 ms                                                          | 223 ms: 1.42x faster                                                          |
| genshi_text              | 21.0 ms                                                         | 15.1 ms: 1.39x faster                                                         |
| sympy_sum                | 122 ms                                                          | 88.8 ms: 1.38x faster                                                         |
| scimark_fft              | 216 ms                                                          | 157 ms: 1.38x faster                                                          |
| genshi_xml               | 46.6 ms                                                         | 33.9 ms: 1.38x faster                                                         |
| html5lib                 | 52.1 ms                                                         | 38.0 ms: 1.37x faster                                                         |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.37 ms: 1.37x faster                                                         |
| xml_etree_parse          | 120 ms                                                          | 88.5 ms: 1.36x faster                                                         |
| pickle_pure_python       | 280 us                                                          | 207 us: 1.35x faster                                                          |
| xml_etree_process        | 48.1 ms                                                         | 36.2 ms: 1.33x faster                                                         |
| sympy_str                | 229 ms                                                          | 173 ms: 1.33x faster                                                          |
| sympy_expand             | 391 ms                                                          | 297 ms: 1.32x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 12.8 ms: 1.30x faster                                                         |
| logging_format           | 7.91 us                                                         | 6.42 us: 1.23x faster                                                         |
| 2to3                     | 265 ms                                                          | 216 ms: 1.23x faster                                                          |
| coroutines               | 17.9 ms                                                         | 14.7 ms: 1.22x faster                                                         |
| spectral_norm            | 80.2 ms                                                         | 66.1 ms: 1.21x faster                                                         |
| xml_etree_generate       | 61.6 ms                                                         | 51.1 ms: 1.21x faster                                                         |
| logging_simple           | 7.29 us                                                         | 6.04 us: 1.21x faster                                                         |
| docutils                 | 1.95 sec                                                        | 1.64 sec: 1.19x faster                                                        |
| meteor_contest           | 80.0 ms                                                         | 71.2 ms: 1.12x faster                                                         |
| telco                    | 4.83 ms                                                         | 4.38 ms: 1.10x faster                                                         |
| regex_v8                 | 15.8 ms                                                         | 14.4 ms: 1.10x faster                                                         |
| xml_etree_iterparse      | 70.8 ms                                                         | 65.4 ms: 1.08x faster                                                         |
| regex_dna                | 131 ms                                                          | 122 ms: 1.07x faster                                                          |
| async_generators         | 241 ms                                                          | 243 ms: 1.01x slower                                                          |
| coverage                 | 46.6 ms                                                         | 49.8 ms: 1.07x slower                                                         |
| python_startup_no_site   | 18.1 ms                                                         | 19.6 ms: 1.08x slower                                                         |
| python_startup           | 22.9 ms                                                         | 25.7 ms: 1.12x slower                                                         |
| gc_traversal             | 1.28 ms                                                         | 2.14 ms: 1.67x slower                                                         |
| create_gc_cycles         | 694 us                                                          | 1.34 ms: 1.93x slower                                                         |
| Geometric mean           | (ref)                                                           | 1.47x faster                                                                  |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250708-3.15.0a0-997a858-JIT/bm-20250708-pythonperf1_win32-amd64-brandtbucher-jit_targets-3.15.0a0-997a858.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.476x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.41x
- 95% likely to have a speedup of 1.40x
- 99% likely to have a speedup of 1.37x

# Memory
- memory change: unknown