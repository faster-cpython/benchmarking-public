# Results vs. 3.10.4

- fork: python
- ref: 9aa1f60e2dedd8a67c42
- machine: linux-x86_64
- commit hash: 9aa1f60
- commit date: 2024-09-16
- overall geometric mean: 1.401x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 257 ms: 1.36x faster                                                  |
| docutils       | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                |
| html5lib       | 88.9 ms                                                | 64.1 ms: 1.39x faster                                                 |
| tornado_http   | 136 ms                                                 | 90.5 ms: 1.51x faster                                                 |
| Geometric mean | (ref)                                                  | 1.37x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.23x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 399 ms: 2.18x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 862 ms: 2.05x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 555 ms: 1.83x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.07x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 88.8 ms: 1.73x faster                                                 |
| float          | 117 ms                                                 | 77.0 ms: 1.52x faster                                                 |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                  |
| regex_v8       | 27.8 ms                                                | 22.9 ms: 1.21x faster                                                 |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 309 us: 1.57x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 2.05 sec: 1.53x faster                                                |
| json_dumps           | 14.2 ms                                                | 10.1 ms: 1.40x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 60.0 ms: 1.32x faster                                                 |
| json_loads           | 31.2 us                                                | 26.7 us: 1.17x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 87.2 ms: 1.14x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 107 ms: 1.08x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 158 ms: 1.06x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.8 ms: 1.51x faster                                                 |
| mako            | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                 |
| genshi_text     | 31.8 ms                                                | 22.1 ms: 1.44x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 49.2 ms: 1.34x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 158 us: 3.44x faster                                                  |
| generators               | 80.1 ms                                                | 27.8 ms: 2.89x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.28 ms: 2.41x faster                                                 |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.23x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 399 ms: 2.18x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 862 ms: 2.05x faster                                                  |
| go                       | 240 ms                                                 | 118 ms: 2.03x faster                                                  |
| chaos                    | 115 ms                                                 | 58.8 ms: 1.96x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 30.4 us: 1.92x faster                                                 |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                                  |
| logging_silent           | 190 ns                                                 | 102 ns: 1.87x faster                                                  |
| deepcopy                 | 479 us                                                 | 261 us: 1.84x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 555 ms: 1.83x faster                                                  |
| richards_super           | 94.7 ms                                                | 52.7 ms: 1.80x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 71.3 ms: 1.79x faster                                                 |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.77x faster                                                  |
| djangocms                | 38.4 us                                                | 21.9 us: 1.75x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 68.0 ms: 1.74x faster                                                 |
| nbody                    | 154 ms                                                 | 88.8 ms: 1.73x faster                                                 |
| pylint                   | 551 ms                                                 | 322 ms: 1.71x faster                                                  |
| richards                 | 79.3 ms                                                | 46.8 ms: 1.70x faster                                                 |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.33 ms: 1.64x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 309 us: 1.57x faster                                                  |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.05 sec: 1.53x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                                 |
| float                    | 117 ms                                                 | 77.0 ms: 1.52x faster                                                 |
| django_template          | 48.2 ms                                                | 31.8 ms: 1.51x faster                                                 |
| pyflate                  | 716 ms                                                 | 475 ms: 1.51x faster                                                  |
| tornado_http             | 136 ms                                                 | 90.5 ms: 1.51x faster                                                 |
| coroutines               | 35.1 ms                                                | 23.5 ms: 1.49x faster                                                 |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.48x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.64 us: 1.47x faster                                                 |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                 |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                  |
| genshi_text              | 31.8 ms                                                | 22.1 ms: 1.44x faster                                                 |
| logging_format           | 9.09 us                                                | 6.32 us: 1.44x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 719 ms: 1.42x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.1 ms: 1.40x faster                                                 |
| thrift                   | 1.07 ms                                                | 770 us: 1.39x faster                                                  |
| html5lib                 | 88.9 ms                                                | 64.1 ms: 1.39x faster                                                 |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.1 ms: 1.37x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.75 ms: 1.36x faster                                                 |
| 2to3                     | 348 ms                                                 | 257 ms: 1.36x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 49.2 ms: 1.34x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                                |
| sqlalchemy_declarative   | 172 ms                                                 | 129 ms: 1.34x faster                                                  |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 60.0 ms: 1.32x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 19.6 ms: 1.32x faster                                                 |
| nqueens                  | 106 ms                                                 | 81.0 ms: 1.31x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 64.6 ms: 1.30x faster                                                 |
| fannkuch                 | 532 ms                                                 | 409 ms: 1.30x faster                                                  |
| sympy_str                | 346 ms                                                 | 267 ms: 1.29x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                 |
| scimark_fft              | 466 ms                                                 | 366 ms: 1.27x faster                                                  |
| sympy_expand             | 566 ms                                                 | 452 ms: 1.25x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                |
| bench_thread_pool        | 986 us                                                 | 802 us: 1.23x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 22.9 ms: 1.21x faster                                                 |
| json                     | 5.69 ms                                                | 4.80 ms: 1.18x faster                                                 |
| json_loads               | 31.2 us                                                | 26.7 us: 1.17x faster                                                 |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 87.2 ms: 1.14x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.51 sec: 1.14x faster                                                |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.09x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 107 ms: 1.08x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.83 us: 1.07x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 158 ms: 1.06x faster                                                  |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                                  |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                  |
| async_generators         | 444 ms                                                 | 437 ms: 1.01x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                  |
| coverage                 | 79.4 ms                                                | 83.9 ms: 1.06x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                 |
| telco                    | 7.27 ms                                                | 8.67 ms: 1.19x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 4.49 ms: 1.24x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.64 ms: 1.63x slower                                                 |
| dask                     | 441 ms                                                 | 782 ms: 1.77x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                          |

Benchmark hidden because not significant (2): bench_mp_pool, regex_effbot
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20240916-3.14.0a0-9aa1f60/bm-20240916-linux-x86_64-python-9aa1f60e2dedd8a67c42-3.14.0a0-9aa1f60.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.401x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.25x