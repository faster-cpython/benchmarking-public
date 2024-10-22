# Results vs. 3.10.4

- fork: python
- ref: d27a53fc02a87e76066f
- machine: windows-x86
- commit hash: d27a53f
- commit date: 2024-07-30
- overall geometric mean: 1.15x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 251 ms: 1.06x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.91 sec: 1.02x faster                                                         |
| html5lib       | 52.1 ms                                                         | 47.8 ms: 1.09x faster                                                          |
| tornado_http   | 118 ms                                                          | 104 ms: 1.13x faster                                                           |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 467 ms: 1.98x faster                                                           |
| async_tree_none         | 394 ms                                                          | 224 ms: 1.75x faster                                                           |
| async_tree_io           | 940 ms                                                          | 549 ms: 1.71x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 276 ms: 1.69x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.78x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 199 ms: 2.53x faster                                                           |
| float          | 69.6 ms                                                         | 58.2 ms: 1.20x faster                                                          |
| nbody          | 79.1 ms                                                         | 88.5 ms: 1.12x slower                                                          |
| Geometric mean | (ref)                                                           | 1.39x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 103 ms: 1.13x faster                                                           |
| regex_dna      | 131 ms                                                          | 122 ms: 1.07x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.3 ms: 1.03x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.91 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.53 ms: 1.30x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 244 us: 1.15x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 107 ms: 1.13x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 169 us: 1.12x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.0 us: 1.12x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.82 sec: 1.05x faster                                                         |
| xml_etree_iterparse  | 70.8 ms                                                         | 69.2 ms: 1.02x faster                                                          |
| xml_etree_process    | 48.1 ms                                                         | 47.3 ms: 1.02x faster                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 66.8 ms: 1.08x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 23.7 ms: 1.03x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 19.7 ms: 1.09x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.01 ms: 1.14x faster                                                          |
| django_template | 36.0 ms                                                         | 34.7 ms: 1.04x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 46.4 ms: 1.01x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 21.6 ms: 1.03x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.04x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 137 us: 2.90x faster                                                           |
| pidigits                 | 502 ms                                                          | 199 ms: 2.53x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 467 ms: 1.98x faster                                                           |
| async_tree_none          | 394 ms                                                          | 224 ms: 1.75x faster                                                           |
| async_tree_io            | 940 ms                                                          | 549 ms: 1.71x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 276 ms: 1.69x faster                                                           |
| pylint                   | 384 ms                                                          | 233 ms: 1.64x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.57 ms: 1.57x faster                                                          |
| chaos                    | 74.4 ms                                                         | 50.5 ms: 1.47x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 55.9 ms: 1.45x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 21.1 us: 1.40x faster                                                          |
| raytrace                 | 303 ms                                                          | 218 ms: 1.39x faster                                                           |
| comprehensions           | 17.7 us                                                         | 13.1 us: 1.35x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 74.2 ns: 1.32x faster                                                          |
| go                       | 146 ms                                                          | 111 ms: 1.32x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 7.53 ms: 1.30x faster                                                          |
| deepcopy                 | 310 us                                                          | 241 us: 1.29x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 70.1 ms: 1.28x faster                                                          |
| pyflate                  | 422 ms                                                          | 331 ms: 1.27x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.06 ms: 1.26x faster                                                          |
| pycparser                | 1.04 sec                                                        | 836 ms: 1.25x faster                                                           |
| richards_super           | 49.9 ms                                                         | 40.2 ms: 1.24x faster                                                          |
| thrift                   | 902 us                                                          | 733 us: 1.23x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 4.99 ms: 1.23x faster                                                          |
| generators               | 31.6 ms                                                         | 25.7 ms: 1.23x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 50.6 ms: 1.22x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.30 ms: 1.22x faster                                                          |
| scimark_sor              | 115 ms                                                          | 94.8 ms: 1.21x faster                                                          |
| float                    | 69.6 ms                                                         | 58.2 ms: 1.20x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 49.4 ms: 1.18x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 73.9 ms: 1.18x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 244 us: 1.15x faster                                                           |
| mako                     | 9.10 ms                                                         | 8.01 ms: 1.14x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 986 us: 1.14x faster                                                           |
| tornado_http             | 118 ms                                                          | 104 ms: 1.13x faster                                                           |
| regex_compile            | 117 ms                                                          | 103 ms: 1.13x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 107 ms: 1.13x faster                                                           |
| sympy_sum                | 122 ms                                                          | 109 ms: 1.13x faster                                                           |
| richards                 | 40.3 ms                                                         | 35.8 ms: 1.12x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 169 us: 1.12x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.0 us: 1.12x faster                                                          |
| json                     | 4.76 ms                                                         | 4.26 ms: 1.12x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.67 sec: 1.09x faster                                                         |
| html5lib                 | 52.1 ms                                                         | 47.8 ms: 1.09x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.4 ms: 1.08x faster                                                          |
| regex_dna                | 131 ms                                                          | 122 ms: 1.07x faster                                                           |
| 2to3                     | 265 ms                                                          | 251 ms: 1.06x faster                                                           |
| sympy_str                | 229 ms                                                          | 217 ms: 1.06x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.55 us: 1.05x faster                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.82 sec: 1.05x faster                                                         |
| spectral_norm            | 80.2 ms                                                         | 76.5 ms: 1.05x faster                                                          |
| meteor_contest           | 80.0 ms                                                         | 76.7 ms: 1.04x faster                                                          |
| coroutines               | 17.9 ms                                                         | 17.3 ms: 1.04x faster                                                          |
| django_template          | 36.0 ms                                                         | 34.7 ms: 1.04x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 719 ms: 1.04x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.14 ms: 1.03x faster                                                          |
| fannkuch                 | 317 ms                                                          | 310 ms: 1.02x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 69.2 ms: 1.02x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.34 sec: 1.02x faster                                                         |
| docutils                 | 1.95 sec                                                        | 1.91 sec: 1.02x faster                                                         |
| xml_etree_process        | 48.1 ms                                                         | 47.3 ms: 1.02x faster                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 44.0 ms: 1.02x faster                                                          |
| sympy_expand             | 391 ms                                                          | 385 ms: 1.02x faster                                                           |
| genshi_xml               | 46.6 ms                                                         | 46.4 ms: 1.01x faster                                                          |
| genshi_text              | 21.0 ms                                                         | 21.6 ms: 1.03x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.3 ms: 1.03x slower                                                          |
| python_startup           | 22.9 ms                                                         | 23.7 ms: 1.03x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 66.8 ms: 1.08x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 19.7 ms: 1.09x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 88.6 ms: 1.09x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 758 us: 1.09x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 73.4 ms: 1.11x slower                                                          |
| coverage                 | 46.6 ms                                                         | 51.8 ms: 1.11x slower                                                          |
| logging_simple           | 7.29 us                                                         | 8.12 us: 1.11x slower                                                          |
| nbody                    | 79.1 ms                                                         | 88.5 ms: 1.12x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.43 ms: 1.12x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.87 us: 1.12x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.91 ms: 1.15x slower                                                          |
| async_generators         | 241 ms                                                          | 280 ms: 1.16x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.15 ms: 1.27x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.15x faster                                                                   |

Benchmark hidden because not significant (4): sqlglot_normalize, pprint_safe_repr, scimark_fft, asyncio_tcp_ssl
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240730-3.14.0a0-d27a53f/bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown