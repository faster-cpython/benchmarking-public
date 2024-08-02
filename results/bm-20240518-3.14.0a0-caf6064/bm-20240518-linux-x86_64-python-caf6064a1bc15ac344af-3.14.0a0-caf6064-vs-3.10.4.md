# Results vs. 3.10.4

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-x86_64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 268 ms: 1.30x faster                                                  |
| chameleon      | 9.68 ms                                                | 6.97 ms: 1.39x faster                                                 |
| docutils       | 3.30 sec                                               | 2.78 sec: 1.18x faster                                                |
| html5lib       | 88.9 ms                                                | 65.6 ms: 1.35x faster                                                 |
| tornado_http   | 136 ms                                                 | 94.1 ms: 1.45x faster                                                 |
| Geometric mean | (ref)                                                  | 1.33x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 362 ms: 2.01x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 947 ms: 1.87x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 471 ms: 1.85x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 617 ms: 1.65x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.84x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 87.2 ms: 1.76x faster                                                 |
| float          | 117 ms                                                 | 77.2 ms: 1.52x faster                                                 |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 134 ms: 1.40x faster                                                  |
| regex_v8       | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                 |
| regex_dna      | 227 ms                                                 | 219 ms: 1.04x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.55 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 305 us: 1.59x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 220 us: 1.50x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 2.11 sec: 1.49x faster                                                |
| json_dumps           | 14.2 ms                                                | 10.7 ms: 1.32x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 60.1 ms: 1.32x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 86.4 ms: 1.15x faster                                                 |
| json_loads           | 31.2 us                                                | 28.9 us: 1.08x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 107 ms: 1.08x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 158 ms: 1.06x faster                                                  |
| unpickle_list        | 5.20 us                                                | 5.47 us: 1.05x slower                                                 |
| pickle               | 10.7 us                                                | 11.7 us: 1.10x slower                                                 |
| pickle_list          | 5.08 us                                                | 5.61 us: 1.10x slower                                                 |
| pickle_dict          | 29.6 us                                                | 34.2 us: 1.16x slower                                                 |
| unpickle             | 14.4 us                                                | 16.9 us: 1.18x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.4 ms: 1.40x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.10 ms: 1.20x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                 |
| django_template | 48.2 ms                                                | 34.3 ms: 1.41x faster                                                 |
| genshi_text     | 31.8 ms                                                | 23.0 ms: 1.38x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 51.0 ms: 1.29x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                                  |
| generators               | 80.1 ms                                                | 29.7 ms: 2.69x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.29 ms: 2.40x faster                                                 |
| async_tree_none          | 728 ms                                                 | 362 ms: 2.01x faster                                                  |
| chaos                    | 115 ms                                                 | 59.8 ms: 1.93x faster                                                 |
| raytrace                 | 507 ms                                                 | 266 ms: 1.91x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 947 ms: 1.87x faster                                                  |
| logging_silent           | 190 ns                                                 | 102 ns: 1.86x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 471 ms: 1.85x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 506 ms: 1.82x faster                                                  |
| nbody                    | 154 ms                                                 | 87.2 ms: 1.76x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 73.4 ms: 1.74x faster                                                 |
| richards_super           | 94.7 ms                                                | 54.5 ms: 1.74x faster                                                 |
| pylint                   | 551 ms                                                 | 318 ms: 1.73x faster                                                  |
| scimark_sor              | 220 ms                                                 | 127 ms: 1.73x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 68.4 ms: 1.73x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.72x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                                 |
| go                       | 240 ms                                                 | 145 ms: 1.65x faster                                                  |
| richards                 | 79.3 ms                                                | 48.0 ms: 1.65x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.30 ms: 1.65x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 617 ms: 1.65x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.61 ms: 1.59x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 305 us: 1.59x faster                                                  |
| spectral_norm            | 170 ms                                                 | 111 ms: 1.52x faster                                                  |
| float                    | 117 ms                                                 | 77.2 ms: 1.52x faster                                                 |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                 |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 220 us: 1.50x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 39.1 us: 1.50x faster                                                 |
| pyflate                  | 716 ms                                                 | 480 ms: 1.49x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.11 sec: 1.49x faster                                                |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.72 us: 1.45x faster                                                 |
| tornado_http             | 136 ms                                                 | 94.1 ms: 1.45x faster                                                 |
| logging_format           | 9.09 us                                                | 6.29 us: 1.45x faster                                                 |
| django_template          | 48.2 ms                                                | 34.3 ms: 1.41x faster                                                 |
| python_startup           | 14.6 ms                                                | 10.4 ms: 1.40x faster                                                 |
| regex_compile            | 188 ms                                                 | 134 ms: 1.40x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.84 sec: 1.40x faster                                                |
| chameleon                | 9.68 ms                                                | 6.97 ms: 1.39x faster                                                 |
| genshi_text              | 31.8 ms                                                | 23.0 ms: 1.38x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.37x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 751 ms: 1.35x faster                                                  |
| html5lib                 | 88.9 ms                                                | 65.6 ms: 1.35x faster                                                 |
| nqueens                  | 106 ms                                                 | 79.6 ms: 1.33x faster                                                 |
| thrift                   | 1.07 ms                                                | 806 us: 1.33x faster                                                  |
| deepcopy                 | 479 us                                                 | 361 us: 1.33x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.7 ms: 1.32x faster                                                 |
| fannkuch                 | 532 ms                                                 | 402 ms: 1.32x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.32x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 60.1 ms: 1.32x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.32x faster                                                  |
| 2to3                     | 348 ms                                                 | 268 ms: 1.30x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 51.0 ms: 1.29x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 3.26 us: 1.28x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 20.3 ms: 1.27x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 66.4 ms: 1.27x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.11 ms: 1.27x faster                                                 |
| sympy_sum                | 196 ms                                                 | 155 ms: 1.27x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 54.7 ms: 1.27x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.25x faster                                                 |
| sympy_str                | 346 ms                                                 | 278 ms: 1.24x faster                                                  |
| scimark_fft              | 466 ms                                                 | 377 ms: 1.23x faster                                                  |
| sympy_expand             | 566 ms                                                 | 467 ms: 1.21x faster                                                  |
| dask                     | 441 ms                                                 | 369 ms: 1.19x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.78 sec: 1.18x faster                                                |
| bench_thread_pool        | 986 us                                                 | 832 us: 1.18x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 86.4 ms: 1.15x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.59 sec: 1.10x faster                                                |
| regex_v8                 | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                 |
| meteor_contest           | 120 ms                                                 | 111 ms: 1.08x faster                                                  |
| json_loads               | 31.2 us                                                | 28.9 us: 1.08x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 107 ms: 1.08x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 158 ms: 1.06x faster                                                  |
| json                     | 5.69 ms                                                | 5.39 ms: 1.06x faster                                                 |
| regex_dna                | 227 ms                                                 | 219 ms: 1.04x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.95 us: 1.03x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.55 ms: 1.02x faster                                                 |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                  |
| bench_mp_pool            | 24.0 ms                                                | 23.8 ms: 1.01x faster                                                 |
| async_generators         | 444 ms                                                 | 447 ms: 1.01x slower                                                  |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.01x slower                                                  |
| flaskblogging            | 8.58 ms                                                | 8.89 ms: 1.04x slower                                                 |
| unpickle_list            | 5.20 us                                                | 5.47 us: 1.05x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 3.90 ms: 1.08x slower                                                 |
| pickle                   | 10.7 us                                                | 11.7 us: 1.10x slower                                                 |
| pickle_list              | 5.08 us                                                | 5.61 us: 1.10x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.82 ms: 1.12x slower                                                 |
| pickle_dict              | 29.6 us                                                | 34.2 us: 1.16x slower                                                 |
| coverage                 | 79.4 ms                                                | 92.8 ms: 1.17x slower                                                 |
| unpickle                 | 14.4 us                                                | 16.9 us: 1.18x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.10 ms: 1.20x slower                                                 |
| telco                    | 7.27 ms                                                | 173 ms: 23.88x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                          |
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240518-3.14.0a0-caf6064/bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.11x