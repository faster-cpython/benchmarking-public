# Results vs. 3.10.4

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: linux-x86_64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.27x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 305 ms: 1.15x faster                                                         |
| chameleon      | 9.44 ms                                                      | 7.60 ms: 1.24x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.11 sec: 1.10x faster                                                       |
| html5lib       | 94.6 ms                                                      | 73.7 ms: 1.28x faster                                                        |
| tornado_http   | 157 ms                                                       | 123 ms: 1.27x faster                                                         |
| Geometric mean | (ref)                                                        | 1.21x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 379 ms: 1.82x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 451 ms: 1.82x faster                                                         |
| async_tree_io           | 1.60 sec                                                     | 907 ms: 1.76x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 633 ms: 1.48x faster                                                         |
| Geometric mean          | (ref)                                                        | 1.71x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 81.9 ms: 1.64x faster                                                        |
| float          | 111 ms                                                       | 76.2 ms: 1.46x faster                                                        |
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.37x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 138 ms: 1.38x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 24.9 ms: 1.09x faster                                                        |
| regex_dna      | 261 ms                                                       | 243 ms: 1.07x faster                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.70 ms: 1.20x slower                                                        |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 314 us: 1.45x faster                                                         |
| unpickle_pure_python | 312 us                                                       | 217 us: 1.44x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.09 sec: 1.40x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 10.6 ms: 1.38x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 58.5 ms: 1.30x faster                                                        |
| json_loads           | 30.3 us                                                      | 24.7 us: 1.23x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 81.4 ms: 1.13x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 100.0 ms: 1.11x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 145 ms: 1.10x faster                                                         |
| unpickle_list        | 4.65 us                                                      | 4.81 us: 1.04x slower                                                        |
| pickle               | 9.89 us                                                      | 10.5 us: 1.07x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 31.8 us: 1.08x slower                                                        |
| pickle_list          | 4.12 us                                                      | 4.56 us: 1.11x slower                                                        |
| unpickle             | 13.5 us                                                      | 15.6 us: 1.16x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.8 ms: 1.20x slower                                                        |
| python_startup_no_site | 7.33 ms                                                      | 9.44 ms: 1.29x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.24x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.02 ms: 1.63x faster                                                        |
| django_template | 50.2 ms                                                      | 41.3 ms: 1.21x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 27.6 ms: 1.14x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 64.8 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.22x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 180 us: 2.98x faster                                                         |
| asyncio_tcp              | 779 ms                                                       | 379 ms: 2.06x faster                                                         |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                       |
| deltablue                | 7.50 ms                                                      | 3.84 ms: 1.95x faster                                                        |
| async_tree_none          | 692 ms                                                       | 379 ms: 1.82x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 451 ms: 1.82x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 907 ms: 1.76x faster                                                         |
| richards_super           | 90.6 ms                                                      | 52.6 ms: 1.72x faster                                                        |
| raytrace                 | 489 ms                                                       | 287 ms: 1.71x faster                                                         |
| crypto_pyaes             | 119 ms                                                       | 69.9 ms: 1.71x faster                                                        |
| spectral_norm            | 139 ms                                                       | 82.1 ms: 1.69x faster                                                        |
| chaos                    | 109 ms                                                       | 64.7 ms: 1.68x faster                                                        |
| generators               | 57.3 ms                                                      | 34.2 ms: 1.68x faster                                                        |
| logging_silent           | 167 ns                                                       | 101 ns: 1.66x faster                                                         |
| richards                 | 75.1 ms                                                      | 45.7 ms: 1.64x faster                                                        |
| nbody                    | 134 ms                                                       | 81.9 ms: 1.64x faster                                                        |
| mako                     | 14.7 ms                                                      | 9.02 ms: 1.63x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 66.7 ms: 1.61x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.40 ms: 1.60x faster                                                        |
| go                       | 262 ms                                                       | 166 ms: 1.58x faster                                                         |
| pyflate                  | 733 ms                                                       | 468 ms: 1.57x faster                                                         |
| pylint                   | 566 ms                                                       | 376 ms: 1.51x faster                                                         |
| comprehensions           | 26.7 us                                                      | 18.0 us: 1.48x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 633 ms: 1.48x faster                                                         |
| sqlglot_transpile        | 2.68 ms                                                      | 1.81 ms: 1.48x faster                                                        |
| scimark_lu               | 167 ms                                                       | 113 ms: 1.48x faster                                                         |
| float                    | 111 ms                                                       | 76.2 ms: 1.46x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 314 us: 1.45x faster                                                         |
| unpickle_pure_python     | 312 us                                                       | 217 us: 1.44x faster                                                         |
| fannkuch                 | 483 ms                                                       | 335 ms: 1.44x faster                                                         |
| hexiom                   | 9.42 ms                                                      | 6.70 ms: 1.41x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.09 sec: 1.40x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 10.6 ms: 1.38x faster                                                        |
| regex_compile            | 190 ms                                                       | 138 ms: 1.38x faster                                                         |
| logging_format           | 9.64 us                                                      | 7.06 us: 1.37x faster                                                        |
| coroutines               | 30.3 ms                                                      | 22.2 ms: 1.36x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.52 us: 1.36x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 36.5 us: 1.36x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.59 sec: 1.35x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 784 ms: 1.34x faster                                                         |
| bench_mp_pool            | 6.37 ms                                                      | 4.82 ms: 1.32x faster                                                        |
| thrift                   | 1.18 ms                                                      | 902 us: 1.30x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 58.5 ms: 1.30x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 73.7 ms: 1.28x faster                                                        |
| tornado_http             | 157 ms                                                       | 123 ms: 1.27x faster                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.01 ms: 1.27x faster                                                        |
| scimark_fft              | 361 ms                                                       | 287 ms: 1.26x faster                                                         |
| scimark_sor              | 180 ms                                                       | 144 ms: 1.25x faster                                                         |
| chameleon                | 9.44 ms                                                      | 7.60 ms: 1.24x faster                                                        |
| json_loads               | 30.3 us                                                      | 24.7 us: 1.23x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 17.5 ms: 1.22x faster                                                        |
| django_template          | 50.2 ms                                                      | 41.3 ms: 1.21x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 66.9 ms: 1.21x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 948 us: 1.20x faster                                                         |
| nqueens                  | 115 ms                                                       | 96.9 ms: 1.19x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.55 sec: 1.18x faster                                                       |
| sympy_sum                | 193 ms                                                       | 164 ms: 1.17x faster                                                         |
| sympy_str                | 360 ms                                                       | 309 ms: 1.17x faster                                                         |
| dask                     | 472 ms                                                       | 405 ms: 1.17x faster                                                         |
| deepcopy                 | 468 us                                                       | 405 us: 1.16x faster                                                         |
| 2to3                     | 350 ms                                                       | 305 ms: 1.15x faster                                                         |
| sympy_expand             | 600 ms                                                       | 525 ms: 1.14x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 27.6 ms: 1.14x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 81.4 ms: 1.13x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 129 ms: 1.12x faster                                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 62.9 ms: 1.12x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 25.4 ms: 1.11x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 3.62 us: 1.11x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 100.0 ms: 1.11x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 145 ms: 1.10x faster                                                         |
| mypy2                    | 933 ms                                                       | 846 ms: 1.10x faster                                                         |
| docutils                 | 3.41 sec                                                     | 3.11 sec: 1.10x faster                                                       |
| async_generators         | 421 ms                                                       | 384 ms: 1.10x faster                                                         |
| json                     | 5.86 ms                                                      | 5.35 ms: 1.10x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 24.9 ms: 1.09x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.74 us: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 250 ms: 1.08x faster                                                         |
| regex_dna                | 261 ms                                                       | 243 ms: 1.07x faster                                                         |
| meteor_contest           | 138 ms                                                       | 130 ms: 1.06x faster                                                         |
| gunicorn                 | 1.16 ms                                                      | 1.13 ms: 1.02x faster                                                        |
| aiohttp                  | 1.19 ms                                                      | 1.17 ms: 1.02x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 64.8 ms: 1.02x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 4.81 us: 1.04x slower                                                        |
| pickle                   | 9.89 us                                                      | 10.5 us: 1.07x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 31.8 us: 1.08x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 1.95 ms: 1.10x slower                                                        |
| pickle_list              | 4.12 us                                                      | 4.56 us: 1.11x slower                                                        |
| flaskblogging            | 4.39 ms                                                      | 4.91 ms: 1.12x slower                                                        |
| telco                    | 7.23 ms                                                      | 8.22 ms: 1.14x slower                                                        |
| unpickle                 | 13.5 us                                                      | 15.6 us: 1.16x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.70 ms: 1.20x slower                                                        |
| python_startup           | 11.5 ms                                                      | 13.8 ms: 1.20x slower                                                        |
| coverage                 | 63.3 ms                                                      | 81.2 ms: 1.28x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.44 ms: 1.29x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 4.91 ms: 1.44x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.27x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240604-3.13.0b1+-6725c78-JIT/bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.23x