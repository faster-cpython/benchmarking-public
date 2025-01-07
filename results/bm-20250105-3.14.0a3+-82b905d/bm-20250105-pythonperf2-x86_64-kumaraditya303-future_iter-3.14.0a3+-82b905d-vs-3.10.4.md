# Results vs. 3.10.4

- fork: kumaraditya303
- ref: future_iter
- machine: linux-x86_64
- commit hash: 82b905d
- commit date: 2025-01-05
- overall geometric mean: 1.349x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 280 ms: 1.25x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                                      |
| html5lib       | 94.6 ms                                                      | 66.8 ms: 1.42x faster                                                       |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 618 ms: 2.59x faster                                                        |
| async_tree_none         | 692 ms                                                       | 282 ms: 2.46x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 346 ms: 2.37x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 512 ms: 1.83x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.29x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 86.2 ms: 1.56x faster                                                       |
| float          | 111 ms                                                       | 71.8 ms: 1.55x faster                                                       |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.37x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 134 ms: 1.42x faster                                                        |
| regex_dna      | 261 ms                                                       | 245 ms: 1.07x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 26.8 ms: 1.01x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.25 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 201 us: 1.56x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.05 sec: 1.42x faster                                                      |
| pickle_pure_python   | 455 us                                                       | 326 us: 1.40x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 58.7 ms: 1.29x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 11.4 ms: 1.28x faster                                                       |
| json_loads           | 30.3 us                                                      | 24.6 us: 1.23x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 134 ms: 1.19x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 95.4 ms: 1.16x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 83.2 ms: 1.11x faster                                                       |
| Geometric mean       | (ref)                                                        | 1.29x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.02 ms: 1.23x slower                                                       |
| python_startup         | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.1 ms: 1.43x faster                                                       |
| mako            | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 23.9 ms: 1.32x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 52.5 ms: 1.21x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.32x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 171 us: 3.14x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 618 ms: 2.59x faster                                                        |
| async_tree_none          | 692 ms                                                       | 282 ms: 2.46x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 346 ms: 2.37x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.39 ms: 2.21x faster                                                       |
| go                       | 262 ms                                                       | 126 ms: 2.07x faster                                                        |
| generators               | 57.3 ms                                                      | 28.6 ms: 2.00x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 512 ms: 1.83x faster                                                        |
| raytrace                 | 489 ms                                                       | 268 ms: 1.83x faster                                                        |
| pylint                   | 566 ms                                                       | 315 ms: 1.80x faster                                                        |
| chaos                    | 109 ms                                                       | 60.9 ms: 1.78x faster                                                       |
| scimark_lu               | 167 ms                                                       | 94.8 ms: 1.76x faster                                                       |
| richards_super           | 90.6 ms                                                      | 52.2 ms: 1.73x faster                                                       |
| logging_silent           | 167 ns                                                       | 98.2 ns: 1.70x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.32 ms: 1.70x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 63.8 ms: 1.68x faster                                                       |
| deepcopy                 | 468 us                                                       | 282 us: 1.66x faster                                                        |
| scimark_sor              | 180 ms                                                       | 110 ms: 1.63x faster                                                        |
| pyflate                  | 733 ms                                                       | 451 ms: 1.63x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 30.7 us: 1.62x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 73.9 ms: 1.61x faster                                                       |
| richards                 | 75.1 ms                                                      | 46.6 ms: 1.61x faster                                                       |
| spectral_norm            | 139 ms                                                       | 87.7 ms: 1.59x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.72 ms: 1.56x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 201 us: 1.56x faster                                                        |
| nbody                    | 134 ms                                                       | 86.2 ms: 1.56x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.08 ms: 1.55x faster                                                       |
| float                    | 111 ms                                                       | 71.8 ms: 1.55x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.7 us: 1.50x faster                                                       |
| coroutines               | 30.3 ms                                                      | 20.6 ms: 1.47x faster                                                       |
| django_template          | 50.2 ms                                                      | 35.1 ms: 1.43x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.05 sec: 1.42x faster                                                      |
| html5lib                 | 94.6 ms                                                      | 66.8 ms: 1.42x faster                                                       |
| regex_compile            | 190 ms                                                       | 134 ms: 1.42x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 326 us: 1.40x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.36 us: 1.40x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.92 us: 1.39x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.55 sec: 1.39x faster                                                      |
| deepcopy_reduce          | 4.01 us                                                      | 2.91 us: 1.38x faster                                                       |
| thrift                   | 1.18 ms                                                      | 854 us: 1.38x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 767 ms: 1.37x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.36x faster                                                      |
| mako                     | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 15.9 ms: 1.34x faster                                                       |
| sqlalchemy_declarative   | 190 ms                                                       | 143 ms: 1.33x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 23.9 ms: 1.32x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 58.7 ms: 1.29x faster                                                       |
| fannkuch                 | 483 ms                                                       | 373 ms: 1.29x faster                                                        |
| sympy_sum                | 193 ms                                                       | 150 ms: 1.28x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.4 ms: 1.28x faster                                                       |
| nqueens                  | 115 ms                                                       | 90.5 ms: 1.27x faster                                                       |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.9 ms: 1.27x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 114 ms: 1.26x faster                                                        |
| 2to3                     | 350 ms                                                       | 280 ms: 1.25x faster                                                        |
| sympy_str                | 360 ms                                                       | 290 ms: 1.24x faster                                                        |
| json_loads               | 30.3 us                                                      | 24.6 us: 1.23x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 22.8 ms: 1.23x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 926 us: 1.23x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 66.3 ms: 1.22x faster                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 57.5 ms: 1.22x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.48 sec: 1.21x faster                                                      |
| genshi_xml               | 63.3 ms                                                      | 52.5 ms: 1.21x faster                                                       |
| sympy_expand             | 600 ms                                                       | 499 ms: 1.20x faster                                                        |
| scimark_fft              | 361 ms                                                       | 302 ms: 1.20x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 134 ms: 1.19x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                                      |
| xml_etree_iterparse      | 110 ms                                                       | 95.4 ms: 1.16x faster                                                       |
| json                     | 5.86 ms                                                      | 5.07 ms: 1.16x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 83.2 ms: 1.11x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.64 ms: 1.09x faster                                                       |
| meteor_contest           | 138 ms                                                       | 127 ms: 1.09x faster                                                        |
| regex_dna                | 261 ms                                                       | 245 ms: 1.07x faster                                                        |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.84 us: 1.05x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 26.8 ms: 1.01x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                                        |
| async_generators         | 421 ms                                                       | 437 ms: 1.04x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.25 ms: 1.05x slower                                                       |
| telco                    | 7.23 ms                                                      | 7.84 ms: 1.08x slower                                                       |
| mypy2                    | 933 ms                                                       | 1.02 sec: 1.09x slower                                                      |
| coverage                 | 63.3 ms                                                      | 77.3 ms: 1.22x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.02 ms: 1.23x slower                                                       |
| python_startup           | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.79 ms: 1.58x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 6.63 ms: 1.94x slower                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 891 ms: 139.76x slower                                                      |
| Geometric mean           | (ref)                                                        | 1.27x faster                                                                |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250105-3.14.0a3+-82b905d/bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.349x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.28x