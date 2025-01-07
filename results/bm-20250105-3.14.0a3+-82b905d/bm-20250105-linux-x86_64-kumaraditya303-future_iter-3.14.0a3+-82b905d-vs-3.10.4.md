# Results vs. 3.10.4

- fork: kumaraditya303
- ref: future_iter
- machine: linux-x86_64
- commit hash: 82b905d
- commit date: 2025-01-05
- overall geometric mean: 1.427x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 257 ms: 1.36x faster                                                  |
| docutils       | 3.30 sec                                               | 2.64 sec: 1.25x faster                                                |
| html5lib       | 88.9 ms                                                | 62.4 ms: 1.42x faster                                                 |
| Geometric mean | (ref)                                                  | 1.34x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 588 ms: 3.01x faster                                                  |
| async_tree_none         | 728 ms                                                 | 259 ms: 2.82x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 326 ms: 2.67x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 488 ms: 2.08x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 94.1 ms: 1.63x faster                                                 |
| float          | 117 ms                                                 | 72.5 ms: 1.61x faster                                                 |
| pidigits       | 191 ms                                                 | 190 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.38x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                  |
| regex_v8       | 27.8 ms                                                | 26.1 ms: 1.06x faster                                                 |
| regex_effbot   | 3.63 ms                                                | 3.47 ms: 1.05x faster                                                 |
| regex_dna      | 227 ms                                                 | 221 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.98 sec: 1.58x faster                                                |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 323 us: 1.50x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 59.5 ms: 1.33x faster                                                 |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 137 ms: 1.23x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 96.6 ms: 1.20x faster                                                 |
| json_loads           | 31.2 us                                                | 26.5 us: 1.18x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 85.1 ms: 1.17x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.5 ms: 1.53x faster                                                 |
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                 |
| genshi_text     | 31.8 ms                                                | 22.4 ms: 1.42x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 50.3 ms: 1.31x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.35x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 588 ms: 3.01x faster                                                  |
| generators               | 80.1 ms                                                | 27.6 ms: 2.90x faster                                                 |
| async_tree_none          | 728 ms                                                 | 259 ms: 2.82x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 326 ms: 2.67x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.28 ms: 2.41x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 488 ms: 2.08x faster                                                  |
| go                       | 240 ms                                                 | 119 ms: 2.02x faster                                                  |
| pylint                   | 551 ms                                                 | 279 ms: 1.98x faster                                                  |
| chaos                    | 115 ms                                                 | 61.2 ms: 1.89x faster                                                 |
| richards_super           | 94.7 ms                                                | 50.9 ms: 1.86x faster                                                 |
| raytrace                 | 507 ms                                                 | 272 ms: 1.86x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 31.5 us: 1.86x faster                                                 |
| deepcopy                 | 479 us                                                 | 261 us: 1.84x faster                                                  |
| logging_silent           | 190 ns                                                 | 104 ns: 1.83x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 71.3 ms: 1.79x faster                                                 |
| richards                 | 79.3 ms                                                | 44.4 ms: 1.79x faster                                                 |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.78x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 68.0 ms: 1.74x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.70x faster                                                 |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.68x faster                                                 |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.64x faster                                                  |
| nbody                    | 154 ms                                                 | 94.1 ms: 1.63x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.39 ms: 1.63x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                                 |
| float                    | 117 ms                                                 | 72.5 ms: 1.61x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.98 sec: 1.58x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                                 |
| django_template          | 48.2 ms                                                | 31.5 ms: 1.53x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                  |
| pyflate                  | 716 ms                                                 | 474 ms: 1.51x faster                                                  |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 323 us: 1.50x faster                                                  |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                  |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                  |
| logging_format           | 9.09 us                                                | 6.28 us: 1.45x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.76 us: 1.44x faster                                                 |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                 |
| html5lib                 | 88.9 ms                                                | 62.4 ms: 1.42x faster                                                 |
| genshi_text              | 31.8 ms                                                | 22.4 ms: 1.42x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.40x faster                                                |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 734 ms: 1.39x faster                                                  |
| thrift                   | 1.07 ms                                                | 780 us: 1.37x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 104 ms: 1.37x faster                                                  |
| 2to3                     | 348 ms                                                 | 257 ms: 1.36x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.77 ms: 1.36x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                                |
| scimark_fft              | 466 ms                                                 | 350 ms: 1.33x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 59.5 ms: 1.33x faster                                                 |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.32x faster                                                  |
| nqueens                  | 106 ms                                                 | 80.3 ms: 1.32x faster                                                 |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 64.2 ms: 1.31x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 52.6 ms: 1.31x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 50.3 ms: 1.31x faster                                                 |
| fannkuch                 | 532 ms                                                 | 410 ms: 1.30x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 20.0 ms: 1.29x faster                                                 |
| sympy_str                | 346 ms                                                 | 271 ms: 1.28x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.64 sec: 1.25x faster                                                |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                 |
| sympy_expand             | 566 ms                                                 | 460 ms: 1.23x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 137 ms: 1.23x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 96.6 ms: 1.20x faster                                                 |
| json_loads               | 31.2 us                                                | 26.5 us: 1.18x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 85.1 ms: 1.17x faster                                                 |
| json                     | 5.69 ms                                                | 4.95 ms: 1.15x faster                                                 |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 869 us: 1.14x faster                                                  |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.08x faster                                                 |
| async_generators         | 444 ms                                                 | 416 ms: 1.07x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 26.1 ms: 1.06x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.68 sec: 1.06x faster                                                |
| regex_effbot             | 3.63 ms                                                | 3.47 ms: 1.05x faster                                                 |
| regex_dna                | 227 ms                                                 | 221 ms: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                  |
| pidigits                 | 191 ms                                                 | 190 ms: 1.00x faster                                                  |
| coverage                 | 79.4 ms                                                | 83.6 ms: 1.05x slower                                                 |
| mypy2                    | 894 ms                                                 | 953 ms: 1.07x slower                                                  |
| telco                    | 7.27 ms                                                | 7.83 ms: 1.08x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 4.78 ms: 1.32x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.45 ms: 1.51x slower                                                 |
| bench_mp_pool            | 24.0 ms                                                | 82.1 ms: 3.42x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                          |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250105-3.14.0a3+-82b905d/bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.427x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.27x