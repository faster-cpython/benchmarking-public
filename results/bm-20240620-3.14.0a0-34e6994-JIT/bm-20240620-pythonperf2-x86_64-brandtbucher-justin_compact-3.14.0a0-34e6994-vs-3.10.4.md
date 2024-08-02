# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_compact
- machine: linux-x86_64
- commit hash: 34e6994
- commit date: 2024-06-20
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 308 ms: 1.14x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.12 sec: 1.10x faster                                                      |
| html5lib       | 94.6 ms                                                      | 73.2 ms: 1.29x faster                                                       |
| tornado_http   | 157 ms                                                       | 123 ms: 1.28x faster                                                        |
| Geometric mean | (ref)                                                        | 1.20x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 383 ms: 1.81x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 915 ms: 1.75x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 476 ms: 1.72x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 629 ms: 1.49x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.69x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 82.4 ms: 1.63x faster                                                       |
| float          | 111 ms                                                       | 74.4 ms: 1.49x faster                                                       |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.38x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 139 ms: 1.37x faster                                                        |
| regex_dna      | 261 ms                                                       | 240 ms: 1.09x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 25.4 ms: 1.07x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.58 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 316 us: 1.44x faster                                                        |
| unpickle_pure_python | 312 us                                                       | 218 us: 1.43x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.11 sec: 1.38x faster                                                      |
| json_dumps           | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 57.9 ms: 1.31x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.6 us: 1.19x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 81.0 ms: 1.14x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 141 ms: 1.13x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 99.8 ms: 1.11x faster                                                       |
| unpickle_list        | 4.65 us                                                      | 4.74 us: 1.02x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.36 us: 1.06x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 31.3 us: 1.06x slower                                                       |
| pickle               | 9.89 us                                                      | 10.9 us: 1.10x slower                                                       |
| unpickle             | 13.5 us                                                      | 15.4 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.9 ms: 1.21x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.50 ms: 1.30x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.25x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.23 ms: 1.59x faster                                                       |
| django_template | 50.2 ms                                                      | 41.2 ms: 1.22x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 27.3 ms: 1.15x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.22x faster                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 185 us: 2.90x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 376 ms: 2.07x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.66 ms: 2.05x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| async_tree_none          | 692 ms                                                       | 383 ms: 1.81x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 915 ms: 1.75x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 476 ms: 1.72x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 29.0 us: 1.72x faster                                                       |
| raytrace                 | 489 ms                                                       | 287 ms: 1.71x faster                                                        |
| generators               | 57.3 ms                                                      | 34.1 ms: 1.68x faster                                                       |
| spectral_norm            | 139 ms                                                       | 82.9 ms: 1.68x faster                                                       |
| richards_super           | 90.6 ms                                                      | 54.5 ms: 1.66x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 72.0 ms: 1.66x faster                                                       |
| chaos                    | 109 ms                                                       | 66.1 ms: 1.64x faster                                                       |
| pyflate                  | 733 ms                                                       | 449 ms: 1.63x faster                                                        |
| nbody                    | 134 ms                                                       | 82.4 ms: 1.63x faster                                                       |
| logging_silent           | 167 ns                                                       | 104 ns: 1.61x faster                                                        |
| richards                 | 75.1 ms                                                      | 46.9 ms: 1.60x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 67.4 ms: 1.59x faster                                                       |
| mako                     | 14.7 ms                                                      | 9.23 ms: 1.59x faster                                                       |
| go                       | 262 ms                                                       | 165 ms: 1.58x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.45 ms: 1.54x faster                                                       |
| deepcopy                 | 468 us                                                       | 307 us: 1.52x faster                                                        |
| float                    | 111 ms                                                       | 74.4 ms: 1.49x faster                                                       |
| pylint                   | 566 ms                                                       | 379 ms: 1.49x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 629 ms: 1.49x faster                                                        |
| comprehensions           | 26.7 us                                                      | 18.3 us: 1.46x faster                                                       |
| scimark_lu               | 167 ms                                                       | 115 ms: 1.45x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.85 ms: 1.45x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 316 us: 1.44x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 218 us: 1.43x faster                                                        |
| fannkuch                 | 483 ms                                                       | 341 ms: 1.41x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.75 ms: 1.40x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.11 sec: 1.38x faster                                                      |
| logging_simple           | 8.88 us                                                      | 6.43 us: 1.38x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                                       |
| regex_compile            | 190 ms                                                       | 139 ms: 1.37x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.06 us: 1.37x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.2 ms: 1.36x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.74 ms: 1.34x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.63 sec: 1.32x faster                                                      |
| deepcopy_reduce          | 4.01 us                                                      | 3.03 us: 1.32x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 793 ms: 1.32x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 16.2 ms: 1.32x faster                                                       |
| scimark_sor              | 180 ms                                                       | 137 ms: 1.32x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 57.9 ms: 1.31x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.28 sec: 1.30x faster                                                      |
| html5lib                 | 94.6 ms                                                      | 73.2 ms: 1.29x faster                                                       |
| tornado_http             | 157 ms                                                       | 123 ms: 1.28x faster                                                        |
| thrift                   | 1.18 ms                                                      | 924 us: 1.27x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.02 ms: 1.26x faster                                                       |
| scimark_fft              | 361 ms                                                       | 296 ms: 1.22x faster                                                        |
| django_template          | 50.2 ms                                                      | 41.2 ms: 1.22x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 67.1 ms: 1.21x faster                                                       |
| nqueens                  | 115 ms                                                       | 96.2 ms: 1.20x faster                                                       |
| json_loads               | 30.3 us                                                      | 25.6 us: 1.19x faster                                                       |
| sympy_sum                | 193 ms                                                       | 164 ms: 1.17x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 975 us: 1.17x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.59 sec: 1.16x faster                                                      |
| dask                     | 472 ms                                                       | 407 ms: 1.16x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 27.3 ms: 1.15x faster                                                       |
| sympy_str                | 360 ms                                                       | 314 ms: 1.15x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 81.0 ms: 1.14x faster                                                       |
| 2to3                     | 350 ms                                                       | 308 ms: 1.14x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 141 ms: 1.13x faster                                                        |
| sympy_expand             | 600 ms                                                       | 533 ms: 1.13x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 99.8 ms: 1.11x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 25.5 ms: 1.10x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 131 ms: 1.10x faster                                                        |
| docutils                 | 3.41 sec                                                     | 3.12 sec: 1.10x faster                                                      |
| sqlglot_optimize         | 70.1 ms                                                      | 64.4 ms: 1.09x faster                                                       |
| regex_dna                | 261 ms                                                       | 240 ms: 1.09x faster                                                        |
| async_generators         | 421 ms                                                       | 389 ms: 1.08x faster                                                        |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.78 us: 1.07x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 25.4 ms: 1.07x faster                                                       |
| json                     | 5.86 ms                                                      | 5.52 ms: 1.06x faster                                                       |
| meteor_contest           | 138 ms                                                       | 130 ms: 1.06x faster                                                        |
| unpickle_list            | 4.65 us                                                      | 4.74 us: 1.02x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.36 us: 1.06x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 31.3 us: 1.06x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.91 ms: 1.08x slower                                                       |
| pickle                   | 9.89 us                                                      | 10.9 us: 1.10x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.22 ms: 1.14x slower                                                       |
| unpickle                 | 13.5 us                                                      | 15.4 us: 1.14x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.58 ms: 1.16x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.9 ms: 1.21x slower                                                       |
| coverage                 | 63.3 ms                                                      | 79.1 ms: 1.25x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.42 ms: 1.29x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.50 ms: 1.30x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.29x faster                                                                |

Benchmark hidden because not significant (2): asyncio_websockets, genshi_xml
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240620-3.14.0a0-34e6994-JIT/bm-20240620-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.22x