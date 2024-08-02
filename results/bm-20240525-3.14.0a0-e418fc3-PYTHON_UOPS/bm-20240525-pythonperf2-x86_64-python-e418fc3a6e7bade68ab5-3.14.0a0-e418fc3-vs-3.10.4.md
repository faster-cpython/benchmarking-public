# Results vs. 3.10.4

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-x86_64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.10x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 343 ms: 1.02x faster                                                        |
| chameleon      | 9.44 ms                                                      | 8.74 ms: 1.08x faster                                                       |
| docutils       | 3.41 sec                                                     | 3.45 sec: 1.01x slower                                                      |
| html5lib       | 94.6 ms                                                      | 87.5 ms: 1.08x faster                                                       |
| tornado_http   | 157 ms                                                       | 130 ms: 1.20x faster                                                        |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 396 ms: 1.75x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 935 ms: 1.71x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 496 ms: 1.65x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 645 ms: 1.45x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.64x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 97.3 ms: 1.14x faster                                                       |
| nbody          | 134 ms                                                       | 124 ms: 1.09x faster                                                        |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 261 ms                                                       | 241 ms: 1.08x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 26.4 ms: 1.03x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.49 ms: 1.13x slower                                                       |
| regex_compile  | 190 ms                                                       | 215 ms: 1.13x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 14.5 ms                                                      | 11.3 ms: 1.28x faster                                                       |
| json_loads           | 30.3 us                                                      | 24.9 us: 1.22x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 145 ms: 1.11x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 68.8 ms: 1.10x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 437 us: 1.04x faster                                                        |
| unpickle_pure_python | 312 us                                                       | 311 us: 1.00x faster                                                        |
| unpickle_list        | 4.65 us                                                      | 4.70 us: 1.01x slower                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.95 sec: 1.01x slower                                                      |
| xml_etree_iterparse  | 110 ms                                                       | 113 ms: 1.03x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 30.8 us: 1.05x slower                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 98.3 ms: 1.06x slower                                                       |
| pickle               | 9.89 us                                                      | 10.6 us: 1.08x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.65 us: 1.13x slower                                                       |
| unpickle             | 13.5 us                                                      | 15.6 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.2 ms: 1.15x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 8.93 ms: 1.22x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.18x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 45.9 ms: 1.09x faster                                                       |
| mako            | 14.7 ms                                                      | 14.0 ms: 1.05x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 33.4 ms: 1.06x slower                                                       |
| genshi_xml      | 63.3 ms                                                      | 67.9 ms: 1.07x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.00x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 204 us: 2.63x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 386 ms: 2.02x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.60 sec: 1.94x faster                                                      |
| async_tree_none          | 692 ms                                                       | 396 ms: 1.75x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 935 ms: 1.71x faster                                                        |
| generators               | 57.3 ms                                                      | 33.9 ms: 1.69x faster                                                       |
| deltablue                | 7.50 ms                                                      | 4.53 ms: 1.66x faster                                                       |
| async_tree_memoization   | 819 ms                                                       | 496 ms: 1.65x faster                                                        |
| raytrace                 | 489 ms                                                       | 323 ms: 1.51x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 645 ms: 1.45x faster                                                        |
| pylint                   | 566 ms                                                       | 396 ms: 1.43x faster                                                        |
| richards_super           | 90.6 ms                                                      | 65.9 ms: 1.37x faster                                                       |
| chaos                    | 109 ms                                                       | 80.9 ms: 1.34x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.9 ms: 1.32x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.90 ms: 1.30x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.73 ms: 1.30x faster                                                       |
| go                       | 262 ms                                                       | 202 ms: 1.30x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.48 us: 1.29x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 11.3 ms: 1.28x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.94 us: 1.28x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 93.4 ms: 1.28x faster                                                       |
| richards                 | 75.1 ms                                                      | 58.9 ms: 1.27x faster                                                       |
| thrift                   | 1.18 ms                                                      | 925 us: 1.27x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 17.2 ms: 1.24x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 2.18 ms: 1.23x faster                                                       |
| json_loads               | 30.3 us                                                      | 24.9 us: 1.22x faster                                                       |
| tornado_http             | 157 ms                                                       | 130 ms: 1.20x faster                                                        |
| scimark_lu               | 167 ms                                                       | 142 ms: 1.18x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.45 sec: 1.15x faster                                                      |
| float                    | 111 ms                                                       | 97.3 ms: 1.14x faster                                                       |
| scimark_sor              | 180 ms                                                       | 159 ms: 1.13x faster                                                        |
| pyflate                  | 733 ms                                                       | 651 ms: 1.13x faster                                                        |
| dask                     | 472 ms                                                       | 422 ms: 1.12x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 1.02 ms: 1.11x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 145 ms: 1.11x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 68.8 ms: 1.10x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 97.8 ms: 1.10x faster                                                       |
| django_template          | 50.2 ms                                                      | 45.9 ms: 1.09x faster                                                       |
| nbody                    | 134 ms                                                       | 124 ms: 1.09x faster                                                        |
| regex_dna                | 261 ms                                                       | 241 ms: 1.08x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 87.5 ms: 1.08x faster                                                       |
| chameleon                | 9.44 ms                                                      | 8.74 ms: 1.08x faster                                                       |
| json                     | 5.86 ms                                                      | 5.46 ms: 1.07x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.81 sec: 1.07x faster                                                      |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                        |
| mako                     | 14.7 ms                                                      | 14.0 ms: 1.05x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 437 us: 1.04x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 78.0 ms: 1.04x faster                                                       |
| async_generators         | 421 ms                                                       | 404 ms: 1.04x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 2.08 sec: 1.04x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 1.02 sec: 1.03x faster                                                      |
| sqlite_synth             | 2.99 us                                                      | 2.90 us: 1.03x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 26.4 ms: 1.03x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 140 ms: 1.02x faster                                                        |
| fannkuch                 | 483 ms                                                       | 473 ms: 1.02x faster                                                        |
| 2to3                     | 350 ms                                                       | 343 ms: 1.02x faster                                                        |
| logging_silent           | 167 ns                                                       | 165 ns: 1.02x faster                                                        |
| sympy_sum                | 193 ms                                                       | 190 ms: 1.01x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 311 us: 1.00x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 70.6 ms: 1.01x slower                                                       |
| docutils                 | 3.41 sec                                                     | 3.45 sec: 1.01x slower                                                      |
| deepcopy                 | 468 us                                                       | 473 us: 1.01x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 4.70 us: 1.01x slower                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.95 sec: 1.01x slower                                                      |
| deepcopy_reduce          | 4.01 us                                                      | 4.08 us: 1.02x slower                                                       |
| comprehensions           | 26.7 us                                                      | 27.4 us: 1.03x slower                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 113 ms: 1.03x slower                                                        |
| nqueens                  | 115 ms                                                       | 118 ms: 1.03x slower                                                        |
| sympy_str                | 360 ms                                                       | 372 ms: 1.03x slower                                                        |
| meteor_contest           | 138 ms                                                       | 144 ms: 1.04x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 30.8 us: 1.05x slower                                                       |
| sympy_expand             | 600 ms                                                       | 636 ms: 1.06x slower                                                        |
| spectral_norm            | 139 ms                                                       | 148 ms: 1.06x slower                                                        |
| genshi_text              | 31.4 ms                                                      | 33.4 ms: 1.06x slower                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 98.3 ms: 1.06x slower                                                       |
| genshi_xml               | 63.3 ms                                                      | 67.9 ms: 1.07x slower                                                       |
| pickle                   | 9.89 us                                                      | 10.6 us: 1.08x slower                                                       |
| hexiom                   | 9.42 ms                                                      | 10.4 ms: 1.11x slower                                                       |
| flaskblogging            | 4.39 ms                                                      | 4.92 ms: 1.12x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.49 ms: 1.13x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.65 us: 1.13x slower                                                       |
| regex_compile            | 190 ms                                                       | 215 ms: 1.13x slower                                                        |
| python_startup           | 11.5 ms                                                      | 13.2 ms: 1.15x slower                                                       |
| unpickle                 | 13.5 us                                                      | 15.6 us: 1.15x slower                                                       |
| deepcopy_memo            | 49.8 us                                                      | 57.8 us: 1.16x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.05 ms: 1.16x slower                                                       |
| scimark_fft              | 361 ms                                                       | 428 ms: 1.19x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 8.93 ms: 1.22x slower                                                       |
| telco                    | 7.23 ms                                                      | 9.20 ms: 1.27x slower                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 6.49 ms: 1.28x slower                                                       |
| coverage                 | 63.3 ms                                                      | 82.4 ms: 1.30x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.51 ms: 1.32x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.10x faster                                                                |

Benchmark hidden because not significant (2): sympy_integrate, asyncio_websockets
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240525-3.14.0a0-e418fc3-PYTHON_UOPS/bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.13x