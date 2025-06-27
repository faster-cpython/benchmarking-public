# Results vs. 3.10.4

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-x86_64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.455x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                  |
| docutils       | 3.30 sec                                               | 2.57 sec: 1.28x faster                                                |
| html5lib       | 88.9 ms                                                | 61.4 ms: 1.45x faster                                                 |
| Geometric mean | (ref)                                                  | 1.37x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 600 ms: 2.95x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 313 ms: 2.77x faster                                                  |
| async_tree_none         | 728 ms                                                 | 263 ms: 2.77x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 495 ms: 2.05x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 71.5 ms: 1.64x faster                                                 |
| nbody          | 154 ms                                                 | 103 ms: 1.50x faster                                                  |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.49x faster                                                  |
| regex_v8       | 27.8 ms                                                | 22.1 ms: 1.26x faster                                                 |
| regex_dna      | 227 ms                                                 | 182 ms: 1.25x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.07 ms: 1.18x faster                                                 |
| Geometric mean | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.04 sec: 1.54x faster                                                |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 318 us: 1.52x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 60.0 ms: 1.32x faster                                                 |
| json_dumps           | 14.2 ms                                                | 11.3 ms: 1.25x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 98.5 ms: 1.17x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 85.1 ms: 1.17x faster                                                 |
| json_loads           | 31.2 us                                                | 28.0 us: 1.11x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.1 ms: 1.20x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 6.90 ms: 1.16x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.3 ms: 1.49x faster                                                 |
| django_template | 48.2 ms                                                | 32.6 ms: 1.48x faster                                                 |
| mako            | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 48.9 ms: 1.35x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 600 ms: 2.95x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 313 ms: 2.77x faster                                                  |
| async_tree_none          | 728 ms                                                 | 263 ms: 2.77x faster                                                  |
| generators               | 80.1 ms                                                | 29.9 ms: 2.68x faster                                                 |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.32x faster                                                |
| deltablue                | 7.91 ms                                                | 3.47 ms: 2.28x faster                                                 |
| go                       | 240 ms                                                 | 111 ms: 2.17x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 495 ms: 2.05x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.3 us: 2.00x faster                                                 |
| pylint                   | 551 ms                                                 | 278 ms: 1.98x faster                                                  |
| richards_super           | 94.7 ms                                                | 48.9 ms: 1.94x faster                                                 |
| chaos                    | 115 ms                                                 | 60.4 ms: 1.91x faster                                                 |
| deepcopy                 | 479 us                                                 | 254 us: 1.89x faster                                                  |
| raytrace                 | 507 ms                                                 | 270 ms: 1.88x faster                                                  |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.87x faster                                                  |
| richards                 | 79.3 ms                                                | 43.0 ms: 1.84x faster                                                 |
| djangocms                | 38.4 us                                                | 21.7 us: 1.77x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.76x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 68.1 ms: 1.73x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.07 ms: 1.71x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 75.7 ms: 1.69x faster                                                 |
| float                    | 117 ms                                                 | 71.5 ms: 1.64x faster                                                 |
| pyflate                  | 716 ms                                                 | 443 ms: 1.62x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.63 us: 1.59x faster                                                 |
| spectral_norm            | 170 ms                                                 | 109 ms: 1.56x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.04 sec: 1.54x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 318 us: 1.52x faster                                                  |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                  |
| nbody                    | 154 ms                                                 | 103 ms: 1.50x faster                                                  |
| regex_compile            | 188 ms                                                 | 126 ms: 1.49x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.3 ms: 1.49x faster                                                 |
| django_template          | 48.2 ms                                                | 32.6 ms: 1.48x faster                                                 |
| html5lib                 | 88.9 ms                                                | 61.4 ms: 1.45x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 58.9 ms: 1.43x faster                                                 |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.41x faster                                                |
| coroutines               | 35.1 ms                                                | 25.1 ms: 1.40x faster                                                 |
| thrift                   | 1.07 ms                                                | 779 us: 1.38x faster                                                  |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.0 ms: 1.36x faster                                                 |
| logging_simple           | 8.30 us                                                | 6.11 us: 1.36x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 48.9 ms: 1.35x faster                                                 |
| logging_format           | 9.09 us                                                | 6.78 us: 1.34x faster                                                 |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 60.0 ms: 1.32x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.60 sec: 1.31x faster                                                |
| sympy_str                | 346 ms                                                 | 266 ms: 1.30x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 785 ms: 1.30x faster                                                  |
| nqueens                  | 106 ms                                                 | 81.7 ms: 1.29x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.01 ms: 1.29x faster                                                 |
| fannkuch                 | 532 ms                                                 | 413 ms: 1.29x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.57 sec: 1.28x faster                                                |
| regex_v8                 | 27.8 ms                                                | 22.1 ms: 1.26x faster                                                 |
| json_dumps               | 14.2 ms                                                | 11.3 ms: 1.25x faster                                                 |
| sympy_expand             | 566 ms                                                 | 453 ms: 1.25x faster                                                  |
| regex_dna                | 227 ms                                                 | 182 ms: 1.25x faster                                                  |
| scimark_fft              | 466 ms                                                 | 379 ms: 1.23x faster                                                  |
| python_startup           | 14.6 ms                                                | 12.1 ms: 1.20x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                  |
| pathlib                  | 20.5 ms                                                | 17.3 ms: 1.18x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.07 ms: 1.18x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 98.5 ms: 1.17x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 85.1 ms: 1.17x faster                                                 |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                  |
| json_loads               | 31.2 us                                                | 28.0 us: 1.11x faster                                                 |
| json                     | 5.69 ms                                                | 5.18 ms: 1.10x faster                                                 |
| async_generators         | 444 ms                                                 | 412 ms: 1.08x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.86 us: 1.06x faster                                                 |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                  |
| telco                    | 7.27 ms                                                | 7.89 ms: 1.09x slower                                                 |
| coverage                 | 79.4 ms                                                | 89.2 ms: 1.12x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 6.90 ms: 1.16x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 5.06 ms: 1.40x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.56 ms: 1.58x slower                                                 |
| logging_silent           | 190 ns                                                 | 475 ns: 2.50x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                          |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.455x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.31x