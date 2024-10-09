# Results vs. 3.10.4

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: aa18ec3
- commit date: 2024-10-07
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 317 ms: 1.10x faster                                                 |
| docutils       | 3.41 sec                                                     | 3.19 sec: 1.07x faster                                               |
| html5lib       | 94.6 ms                                                      | 73.1 ms: 1.29x faster                                                |
| tornado_http   | 157 ms                                                       | 122 ms: 1.29x faster                                                 |
| Geometric mean | (ref)                                                        | 1.18x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 327 ms: 2.11x faster                                                 |
| async_tree_memoization  | 819 ms                                                       | 406 ms: 2.02x faster                                                 |
| async_tree_io           | 1.60 sec                                                     | 804 ms: 1.99x faster                                                 |
| async_tree_cpu_io_mixed | 936 ms                                                       | 580 ms: 1.61x faster                                                 |
| Geometric mean          | (ref)                                                        | 1.92x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 84.2 ms: 1.59x faster                                                |
| float          | 111 ms                                                       | 75.8 ms: 1.47x faster                                                |
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                        | 1.36x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 152 ms: 1.25x faster                                                 |
| regex_v8       | 27.2 ms                                                      | 24.7 ms: 1.10x faster                                                |
| regex_dna      | 261 ms                                                       | 245 ms: 1.07x faster                                                 |
| regex_effbot   | 3.09 ms                                                      | 3.43 ms: 1.11x slower                                                |
| Geometric mean | (ref)                                                        | 1.07x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 215 us: 1.45x faster                                                 |
| json_dumps           | 14.5 ms                                                      | 10.5 ms: 1.39x faster                                                |
| pickle_pure_python   | 455 us                                                       | 329 us: 1.38x faster                                                 |
| xml_etree_process    | 75.9 ms                                                      | 56.2 ms: 1.35x faster                                                |
| tomli_loads          | 2.92 sec                                                     | 2.17 sec: 1.34x faster                                               |
| json_loads           | 30.3 us                                                      | 23.8 us: 1.27x faster                                                |
| xml_etree_generate   | 92.3 ms                                                      | 78.0 ms: 1.18x faster                                                |
| xml_etree_parse      | 160 ms                                                       | 140 ms: 1.15x faster                                                 |
| xml_etree_iterparse  | 110 ms                                                       | 98.4 ms: 1.12x faster                                                |
| pickle_list          | 4.12 us                                                      | 4.20 us: 1.02x slower                                                |
| unpickle_list        | 4.65 us                                                      | 4.76 us: 1.02x slower                                                |
| pickle_dict          | 29.5 us                                                      | 30.8 us: 1.04x slower                                                |
| pickle               | 9.89 us                                                      | 10.3 us: 1.05x slower                                                |
| unpickle             | 13.5 us                                                      | 15.6 us: 1.15x slower                                                |
| Geometric mean       | (ref)                                                        | 1.15x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                |
| python_startup_no_site | 7.33 ms                                                      | 8.96 ms: 1.22x slower                                                |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.20 ms: 1.60x faster                                                |
| django_template | 50.2 ms                                                      | 43.2 ms: 1.16x faster                                                |
| genshi_text     | 31.4 ms                                                      | 29.0 ms: 1.08x faster                                                |
| genshi_xml      | 63.3 ms                                                      | 64.4 ms: 1.02x slower                                                |
| Geometric mean  | (ref)                                                        | 1.19x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 189 us: 2.84x faster                                                 |
| deltablue                | 7.50 ms                                                      | 3.21 ms: 2.34x faster                                                |
| async_tree_none          | 692 ms                                                       | 327 ms: 2.11x faster                                                 |
| asyncio_tcp              | 779 ms                                                       | 369 ms: 2.11x faster                                                 |
| async_tree_memoization   | 819 ms                                                       | 406 ms: 2.02x faster                                                 |
| async_tree_io            | 1.60 sec                                                     | 804 ms: 1.99x faster                                                 |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                               |
| deepcopy_memo            | 49.8 us                                                      | 27.7 us: 1.80x faster                                                |
| richards_super           | 90.6 ms                                                      | 50.6 ms: 1.79x faster                                                |
| scimark_lu               | 167 ms                                                       | 96.9 ms: 1.72x faster                                                |
| go                       | 262 ms                                                       | 154 ms: 1.70x faster                                                 |
| richards                 | 75.1 ms                                                      | 44.2 ms: 1.70x faster                                                |
| logging_silent           | 167 ns                                                       | 98.9 ns: 1.69x faster                                                |
| scimark_sor              | 180 ms                                                       | 107 ms: 1.69x faster                                                 |
| crypto_pyaes             | 119 ms                                                       | 70.7 ms: 1.68x faster                                                |
| spectral_norm            | 139 ms                                                       | 83.3 ms: 1.67x faster                                                |
| chaos                    | 109 ms                                                       | 66.8 ms: 1.63x faster                                                |
| pyflate                  | 733 ms                                                       | 451 ms: 1.62x faster                                                 |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 580 ms: 1.61x faster                                                 |
| mako                     | 14.7 ms                                                      | 9.20 ms: 1.60x faster                                                |
| nbody                    | 134 ms                                                       | 84.2 ms: 1.59x faster                                                |
| scimark_monte_carlo      | 107 ms                                                       | 68.7 ms: 1.56x faster                                                |
| deepcopy                 | 468 us                                                       | 299 us: 1.56x faster                                                 |
| raytrace                 | 489 ms                                                       | 322 ms: 1.52x faster                                                 |
| sqlglot_parse            | 2.24 ms                                                      | 1.52 ms: 1.47x faster                                                |
| float                    | 111 ms                                                       | 75.8 ms: 1.47x faster                                                |
| unpickle_pure_python     | 312 us                                                       | 215 us: 1.45x faster                                                 |
| generators               | 57.3 ms                                                      | 39.5 ms: 1.45x faster                                                |
| coroutines               | 30.3 ms                                                      | 21.2 ms: 1.43x faster                                                |
| comprehensions           | 26.7 us                                                      | 18.8 us: 1.42x faster                                                |
| pprint_safe_repr         | 1.05 sec                                                     | 755 ms: 1.39x faster                                                 |
| json_dumps               | 14.5 ms                                                      | 10.5 ms: 1.39x faster                                                |
| pickle_pure_python       | 455 us                                                       | 329 us: 1.38x faster                                                 |
| pylint                   | 566 ms                                                       | 414 ms: 1.37x faster                                                 |
| pprint_pformat           | 2.15 sec                                                     | 1.58 sec: 1.37x faster                                               |
| fannkuch                 | 483 ms                                                       | 356 ms: 1.36x faster                                                 |
| pathlib                  | 21.4 ms                                                      | 15.8 ms: 1.36x faster                                                |
| deepcopy_reduce          | 4.01 us                                                      | 2.96 us: 1.35x faster                                                |
| sqlglot_transpile        | 2.68 ms                                                      | 1.98 ms: 1.35x faster                                                |
| xml_etree_process        | 75.9 ms                                                      | 56.2 ms: 1.35x faster                                                |
| tomli_loads              | 2.92 sec                                                     | 2.17 sec: 1.34x faster                                               |
| logging_format           | 9.64 us                                                      | 7.18 us: 1.34x faster                                                |
| logging_simple           | 8.88 us                                                      | 6.61 us: 1.34x faster                                                |
| hexiom                   | 9.42 ms                                                      | 7.06 ms: 1.33x faster                                                |
| pycparser                | 1.67 sec                                                     | 1.29 sec: 1.29x faster                                               |
| html5lib                 | 94.6 ms                                                      | 73.1 ms: 1.29x faster                                                |
| tornado_http             | 157 ms                                                       | 122 ms: 1.29x faster                                                 |
| thrift                   | 1.18 ms                                                      | 916 us: 1.28x faster                                                 |
| scimark_fft              | 361 ms                                                       | 283 ms: 1.28x faster                                                 |
| json_loads               | 30.3 us                                                      | 23.8 us: 1.27x faster                                                |
| dulwich_log              | 81.1 ms                                                      | 64.0 ms: 1.27x faster                                                |
| regex_compile            | 190 ms                                                       | 152 ms: 1.25x faster                                                 |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.14 ms: 1.23x faster                                                |
| bench_thread_pool        | 1.14 ms                                                      | 947 us: 1.20x faster                                                 |
| xml_etree_generate       | 92.3 ms                                                      | 78.0 ms: 1.18x faster                                                |
| mdp                      | 3.01 sec                                                     | 2.56 sec: 1.17x faster                                               |
| django_template          | 50.2 ms                                                      | 43.2 ms: 1.16x faster                                                |
| xml_etree_parse          | 160 ms                                                       | 140 ms: 1.15x faster                                                 |
| sympy_expand             | 600 ms                                                       | 525 ms: 1.14x faster                                                 |
| nqueens                  | 115 ms                                                       | 101 ms: 1.14x faster                                                 |
| sympy_str                | 360 ms                                                       | 318 ms: 1.13x faster                                                 |
| json                     | 5.86 ms                                                      | 5.20 ms: 1.13x faster                                                |
| xml_etree_iterparse      | 110 ms                                                       | 98.4 ms: 1.12x faster                                                |
| sympy_sum                | 193 ms                                                       | 173 ms: 1.12x faster                                                 |
| 2to3                     | 350 ms                                                       | 317 ms: 1.10x faster                                                 |
| sqlglot_normalize        | 144 ms                                                       | 130 ms: 1.10x faster                                                 |
| sqlite_synth             | 2.99 us                                                      | 2.71 us: 1.10x faster                                                |
| regex_v8                 | 27.2 ms                                                      | 24.7 ms: 1.10x faster                                                |
| async_generators         | 421 ms                                                       | 383 ms: 1.10x faster                                                 |
| pidigits                 | 271 ms                                                       | 250 ms: 1.08x faster                                                 |
| genshi_text              | 31.4 ms                                                      | 29.0 ms: 1.08x faster                                                |
| docutils                 | 3.41 sec                                                     | 3.19 sec: 1.07x faster                                               |
| regex_dna                | 261 ms                                                       | 245 ms: 1.07x faster                                                 |
| meteor_contest           | 138 ms                                                       | 133 ms: 1.04x faster                                                 |
| sympy_integrate          | 28.2 ms                                                      | 27.2 ms: 1.04x faster                                                |
| sqlglot_optimize         | 70.1 ms                                                      | 68.7 ms: 1.02x faster                                                |
| genshi_xml               | 63.3 ms                                                      | 64.4 ms: 1.02x slower                                                |
| pickle_list              | 4.12 us                                                      | 4.20 us: 1.02x slower                                                |
| unpickle_list            | 4.65 us                                                      | 4.76 us: 1.02x slower                                                |
| pickle_dict              | 29.5 us                                                      | 30.8 us: 1.04x slower                                                |
| pickle                   | 9.89 us                                                      | 10.3 us: 1.05x slower                                                |
| create_gc_cycles         | 1.76 ms                                                      | 1.87 ms: 1.06x slower                                                |
| telco                    | 7.23 ms                                                      | 7.71 ms: 1.07x slower                                                |
| regex_effbot             | 3.09 ms                                                      | 3.43 ms: 1.11x slower                                                |
| unpickle                 | 13.5 us                                                      | 15.6 us: 1.15x slower                                                |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                |
| python_startup_no_site   | 7.33 ms                                                      | 8.96 ms: 1.22x slower                                                |
| gc_traversal             | 3.42 ms                                                      | 4.30 ms: 1.26x slower                                                |
| coverage                 | 63.3 ms                                                      | 80.7 ms: 1.27x slower                                                |
| unpack_sequence          | 59.9 ns                                                      | 88.7 ns: 1.48x slower                                                |
| bench_mp_pool            | 6.37 ms                                                      | 4.58 sec: 719.38x slower                                             |
| Geometric mean           | (ref)                                                        | 1.20x faster                                                         |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241007-3.14.0a0-aa18ec3-JIT/bm-20241007-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a0-aa18ec3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.21x