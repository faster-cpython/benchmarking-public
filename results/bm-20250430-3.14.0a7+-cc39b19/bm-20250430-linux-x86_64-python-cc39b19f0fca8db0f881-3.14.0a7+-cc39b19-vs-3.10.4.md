# Results vs. 3.10.4

- fork: python
- ref: cc39b19f0fca8db0f881
- machine: linux-x86_64
- commit hash: cc39b19
- commit date: 2025-04-30
- overall geometric mean: 1.437x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                   |
| docutils       | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                 |
| html5lib       | 88.9 ms                                                | 61.3 ms: 1.45x faster                                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 596 ms: 2.97x faster                                                   |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 314 ms: 2.77x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 493 ms: 2.06x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 71.5 ms: 1.64x faster                                                  |
| nbody          | 154 ms                                                 | 102 ms: 1.51x faster                                                   |
| pidigits       | 191 ms                                                 | 195 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                  | 1.34x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.48x faster                                                   |
| regex_v8       | 27.8 ms                                                | 22.5 ms: 1.23x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.20 ms: 1.13x faster                                                  |
| regex_dna      | 227 ms                                                 | 210 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                  | 1.22x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.03 sec: 1.55x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 318 us: 1.52x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.8 ms: 1.20x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 143 ms: 1.18x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 85.7 ms: 1.16x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 99.6 ms: 1.16x faster                                                  |
| json_loads           | 31.2 us                                                | 30.7 us: 1.02x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.28x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 6.95 ms: 1.17x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                  |
| django_template | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                  |
| mako            | 16.3 ms                                                | 11.6 ms: 1.40x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 49.3 ms: 1.34x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.22x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 596 ms: 2.97x faster                                                   |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 314 ms: 2.77x faster                                                   |
| generators               | 80.1 ms                                                | 29.2 ms: 2.75x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.31 ms: 2.39x faster                                                  |
| mdp                      | 2.85 sec                                               | 1.24 sec: 2.29x faster                                                 |
| go                       | 240 ms                                                 | 113 ms: 2.13x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 493 ms: 2.06x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 29.0 us: 2.02x faster                                                  |
| pylint                   | 551 ms                                                 | 280 ms: 1.97x faster                                                   |
| logging_silent           | 190 ns                                                 | 96.5 ns: 1.97x faster                                                  |
| chaos                    | 115 ms                                                 | 60.0 ms: 1.93x faster                                                  |
| richards_super           | 94.7 ms                                                | 49.4 ms: 1.92x faster                                                  |
| raytrace                 | 507 ms                                                 | 267 ms: 1.90x faster                                                   |
| deepcopy                 | 479 us                                                 | 255 us: 1.88x faster                                                   |
| richards                 | 79.3 ms                                                | 42.8 ms: 1.85x faster                                                  |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.78x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 68.3 ms: 1.73x faster                                                  |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.68x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 76.1 ms: 1.68x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.29 ms: 1.65x faster                                                  |
| float                    | 117 ms                                                 | 71.5 ms: 1.64x faster                                                  |
| spectral_norm            | 170 ms                                                 | 108 ms: 1.57x faster                                                   |
| pyflate                  | 716 ms                                                 | 455 ms: 1.57x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 2.03 sec: 1.55x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.54x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 318 us: 1.52x faster                                                   |
| genshi_text              | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                  |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                   |
| nbody                    | 154 ms                                                 | 102 ms: 1.51x faster                                                   |
| django_template          | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.62 us: 1.48x faster                                                  |
| regex_compile            | 188 ms                                                 | 128 ms: 1.48x faster                                                   |
| html5lib                 | 88.9 ms                                                | 61.3 ms: 1.45x faster                                                  |
| logging_format           | 9.09 us                                                | 6.32 us: 1.44x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                 |
| mako                     | 16.3 ms                                                | 11.6 ms: 1.40x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 60.4 ms: 1.40x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 733 ms: 1.39x faster                                                   |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                   |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.3 ms: 1.35x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.1 ms: 1.35x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                 |
| coroutines               | 35.1 ms                                                | 26.1 ms: 1.34x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 49.3 ms: 1.34x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                  |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.30x faster                                                   |
| nqueens                  | 106 ms                                                 | 81.9 ms: 1.29x faster                                                  |
| sympy_str                | 346 ms                                                 | 269 ms: 1.29x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                 |
| fannkuch                 | 532 ms                                                 | 425 ms: 1.25x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 22.5 ms: 1.23x faster                                                  |
| sympy_expand             | 566 ms                                                 | 461 ms: 1.23x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.27 ms: 1.23x faster                                                  |
| scimark_fft              | 466 ms                                                 | 380 ms: 1.23x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.9 ms: 1.21x faster                                                  |
| json_dumps               | 14.2 ms                                                | 11.8 ms: 1.20x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 143 ms: 1.18x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 85.7 ms: 1.16x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 99.6 ms: 1.16x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.20 ms: 1.13x faster                                                  |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                   |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 893 us: 1.10x faster                                                   |
| async_generators         | 444 ms                                                 | 410 ms: 1.08x faster                                                   |
| regex_dna                | 227 ms                                                 | 210 ms: 1.08x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.85 us: 1.06x faster                                                  |
| json                     | 5.69 ms                                                | 5.56 ms: 1.02x faster                                                  |
| json_loads               | 31.2 us                                                | 30.7 us: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                   |
| pidigits                 | 191 ms                                                 | 195 ms: 1.02x slower                                                   |
| telco                    | 7.27 ms                                                | 8.01 ms: 1.10x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 6.95 ms: 1.17x slower                                                  |
| coverage                 | 79.4 ms                                                | 93.2 ms: 1.17x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.99 ms: 1.38x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.49 ms: 1.54x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 83.0 ms: 3.46x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                           |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250430-3.14.0a7+-cc39b19/bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.437x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.28x