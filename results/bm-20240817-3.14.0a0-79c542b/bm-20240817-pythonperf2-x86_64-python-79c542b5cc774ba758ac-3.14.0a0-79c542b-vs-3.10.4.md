# Results vs. 3.10.4

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: linux-x86_64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.36x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 284 ms: 1.23x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.98 sec: 1.15x faster                                                      |
| html5lib       | 94.6 ms                                                      | 73.6 ms: 1.29x faster                                                       |
| tornado_http   | 157 ms                                                       | 116 ms: 1.35x faster                                                        |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 336 ms: 2.06x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 401 ms: 2.04x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 800 ms: 2.00x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 577 ms: 1.62x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.92x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 86.3 ms: 1.55x faster                                                       |
| float          | 111 ms                                                       | 79.6 ms: 1.40x faster                                                       |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.32x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 139 ms: 1.37x faster                                                        |
| regex_dna      | 261 ms                                                       | 240 ms: 1.09x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.59 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 312 us: 1.46x faster                                                        |
| unpickle_pure_python | 312 us                                                       | 214 us: 1.46x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 58.7 ms: 1.29x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.27 sec: 1.28x faster                                                      |
| json_loads           | 30.3 us                                                      | 25.2 us: 1.20x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 101 ms: 1.10x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 84.7 ms: 1.09x faster                                                       |
| Geometric mean       | (ref)                                                        | 1.26x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.06 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                                       |
| django_template | 50.2 ms                                                      | 38.9 ms: 1.29x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 25.4 ms: 1.24x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 55.0 ms: 1.15x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.27x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 174 us: 3.08x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.31 ms: 2.26x faster                                                       |
| asyncio_tcp              | 779 ms                                                       | 372 ms: 2.10x faster                                                        |
| async_tree_none          | 692 ms                                                       | 336 ms: 2.06x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 401 ms: 2.04x faster                                                        |
| generators               | 57.3 ms                                                      | 28.4 ms: 2.02x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 800 ms: 2.00x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                                      |
| raytrace                 | 489 ms                                                       | 269 ms: 1.82x faster                                                        |
| chaos                    | 109 ms                                                       | 61.0 ms: 1.78x faster                                                       |
| scimark_lu               | 167 ms                                                       | 94.1 ms: 1.77x faster                                                       |
| logging_silent           | 167 ns                                                       | 96.3 ns: 1.74x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 29.3 us: 1.70x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 64.9 ms: 1.66x faster                                                       |
| go                       | 262 ms                                                       | 158 ms: 1.65x faster                                                        |
| scimark_sor              | 180 ms                                                       | 110 ms: 1.64x faster                                                        |
| deepcopy                 | 468 us                                                       | 285 us: 1.64x faster                                                        |
| richards_super           | 90.6 ms                                                      | 55.4 ms: 1.64x faster                                                       |
| pylint                   | 566 ms                                                       | 347 ms: 1.63x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 73.1 ms: 1.63x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 577 ms: 1.62x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.41 ms: 1.59x faster                                                       |
| nbody                    | 134 ms                                                       | 86.3 ms: 1.55x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.2 us: 1.55x faster                                                       |
| pyflate                  | 733 ms                                                       | 478 ms: 1.53x faster                                                        |
| richards                 | 75.1 ms                                                      | 49.4 ms: 1.52x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.78 ms: 1.50x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.36 ms: 1.48x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 312 us: 1.46x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 214 us: 1.46x faster                                                        |
| spectral_norm            | 139 ms                                                       | 96.6 ms: 1.44x faster                                                       |
| coroutines               | 30.3 ms                                                      | 21.2 ms: 1.43x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.25 us: 1.42x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.86 us: 1.40x faster                                                       |
| float                    | 111 ms                                                       | 79.6 ms: 1.40x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.92 us: 1.39x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.21 sec: 1.38x faster                                                      |
| regex_compile            | 190 ms                                                       | 139 ms: 1.37x faster                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 4.67 ms: 1.37x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                       |
| fannkuch                 | 483 ms                                                       | 357 ms: 1.35x faster                                                        |
| tornado_http             | 157 ms                                                       | 116 ms: 1.35x faster                                                        |
| thrift                   | 1.18 ms                                                      | 877 us: 1.34x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 16.0 ms: 1.33x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 865 us: 1.32x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 58.7 ms: 1.29x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 814 ms: 1.29x faster                                                        |
| django_template          | 50.2 ms                                                      | 38.9 ms: 1.29x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 73.6 ms: 1.29x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.27 sec: 1.28x faster                                                      |
| pprint_pformat           | 2.15 sec                                                     | 1.68 sec: 1.28x faster                                                      |
| nqueens                  | 115 ms                                                       | 90.9 ms: 1.27x faster                                                       |
| sympy_sum                | 193 ms                                                       | 154 ms: 1.25x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 25.4 ms: 1.24x faster                                                       |
| 2to3                     | 350 ms                                                       | 284 ms: 1.23x faster                                                        |
| sympy_str                | 360 ms                                                       | 295 ms: 1.22x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 23.1 ms: 1.22x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.21x faster                                                        |
| scimark_fft              | 361 ms                                                       | 299 ms: 1.21x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.49 sec: 1.21x faster                                                      |
| sympy_expand             | 600 ms                                                       | 497 ms: 1.21x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.22 ms: 1.20x faster                                                       |
| json_loads               | 30.3 us                                                      | 25.2 us: 1.20x faster                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 58.4 ms: 1.20x faster                                                       |
| async_generators         | 421 ms                                                       | 364 ms: 1.16x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 55.0 ms: 1.15x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.98 sec: 1.15x faster                                                      |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| json                     | 5.86 ms                                                      | 5.31 ms: 1.11x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 101 ms: 1.10x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 84.7 ms: 1.09x faster                                                       |
| regex_dna                | 261 ms                                                       | 240 ms: 1.09x faster                                                        |
| meteor_contest           | 138 ms                                                       | 128 ms: 1.08x faster                                                        |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                       |
| telco                    | 7.23 ms                                                      | 7.98 ms: 1.10x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.97 ms: 1.12x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.59 ms: 1.16x slower                                                       |
| coverage                 | 63.3 ms                                                      | 77.8 ms: 1.23x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.06 ms: 1.24x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.48 ms: 1.31x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.36x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240817-3.14.0a0-79c542b/bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.13x