# Results vs. 3.10.4

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-x86_64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.09x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.05x slower
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 424 ms: 1.21x slower                                                        |
| docutils       | 3.41 sec                                                     | 3.37 sec: 1.01x faster                                                      |
| html5lib       | 94.6 ms                                                      | 105 ms: 1.11x slower                                                        |
| tornado_http   | 157 ms                                                       | 166 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 928 ms: 1.72x faster                                                        |
| async_tree_none         | 692 ms                                                       | 411 ms: 1.68x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 511 ms: 1.60x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 673 ms: 1.39x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.59x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 271 ms                                                       | 249 ms: 1.09x faster                                                        |
| float          | 111 ms                                                       | 142 ms: 1.28x slower                                                        |
| nbody          | 134 ms                                                       | 191 ms: 1.43x slower                                                        |
| Geometric mean | (ref)                                                        | 1.19x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 261 ms                                                       | 250 ms: 1.04x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 28.0 ms: 1.03x slower                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.61 ms: 1.17x slower                                                       |
| regex_compile  | 190 ms                                                       | 224 ms: 1.18x slower                                                        |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 160 ms                                                       | 139 ms: 1.15x faster                                                        |
| json_loads           | 30.3 us                                                      | 28.8 us: 1.05x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 13.9 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 107 ms: 1.03x faster                                                        |
| pickle               | 9.89 us                                                      | 10.4 us: 1.05x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.53 us: 1.10x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 32.6 us: 1.11x slower                                                       |
| tomli_loads          | 2.92 sec                                                     | 3.33 sec: 1.14x slower                                                      |
| unpickle_list        | 4.65 us                                                      | 5.31 us: 1.14x slower                                                       |
| xml_etree_process    | 75.9 ms                                                      | 91.6 ms: 1.21x slower                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 113 ms: 1.23x slower                                                        |
| unpickle_pure_python | 312 us                                                       | 399 us: 1.28x slower                                                        |
| pickle_pure_python   | 455 us                                                       | 583 us: 1.28x slower                                                        |
| unpickle             | 13.5 us                                                      | 17.4 us: 1.29x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 17.5 ms: 1.52x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 11.8 ms: 1.61x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.57x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 63.3 ms                                                      | 82.4 ms: 1.30x slower                                                       |
| django_template | 50.2 ms                                                      | 66.4 ms: 1.32x slower                                                       |
| genshi_text     | 31.4 ms                                                      | 42.3 ms: 1.35x slower                                                       |
| mako            | 14.7 ms                                                      | 21.4 ms: 1.46x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.36x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 263 us: 2.04x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 452 ms: 1.72x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 928 ms: 1.72x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.80 sec: 1.72x faster                                                      |
| async_tree_none          | 692 ms                                                       | 411 ms: 1.68x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 511 ms: 1.60x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 673 ms: 1.39x faster                                                        |
| generators               | 57.3 ms                                                      | 41.4 ms: 1.38x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.79 ms: 1.33x faster                                                       |
| pylint                   | 566 ms                                                       | 433 ms: 1.31x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 139 ms: 1.15x faster                                                        |
| gc_traversal             | 3.42 ms                                                      | 3.04 ms: 1.12x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 19.6 ms: 1.09x faster                                                       |
| coroutines               | 30.3 ms                                                      | 27.8 ms: 1.09x faster                                                       |
| deepcopy                 | 468 us                                                       | 430 us: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 249 ms: 1.09x faster                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 1.67 ms: 1.06x faster                                                       |
| json_loads               | 30.3 us                                                      | 28.8 us: 1.05x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 13.9 ms: 1.05x faster                                                       |
| regex_dna                | 261 ms                                                       | 250 ms: 1.04x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 107 ms: 1.03x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 379 ms: 1.03x faster                                                        |
| docutils                 | 3.41 sec                                                     | 3.37 sec: 1.01x faster                                                      |
| deepcopy_memo            | 49.8 us                                                      | 49.2 us: 1.01x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 118 ms: 1.01x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.70 sec: 1.01x slower                                                      |
| json                     | 5.86 ms                                                      | 6.03 ms: 1.03x slower                                                       |
| regex_v8                 | 27.2 ms                                                      | 28.0 ms: 1.03x slower                                                       |
| pyflate                  | 733 ms                                                       | 760 ms: 1.04x slower                                                        |
| pickle                   | 9.89 us                                                      | 10.4 us: 1.05x slower                                                       |
| logging_silent           | 167 ns                                                       | 177 ns: 1.06x slower                                                        |
| tornado_http             | 157 ms                                                       | 166 ms: 1.06x slower                                                        |
| richards_super           | 90.6 ms                                                      | 96.3 ms: 1.06x slower                                                       |
| richards                 | 75.1 ms                                                      | 79.9 ms: 1.06x slower                                                       |
| mdp                      | 3.01 sec                                                     | 3.25 sec: 1.08x slower                                                      |
| deltablue                | 7.50 ms                                                      | 8.16 ms: 1.09x slower                                                       |
| go                       | 262 ms                                                       | 285 ms: 1.09x slower                                                        |
| comprehensions           | 26.7 us                                                      | 29.1 us: 1.09x slower                                                       |
| dulwich_log              | 81.1 ms                                                      | 89.1 ms: 1.10x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.53 us: 1.10x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 32.6 us: 1.11x slower                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.63 ms: 1.11x slower                                                       |
| html5lib                 | 94.6 ms                                                      | 105 ms: 1.11x slower                                                        |
| chaos                    | 109 ms                                                       | 122 ms: 1.12x slower                                                        |
| nqueens                  | 115 ms                                                       | 129 ms: 1.12x slower                                                        |
| scimark_fft              | 361 ms                                                       | 407 ms: 1.13x slower                                                        |
| tomli_loads              | 2.92 sec                                                     | 3.33 sec: 1.14x slower                                                      |
| unpickle_list            | 4.65 us                                                      | 5.31 us: 1.14x slower                                                       |
| sympy_integrate          | 28.2 ms                                                      | 32.2 ms: 1.14x slower                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 4.61 us: 1.15x slower                                                       |
| spectral_norm            | 139 ms                                                       | 160 ms: 1.15x slower                                                        |
| thrift                   | 1.18 ms                                                      | 1.36 ms: 1.15x slower                                                       |
| async_generators         | 421 ms                                                       | 489 ms: 1.16x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.61 ms: 1.17x slower                                                       |
| regex_compile            | 190 ms                                                       | 224 ms: 1.18x slower                                                        |
| fannkuch                 | 483 ms                                                       | 575 ms: 1.19x slower                                                        |
| xml_etree_process        | 75.9 ms                                                      | 91.6 ms: 1.21x slower                                                       |
| 2to3                     | 350 ms                                                       | 424 ms: 1.21x slower                                                        |
| hexiom                   | 9.42 ms                                                      | 11.4 ms: 1.21x slower                                                       |
| raytrace                 | 489 ms                                                       | 596 ms: 1.22x slower                                                        |
| meteor_contest           | 138 ms                                                       | 169 ms: 1.22x slower                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 113 ms: 1.23x slower                                                        |
| sympy_str                | 360 ms                                                       | 446 ms: 1.24x slower                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 133 ms: 1.24x slower                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 3.35 ms: 1.25x slower                                                       |
| sqlglot_normalize        | 144 ms                                                       | 180 ms: 1.25x slower                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 2.84 ms: 1.27x slower                                                       |
| float                    | 111 ms                                                       | 142 ms: 1.28x slower                                                        |
| unpickle_pure_python     | 312 us                                                       | 399 us: 1.28x slower                                                        |
| pickle_pure_python       | 455 us                                                       | 583 us: 1.28x slower                                                        |
| unpickle                 | 13.5 us                                                      | 17.4 us: 1.29x slower                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 91.1 ms: 1.30x slower                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 1.37 sec: 1.30x slower                                                      |
| genshi_xml               | 63.3 ms                                                      | 82.4 ms: 1.30x slower                                                       |
| pprint_pformat           | 2.15 sec                                                     | 2.81 sec: 1.30x slower                                                      |
| logging_format           | 9.64 us                                                      | 12.6 us: 1.31x slower                                                       |
| logging_simple           | 8.88 us                                                      | 11.6 us: 1.31x slower                                                       |
| django_template          | 50.2 ms                                                      | 66.4 ms: 1.32x slower                                                       |
| genshi_text              | 31.4 ms                                                      | 42.3 ms: 1.35x slower                                                       |
| sympy_sum                | 193 ms                                                       | 260 ms: 1.35x slower                                                        |
| sympy_expand             | 600 ms                                                       | 811 ms: 1.35x slower                                                        |
| scimark_sor              | 180 ms                                                       | 244 ms: 1.35x slower                                                        |
| scimark_lu               | 167 ms                                                       | 228 ms: 1.36x slower                                                        |
| nbody                    | 134 ms                                                       | 191 ms: 1.43x slower                                                        |
| telco                    | 7.23 ms                                                      | 10.4 ms: 1.45x slower                                                       |
| mako                     | 14.7 ms                                                      | 21.4 ms: 1.46x slower                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 1.70 ms: 1.49x slower                                                       |
| python_startup           | 11.5 ms                                                      | 17.5 ms: 1.52x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 11.8 ms: 1.61x slower                                                       |
| coverage                 | 63.3 ms                                                      | 108 ms: 1.70x slower                                                        |
| unpack_sequence          | 59.9 ns                                                      | 131 ns: 2.18x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.09x slower                                                                |

Benchmark hidden because not significant (1): sqlite_synth
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240914-3.14.0a0-401fff7-NOGIL/bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: 1.30x