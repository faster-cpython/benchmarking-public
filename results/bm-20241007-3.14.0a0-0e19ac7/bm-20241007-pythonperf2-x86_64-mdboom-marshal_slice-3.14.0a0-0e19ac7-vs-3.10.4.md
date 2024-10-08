# Results vs. 3.10.4

- fork: mdboom
- ref: marshal_slice
- machine: linux-x86_64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.25x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 279 ms: 1.26x faster                                                 |
| docutils       | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                               |
| html5lib       | 94.6 ms                                                      | 70.8 ms: 1.34x faster                                                |
| tornado_http   | 157 ms                                                       | 115 ms: 1.36x faster                                                 |
| Geometric mean | (ref)                                                        | 1.28x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 318 ms: 2.17x faster                                                 |
| async_tree_memoization  | 819 ms                                                       | 398 ms: 2.06x faster                                                 |
| async_tree_io           | 1.60 sec                                                     | 806 ms: 1.98x faster                                                 |
| async_tree_cpu_io_mixed | 936 ms                                                       | 571 ms: 1.64x faster                                                 |
| Geometric mean          | (ref)                                                        | 1.95x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 87.3 ms: 1.54x faster                                                |
| float          | 111 ms                                                       | 78.8 ms: 1.41x faster                                                |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                 |
| Geometric mean | (ref)                                                        | 1.32x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 139 ms: 1.36x faster                                                 |
| regex_dna      | 261 ms                                                       | 252 ms: 1.04x faster                                                 |
| regex_v8       | 27.2 ms                                                      | 26.9 ms: 1.01x faster                                                |
| regex_effbot   | 3.09 ms                                                      | 3.50 ms: 1.13x slower                                                |
| Geometric mean | (ref)                                                        | 1.06x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 310 us: 1.47x faster                                                 |
| unpickle_pure_python | 312 us                                                       | 217 us: 1.44x faster                                                 |
| json_dumps           | 14.5 ms                                                      | 10.8 ms: 1.34x faster                                                |
| xml_etree_process    | 75.9 ms                                                      | 59.6 ms: 1.27x faster                                                |
| json_loads           | 30.3 us                                                      | 24.6 us: 1.23x faster                                                |
| tomli_loads          | 2.92 sec                                                     | 2.52 sec: 1.16x faster                                               |
| xml_etree_parse      | 160 ms                                                       | 140 ms: 1.15x faster                                                 |
| xml_etree_iterparse  | 110 ms                                                       | 98.5 ms: 1.12x faster                                                |
| xml_etree_generate   | 92.3 ms                                                      | 85.1 ms: 1.08x faster                                                |
| unpickle_list        | 4.65 us                                                      | 4.72 us: 1.01x slower                                                |
| pickle               | 9.89 us                                                      | 10.7 us: 1.08x slower                                                |
| pickle_dict          | 29.5 us                                                      | 32.4 us: 1.10x slower                                                |
| unpickle             | 13.5 us                                                      | 15.1 us: 1.12x slower                                                |
| pickle_list          | 4.12 us                                                      | 4.65 us: 1.13x slower                                                |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.5 ms: 1.17x slower                                                |
| python_startup_no_site | 7.33 ms                                                      | 9.01 ms: 1.23x slower                                                |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                |
| genshi_text     | 31.4 ms                                                      | 24.2 ms: 1.30x faster                                                |
| django_template | 50.2 ms                                                      | 39.0 ms: 1.29x faster                                                |
| genshi_xml      | 63.3 ms                                                      | 52.8 ms: 1.20x faster                                                |
| Geometric mean  | (ref)                                                        | 1.30x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 170 us: 3.15x faster                                                 |
| deltablue                | 7.50 ms                                                      | 3.38 ms: 2.22x faster                                                |
| async_tree_none          | 692 ms                                                       | 318 ms: 2.17x faster                                                 |
| asyncio_tcp              | 779 ms                                                       | 376 ms: 2.07x faster                                                 |
| async_tree_memoization   | 819 ms                                                       | 398 ms: 2.06x faster                                                 |
| generators               | 57.3 ms                                                      | 28.1 ms: 2.04x faster                                                |
| async_tree_io            | 1.60 sec                                                     | 806 ms: 1.98x faster                                                 |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                               |
| go                       | 262 ms                                                       | 133 ms: 1.96x faster                                                 |
| raytrace                 | 489 ms                                                       | 266 ms: 1.84x faster                                                 |
| scimark_lu               | 167 ms                                                       | 93.1 ms: 1.79x faster                                                |
| chaos                    | 109 ms                                                       | 62.5 ms: 1.74x faster                                                |
| deepcopy_memo            | 49.8 us                                                      | 29.0 us: 1.72x faster                                                |
| scimark_monte_carlo      | 107 ms                                                       | 63.8 ms: 1.68x faster                                                |
| logging_silent           | 167 ns                                                       | 99.3 ns: 1.68x faster                                                |
| crypto_pyaes             | 119 ms                                                       | 72.3 ms: 1.65x faster                                                |
| deepcopy                 | 468 us                                                       | 285 us: 1.64x faster                                                 |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 571 ms: 1.64x faster                                                 |
| pylint                   | 566 ms                                                       | 346 ms: 1.64x faster                                                 |
| richards_super           | 90.6 ms                                                      | 55.8 ms: 1.63x faster                                                |
| scimark_sor              | 180 ms                                                       | 111 ms: 1.62x faster                                                 |
| sqlglot_parse            | 2.24 ms                                                      | 1.41 ms: 1.59x faster                                                |
| comprehensions           | 26.7 us                                                      | 17.3 us: 1.54x faster                                                |
| nbody                    | 134 ms                                                       | 87.3 ms: 1.54x faster                                                |
| hexiom                   | 9.42 ms                                                      | 6.16 ms: 1.53x faster                                                |
| pyflate                  | 733 ms                                                       | 488 ms: 1.50x faster                                                 |
| sqlglot_transpile        | 2.68 ms                                                      | 1.79 ms: 1.50x faster                                                |
| richards                 | 75.1 ms                                                      | 50.8 ms: 1.48x faster                                                |
| pickle_pure_python       | 455 us                                                       | 310 us: 1.47x faster                                                 |
| coroutines               | 30.3 ms                                                      | 20.9 ms: 1.45x faster                                                |
| logging_simple           | 8.88 us                                                      | 6.14 us: 1.45x faster                                                |
| spectral_norm            | 139 ms                                                       | 96.8 ms: 1.44x faster                                                |
| unpickle_pure_python     | 312 us                                                       | 217 us: 1.44x faster                                                 |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                |
| float                    | 111 ms                                                       | 78.8 ms: 1.41x faster                                                |
| logging_format           | 9.64 us                                                      | 6.89 us: 1.40x faster                                                |
| deepcopy_reduce          | 4.01 us                                                      | 2.89 us: 1.39x faster                                                |
| pycparser                | 1.67 sec                                                     | 1.22 sec: 1.38x faster                                               |
| regex_compile            | 190 ms                                                       | 139 ms: 1.36x faster                                                 |
| thrift                   | 1.18 ms                                                      | 864 us: 1.36x faster                                                 |
| tornado_http             | 157 ms                                                       | 115 ms: 1.36x faster                                                 |
| pathlib                  | 21.4 ms                                                      | 15.7 ms: 1.36x faster                                                |
| fannkuch                 | 483 ms                                                       | 359 ms: 1.35x faster                                                 |
| json_dumps               | 14.5 ms                                                      | 10.8 ms: 1.34x faster                                                |
| html5lib                 | 94.6 ms                                                      | 70.8 ms: 1.34x faster                                                |
| pprint_pformat           | 2.15 sec                                                     | 1.63 sec: 1.32x faster                                               |
| pprint_safe_repr         | 1.05 sec                                                     | 797 ms: 1.32x faster                                                 |
| genshi_text              | 31.4 ms                                                      | 24.2 ms: 1.30x faster                                                |
| nqueens                  | 115 ms                                                       | 89.0 ms: 1.29x faster                                                |
| django_template          | 50.2 ms                                                      | 39.0 ms: 1.29x faster                                                |
| bench_thread_pool        | 1.14 ms                                                      | 895 us: 1.27x faster                                                 |
| xml_etree_process        | 75.9 ms                                                      | 59.6 ms: 1.27x faster                                                |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                 |
| scimark_fft              | 361 ms                                                       | 284 ms: 1.27x faster                                                 |
| 2to3                     | 350 ms                                                       | 279 ms: 1.26x faster                                                 |
| sympy_str                | 360 ms                                                       | 291 ms: 1.24x faster                                                 |
| json_loads               | 30.3 us                                                      | 24.6 us: 1.23x faster                                                |
| sqlglot_normalize        | 144 ms                                                       | 117 ms: 1.23x faster                                                 |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.17 ms: 1.22x faster                                                |
| dulwich_log              | 81.1 ms                                                      | 66.7 ms: 1.22x faster                                                |
| sympy_integrate          | 28.2 ms                                                      | 23.3 ms: 1.21x faster                                                |
| sympy_expand             | 600 ms                                                       | 497 ms: 1.21x faster                                                 |
| mdp                      | 3.01 sec                                                     | 2.50 sec: 1.20x faster                                               |
| genshi_xml               | 63.3 ms                                                      | 52.8 ms: 1.20x faster                                                |
| async_generators         | 421 ms                                                       | 353 ms: 1.19x faster                                                 |
| sqlglot_optimize         | 70.1 ms                                                      | 59.0 ms: 1.19x faster                                                |
| docutils                 | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                               |
| tomli_loads              | 2.92 sec                                                     | 2.52 sec: 1.16x faster                                               |
| xml_etree_parse          | 160 ms                                                       | 140 ms: 1.15x faster                                                 |
| json                     | 5.86 ms                                                      | 5.19 ms: 1.13x faster                                                |
| unpack_sequence          | 59.9 ns                                                      | 53.2 ns: 1.13x faster                                                |
| xml_etree_iterparse      | 110 ms                                                       | 98.5 ms: 1.12x faster                                                |
| meteor_contest           | 138 ms                                                       | 125 ms: 1.11x faster                                                 |
| sqlite_synth             | 2.99 us                                                      | 2.74 us: 1.09x faster                                                |
| xml_etree_generate       | 92.3 ms                                                      | 85.1 ms: 1.08x faster                                                |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                 |
| regex_dna                | 261 ms                                                       | 252 ms: 1.04x faster                                                 |
| regex_v8                 | 27.2 ms                                                      | 26.9 ms: 1.01x faster                                                |
| unpickle_list            | 4.65 us                                                      | 4.72 us: 1.01x slower                                                |
| pickle                   | 9.89 us                                                      | 10.7 us: 1.08x slower                                                |
| pickle_dict              | 29.5 us                                                      | 32.4 us: 1.10x slower                                                |
| telco                    | 7.23 ms                                                      | 7.96 ms: 1.10x slower                                                |
| unpickle                 | 13.5 us                                                      | 15.1 us: 1.12x slower                                                |
| pickle_list              | 4.12 us                                                      | 4.65 us: 1.13x slower                                                |
| regex_effbot             | 3.09 ms                                                      | 3.50 ms: 1.13x slower                                                |
| create_gc_cycles         | 1.76 ms                                                      | 2.02 ms: 1.14x slower                                                |
| python_startup           | 11.5 ms                                                      | 13.5 ms: 1.17x slower                                                |
| python_startup_no_site   | 7.33 ms                                                      | 9.01 ms: 1.23x slower                                                |
| coverage                 | 63.3 ms                                                      | 83.6 ms: 1.32x slower                                                |
| gc_traversal             | 3.42 ms                                                      | 4.53 ms: 1.33x slower                                                |
| bench_mp_pool            | 6.37 ms                                                      | 1.98 sec: 310.22x slower                                             |
| Geometric mean           | (ref)                                                        | 1.25x faster                                                         |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241007-3.14.0a0-0e19ac7/bm-20241007-pythonperf2-x86_64-mdboom-marshal_slice-3.14.0a0-0e19ac7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.12x