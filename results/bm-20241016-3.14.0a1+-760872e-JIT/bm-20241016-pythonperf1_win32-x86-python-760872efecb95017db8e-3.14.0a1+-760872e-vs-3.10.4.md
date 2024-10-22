# Results vs. 3.10.4

- fork: python
- ref: 760872efecb95017db8e
- machine: windows-x86
- commit hash: 760872e
- commit date: 2024-10-16
- overall geometric mean: 1.15x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 1.95 sec                                                        | 2.03 sec: 1.04x slower                                                          |
| html5lib       | 52.1 ms                                                         | 44.6 ms: 1.17x faster                                                           |
| tornado_http   | 118 ms                                                          | 108 ms: 1.09x faster                                                            |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|-------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 499 ms: 1.85x faster                                                            |
| async_tree_io           | 940 ms                                                          | 514 ms: 1.83x faster                                                            |
| async_tree_none         | 394 ms                                                          | 219 ms: 1.79x faster                                                            |
| async_tree_memoization  | 467 ms                                                          | 274 ms: 1.70x faster                                                            |
| Geometric mean          | (ref)                                                           | 1.79x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 201 ms: 2.50x faster                                                            |
| float          | 69.6 ms                                                         | 46.1 ms: 1.51x faster                                                           |
| nbody          | 79.1 ms                                                         | 65.2 ms: 1.21x faster                                                           |
| Geometric mean | (ref)                                                           | 1.66x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 104 ms: 1.12x faster                                                            |
| regex_dna      | 131 ms                                                          | 118 ms: 1.10x faster                                                            |
| regex_v8       | 15.8 ms                                                         | 15.4 ms: 1.03x faster                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.86 ms: 1.12x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.49 sec: 1.28x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 230 us: 1.22x faster                                                            |
| xml_etree_process    | 48.1 ms                                                         | 40.5 ms: 1.19x faster                                                           |
| json_dumps           | 9.82 ms                                                         | 8.31 ms: 1.18x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 161 us: 1.17x faster                                                            |
| xml_etree_iterparse  | 70.8 ms                                                         | 63.8 ms: 1.11x faster                                                           |
| xml_etree_generate   | 61.6 ms                                                         | 55.8 ms: 1.11x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 109 ms: 1.10x faster                                                            |
| json_loads           | 22.4 us                                                         | 20.6 us: 1.09x faster                                                           |
| unpickle_list        | 2.98 us                                                         | 2.96 us: 1.01x faster                                                           |
| unpickle             | 9.82 us                                                         | 10.3 us: 1.05x slower                                                           |
| pickle_list          | 3.22 us                                                         | 3.40 us: 1.06x slower                                                           |
| pickle               | 7.83 us                                                         | 8.44 us: 1.08x slower                                                           |
| pickle_dict          | 18.2 us                                                         | 21.2 us: 1.16x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.07x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.4 ms: 1.13x slower                                                           |
| python_startup         | 22.9 ms                                                         | 26.7 ms: 1.16x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.15x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.75 ms: 1.58x faster                                                           |
| django_template | 36.0 ms                                                         | 32.1 ms: 1.12x faster                                                           |
| genshi_text     | 21.0 ms                                                         | 22.6 ms: 1.08x slower                                                           |
| genshi_xml      | 46.6 ms                                                         | 53.8 ms: 1.15x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.09x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|--------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 141 us: 2.80x faster                                                            |
| pidigits                 | 502 ms                                                          | 201 ms: 2.50x faster                                                            |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 499 ms: 1.85x faster                                                            |
| async_tree_io            | 940 ms                                                          | 514 ms: 1.83x faster                                                            |
| async_tree_none          | 394 ms                                                          | 219 ms: 1.79x faster                                                            |
| deepcopy_memo            | 29.6 us                                                         | 17.0 us: 1.74x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 56.2 ns: 1.74x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 274 ms: 1.70x faster                                                            |
| scimark_sor              | 115 ms                                                          | 68.5 ms: 1.68x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 50.2 ms: 1.62x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.53 ms: 1.59x faster                                                           |
| mako                     | 9.10 ms                                                         | 5.75 ms: 1.58x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 39.6 ms: 1.56x faster                                                           |
| float                    | 69.6 ms                                                         | 46.1 ms: 1.51x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 59.5 ms: 1.51x faster                                                           |
| go                       | 146 ms                                                          | 96.6 ms: 1.51x faster                                                           |
| comprehensions           | 17.7 us                                                         | 12.7 us: 1.40x faster                                                           |
| spectral_norm            | 80.2 ms                                                         | 57.8 ms: 1.39x faster                                                           |
| pylint                   | 384 ms                                                          | 283 ms: 1.36x faster                                                            |
| chaos                    | 74.4 ms                                                         | 55.1 ms: 1.35x faster                                                           |
| pyflate                  | 422 ms                                                          | 316 ms: 1.33x faster                                                            |
| deepcopy                 | 310 us                                                          | 236 us: 1.32x faster                                                            |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.50 ms: 1.30x faster                                                           |
| sqlglot_parse            | 1.33 ms                                                         | 1.04 ms: 1.29x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.49 sec: 1.28x faster                                                          |
| fannkuch                 | 317 ms                                                          | 248 ms: 1.28x faster                                                            |
| pycparser                | 1.04 sec                                                        | 821 ms: 1.27x faster                                                            |
| generators               | 31.6 ms                                                         | 24.9 ms: 1.27x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 230 us: 1.22x faster                                                            |
| nbody                    | 79.1 ms                                                         | 65.2 ms: 1.21x faster                                                           |
| scimark_fft              | 216 ms                                                          | 180 ms: 1.20x faster                                                            |
| sqlite_synth             | 2.29 us                                                         | 1.92 us: 1.19x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 40.5 ms: 1.19x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.34 ms: 1.19x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 49.5 ms: 1.18x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 8.31 ms: 1.18x faster                                                           |
| richards_super           | 49.9 ms                                                         | 42.3 ms: 1.18x faster                                                           |
| thrift                   | 902 us                                                          | 767 us: 1.18x faster                                                            |
| unpickle_pure_python     | 189 us                                                          | 161 us: 1.17x faster                                                            |
| nqueens                  | 87.1 ms                                                         | 74.6 ms: 1.17x faster                                                           |
| html5lib                 | 52.1 ms                                                         | 44.6 ms: 1.17x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.21 sec: 1.13x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 995 us: 1.13x faster                                                            |
| pprint_safe_repr         | 658 ms                                                          | 585 ms: 1.13x faster                                                            |
| django_template          | 36.0 ms                                                         | 32.1 ms: 1.12x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 5.46 ms: 1.12x faster                                                           |
| regex_compile            | 117 ms                                                          | 104 ms: 1.12x faster                                                            |
| raytrace                 | 303 ms                                                          | 271 ms: 1.11x faster                                                            |
| xml_etree_iterparse      | 70.8 ms                                                         | 63.8 ms: 1.11x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 72.1 ms: 1.11x faster                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 55.8 ms: 1.11x faster                                                           |
| deepcopy_reduce          | 2.68 us                                                         | 2.43 us: 1.10x faster                                                           |
| regex_dna                | 131 ms                                                          | 118 ms: 1.10x faster                                                            |
| xml_etree_parse          | 120 ms                                                          | 109 ms: 1.10x faster                                                            |
| tornado_http             | 118 ms                                                          | 108 ms: 1.09x faster                                                            |
| json_loads               | 22.4 us                                                         | 20.6 us: 1.09x faster                                                           |
| sympy_sum                | 122 ms                                                          | 116 ms: 1.05x faster                                                            |
| richards                 | 40.3 ms                                                         | 38.3 ms: 1.05x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.74 sec: 1.05x faster                                                          |
| coroutines               | 17.9 ms                                                         | 17.4 ms: 1.03x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 15.4 ms: 1.03x faster                                                           |
| unpickle_list            | 2.98 us                                                         | 2.96 us: 1.01x faster                                                           |
| sympy_expand             | 391 ms                                                          | 394 ms: 1.01x slower                                                            |
| logging_simple           | 7.29 us                                                         | 7.36 us: 1.01x slower                                                           |
| unpack_sequence          | 40.0 ns                                                         | 40.5 ns: 1.01x slower                                                           |
| logging_format           | 7.91 us                                                         | 8.11 us: 1.03x slower                                                           |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.4 sec: 1.03x slower                                                          |
| sqlglot_normalize        | 230 ms                                                          | 239 ms: 1.04x slower                                                            |
| docutils                 | 1.95 sec                                                        | 2.03 sec: 1.04x slower                                                          |
| sympy_integrate          | 16.6 ms                                                         | 17.4 ms: 1.05x slower                                                           |
| unpickle                 | 9.82 us                                                         | 10.3 us: 1.05x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.40 us: 1.06x slower                                                           |
| pickle                   | 7.83 us                                                         | 8.44 us: 1.08x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 22.6 ms: 1.08x slower                                                           |
| pathlib                  | 81.2 ms                                                         | 88.5 ms: 1.09x slower                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 49.2 ms: 1.10x slower                                                           |
| asyncio_tcp              | 744 ms                                                          | 826 ms: 1.11x slower                                                            |
| regex_effbot             | 1.66 ms                                                         | 1.86 ms: 1.12x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 20.4 ms: 1.13x slower                                                           |
| coverage                 | 46.6 ms                                                         | 53.5 ms: 1.15x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 53.8 ms: 1.15x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 21.2 us: 1.16x slower                                                           |
| python_startup           | 22.9 ms                                                         | 26.7 ms: 1.16x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.08 ms: 1.26x slower                                                           |
| async_generators         | 241 ms                                                          | 324 ms: 1.35x slower                                                            |
| gc_traversal             | 1.28 ms                                                         | 1.80 ms: 1.41x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 94.3 ms: 1.42x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 1.20 ms: 1.73x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.15x faster                                                                    |

Benchmark hidden because not significant (3): sympy_str, 2to3, json
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241016-3.14.0a1+-760872e-JIT/bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown