# Results vs. 3.10.4

- fork: python
- ref: a19bb261a327e1008f21
- machine: windows-amd64
- commit hash: a19bb26
- commit date: 2024-06-15
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 229 ms: 1.07x faster                                                        |
| chameleon      | 5.79 ms                                                     | 4.95 ms: 1.17x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.78 sec: 1.08x faster                                                      |
| html5lib       | 51.0 ms                                                     | 37.8 ms: 1.35x faster                                                       |
| tornado_http   | 108 ms                                                      | 85.7 ms: 1.26x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 228 ms: 1.91x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 276 ms: 1.91x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 603 ms: 1.84x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 397 ms: 1.61x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.81x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.5 ms: 1.42x faster                                                       |
| nbody          | 71.3 ms                                                     | 51.4 ms: 1.39x faster                                                       |
| Geometric mean | (ref)                                                       | 1.25x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 88.9 ms: 1.19x faster                                                       |
| regex_dna      | 136 ms                                                      | 119 ms: 1.15x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.05x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 22.7 ms: 1.47x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.69 ms: 1.61x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 172 us: 1.57x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 125 us: 1.46x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.21 sec: 1.38x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 36.6 ms: 1.21x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 51.3 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 60.6 ms: 1.07x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 91.7 ms: 1.06x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.98 us: 1.01x faster                                                       |
| json_loads           | 14.0 us                                                     | 13.9 us: 1.01x faster                                                       |
| pickle_dict          | 17.2 us                                                     | 17.5 us: 1.02x slower                                                       |
| pickle_list          | 2.75 us                                                     | 2.86 us: 1.04x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 2.85 us: 1.05x slower                                                       |
| pickle               | 6.85 us                                                     | 7.28 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 22.0 ms: 1.07x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.18 ms: 1.74x faster                                                       |
| django_template | 28.9 ms                                                     | 25.4 ms: 1.14x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 18.0 ms: 1.10x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 44.6 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 110 us: 3.05x faster                                                        |
| async_tree_none          | 435 ms                                                      | 228 ms: 1.91x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 276 ms: 1.91x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 603 ms: 1.84x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.36 ms: 1.77x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.18 ms: 1.74x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 45.1 ms: 1.71x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 55.6 ns: 1.70x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.2 us: 1.62x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.69 ms: 1.61x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 397 ms: 1.61x faster                                                        |
| richards_super           | 52.2 ms                                                     | 33.0 ms: 1.58x faster                                                       |
| pyflate                  | 409 ms                                                      | 259 ms: 1.58x faster                                                        |
| chaos                    | 61.7 ms                                                     | 39.2 ms: 1.58x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 172 us: 1.57x faster                                                        |
| raytrace                 | 273 ms                                                      | 175 ms: 1.56x faster                                                        |
| asyncio_tcp              | 732 ms                                                      | 471 ms: 1.55x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 41.0 ms: 1.53x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 809 us: 1.50x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 38.2 ms: 1.50x faster                                                       |
| go                       | 139 ms                                                      | 93.2 ms: 1.49x faster                                                       |
| pylint                   | 350 ms                                                      | 236 ms: 1.49x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 125 us: 1.46x faster                                                        |
| richards                 | 42.4 ms                                                     | 29.1 ms: 1.46x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.45 sec: 1.46x faster                                                      |
| generators               | 32.4 ms                                                     | 22.5 ms: 1.44x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 20.1 us: 1.43x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.04 ms: 1.42x faster                                                       |
| float                    | 61.7 ms                                                     | 43.5 ms: 1.42x faster                                                       |
| nbody                    | 71.3 ms                                                     | 51.4 ms: 1.39x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.21 sec: 1.38x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 37.8 ms: 1.35x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 929 ms: 1.31x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.36 sec: 1.31x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 452 ms: 1.31x faster                                                        |
| scimark_sor              | 106 ms                                                      | 82.7 ms: 1.28x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.14 ms: 1.27x faster                                                       |
| tornado_http             | 108 ms                                                      | 85.7 ms: 1.26x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 40.7 ms: 1.24x faster                                                       |
| scimark_fft              | 187 ms                                                      | 152 ms: 1.24x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 69.6 ms: 1.23x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.68 ms: 1.23x faster                                                       |
| pycparser                | 930 ms                                                      | 764 ms: 1.22x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 36.6 ms: 1.21x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 792 us: 1.21x faster                                                        |
| regex_compile            | 106 ms                                                      | 88.9 ms: 1.19x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.5 ms: 1.18x faster                                                       |
| chameleon                | 5.79 ms                                                     | 4.95 ms: 1.17x faster                                                       |
| regex_dna                | 136 ms                                                      | 119 ms: 1.15x faster                                                        |
| sympy_sum                | 107 ms                                                      | 93.6 ms: 1.14x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.4 ms: 1.14x faster                                                       |
| fannkuch                 | 256 ms                                                      | 226 ms: 1.13x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 18.0 ms: 1.10x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 60.5 ms: 1.10x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.19 us: 1.09x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 14.1 ms: 1.09x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 51.3 ms: 1.08x faster                                                       |
| json                     | 3.14 ms                                                     | 2.90 ms: 1.08x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.78 sec: 1.08x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 36.9 ms: 1.08x faster                                                       |
| sympy_str                | 194 ms                                                      | 180 ms: 1.08x faster                                                        |
| logging_simple           | 6.22 us                                                     | 5.77 us: 1.08x faster                                                       |
| deepcopy                 | 255 us                                                      | 237 us: 1.08x faster                                                        |
| 2to3                     | 246 ms                                                      | 229 ms: 1.07x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 60.6 ms: 1.07x faster                                                       |
| aiohttp                  | 995 us                                                      | 932 us: 1.07x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 2.08 us: 1.06x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 91.7 ms: 1.06x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.05x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 74.1 ms: 1.02x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.98 us: 1.01x faster                                                       |
| json_loads               | 14.0 us                                                     | 13.9 us: 1.01x faster                                                       |
| flaskblogging            | 2.03 sec                                                    | 2.04 sec: 1.00x slower                                                      |
| sympy_expand             | 314 ms                                                      | 316 ms: 1.00x slower                                                        |
| pickle_dict              | 17.2 us                                                     | 17.5 us: 1.02x slower                                                       |
| pickle_list              | 2.75 us                                                     | 2.86 us: 1.04x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.85 us: 1.05x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.28 us: 1.06x slower                                                       |
| python_startup           | 20.6 ms                                                     | 22.0 ms: 1.07x slower                                                       |
| genshi_xml               | 41.0 ms                                                     | 44.6 ms: 1.09x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 68.9 ms: 1.11x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.57 ms: 1.11x slower                                                       |
| async_generators         | 222 ms                                                      | 250 ms: 1.13x slower                                                        |
| coverage                 | 39.0 ms                                                     | 44.5 ms: 1.14x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 917 us: 1.15x slower                                                        |
| python_startup_no_site   | 15.5 ms                                                     | 17.8 ms: 1.15x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.56 ms: 1.16x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 22.7 ms: 1.47x slower                                                       |
| thrift                   | 617 us                                                      | 8.96 ms: 14.51x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.19x faster                                                                |

Benchmark hidden because not significant (2): pidigits, pathlib
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (4) of results/bm-20240615-3.13.0b2+-a19bb26-JIT/bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown