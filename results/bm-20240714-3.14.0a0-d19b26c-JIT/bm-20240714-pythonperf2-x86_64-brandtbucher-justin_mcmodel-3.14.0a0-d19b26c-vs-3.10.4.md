# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_mcmodel
- machine: linux-x86_64
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 298 ms: 1.17x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.10 sec: 1.10x faster                                                      |
| html5lib       | 94.6 ms                                                      | 69.1 ms: 1.37x faster                                                       |
| tornado_http   | 157 ms                                                       | 121 ms: 1.29x faster                                                        |
| Geometric mean | (ref)                                                        | 1.23x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 338 ms: 2.05x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 405 ms: 2.02x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 811 ms: 1.97x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 579 ms: 1.62x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.91x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 81.1 ms: 1.65x faster                                                       |
| float          | 111 ms                                                       | 73.2 ms: 1.52x faster                                                       |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.39x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 133 ms: 1.43x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 27.1 ms: 1.00x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.58 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 312 us: 1.46x faster                                                        |
| unpickle_pure_python | 312 us                                                       | 217 us: 1.44x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.04 sec: 1.43x faster                                                      |
| xml_etree_process    | 75.9 ms                                                      | 57.6 ms: 1.32x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 11.0 ms: 1.32x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.4 us: 1.19x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 80.9 ms: 1.14x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 97.7 ms: 1.13x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.12x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.28x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.04 ms: 1.23x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 8.96 ms: 1.64x faster                                                       |
| django_template | 50.2 ms                                                      | 40.8 ms: 1.23x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 26.5 ms: 1.19x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 58.8 ms: 1.08x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.27x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 185 us: 2.90x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.57 ms: 2.10x faster                                                       |
| asyncio_tcp              | 779 ms                                                       | 379 ms: 2.05x faster                                                        |
| async_tree_none          | 692 ms                                                       | 338 ms: 2.05x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 405 ms: 2.02x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 811 ms: 1.97x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                                      |
| richards_super           | 90.6 ms                                                      | 49.6 ms: 1.83x faster                                                       |
| raytrace                 | 489 ms                                                       | 275 ms: 1.78x faster                                                        |
| richards                 | 75.1 ms                                                      | 43.0 ms: 1.75x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 28.6 us: 1.74x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 70.1 ms: 1.70x faster                                                       |
| go                       | 262 ms                                                       | 155 ms: 1.69x faster                                                        |
| chaos                    | 109 ms                                                       | 64.3 ms: 1.69x faster                                                       |
| spectral_norm            | 139 ms                                                       | 82.9 ms: 1.68x faster                                                       |
| pyflate                  | 733 ms                                                       | 438 ms: 1.67x faster                                                        |
| generators               | 57.3 ms                                                      | 34.4 ms: 1.67x faster                                                       |
| nbody                    | 134 ms                                                       | 81.1 ms: 1.65x faster                                                       |
| mako                     | 14.7 ms                                                      | 8.96 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 579 ms: 1.62x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.39 ms: 1.61x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 66.9 ms: 1.61x faster                                                       |
| logging_silent           | 167 ns                                                       | 105 ns: 1.60x faster                                                        |
| deepcopy                 | 468 us                                                       | 301 us: 1.55x faster                                                        |
| pylint                   | 566 ms                                                       | 372 ms: 1.52x faster                                                        |
| float                    | 111 ms                                                       | 73.2 ms: 1.52x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.80 ms: 1.49x faster                                                       |
| comprehensions           | 26.7 us                                                      | 18.1 us: 1.47x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 312 us: 1.46x faster                                                        |
| scimark_sor              | 180 ms                                                       | 124 ms: 1.45x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.0 ms: 1.44x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 217 us: 1.44x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.57 ms: 1.43x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.04 sec: 1.43x faster                                                      |
| regex_compile            | 190 ms                                                       | 133 ms: 1.43x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.27 us: 1.42x faster                                                       |
| fannkuch                 | 483 ms                                                       | 346 ms: 1.40x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.20 sec: 1.39x faster                                                      |
| logging_format           | 9.64 us                                                      | 7.00 us: 1.38x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 69.1 ms: 1.37x faster                                                       |
| scimark_lu               | 167 ms                                                       | 123 ms: 1.36x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.60 sec: 1.34x faster                                                      |
| bench_mp_pool            | 6.37 ms                                                      | 4.78 ms: 1.33x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.02 us: 1.33x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 16.1 ms: 1.32x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 794 ms: 1.32x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 57.6 ms: 1.32x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 11.0 ms: 1.32x faster                                                       |
| thrift                   | 1.18 ms                                                      | 897 us: 1.31x faster                                                        |
| tornado_http             | 157 ms                                                       | 121 ms: 1.29x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 924 us: 1.23x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 65.9 ms: 1.23x faster                                                       |
| django_template          | 50.2 ms                                                      | 40.8 ms: 1.23x faster                                                       |
| nqueens                  | 115 ms                                                       | 94.7 ms: 1.21x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.20 ms: 1.21x faster                                                       |
| json_loads               | 30.3 us                                                      | 25.4 us: 1.19x faster                                                       |
| dask                     | 472 ms                                                       | 397 ms: 1.19x faster                                                        |
| sympy_str                | 360 ms                                                       | 303 ms: 1.19x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 26.5 ms: 1.19x faster                                                       |
| scimark_fft              | 361 ms                                                       | 306 ms: 1.18x faster                                                        |
| sympy_sum                | 193 ms                                                       | 164 ms: 1.18x faster                                                        |
| 2to3                     | 350 ms                                                       | 298 ms: 1.17x faster                                                        |
| sympy_expand             | 600 ms                                                       | 512 ms: 1.17x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.62 sec: 1.15x faster                                                      |
| xml_etree_generate       | 92.3 ms                                                      | 80.9 ms: 1.14x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 97.7 ms: 1.13x faster                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 62.2 ms: 1.13x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 128 ms: 1.13x faster                                                        |
| async_generators         | 421 ms                                                       | 376 ms: 1.12x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.12x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 25.4 ms: 1.11x faster                                                       |
| docutils                 | 3.41 sec                                                     | 3.10 sec: 1.10x faster                                                      |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 58.8 ms: 1.08x faster                                                       |
| meteor_contest           | 138 ms                                                       | 130 ms: 1.07x faster                                                        |
| json                     | 5.86 ms                                                      | 5.50 ms: 1.07x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 27.1 ms: 1.00x faster                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.92 ms: 1.09x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.35 ms: 1.16x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.58 ms: 1.16x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.04 ms: 1.23x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.43 ms: 1.30x slower                                                       |
| coverage                 | 63.3 ms                                                      | 82.8 ms: 1.31x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.34x faster                                                                |

Benchmark hidden because not significant (2): regex_dna, asyncio_websockets
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240714-3.14.0a0-d19b26c-JIT/bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.20x