# Results vs. 3.10.4

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: windows-x86
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.13x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 250 ms: 1.06x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.85 sec: 1.05x faster                                                         |
| html5lib       | 52.1 ms                                                         | 45.1 ms: 1.16x faster                                                          |
| tornado_http   | 118 ms                                                          | 105 ms: 1.12x faster                                                           |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 471 ms: 1.96x faster                                                           |
| async_tree_none         | 394 ms                                                          | 221 ms: 1.78x faster                                                           |
| async_tree_io           | 940 ms                                                          | 539 ms: 1.74x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 278 ms: 1.68x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.79x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 200 ms: 2.51x faster                                                           |
| float          | 69.6 ms                                                         | 60.6 ms: 1.15x faster                                                          |
| nbody          | 79.1 ms                                                         | 96.5 ms: 1.22x slower                                                          |
| Geometric mean | (ref)                                                           | 1.33x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 107 ms: 1.10x faster                                                           |
| regex_dna      | 131 ms                                                          | 127 ms: 1.03x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 2.00 ms: 1.20x slower                                                          |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.21 ms: 1.36x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 109 ms: 1.10x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 254 us: 1.10x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.4 us: 1.10x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 176 us: 1.08x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 68.5 ms: 1.03x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.90 sec: 1.00x faster                                                         |
| xml_etree_process    | 48.1 ms                                                         | 50.8 ms: 1.05x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 69.1 ms: 1.12x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.1 ms: 1.05x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 19.9 ms: 1.10x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.10 ms: 1.12x faster                                                          |
| django_template | 36.0 ms                                                         | 33.3 ms: 1.08x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 21.2 ms: 1.01x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 144 us: 2.75x faster                                                           |
| pidigits                 | 502 ms                                                          | 200 ms: 2.51x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 471 ms: 1.96x faster                                                           |
| async_tree_none          | 394 ms                                                          | 221 ms: 1.78x faster                                                           |
| async_tree_io            | 940 ms                                                          | 539 ms: 1.74x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 278 ms: 1.68x faster                                                           |
| pylint                   | 384 ms                                                          | 239 ms: 1.60x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.70 ms: 1.49x faster                                                          |
| go                       | 146 ms                                                          | 103 ms: 1.41x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 57.8 ms: 1.41x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 21.6 us: 1.37x faster                                                          |
| chaos                    | 74.4 ms                                                         | 54.6 ms: 1.36x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 7.21 ms: 1.36x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 72.8 ns: 1.35x faster                                                          |
| raytrace                 | 303 ms                                                          | 227 ms: 1.33x faster                                                           |
| comprehensions           | 17.7 us                                                         | 13.6 us: 1.30x faster                                                          |
| deepcopy                 | 310 us                                                          | 243 us: 1.28x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 70.3 ms: 1.28x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 1.08 ms: 1.24x faster                                                          |
| thrift                   | 902 us                                                          | 738 us: 1.22x faster                                                           |
| pycparser                | 1.04 sec                                                        | 864 ms: 1.21x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.32 ms: 1.20x faster                                                          |
| generators               | 31.6 ms                                                         | 26.7 ms: 1.18x faster                                                          |
| pyflate                  | 422 ms                                                          | 358 ms: 1.18x faster                                                           |
| scimark_sor              | 115 ms                                                          | 98.2 ms: 1.17x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 50.3 ms: 1.16x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 5.29 ms: 1.16x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 45.1 ms: 1.16x faster                                                          |
| float                    | 69.6 ms                                                         | 60.6 ms: 1.15x faster                                                          |
| sympy_sum                | 122 ms                                                          | 107 ms: 1.15x faster                                                           |
| json                     | 4.76 ms                                                         | 4.18 ms: 1.14x faster                                                          |
| richards_super           | 49.9 ms                                                         | 44.3 ms: 1.13x faster                                                          |
| mako                     | 9.10 ms                                                         | 8.10 ms: 1.12x faster                                                          |
| tornado_http             | 118 ms                                                          | 105 ms: 1.12x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 55.8 ms: 1.11x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 109 ms: 1.10x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 254 us: 1.10x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 79.0 ms: 1.10x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.4 us: 1.10x faster                                                          |
| regex_compile            | 117 ms                                                          | 107 ms: 1.10x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 15.3 ms: 1.09x faster                                                          |
| django_template          | 36.0 ms                                                         | 33.3 ms: 1.08x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 176 us: 1.08x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.50 us: 1.07x faster                                                          |
| sympy_str                | 229 ms                                                          | 214 ms: 1.07x faster                                                           |
| 2to3                     | 265 ms                                                          | 250 ms: 1.06x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 75.5 ms: 1.06x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.72 sec: 1.06x faster                                                         |
| docutils                 | 1.95 sec                                                        | 1.85 sec: 1.05x faster                                                         |
| sympy_expand             | 391 ms                                                          | 375 ms: 1.04x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 68.5 ms: 1.03x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.33 sec: 1.03x faster                                                         |
| coroutines               | 17.9 ms                                                         | 17.4 ms: 1.03x faster                                                          |
| regex_dna                | 131 ms                                                          | 127 ms: 1.03x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.17 ms: 1.02x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 645 ms: 1.02x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 44.2 ms: 1.01x faster                                                          |
| sqlglot_normalize        | 230 ms                                                          | 229 ms: 1.00x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.90 sec: 1.00x faster                                                         |
| genshi_text              | 21.0 ms                                                         | 21.2 ms: 1.01x slower                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.2 sec: 1.01x slower                                                         |
| meteor_contest           | 80.0 ms                                                         | 81.3 ms: 1.02x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.2 ms: 1.03x slower                                                          |
| fannkuch                 | 317 ms                                                          | 332 ms: 1.05x slower                                                           |
| python_startup           | 22.9 ms                                                         | 24.1 ms: 1.05x slower                                                          |
| xml_etree_process        | 48.1 ms                                                         | 50.8 ms: 1.05x slower                                                          |
| scimark_fft              | 216 ms                                                          | 231 ms: 1.07x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 741 us: 1.07x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 87.2 ms: 1.07x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.58 us: 1.08x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.94 us: 1.09x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 19.9 ms: 1.10x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 73.5 ms: 1.11x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.42 ms: 1.11x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 69.1 ms: 1.12x slower                                                          |
| coverage                 | 46.6 ms                                                         | 52.5 ms: 1.13x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 2.00 ms: 1.20x slower                                                          |
| nbody                    | 79.1 ms                                                         | 96.5 ms: 1.22x slower                                                          |
| async_generators         | 241 ms                                                          | 300 ms: 1.24x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.78 ms: 1.40x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.13x faster                                                                   |

Benchmark hidden because not significant (4): bench_thread_pool, asyncio_tcp, richards, genshi_xml
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown