# Results vs. 3.10.4

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: linux-x86_64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.09x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 346 ms: 1.01x faster                                                         |
| chameleon      | 9.44 ms                                                      | 8.73 ms: 1.08x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.48 sec: 1.02x slower                                                       |
| html5lib       | 94.6 ms                                                      | 89.0 ms: 1.06x faster                                                        |
| tornado_http   | 157 ms                                                       | 130 ms: 1.21x faster                                                         |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 921 ms: 1.74x faster                                                         |
| async_tree_none         | 692 ms                                                       | 402 ms: 1.72x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 480 ms: 1.71x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 656 ms: 1.43x faster                                                         |
| Geometric mean          | (ref)                                                        | 1.64x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 97.4 ms: 1.14x faster                                                        |
| nbody          | 134 ms                                                       | 125 ms: 1.07x faster                                                         |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 261 ms                                                       | 247 ms: 1.06x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 26.5 ms: 1.03x faster                                                        |
| regex_compile  | 190 ms                                                       | 216 ms: 1.14x slower                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.63 ms: 1.18x slower                                                        |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 14.5 ms                                                      | 11.4 ms: 1.28x faster                                                        |
| json_loads           | 30.3 us                                                      | 24.4 us: 1.24x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 69.0 ms: 1.10x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 148 ms: 1.08x faster                                                         |
| pickle_pure_python   | 455 us                                                       | 434 us: 1.05x faster                                                         |
| unpickle_pure_python | 312 us                                                       | 305 us: 1.02x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.94 sec: 1.01x slower                                                       |
| unpickle_list        | 4.65 us                                                      | 4.81 us: 1.03x slower                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 115 ms: 1.04x slower                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 96.7 ms: 1.05x slower                                                        |
| pickle_list          | 4.12 us                                                      | 4.49 us: 1.09x slower                                                        |
| pickle               | 9.89 us                                                      | 10.8 us: 1.09x slower                                                        |
| unpickle             | 13.5 us                                                      | 15.0 us: 1.11x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 32.9 us: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                        |
| python_startup_no_site | 7.33 ms                                                      | 8.92 ms: 1.22x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 46.4 ms: 1.08x faster                                                        |
| mako            | 14.7 ms                                                      | 14.5 ms: 1.01x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 33.3 ms: 1.06x slower                                                        |
| genshi_xml      | 63.3 ms                                                      | 70.3 ms: 1.11x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 199 us: 2.70x faster                                                         |
| asyncio_tcp              | 779 ms                                                       | 389 ms: 2.01x faster                                                         |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.60 sec: 1.93x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 921 ms: 1.74x faster                                                         |
| async_tree_none          | 692 ms                                                       | 402 ms: 1.72x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 480 ms: 1.71x faster                                                         |
| generators               | 57.3 ms                                                      | 34.3 ms: 1.67x faster                                                        |
| deltablue                | 7.50 ms                                                      | 4.60 ms: 1.63x faster                                                        |
| raytrace                 | 489 ms                                                       | 333 ms: 1.47x faster                                                         |
| pylint                   | 566 ms                                                       | 396 ms: 1.43x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 656 ms: 1.43x faster                                                         |
| chaos                    | 109 ms                                                       | 81.1 ms: 1.34x faster                                                        |
| coroutines               | 30.3 ms                                                      | 23.0 ms: 1.32x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.84 us: 1.30x faster                                                        |
| thrift                   | 1.18 ms                                                      | 907 us: 1.30x faster                                                         |
| richards_super           | 90.6 ms                                                      | 70.1 ms: 1.29x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.73 ms: 1.29x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.48 us: 1.29x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 92.6 ms: 1.29x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.4 ms: 1.28x faster                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 5.00 ms: 1.28x faster                                                        |
| go                       | 262 ms                                                       | 206 ms: 1.27x faster                                                         |
| json_loads               | 30.3 us                                                      | 24.4 us: 1.24x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 2.19 ms: 1.22x faster                                                        |
| tornado_http             | 157 ms                                                       | 130 ms: 1.21x faster                                                         |
| richards                 | 75.1 ms                                                      | 62.3 ms: 1.21x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 18.4 ms: 1.16x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.46 sec: 1.15x faster                                                       |
| float                    | 111 ms                                                       | 97.4 ms: 1.14x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 1.01 ms: 1.13x faster                                                        |
| scimark_lu               | 167 ms                                                       | 149 ms: 1.12x faster                                                         |
| pyflate                  | 733 ms                                                       | 654 ms: 1.12x faster                                                         |
| dask                     | 472 ms                                                       | 426 ms: 1.11x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 69.0 ms: 1.10x faster                                                        |
| scimark_sor              | 180 ms                                                       | 165 ms: 1.10x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.77 sec: 1.08x faster                                                       |
| django_template          | 50.2 ms                                                      | 46.4 ms: 1.08x faster                                                        |
| chameleon                | 9.44 ms                                                      | 8.73 ms: 1.08x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 148 ms: 1.08x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 99.5 ms: 1.08x faster                                                        |
| logging_silent           | 167 ns                                                       | 155 ns: 1.08x faster                                                         |
| async_generators         | 421 ms                                                       | 391 ms: 1.08x faster                                                         |
| nbody                    | 134 ms                                                       | 125 ms: 1.07x faster                                                         |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                         |
| html5lib                 | 94.6 ms                                                      | 89.0 ms: 1.06x faster                                                        |
| regex_dna                | 261 ms                                                       | 247 ms: 1.06x faster                                                         |
| json                     | 5.86 ms                                                      | 5.57 ms: 1.05x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 434 us: 1.05x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.87 us: 1.04x faster                                                        |
| mypy2                    | 933 ms                                                       | 908 ms: 1.03x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 26.5 ms: 1.03x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 305 us: 1.02x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 2.12 sec: 1.02x faster                                                       |
| sympy_sum                | 193 ms                                                       | 189 ms: 1.02x faster                                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 1.03 sec: 1.02x faster                                                       |
| 2to3                     | 350 ms                                                       | 346 ms: 1.01x faster                                                         |
| mako                     | 14.7 ms                                                      | 14.5 ms: 1.01x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 80.2 ms: 1.01x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 144 ms: 1.00x slower                                                         |
| tomli_loads              | 2.92 sec                                                     | 2.94 sec: 1.01x slower                                                       |
| fannkuch                 | 483 ms                                                       | 490 ms: 1.02x slower                                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 71.5 ms: 1.02x slower                                                        |
| docutils                 | 3.41 sec                                                     | 3.48 sec: 1.02x slower                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 4.10 us: 1.02x slower                                                        |
| deepcopy                 | 468 us                                                       | 483 us: 1.03x slower                                                         |
| sympy_str                | 360 ms                                                       | 372 ms: 1.03x slower                                                         |
| unpickle_list            | 4.65 us                                                      | 4.81 us: 1.03x slower                                                        |
| comprehensions           | 26.7 us                                                      | 27.8 us: 1.04x slower                                                        |
| meteor_contest           | 138 ms                                                       | 144 ms: 1.04x slower                                                         |
| sympy_expand             | 600 ms                                                       | 625 ms: 1.04x slower                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 115 ms: 1.04x slower                                                         |
| xml_etree_generate       | 92.3 ms                                                      | 96.7 ms: 1.05x slower                                                        |
| nqueens                  | 115 ms                                                       | 120 ms: 1.05x slower                                                         |
| genshi_text              | 31.4 ms                                                      | 33.3 ms: 1.06x slower                                                        |
| spectral_norm            | 139 ms                                                       | 149 ms: 1.07x slower                                                         |
| pickle_list              | 4.12 us                                                      | 4.49 us: 1.09x slower                                                        |
| pickle                   | 9.89 us                                                      | 10.8 us: 1.09x slower                                                        |
| genshi_xml               | 63.3 ms                                                      | 70.3 ms: 1.11x slower                                                        |
| unpickle                 | 13.5 us                                                      | 15.0 us: 1.11x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 32.9 us: 1.12x slower                                                        |
| flaskblogging            | 4.39 ms                                                      | 4.97 ms: 1.13x slower                                                        |
| regex_compile            | 190 ms                                                       | 216 ms: 1.14x slower                                                         |
| hexiom                   | 9.42 ms                                                      | 10.7 ms: 1.14x slower                                                        |
| python_startup           | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.07 ms: 1.17x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.63 ms: 1.18x slower                                                        |
| scimark_fft              | 361 ms                                                       | 425 ms: 1.18x slower                                                         |
| deepcopy_memo            | 49.8 us                                                      | 58.6 us: 1.18x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 8.92 ms: 1.22x slower                                                        |
| coverage                 | 63.3 ms                                                      | 79.5 ms: 1.26x slower                                                        |
| telco                    | 7.23 ms                                                      | 9.17 ms: 1.27x slower                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 6.60 ms: 1.30x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 4.70 ms: 1.38x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.09x faster                                                                 |

Benchmark hidden because not significant (4): asyncio_websockets, sympy_integrate, aiohttp, gunicorn
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240604-3.13.0b1+-6725c78-PYTHON_UOPS/bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.14x