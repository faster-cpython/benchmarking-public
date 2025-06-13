# Results vs. 3.10.4

- fork: python
- ref: e6c3039cb39e68ae9af9
- machine: linux-x86_64
- commit hash: e6c3039
- commit date: 2025-06-12
- overall geometric mean: 1.148x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.36x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 321 ms: 1.09x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.13 sec: 1.09x faster                                                      |
| html5lib       | 94.6 ms                                                      | 70.2 ms: 1.35x faster                                                       |
| Geometric mean | (ref)                                                        | 1.17x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 666 ms: 2.40x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 356 ms: 2.30x faster                                                        |
| async_tree_none         | 692 ms                                                       | 307 ms: 2.25x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 531 ms: 1.76x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.16x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 105 ms: 1.05x faster                                                        |
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                                        |
| nbody          | 134 ms                                                       | 187 ms: 1.39x slower                                                        |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 160 ms: 1.19x faster                                                        |
| regex_dna      | 261 ms                                                       | 221 ms: 1.18x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 24.8 ms: 1.10x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.77 ms: 1.22x slower                                                       |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.0 us: 1.21x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 410 us: 1.11x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 107 ms: 1.03x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 75.0 ms: 1.01x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 3.17 sec: 1.09x slower                                                      |
| xml_etree_generate   | 92.3 ms                                                      | 107 ms: 1.16x slower                                                        |
| unpickle_pure_python | 312 us                                                       | 382 us: 1.22x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.80 ms: 1.20x slower                                                       |
| python_startup         | 11.5 ms                                                      | 15.2 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.26x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 36.0 ms: 1.40x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 23.5 ms: 1.34x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 56.0 ms: 1.13x faster                                                       |
| mako            | 14.7 ms                                                      | 16.8 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.17x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 202 us: 2.65x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 666 ms: 2.40x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 356 ms: 2.30x faster                                                        |
| async_tree_none          | 692 ms                                                       | 307 ms: 2.25x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.46 sec: 2.06x faster                                                      |
| generators               | 57.3 ms                                                      | 29.9 ms: 1.91x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 27.4 us: 1.82x faster                                                       |
| scimark_lu               | 167 ms                                                       | 93.5 ms: 1.78x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 531 ms: 1.76x faster                                                        |
| scimark_sor              | 180 ms                                                       | 104 ms: 1.73x faster                                                        |
| chaos                    | 109 ms                                                       | 63.9 ms: 1.70x faster                                                       |
| pylint                   | 566 ms                                                       | 333 ms: 1.70x faster                                                        |
| deepcopy                 | 468 us                                                       | 280 us: 1.67x faster                                                        |
| richards_super           | 90.6 ms                                                      | 61.1 ms: 1.48x faster                                                       |
| raytrace                 | 489 ms                                                       | 334 ms: 1.46x faster                                                        |
| django_template          | 50.2 ms                                                      | 36.0 ms: 1.40x faster                                                       |
| thrift                   | 1.18 ms                                                      | 843 us: 1.39x faster                                                        |
| richards                 | 75.1 ms                                                      | 54.2 ms: 1.38x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.3 ms: 1.36x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.97 us: 1.35x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 70.2 ms: 1.35x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.61 us: 1.34x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 23.5 ms: 1.34x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.26 us: 1.33x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 61.8 ms: 1.31x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                                       |
| deltablue                | 7.50 ms                                                      | 5.92 ms: 1.27x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 17.4 ms: 1.23x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 87.7 ms: 1.23x faster                                                       |
| json_loads               | 30.3 us                                                      | 25.0 us: 1.21x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 23.6 ms: 1.19x faster                                                       |
| sympy_sum                | 193 ms                                                       | 162 ms: 1.19x faster                                                        |
| regex_compile            | 190 ms                                                       | 160 ms: 1.19x faster                                                        |
| go                       | 262 ms                                                       | 220 ms: 1.19x faster                                                        |
| regex_dna                | 261 ms                                                       | 221 ms: 1.18x faster                                                        |
| sympy_str                | 360 ms                                                       | 314 ms: 1.15x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.47 sec: 1.14x faster                                                      |
| genshi_xml               | 63.3 ms                                                      | 56.0 ms: 1.13x faster                                                       |
| pyflate                  | 733 ms                                                       | 650 ms: 1.13x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 410 us: 1.11x faster                                                        |
| json                     | 5.86 ms                                                      | 5.29 ms: 1.11x faster                                                       |
| nqueens                  | 115 ms                                                       | 104 ms: 1.11x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 108 ms: 1.11x faster                                                        |
| sympy_expand             | 600 ms                                                       | 543 ms: 1.10x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 24.8 ms: 1.10x faster                                                       |
| 2to3                     | 350 ms                                                       | 321 ms: 1.09x faster                                                        |
| docutils                 | 3.41 sec                                                     | 3.13 sec: 1.09x faster                                                      |
| float                    | 111 ms                                                       | 105 ms: 1.05x faster                                                        |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 107 ms: 1.03x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 75.0 ms: 1.01x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 386 ms: 1.01x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 3.04 us: 1.02x slower                                                       |
| tomli_loads              | 2.92 sec                                                     | 3.17 sec: 1.09x slower                                                      |
| async_generators         | 421 ms                                                       | 460 ms: 1.09x slower                                                        |
| hexiom                   | 9.42 ms                                                      | 10.4 ms: 1.11x slower                                                       |
| pprint_pformat           | 2.15 sec                                                     | 2.40 sec: 1.11x slower                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 1.18 sec: 1.13x slower                                                      |
| comprehensions           | 26.7 us                                                      | 30.3 us: 1.14x slower                                                       |
| mako                     | 14.7 ms                                                      | 16.8 ms: 1.14x slower                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 107 ms: 1.16x slower                                                        |
| meteor_contest           | 138 ms                                                       | 164 ms: 1.18x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 8.80 ms: 1.20x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.77 ms: 1.22x slower                                                       |
| unpickle_pure_python     | 312 us                                                       | 382 us: 1.22x slower                                                        |
| telco                    | 7.23 ms                                                      | 9.18 ms: 1.27x slower                                                       |
| coverage                 | 63.3 ms                                                      | 80.5 ms: 1.27x slower                                                       |
| python_startup           | 11.5 ms                                                      | 15.2 ms: 1.33x slower                                                       |
| fannkuch                 | 483 ms                                                       | 644 ms: 1.33x slower                                                        |
| scimark_fft              | 361 ms                                                       | 493 ms: 1.36x slower                                                        |
| spectral_norm            | 139 ms                                                       | 191 ms: 1.37x slower                                                        |
| nbody                    | 134 ms                                                       | 187 ms: 1.39x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.88 ms: 1.63x slower                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 8.32 ms: 1.64x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 6.70 ms: 1.96x slower                                                       |
| logging_silent           | 167 ns                                                       | 504 ns: 3.01x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.13x faster                                                                |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250612-3.15.0a0-e6c3039-PYTHON_UOPS/bm-20250612-pythonperf2-x86_64-python-e6c3039cb39e68ae9af9-3.15.0a0-e6c3039.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.148x faster

# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.36x