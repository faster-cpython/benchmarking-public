# Results vs. 3.10.4

- fork: python
- ref: e83ce850f433fd8bbf8f
- machine: linux-x86_64
- commit hash: e83ce85
- commit date: 2024-06-05
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 305 ms: 1.15x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.11 sec: 1.10x faster                                                      |
| html5lib       | 94.6 ms                                                      | 73.0 ms: 1.30x faster                                                       |
| tornado_http   | 157 ms                                                       | 123 ms: 1.27x faster                                                        |
| Geometric mean | (ref)                                                        | 1.20x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 380 ms: 1.82x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 893 ms: 1.79x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 482 ms: 1.70x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 629 ms: 1.49x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.69x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 81.1 ms: 1.65x faster                                                       |
| float          | 111 ms                                                       | 73.2 ms: 1.52x faster                                                       |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.39x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 137 ms: 1.38x faster                                                        |
| regex_dna      | 261 ms                                                       | 240 ms: 1.09x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.54 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 216 us: 1.45x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 318 us: 1.43x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.11 sec: 1.38x faster                                                      |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 58.1 ms: 1.31x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 81.1 ms: 1.14x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 99.8 ms: 1.11x faster                                                       |
| unpickle_list        | 4.65 us                                                      | 4.96 us: 1.07x slower                                                       |
| pickle               | 9.89 us                                                      | 10.8 us: 1.09x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.59 us: 1.11x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 33.3 us: 1.13x slower                                                       |
| unpickle             | 13.5 us                                                      | 15.5 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.8 ms: 1.20x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.46 ms: 1.29x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.25x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.19 ms: 1.60x faster                                                       |
| django_template | 50.2 ms                                                      | 41.8 ms: 1.20x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 29.5 ms: 1.07x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 66.8 ms: 1.06x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.18x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 184 us: 2.92x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 382 ms: 2.04x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.75 ms: 2.00x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| async_tree_none          | 692 ms                                                       | 380 ms: 1.82x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 893 ms: 1.79x faster                                                        |
| richards_super           | 90.6 ms                                                      | 51.8 ms: 1.75x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 69.9 ms: 1.70x faster                                                       |
| richards                 | 75.1 ms                                                      | 44.2 ms: 1.70x faster                                                       |
| async_tree_memoization   | 819 ms                                                       | 482 ms: 1.70x faster                                                        |
| raytrace                 | 489 ms                                                       | 292 ms: 1.67x faster                                                        |
| generators               | 57.3 ms                                                      | 34.3 ms: 1.67x faster                                                       |
| nbody                    | 134 ms                                                       | 81.1 ms: 1.65x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 65.7 ms: 1.63x faster                                                       |
| go                       | 262 ms                                                       | 161 ms: 1.63x faster                                                        |
| chaos                    | 109 ms                                                       | 66.8 ms: 1.62x faster                                                       |
| spectral_norm            | 139 ms                                                       | 86.5 ms: 1.61x faster                                                       |
| mako                     | 14.7 ms                                                      | 9.19 ms: 1.60x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.42 ms: 1.57x faster                                                       |
| pyflate                  | 733 ms                                                       | 469 ms: 1.56x faster                                                        |
| logging_silent           | 167 ns                                                       | 107 ns: 1.56x faster                                                        |
| float                    | 111 ms                                                       | 73.2 ms: 1.52x faster                                                       |
| pylint                   | 566 ms                                                       | 380 ms: 1.49x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 629 ms: 1.49x faster                                                        |
| scimark_lu               | 167 ms                                                       | 113 ms: 1.48x faster                                                        |
| comprehensions           | 26.7 us                                                      | 18.2 us: 1.47x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.83 ms: 1.46x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 216 us: 1.45x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 318 us: 1.43x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.5 ms: 1.41x faster                                                       |
| fannkuch                 | 483 ms                                                       | 344 ms: 1.40x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.76 ms: 1.39x faster                                                       |
| scimark_sor              | 180 ms                                                       | 130 ms: 1.39x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.11 sec: 1.38x faster                                                      |
| regex_compile            | 190 ms                                                       | 137 ms: 1.38x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.58 us: 1.35x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.16 us: 1.35x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 16.0 ms: 1.33x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 37.5 us: 1.33x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 799 ms: 1.31x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.28 sec: 1.31x faster                                                      |
| xml_etree_process        | 75.9 ms                                                      | 58.1 ms: 1.31x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.65 sec: 1.31x faster                                                      |
| html5lib                 | 94.6 ms                                                      | 73.0 ms: 1.30x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.93 ms: 1.29x faster                                                       |
| thrift                   | 1.18 ms                                                      | 914 us: 1.29x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 3.95 ms: 1.29x faster                                                       |
| scimark_fft              | 361 ms                                                       | 284 ms: 1.27x faster                                                        |
| tornado_http             | 157 ms                                                       | 123 ms: 1.27x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 65.3 ms: 1.24x faster                                                       |
| json_loads               | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| django_template          | 50.2 ms                                                      | 41.8 ms: 1.20x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 951 us: 1.20x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.55 sec: 1.18x faster                                                      |
| dask                     | 472 ms                                                       | 405 ms: 1.17x faster                                                        |
| sympy_sum                | 193 ms                                                       | 166 ms: 1.16x faster                                                        |
| sympy_str                | 360 ms                                                       | 312 ms: 1.15x faster                                                        |
| nqueens                  | 115 ms                                                       | 99.7 ms: 1.15x faster                                                       |
| 2to3                     | 350 ms                                                       | 305 ms: 1.15x faster                                                        |
| deepcopy                 | 468 us                                                       | 411 us: 1.14x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 81.1 ms: 1.14x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 127 ms: 1.13x faster                                                        |
| sympy_expand             | 600 ms                                                       | 531 ms: 1.13x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.11x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 63.3 ms: 1.11x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 99.8 ms: 1.11x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.62 us: 1.11x faster                                                       |
| json                     | 5.86 ms                                                      | 5.32 ms: 1.10x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 25.6 ms: 1.10x faster                                                       |
| docutils                 | 3.41 sec                                                     | 3.11 sec: 1.10x faster                                                      |
| regex_dna                | 261 ms                                                       | 240 ms: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| meteor_contest           | 138 ms                                                       | 129 ms: 1.07x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.79 us: 1.07x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 29.5 ms: 1.07x faster                                                       |
| async_generators         | 421 ms                                                       | 399 ms: 1.05x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 66.8 ms: 1.06x slower                                                       |
| unpickle_list            | 4.65 us                                                      | 4.96 us: 1.07x slower                                                       |
| pickle                   | 9.89 us                                                      | 10.8 us: 1.09x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.96 ms: 1.11x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.59 us: 1.11x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 33.3 us: 1.13x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.27 ms: 1.14x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.54 ms: 1.14x slower                                                       |
| unpickle                 | 13.5 us                                                      | 15.5 us: 1.15x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.8 ms: 1.20x slower                                                       |
| coverage                 | 63.3 ms                                                      | 78.8 ms: 1.25x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.38 ms: 1.28x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.46 ms: 1.29x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240605-3.14.0a0-e83ce85-JIT/bm-20240605-pythonperf2-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.22x