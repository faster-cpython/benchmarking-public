# Results vs. 3.10.4

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-x86_64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 309 ms: 1.13x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.16 sec: 1.08x faster                                                      |
| html5lib       | 94.6 ms                                                      | 71.3 ms: 1.33x faster                                                       |
| tornado_http   | 157 ms                                                       | 121 ms: 1.30x faster                                                        |
| Geometric mean | (ref)                                                        | 1.20x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 319 ms: 2.17x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 401 ms: 2.04x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 805 ms: 1.99x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 571 ms: 1.64x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.95x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 78.7 ms: 1.70x faster                                                       |
| float          | 111 ms                                                       | 74.2 ms: 1.50x faster                                                       |
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.40x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 146 ms: 1.30x faster                                                        |
| regex_dna      | 261 ms                                                       | 237 ms: 1.10x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.61 ms: 1.17x slower                                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 214 us: 1.46x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.09 sec: 1.40x faster                                                      |
| pickle_pure_python   | 455 us                                                       | 326 us: 1.39x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 55.8 ms: 1.36x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 10.8 ms: 1.35x faster                                                       |
| json_loads           | 30.3 us                                                      | 24.5 us: 1.24x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 78.5 ms: 1.18x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 97.4 ms: 1.13x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 142 ms: 1.12x faster                                                        |
| unpickle_list        | 4.65 us                                                      | 4.69 us: 1.01x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.22 us: 1.02x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 30.7 us: 1.04x slower                                                       |
| pickle               | 9.89 us                                                      | 10.4 us: 1.05x slower                                                       |
| unpickle             | 13.5 us                                                      | 15.2 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.16x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 8.93 ms: 1.22x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.18 ms: 1.60x faster                                                       |
| django_template | 50.2 ms                                                      | 41.6 ms: 1.21x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 29.3 ms: 1.07x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 66.1 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.19x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 186 us: 2.88x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.23 ms: 2.32x faster                                                       |
| async_tree_none          | 692 ms                                                       | 319 ms: 2.17x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 376 ms: 2.07x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 401 ms: 2.04x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 805 ms: 1.99x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| deepcopy_memo            | 49.8 us                                                      | 26.5 us: 1.88x faster                                                       |
| go                       | 262 ms                                                       | 150 ms: 1.75x faster                                                        |
| scimark_sor              | 180 ms                                                       | 103 ms: 1.74x faster                                                        |
| richards_super           | 90.6 ms                                                      | 52.4 ms: 1.73x faster                                                       |
| scimark_lu               | 167 ms                                                       | 97.5 ms: 1.71x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 69.7 ms: 1.71x faster                                                       |
| spectral_norm            | 139 ms                                                       | 81.4 ms: 1.71x faster                                                       |
| nbody                    | 134 ms                                                       | 78.7 ms: 1.70x faster                                                       |
| richards                 | 75.1 ms                                                      | 44.7 ms: 1.68x faster                                                       |
| chaos                    | 109 ms                                                       | 65.6 ms: 1.66x faster                                                       |
| logging_silent           | 167 ns                                                       | 101 ns: 1.65x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 571 ms: 1.64x faster                                                        |
| pyflate                  | 733 ms                                                       | 454 ms: 1.61x faster                                                        |
| deepcopy                 | 468 us                                                       | 292 us: 1.60x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 67.1 ms: 1.60x faster                                                       |
| mako                     | 14.7 ms                                                      | 9.18 ms: 1.60x faster                                                       |
| generators               | 57.3 ms                                                      | 36.5 ms: 1.57x faster                                                       |
| raytrace                 | 489 ms                                                       | 313 ms: 1.56x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.48 ms: 1.51x faster                                                       |
| float                    | 111 ms                                                       | 74.2 ms: 1.50x faster                                                       |
| comprehensions           | 26.7 us                                                      | 18.3 us: 1.46x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 214 us: 1.46x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.09 sec: 1.40x faster                                                      |
| coroutines               | 30.3 ms                                                      | 21.7 ms: 1.40x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 326 us: 1.39x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.93 ms: 1.39x faster                                                       |
| pylint                   | 566 ms                                                       | 408 ms: 1.39x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.90 us: 1.38x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 15.7 ms: 1.36x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 55.8 ms: 1.36x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.53 us: 1.36x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.95 ms: 1.36x faster                                                       |
| fannkuch                 | 483 ms                                                       | 358 ms: 1.35x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.8 ms: 1.35x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 783 ms: 1.34x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.20 us: 1.34x faster                                                       |
| thrift                   | 1.18 ms                                                      | 885 us: 1.33x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 71.3 ms: 1.33x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.63 sec: 1.32x faster                                                      |
| regex_compile            | 190 ms                                                       | 146 ms: 1.30x faster                                                        |
| tornado_http             | 157 ms                                                       | 121 ms: 1.30x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.30 sec: 1.29x faster                                                      |
| bench_mp_pool            | 6.37 ms                                                      | 5.00 ms: 1.28x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 64.6 ms: 1.26x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.06 ms: 1.25x faster                                                       |
| scimark_fft              | 361 ms                                                       | 290 ms: 1.25x faster                                                        |
| json_loads               | 30.3 us                                                      | 24.5 us: 1.24x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 922 us: 1.24x faster                                                        |
| django_template          | 50.2 ms                                                      | 41.6 ms: 1.21x faster                                                       |
| nqueens                  | 115 ms                                                       | 97.0 ms: 1.18x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 78.5 ms: 1.18x faster                                                       |
| sympy_str                | 360 ms                                                       | 308 ms: 1.17x faster                                                        |
| sympy_sum                | 193 ms                                                       | 167 ms: 1.16x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.61 sec: 1.15x faster                                                      |
| sympy_expand             | 600 ms                                                       | 525 ms: 1.14x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 97.4 ms: 1.13x faster                                                       |
| 2to3                     | 350 ms                                                       | 309 ms: 1.13x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 128 ms: 1.13x faster                                                        |
| json                     | 5.86 ms                                                      | 5.20 ms: 1.13x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 142 ms: 1.12x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.71 us: 1.10x faster                                                       |
| regex_dna                | 261 ms                                                       | 237 ms: 1.10x faster                                                        |
| async_generators         | 421 ms                                                       | 386 ms: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| meteor_contest           | 138 ms                                                       | 128 ms: 1.08x faster                                                        |
| docutils                 | 3.41 sec                                                     | 3.16 sec: 1.08x faster                                                      |
| sqlglot_optimize         | 70.1 ms                                                      | 65.0 ms: 1.08x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 29.3 ms: 1.07x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 26.3 ms: 1.07x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                       |
| unpickle_list            | 4.65 us                                                      | 4.69 us: 1.01x slower                                                       |
| asyncio_websockets       | 390 ms                                                       | 397 ms: 1.02x slower                                                        |
| pickle_list              | 4.12 us                                                      | 4.22 us: 1.02x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 30.7 us: 1.04x slower                                                       |
| genshi_xml               | 63.3 ms                                                      | 66.1 ms: 1.04x slower                                                       |
| pickle                   | 9.89 us                                                      | 10.4 us: 1.05x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.91 ms: 1.08x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.08 ms: 1.12x slower                                                       |
| unpickle                 | 13.5 us                                                      | 15.2 us: 1.13x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.61 ms: 1.17x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.93 ms: 1.22x slower                                                       |
| coverage                 | 63.3 ms                                                      | 79.4 ms: 1.25x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.36 ms: 1.28x slower                                                       |
| unpack_sequence          | 59.9 ns                                                      | 87.7 ns: 1.46x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.30x faster                                                                |
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.22x