# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: macro_ify
- machine: windows-x86
- commit hash: 2302696
- commit date: 2024-07-02
- overall geometric mean: 1.14x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 253 ms: 1.05x faster                                                          |
| docutils       | 1.95 sec                                                        | 1.89 sec: 1.03x faster                                                        |
| html5lib       | 52.1 ms                                                         | 49.9 ms: 1.04x faster                                                         |
| tornado_http   | 118 ms                                                          | 95.2 ms: 1.24x faster                                                         |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|-------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 470 ms: 1.96x faster                                                          |
| async_tree_none         | 394 ms                                                          | 223 ms: 1.77x faster                                                          |
| async_tree_io           | 940 ms                                                          | 539 ms: 1.75x faster                                                          |
| async_tree_memoization  | 467 ms                                                          | 272 ms: 1.72x faster                                                          |
| Geometric mean          | (ref)                                                           | 1.80x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 196 ms: 2.56x faster                                                          |
| float          | 69.6 ms                                                         | 60.9 ms: 1.14x faster                                                         |
| nbody          | 79.1 ms                                                         | 93.6 ms: 1.18x slower                                                         |
| Geometric mean | (ref)                                                           | 1.35x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 106 ms: 1.10x faster                                                          |
| regex_dna      | 131 ms                                                          | 124 ms: 1.05x faster                                                          |
| regex_v8       | 15.8 ms                                                         | 16.3 ms: 1.03x slower                                                         |
| regex_effbot   | 1.66 ms                                                         | 1.92 ms: 1.15x slower                                                         |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.29 ms: 1.35x faster                                                         |
| pickle_pure_python   | 280 us                                                          | 245 us: 1.14x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 106 ms: 1.13x faster                                                          |
| unpickle_pure_python | 189 us                                                          | 171 us: 1.11x faster                                                          |
| json_loads           | 22.4 us                                                         | 20.5 us: 1.09x faster                                                         |
| xml_etree_iterparse  | 70.8 ms                                                         | 67.1 ms: 1.06x faster                                                         |
| tomli_loads          | 1.91 sec                                                        | 1.82 sec: 1.05x faster                                                        |
| xml_etree_process    | 48.1 ms                                                         | 48.6 ms: 1.01x slower                                                         |
| xml_etree_generate   | 61.6 ms                                                         | 66.0 ms: 1.07x slower                                                         |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 18.8 ms: 1.04x slower                                                         |
| Geometric mean         | (ref)                                                           | 1.02x slower                                                                  |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 8.10 ms: 1.12x faster                                                         |
| django_template | 36.0 ms                                                         | 34.0 ms: 1.06x faster                                                         |
| genshi_xml      | 46.6 ms                                                         | 47.6 ms: 1.02x slower                                                         |
| genshi_text     | 21.0 ms                                                         | 22.0 ms: 1.05x slower                                                         |
| Geometric mean  | (ref)                                                           | 1.03x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|--------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 153 us: 2.59x faster                                                          |
| pidigits                 | 502 ms                                                          | 196 ms: 2.56x faster                                                          |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 470 ms: 1.96x faster                                                          |
| async_tree_none          | 394 ms                                                          | 223 ms: 1.77x faster                                                          |
| async_tree_io            | 940 ms                                                          | 539 ms: 1.75x faster                                                          |
| async_tree_memoization   | 467 ms                                                          | 272 ms: 1.72x faster                                                          |
| pylint                   | 384 ms                                                          | 227 ms: 1.69x faster                                                          |
| deltablue                | 4.04 ms                                                         | 2.64 ms: 1.53x faster                                                         |
| crypto_pyaes             | 81.3 ms                                                         | 58.2 ms: 1.40x faster                                                         |
| chaos                    | 74.4 ms                                                         | 53.7 ms: 1.39x faster                                                         |
| deepcopy_memo            | 29.6 us                                                         | 21.6 us: 1.37x faster                                                         |
| json_dumps               | 9.82 ms                                                         | 7.29 ms: 1.35x faster                                                         |
| raytrace                 | 303 ms                                                          | 226 ms: 1.34x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 68.7 ms: 1.31x faster                                                         |
| logging_silent           | 97.9 ns                                                         | 75.1 ns: 1.30x faster                                                         |
| go                       | 146 ms                                                          | 115 ms: 1.27x faster                                                          |
| comprehensions           | 17.7 us                                                         | 14.0 us: 1.27x faster                                                         |
| richards_super           | 49.9 ms                                                         | 40.1 ms: 1.24x faster                                                         |
| deepcopy                 | 310 us                                                          | 249 us: 1.24x faster                                                          |
| pycparser                | 1.04 sec                                                        | 838 ms: 1.24x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 1.07 ms: 1.24x faster                                                         |
| tornado_http             | 118 ms                                                          | 95.2 ms: 1.24x faster                                                         |
| pyflate                  | 422 ms                                                          | 342 ms: 1.23x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.31 ms: 1.21x faster                                                         |
| hexiom                   | 6.13 ms                                                         | 5.09 ms: 1.20x faster                                                         |
| scimark_sor              | 115 ms                                                          | 97.2 ms: 1.18x faster                                                         |
| thrift                   | 902 us                                                          | 763 us: 1.18x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 53.1 ms: 1.17x faster                                                         |
| generators               | 31.6 ms                                                         | 27.3 ms: 1.16x faster                                                         |
| pickle_pure_python       | 280 us                                                          | 245 us: 1.14x faster                                                          |
| float                    | 69.6 ms                                                         | 60.9 ms: 1.14x faster                                                         |
| bench_thread_pool        | 1.12 ms                                                         | 983 us: 1.14x faster                                                          |
| richards                 | 40.3 ms                                                         | 35.4 ms: 1.14x faster                                                         |
| sympy_sum                | 122 ms                                                          | 109 ms: 1.13x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 106 ms: 1.13x faster                                                          |
| mako                     | 9.10 ms                                                         | 8.10 ms: 1.12x faster                                                         |
| json                     | 4.76 ms                                                         | 4.24 ms: 1.12x faster                                                         |
| nqueens                  | 87.1 ms                                                         | 77.8 ms: 1.12x faster                                                         |
| asyncio_tcp              | 744 ms                                                          | 665 ms: 1.12x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 171 us: 1.11x faster                                                          |
| regex_compile            | 117 ms                                                          | 106 ms: 1.10x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.67 sec: 1.09x faster                                                        |
| json_loads               | 22.4 us                                                         | 20.5 us: 1.09x faster                                                         |
| sympy_integrate          | 16.6 ms                                                         | 15.4 ms: 1.08x faster                                                         |
| django_template          | 36.0 ms                                                         | 34.0 ms: 1.06x faster                                                         |
| xml_etree_iterparse      | 70.8 ms                                                         | 67.1 ms: 1.06x faster                                                         |
| regex_dna                | 131 ms                                                          | 124 ms: 1.05x faster                                                          |
| sympy_str                | 229 ms                                                          | 218 ms: 1.05x faster                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.82 sec: 1.05x faster                                                        |
| 2to3                     | 265 ms                                                          | 253 ms: 1.05x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 76.4 ms: 1.05x faster                                                         |
| deepcopy_reduce          | 2.68 us                                                         | 2.57 us: 1.04x faster                                                         |
| html5lib                 | 52.1 ms                                                         | 49.9 ms: 1.04x faster                                                         |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 3.12 ms: 1.04x faster                                                         |
| coroutines               | 17.9 ms                                                         | 17.3 ms: 1.04x faster                                                         |
| docutils                 | 1.95 sec                                                        | 1.89 sec: 1.03x faster                                                        |
| sympy_expand             | 391 ms                                                          | 382 ms: 1.02x faster                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 44.0 ms: 1.02x faster                                                         |
| pprint_pformat           | 1.37 sec                                                        | 1.35 sec: 1.02x faster                                                        |
| sqlglot_normalize        | 230 ms                                                          | 228 ms: 1.01x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 653 ms: 1.01x faster                                                          |
| meteor_contest           | 80.0 ms                                                         | 79.4 ms: 1.01x faster                                                         |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.9 sec: 1.01x faster                                                        |
| fannkuch                 | 317 ms                                                          | 320 ms: 1.01x slower                                                          |
| xml_etree_process        | 48.1 ms                                                         | 48.6 ms: 1.01x slower                                                         |
| genshi_xml               | 46.6 ms                                                         | 47.6 ms: 1.02x slower                                                         |
| pathlib                  | 81.2 ms                                                         | 83.8 ms: 1.03x slower                                                         |
| regex_v8                 | 15.8 ms                                                         | 16.3 ms: 1.03x slower                                                         |
| python_startup_no_site   | 18.1 ms                                                         | 18.8 ms: 1.04x slower                                                         |
| genshi_text              | 21.0 ms                                                         | 22.0 ms: 1.05x slower                                                         |
| bench_mp_pool            | 66.4 ms                                                         | 70.5 ms: 1.06x slower                                                         |
| xml_etree_generate       | 61.6 ms                                                         | 66.0 ms: 1.07x slower                                                         |
| create_gc_cycles         | 694 us                                                          | 749 us: 1.08x slower                                                          |
| logging_simple           | 7.29 us                                                         | 8.04 us: 1.10x slower                                                         |
| coverage                 | 46.6 ms                                                         | 51.5 ms: 1.11x slower                                                         |
| logging_format           | 7.91 us                                                         | 8.75 us: 1.11x slower                                                         |
| gc_traversal             | 1.28 ms                                                         | 1.43 ms: 1.12x slower                                                         |
| regex_effbot             | 1.66 ms                                                         | 1.92 ms: 1.15x slower                                                         |
| nbody                    | 79.1 ms                                                         | 93.6 ms: 1.18x slower                                                         |
| async_generators         | 241 ms                                                          | 292 ms: 1.21x slower                                                          |
| telco                    | 4.83 ms                                                         | 6.23 ms: 1.29x slower                                                         |
| Geometric mean           | (ref)                                                           | 1.14x faster                                                                  |

Benchmark hidden because not significant (2): python_startup, scimark_fft
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240702-3.14.0a0-2302696/bm-20240702-pythonperf1_win32-x86-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown