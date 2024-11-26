# Results vs. 3.10.4

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: windows-x86
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.111x faster
- HPT reliability: 99.89%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 252 ms: 1.05x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.87 sec: 1.04x faster                                                         |
| html5lib       | 52.1 ms                                                         | 46.7 ms: 1.11x faster                                                          |
| tornado_http   | 118 ms                                                          | 105 ms: 1.11x faster                                                           |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 479 ms: 1.92x faster                                                           |
| async_tree_none         | 394 ms                                                          | 219 ms: 1.80x faster                                                           |
| async_tree_io           | 940 ms                                                          | 540 ms: 1.74x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 275 ms: 1.70x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.79x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 196 ms: 2.56x faster                                                           |
| float          | 69.6 ms                                                         | 62.7 ms: 1.11x faster                                                          |
| nbody          | 79.1 ms                                                         | 93.9 ms: 1.19x slower                                                          |
| Geometric mean | (ref)                                                           | 1.34x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 118 ms: 1.11x faster                                                           |
| regex_compile  | 117 ms                                                          | 111 ms: 1.06x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.92 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.61 ms: 1.29x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.12x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.7 us: 1.08x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 263 us: 1.06x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.3 ms: 1.05x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 188 us: 1.01x faster                                                           |
| pickle               | 7.83 us                                                         | 8.00 us: 1.02x slower                                                          |
| unpickle_list        | 2.98 us                                                         | 3.07 us: 1.03x slower                                                          |
| pickle_list          | 3.22 us                                                         | 3.33 us: 1.03x slower                                                          |
| unpickle             | 9.82 us                                                         | 10.5 us: 1.07x slower                                                          |
| xml_etree_process    | 48.1 ms                                                         | 51.8 ms: 1.08x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 20.5 us: 1.12x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 70.2 ms: 1.14x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.8 ms: 1.08x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 20.5 ms: 1.14x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.31 ms: 1.10x faster                                                          |
| django_template | 36.0 ms                                                         | 34.7 ms: 1.04x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 48.5 ms: 1.04x slower                                                          |
| genshi_text     | 21.0 ms                                                         | 22.3 ms: 1.06x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.01x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 145 us: 2.72x faster                                                           |
| pidigits                 | 502 ms                                                          | 196 ms: 2.56x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 479 ms: 1.92x faster                                                           |
| async_tree_none          | 394 ms                                                          | 219 ms: 1.80x faster                                                           |
| async_tree_io            | 940 ms                                                          | 540 ms: 1.74x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 275 ms: 1.70x faster                                                           |
| pylint                   | 384 ms                                                          | 235 ms: 1.63x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.81 ms: 1.43x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 59.0 ms: 1.38x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 73.7 ns: 1.33x faster                                                          |
| go                       | 146 ms                                                          | 111 ms: 1.31x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 7.61 ms: 1.29x faster                                                          |
| chaos                    | 74.4 ms                                                         | 58.0 ms: 1.28x faster                                                          |
| comprehensions           | 17.7 us                                                         | 13.9 us: 1.28x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 70.5 ms: 1.27x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 23.5 us: 1.26x faster                                                          |
| deepcopy                 | 310 us                                                          | 250 us: 1.24x faster                                                           |
| thrift                   | 902 us                                                          | 743 us: 1.22x faster                                                           |
| pycparser                | 1.04 sec                                                        | 863 ms: 1.21x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.10 ms: 1.20x faster                                                          |
| raytrace                 | 303 ms                                                          | 252 ms: 1.20x faster                                                           |
| generators               | 31.6 ms                                                         | 26.8 ms: 1.18x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.37 ms: 1.16x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 75.5 ms: 1.15x faster                                                          |
| sqlite_synth             | 2.29 us                                                         | 1.99 us: 1.15x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 5.36 ms: 1.14x faster                                                          |
| sympy_sum                | 122 ms                                                          | 107 ms: 1.14x faster                                                           |
| pyflate                  | 422 ms                                                          | 370 ms: 1.14x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.12x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 52.5 ms: 1.12x faster                                                          |
| tornado_http             | 118 ms                                                          | 105 ms: 1.11x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 46.7 ms: 1.11x faster                                                          |
| scimark_sor              | 115 ms                                                          | 104 ms: 1.11x faster                                                           |
| json                     | 4.76 ms                                                         | 4.29 ms: 1.11x faster                                                          |
| float                    | 69.6 ms                                                         | 62.7 ms: 1.11x faster                                                          |
| regex_dna                | 131 ms                                                          | 118 ms: 1.11x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.02 ms: 1.10x faster                                                          |
| mako                     | 9.10 ms                                                         | 8.31 ms: 1.10x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.7 us: 1.08x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.69 sec: 1.08x faster                                                         |
| asyncio_tcp              | 744 ms                                                          | 696 ms: 1.07x faster                                                           |
| richards_super           | 49.9 ms                                                         | 46.8 ms: 1.07x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 263 us: 1.06x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 15.6 ms: 1.06x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 58.3 ms: 1.06x faster                                                          |
| regex_compile            | 117 ms                                                          | 111 ms: 1.06x faster                                                           |
| 2to3                     | 265 ms                                                          | 252 ms: 1.05x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.3 ms: 1.05x faster                                                          |
| sympy_str                | 229 ms                                                          | 218 ms: 1.05x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.87 sec: 1.04x faster                                                         |
| django_template          | 36.0 ms                                                         | 34.7 ms: 1.04x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.59 us: 1.04x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.15 ms: 1.03x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 78.6 ms: 1.02x faster                                                          |
| sympy_expand             | 391 ms                                                          | 384 ms: 1.02x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 188 us: 1.01x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 80.6 ms: 1.01x slower                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.1 sec: 1.01x slower                                                         |
| pprint_safe_repr         | 658 ms                                                          | 668 ms: 1.01x slower                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.40 sec: 1.02x slower                                                         |
| regex_v8                 | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                          |
| pickle                   | 7.83 us                                                         | 8.00 us: 1.02x slower                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 45.8 ms: 1.03x slower                                                          |
| unpickle_list            | 2.98 us                                                         | 3.07 us: 1.03x slower                                                          |
| richards                 | 40.3 ms                                                         | 41.4 ms: 1.03x slower                                                          |
| coroutines               | 17.9 ms                                                         | 18.5 ms: 1.03x slower                                                          |
| sqlglot_normalize        | 230 ms                                                          | 238 ms: 1.03x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.33 us: 1.03x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 48.5 ms: 1.04x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 723 us: 1.04x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 22.3 ms: 1.06x slower                                                          |
| fannkuch                 | 317 ms                                                          | 340 ms: 1.07x slower                                                           |
| unpickle                 | 9.82 us                                                         | 10.5 us: 1.07x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 87.2 ms: 1.07x slower                                                          |
| xml_etree_process        | 48.1 ms                                                         | 51.8 ms: 1.08x slower                                                          |
| python_startup           | 22.9 ms                                                         | 24.8 ms: 1.08x slower                                                          |
| coverage                 | 46.6 ms                                                         | 51.0 ms: 1.09x slower                                                          |
| unpack_sequence          | 40.0 ns                                                         | 44.0 ns: 1.10x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.41 ms: 1.10x slower                                                          |
| scimark_fft              | 216 ms                                                          | 238 ms: 1.10x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 20.5 us: 1.12x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.91 us: 1.13x slower                                                          |
| logging_simple           | 7.29 us                                                         | 8.23 us: 1.13x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 20.5 ms: 1.14x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 70.2 ms: 1.14x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.92 ms: 1.15x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 77.0 ms: 1.16x slower                                                          |
| nbody                    | 79.1 ms                                                         | 93.9 ms: 1.19x slower                                                          |
| async_generators         | 241 ms                                                          | 310 ms: 1.29x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.82 ms: 1.41x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.09x faster                                                                   |

Benchmark hidden because not significant (1): tomli_loads
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.111x faster
# HPT report

- Reliability score: 99.89% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown