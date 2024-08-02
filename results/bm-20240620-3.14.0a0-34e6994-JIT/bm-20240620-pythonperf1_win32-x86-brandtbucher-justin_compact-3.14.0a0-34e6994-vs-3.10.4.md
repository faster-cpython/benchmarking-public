# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_compact
- machine: windows-x86
- commit hash: 34e6994
- commit date: 2024-06-20
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 257 ms: 1.03x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.93 sec: 1.01x faster                                                         |
| html5lib       | 52.1 ms                                                         | 48.6 ms: 1.07x faster                                                          |
| tornado_http   | 118 ms                                                          | 97.8 ms: 1.20x faster                                                          |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 498 ms: 1.85x faster                                                           |
| async_tree_io           | 940 ms                                                          | 559 ms: 1.68x faster                                                           |
| async_tree_none         | 394 ms                                                          | 242 ms: 1.63x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 295 ms: 1.58x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.68x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 195 ms: 2.57x faster                                                           |
| float          | 69.6 ms                                                         | 43.1 ms: 1.62x faster                                                          |
| nbody          | 79.1 ms                                                         | 54.4 ms: 1.45x faster                                                          |
| Geometric mean | (ref)                                                           | 1.82x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 93.6 ms: 1.25x faster                                                          |
| regex_dna      | 131 ms                                                          | 129 ms: 1.01x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.0 ms: 1.01x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 2.07 ms: 1.25x slower                                                          |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.87 ms: 1.43x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 211 us: 1.33x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 146 us: 1.30x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.50 sec: 1.27x faster                                                         |
| xml_etree_parse      | 120 ms                                                          | 104 ms: 1.15x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 61.9 ms: 1.14x faster                                                          |
| xml_etree_process    | 48.1 ms                                                         | 42.8 ms: 1.12x faster                                                          |
| json_loads           | 22.4 us                                                         | 20.7 us: 1.08x faster                                                          |
| unpickle_list        | 2.98 us                                                         | 2.78 us: 1.07x faster                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 57.8 ms: 1.07x faster                                                          |
| unpickle             | 9.82 us                                                         | 10.3 us: 1.05x slower                                                          |
| pickle               | 7.83 us                                                         | 8.28 us: 1.06x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 20.8 us: 1.14x slower                                                          |
| pickle_list          | 3.22 us                                                         | 4.10 us: 1.27x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 25.1 ms: 1.09x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 21.0 ms: 1.16x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.34 ms: 1.70x faster                                                          |
| django_template | 36.0 ms                                                         | 34.1 ms: 1.06x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 21.4 ms: 1.02x slower                                                          |
| genshi_xml      | 46.6 ms                                                         | 51.0 ms: 1.09x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.13x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 148 us: 2.68x faster                                                           |
| pidigits                 | 502 ms                                                          | 195 ms: 2.57x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 15.8 us: 1.87x faster                                                          |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 498 ms: 1.85x faster                                                           |
| mako                     | 9.10 ms                                                         | 5.34 ms: 1.70x faster                                                          |
| async_tree_io            | 940 ms                                                          | 559 ms: 1.68x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 58.3 ns: 1.68x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 48.5 ms: 1.67x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 49.0 ms: 1.64x faster                                                          |
| async_tree_none          | 394 ms                                                          | 242 ms: 1.63x faster                                                           |
| float                    | 69.6 ms                                                         | 43.1 ms: 1.62x faster                                                          |
| async_tree_memoization   | 467 ms                                                          | 295 ms: 1.58x faster                                                           |
| pylint                   | 384 ms                                                          | 244 ms: 1.57x faster                                                           |
| comprehensions           | 17.7 us                                                         | 11.4 us: 1.55x faster                                                          |
| pyflate                  | 422 ms                                                          | 277 ms: 1.52x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 41.2 ms: 1.50x faster                                                          |
| fannkuch                 | 317 ms                                                          | 213 ms: 1.49x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.78 ms: 1.45x faster                                                          |
| nbody                    | 79.1 ms                                                         | 54.4 ms: 1.45x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 922 us: 1.44x faster                                                           |
| json_dumps               | 9.82 ms                                                         | 6.87 ms: 1.43x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 4.32 ms: 1.42x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.19 ms: 1.33x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 211 us: 1.33x faster                                                           |
| chaos                    | 74.4 ms                                                         | 56.1 ms: 1.33x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.48 ms: 1.31x faster                                                          |
| deepcopy                 | 310 us                                                          | 238 us: 1.30x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 146 us: 1.30x faster                                                           |
| go                       | 146 ms                                                          | 114 ms: 1.28x faster                                                           |
| tomli_loads              | 1.91 sec                                                        | 1.50 sec: 1.27x faster                                                         |
| scimark_fft              | 216 ms                                                          | 170 ms: 1.27x faster                                                           |
| richards_super           | 49.9 ms                                                         | 39.3 ms: 1.27x faster                                                          |
| raytrace                 | 303 ms                                                          | 241 ms: 1.26x faster                                                           |
| pycparser                | 1.04 sec                                                        | 831 ms: 1.25x faster                                                           |
| regex_compile            | 117 ms                                                          | 93.6 ms: 1.25x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 71.2 ms: 1.22x faster                                                          |
| tornado_http             | 118 ms                                                          | 97.8 ms: 1.20x faster                                                          |
| sqlite_synth             | 2.29 us                                                         | 1.92 us: 1.20x faster                                                          |
| thrift                   | 902 us                                                          | 756 us: 1.19x faster                                                           |
| asyncio_tcp              | 744 ms                                                          | 629 ms: 1.18x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 75.9 ms: 1.18x faster                                                          |
| scimark_sor              | 115 ms                                                          | 99.5 ms: 1.16x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 104 ms: 1.15x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 976 us: 1.15x faster                                                           |
| richards                 | 40.3 ms                                                         | 35.2 ms: 1.14x faster                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 61.9 ms: 1.14x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.35 us: 1.14x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.20 sec: 1.14x faster                                                         |
| generators               | 31.6 ms                                                         | 27.7 ms: 1.14x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 584 ms: 1.13x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 42.8 ms: 1.12x faster                                                          |
| sympy_sum                | 122 ms                                                          | 109 ms: 1.12x faster                                                           |
| mdp                      | 1.83 sec                                                        | 1.64 sec: 1.11x faster                                                         |
| meteor_contest           | 80.0 ms                                                         | 73.4 ms: 1.09x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.7 us: 1.08x faster                                                          |
| unpickle_list            | 2.98 us                                                         | 2.78 us: 1.07x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 48.6 ms: 1.07x faster                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 57.8 ms: 1.07x faster                                                          |
| django_template          | 36.0 ms                                                         | 34.1 ms: 1.06x faster                                                          |
| sympy_str                | 229 ms                                                          | 217 ms: 1.05x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 16.0 ms: 1.04x faster                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 43.2 ms: 1.04x faster                                                          |
| 2to3                     | 265 ms                                                          | 257 ms: 1.03x faster                                                           |
| coroutines               | 17.9 ms                                                         | 17.5 ms: 1.02x faster                                                          |
| regex_dna                | 131 ms                                                          | 129 ms: 1.01x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.93 sec: 1.01x faster                                                         |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.9 sec: 1.01x faster                                                         |
| sympy_expand             | 391 ms                                                          | 389 ms: 1.00x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 233 ms: 1.01x slower                                                           |
| regex_v8                 | 15.8 ms                                                         | 16.0 ms: 1.01x slower                                                          |
| genshi_text              | 21.0 ms                                                         | 21.4 ms: 1.02x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 83.3 ms: 1.03x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.65 us: 1.05x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.31 us: 1.05x slower                                                          |
| unpickle                 | 9.82 us                                                         | 10.3 us: 1.05x slower                                                          |
| pickle                   | 7.83 us                                                         | 8.28 us: 1.06x slower                                                          |
| coverage                 | 46.6 ms                                                         | 49.6 ms: 1.06x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 751 us: 1.08x slower                                                           |
| python_startup           | 22.9 ms                                                         | 25.1 ms: 1.09x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 51.0 ms: 1.09x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 20.8 us: 1.14x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.46 ms: 1.14x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 76.1 ms: 1.15x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 21.0 ms: 1.16x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 2.07 ms: 1.25x slower                                                          |
| telco                    | 4.83 ms                                                         | 6.04 ms: 1.25x slower                                                          |
| async_generators         | 241 ms                                                          | 305 ms: 1.26x slower                                                           |
| pickle_list              | 3.22 us                                                         | 4.10 us: 1.27x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.19x faster                                                                   |

Benchmark hidden because not significant (1): json
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240620-3.14.0a0-34e6994-JIT/bm-20240620-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-34e6994.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown