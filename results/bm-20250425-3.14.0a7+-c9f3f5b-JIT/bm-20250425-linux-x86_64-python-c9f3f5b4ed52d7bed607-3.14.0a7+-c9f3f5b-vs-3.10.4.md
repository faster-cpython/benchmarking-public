# Results vs. 3.10.4

- fork: python
- ref: c9f3f5b4ed52d7bed607
- machine: linux-x86_64
- commit hash: c9f3f5b
- commit date: 2025-04-25
- overall geometric mean: 1.458x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 259 ms: 1.35x faster                                                   |
| docutils       | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                 |
| html5lib       | 88.9 ms                                                | 59.8 ms: 1.49x faster                                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 594 ms: 2.98x faster                                                   |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.78x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 313 ms: 2.78x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 487 ms: 2.09x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.63x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 87.3 ms: 1.76x faster                                                  |
| float          | 117 ms                                                 | 71.2 ms: 1.64x faster                                                  |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.43x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.49x faster                                                   |
| regex_v8       | 27.8 ms                                                | 22.4 ms: 1.24x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.06 ms: 1.19x faster                                                  |
| regex_dna      | 227 ms                                                 | 201 ms: 1.13x faster                                                   |
| Geometric mean | (ref)                                                  | 1.25x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.81 sec: 1.73x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 209 us: 1.58x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 325 us: 1.49x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 56.8 ms: 1.39x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 80.4 ms: 1.24x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.19x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 98.3 ms: 1.17x faster                                                  |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 8.22 ms: 1.39x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                  |
| django_template | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                  |
| mako            | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 49.8 ms: 1.33x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 173 us: 3.15x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 594 ms: 2.98x faster                                                   |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.78x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 313 ms: 2.78x faster                                                   |
| generators               | 80.1 ms                                                | 30.2 ms: 2.65x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.07 ms: 2.58x faster                                                  |
| mdp                      | 2.85 sec                                               | 1.21 sec: 2.36x faster                                                 |
| richards_super           | 94.7 ms                                                | 42.0 ms: 2.25x faster                                                  |
| richards                 | 79.3 ms                                                | 36.6 ms: 2.17x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 487 ms: 2.09x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 29.0 us: 2.02x faster                                                  |
| chaos                    | 115 ms                                                 | 59.2 ms: 1.95x faster                                                  |
| pylint                   | 551 ms                                                 | 284 ms: 1.94x faster                                                   |
| logging_silent           | 190 ns                                                 | 98.4 ns: 1.93x faster                                                  |
| go                       | 240 ms                                                 | 128 ms: 1.88x faster                                                   |
| deepcopy                 | 479 us                                                 | 255 us: 1.88x faster                                                   |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                                   |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.81x faster                                                   |
| nbody                    | 154 ms                                                 | 87.3 ms: 1.76x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 67.4 ms: 1.75x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.81 sec: 1.73x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 74.8 ms: 1.71x faster                                                  |
| float                    | 117 ms                                                 | 71.2 ms: 1.64x faster                                                  |
| spectral_norm            | 170 ms                                                 | 105 ms: 1.62x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 209 us: 1.58x faster                                                   |
| pyflate                  | 716 ms                                                 | 457 ms: 1.57x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                  |
| comprehensions           | 28.8 us                                                | 18.5 us: 1.55x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.71 ms: 1.55x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                  |
| django_template          | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                  |
| scimark_fft              | 466 ms                                                 | 312 ms: 1.49x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 325 us: 1.49x faster                                                   |
| regex_compile            | 188 ms                                                 | 127 ms: 1.49x faster                                                   |
| html5lib                 | 88.9 ms                                                | 59.8 ms: 1.49x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.61 us: 1.48x faster                                                  |
| scimark_lu               | 176 ms                                                 | 120 ms: 1.47x faster                                                   |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                  |
| logging_format           | 9.09 us                                                | 6.20 us: 1.47x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.41x faster                                                 |
| coroutines               | 35.1 ms                                                | 25.0 ms: 1.40x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 725 ms: 1.40x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 56.8 ms: 1.39x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.67 ms: 1.39x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 61.1 ms: 1.38x faster                                                  |
| 2to3                     | 348 ms                                                 | 259 ms: 1.35x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                                 |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.5 ms: 1.33x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.4 ms: 1.33x faster                                                  |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 49.8 ms: 1.33x faster                                                  |
| nqueens                  | 106 ms                                                 | 81.5 ms: 1.30x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.29x faster                                                   |
| sympy_str                | 346 ms                                                 | 270 ms: 1.28x faster                                                   |
| fannkuch                 | 532 ms                                                 | 424 ms: 1.26x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 22.4 ms: 1.24x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 80.4 ms: 1.24x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.22x faster                                                  |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                  |
| sympy_expand             | 566 ms                                                 | 469 ms: 1.20x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.06 ms: 1.19x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.19x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 98.3 ms: 1.17x faster                                                  |
| regex_dna                | 227 ms                                                 | 201 ms: 1.13x faster                                                   |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 895 us: 1.10x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.76 us: 1.10x faster                                                  |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.09x faster                                                   |
| async_generators         | 444 ms                                                 | 415 ms: 1.07x faster                                                   |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                                  |
| json                     | 5.69 ms                                                | 5.52 ms: 1.03x faster                                                  |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                   |
| telco                    | 7.27 ms                                                | 7.78 ms: 1.07x slower                                                  |
| coverage                 | 79.4 ms                                                | 94.0 ms: 1.18x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.83 ms: 1.33x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 8.22 ms: 1.39x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 81.9 ms: 3.41x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                           |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250425-3.14.0a7+-c9f3f5b-JIT/bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.458x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.30x