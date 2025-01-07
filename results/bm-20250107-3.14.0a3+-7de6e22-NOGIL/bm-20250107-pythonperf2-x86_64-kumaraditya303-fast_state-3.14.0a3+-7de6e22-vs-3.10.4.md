# Results vs. 3.10.4

- fork: kumaraditya303
- ref: fast_state
- machine: linux-x86_64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.045x faster
- HPT reliability: 99.34%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.53x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 383 ms: 1.09x slower                                                       |
| docutils       | 3.41 sec                                                     | 3.15 sec: 1.09x faster                                                     |
| Geometric mean | (ref)                                                        | 1.00x faster                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 765 ms: 2.09x faster                                                       |
| async_tree_none         | 692 ms                                                       | 357 ms: 1.94x faster                                                       |
| async_tree_memoization  | 819 ms                                                       | 442 ms: 1.85x faster                                                       |
| async_tree_cpu_io_mixed | 936 ms                                                       | 605 ms: 1.55x faster                                                       |
| Geometric mean          | (ref)                                                        | 1.85x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 271 ms                                                       | 248 ms: 1.09x faster                                                       |
| float          | 111 ms                                                       | 104 ms: 1.06x faster                                                       |
| nbody          | 134 ms                                                       | 132 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.06x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 172 ms: 1.10x faster                                                       |
| regex_dna      | 261 ms                                                       | 251 ms: 1.04x faster                                                       |
| regex_v8       | 27.2 ms                                                      | 26.3 ms: 1.03x faster                                                      |
| regex_effbot   | 3.09 ms                                                      | 3.31 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                        | 1.03x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 110 ms                                                       | 91.3 ms: 1.21x faster                                                      |
| xml_etree_parse      | 160 ms                                                       | 134 ms: 1.19x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.62 sec: 1.11x faster                                                     |
| json_loads           | 30.3 us                                                      | 28.1 us: 1.08x faster                                                      |
| json_dumps           | 14.5 ms                                                      | 14.4 ms: 1.01x faster                                                      |
| unpickle_pure_python | 312 us                                                       | 325 us: 1.04x slower                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 100 ms: 1.09x slower                                                       |
| pickle_pure_python   | 455 us                                                       | 514 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 12.0 ms: 1.64x slower                                                      |
| python_startup         | 11.5 ms                                                      | 19.1 ms: 1.66x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.65x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 31.4 ms                                                      | 33.0 ms: 1.05x slower                                                      |
| django_template | 50.2 ms                                                      | 53.4 ms: 1.06x slower                                                      |
| genshi_xml      | 63.3 ms                                                      | 67.8 ms: 1.07x slower                                                      |
| mako            | 14.7 ms                                                      | 19.4 ms: 1.32x slower                                                      |
| Geometric mean  | (ref)                                                        | 1.12x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 231 us: 2.32x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 765 ms: 2.09x faster                                                       |
| async_tree_none          | 692 ms                                                       | 357 ms: 1.94x faster                                                       |
| async_tree_memoization   | 819 ms                                                       | 442 ms: 1.85x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 605 ms: 1.55x faster                                                       |
| pylint                   | 566 ms                                                       | 380 ms: 1.49x faster                                                       |
| generators               | 57.3 ms                                                      | 38.7 ms: 1.48x faster                                                      |
| deepcopy                 | 468 us                                                       | 348 us: 1.34x faster                                                       |
| spectral_norm            | 139 ms                                                       | 105 ms: 1.32x faster                                                       |
| coroutines               | 30.3 ms                                                      | 23.3 ms: 1.30x faster                                                      |
| deepcopy_memo            | 49.8 us                                                      | 39.2 us: 1.27x faster                                                      |
| scimark_lu               | 167 ms                                                       | 133 ms: 1.26x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 17.1 ms: 1.25x faster                                                      |
| xml_etree_iterparse      | 110 ms                                                       | 91.3 ms: 1.21x faster                                                      |
| crypto_pyaes             | 119 ms                                                       | 99.2 ms: 1.20x faster                                                      |
| xml_etree_parse          | 160 ms                                                       | 134 ms: 1.19x faster                                                       |
| richards_super           | 90.6 ms                                                      | 77.9 ms: 1.16x faster                                                      |
| pycparser                | 1.67 sec                                                     | 1.45 sec: 1.15x faster                                                     |
| sqlite_synth             | 2.99 us                                                      | 2.64 us: 1.13x faster                                                      |
| chaos                    | 109 ms                                                       | 96.4 ms: 1.13x faster                                                      |
| pyflate                  | 733 ms                                                       | 654 ms: 1.12x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.62 sec: 1.11x faster                                                     |
| regex_compile            | 190 ms                                                       | 172 ms: 1.10x faster                                                       |
| pidigits                 | 271 ms                                                       | 248 ms: 1.09x faster                                                       |
| docutils                 | 3.41 sec                                                     | 3.15 sec: 1.09x faster                                                     |
| json_loads               | 30.3 us                                                      | 28.1 us: 1.08x faster                                                      |
| richards                 | 75.1 ms                                                      | 70.0 ms: 1.07x faster                                                      |
| go                       | 262 ms                                                       | 245 ms: 1.07x faster                                                       |
| float                    | 111 ms                                                       | 104 ms: 1.06x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.78 us: 1.06x faster                                                      |
| thrift                   | 1.18 ms                                                      | 1.11 ms: 1.06x faster                                                      |
| sympy_sum                | 193 ms                                                       | 183 ms: 1.05x faster                                                       |
| deltablue                | 7.50 ms                                                      | 7.14 ms: 1.05x faster                                                      |
| json                     | 5.86 ms                                                      | 5.59 ms: 1.05x faster                                                      |
| scimark_fft              | 361 ms                                                       | 345 ms: 1.05x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.88 sec: 1.04x faster                                                     |
| regex_dna                | 261 ms                                                       | 251 ms: 1.04x faster                                                       |
| raytrace                 | 489 ms                                                       | 471 ms: 1.04x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 78.3 ms: 1.04x faster                                                      |
| regex_v8                 | 27.2 ms                                                      | 26.3 ms: 1.03x faster                                                      |
| asyncio_websockets       | 390 ms                                                       | 379 ms: 1.03x faster                                                       |
| logging_silent           | 167 ns                                                       | 164 ns: 1.02x faster                                                       |
| nqueens                  | 115 ms                                                       | 113 ms: 1.02x faster                                                       |
| logging_simple           | 8.88 us                                                      | 8.72 us: 1.02x faster                                                      |
| nbody                    | 134 ms                                                       | 132 ms: 1.01x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 9.32 ms: 1.01x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 1.04 sec: 1.01x faster                                                     |
| json_dumps               | 14.5 ms                                                      | 14.4 ms: 1.01x faster                                                      |
| logging_format           | 9.64 us                                                      | 9.59 us: 1.01x faster                                                      |
| pprint_pformat           | 2.15 sec                                                     | 2.17 sec: 1.01x slower                                                     |
| sympy_integrate          | 28.2 ms                                                      | 28.5 ms: 1.01x slower                                                      |
| sqlglot_normalize        | 144 ms                                                       | 145 ms: 1.01x slower                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 109 ms: 1.02x slower                                                       |
| comprehensions           | 26.7 us                                                      | 27.2 us: 1.02x slower                                                      |
| sqlglot_optimize         | 70.1 ms                                                      | 72.6 ms: 1.03x slower                                                      |
| unpickle_pure_python     | 312 us                                                       | 325 us: 1.04x slower                                                       |
| genshi_text              | 31.4 ms                                                      | 33.0 ms: 1.05x slower                                                      |
| sqlglot_parse            | 2.24 ms                                                      | 2.35 ms: 1.05x slower                                                      |
| sqlglot_transpile        | 2.68 ms                                                      | 2.82 ms: 1.05x slower                                                      |
| sqlalchemy_declarative   | 190 ms                                                       | 201 ms: 1.06x slower                                                       |
| django_template          | 50.2 ms                                                      | 53.4 ms: 1.06x slower                                                      |
| fannkuch                 | 483 ms                                                       | 516 ms: 1.07x slower                                                       |
| genshi_xml               | 63.3 ms                                                      | 67.8 ms: 1.07x slower                                                      |
| regex_effbot             | 3.09 ms                                                      | 3.31 ms: 1.07x slower                                                      |
| scimark_sor              | 180 ms                                                       | 194 ms: 1.08x slower                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.51 ms: 1.09x slower                                                      |
| xml_etree_generate       | 92.3 ms                                                      | 100 ms: 1.09x slower                                                       |
| 2to3                     | 350 ms                                                       | 383 ms: 1.09x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 3.81 ms: 1.12x slower                                                      |
| meteor_contest           | 138 ms                                                       | 156 ms: 1.13x slower                                                       |
| pickle_pure_python       | 455 us                                                       | 514 us: 1.13x slower                                                       |
| async_generators         | 421 ms                                                       | 515 ms: 1.22x slower                                                       |
| telco                    | 7.23 ms                                                      | 9.52 ms: 1.32x slower                                                      |
| mako                     | 14.7 ms                                                      | 19.4 ms: 1.32x slower                                                      |
| bench_thread_pool        | 1.14 ms                                                      | 1.55 ms: 1.36x slower                                                      |
| mypy2                    | 933 ms                                                       | 1.31 sec: 1.40x slower                                                     |
| create_gc_cycles         | 1.76 ms                                                      | 2.84 ms: 1.61x slower                                                      |
| python_startup_no_site   | 7.33 ms                                                      | 12.0 ms: 1.64x slower                                                      |
| python_startup           | 11.5 ms                                                      | 19.1 ms: 1.66x slower                                                      |
| coverage                 | 63.3 ms                                                      | 106 ms: 1.67x slower                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 52.5 ms: 8.23x slower                                                      |
| Geometric mean           | (ref)                                                        | 1.02x faster                                                               |

Benchmark hidden because not significant (5): html5lib, sympy_str, xml_etree_process, sympy_expand, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250107-3.14.0a3+-7de6e22-NOGIL/bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.045x faster

# HPT report

- Reliability score: 99.34% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.53x