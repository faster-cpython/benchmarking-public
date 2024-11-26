# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_likely
- machine: windows-x86
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.175x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 1.95 sec                                                        | 2.05 sec: 1.05x slower                                                         |
| html5lib       | 52.1 ms                                                         | 46.0 ms: 1.13x faster                                                          |
| tornado_http   | 118 ms                                                          | 109 ms: 1.08x faster                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 465 ms: 1.98x faster                                                           |
| async_tree_io           | 940 ms                                                          | 510 ms: 1.84x faster                                                           |
| async_tree_none         | 394 ms                                                          | 215 ms: 1.83x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 273 ms: 1.71x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.84x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 199 ms: 2.53x faster                                                           |
| float          | 69.6 ms                                                         | 45.7 ms: 1.52x faster                                                          |
| nbody          | 79.1 ms                                                         | 59.6 ms: 1.33x faster                                                          |
| Geometric mean | (ref)                                                           | 1.72x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 118 ms: 1.10x faster                                                           |
| regex_compile  | 117 ms                                                          | 106 ms: 1.10x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 15.6 ms: 1.01x faster                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.76 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.91 sec                                                        | 1.51 sec: 1.27x faster                                                         |
| unpickle_pure_python | 189 us                                                          | 164 us: 1.15x faster                                                           |
| xml_etree_process    | 48.1 ms                                                         | 42.3 ms: 1.14x faster                                                          |
| json_dumps           | 9.82 ms                                                         | 8.74 ms: 1.12x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 251 us: 1.12x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 64.0 ms: 1.11x faster                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 56.1 ms: 1.10x faster                                                          |
| json_loads           | 22.4 us                                                         | 20.5 us: 1.09x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 110 ms: 1.09x faster                                                           |
| unpickle_list        | 2.98 us                                                         | 2.81 us: 1.06x faster                                                          |
| unpickle             | 9.82 us                                                         | 10.3 us: 1.05x slower                                                          |
| pickle_list          | 3.22 us                                                         | 3.44 us: 1.07x slower                                                          |
| pickle               | 7.83 us                                                         | 8.39 us: 1.07x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 21.2 us: 1.16x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 20.3 ms: 1.12x slower                                                          |
| python_startup         | 22.9 ms                                                         | 26.9 ms: 1.17x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.15x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.78 ms: 1.57x faster                                                          |
| django_template | 36.0 ms                                                         | 33.1 ms: 1.09x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 22.9 ms: 1.09x slower                                                          |
| genshi_xml      | 46.6 ms                                                         | 53.7 ms: 1.15x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.08x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 142 us: 2.79x faster                                                           |
| pidigits                 | 502 ms                                                          | 199 ms: 2.53x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 465 ms: 1.98x faster                                                           |
| async_tree_io            | 940 ms                                                          | 510 ms: 1.84x faster                                                           |
| async_tree_none          | 394 ms                                                          | 215 ms: 1.83x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 16.7 us: 1.77x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 55.7 ns: 1.76x faster                                                          |
| async_tree_memoization   | 467 ms                                                          | 273 ms: 1.71x faster                                                           |
| scimark_sor              | 115 ms                                                          | 69.2 ms: 1.66x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 50.3 ms: 1.62x faster                                                          |
| mako                     | 9.10 ms                                                         | 5.78 ms: 1.57x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 39.6 ms: 1.56x faster                                                          |
| deltablue                | 4.04 ms                                                         | 2.58 ms: 1.56x faster                                                          |
| float                    | 69.6 ms                                                         | 45.7 ms: 1.52x faster                                                          |
| go                       | 146 ms                                                          | 96.0 ms: 1.52x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 59.9 ms: 1.50x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 57.8 ms: 1.39x faster                                                          |
| comprehensions           | 17.7 us                                                         | 12.8 us: 1.39x faster                                                          |
| pylint                   | 384 ms                                                          | 284 ms: 1.35x faster                                                           |
| chaos                    | 74.4 ms                                                         | 55.3 ms: 1.35x faster                                                          |
| deepcopy                 | 310 us                                                          | 231 us: 1.34x faster                                                           |
| pyflate                  | 422 ms                                                          | 317 ms: 1.33x faster                                                           |
| nbody                    | 79.1 ms                                                         | 59.6 ms: 1.33x faster                                                          |
| generators               | 31.6 ms                                                         | 24.3 ms: 1.30x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 1.04 ms: 1.28x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.55 ms: 1.27x faster                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.51 sec: 1.27x faster                                                         |
| pycparser                | 1.04 sec                                                        | 824 ms: 1.26x faster                                                           |
| fannkuch                 | 317 ms                                                          | 254 ms: 1.25x faster                                                           |
| dulwich_log              | 58.5 ms                                                         | 49.5 ms: 1.18x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.34 ms: 1.18x faster                                                          |
| scimark_fft              | 216 ms                                                          | 184 ms: 1.18x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.96 us: 1.17x faster                                                          |
| unpickle_pure_python     | 189 us                                                          | 164 us: 1.15x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 76.0 ms: 1.15x faster                                                          |
| thrift                   | 902 us                                                          | 790 us: 1.14x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 577 ms: 1.14x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.20 sec: 1.14x faster                                                         |
| xml_etree_process        | 48.1 ms                                                         | 42.3 ms: 1.14x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 5.42 ms: 1.13x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 46.0 ms: 1.13x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.38 us: 1.13x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 8.74 ms: 1.12x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 998 us: 1.12x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 251 us: 1.12x faster                                                           |
| raytrace                 | 303 ms                                                          | 272 ms: 1.11x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 72.1 ms: 1.11x faster                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 64.0 ms: 1.11x faster                                                          |
| richards_super           | 49.9 ms                                                         | 45.2 ms: 1.10x faster                                                          |
| regex_dna                | 131 ms                                                          | 118 ms: 1.10x faster                                                           |
| xml_etree_generate       | 61.6 ms                                                         | 56.1 ms: 1.10x faster                                                          |
| regex_compile            | 117 ms                                                          | 106 ms: 1.10x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.5 us: 1.09x faster                                                          |
| django_template          | 36.0 ms                                                         | 33.1 ms: 1.09x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 110 ms: 1.09x faster                                                           |
| tornado_http             | 118 ms                                                          | 109 ms: 1.08x faster                                                           |
| unpickle_list            | 2.98 us                                                         | 2.81 us: 1.06x faster                                                          |
| sympy_sum                | 122 ms                                                          | 117 ms: 1.05x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.75 sec: 1.04x faster                                                         |
| richards                 | 40.3 ms                                                         | 38.8 ms: 1.04x faster                                                          |
| coroutines               | 17.9 ms                                                         | 17.5 ms: 1.02x faster                                                          |
| sympy_str                | 229 ms                                                          | 226 ms: 1.02x faster                                                           |
| regex_v8                 | 15.8 ms                                                         | 15.6 ms: 1.01x faster                                                          |
| unpack_sequence          | 40.0 ns                                                         | 41.2 ns: 1.03x slower                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 17.5 sec: 1.03x slower                                                         |
| logging_format           | 7.91 us                                                         | 8.24 us: 1.04x slower                                                          |
| sympy_integrate          | 16.6 ms                                                         | 17.4 ms: 1.04x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.62 us: 1.04x slower                                                          |
| unpickle                 | 9.82 us                                                         | 10.3 us: 1.05x slower                                                          |
| docutils                 | 1.95 sec                                                        | 2.05 sec: 1.05x slower                                                         |
| regex_effbot             | 1.66 ms                                                         | 1.76 ms: 1.06x slower                                                          |
| sqlglot_normalize        | 230 ms                                                          | 244 ms: 1.06x slower                                                           |
| pickle_list              | 3.22 us                                                         | 3.44 us: 1.07x slower                                                          |
| pickle                   | 7.83 us                                                         | 8.39 us: 1.07x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 22.9 ms: 1.09x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 89.1 ms: 1.10x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 20.3 ms: 1.12x slower                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 50.3 ms: 1.12x slower                                                          |
| coverage                 | 46.6 ms                                                         | 52.7 ms: 1.13x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 53.7 ms: 1.15x slower                                                          |
| asyncio_tcp              | 744 ms                                                          | 866 ms: 1.16x slower                                                           |
| pickle_dict              | 18.2 us                                                         | 21.2 us: 1.16x slower                                                          |
| python_startup           | 22.9 ms                                                         | 26.9 ms: 1.17x slower                                                          |
| telco                    | 4.83 ms                                                         | 6.10 ms: 1.26x slower                                                          |
| async_generators         | 241 ms                                                          | 322 ms: 1.34x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 94.1 ms: 1.42x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.83 ms: 1.43x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 1.20 ms: 1.73x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.15x faster                                                                   |

Benchmark hidden because not significant (3): json, 2to3, sympy_expand
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241018-3.14.0a1+-bad9944-JIT/bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sphinx

- Geometric mean (including insignificant results): 1.175x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown