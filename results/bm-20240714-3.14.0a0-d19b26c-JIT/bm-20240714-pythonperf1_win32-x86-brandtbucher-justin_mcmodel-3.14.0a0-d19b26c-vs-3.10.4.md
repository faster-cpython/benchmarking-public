# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_mcmodel
- machine: windows-x86
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 254 ms: 1.05x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.92 sec: 1.02x faster                                                         |
| html5lib       | 52.1 ms                                                         | 47.7 ms: 1.09x faster                                                          |
| tornado_http   | 118 ms                                                          | 97.7 ms: 1.20x faster                                                          |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 475 ms: 1.94x faster                                                           |
| async_tree_none         | 394 ms                                                          | 219 ms: 1.80x faster                                                           |
| async_tree_io           | 940 ms                                                          | 538 ms: 1.75x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 271 ms: 1.72x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.80x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 196 ms: 2.57x faster                                                           |
| float          | 69.6 ms                                                         | 43.2 ms: 1.61x faster                                                          |
| nbody          | 79.1 ms                                                         | 54.9 ms: 1.44x faster                                                          |
| Geometric mean | (ref)                                                           | 1.81x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 96.0 ms: 1.22x faster                                                          |
| regex_dna      | 131 ms                                                          | 117 ms: 1.12x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.0 ms: 1.01x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.90 ms: 1.14x slower                                                          |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 7.15 ms: 1.37x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 215 us: 1.31x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 147 us: 1.29x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.51 sec: 1.27x faster                                                         |
| xml_etree_iterparse  | 70.8 ms                                                         | 61.4 ms: 1.15x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 104 ms: 1.15x faster                                                           |
| xml_etree_process    | 48.1 ms                                                         | 44.4 ms: 1.08x faster                                                          |
| json_loads           | 22.4 us                                                         | 21.6 us: 1.04x faster                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 62.1 ms: 1.01x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.18x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.1 ms: 1.06x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.03x slower                                                                   |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.45 ms: 1.67x faster                                                          |
| django_template | 36.0 ms                                                         | 32.6 ms: 1.11x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 22.6 ms: 1.08x slower                                                          |
| genshi_xml      | 46.6 ms                                                         | 53.2 ms: 1.14x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.11x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 153 us: 2.59x faster                                                           |
| pidigits                 | 502 ms                                                          | 196 ms: 2.57x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 15.2 us: 1.95x faster                                                          |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 475 ms: 1.94x faster                                                           |
| async_tree_none          | 394 ms                                                          | 219 ms: 1.80x faster                                                           |
| async_tree_io            | 940 ms                                                          | 538 ms: 1.75x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 271 ms: 1.72x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 57.3 ns: 1.71x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 48.3 ms: 1.68x faster                                                          |
| mako                     | 9.10 ms                                                         | 5.45 ms: 1.67x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 48.2 ms: 1.66x faster                                                          |
| float                    | 69.6 ms                                                         | 43.2 ms: 1.61x faster                                                          |
| pylint                   | 384 ms                                                          | 241 ms: 1.59x faster                                                           |
| comprehensions           | 17.7 us                                                         | 11.2 us: 1.58x faster                                                          |
| pyflate                  | 422 ms                                                          | 283 ms: 1.49x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 41.9 ms: 1.48x faster                                                          |
| deltablue                | 4.04 ms                                                         | 2.74 ms: 1.47x faster                                                          |
| nbody                    | 79.1 ms                                                         | 54.9 ms: 1.44x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 941 us: 1.41x faster                                                           |
| chaos                    | 74.4 ms                                                         | 53.5 ms: 1.39x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 7.15 ms: 1.37x faster                                                          |
| fannkuch                 | 317 ms                                                          | 233 ms: 1.36x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 4.56 ms: 1.34x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.45 ms: 1.32x faster                                                          |
| deepcopy                 | 310 us                                                          | 237 us: 1.31x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 215 us: 1.31x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.21 ms: 1.31x faster                                                          |
| raytrace                 | 303 ms                                                          | 233 ms: 1.30x faster                                                           |
| richards_super           | 49.9 ms                                                         | 38.6 ms: 1.29x faster                                                          |
| go                       | 146 ms                                                          | 113 ms: 1.29x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 147 us: 1.29x faster                                                           |
| scimark_fft              | 216 ms                                                          | 168 ms: 1.29x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.51 sec: 1.27x faster                                                         |
| pycparser                | 1.04 sec                                                        | 834 ms: 1.25x faster                                                           |
| richards                 | 40.3 ms                                                         | 32.9 ms: 1.22x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 609 ms: 1.22x faster                                                           |
| regex_compile            | 117 ms                                                          | 96.0 ms: 1.22x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 72.2 ms: 1.21x faster                                                          |
| tornado_http             | 118 ms                                                          | 97.7 ms: 1.20x faster                                                          |
| thrift                   | 902 us                                                          | 753 us: 1.20x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.15 sec: 1.19x faster                                                         |
| pprint_safe_repr         | 658 ms                                                          | 560 ms: 1.18x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 61.4 ms: 1.15x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 77.8 ms: 1.15x faster                                                          |
| scimark_sor              | 115 ms                                                          | 100 ms: 1.15x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 975 us: 1.15x faster                                                           |
| xml_etree_parse          | 120 ms                                                          | 104 ms: 1.15x faster                                                           |
| generators               | 31.6 ms                                                         | 27.6 ms: 1.15x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.37 us: 1.13x faster                                                          |
| sympy_sum                | 122 ms                                                          | 109 ms: 1.12x faster                                                           |
| regex_dna                | 131 ms                                                          | 117 ms: 1.12x faster                                                           |
| django_template          | 36.0 ms                                                         | 32.6 ms: 1.11x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 47.7 ms: 1.09x faster                                                          |
| xml_etree_process        | 48.1 ms                                                         | 44.4 ms: 1.08x faster                                                          |
| meteor_contest           | 80.0 ms                                                         | 74.6 ms: 1.07x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.72 sec: 1.06x faster                                                         |
| sympy_str                | 229 ms                                                          | 217 ms: 1.05x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 15.9 ms: 1.05x faster                                                          |
| 2to3                     | 265 ms                                                          | 254 ms: 1.05x faster                                                           |
| json_loads               | 22.4 us                                                         | 21.6 us: 1.04x faster                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 43.7 ms: 1.02x faster                                                          |
| docutils                 | 1.95 sec                                                        | 1.92 sec: 1.02x faster                                                         |
| sympy_expand             | 391 ms                                                          | 385 ms: 1.01x faster                                                           |
| coroutines               | 17.9 ms                                                         | 17.8 ms: 1.01x faster                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.9 sec: 1.01x faster                                                         |
| xml_etree_generate       | 61.6 ms                                                         | 62.1 ms: 1.01x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 82.3 ms: 1.01x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.0 ms: 1.01x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.40 us: 1.01x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.05 us: 1.02x slower                                                          |
| sqlglot_normalize        | 230 ms                                                          | 236 ms: 1.02x slower                                                           |
| python_startup_no_site   | 18.1 ms                                                         | 19.1 ms: 1.06x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 22.6 ms: 1.08x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 756 us: 1.09x slower                                                           |
| coverage                 | 46.6 ms                                                         | 51.1 ms: 1.10x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 73.6 ms: 1.11x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.43 ms: 1.12x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.90 ms: 1.14x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 53.2 ms: 1.14x slower                                                          |
| telco                    | 4.83 ms                                                         | 5.64 ms: 1.17x slower                                                          |
| async_generators         | 241 ms                                                          | 308 ms: 1.28x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.22x faster                                                                   |

Benchmark hidden because not significant (2): json, python_startup
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (4) of results/bm-20240714-3.14.0a0-d19b26c-JIT/bm-20240714-pythonperf1_win32-x86-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown