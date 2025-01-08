# Results vs. 3.10.4

- fork: kumaraditya303
- ref: fast_state
- machine: windows-x86
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.163x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 244 ms: 1.09x faster                                                          |
| docutils       | 1.95 sec                                                        | 1.80 sec: 1.08x faster                                                        |
| html5lib       | 52.1 ms                                                         | 43.1 ms: 1.21x faster                                                         |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io           | 940 ms                                                          | 421 ms: 2.23x faster                                                          |
| async_tree_cpu_io_mixed | 922 ms                                                          | 434 ms: 2.12x faster                                                          |
| async_tree_none         | 394 ms                                                          | 193 ms: 2.04x faster                                                          |
| async_tree_memoization  | 467 ms                                                          | 235 ms: 1.98x faster                                                          |
| Geometric mean          | (ref)                                                           | 2.09x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 197 ms: 2.55x faster                                                          |
| float          | 69.6 ms                                                         | 56.5 ms: 1.23x faster                                                         |
| nbody          | 79.1 ms                                                         | 84.4 ms: 1.07x slower                                                         |
| Geometric mean | (ref)                                                           | 1.43x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 99.6 ms: 1.17x faster                                                         |
| regex_dna      | 131 ms                                                          | 117 ms: 1.11x faster                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.57 ms: 1.06x faster                                                         |
| regex_v8       | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.58 sec: 1.21x faster                                                        |
| json_dumps           | 9.82 ms                                                         | 8.60 ms: 1.14x faster                                                         |
| unpickle_pure_python | 189 us                                                          | 169 us: 1.12x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.12x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 65.5 ms: 1.08x faster                                                         |
| json_loads           | 22.4 us                                                         | 20.8 us: 1.08x faster                                                         |
| pickle_pure_python   | 280 us                                                          | 268 us: 1.04x faster                                                          |
| xml_etree_process    | 48.1 ms                                                         | 47.9 ms: 1.00x faster                                                         |
| xml_etree_generate   | 61.6 ms                                                         | 66.2 ms: 1.07x slower                                                         |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.2 ms: 1.06x slower                                                         |
| python_startup         | 22.9 ms                                                         | 25.5 ms: 1.11x slower                                                         |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.55 ms: 1.21x faster                                                         |
| django_template | 36.0 ms                                                         | 33.3 ms: 1.08x faster                                                         |
| genshi_xml      | 46.6 ms                                                         | 45.3 ms: 1.03x faster                                                         |
| genshi_text     | 21.0 ms                                                         | 21.2 ms: 1.01x slower                                                         |
| Geometric mean  | (ref)                                                           | 1.07x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|--------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 143 us: 2.77x faster                                                          |
| pidigits                 | 502 ms                                                          | 197 ms: 2.55x faster                                                          |
| async_tree_io            | 940 ms                                                          | 421 ms: 2.23x faster                                                          |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 434 ms: 2.12x faster                                                          |
| async_tree_none          | 394 ms                                                          | 193 ms: 2.04x faster                                                          |
| async_tree_memoization   | 467 ms                                                          | 235 ms: 1.98x faster                                                          |
| pylint                   | 384 ms                                                          | 218 ms: 1.76x faster                                                          |
| deltablue                | 4.04 ms                                                         | 2.57 ms: 1.57x faster                                                         |
| go                       | 146 ms                                                          | 95.0 ms: 1.53x faster                                                         |
| logging_silent           | 97.9 ns                                                         | 69.2 ns: 1.41x faster                                                         |
| chaos                    | 74.4 ms                                                         | 53.8 ms: 1.38x faster                                                         |
| scimark_lu               | 89.8 ms                                                         | 66.5 ms: 1.35x faster                                                         |
| crypto_pyaes             | 81.3 ms                                                         | 60.5 ms: 1.34x faster                                                         |
| deepcopy                 | 310 us                                                          | 233 us: 1.33x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 22.3 us: 1.33x faster                                                         |
| sqlglot_parse            | 1.33 ms                                                         | 1.02 ms: 1.31x faster                                                         |
| pycparser                | 1.04 sec                                                        | 809 ms: 1.29x faster                                                          |
| comprehensions           | 17.7 us                                                         | 13.9 us: 1.28x faster                                                         |
| hexiom                   | 6.13 ms                                                         | 4.85 ms: 1.26x faster                                                         |
| generators               | 31.6 ms                                                         | 25.0 ms: 1.26x faster                                                         |
| pyflate                  | 422 ms                                                          | 335 ms: 1.26x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.27 ms: 1.25x faster                                                         |
| thrift                   | 902 us                                                          | 728 us: 1.24x faster                                                          |
| float                    | 69.6 ms                                                         | 56.5 ms: 1.23x faster                                                         |
| tomli_loads              | 1.91 sec                                                        | 1.58 sec: 1.21x faster                                                        |
| html5lib                 | 52.1 ms                                                         | 43.1 ms: 1.21x faster                                                         |
| raytrace                 | 303 ms                                                          | 250 ms: 1.21x faster                                                          |
| mako                     | 9.10 ms                                                         | 7.55 ms: 1.21x faster                                                         |
| scimark_sor              | 115 ms                                                          | 96.5 ms: 1.19x faster                                                         |
| sqlite_synth             | 2.29 us                                                         | 1.93 us: 1.19x faster                                                         |
| richards_super           | 49.9 ms                                                         | 42.1 ms: 1.18x faster                                                         |
| scimark_monte_carlo      | 61.9 ms                                                         | 52.4 ms: 1.18x faster                                                         |
| regex_compile            | 117 ms                                                          | 99.6 ms: 1.17x faster                                                         |
| dulwich_log              | 58.5 ms                                                         | 50.1 ms: 1.17x faster                                                         |
| nqueens                  | 87.1 ms                                                         | 74.8 ms: 1.16x faster                                                         |
| sympy_sum                | 122 ms                                                          | 106 ms: 1.16x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 70.1 ms: 1.14x faster                                                         |
| json_dumps               | 9.82 ms                                                         | 8.60 ms: 1.14x faster                                                         |
| richards                 | 40.3 ms                                                         | 35.6 ms: 1.13x faster                                                         |
| unpickle_pure_python     | 189 us                                                          | 169 us: 1.12x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                                          |
| json                     | 4.76 ms                                                         | 4.25 ms: 1.12x faster                                                         |
| bench_thread_pool        | 1.12 ms                                                         | 1.00 ms: 1.12x faster                                                         |
| regex_dna                | 131 ms                                                          | 117 ms: 1.11x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.2 ms: 1.09x faster                                                         |
| coroutines               | 17.9 ms                                                         | 16.4 ms: 1.09x faster                                                         |
| 2to3                     | 265 ms                                                          | 244 ms: 1.09x faster                                                          |
| docutils                 | 1.95 sec                                                        | 1.80 sec: 1.08x faster                                                        |
| django_template          | 36.0 ms                                                         | 33.3 ms: 1.08x faster                                                         |
| xml_etree_iterparse      | 70.8 ms                                                         | 65.5 ms: 1.08x faster                                                         |
| fannkuch                 | 317 ms                                                          | 294 ms: 1.08x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.27 sec: 1.08x faster                                                        |
| json_loads               | 22.4 us                                                         | 20.8 us: 1.08x faster                                                         |
| deepcopy_reduce          | 2.68 us                                                         | 2.50 us: 1.08x faster                                                         |
| pprint_safe_repr         | 658 ms                                                          | 617 ms: 1.07x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.04 ms: 1.06x faster                                                         |
| sympy_str                | 229 ms                                                          | 216 ms: 1.06x faster                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.57 ms: 1.06x faster                                                         |
| pickle_pure_python       | 280 us                                                          | 268 us: 1.04x faster                                                          |
| sympy_expand             | 391 ms                                                          | 377 ms: 1.04x faster                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 43.4 ms: 1.03x faster                                                         |
| genshi_xml               | 46.6 ms                                                         | 45.3 ms: 1.03x faster                                                         |
| sqlglot_normalize        | 230 ms                                                          | 229 ms: 1.01x faster                                                          |
| xml_etree_process        | 48.1 ms                                                         | 47.9 ms: 1.00x faster                                                         |
| genshi_text              | 21.0 ms                                                         | 21.2 ms: 1.01x slower                                                         |
| meteor_contest           | 80.0 ms                                                         | 81.1 ms: 1.01x slower                                                         |
| regex_v8                 | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                         |
| pathlib                  | 81.2 ms                                                         | 83.9 ms: 1.03x slower                                                         |
| scimark_fft              | 216 ms                                                          | 225 ms: 1.04x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 19.2 ms: 1.06x slower                                                         |
| logging_simple           | 7.29 us                                                         | 7.76 us: 1.06x slower                                                         |
| logging_format           | 7.91 us                                                         | 8.42 us: 1.06x slower                                                         |
| nbody                    | 79.1 ms                                                         | 84.4 ms: 1.07x slower                                                         |
| xml_etree_generate       | 61.6 ms                                                         | 66.2 ms: 1.07x slower                                                         |
| coverage                 | 46.6 ms                                                         | 51.1 ms: 1.10x slower                                                         |
| python_startup           | 22.9 ms                                                         | 25.5 ms: 1.11x slower                                                         |
| mypy2                    | 590 ms                                                          | 686 ms: 1.16x slower                                                          |
| async_generators         | 241 ms                                                          | 294 ms: 1.22x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 87.2 ms: 1.31x slower                                                         |
| gc_traversal             | 1.28 ms                                                         | 1.78 ms: 1.39x slower                                                         |
| telco                    | 4.83 ms                                                         | 6.90 ms: 1.43x slower                                                         |
| create_gc_cycles         | 694 us                                                          | 1.05 ms: 1.52x slower                                                         |
| Geometric mean           | (ref)                                                           | 1.16x faster                                                                  |

Benchmark hidden because not significant (1): mdp
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250107-3.14.0a3+-7de6e22/bm-20250107-pythonperf1_win32-x86-kumaraditya303-fast_state-3.14.0a3+-7de6e22.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.163x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown