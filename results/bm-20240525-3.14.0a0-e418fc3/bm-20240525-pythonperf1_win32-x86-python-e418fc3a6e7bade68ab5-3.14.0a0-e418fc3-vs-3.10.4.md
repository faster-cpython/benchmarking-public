# Results vs. 3.10.4

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: windows-x86
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 233 ms: 1.14x faster                                                           |
| chameleon      | 6.42 ms                                                         | 5.72 ms: 1.12x faster                                                          |
| docutils       | 1.95 sec                                                        | 1.81 sec: 1.08x faster                                                         |
| html5lib       | 52.1 ms                                                         | 45.0 ms: 1.16x faster                                                          |
| tornado_http   | 118 ms                                                          | 94.8 ms: 1.24x faster                                                          |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 476 ms: 1.94x faster                                                           |
| async_tree_io           | 940 ms                                                          | 528 ms: 1.78x faster                                                           |
| async_tree_none         | 394 ms                                                          | 227 ms: 1.73x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 276 ms: 1.69x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.78x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 199 ms: 2.52x faster                                                           |
| float          | 69.6 ms                                                         | 52.6 ms: 1.32x faster                                                          |
| nbody          | 79.1 ms                                                         | 76.4 ms: 1.04x faster                                                          |
| Geometric mean | (ref)                                                           | 1.51x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 98.9 ms: 1.18x faster                                                          |
| regex_dna      | 131 ms                                                          | 116 ms: 1.13x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.89 ms: 1.14x slower                                                          |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.95 ms: 1.41x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 148 us: 1.28x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 221 us: 1.27x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.60 sec: 1.19x faster                                                         |
| xml_etree_parse      | 120 ms                                                          | 105 ms: 1.14x faster                                                           |
| xml_etree_process    | 48.1 ms                                                         | 42.9 ms: 1.12x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 63.8 ms: 1.11x faster                                                          |
| json_loads           | 22.4 us                                                         | 20.9 us: 1.07x faster                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 60.0 ms: 1.03x faster                                                          |
| pickle               | 7.83 us                                                         | 8.15 us: 1.04x slower                                                          |
| unpickle             | 9.82 us                                                         | 10.4 us: 1.05x slower                                                          |
| pickle_list          | 3.22 us                                                         | 3.63 us: 1.13x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 20.9 us: 1.14x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                                   |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 18.6 ms: 1.03x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 6.94 ms: 1.31x faster                                                          |
| django_template | 36.0 ms                                                         | 30.4 ms: 1.19x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 19.1 ms: 1.10x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 44.2 ms: 1.06x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.16x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 133 us: 2.98x faster                                                           |
| pidigits                 | 502 ms                                                          | 199 ms: 2.52x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 476 ms: 1.94x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.26 ms: 1.79x faster                                                          |
| async_tree_io            | 940 ms                                                          | 528 ms: 1.78x faster                                                           |
| pylint                   | 384 ms                                                          | 218 ms: 1.76x faster                                                           |
| async_tree_none          | 394 ms                                                          | 227 ms: 1.73x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 57.7 ns: 1.70x faster                                                          |
| async_tree_memoization   | 467 ms                                                          | 276 ms: 1.69x faster                                                           |
| raytrace                 | 303 ms                                                          | 185 ms: 1.63x faster                                                           |
| chaos                    | 74.4 ms                                                         | 46.7 ms: 1.59x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 58.3 ms: 1.54x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 54.4 ms: 1.49x faster                                                          |
| comprehensions           | 17.7 us                                                         | 11.9 us: 1.49x faster                                                          |
| generators               | 31.6 ms                                                         | 21.5 ms: 1.47x faster                                                          |
| richards_super           | 49.9 ms                                                         | 34.2 ms: 1.46x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 4.33 ms: 1.42x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 6.95 ms: 1.41x faster                                                          |
| go                       | 146 ms                                                          | 104 ms: 1.40x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 965 us: 1.38x faster                                                           |
| pyflate                  | 422 ms                                                          | 311 ms: 1.35x faster                                                           |
| scimark_sor              | 115 ms                                                          | 85.0 ms: 1.35x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 46.3 ms: 1.34x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.19 ms: 1.33x faster                                                          |
| float                    | 69.6 ms                                                         | 52.6 ms: 1.32x faster                                                          |
| thrift                   | 902 us                                                          | 682 us: 1.32x faster                                                           |
| pycparser                | 1.04 sec                                                        | 788 ms: 1.32x faster                                                           |
| richards                 | 40.3 ms                                                         | 30.5 ms: 1.32x faster                                                          |
| mako                     | 9.10 ms                                                         | 6.94 ms: 1.31x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 66.5 ms: 1.31x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 148 us: 1.28x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 221 us: 1.27x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 23.5 us: 1.26x faster                                                          |
| tornado_http             | 118 ms                                                          | 94.8 ms: 1.24x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 66.2 ms: 1.21x faster                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.60 sec: 1.19x faster                                                         |
| django_template          | 36.0 ms                                                         | 30.4 ms: 1.19x faster                                                          |
| sympy_sum                | 122 ms                                                          | 104 ms: 1.18x faster                                                           |
| regex_compile            | 117 ms                                                          | 98.9 ms: 1.18x faster                                                          |
| fannkuch                 | 317 ms                                                          | 269 ms: 1.18x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.94 us: 1.18x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 45.0 ms: 1.16x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.80 ms: 1.16x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 975 us: 1.15x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 14.6 ms: 1.14x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 105 ms: 1.14x faster                                                           |
| 2to3                     | 265 ms                                                          | 233 ms: 1.14x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 204 ms: 1.13x faster                                                           |
| coroutines               | 17.9 ms                                                         | 15.9 ms: 1.13x faster                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 39.6 ms: 1.13x faster                                                          |
| regex_dna                | 131 ms                                                          | 116 ms: 1.13x faster                                                           |
| chameleon                | 6.42 ms                                                         | 5.72 ms: 1.12x faster                                                          |
| xml_etree_process        | 48.1 ms                                                         | 42.9 ms: 1.12x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.63 sec: 1.12x faster                                                         |
| json                     | 4.76 ms                                                         | 4.27 ms: 1.11x faster                                                          |
| sympy_str                | 229 ms                                                          | 206 ms: 1.11x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 63.8 ms: 1.11x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 674 ms: 1.10x faster                                                           |
| genshi_text              | 21.0 ms                                                         | 19.1 ms: 1.10x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.25 sec: 1.10x faster                                                         |
| deepcopy                 | 310 us                                                          | 283 us: 1.09x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 607 ms: 1.08x faster                                                           |
| sympy_expand             | 391 ms                                                          | 361 ms: 1.08x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 74.4 ms: 1.08x faster                                                          |
| docutils                 | 1.95 sec                                                        | 1.81 sec: 1.08x faster                                                         |
| json_loads               | 22.4 us                                                         | 20.9 us: 1.07x faster                                                          |
| scimark_fft              | 216 ms                                                          | 203 ms: 1.06x faster                                                           |
| genshi_xml               | 46.6 ms                                                         | 44.2 ms: 1.06x faster                                                          |
| nbody                    | 79.1 ms                                                         | 76.4 ms: 1.04x faster                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 60.0 ms: 1.03x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.66 us: 1.01x faster                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.9 sec: 1.01x faster                                                         |
| regex_v8                 | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.47 us: 1.02x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 18.6 ms: 1.03x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.19 us: 1.04x slower                                                          |
| coverage                 | 46.6 ms                                                         | 48.4 ms: 1.04x slower                                                          |
| pickle                   | 7.83 us                                                         | 8.15 us: 1.04x slower                                                          |
| unpickle                 | 9.82 us                                                         | 10.4 us: 1.05x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 71.2 ms: 1.07x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 87.5 ms: 1.08x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 750 us: 1.08x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.13x slower                                                          |
| async_generators         | 241 ms                                                          | 271 ms: 1.13x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.63 us: 1.13x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.89 ms: 1.14x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 20.9 us: 1.14x slower                                                          |
| telco                    | 4.83 ms                                                         | 6.20 ms: 1.28x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.20x faster                                                                   |

Benchmark hidden because not significant (3): python_startup, unpickle_list, flaskblogging
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown