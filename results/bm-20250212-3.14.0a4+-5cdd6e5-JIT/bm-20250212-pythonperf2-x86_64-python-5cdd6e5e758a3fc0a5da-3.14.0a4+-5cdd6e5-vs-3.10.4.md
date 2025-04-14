# Results vs. 3.10.4

- fork: python
- ref: 5cdd6e5e758a3fc0a5da
- machine: linux-x86_64
- commit hash: 5cdd6e5
- commit date: 2025-02-12
- overall geometric mean: 1.328x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 290 ms: 1.21x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.98 sec: 1.15x faster                                                       |
| html5lib       | 94.6 ms                                                      | 67.7 ms: 1.40x faster                                                        |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 654 ms: 2.44x faster                                                         |
| async_tree_none         | 692 ms                                                       | 292 ms: 2.37x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 356 ms: 2.30x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 526 ms: 1.78x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.21x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 70.5 ms: 1.58x faster                                                        |
| nbody          | 134 ms                                                       | 104 ms: 1.28x faster                                                         |
| pidigits       | 271 ms                                                       | 254 ms: 1.06x faster                                                         |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 137 ms: 1.39x faster                                                         |
| regex_dna      | 261 ms                                                       | 234 ms: 1.12x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.14x faster                                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 204 us: 1.53x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.06 sec: 1.41x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 56.1 ms: 1.35x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 337 us: 1.35x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 11.8 ms: 1.24x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 137 ms: 1.17x faster                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 79.8 ms: 1.16x faster                                                        |
| json_loads           | 30.3 us                                                      | 26.8 us: 1.13x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 98.4 ms: 1.12x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.27x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.02 ms: 1.23x slower                                                        |
| python_startup         | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.66 ms: 1.52x faster                                                        |
| django_template | 50.2 ms                                                      | 36.6 ms: 1.37x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 24.3 ms: 1.30x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 56.0 ms: 1.13x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.32x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 174 us: 3.08x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 654 ms: 2.44x faster                                                         |
| async_tree_none          | 692 ms                                                       | 292 ms: 2.37x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 356 ms: 2.30x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.53 ms: 2.13x faster                                                        |
| generators               | 57.3 ms                                                      | 28.5 ms: 2.01x faster                                                        |
| richards_super           | 90.6 ms                                                      | 50.8 ms: 1.78x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 526 ms: 1.78x faster                                                         |
| go                       | 262 ms                                                       | 148 ms: 1.77x faster                                                         |
| pylint                   | 566 ms                                                       | 321 ms: 1.76x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 61.1 ms: 1.76x faster                                                        |
| chaos                    | 109 ms                                                       | 62.0 ms: 1.75x faster                                                        |
| logging_silent           | 167 ns                                                       | 96.8 ns: 1.73x faster                                                        |
| pyflate                  | 733 ms                                                       | 425 ms: 1.72x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 29.0 us: 1.71x faster                                                        |
| deepcopy                 | 468 us                                                       | 278 us: 1.68x faster                                                         |
| richards                 | 75.1 ms                                                      | 44.9 ms: 1.67x faster                                                        |
| scimark_lu               | 167 ms                                                       | 100 ms: 1.67x faster                                                         |
| spectral_norm            | 139 ms                                                       | 83.9 ms: 1.66x faster                                                        |
| scimark_sor              | 180 ms                                                       | 109 ms: 1.65x faster                                                         |
| raytrace                 | 489 ms                                                       | 302 ms: 1.62x faster                                                         |
| sqlglot_parse            | 2.24 ms                                                      | 1.38 ms: 1.62x faster                                                        |
| float                    | 111 ms                                                       | 70.5 ms: 1.58x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 77.4 ms: 1.54x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 204 us: 1.53x faster                                                         |
| mako                     | 14.7 ms                                                      | 9.66 ms: 1.52x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.77 ms: 1.51x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.0 ms: 1.45x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.06 sec: 1.41x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.90 us: 1.40x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 67.7 ms: 1.40x faster                                                        |
| regex_compile            | 190 ms                                                       | 137 ms: 1.39x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 2.88 us: 1.39x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.41 us: 1.38x faster                                                        |
| comprehensions           | 26.7 us                                                      | 19.4 us: 1.38x faster                                                        |
| thrift                   | 1.18 ms                                                      | 857 us: 1.37x faster                                                         |
| django_template          | 50.2 ms                                                      | 36.6 ms: 1.37x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 56.1 ms: 1.35x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 337 us: 1.35x faster                                                         |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 7.14 ms: 1.32x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 803 ms: 1.31x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.65 sec: 1.30x faster                                                       |
| sqlalchemy_declarative   | 190 ms                                                       | 145 ms: 1.30x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 24.3 ms: 1.30x faster                                                        |
| nbody                    | 134 ms                                                       | 104 ms: 1.28x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 16.7 ms: 1.28x faster                                                        |
| fannkuch                 | 483 ms                                                       | 381 ms: 1.27x faster                                                         |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.0 ms: 1.26x faster                                                        |
| sympy_sum                | 193 ms                                                       | 155 ms: 1.24x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 11.8 ms: 1.24x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.21x faster                                                         |
| sympy_str                | 360 ms                                                       | 298 ms: 1.21x faster                                                         |
| 2to3                     | 350 ms                                                       | 290 ms: 1.21x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 67.6 ms: 1.20x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 23.6 ms: 1.19x faster                                                        |
| scimark_fft              | 361 ms                                                       | 306 ms: 1.18x faster                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 966 us: 1.18x faster                                                         |
| sympy_expand             | 600 ms                                                       | 508 ms: 1.18x faster                                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 59.9 ms: 1.17x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 137 ms: 1.17x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.60 sec: 1.16x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 79.8 ms: 1.16x faster                                                        |
| nqueens                  | 115 ms                                                       | 100.0 ms: 1.15x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.98 sec: 1.15x faster                                                       |
| json_loads               | 30.3 us                                                      | 26.8 us: 1.13x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 56.0 ms: 1.13x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 98.4 ms: 1.12x faster                                                        |
| regex_dna                | 261 ms                                                       | 234 ms: 1.12x faster                                                         |
| json                     | 5.86 ms                                                      | 5.43 ms: 1.08x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.78 us: 1.07x faster                                                        |
| pidigits                 | 271 ms                                                       | 254 ms: 1.06x faster                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.84 ms: 1.05x faster                                                        |
| meteor_contest           | 138 ms                                                       | 134 ms: 1.04x faster                                                         |
| async_generators         | 421 ms                                                       | 426 ms: 1.01x slower                                                         |
| telco                    | 7.23 ms                                                      | 7.76 ms: 1.07x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.02 ms: 1.23x slower                                                        |
| coverage                 | 63.3 ms                                                      | 82.8 ms: 1.31x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.73 ms: 1.55x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.50 ms: 1.90x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.55 sec: 243.62x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.24x faster                                                                 |

Benchmark hidden because not significant (2): asyncio_websockets, regex_effbot
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250212-3.14.0a4+-5cdd6e5-JIT/bm-20250212-pythonperf2-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.328x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.29x