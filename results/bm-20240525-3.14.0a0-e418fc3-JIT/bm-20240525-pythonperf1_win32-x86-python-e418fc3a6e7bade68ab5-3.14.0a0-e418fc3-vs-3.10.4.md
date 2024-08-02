# Results vs. 3.10.4

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: windows-x86
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 248 ms: 1.07x faster                                                           |
| chameleon      | 6.42 ms                                                         | 6.16 ms: 1.04x faster                                                          |
| docutils       | 1.95 sec                                                        | 1.88 sec: 1.03x faster                                                         |
| html5lib       | 52.1 ms                                                         | 45.1 ms: 1.15x faster                                                          |
| tornado_http   | 118 ms                                                          | 96.9 ms: 1.21x faster                                                          |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 475 ms: 1.94x faster                                                           |
| async_tree_io           | 940 ms                                                          | 539 ms: 1.75x faster                                                           |
| async_tree_none         | 394 ms                                                          | 226 ms: 1.74x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 276 ms: 1.69x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.78x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 195 ms: 2.58x faster                                                           |
| float          | 69.6 ms                                                         | 41.8 ms: 1.67x faster                                                          |
| nbody          | 79.1 ms                                                         | 52.6 ms: 1.50x faster                                                          |
| Geometric mean | (ref)                                                           | 1.86x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 98.3 ms: 1.19x faster                                                          |
| regex_dna      | 131 ms                                                          | 118 ms: 1.11x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.98 ms: 1.19x slower                                                          |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.76 ms: 1.45x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 135 us: 1.41x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 201 us: 1.39x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.41 sec: 1.35x faster                                                         |
| xml_etree_process    | 48.1 ms                                                         | 41.1 ms: 1.17x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 61.0 ms: 1.16x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 103 ms: 1.16x faster                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 55.7 ms: 1.11x faster                                                          |
| json_loads           | 22.4 us                                                         | 20.8 us: 1.08x faster                                                          |
| unpickle_list        | 2.98 us                                                         | 2.88 us: 1.04x faster                                                          |
| pickle               | 7.83 us                                                         | 8.10 us: 1.03x slower                                                          |
| unpickle             | 9.82 us                                                         | 10.3 us: 1.05x slower                                                          |
| pickle_list          | 3.22 us                                                         | 3.57 us: 1.11x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 20.5 us: 1.13x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.8 ms: 1.08x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 20.5 ms: 1.14x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.29 ms: 1.72x faster                                                          |
| django_template | 36.0 ms                                                         | 32.3 ms: 1.12x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 21.4 ms: 1.02x slower                                                          |
| genshi_xml      | 46.6 ms                                                         | 51.3 ms: 1.10x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.14x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 137 us: 2.88x faster                                                           |
| pidigits                 | 502 ms                                                          | 195 ms: 2.58x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 475 ms: 1.94x faster                                                           |
| async_tree_io            | 940 ms                                                          | 539 ms: 1.75x faster                                                           |
| async_tree_none          | 394 ms                                                          | 226 ms: 1.74x faster                                                           |
| mako                     | 9.10 ms                                                         | 5.29 ms: 1.72x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 57.3 ns: 1.71x faster                                                          |
| async_tree_memoization   | 467 ms                                                          | 276 ms: 1.69x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 47.6 ms: 1.69x faster                                                          |
| float                    | 69.6 ms                                                         | 41.8 ms: 1.67x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 49.7 ms: 1.64x faster                                                          |
| comprehensions           | 17.7 us                                                         | 11.1 us: 1.61x faster                                                          |
| pylint                   | 384 ms                                                          | 241 ms: 1.59x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.57 ms: 1.57x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 40.9 ms: 1.51x faster                                                          |
| nbody                    | 79.1 ms                                                         | 52.6 ms: 1.50x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 908 us: 1.46x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 6.76 ms: 1.45x faster                                                          |
| chaos                    | 74.4 ms                                                         | 51.4 ms: 1.45x faster                                                          |
| raytrace                 | 303 ms                                                          | 211 ms: 1.43x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 20.6 us: 1.43x faster                                                          |
| fannkuch                 | 317 ms                                                          | 225 ms: 1.41x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 135 us: 1.41x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 201 us: 1.39x faster                                                           |
| richards_super           | 49.9 ms                                                         | 35.9 ms: 1.39x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.36 ms: 1.37x faster                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.41 sec: 1.35x faster                                                         |
| sqlglot_transpile        | 1.58 ms                                                         | 1.17 ms: 1.35x faster                                                          |
| pyflate                  | 422 ms                                                          | 313 ms: 1.35x faster                                                           |
| generators               | 31.6 ms                                                         | 23.4 ms: 1.35x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 4.58 ms: 1.34x faster                                                          |
| go                       | 146 ms                                                          | 113 ms: 1.29x faster                                                           |
| pycparser                | 1.04 sec                                                        | 811 ms: 1.28x faster                                                           |
| scimark_sor              | 115 ms                                                          | 90.3 ms: 1.27x faster                                                          |
| thrift                   | 902 us                                                          | 710 us: 1.27x faster                                                           |
| richards                 | 40.3 ms                                                         | 31.9 ms: 1.26x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 69.6 ms: 1.25x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 72.1 ms: 1.25x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 608 ms: 1.22x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.87 us: 1.22x faster                                                          |
| tornado_http             | 118 ms                                                          | 96.9 ms: 1.21x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.15 sec: 1.19x faster                                                         |
| regex_compile            | 117 ms                                                          | 98.3 ms: 1.19x faster                                                          |
| scimark_fft              | 216 ms                                                          | 185 ms: 1.17x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 562 ms: 1.17x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 41.1 ms: 1.17x faster                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 61.0 ms: 1.16x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 103 ms: 1.16x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 45.1 ms: 1.15x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 981 us: 1.14x faster                                                           |
| sympy_sum                | 122 ms                                                          | 108 ms: 1.13x faster                                                           |
| json                     | 4.76 ms                                                         | 4.21 ms: 1.13x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.63 sec: 1.12x faster                                                         |
| django_template          | 36.0 ms                                                         | 32.3 ms: 1.12x faster                                                          |
| regex_dna                | 131 ms                                                          | 118 ms: 1.11x faster                                                           |
| coroutines               | 17.9 ms                                                         | 16.2 ms: 1.11x faster                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 55.7 ms: 1.11x faster                                                          |
| meteor_contest           | 80.0 ms                                                         | 72.9 ms: 1.10x faster                                                          |
| sympy_str                | 229 ms                                                          | 212 ms: 1.08x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.8 us: 1.08x faster                                                          |
| 2to3                     | 265 ms                                                          | 248 ms: 1.07x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 15.6 ms: 1.06x faster                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 42.5 ms: 1.05x faster                                                          |
| chameleon                | 6.42 ms                                                         | 6.16 ms: 1.04x faster                                                          |
| unpickle_list            | 2.98 us                                                         | 2.88 us: 1.04x faster                                                          |
| sqlglot_normalize        | 230 ms                                                          | 222 ms: 1.04x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.88 sec: 1.03x faster                                                         |
| sympy_expand             | 391 ms                                                          | 379 ms: 1.03x faster                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.9 sec: 1.01x faster                                                         |
| flaskblogging            | 2.03 sec                                                        | 2.03 sec: 1.00x slower                                                         |
| regex_v8                 | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.35 us: 1.01x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 21.4 ms: 1.02x slower                                                          |
| pickle                   | 7.83 us                                                         | 8.10 us: 1.03x slower                                                          |
| unpickle                 | 9.82 us                                                         | 10.3 us: 1.05x slower                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.84 us: 1.06x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 86.4 ms: 1.06x slower                                                          |
| coverage                 | 46.6 ms                                                         | 49.9 ms: 1.07x slower                                                          |
| python_startup           | 22.9 ms                                                         | 24.8 ms: 1.08x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 51.3 ms: 1.10x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 765 us: 1.10x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.57 us: 1.11x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 20.5 us: 1.13x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 75.4 ms: 1.14x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 20.5 ms: 1.14x slower                                                          |
| telco                    | 4.83 ms                                                         | 5.51 ms: 1.14x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.47 ms: 1.14x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.98 ms: 1.19x slower                                                          |
| async_generators         | 241 ms                                                          | 296 ms: 1.23x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.21x faster                                                                   |

Benchmark hidden because not significant (2): deepcopy, logging_format
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240525-3.14.0a0-e418fc3-JIT/bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown