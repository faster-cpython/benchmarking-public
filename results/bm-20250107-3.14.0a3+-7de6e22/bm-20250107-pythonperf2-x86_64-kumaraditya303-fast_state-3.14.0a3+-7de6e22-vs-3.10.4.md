# Results vs. 3.10.4

- fork: kumaraditya303
- ref: fast_state
- machine: linux-x86_64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.353x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 279 ms: 1.25x faster                                                       |
| docutils       | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                                     |
| html5lib       | 94.6 ms                                                      | 67.2 ms: 1.41x faster                                                      |
| Geometric mean | (ref)                                                        | 1.28x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 618 ms: 2.59x faster                                                       |
| async_tree_none         | 692 ms                                                       | 282 ms: 2.45x faster                                                       |
| async_tree_memoization  | 819 ms                                                       | 345 ms: 2.37x faster                                                       |
| async_tree_cpu_io_mixed | 936 ms                                                       | 511 ms: 1.83x faster                                                       |
| Geometric mean          | (ref)                                                        | 2.29x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 86.6 ms: 1.55x faster                                                      |
| float          | 111 ms                                                       | 72.3 ms: 1.54x faster                                                      |
| pidigits       | 271 ms                                                       | 254 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                        | 1.36x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 134 ms: 1.42x faster                                                       |
| regex_dna      | 261 ms                                                       | 231 ms: 1.13x faster                                                       |
| regex_v8       | 27.2 ms                                                      | 26.5 ms: 1.02x faster                                                      |
| regex_effbot   | 3.09 ms                                                      | 3.19 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                        | 1.12x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 206 us: 1.52x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.03 sec: 1.43x faster                                                     |
| pickle_pure_python   | 455 us                                                       | 326 us: 1.39x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 58.6 ms: 1.30x faster                                                      |
| json_dumps           | 14.5 ms                                                      | 11.5 ms: 1.27x faster                                                      |
| json_loads           | 30.3 us                                                      | 24.2 us: 1.25x faster                                                      |
| xml_etree_parse      | 160 ms                                                       | 137 ms: 1.17x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 95.1 ms: 1.16x faster                                                      |
| xml_etree_generate   | 92.3 ms                                                      | 82.2 ms: 1.12x faster                                                      |
| Geometric mean       | (ref)                                                        | 1.28x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.98 ms: 1.23x slower                                                      |
| python_startup         | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 36.1 ms: 1.39x faster                                                      |
| mako            | 14.7 ms                                                      | 11.0 ms: 1.33x faster                                                      |
| genshi_text     | 31.4 ms                                                      | 24.0 ms: 1.31x faster                                                      |
| genshi_xml      | 63.3 ms                                                      | 54.4 ms: 1.16x faster                                                      |
| Geometric mean  | (ref)                                                        | 1.30x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 173 us: 3.10x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 618 ms: 2.59x faster                                                       |
| async_tree_none          | 692 ms                                                       | 282 ms: 2.45x faster                                                       |
| async_tree_memoization   | 819 ms                                                       | 345 ms: 2.37x faster                                                       |
| deltablue                | 7.50 ms                                                      | 3.41 ms: 2.20x faster                                                      |
| generators               | 57.3 ms                                                      | 28.1 ms: 2.04x faster                                                      |
| go                       | 262 ms                                                       | 129 ms: 2.03x faster                                                       |
| raytrace                 | 489 ms                                                       | 266 ms: 1.84x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 511 ms: 1.83x faster                                                       |
| pylint                   | 566 ms                                                       | 318 ms: 1.78x faster                                                       |
| chaos                    | 109 ms                                                       | 62.3 ms: 1.74x faster                                                      |
| scimark_lu               | 167 ms                                                       | 95.8 ms: 1.74x faster                                                      |
| richards_super           | 90.6 ms                                                      | 52.3 ms: 1.73x faster                                                      |
| sqlglot_parse            | 2.24 ms                                                      | 1.32 ms: 1.69x faster                                                      |
| scimark_monte_carlo      | 107 ms                                                       | 63.5 ms: 1.69x faster                                                      |
| logging_silent           | 167 ns                                                       | 99.4 ns: 1.68x faster                                                      |
| deepcopy_memo            | 49.8 us                                                      | 29.6 us: 1.68x faster                                                      |
| deepcopy                 | 468 us                                                       | 280 us: 1.67x faster                                                       |
| pyflate                  | 733 ms                                                       | 440 ms: 1.67x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 73.0 ms: 1.63x faster                                                      |
| richards                 | 75.1 ms                                                      | 46.3 ms: 1.62x faster                                                      |
| scimark_sor              | 180 ms                                                       | 112 ms: 1.61x faster                                                       |
| spectral_norm            | 139 ms                                                       | 87.4 ms: 1.59x faster                                                      |
| sqlglot_transpile        | 2.68 ms                                                      | 1.71 ms: 1.56x faster                                                      |
| hexiom                   | 9.42 ms                                                      | 6.04 ms: 1.56x faster                                                      |
| nbody                    | 134 ms                                                       | 86.6 ms: 1.55x faster                                                      |
| float                    | 111 ms                                                       | 72.3 ms: 1.54x faster                                                      |
| unpickle_pure_python     | 312 us                                                       | 206 us: 1.52x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.7 us: 1.51x faster                                                      |
| coroutines               | 30.3 ms                                                      | 20.9 ms: 1.45x faster                                                      |
| tomli_loads              | 2.92 sec                                                     | 2.03 sec: 1.43x faster                                                     |
| logging_simple           | 8.88 us                                                      | 6.20 us: 1.43x faster                                                      |
| regex_compile            | 190 ms                                                       | 134 ms: 1.42x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 67.2 ms: 1.41x faster                                                      |
| logging_format           | 9.64 us                                                      | 6.89 us: 1.40x faster                                                      |
| pickle_pure_python       | 455 us                                                       | 326 us: 1.39x faster                                                       |
| django_template          | 50.2 ms                                                      | 36.1 ms: 1.39x faster                                                      |
| pprint_pformat           | 2.15 sec                                                     | 1.56 sec: 1.38x faster                                                     |
| deepcopy_reduce          | 4.01 us                                                      | 2.91 us: 1.38x faster                                                      |
| pycparser                | 1.67 sec                                                     | 1.22 sec: 1.37x faster                                                     |
| pprint_safe_repr         | 1.05 sec                                                     | 768 ms: 1.37x faster                                                       |
| fannkuch                 | 483 ms                                                       | 355 ms: 1.36x faster                                                       |
| thrift                   | 1.18 ms                                                      | 866 us: 1.36x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 15.9 ms: 1.34x faster                                                      |
| mako                     | 14.7 ms                                                      | 11.0 ms: 1.33x faster                                                      |
| sqlalchemy_declarative   | 190 ms                                                       | 144 ms: 1.32x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 24.0 ms: 1.31x faster                                                      |
| xml_etree_process        | 75.9 ms                                                      | 58.6 ms: 1.30x faster                                                      |
| nqueens                  | 115 ms                                                       | 89.5 ms: 1.28x faster                                                      |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.28x faster                                                       |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.8 ms: 1.27x faster                                                      |
| sqlglot_normalize        | 144 ms                                                       | 113 ms: 1.27x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 11.5 ms: 1.27x faster                                                      |
| 2to3                     | 350 ms                                                       | 279 ms: 1.25x faster                                                       |
| json_loads               | 30.3 us                                                      | 24.2 us: 1.25x faster                                                      |
| sympy_str                | 360 ms                                                       | 290 ms: 1.24x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 926 us: 1.23x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 23.0 ms: 1.23x faster                                                      |
| dulwich_log              | 81.1 ms                                                      | 66.2 ms: 1.22x faster                                                      |
| sqlglot_optimize         | 70.1 ms                                                      | 57.3 ms: 1.22x faster                                                      |
| mdp                      | 3.01 sec                                                     | 2.46 sec: 1.22x faster                                                     |
| scimark_fft              | 361 ms                                                       | 298 ms: 1.21x faster                                                       |
| sympy_expand             | 600 ms                                                       | 499 ms: 1.20x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                                     |
| xml_etree_parse          | 160 ms                                                       | 137 ms: 1.17x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 54.4 ms: 1.16x faster                                                      |
| xml_etree_iterparse      | 110 ms                                                       | 95.1 ms: 1.16x faster                                                      |
| json                     | 5.86 ms                                                      | 5.10 ms: 1.15x faster                                                      |
| regex_dna                | 261 ms                                                       | 231 ms: 1.13x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.52 ms: 1.12x faster                                                      |
| xml_etree_generate       | 92.3 ms                                                      | 82.2 ms: 1.12x faster                                                      |
| meteor_contest           | 138 ms                                                       | 126 ms: 1.10x faster                                                       |
| pidigits                 | 271 ms                                                       | 254 ms: 1.06x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.83 us: 1.05x faster                                                      |
| regex_v8                 | 27.2 ms                                                      | 26.5 ms: 1.02x faster                                                      |
| asyncio_websockets       | 390 ms                                                       | 384 ms: 1.02x faster                                                       |
| async_generators         | 421 ms                                                       | 430 ms: 1.02x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.19 ms: 1.03x slower                                                      |
| telco                    | 7.23 ms                                                      | 7.75 ms: 1.07x slower                                                      |
| mypy2                    | 933 ms                                                       | 1.02 sec: 1.10x slower                                                     |
| coverage                 | 63.3 ms                                                      | 76.7 ms: 1.21x slower                                                      |
| python_startup_no_site   | 7.33 ms                                                      | 8.98 ms: 1.23x slower                                                      |
| python_startup           | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                      |
| create_gc_cycles         | 1.76 ms                                                      | 2.75 ms: 1.56x slower                                                      |
| gc_traversal             | 3.42 ms                                                      | 6.15 ms: 1.80x slower                                                      |
| bench_mp_pool            | 6.37 ms                                                      | 1.31 sec: 206.18x slower                                                   |
| Geometric mean           | (ref)                                                        | 1.27x faster                                                               |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250107-3.14.0a3+-7de6e22/bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.353x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.28x