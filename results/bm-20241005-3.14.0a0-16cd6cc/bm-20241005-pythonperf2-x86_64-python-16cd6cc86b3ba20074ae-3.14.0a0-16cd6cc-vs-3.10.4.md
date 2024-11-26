# Results vs. 3.10.4

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-x86_64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.331x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 283 ms: 1.24x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.88 sec: 1.18x faster                                                      |
| html5lib       | 94.6 ms                                                      | 71.0 ms: 1.33x faster                                                       |
| tornado_http   | 157 ms                                                       | 115 ms: 1.36x faster                                                        |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 319 ms: 2.17x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 401 ms: 2.04x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 821 ms: 1.95x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 571 ms: 1.64x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.94x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 89.9 ms: 1.49x faster                                                       |
| float          | 111 ms                                                       | 78.8 ms: 1.41x faster                                                       |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 140 ms: 1.35x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 25.0 ms: 1.09x faster                                                       |
| regex_dna      | 261 ms                                                       | 242 ms: 1.08x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.48 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 315 us: 1.44x faster                                                        |
| unpickle_pure_python | 312 us                                                       | 218 us: 1.43x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.8 ms: 1.34x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 61.4 ms: 1.24x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.54 sec: 1.15x faster                                                      |
| xml_etree_iterparse  | 110 ms                                                       | 102 ms: 1.08x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 86.1 ms: 1.07x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 150 ms: 1.07x faster                                                        |
| unpickle_list        | 4.65 us                                                      | 4.76 us: 1.03x slower                                                       |
| pickle               | 9.89 us                                                      | 10.8 us: 1.09x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 32.8 us: 1.11x slower                                                       |
| unpickle             | 13.5 us                                                      | 15.1 us: 1.12x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.71 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.10x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 8.95 ms: 1.22x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                                       |
| django_template | 50.2 ms                                                      | 39.9 ms: 1.26x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 25.5 ms: 1.23x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 54.6 ms: 1.16x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.26x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 173 us: 3.11x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.35 ms: 2.24x faster                                                       |
| async_tree_none          | 692 ms                                                       | 319 ms: 2.17x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 374 ms: 2.08x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 401 ms: 2.04x faster                                                        |
| generators               | 57.3 ms                                                      | 29.1 ms: 1.97x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                                      |
| async_tree_io            | 1.60 sec                                                     | 821 ms: 1.95x faster                                                        |
| go                       | 262 ms                                                       | 135 ms: 1.94x faster                                                        |
| raytrace                 | 489 ms                                                       | 273 ms: 1.79x faster                                                        |
| scimark_lu               | 167 ms                                                       | 93.5 ms: 1.78x faster                                                       |
| chaos                    | 109 ms                                                       | 63.0 ms: 1.72x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 29.5 us: 1.69x faster                                                       |
| logging_silent           | 167 ns                                                       | 99.3 ns: 1.69x faster                                                       |
| deepcopy                 | 468 us                                                       | 284 us: 1.65x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 571 ms: 1.64x faster                                                        |
| pylint                   | 566 ms                                                       | 346 ms: 1.64x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 74.2 ms: 1.61x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 67.1 ms: 1.60x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.42 ms: 1.57x faster                                                       |
| richards_super           | 90.6 ms                                                      | 57.9 ms: 1.57x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.1 us: 1.56x faster                                                       |
| scimark_sor              | 180 ms                                                       | 118 ms: 1.53x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.23 ms: 1.51x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.80 ms: 1.49x faster                                                       |
| nbody                    | 134 ms                                                       | 89.9 ms: 1.49x faster                                                       |
| richards                 | 75.1 ms                                                      | 51.2 ms: 1.47x faster                                                       |
| pyflate                  | 733 ms                                                       | 504 ms: 1.45x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 315 us: 1.44x faster                                                        |
| spectral_norm            | 139 ms                                                       | 97.2 ms: 1.43x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 218 us: 1.43x faster                                                        |
| logging_format           | 9.64 us                                                      | 6.80 us: 1.42x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.28 us: 1.41x faster                                                       |
| float                    | 111 ms                                                       | 78.8 ms: 1.41x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                                       |
| coroutines               | 30.3 ms                                                      | 21.9 ms: 1.39x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.90 us: 1.38x faster                                                       |
| thrift                   | 1.18 ms                                                      | 855 us: 1.37x faster                                                        |
| tornado_http             | 157 ms                                                       | 115 ms: 1.36x faster                                                        |
| fannkuch                 | 483 ms                                                       | 355 ms: 1.36x faster                                                        |
| regex_compile            | 190 ms                                                       | 140 ms: 1.35x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 15.8 ms: 1.35x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 10.8 ms: 1.34x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                                      |
| html5lib                 | 94.6 ms                                                      | 71.0 ms: 1.33x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.64 sec: 1.31x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 803 ms: 1.31x faster                                                        |
| nqueens                  | 115 ms                                                       | 88.8 ms: 1.29x faster                                                       |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.28x faster                                                        |
| django_template          | 50.2 ms                                                      | 39.9 ms: 1.26x faster                                                       |
| sympy_str                | 360 ms                                                       | 289 ms: 1.25x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 919 us: 1.24x faster                                                        |
| 2to3                     | 350 ms                                                       | 283 ms: 1.24x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 61.4 ms: 1.24x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 25.5 ms: 1.23x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 117 ms: 1.23x faster                                                        |
| sympy_expand             | 600 ms                                                       | 491 ms: 1.22x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 66.6 ms: 1.22x faster                                                       |
| scimark_fft              | 361 ms                                                       | 297 ms: 1.22x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 23.2 ms: 1.21x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.48 sec: 1.21x faster                                                      |
| json_loads               | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 58.8 ms: 1.19x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.88 sec: 1.18x faster                                                      |
| unpack_sequence          | 59.9 ns                                                      | 50.7 ns: 1.18x faster                                                       |
| async_generators         | 421 ms                                                       | 358 ms: 1.17x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 54.6 ms: 1.16x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.41 ms: 1.15x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.54 sec: 1.15x faster                                                      |
| json                     | 5.86 ms                                                      | 5.34 ms: 1.10x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.72 us: 1.10x faster                                                       |
| meteor_contest           | 138 ms                                                       | 127 ms: 1.09x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.0 ms: 1.09x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 102 ms: 1.08x faster                                                        |
| regex_dna                | 261 ms                                                       | 242 ms: 1.08x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 86.1 ms: 1.07x faster                                                       |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 150 ms: 1.07x faster                                                        |
| unpickle_list            | 4.65 us                                                      | 4.76 us: 1.03x slower                                                       |
| pickle                   | 9.89 us                                                      | 10.8 us: 1.09x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 32.8 us: 1.11x slower                                                       |
| unpickle                 | 13.5 us                                                      | 15.1 us: 1.12x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.48 ms: 1.13x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.19 ms: 1.13x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.71 us: 1.14x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.03 ms: 1.15x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.95 ms: 1.22x slower                                                       |
| coverage                 | 63.3 ms                                                      | 85.7 ms: 1.35x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.81 ms: 1.41x slower                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 1.33 sec: 208.66x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.24x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-pythonperf2-x86_64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.331x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.12x