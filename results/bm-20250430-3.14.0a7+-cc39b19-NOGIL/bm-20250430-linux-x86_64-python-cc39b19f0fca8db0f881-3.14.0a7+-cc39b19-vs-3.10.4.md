# Results vs. 3.10.4

- fork: python
- ref: cc39b19f0fca8db0f881
- machine: linux-x86_64
- commit hash: cc39b19
- commit date: 2025-04-30
- overall geometric mean: 1.312x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 1.53x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 292 ms: 1.20x faster                                                   |
| docutils       | 3.30 sec                                               | 2.78 sec: 1.18x faster                                                 |
| html5lib       | 88.9 ms                                                | 67.6 ms: 1.31x faster                                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 548 ms: 3.23x faster                                                   |
| async_tree_none         | 728 ms                                                 | 266 ms: 2.74x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 330 ms: 2.63x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 500 ms: 2.03x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.9 ms: 1.65x faster                                                  |
| nbody          | 154 ms                                                 | 129 ms: 1.19x faster                                                   |
| pidigits       | 191 ms                                                 | 181 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 145 ms: 1.30x faster                                                   |
| regex_v8       | 27.8 ms                                                | 22.4 ms: 1.24x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.17 ms: 1.14x faster                                                  |
| regex_dna      | 227 ms                                                 | 212 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 345 us: 1.40x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 2.24 sec: 1.40x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 239 us: 1.38x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 97.6 ms: 1.18x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 68.1 ms: 1.16x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 150 ms: 1.12x faster                                                   |
| json_dumps           | 14.2 ms                                                | 13.1 ms: 1.08x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 96.3 ms: 1.03x faster                                                  |
| json_loads           | 31.2 us                                                | 32.6 us: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 15.5 ms: 1.06x slower                                                  |
| python_startup_no_site | 5.93 ms                                                | 9.12 ms: 1.54x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 39.3 ms: 1.22x faster                                                  |
| genshi_text     | 31.8 ms                                                | 27.3 ms: 1.17x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 59.5 ms: 1.11x faster                                                  |
| mako            | 16.3 ms                                                | 16.2 ms: 1.01x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io            | 1.77 sec                                               | 548 ms: 3.23x faster                                                   |
| async_tree_none          | 728 ms                                                 | 266 ms: 2.74x faster                                                   |
| typing_runtime_protocols | 544 us                                                 | 202 us: 2.70x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 330 ms: 2.63x faster                                                   |
| generators               | 80.1 ms                                                | 30.6 ms: 2.62x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.70 ms: 2.14x faster                                                  |
| mdp                      | 2.85 sec                                               | 1.39 sec: 2.05x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 500 ms: 2.03x faster                                                   |
| pylint                   | 551 ms                                                 | 293 ms: 1.88x faster                                                   |
| go                       | 240 ms                                                 | 133 ms: 1.80x faster                                                   |
| logging_silent           | 190 ns                                                 | 110 ns: 1.73x faster                                                   |
| chaos                    | 115 ms                                                 | 67.7 ms: 1.71x faster                                                  |
| float                    | 117 ms                                                 | 70.9 ms: 1.65x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 36.4 us: 1.61x faster                                                  |
| deepcopy                 | 479 us                                                 | 298 us: 1.61x faster                                                   |
| scimark_sor              | 220 ms                                                 | 137 ms: 1.60x faster                                                   |
| gc_traversal             | 3.62 ms                                                | 2.29 ms: 1.58x faster                                                  |
| richards_super           | 94.7 ms                                                | 60.0 ms: 1.58x faster                                                  |
| raytrace                 | 507 ms                                                 | 321 ms: 1.58x faster                                                   |
| richards                 | 79.3 ms                                                | 50.6 ms: 1.57x faster                                                  |
| comprehensions           | 28.8 us                                                | 19.7 us: 1.46x faster                                                  |
| spectral_norm            | 170 ms                                                 | 119 ms: 1.43x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 89.4 ms: 1.43x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 82.8 ms: 1.43x faster                                                  |
| hexiom                   | 10.4 ms                                                | 7.29 ms: 1.43x faster                                                  |
| pyflate                  | 716 ms                                                 | 503 ms: 1.42x faster                                                   |
| coroutines               | 35.1 ms                                                | 24.9 ms: 1.41x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 345 us: 1.40x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 2.24 sec: 1.40x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 239 us: 1.38x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 62.4 ms: 1.35x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 3.16 us: 1.32x faster                                                  |
| html5lib                 | 88.9 ms                                                | 67.6 ms: 1.31x faster                                                  |
| regex_compile            | 188 ms                                                 | 145 ms: 1.30x faster                                                   |
| scimark_lu               | 176 ms                                                 | 139 ms: 1.27x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 806 ms: 1.26x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.67 sec: 1.26x faster                                                 |
| logging_simple           | 8.30 us                                                | 6.58 us: 1.26x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 22.4 ms: 1.24x faster                                                  |
| logging_format           | 9.09 us                                                | 7.38 us: 1.23x faster                                                  |
| django_template          | 48.2 ms                                                | 39.3 ms: 1.22x faster                                                  |
| 2to3                     | 348 ms                                                 | 292 ms: 1.20x faster                                                   |
| nbody                    | 154 ms                                                 | 129 ms: 1.19x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.78 sec: 1.18x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 97.6 ms: 1.18x faster                                                  |
| pathlib                  | 20.5 ms                                                | 17.5 ms: 1.17x faster                                                  |
| genshi_text              | 31.8 ms                                                | 27.3 ms: 1.17x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 68.1 ms: 1.16x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 22.3 ms: 1.16x faster                                                  |
| nqueens                  | 106 ms                                                 | 91.7 ms: 1.15x faster                                                  |
| sympy_sum                | 196 ms                                                 | 171 ms: 1.15x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.17 ms: 1.14x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 20.4 ms: 1.14x faster                                                  |
| sympy_str                | 346 ms                                                 | 305 ms: 1.13x faster                                                   |
| scimark_fft              | 466 ms                                                 | 411 ms: 1.13x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 150 ms: 1.12x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 59.5 ms: 1.11x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.87 ms: 1.10x faster                                                  |
| sympy_expand             | 566 ms                                                 | 516 ms: 1.10x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 157 ms: 1.09x faster                                                   |
| json_dumps               | 14.2 ms                                                | 13.1 ms: 1.08x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                                  |
| regex_dna                | 227 ms                                                 | 212 ms: 1.07x faster                                                   |
| fannkuch                 | 532 ms                                                 | 503 ms: 1.06x faster                                                   |
| pidigits                 | 191 ms                                                 | 181 ms: 1.06x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 96.3 ms: 1.03x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                   |
| mako                     | 16.3 ms                                                | 16.2 ms: 1.01x faster                                                  |
| async_generators         | 444 ms                                                 | 442 ms: 1.00x faster                                                   |
| create_gc_cycles         | 1.62 ms                                                | 1.69 ms: 1.04x slower                                                  |
| json_loads               | 31.2 us                                                | 32.6 us: 1.04x slower                                                  |
| python_startup           | 14.6 ms                                                | 15.5 ms: 1.06x slower                                                  |
| meteor_contest           | 120 ms                                                 | 132 ms: 1.10x slower                                                   |
| telco                    | 7.27 ms                                                | 9.08 ms: 1.25x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 9.12 ms: 1.54x slower                                                  |
| coverage                 | 79.4 ms                                                | 123 ms: 1.55x slower                                                   |
| bench_thread_pool        | 986 us                                                 | 3.27 ms: 3.32x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 90.6 ms: 3.77x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.27x faster                                                           |

Benchmark hidden because not significant (1): json
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250430-3.14.0a7+-cc39b19-NOGIL/bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.312x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 1.53x