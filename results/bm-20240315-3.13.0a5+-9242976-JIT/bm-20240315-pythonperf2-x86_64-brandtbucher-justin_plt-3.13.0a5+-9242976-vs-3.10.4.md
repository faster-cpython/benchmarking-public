# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_plt
- machine: linux-x86_64
- commit hash: 9242976
- commit date: 2024-03-15
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 308 ms: 1.14x faster                                                     |
| chameleon      | 9.44 ms                                                      | 7.33 ms: 1.29x faster                                                    |
| docutils       | 3.41 sec                                                     | 2.96 sec: 1.15x faster                                                   |
| html5lib       | 94.6 ms                                                      | 74.7 ms: 1.27x faster                                                    |
| tornado_http   | 157 ms                                                       | 125 ms: 1.25x faster                                                     |
| Geometric mean | (ref)                                                        | 1.22x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 438 ms: 1.58x faster                                                     |
| async_tree_memoization  | 819 ms                                                       | 550 ms: 1.49x faster                                                     |
| async_tree_io           | 1.60 sec                                                     | 1.09 sec: 1.46x faster                                                   |
| async_tree_cpu_io_mixed | 936 ms                                                       | 701 ms: 1.34x faster                                                     |
| Geometric mean          | (ref)                                                        | 1.46x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 79.2 ms: 1.40x faster                                                    |
| nbody          | 134 ms                                                       | 103 ms: 1.30x faster                                                     |
| pidigits       | 271 ms                                                       | 262 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                        | 1.23x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 152 ms: 1.25x faster                                                     |
| regex_dna      | 261 ms                                                       | 236 ms: 1.11x faster                                                     |
| regex_v8       | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                                    |
| regex_effbot   | 3.09 ms                                                      | 3.54 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                        | 1.06x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 316 us: 1.44x faster                                                     |
| json_dumps           | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                                    |
| unpickle_pure_python | 312 us                                                       | 241 us: 1.30x faster                                                     |
| xml_etree_process    | 75.9 ms                                                      | 58.9 ms: 1.29x faster                                                    |
| tomli_loads          | 2.92 sec                                                     | 2.34 sec: 1.25x faster                                                   |
| json_loads           | 30.3 us                                                      | 25.0 us: 1.21x faster                                                    |
| xml_etree_parse      | 160 ms                                                       | 145 ms: 1.10x faster                                                     |
| xml_etree_generate   | 92.3 ms                                                      | 85.5 ms: 1.08x faster                                                    |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.06x faster                                                     |
| unpickle_list        | 4.65 us                                                      | 4.57 us: 1.02x faster                                                    |
| pickle               | 9.89 us                                                      | 10.7 us: 1.08x slower                                                    |
| pickle_list          | 4.12 us                                                      | 4.45 us: 1.08x slower                                                    |
| pickle_dict          | 29.5 us                                                      | 32.5 us: 1.10x slower                                                    |
| unpickle             | 13.5 us                                                      | 15.2 us: 1.12x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.11x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 14.2 ms: 1.23x slower                                                    |
| python_startup_no_site | 7.33 ms                                                      | 12.6 ms: 1.72x slower                                                    |
| Geometric mean         | (ref)                                                        | 1.46x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                                    |
| django_template | 50.2 ms                                                      | 38.4 ms: 1.31x faster                                                    |
| genshi_text     | 31.4 ms                                                      | 28.5 ms: 1.10x faster                                                    |
| genshi_xml      | 63.3 ms                                                      | 61.9 ms: 1.02x faster                                                    |
| Geometric mean  | (ref)                                                        | 1.20x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 120 us: 4.49x faster                                                     |
| asyncio_tcp              | 779 ms                                                       | 373 ms: 2.09x faster                                                     |
| deltablue                | 7.50 ms                                                      | 3.74 ms: 2.00x faster                                                    |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                   |
| logging_silent           | 167 ns                                                       | 97.5 ns: 1.72x faster                                                    |
| generators               | 57.3 ms                                                      | 34.2 ms: 1.68x faster                                                    |
| raytrace                 | 489 ms                                                       | 306 ms: 1.60x faster                                                     |
| async_tree_none          | 692 ms                                                       | 438 ms: 1.58x faster                                                     |
| richards_super           | 90.6 ms                                                      | 57.6 ms: 1.57x faster                                                    |
| pylint                   | 566 ms                                                       | 362 ms: 1.57x faster                                                     |
| sqlglot_parse            | 2.24 ms                                                      | 1.44 ms: 1.55x faster                                                    |
| chaos                    | 109 ms                                                       | 69.9 ms: 1.55x faster                                                    |
| crypto_pyaes             | 119 ms                                                       | 79.1 ms: 1.51x faster                                                    |
| go                       | 262 ms                                                       | 175 ms: 1.49x faster                                                     |
| async_tree_memoization   | 819 ms                                                       | 550 ms: 1.49x faster                                                     |
| async_tree_io            | 1.60 sec                                                     | 1.09 sec: 1.46x faster                                                   |
| richards                 | 75.1 ms                                                      | 51.5 ms: 1.46x faster                                                    |
| pickle_pure_python       | 455 us                                                       | 316 us: 1.44x faster                                                     |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                                    |
| sqlglot_transpile        | 2.68 ms                                                      | 1.88 ms: 1.43x faster                                                    |
| float                    | 111 ms                                                       | 79.2 ms: 1.40x faster                                                    |
| spectral_norm            | 139 ms                                                       | 101 ms: 1.38x faster                                                     |
| comprehensions           | 26.7 us                                                      | 19.3 us: 1.38x faster                                                    |
| json_dumps               | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                                    |
| thrift                   | 1.18 ms                                                      | 857 us: 1.37x faster                                                     |
| pyflate                  | 733 ms                                                       | 536 ms: 1.37x faster                                                     |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 701 ms: 1.34x faster                                                     |
| bench_mp_pool            | 6.37 ms                                                      | 4.77 ms: 1.34x faster                                                    |
| logging_simple           | 8.88 us                                                      | 6.66 us: 1.33x faster                                                    |
| deepcopy_memo            | 49.8 us                                                      | 37.4 us: 1.33x faster                                                    |
| coroutines               | 30.3 ms                                                      | 22.8 ms: 1.33x faster                                                    |
| logging_format           | 9.64 us                                                      | 7.28 us: 1.32x faster                                                    |
| scimark_monte_carlo      | 107 ms                                                       | 81.4 ms: 1.32x faster                                                    |
| django_template          | 50.2 ms                                                      | 38.4 ms: 1.31x faster                                                    |
| nbody                    | 134 ms                                                       | 103 ms: 1.30x faster                                                     |
| unpickle_pure_python     | 312 us                                                       | 241 us: 1.30x faster                                                     |
| chameleon                | 9.44 ms                                                      | 7.33 ms: 1.29x faster                                                    |
| xml_etree_process        | 75.9 ms                                                      | 58.9 ms: 1.29x faster                                                    |
| html5lib                 | 94.6 ms                                                      | 74.7 ms: 1.27x faster                                                    |
| tornado_http             | 157 ms                                                       | 125 ms: 1.25x faster                                                     |
| regex_compile            | 190 ms                                                       | 152 ms: 1.25x faster                                                     |
| tomli_loads              | 2.92 sec                                                     | 2.34 sec: 1.25x faster                                                   |
| scimark_lu               | 167 ms                                                       | 134 ms: 1.24x faster                                                     |
| deepcopy                 | 468 us                                                       | 378 us: 1.24x faster                                                     |
| hexiom                   | 9.42 ms                                                      | 7.68 ms: 1.23x faster                                                    |
| pycparser                | 1.67 sec                                                     | 1.37 sec: 1.23x faster                                                   |
| json_loads               | 30.3 us                                                      | 25.0 us: 1.21x faster                                                    |
| deepcopy_reduce          | 4.01 us                                                      | 3.30 us: 1.21x faster                                                    |
| pprint_pformat           | 2.15 sec                                                     | 1.80 sec: 1.20x faster                                                   |
| sqlglot_normalize        | 144 ms                                                       | 120 ms: 1.20x faster                                                     |
| sympy_sum                | 193 ms                                                       | 162 ms: 1.19x faster                                                     |
| pprint_safe_repr         | 1.05 sec                                                     | 883 ms: 1.19x faster                                                     |
| sympy_str                | 360 ms                                                       | 305 ms: 1.18x faster                                                     |
| dulwich_log              | 81.1 ms                                                      | 68.8 ms: 1.18x faster                                                    |
| dask                     | 472 ms                                                       | 405 ms: 1.17x faster                                                     |
| bench_thread_pool        | 1.14 ms                                                      | 979 us: 1.17x faster                                                     |
| sympy_expand             | 600 ms                                                       | 517 ms: 1.16x faster                                                     |
| docutils                 | 3.41 sec                                                     | 2.96 sec: 1.15x faster                                                   |
| scimark_sor              | 180 ms                                                       | 156 ms: 1.15x faster                                                     |
| mdp                      | 3.01 sec                                                     | 2.61 sec: 1.15x faster                                                   |
| 2to3                     | 350 ms                                                       | 308 ms: 1.14x faster                                                     |
| sympy_integrate          | 28.2 ms                                                      | 25.1 ms: 1.12x faster                                                    |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.56 ms: 1.11x faster                                                    |
| sqlglot_optimize         | 70.1 ms                                                      | 63.4 ms: 1.11x faster                                                    |
| regex_dna                | 261 ms                                                       | 236 ms: 1.11x faster                                                     |
| genshi_text              | 31.4 ms                                                      | 28.5 ms: 1.10x faster                                                    |
| xml_etree_parse          | 160 ms                                                       | 145 ms: 1.10x faster                                                     |
| create_gc_cycles         | 1.76 ms                                                      | 1.60 ms: 1.10x faster                                                    |
| sqlite_synth             | 2.99 us                                                      | 2.73 us: 1.09x faster                                                    |
| pathlib                  | 21.4 ms                                                      | 19.6 ms: 1.09x faster                                                    |
| json                     | 5.86 ms                                                      | 5.37 ms: 1.09x faster                                                    |
| nqueens                  | 115 ms                                                       | 106 ms: 1.08x faster                                                     |
| xml_etree_generate       | 92.3 ms                                                      | 85.5 ms: 1.08x faster                                                    |
| fannkuch                 | 483 ms                                                       | 448 ms: 1.08x faster                                                     |
| gunicorn                 | 1.16 ms                                                      | 1.08 ms: 1.07x faster                                                    |
| aiohttp                  | 1.19 ms                                                      | 1.11 ms: 1.07x faster                                                    |
| async_generators         | 421 ms                                                       | 395 ms: 1.06x faster                                                     |
| xml_etree_iterparse      | 110 ms                                                       | 104 ms: 1.06x faster                                                     |
| regex_v8                 | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                                    |
| meteor_contest           | 138 ms                                                       | 133 ms: 1.04x faster                                                     |
| pidigits                 | 271 ms                                                       | 262 ms: 1.03x faster                                                     |
| scimark_fft              | 361 ms                                                       | 353 ms: 1.02x faster                                                     |
| genshi_xml               | 63.3 ms                                                      | 61.9 ms: 1.02x faster                                                    |
| unpickle_list            | 4.65 us                                                      | 4.57 us: 1.02x faster                                                    |
| asyncio_websockets       | 390 ms                                                       | 386 ms: 1.01x faster                                                     |
| pickle                   | 9.89 us                                                      | 10.7 us: 1.08x slower                                                    |
| pickle_list              | 4.12 us                                                      | 4.45 us: 1.08x slower                                                    |
| pickle_dict              | 29.5 us                                                      | 32.5 us: 1.10x slower                                                    |
| unpickle                 | 13.5 us                                                      | 15.2 us: 1.12x slower                                                    |
| regex_effbot             | 3.09 ms                                                      | 3.54 ms: 1.15x slower                                                    |
| gc_traversal             | 3.42 ms                                                      | 3.92 ms: 1.15x slower                                                    |
| telco                    | 7.23 ms                                                      | 8.30 ms: 1.15x slower                                                    |
| python_startup           | 11.5 ms                                                      | 14.2 ms: 1.23x slower                                                    |
| coverage                 | 63.3 ms                                                      | 80.0 ms: 1.26x slower                                                    |
| unpack_sequence          | 59.9 ns                                                      | 80.1 ns: 1.34x slower                                                    |
| python_startup_no_site   | 7.33 ms                                                      | 12.6 ms: 1.72x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.22x faster                                                             |

Benchmark hidden because not significant (1): mypy2
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240315-3.13.0a5+-9242976-JIT/bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x


# Memory

- memory change: 1.23x