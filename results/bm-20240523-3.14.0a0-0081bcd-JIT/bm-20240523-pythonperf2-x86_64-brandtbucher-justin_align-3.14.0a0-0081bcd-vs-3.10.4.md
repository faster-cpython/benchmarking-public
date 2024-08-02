# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_align
- machine: linux-x86_64
- commit hash: 0081bcd
- commit date: 2024-05-23
- overall geometric mean: 1.27x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 305 ms: 1.15x faster                                                      |
| chameleon      | 9.44 ms                                                      | 7.66 ms: 1.23x faster                                                     |
| html5lib       | 94.6 ms                                                      | 73.3 ms: 1.29x faster                                                     |
| tornado_http   | 157 ms                                                       | 123 ms: 1.28x faster                                                      |
| Geometric mean | (ref)                                                        | 1.24x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 377 ms: 1.83x faster                                                      |
| async_tree_io           | 1.60 sec                                                     | 909 ms: 1.76x faster                                                      |
| async_tree_memoization  | 819 ms                                                       | 480 ms: 1.71x faster                                                      |
| async_tree_cpu_io_mixed | 936 ms                                                       | 627 ms: 1.49x faster                                                      |
| Geometric mean          | (ref)                                                        | 1.69x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 84.1 ms: 1.59x faster                                                     |
| float          | 111 ms                                                       | 77.6 ms: 1.43x faster                                                     |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                      |
| Geometric mean | (ref)                                                        | 1.35x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 139 ms: 1.37x faster                                                      |
| regex_dna      | 261 ms                                                       | 243 ms: 1.07x faster                                                      |
| regex_v8       | 27.2 ms                                                      | 25.5 ms: 1.06x faster                                                     |
| regex_effbot   | 3.09 ms                                                      | 3.65 ms: 1.18x slower                                                     |
| Geometric mean | (ref)                                                        | 1.07x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 213 us: 1.46x faster                                                      |
| pickle_pure_python   | 455 us                                                       | 311 us: 1.46x faster                                                      |
| tomli_loads          | 2.92 sec                                                     | 2.08 sec: 1.40x faster                                                    |
| json_dumps           | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                                     |
| xml_etree_process    | 75.9 ms                                                      | 59.2 ms: 1.28x faster                                                     |
| json_loads           | 30.3 us                                                      | 24.6 us: 1.23x faster                                                     |
| xml_etree_generate   | 92.3 ms                                                      | 82.2 ms: 1.12x faster                                                     |
| xml_etree_iterparse  | 110 ms                                                       | 100 ms: 1.10x faster                                                      |
| xml_etree_parse      | 160 ms                                                       | 146 ms: 1.10x faster                                                      |
| pickle_list          | 4.12 us                                                      | 4.40 us: 1.07x slower                                                     |
| pickle               | 9.89 us                                                      | 10.6 us: 1.07x slower                                                     |
| pickle_dict          | 29.5 us                                                      | 32.4 us: 1.10x slower                                                     |
| unpickle             | 13.5 us                                                      | 14.9 us: 1.11x slower                                                     |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                              |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.5 ms: 1.17x slower                                                     |
| python_startup_no_site | 7.33 ms                                                      | 9.45 ms: 1.29x slower                                                     |
| Geometric mean         | (ref)                                                        | 1.23x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.10 ms: 1.62x faster                                                     |
| django_template | 50.2 ms                                                      | 41.2 ms: 1.22x faster                                                     |
| genshi_text     | 31.4 ms                                                      | 28.2 ms: 1.11x faster                                                     |
| genshi_xml      | 63.3 ms                                                      | 64.8 ms: 1.02x slower                                                     |
| Geometric mean  | (ref)                                                        | 1.21x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 185 us: 2.90x faster                                                      |
| asyncio_tcp              | 779 ms                                                       | 377 ms: 2.07x faster                                                      |
| deltablue                | 7.50 ms                                                      | 3.75 ms: 2.00x faster                                                     |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                    |
| async_tree_none          | 692 ms                                                       | 377 ms: 1.83x faster                                                      |
| richards_super           | 90.6 ms                                                      | 50.9 ms: 1.78x faster                                                     |
| async_tree_io            | 1.60 sec                                                     | 909 ms: 1.76x faster                                                      |
| richards                 | 75.1 ms                                                      | 43.8 ms: 1.72x faster                                                     |
| async_tree_memoization   | 819 ms                                                       | 480 ms: 1.71x faster                                                      |
| raytrace                 | 489 ms                                                       | 288 ms: 1.70x faster                                                      |
| spectral_norm            | 139 ms                                                       | 82.2 ms: 1.69x faster                                                     |
| crypto_pyaes             | 119 ms                                                       | 71.1 ms: 1.68x faster                                                     |
| generators               | 57.3 ms                                                      | 34.8 ms: 1.65x faster                                                     |
| chaos                    | 109 ms                                                       | 66.1 ms: 1.64x faster                                                     |
| pyflate                  | 733 ms                                                       | 447 ms: 1.64x faster                                                      |
| scimark_monte_carlo      | 107 ms                                                       | 65.6 ms: 1.64x faster                                                     |
| go                       | 262 ms                                                       | 160 ms: 1.63x faster                                                      |
| logging_silent           | 167 ns                                                       | 103 ns: 1.63x faster                                                      |
| mako                     | 14.7 ms                                                      | 9.10 ms: 1.62x faster                                                     |
| nbody                    | 134 ms                                                       | 84.1 ms: 1.59x faster                                                     |
| sqlglot_parse            | 2.24 ms                                                      | 1.42 ms: 1.58x faster                                                     |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 627 ms: 1.49x faster                                                      |
| pylint                   | 566 ms                                                       | 381 ms: 1.49x faster                                                      |
| comprehensions           | 26.7 us                                                      | 18.0 us: 1.48x faster                                                     |
| sqlglot_transpile        | 2.68 ms                                                      | 1.82 ms: 1.47x faster                                                     |
| unpickle_pure_python     | 312 us                                                       | 213 us: 1.46x faster                                                      |
| pickle_pure_python       | 455 us                                                       | 311 us: 1.46x faster                                                      |
| scimark_lu               | 167 ms                                                       | 115 ms: 1.45x faster                                                      |
| float                    | 111 ms                                                       | 77.6 ms: 1.43x faster                                                     |
| coroutines               | 30.3 ms                                                      | 21.3 ms: 1.43x faster                                                     |
| tomli_loads              | 2.92 sec                                                     | 2.08 sec: 1.40x faster                                                    |
| fannkuch                 | 483 ms                                                       | 345 ms: 1.40x faster                                                      |
| hexiom                   | 9.42 ms                                                      | 6.74 ms: 1.40x faster                                                     |
| scimark_sor              | 180 ms                                                       | 130 ms: 1.39x faster                                                      |
| regex_compile            | 190 ms                                                       | 139 ms: 1.37x faster                                                      |
| json_dumps               | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                                     |
| logging_simple           | 8.88 us                                                      | 6.58 us: 1.35x faster                                                     |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                                    |
| logging_format           | 9.64 us                                                      | 7.22 us: 1.34x faster                                                     |
| deepcopy_memo            | 49.8 us                                                      | 37.3 us: 1.33x faster                                                     |
| bench_mp_pool            | 6.37 ms                                                      | 4.82 ms: 1.32x faster                                                     |
| pprint_pformat           | 2.15 sec                                                     | 1.63 sec: 1.32x faster                                                    |
| pprint_safe_repr         | 1.05 sec                                                     | 802 ms: 1.31x faster                                                      |
| pathlib                  | 21.4 ms                                                      | 16.4 ms: 1.30x faster                                                     |
| html5lib                 | 94.6 ms                                                      | 73.3 ms: 1.29x faster                                                     |
| thrift                   | 1.18 ms                                                      | 916 us: 1.28x faster                                                      |
| xml_etree_process        | 75.9 ms                                                      | 59.2 ms: 1.28x faster                                                     |
| tornado_http             | 157 ms                                                       | 123 ms: 1.28x faster                                                      |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.07 ms: 1.25x faster                                                     |
| scimark_fft              | 361 ms                                                       | 291 ms: 1.24x faster                                                      |
| chameleon                | 9.44 ms                                                      | 7.66 ms: 1.23x faster                                                     |
| json_loads               | 30.3 us                                                      | 24.6 us: 1.23x faster                                                     |
| dulwich_log              | 81.1 ms                                                      | 66.5 ms: 1.22x faster                                                     |
| django_template          | 50.2 ms                                                      | 41.2 ms: 1.22x faster                                                     |
| bench_thread_pool        | 1.14 ms                                                      | 948 us: 1.20x faster                                                      |
| mdp                      | 3.01 sec                                                     | 2.55 sec: 1.18x faster                                                    |
| nqueens                  | 115 ms                                                       | 97.8 ms: 1.17x faster                                                     |
| sympy_sum                | 193 ms                                                       | 166 ms: 1.16x faster                                                      |
| dask                     | 472 ms                                                       | 406 ms: 1.16x faster                                                      |
| sympy_str                | 360 ms                                                       | 312 ms: 1.15x faster                                                      |
| 2to3                     | 350 ms                                                       | 305 ms: 1.15x faster                                                      |
| deepcopy                 | 468 us                                                       | 411 us: 1.14x faster                                                      |
| sympy_expand             | 600 ms                                                       | 528 ms: 1.14x faster                                                      |
| xml_etree_generate       | 92.3 ms                                                      | 82.2 ms: 1.12x faster                                                     |
| genshi_text              | 31.4 ms                                                      | 28.2 ms: 1.11x faster                                                     |
| json                     | 5.86 ms                                                      | 5.28 ms: 1.11x faster                                                     |
| sqlglot_optimize         | 70.1 ms                                                      | 63.5 ms: 1.10x faster                                                     |
| async_generators         | 421 ms                                                       | 381 ms: 1.10x faster                                                      |
| xml_etree_iterparse      | 110 ms                                                       | 100 ms: 1.10x faster                                                      |
| sympy_integrate          | 28.2 ms                                                      | 25.6 ms: 1.10x faster                                                     |
| sqlglot_normalize        | 144 ms                                                       | 131 ms: 1.10x faster                                                      |
| xml_etree_parse          | 160 ms                                                       | 146 ms: 1.10x faster                                                      |
| sqlite_synth             | 2.99 us                                                      | 2.76 us: 1.08x faster                                                     |
| deepcopy_reduce          | 4.01 us                                                      | 3.71 us: 1.08x faster                                                     |
| meteor_contest           | 138 ms                                                       | 128 ms: 1.08x faster                                                      |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                      |
| regex_dna                | 261 ms                                                       | 243 ms: 1.07x faster                                                      |
| regex_v8                 | 27.2 ms                                                      | 25.5 ms: 1.06x faster                                                     |
| genshi_xml               | 63.3 ms                                                      | 64.8 ms: 1.02x slower                                                     |
| pickle_list              | 4.12 us                                                      | 4.40 us: 1.07x slower                                                     |
| pickle                   | 9.89 us                                                      | 10.6 us: 1.07x slower                                                     |
| pickle_dict              | 29.5 us                                                      | 32.4 us: 1.10x slower                                                     |
| unpickle                 | 13.5 us                                                      | 14.9 us: 1.11x slower                                                     |
| flaskblogging            | 4.39 ms                                                      | 4.91 ms: 1.12x slower                                                     |
| telco                    | 7.23 ms                                                      | 8.14 ms: 1.13x slower                                                     |
| create_gc_cycles         | 1.76 ms                                                      | 1.99 ms: 1.13x slower                                                     |
| python_startup           | 11.5 ms                                                      | 13.5 ms: 1.17x slower                                                     |
| regex_effbot             | 3.09 ms                                                      | 3.65 ms: 1.18x slower                                                     |
| python_startup_no_site   | 7.33 ms                                                      | 9.45 ms: 1.29x slower                                                     |
| coverage                 | 63.3 ms                                                      | 82.6 ms: 1.31x slower                                                     |
| gc_traversal             | 3.42 ms                                                      | 4.94 ms: 1.45x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.27x faster                                                              |

Benchmark hidden because not significant (2): asyncio_websockets, unpickle_list
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, docutils, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240523-3.14.0a0-0081bcd-JIT/bm-20240523-pythonperf2-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.22x