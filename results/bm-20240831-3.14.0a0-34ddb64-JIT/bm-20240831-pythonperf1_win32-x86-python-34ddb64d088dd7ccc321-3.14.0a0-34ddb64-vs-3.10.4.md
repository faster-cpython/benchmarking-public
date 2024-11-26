# Results vs. 3.10.4

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: windows-x86
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.217x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 263 ms: 1.01x faster                                                           |
| docutils       | 1.95 sec                                                        | 2.00 sec: 1.03x slower                                                         |
| html5lib       | 52.1 ms                                                         | 47.5 ms: 1.10x faster                                                          |
| tornado_http   | 118 ms                                                          | 108 ms: 1.09x faster                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 473 ms: 1.95x faster                                                           |
| async_tree_none         | 394 ms                                                          | 215 ms: 1.83x faster                                                           |
| async_tree_io           | 940 ms                                                          | 534 ms: 1.76x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 274 ms: 1.71x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.81x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 195 ms: 2.57x faster                                                           |
| nbody          | 79.1 ms                                                         | 47.8 ms: 1.65x faster                                                          |
| float          | 69.6 ms                                                         | 43.9 ms: 1.59x faster                                                          |
| Geometric mean | (ref)                                                           | 1.89x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 102 ms: 1.15x faster                                                           |
| regex_dna      | 131 ms                                                          | 122 ms: 1.07x faster                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.95 ms: 1.17x slower                                                          |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.86 ms: 1.43x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.48 sec: 1.29x faster                                                         |
| pickle_pure_python   | 280 us                                                          | 233 us: 1.20x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 162 us: 1.17x faster                                                           |
| xml_etree_process    | 48.1 ms                                                         | 41.4 ms: 1.16x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 104 ms: 1.15x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 62.5 ms: 1.13x faster                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 54.5 ms: 1.13x faster                                                          |
| json_loads           | 22.4 us                                                         | 20.9 us: 1.07x faster                                                          |
| Geometric mean       | (ref)                                                           | 1.19x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.9 ms: 1.09x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 21.0 ms: 1.16x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.12x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.60 ms: 1.63x faster                                                          |
| django_template | 36.0 ms                                                         | 33.6 ms: 1.07x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 24.9 ms: 1.19x slower                                                          |
| genshi_xml      | 46.6 ms                                                         | 56.4 ms: 1.21x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.05x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 144 us: 2.75x faster                                                           |
| pidigits                 | 502 ms                                                          | 195 ms: 2.57x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 15.0 us: 1.97x faster                                                          |
| deltablue                | 4.04 ms                                                         | 2.06 ms: 1.96x faster                                                          |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 473 ms: 1.95x faster                                                           |
| async_tree_none          | 394 ms                                                          | 215 ms: 1.83x faster                                                           |
| async_tree_io            | 940 ms                                                          | 534 ms: 1.76x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 46.3 ms: 1.73x faster                                                          |
| async_tree_memoization   | 467 ms                                                          | 274 ms: 1.71x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 48.2 ms: 1.69x faster                                                          |
| scimark_sor              | 115 ms                                                          | 69.4 ms: 1.66x faster                                                          |
| nbody                    | 79.1 ms                                                         | 47.8 ms: 1.65x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 59.4 ns: 1.65x faster                                                          |
| mako                     | 9.10 ms                                                         | 5.60 ms: 1.63x faster                                                          |
| float                    | 69.6 ms                                                         | 43.9 ms: 1.59x faster                                                          |
| pyflate                  | 422 ms                                                          | 279 ms: 1.51x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 59.5 ms: 1.51x faster                                                          |
| comprehensions           | 17.7 us                                                         | 11.8 us: 1.51x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 6.86 ms: 1.43x faster                                                          |
| go                       | 146 ms                                                          | 102 ms: 1.43x faster                                                           |
| pylint                   | 384 ms                                                          | 269 ms: 1.42x faster                                                           |
| richards_super           | 49.9 ms                                                         | 35.5 ms: 1.40x faster                                                          |
| chaos                    | 74.4 ms                                                         | 53.6 ms: 1.39x faster                                                          |
| deepcopy                 | 310 us                                                          | 230 us: 1.35x faster                                                           |
| fannkuch                 | 317 ms                                                          | 237 ms: 1.34x faster                                                           |
| scimark_fft              | 216 ms                                                          | 168 ms: 1.29x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.48 sec: 1.29x faster                                                         |
| generators               | 31.6 ms                                                         | 24.5 ms: 1.29x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 1.04 ms: 1.28x faster                                                          |
| pycparser                | 1.04 sec                                                        | 819 ms: 1.27x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 4.91 ms: 1.25x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 49.8 ms: 1.24x faster                                                          |
| richards                 | 40.3 ms                                                         | 32.4 ms: 1.24x faster                                                          |
| raytrace                 | 303 ms                                                          | 245 ms: 1.23x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.64 ms: 1.23x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 233 us: 1.20x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.34 ms: 1.18x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 162 us: 1.17x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 49.9 ms: 1.17x faster                                                          |
| xml_etree_process        | 48.1 ms                                                         | 41.4 ms: 1.16x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 104 ms: 1.15x faster                                                           |
| json                     | 4.76 ms                                                         | 4.14 ms: 1.15x faster                                                          |
| regex_compile            | 117 ms                                                          | 102 ms: 1.15x faster                                                           |
| thrift                   | 902 us                                                          | 788 us: 1.14x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 62.5 ms: 1.13x faster                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 54.5 ms: 1.13x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 78.3 ms: 1.11x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.24 sec: 1.11x faster                                                         |
| pprint_safe_repr         | 658 ms                                                          | 596 ms: 1.11x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.01 ms: 1.10x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 47.5 ms: 1.10x faster                                                          |
| meteor_contest           | 80.0 ms                                                         | 73.2 ms: 1.09x faster                                                          |
| tornado_http             | 118 ms                                                          | 108 ms: 1.09x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 687 ms: 1.08x faster                                                           |
| sympy_sum                | 122 ms                                                          | 114 ms: 1.07x faster                                                           |
| django_template          | 36.0 ms                                                         | 33.6 ms: 1.07x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.9 us: 1.07x faster                                                          |
| regex_dna                | 131 ms                                                          | 122 ms: 1.07x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.51 us: 1.07x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.73 sec: 1.05x faster                                                         |
| sympy_str                | 229 ms                                                          | 223 ms: 1.03x faster                                                           |
| 2to3                     | 265 ms                                                          | 263 ms: 1.01x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 232 ms: 1.01x slower                                                           |
| sympy_integrate          | 16.6 ms                                                         | 16.8 ms: 1.01x slower                                                          |
| sympy_expand             | 391 ms                                                          | 398 ms: 1.02x slower                                                           |
| docutils                 | 1.95 sec                                                        | 2.00 sec: 1.03x slower                                                         |
| sqlglot_optimize         | 44.7 ms                                                         | 45.9 ms: 1.03x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.34 us: 1.05x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.71 us: 1.06x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 86.8 ms: 1.07x slower                                                          |
| python_startup           | 22.9 ms                                                         | 24.9 ms: 1.09x slower                                                          |
| coverage                 | 46.6 ms                                                         | 51.6 ms: 1.11x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 769 us: 1.11x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.46 ms: 1.14x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 21.0 ms: 1.16x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.95 ms: 1.17x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 24.9 ms: 1.19x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 56.4 ms: 1.21x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 82.7 ms: 1.25x slower                                                          |
| telco                    | 4.83 ms                                                         | 6.14 ms: 1.27x slower                                                          |
| async_generators         | 241 ms                                                          | 309 ms: 1.28x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.21x faster                                                                   |

Benchmark hidden because not significant (3): coroutines, regex_v8, asyncio_tcp_ssl
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.217x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown