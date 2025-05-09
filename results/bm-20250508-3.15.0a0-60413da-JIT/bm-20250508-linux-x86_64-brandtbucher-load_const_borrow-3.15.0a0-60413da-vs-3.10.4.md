# Results vs. 3.10.4

- fork: brandtbucher
- ref: load_const_borrow
- machine: linux-x86_64
- commit hash: 60413da
- commit date: 2025-05-08
- overall geometric mean: 1.315x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 263 ms: 1.33x faster                                                     |
| docutils       | 3.30 sec                                               | 2.66 sec: 1.24x faster                                                   |
| html5lib       | 88.9 ms                                                | 61.9 ms: 1.43x faster                                                    |
| Geometric mean | (ref)                                                  | 1.33x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 600 ms: 2.95x faster                                                     |
| async_tree_memoization  | 870 ms                                                 | 312 ms: 2.79x faster                                                     |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 487 ms: 2.09x faster                                                     |
| Geometric mean          | (ref)                                                  | 2.63x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 64.2 ms: 1.82x faster                                                    |
| nbody          | 154 ms                                                 | 89.5 ms: 1.72x faster                                                    |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.47x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                     |
| regex_v8       | 27.8 ms                                                | 22.7 ms: 1.22x faster                                                    |
| regex_effbot   | 3.63 ms                                                | 3.01 ms: 1.20x faster                                                    |
| regex_dna      | 227 ms                                                 | 197 ms: 1.15x faster                                                     |
| Geometric mean | (ref)                                                  | 1.26x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.87 sec: 1.68x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 205 us: 1.61x faster                                                     |
| pickle_pure_python   | 484 us                                                 | 329 us: 1.47x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 56.0 ms: 1.41x faster                                                    |
| xml_etree_generate   | 99.4 ms                                                | 80.4 ms: 1.24x faster                                                    |
| json_dumps           | 14.2 ms                                                | 11.9 ms: 1.20x faster                                                    |
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.18x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 98.5 ms: 1.17x faster                                                    |
| json_loads           | 31.2 us                                                | 29.7 us: 1.05x faster                                                    |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.3 ms: 1.19x faster                                                    |
| python_startup_no_site | 5.93 ms                                                | 6.96 ms: 1.17x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.6 ms: 1.48x faster                                                    |
| mako            | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                    |
| genshi_text     | 31.8 ms                                                | 21.7 ms: 1.47x faster                                                    |
| genshi_xml      | 66.0 ms                                                | 49.1 ms: 1.34x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.20x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 600 ms: 2.95x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 312 ms: 2.79x faster                                                     |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                                     |
| deltablue                | 7.91 ms                                                | 3.08 ms: 2.57x faster                                                    |
| generators               | 80.1 ms                                                | 31.3 ms: 2.56x faster                                                    |
| richards_super           | 94.7 ms                                                | 38.6 ms: 2.45x faster                                                    |
| richards                 | 79.3 ms                                                | 34.2 ms: 2.32x faster                                                    |
| mdp                      | 2.85 sec                                               | 1.25 sec: 2.28x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 487 ms: 2.09x faster                                                     |
| pylint                   | 551 ms                                                 | 284 ms: 1.94x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 30.4 us: 1.92x faster                                                    |
| go                       | 240 ms                                                 | 126 ms: 1.91x faster                                                     |
| chaos                    | 115 ms                                                 | 61.1 ms: 1.89x faster                                                    |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                     |
| raytrace                 | 507 ms                                                 | 276 ms: 1.83x faster                                                     |
| float                    | 117 ms                                                 | 64.2 ms: 1.82x faster                                                    |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.81x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 67.3 ms: 1.76x faster                                                    |
| nbody                    | 154 ms                                                 | 89.5 ms: 1.72x faster                                                    |
| spectral_norm            | 170 ms                                                 | 99.3 ms: 1.71x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 75.5 ms: 1.69x faster                                                    |
| tomli_loads              | 3.14 sec                                               | 1.87 sec: 1.68x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 205 us: 1.61x faster                                                     |
| comprehensions           | 28.8 us                                                | 17.9 us: 1.61x faster                                                    |
| pyflate                  | 716 ms                                                 | 447 ms: 1.60x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.72 ms: 1.55x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 2.73 us: 1.53x faster                                                    |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.50x faster                                                     |
| django_template          | 48.2 ms                                                | 32.6 ms: 1.48x faster                                                    |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                    |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 329 us: 1.47x faster                                                     |
| genshi_text              | 31.8 ms                                                | 21.7 ms: 1.47x faster                                                    |
| scimark_fft              | 466 ms                                                 | 320 ms: 1.45x faster                                                     |
| html5lib                 | 88.9 ms                                                | 61.9 ms: 1.43x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 56.0 ms: 1.41x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 728 ms: 1.40x faster                                                     |
| coroutines               | 35.1 ms                                                | 25.1 ms: 1.40x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.38x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 61.6 ms: 1.37x faster                                                    |
| genshi_xml               | 66.0 ms                                                | 49.1 ms: 1.34x faster                                                    |
| logging_simple           | 8.30 us                                                | 6.20 us: 1.34x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 19.4 ms: 1.33x faster                                                    |
| 2to3                     | 348 ms                                                 | 263 ms: 1.33x faster                                                     |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.92 ms: 1.32x faster                                                    |
| logging_format           | 9.09 us                                                | 6.93 us: 1.31x faster                                                    |
| fannkuch                 | 532 ms                                                 | 413 ms: 1.29x faster                                                     |
| sympy_str                | 346 ms                                                 | 273 ms: 1.27x faster                                                     |
| nqueens                  | 106 ms                                                 | 85.1 ms: 1.24x faster                                                    |
| docutils                 | 3.30 sec                                               | 2.66 sec: 1.24x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 80.4 ms: 1.24x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 22.7 ms: 1.22x faster                                                    |
| regex_effbot             | 3.63 ms                                                | 3.01 ms: 1.20x faster                                                    |
| json_dumps               | 14.2 ms                                                | 11.9 ms: 1.20x faster                                                    |
| sympy_expand             | 566 ms                                                 | 474 ms: 1.19x faster                                                     |
| python_startup           | 14.6 ms                                                | 12.3 ms: 1.19x faster                                                    |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.18x faster                                                     |
| pathlib                  | 20.5 ms                                                | 17.4 ms: 1.17x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 98.5 ms: 1.17x faster                                                    |
| regex_dna                | 227 ms                                                 | 197 ms: 1.15x faster                                                     |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 907 us: 1.09x faster                                                     |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                                    |
| json                     | 5.69 ms                                                | 5.28 ms: 1.08x faster                                                    |
| json_loads               | 31.2 us                                                | 29.7 us: 1.05x faster                                                    |
| async_generators         | 444 ms                                                 | 426 ms: 1.04x faster                                                     |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                     |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                     |
| telco                    | 7.27 ms                                                | 7.77 ms: 1.07x slower                                                    |
| python_startup_no_site   | 5.93 ms                                                | 6.96 ms: 1.17x slower                                                    |
| gc_traversal             | 3.62 ms                                                | 4.94 ms: 1.36x slower                                                    |
| create_gc_cycles         | 1.62 ms                                                | 2.56 ms: 1.58x slower                                                    |
| dask                     | 441 ms                                                 | 928 ms: 2.11x slower                                                     |
| logging_silent           | 190 ns                                                 | 476 ns: 2.51x slower                                                     |
| bench_mp_pool            | 24.0 ms                                                | 93.7 ms: 3.90x slower                                                    |
| coverage                 | 79.4 ms                                                | 430 ms: 5.42x slower                                                     |
| thrift                   | 1.07 ms                                                | 148 ms: 138.40x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.27x faster                                                             |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250508-3.15.0a0-60413da-JIT/bm-20250508-linux-x86_64-brandtbucher-load_const_borrow-3.15.0a0-60413da.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.315x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.32x