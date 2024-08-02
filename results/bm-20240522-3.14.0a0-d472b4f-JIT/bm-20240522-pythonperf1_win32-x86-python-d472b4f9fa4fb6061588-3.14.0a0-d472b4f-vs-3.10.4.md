# Results vs. 3.10.4

- fork: python
- ref: d472b4f9fa4fb6061588
- machine: windows-x86
- commit hash: d472b4f
- commit date: 2024-05-22
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 248 ms: 1.07x faster                                                           |
| chameleon      | 6.42 ms                                                         | 6.12 ms: 1.05x faster                                                          |
| docutils       | 1.95 sec                                                        | 1.87 sec: 1.04x faster                                                         |
| html5lib       | 52.1 ms                                                         | 45.0 ms: 1.16x faster                                                          |
| tornado_http   | 118 ms                                                          | 96.8 ms: 1.21x faster                                                          |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 472 ms: 1.95x faster                                                           |
| async_tree_io           | 940 ms                                                          | 540 ms: 1.74x faster                                                           |
| async_tree_none         | 394 ms                                                          | 228 ms: 1.73x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 280 ms: 1.67x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.77x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 194 ms: 2.59x faster                                                           |
| float          | 69.6 ms                                                         | 41.5 ms: 1.68x faster                                                          |
| nbody          | 79.1 ms                                                         | 52.1 ms: 1.52x faster                                                          |
| Geometric mean | (ref)                                                           | 1.88x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 96.8 ms: 1.20x faster                                                          |
| regex_dna      | 131 ms                                                          | 120 ms: 1.09x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.0 ms: 1.01x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.94 ms: 1.17x slower                                                          |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.74 ms: 1.46x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 196 us: 1.43x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.38 sec: 1.38x faster                                                         |
| unpickle_pure_python | 189 us                                                          | 138 us: 1.38x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 60.0 ms: 1.18x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 102 ms: 1.17x faster                                                           |
| xml_etree_process    | 48.1 ms                                                         | 41.2 ms: 1.17x faster                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 55.3 ms: 1.11x faster                                                          |
| json_loads           | 22.4 us                                                         | 21.0 us: 1.07x faster                                                          |
| unpickle_list        | 2.98 us                                                         | 3.06 us: 1.02x slower                                                          |
| unpickle             | 9.82 us                                                         | 10.2 us: 1.04x slower                                                          |
| pickle               | 7.83 us                                                         | 8.51 us: 1.09x slower                                                          |
| pickle_list          | 3.22 us                                                         | 3.53 us: 1.10x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 20.7 us: 1.14x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.2 ms: 1.05x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 20.4 ms: 1.13x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.25 ms: 1.73x faster                                                          |
| django_template | 36.0 ms                                                         | 31.2 ms: 1.16x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 21.6 ms: 1.03x slower                                                          |
| genshi_xml      | 46.6 ms                                                         | 51.1 ms: 1.10x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 147 us: 2.69x faster                                                           |
| pidigits                 | 502 ms                                                          | 194 ms: 2.59x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 472 ms: 1.95x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 54.8 ns: 1.79x faster                                                          |
| async_tree_io            | 940 ms                                                          | 540 ms: 1.74x faster                                                           |
| mako                     | 9.10 ms                                                         | 5.25 ms: 1.73x faster                                                          |
| async_tree_none          | 394 ms                                                          | 228 ms: 1.73x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 47.3 ms: 1.70x faster                                                          |
| float                    | 69.6 ms                                                         | 41.5 ms: 1.68x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 48.5 ms: 1.68x faster                                                          |
| async_tree_memoization   | 467 ms                                                          | 280 ms: 1.67x faster                                                           |
| pylint                   | 384 ms                                                          | 239 ms: 1.61x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.54 ms: 1.59x faster                                                          |
| comprehensions           | 17.7 us                                                         | 11.2 us: 1.58x faster                                                          |
| nbody                    | 79.1 ms                                                         | 52.1 ms: 1.52x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 891 us: 1.49x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 41.6 ms: 1.49x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 6.74 ms: 1.46x faster                                                          |
| raytrace                 | 303 ms                                                          | 208 ms: 1.46x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 20.5 us: 1.44x faster                                                          |
| pyflate                  | 422 ms                                                          | 292 ms: 1.44x faster                                                           |
| chaos                    | 74.4 ms                                                         | 52.0 ms: 1.43x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 196 us: 1.43x faster                                                           |
| fannkuch                 | 317 ms                                                          | 224 ms: 1.42x faster                                                           |
| richards_super           | 49.9 ms                                                         | 35.3 ms: 1.41x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.34 ms: 1.38x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 4.43 ms: 1.38x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.15 ms: 1.38x faster                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.38 sec: 1.38x faster                                                         |
| unpickle_pure_python     | 189 us                                                          | 138 us: 1.38x faster                                                           |
| generators               | 31.6 ms                                                         | 23.6 ms: 1.34x faster                                                          |
| pycparser                | 1.04 sec                                                        | 794 ms: 1.31x faster                                                           |
| go                       | 146 ms                                                          | 111 ms: 1.31x faster                                                           |
| richards                 | 40.3 ms                                                         | 30.9 ms: 1.30x faster                                                          |
| scimark_sor              | 115 ms                                                          | 89.5 ms: 1.29x faster                                                          |
| thrift                   | 902 us                                                          | 705 us: 1.28x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 70.5 ms: 1.27x faster                                                          |
| scimark_fft              | 216 ms                                                          | 171 ms: 1.26x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 599 ms: 1.24x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 71.0 ms: 1.23x faster                                                          |
| sqlite_synth             | 2.29 us                                                         | 1.88 us: 1.22x faster                                                          |
| tornado_http             | 118 ms                                                          | 96.8 ms: 1.21x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.14 sec: 1.21x faster                                                         |
| regex_compile            | 117 ms                                                          | 96.8 ms: 1.20x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 551 ms: 1.20x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 60.0 ms: 1.18x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 102 ms: 1.17x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 41.2 ms: 1.17x faster                                                          |
| sympy_sum                | 122 ms                                                          | 105 ms: 1.16x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 45.0 ms: 1.16x faster                                                          |
| django_template          | 36.0 ms                                                         | 31.2 ms: 1.16x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.60 sec: 1.14x faster                                                         |
| bench_thread_pool        | 1.12 ms                                                         | 987 us: 1.13x faster                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 55.3 ms: 1.11x faster                                                          |
| meteor_contest           | 80.0 ms                                                         | 72.2 ms: 1.11x faster                                                          |
| sympy_str                | 229 ms                                                          | 209 ms: 1.10x faster                                                           |
| json                     | 4.76 ms                                                         | 4.37 ms: 1.09x faster                                                          |
| regex_dna                | 131 ms                                                          | 120 ms: 1.09x faster                                                           |
| coroutines               | 17.9 ms                                                         | 16.5 ms: 1.09x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.5 ms: 1.08x faster                                                          |
| 2to3                     | 265 ms                                                          | 248 ms: 1.07x faster                                                           |
| json_loads               | 22.4 us                                                         | 21.0 us: 1.07x faster                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 42.0 ms: 1.06x faster                                                          |
| chameleon                | 6.42 ms                                                         | 6.12 ms: 1.05x faster                                                          |
| sqlglot_normalize        | 230 ms                                                          | 220 ms: 1.05x faster                                                           |
| sympy_expand             | 391 ms                                                          | 374 ms: 1.04x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.87 sec: 1.04x faster                                                         |
| deepcopy                 | 310 us                                                          | 298 us: 1.04x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 16.0 ms: 1.01x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.44 us: 1.02x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.09 us: 1.02x slower                                                          |
| unpickle_list            | 2.98 us                                                         | 3.06 us: 1.02x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 21.6 ms: 1.03x slower                                                          |
| unpickle                 | 9.82 us                                                         | 10.2 us: 1.04x slower                                                          |
| python_startup           | 22.9 ms                                                         | 24.2 ms: 1.05x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 85.8 ms: 1.06x slower                                                          |
| coverage                 | 46.6 ms                                                         | 50.2 ms: 1.08x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 749 us: 1.08x slower                                                           |
| pickle                   | 7.83 us                                                         | 8.51 us: 1.09x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 51.1 ms: 1.10x slower                                                          |
| pickle_list              | 3.22 us                                                         | 3.53 us: 1.10x slower                                                          |
| telco                    | 4.83 ms                                                         | 5.45 ms: 1.13x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 74.9 ms: 1.13x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 20.4 ms: 1.13x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 20.7 us: 1.14x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.47 ms: 1.15x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.94 ms: 1.17x slower                                                          |
| async_generators         | 241 ms                                                          | 292 ms: 1.21x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.22x faster                                                                   |

Benchmark hidden because not significant (3): asyncio_tcp_ssl, flaskblogging, deepcopy_reduce
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240522-3.14.0a0-d472b4f-JIT/bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown