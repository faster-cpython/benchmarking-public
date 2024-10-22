# Results vs. 3.10.4

- fork: python
- ref: 5436d8b9c397c48d9b0d
- machine: windows-x86
- commit hash: 5436d8b
- commit date: 2024-09-11
- overall geometric mean: 1.11x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 249 ms: 1.07x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.86 sec: 1.05x faster                                                         |
| html5lib       | 52.1 ms                                                         | 44.1 ms: 1.18x faster                                                          |
| tornado_http   | 118 ms                                                          | 94.8 ms: 1.24x faster                                                          |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 464 ms: 1.99x faster                                                           |
| async_tree_none         | 394 ms                                                          | 218 ms: 1.81x faster                                                           |
| async_tree_io           | 940 ms                                                          | 529 ms: 1.78x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 271 ms: 1.72x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.82x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 196 ms: 2.56x faster                                                           |
| float          | 69.6 ms                                                         | 62.2 ms: 1.12x faster                                                          |
| nbody          | 79.1 ms                                                         | 91.9 ms: 1.16x slower                                                          |
| Geometric mean | (ref)                                                           | 1.35x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 119 ms: 1.09x faster                                                           |
| regex_compile  | 117 ms                                                          | 108 ms: 1.08x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.3 ms: 1.03x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.92 ms: 1.16x slower                                                          |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.62 ms: 1.29x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 108 ms: 1.11x faster                                                           |
| json_loads           | 22.4 us                                                         | 20.6 us: 1.09x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 262 us: 1.07x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 66.9 ms: 1.06x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 181 us: 1.04x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.89 sec: 1.01x faster                                                         |
| pickle               | 7.83 us                                                         | 7.99 us: 1.02x slower                                                          |
| xml_etree_process    | 48.1 ms                                                         | 49.8 ms: 1.03x slower                                                          |
| unpickle_list        | 2.98 us                                                         | 3.10 us: 1.04x slower                                                          |
| unpickle             | 9.82 us                                                         | 10.3 us: 1.05x slower                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 68.2 ms: 1.11x slower                                                          |
| pickle_list          | 3.22 us                                                         | 3.65 us: 1.14x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 21.0 us: 1.15x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.01x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.0 ms: 1.05x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 19.8 ms: 1.10x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.18 ms: 1.11x faster                                                          |
| django_template | 36.0 ms                                                         | 32.6 ms: 1.10x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 46.9 ms: 1.01x slower                                                          |
| genshi_text     | 21.0 ms                                                         | 22.2 ms: 1.06x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.04x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 145 us: 2.74x faster                                                           |
| pidigits                 | 502 ms                                                          | 196 ms: 2.56x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 464 ms: 1.99x faster                                                           |
| async_tree_none          | 394 ms                                                          | 218 ms: 1.81x faster                                                           |
| async_tree_io            | 940 ms                                                          | 529 ms: 1.78x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 271 ms: 1.72x faster                                                           |
| pylint                   | 384 ms                                                          | 232 ms: 1.65x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.72 ms: 1.48x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 58.1 ms: 1.40x faster                                                          |
| go                       | 146 ms                                                          | 104 ms: 1.40x faster                                                           |
| chaos                    | 74.4 ms                                                         | 53.7 ms: 1.39x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 22.3 us: 1.33x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 68.1 ms: 1.32x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 75.0 ns: 1.30x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 7.62 ms: 1.29x faster                                                          |
| raytrace                 | 303 ms                                                          | 235 ms: 1.29x faster                                                           |
| comprehensions           | 17.7 us                                                         | 14.0 us: 1.27x faster                                                          |
| deepcopy                 | 310 us                                                          | 246 us: 1.26x faster                                                           |
| tornado_http             | 118 ms                                                          | 94.8 ms: 1.24x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 1.08 ms: 1.23x faster                                                          |
| thrift                   | 902 us                                                          | 737 us: 1.22x faster                                                           |
| generators               | 31.6 ms                                                         | 26.2 ms: 1.21x faster                                                          |
| pycparser                | 1.04 sec                                                        | 864 ms: 1.21x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 5.15 ms: 1.19x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 44.1 ms: 1.18x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.35 ms: 1.18x faster                                                          |
| pyflate                  | 422 ms                                                          | 360 ms: 1.17x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 74.9 ms: 1.16x faster                                                          |
| sqlite_synth             | 2.29 us                                                         | 1.97 us: 1.16x faster                                                          |
| dulwich_log              | 58.5 ms                                                         | 50.8 ms: 1.15x faster                                                          |
| sympy_sum                | 122 ms                                                          | 108 ms: 1.14x faster                                                           |
| json                     | 4.76 ms                                                         | 4.25 ms: 1.12x faster                                                          |
| float                    | 69.6 ms                                                         | 62.2 ms: 1.12x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 666 ms: 1.12x faster                                                           |
| mako                     | 9.10 ms                                                         | 8.18 ms: 1.11x faster                                                          |
| richards_super           | 49.9 ms                                                         | 45.0 ms: 1.11x faster                                                          |
| scimark_sor              | 115 ms                                                          | 104 ms: 1.11x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 108 ms: 1.11x faster                                                           |
| django_template          | 36.0 ms                                                         | 32.6 ms: 1.10x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 1.02 ms: 1.10x faster                                                          |
| regex_dna                | 131 ms                                                          | 119 ms: 1.09x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.6 us: 1.09x faster                                                          |
| regex_compile            | 117 ms                                                          | 108 ms: 1.08x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 15.4 ms: 1.08x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 57.5 ms: 1.08x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.70 sec: 1.08x faster                                                         |
| pickle_pure_python       | 280 us                                                          | 262 us: 1.07x faster                                                           |
| 2to3                     | 265 ms                                                          | 249 ms: 1.07x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 66.9 ms: 1.06x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.54 us: 1.06x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 76.1 ms: 1.05x faster                                                          |
| sympy_str                | 229 ms                                                          | 218 ms: 1.05x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.08 ms: 1.05x faster                                                          |
| docutils                 | 1.95 sec                                                        | 1.86 sec: 1.05x faster                                                         |
| unpickle_pure_python     | 189 us                                                          | 181 us: 1.04x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 43.2 ms: 1.03x faster                                                          |
| sqlglot_normalize        | 230 ms                                                          | 226 ms: 1.02x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.89 sec: 1.01x faster                                                         |
| pprint_pformat           | 1.37 sec                                                        | 1.35 sec: 1.01x faster                                                         |
| richards                 | 40.3 ms                                                         | 39.8 ms: 1.01x faster                                                          |
| sympy_expand             | 391 ms                                                          | 388 ms: 1.01x faster                                                           |
| genshi_xml               | 46.6 ms                                                         | 46.9 ms: 1.01x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 81.8 ms: 1.01x slower                                                          |
| pickle                   | 7.83 us                                                         | 7.99 us: 1.02x slower                                                          |
| meteor_contest           | 80.0 ms                                                         | 81.9 ms: 1.02x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.3 ms: 1.03x slower                                                          |
| xml_etree_process        | 48.1 ms                                                         | 49.8 ms: 1.03x slower                                                          |
| unpickle_list            | 2.98 us                                                         | 3.10 us: 1.04x slower                                                          |
| coroutines               | 17.9 ms                                                         | 18.7 ms: 1.04x slower                                                          |
| python_startup           | 22.9 ms                                                         | 24.0 ms: 1.05x slower                                                          |
| unpickle                 | 9.82 us                                                         | 10.3 us: 1.05x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 731 us: 1.05x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 69.9 ms: 1.05x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 22.2 ms: 1.06x slower                                                          |
| fannkuch                 | 317 ms                                                          | 338 ms: 1.07x slower                                                           |
| gc_traversal             | 1.28 ms                                                         | 1.39 ms: 1.09x slower                                                          |
| scimark_fft              | 216 ms                                                          | 236 ms: 1.09x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 19.8 ms: 1.10x slower                                                          |
| logging_simple           | 7.29 us                                                         | 8.04 us: 1.10x slower                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 68.2 ms: 1.11x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.77 us: 1.11x slower                                                          |
| pickle_list              | 3.22 us                                                         | 3.65 us: 1.14x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 21.0 us: 1.15x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.92 ms: 1.16x slower                                                          |
| nbody                    | 79.1 ms                                                         | 91.9 ms: 1.16x slower                                                          |
| coverage                 | 46.6 ms                                                         | 54.7 ms: 1.18x slower                                                          |
| unpack_sequence          | 40.0 ns                                                         | 49.3 ns: 1.23x slower                                                          |
| async_generators         | 241 ms                                                          | 305 ms: 1.27x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.37 ms: 1.32x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.11x faster                                                                   |

Benchmark hidden because not significant (2): pprint_safe_repr, asyncio_tcp_ssl
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240911-3.14.0a0-5436d8b/bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown