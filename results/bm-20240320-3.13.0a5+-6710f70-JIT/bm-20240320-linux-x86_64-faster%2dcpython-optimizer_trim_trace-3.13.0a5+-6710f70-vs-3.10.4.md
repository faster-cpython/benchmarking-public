# Results vs. 3.10.4

- fork: faster-cpython
- ref: optimizer_trim_trace
- machine: linux-x86_64
- commit hash: 6710f70
- commit date: 2024-03-20
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 282 ms: 1.23x faster                                                             |
| chameleon      | 9.68 ms                                                | 7.06 ms: 1.37x faster                                                            |
| docutils       | 3.30 sec                                               | 2.80 sec: 1.18x faster                                                           |
| html5lib       | 88.9 ms                                                | 65.9 ms: 1.35x faster                                                            |
| tornado_http   | 136 ms                                                 | 98.8 ms: 1.38x faster                                                            |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 449 ms: 1.62x faster                                                             |
| async_tree_memoization  | 870 ms                                                 | 578 ms: 1.50x faster                                                             |
| async_tree_io           | 1.77 sec                                               | 1.22 sec: 1.45x faster                                                           |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 727 ms: 1.40x faster                                                             |
| Geometric mean          | (ref)                                                  | 1.49x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 94.6 ms: 1.62x faster                                                            |
| float          | 117 ms                                                 | 80.2 ms: 1.46x faster                                                            |
| pidigits       | 191 ms                                                 | 190 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 145 ms: 1.30x faster                                                             |
| regex_v8       | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                            |
| regex_dna      | 227 ms                                                 | 230 ms: 1.02x slower                                                             |
| regex_effbot   | 3.63 ms                                                | 3.81 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 304 us: 1.59x faster                                                             |
| tomli_loads          | 3.14 sec                                               | 2.06 sec: 1.52x faster                                                           |
| unpickle_pure_python | 331 us                                                 | 239 us: 1.38x faster                                                             |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 60.1 ms: 1.32x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 87.2 ms: 1.14x faster                                                            |
| json_loads           | 31.2 us                                                | 28.4 us: 1.10x faster                                                            |
| xml_etree_iterparse  | 115 ms                                                 | 109 ms: 1.06x faster                                                             |
| xml_etree_parse      | 168 ms                                                 | 160 ms: 1.05x faster                                                             |
| pickle_list          | 5.08 us                                                | 4.95 us: 1.03x faster                                                            |
| pickle               | 10.7 us                                                | 11.5 us: 1.08x slower                                                            |
| unpickle             | 14.4 us                                                | 15.5 us: 1.08x slower                                                            |
| pickle_dict          | 29.6 us                                                | 34.4 us: 1.16x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                                     |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.6 ms: 1.16x faster                                                            |
| python_startup_no_site | 5.93 ms                                                | 11.1 ms: 1.88x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                            |
| django_template | 48.2 ms                                                | 35.2 ms: 1.37x faster                                                            |
| genshi_text     | 31.8 ms                                                | 24.6 ms: 1.29x faster                                                            |
| genshi_xml      | 66.0 ms                                                | 55.1 ms: 1.20x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 112 us: 4.85x faster                                                             |
| generators               | 80.1 ms                                                | 29.6 ms: 2.71x faster                                                            |
| deltablue                | 7.91 ms                                                | 3.43 ms: 2.31x faster                                                            |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                                             |
| richards_super           | 94.7 ms                                                | 52.1 ms: 1.82x faster                                                            |
| chaos                    | 115 ms                                                 | 64.0 ms: 1.80x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 515 ms: 1.79x faster                                                             |
| raytrace                 | 507 ms                                                 | 293 ms: 1.73x faster                                                             |
| richards                 | 79.3 ms                                                | 46.0 ms: 1.72x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 75.1 ms: 1.70x faster                                                            |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.70x faster                                                             |
| pylint                   | 551 ms                                                 | 326 ms: 1.69x faster                                                             |
| scimark_monte_carlo      | 118 ms                                                 | 70.9 ms: 1.67x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.65x faster                                                            |
| async_tree_none          | 728 ms                                                 | 449 ms: 1.62x faster                                                             |
| nbody                    | 154 ms                                                 | 94.6 ms: 1.62x faster                                                            |
| comprehensions           | 28.8 us                                                | 17.8 us: 1.62x faster                                                            |
| pickle_pure_python       | 484 us                                                 | 304 us: 1.59x faster                                                             |
| go                       | 240 ms                                                 | 154 ms: 1.56x faster                                                             |
| sqlglot_transpile        | 2.57 ms                                                | 1.66 ms: 1.55x faster                                                            |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.52x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 2.06 sec: 1.52x faster                                                           |
| deepcopy_memo            | 58.5 us                                                | 38.6 us: 1.51x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 578 ms: 1.50x faster                                                             |
| hexiom                   | 10.4 ms                                                | 6.99 ms: 1.49x faster                                                            |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                            |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.47x faster                                                             |
| pyflate                  | 716 ms                                                 | 488 ms: 1.47x faster                                                             |
| float                    | 117 ms                                                 | 80.2 ms: 1.46x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 1.22 sec: 1.45x faster                                                           |
| logging_simple           | 8.30 us                                                | 5.86 us: 1.42x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 727 ms: 1.40x faster                                                             |
| logging_format           | 9.09 us                                                | 6.51 us: 1.40x faster                                                            |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                                           |
| unpickle_pure_python     | 331 us                                                 | 239 us: 1.38x faster                                                             |
| tornado_http             | 136 ms                                                 | 98.8 ms: 1.38x faster                                                            |
| chameleon                | 9.68 ms                                                | 7.06 ms: 1.37x faster                                                            |
| deepcopy                 | 479 us                                                 | 349 us: 1.37x faster                                                             |
| django_template          | 48.2 ms                                                | 35.2 ms: 1.37x faster                                                            |
| scimark_lu               | 176 ms                                                 | 129 ms: 1.36x faster                                                             |
| scimark_fft              | 466 ms                                                 | 345 ms: 1.35x faster                                                             |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                            |
| pprint_pformat           | 2.10 sec                                               | 1.56 sec: 1.35x faster                                                           |
| html5lib                 | 88.9 ms                                                | 65.9 ms: 1.35x faster                                                            |
| fannkuch                 | 532 ms                                                 | 398 ms: 1.34x faster                                                             |
| pprint_safe_repr         | 1.02 sec                                               | 762 ms: 1.34x faster                                                             |
| deepcopy_reduce          | 4.17 us                                                | 3.13 us: 1.33x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 60.1 ms: 1.32x faster                                                            |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.30x faster                                                             |
| thrift                   | 1.07 ms                                                | 827 us: 1.30x faster                                                             |
| regex_compile            | 188 ms                                                 | 145 ms: 1.30x faster                                                             |
| genshi_text              | 31.8 ms                                                | 24.6 ms: 1.29x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.07 ms: 1.28x faster                                                            |
| pycparser                | 1.58 sec                                               | 1.24 sec: 1.27x faster                                                           |
| 2to3                     | 348 ms                                                 | 282 ms: 1.23x faster                                                             |
| sqlglot_optimize         | 69.2 ms                                                | 56.9 ms: 1.22x faster                                                            |
| dulwich_log              | 84.3 ms                                                | 70.1 ms: 1.20x faster                                                            |
| sympy_sum                | 196 ms                                                 | 163 ms: 1.20x faster                                                             |
| sympy_str                | 346 ms                                                 | 288 ms: 1.20x faster                                                             |
| genshi_xml               | 66.0 ms                                                | 55.1 ms: 1.20x faster                                                            |
| aiohttp                  | 1.44 ms                                                | 1.20 ms: 1.20x faster                                                            |
| djangocms                | 38.4 us                                                | 32.4 us: 1.19x faster                                                            |
| nqueens                  | 106 ms                                                 | 89.3 ms: 1.19x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 21.8 ms: 1.18x faster                                                            |
| dask                     | 441 ms                                                 | 373 ms: 1.18x faster                                                             |
| docutils                 | 3.30 sec                                               | 2.80 sec: 1.18x faster                                                           |
| gunicorn                 | 1.53 ms                                                | 1.30 ms: 1.18x faster                                                            |
| sympy_expand             | 566 ms                                                 | 485 ms: 1.17x faster                                                             |
| python_startup           | 14.6 ms                                                | 12.6 ms: 1.16x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 853 us: 1.16x faster                                                             |
| xml_etree_generate       | 99.4 ms                                                | 87.2 ms: 1.14x faster                                                            |
| json_loads               | 31.2 us                                                | 28.4 us: 1.10x faster                                                            |
| pathlib                  | 20.5 ms                                                | 18.6 ms: 1.10x faster                                                            |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.09x faster                                                             |
| regex_v8                 | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                            |
| json                     | 5.69 ms                                                | 5.25 ms: 1.08x faster                                                            |
| create_gc_cycles         | 1.62 ms                                                | 1.51 ms: 1.07x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 109 ms: 1.06x faster                                                             |
| mdp                      | 2.85 sec                                               | 2.68 sec: 1.06x faster                                                           |
| sqlite_synth             | 3.02 us                                                | 2.87 us: 1.06x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 160 ms: 1.05x faster                                                             |
| pickle_list              | 5.08 us                                                | 4.95 us: 1.03x faster                                                            |
| pidigits                 | 191 ms                                                 | 190 ms: 1.01x faster                                                             |
| asyncio_websockets       | 559 ms                                                 | 564 ms: 1.01x slower                                                             |
| regex_dna                | 227 ms                                                 | 230 ms: 1.02x slower                                                             |
| regex_effbot             | 3.63 ms                                                | 3.81 ms: 1.05x slower                                                            |
| async_generators         | 444 ms                                                 | 469 ms: 1.06x slower                                                             |
| pickle                   | 10.7 us                                                | 11.5 us: 1.08x slower                                                            |
| unpickle                 | 14.4 us                                                | 15.5 us: 1.08x slower                                                            |
| bench_mp_pool            | 24.0 ms                                                | 26.4 ms: 1.10x slower                                                            |
| gc_traversal             | 3.62 ms                                                | 4.08 ms: 1.12x slower                                                            |
| telco                    | 7.27 ms                                                | 8.41 ms: 1.16x slower                                                            |
| pickle_dict              | 29.6 us                                                | 34.4 us: 1.16x slower                                                            |
| coverage                 | 79.4 ms                                                | 98.0 ms: 1.23x slower                                                            |
| unpack_sequence          | 60.0 ns                                                | 92.9 ns: 1.55x slower                                                            |
| python_startup_no_site   | 5.93 ms                                                | 11.1 ms: 1.88x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                                     |

Benchmark hidden because not significant (2): unpickle_list, mypy2
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240320-3.13.0a5+-6710f70-JIT/bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x


# Memory

- memory change: 1.34x