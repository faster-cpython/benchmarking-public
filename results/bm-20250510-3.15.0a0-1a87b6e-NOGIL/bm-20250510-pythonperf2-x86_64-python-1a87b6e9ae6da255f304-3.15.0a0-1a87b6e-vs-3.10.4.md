# Results vs. 3.10.4

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-x86_64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.239x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 1.61x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 317 ms: 1.10x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                      |
| html5lib       | 94.6 ms                                                      | 69.9 ms: 1.35x faster                                                       |
| Geometric mean | (ref)                                                        | 1.21x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 560 ms: 2.85x faster                                                        |
| async_tree_none         | 692 ms                                                       | 265 ms: 2.61x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 321 ms: 2.55x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 502 ms: 1.86x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.44x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 71.6 ms: 1.55x faster                                                       |
| pidigits       | 271 ms                                                       | 252 ms: 1.08x faster                                                        |
| nbody          | 134 ms                                                       | 128 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                        | 1.21x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 156 ms: 1.22x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 23.8 ms: 1.14x faster                                                       |
| regex_dna      | 261 ms                                                       | 236 ms: 1.11x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.37 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 234 us: 1.34x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.28 sec: 1.28x faster                                                      |
| pickle_pure_python   | 455 us                                                       | 359 us: 1.27x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 88.4 ms: 1.25x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 138 ms: 1.16x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 69.9 ms: 1.09x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 13.7 ms: 1.06x faster                                                       |
| json_loads           | 30.3 us                                                      | 29.1 us: 1.04x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 99.6 ms: 1.08x slower                                                       |
| unpickle             | 13.5 us                                                      | 16.4 us: 1.22x slower                                                       |
| unpickle_list        | 4.65 us                                                      | 5.68 us: 1.22x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 36.1 us: 1.22x slower                                                       |
| pickle               | 9.89 us                                                      | 12.5 us: 1.26x slower                                                       |
| pickle_list          | 4.12 us                                                      | 5.27 us: 1.28x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 17.7 ms: 1.54x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 11.8 ms: 1.60x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.57x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 42.6 ms: 1.18x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 29.4 ms: 1.07x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 61.6 ms: 1.03x faster                                                       |
| mako            | 14.7 ms                                                      | 17.4 ms: 1.18x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io            | 1.60 sec                                                     | 560 ms: 2.85x faster                                                        |
| async_tree_none          | 692 ms                                                       | 265 ms: 2.61x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 321 ms: 2.55x faster                                                        |
| typing_runtime_protocols | 537 us                                                       | 218 us: 2.46x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.65 ms: 2.05x faster                                                       |
| mdp                      | 3.01 sec                                                     | 1.49 sec: 2.02x faster                                                      |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 502 ms: 1.86x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 423 ms: 1.84x faster                                                        |
| go                       | 262 ms                                                       | 143 ms: 1.83x faster                                                        |
| generators               | 57.3 ms                                                      | 32.2 ms: 1.78x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.88 sec: 1.65x faster                                                      |
| pylint                   | 566 ms                                                       | 350 ms: 1.62x faster                                                        |
| chaos                    | 109 ms                                                       | 67.4 ms: 1.61x faster                                                       |
| float                    | 111 ms                                                       | 71.6 ms: 1.55x faster                                                       |
| pyflate                  | 733 ms                                                       | 475 ms: 1.54x faster                                                        |
| scimark_sor              | 180 ms                                                       | 117 ms: 1.54x faster                                                        |
| gc_traversal             | 3.42 ms                                                      | 2.22 ms: 1.54x faster                                                       |
| raytrace                 | 489 ms                                                       | 323 ms: 1.51x faster                                                        |
| scimark_lu               | 167 ms                                                       | 111 ms: 1.51x faster                                                        |
| deepcopy                 | 468 us                                                       | 319 us: 1.47x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 34.1 us: 1.46x faster                                                       |
| richards_super           | 90.6 ms                                                      | 62.2 ms: 1.46x faster                                                       |
| richards                 | 75.1 ms                                                      | 54.2 ms: 1.38x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.83 ms: 1.38x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.0 ms: 1.38x faster                                                       |
| spectral_norm            | 139 ms                                                       | 103 ms: 1.36x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 69.9 ms: 1.35x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 234 us: 1.34x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                                      |
| comprehensions           | 26.7 us                                                      | 20.2 us: 1.32x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 81.9 ms: 1.31x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 62.7 ms: 1.29x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.28 sec: 1.28x faster                                                      |
| pickle_pure_python       | 455 us                                                       | 359 us: 1.27x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 94.8 ms: 1.26x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 88.4 ms: 1.25x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 17.3 ms: 1.24x faster                                                       |
| regex_compile            | 190 ms                                                       | 156 ms: 1.22x faster                                                        |
| logging_simple           | 8.88 us                                                      | 7.41 us: 1.20x faster                                                       |
| thrift                   | 1.18 ms                                                      | 995 us: 1.18x faster                                                        |
| django_template          | 50.2 ms                                                      | 42.6 ms: 1.18x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 893 ms: 1.18x faster                                                        |
| logging_format           | 9.64 us                                                      | 8.21 us: 1.17x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                      |
| pprint_pformat           | 2.15 sec                                                     | 1.84 sec: 1.17x faster                                                      |
| deepcopy_reduce          | 4.01 us                                                      | 3.42 us: 1.17x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 138 ms: 1.16x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 23.8 ms: 1.14x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.65 us: 1.13x faster                                                       |
| sympy_sum                | 193 ms                                                       | 172 ms: 1.12x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 25.4 ms: 1.11x faster                                                       |
| nqueens                  | 115 ms                                                       | 104 ms: 1.11x faster                                                        |
| regex_dna                | 261 ms                                                       | 236 ms: 1.11x faster                                                        |
| 2to3                     | 350 ms                                                       | 317 ms: 1.10x faster                                                        |
| sympy_str                | 360 ms                                                       | 328 ms: 1.10x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 69.9 ms: 1.09x faster                                                       |
| pidigits                 | 271 ms                                                       | 252 ms: 1.08x faster                                                        |
| sympy_expand             | 600 ms                                                       | 559 ms: 1.07x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 29.4 ms: 1.07x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 13.7 ms: 1.06x faster                                                       |
| unpack_sequence          | 59.9 ns                                                      | 57.0 ns: 1.05x faster                                                       |
| nbody                    | 134 ms                                                       | 128 ms: 1.05x faster                                                        |
| json_loads               | 30.3 us                                                      | 29.1 us: 1.04x faster                                                       |
| fannkuch                 | 483 ms                                                       | 463 ms: 1.04x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 379 ms: 1.03x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 61.6 ms: 1.03x faster                                                       |
| json                     | 5.86 ms                                                      | 5.71 ms: 1.03x faster                                                       |
| scimark_fft              | 361 ms                                                       | 356 ms: 1.02x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 99.6 ms: 1.08x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.37 ms: 1.09x slower                                                       |
| meteor_contest           | 138 ms                                                       | 154 ms: 1.12x slower                                                        |
| async_generators         | 421 ms                                                       | 484 ms: 1.15x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.04 ms: 1.15x slower                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.93 ms: 1.17x slower                                                       |
| mako                     | 14.7 ms                                                      | 17.4 ms: 1.18x slower                                                       |
| unpickle                 | 13.5 us                                                      | 16.4 us: 1.22x slower                                                       |
| unpickle_list            | 4.65 us                                                      | 5.68 us: 1.22x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 36.1 us: 1.22x slower                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 1.42 ms: 1.24x slower                                                       |
| pickle                   | 9.89 us                                                      | 12.5 us: 1.26x slower                                                       |
| telco                    | 7.23 ms                                                      | 9.20 ms: 1.27x slower                                                       |
| pickle_list              | 4.12 us                                                      | 5.27 us: 1.28x slower                                                       |
| python_startup           | 11.5 ms                                                      | 17.7 ms: 1.54x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 11.8 ms: 1.60x slower                                                       |
| coverage                 | 63.3 ms                                                      | 122 ms: 1.93x slower                                                        |
| logging_silent           | 167 ns                                                       | 608 ns: 3.64x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 57.1 ms: 8.96x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.16x faster                                                                |
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (7) of results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: bpe_tokeniser, many_optionals, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.239x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: 1.61x