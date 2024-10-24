# Results vs. 3.10.4

- fork: brandtbucher
- ref: exit_operand
- machine: linux-x86_64
- commit hash: d4c66d7
- commit date: 2024-07-24
- overall geometric mean: 1.41x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 274 ms: 1.27x faster                                                |
| docutils       | 3.30 sec                                               | 2.91 sec: 1.13x faster                                              |
| html5lib       | 88.9 ms                                                | 63.9 ms: 1.39x faster                                               |
| tornado_http   | 136 ms                                                 | 94.1 ms: 1.45x faster                                               |
| Geometric mean | (ref)                                                  | 1.31x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.23x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 420 ms: 2.07x faster                                                |
| async_tree_io           | 1.77 sec                                               | 891 ms: 1.99x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 565 ms: 1.80x faster                                                |
| Geometric mean          | (ref)                                                  | 2.02x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.4 ms: 1.91x faster                                               |
| float          | 117 ms                                                 | 70.8 ms: 1.65x faster                                               |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.48x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 139 ms: 1.35x faster                                                |
| regex_v8       | 27.8 ms                                                | 25.3 ms: 1.10x faster                                               |
| regex_dna      | 227 ms                                                 | 229 ms: 1.01x slower                                                |
| regex_effbot   | 3.63 ms                                                | 3.94 ms: 1.09x slower                                               |
| Geometric mean | (ref)                                                  | 1.08x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 298 us: 1.63x faster                                                |
| tomli_loads          | 3.14 sec                                               | 1.97 sec: 1.59x faster                                              |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.51x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 57.9 ms: 1.37x faster                                               |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.37x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 80.7 ms: 1.23x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 100 ms: 1.15x faster                                                |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                |
| json_loads           | 31.2 us                                                | 28.2 us: 1.11x faster                                               |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.37x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 7.19 ms: 1.21x slower                                               |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.79 ms: 1.67x faster                                               |
| django_template | 48.2 ms                                                | 35.9 ms: 1.34x faster                                               |
| genshi_text     | 31.8 ms                                                | 25.0 ms: 1.27x faster                                               |
| genshi_xml      | 66.0 ms                                                | 57.8 ms: 1.14x faster                                               |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.24x faster                                                |
| generators               | 80.1 ms                                                | 29.4 ms: 2.72x faster                                               |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.23x faster                                                |
| deltablue                | 7.91 ms                                                | 3.64 ms: 2.17x faster                                               |
| async_tree_memoization   | 870 ms                                                 | 420 ms: 2.07x faster                                                |
| richards_super           | 94.7 ms                                                | 47.1 ms: 2.01x faster                                               |
| deepcopy_memo            | 58.5 us                                                | 29.4 us: 1.99x faster                                               |
| async_tree_io            | 1.77 sec                                               | 891 ms: 1.99x faster                                                |
| chaos                    | 115 ms                                                 | 58.3 ms: 1.98x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 60.9 ms: 1.94x faster                                               |
| richards                 | 79.3 ms                                                | 41.0 ms: 1.93x faster                                               |
| nbody                    | 154 ms                                                 | 80.4 ms: 1.91x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 68.0 ms: 1.88x faster                                               |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                                |
| asyncio_tcp              | 922 ms                                                 | 505 ms: 1.82x faster                                                |
| logging_silent           | 190 ns                                                 | 105 ns: 1.81x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 565 ms: 1.80x faster                                                |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                               |
| deepcopy                 | 479 us                                                 | 277 us: 1.73x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.70x faster                                               |
| scimark_sor              | 220 ms                                                 | 130 ms: 1.69x faster                                                |
| mako                     | 16.3 ms                                                | 9.79 ms: 1.67x faster                                               |
| float                    | 117 ms                                                 | 70.8 ms: 1.65x faster                                               |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.64x faster                                                |
| pyflate                  | 716 ms                                                 | 437 ms: 1.64x faster                                                |
| pickle_pure_python       | 484 us                                                 | 298 us: 1.63x faster                                                |
| go                       | 240 ms                                                 | 148 ms: 1.62x faster                                                |
| sqlglot_transpile        | 2.57 ms                                                | 1.61 ms: 1.59x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.97 sec: 1.59x faster                                              |
| hexiom                   | 10.4 ms                                                | 6.62 ms: 1.57x faster                                               |
| pylint                   | 551 ms                                                 | 353 ms: 1.56x faster                                                |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                               |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.51x faster                                                |
| logging_simple           | 8.30 us                                                | 5.54 us: 1.50x faster                                               |
| logging_format           | 9.09 us                                                | 6.10 us: 1.49x faster                                               |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.36 ms: 1.48x faster                                               |
| deepcopy_reduce          | 4.17 us                                                | 2.85 us: 1.46x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                              |
| tornado_http             | 136 ms                                                 | 94.1 ms: 1.45x faster                                               |
| fannkuch                 | 532 ms                                                 | 368 ms: 1.44x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 715 ms: 1.42x faster                                                |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                              |
| html5lib                 | 88.9 ms                                                | 63.9 ms: 1.39x faster                                               |
| scimark_lu               | 176 ms                                                 | 127 ms: 1.39x faster                                                |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.37x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 57.9 ms: 1.37x faster                                               |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.37x faster                                               |
| regex_compile            | 188 ms                                                 | 139 ms: 1.35x faster                                                |
| thrift                   | 1.07 ms                                                | 797 us: 1.35x faster                                                |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.34x faster                                              |
| django_template          | 48.2 ms                                                | 35.9 ms: 1.34x faster                                               |
| 2to3                     | 348 ms                                                 | 274 ms: 1.27x faster                                                |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                               |
| genshi_text              | 31.8 ms                                                | 25.0 ms: 1.27x faster                                               |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.27x faster                                                |
| sqlglot_optimize         | 69.2 ms                                                | 56.1 ms: 1.23x faster                                               |
| xml_etree_generate       | 99.4 ms                                                | 80.7 ms: 1.23x faster                                               |
| dulwich_log              | 84.3 ms                                                | 69.8 ms: 1.21x faster                                               |
| dask                     | 441 ms                                                 | 366 ms: 1.21x faster                                                |
| nqueens                  | 106 ms                                                 | 88.7 ms: 1.19x faster                                               |
| bench_thread_pool        | 986 us                                                 | 834 us: 1.18x faster                                                |
| sympy_str                | 346 ms                                                 | 299 ms: 1.16x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 22.3 ms: 1.16x faster                                               |
| sympy_sum                | 196 ms                                                 | 170 ms: 1.16x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 100 ms: 1.15x faster                                                |
| genshi_xml               | 66.0 ms                                                | 57.8 ms: 1.14x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                |
| docutils                 | 3.30 sec                                               | 2.91 sec: 1.13x faster                                              |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                |
| sympy_expand             | 566 ms                                                 | 506 ms: 1.12x faster                                                |
| mdp                      | 2.85 sec                                               | 2.55 sec: 1.12x faster                                              |
| json_loads               | 31.2 us                                                | 28.2 us: 1.11x faster                                               |
| regex_v8                 | 27.8 ms                                                | 25.3 ms: 1.10x faster                                               |
| json                     | 5.69 ms                                                | 5.18 ms: 1.10x faster                                               |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                |
| regex_dna                | 227 ms                                                 | 229 ms: 1.01x slower                                                |
| gc_traversal             | 3.62 ms                                                | 3.72 ms: 1.03x slower                                               |
| async_generators         | 444 ms                                                 | 465 ms: 1.05x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                               |
| regex_effbot             | 3.63 ms                                                | 3.94 ms: 1.09x slower                                               |
| telco                    | 7.27 ms                                                | 7.91 ms: 1.09x slower                                               |
| coverage                 | 79.4 ms                                                | 90.9 ms: 1.14x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 7.19 ms: 1.21x slower                                               |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                        |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240724-3.14.0a0-d4c66d7-JIT/bm-20240724-linux-x86_64-brandtbucher-exit_operand-3.14.0a0-d4c66d7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.19x