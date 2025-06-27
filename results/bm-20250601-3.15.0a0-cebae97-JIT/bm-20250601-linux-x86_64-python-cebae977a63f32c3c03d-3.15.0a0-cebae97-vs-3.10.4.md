# Results vs. 3.10.4

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-x86_64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 2.127x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                                  |
| docutils       | 3.30 sec                                               | 2.64 sec: 1.25x faster                                                |
| html5lib       | 88.9 ms                                                | 61.7 ms: 1.44x faster                                                 |
| Geometric mean | (ref)                                                  | 1.34x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 601 ms: 2.94x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 311 ms: 2.80x faster                                                  |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 490 ms: 2.07x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.63x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 63.7 ms: 1.84x faster                                                 |
| nbody          | 154 ms                                                 | 93.1 ms: 1.65x faster                                                 |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.46x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 27.8 ms                                                | 23.1 ms: 1.20x faster                                                 |
| regex_dna      | 227 ms                                                 | 197 ms: 1.15x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.29 ms: 1.10x faster                                                 |
| Geometric mean | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 199 us: 1.66x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 1.89 sec: 1.66x faster                                                |
| pickle_pure_python   | 484 us                                                 | 323 us: 1.50x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 56.3 ms: 1.41x faster                                                 |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 80.5 ms: 1.23x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 97.1 ms: 1.19x faster                                                 |
| json_loads           | 31.2 us                                                | 28.3 us: 1.10x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 6.94 ms: 1.17x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.7 ms: 1.52x faster                                                 |
| genshi_text     | 31.8 ms                                                | 21.3 ms: 1.50x faster                                                 |
| django_template | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 50.0 ms: 1.32x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pprint_pformat           | 2.10 sec                                               | 1.45 us: 1448877.24x faster                                           |
| pprint_safe_repr         | 1.02 sec                                               | 837 ns: 1216651.76x faster                                            |
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.21x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 601 ms: 2.94x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 311 ms: 2.80x faster                                                  |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                                  |
| generators               | 80.1 ms                                                | 30.6 ms: 2.62x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.09 ms: 2.56x faster                                                 |
| richards_super           | 94.7 ms                                                | 39.2 ms: 2.41x faster                                                 |
| richards                 | 79.3 ms                                                | 33.5 ms: 2.37x faster                                                 |
| mdp                      | 2.85 sec                                               | 1.24 sec: 2.29x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 490 ms: 2.07x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.6 us: 1.98x faster                                                 |
| pylint                   | 551 ms                                                 | 282 ms: 1.95x faster                                                  |
| go                       | 240 ms                                                 | 123 ms: 1.95x faster                                                  |
| deepcopy                 | 479 us                                                 | 255 us: 1.88x faster                                                  |
| chaos                    | 115 ms                                                 | 62.1 ms: 1.86x faster                                                 |
| float                    | 117 ms                                                 | 63.7 ms: 1.84x faster                                                 |
| raytrace                 | 507 ms                                                 | 277 ms: 1.83x faster                                                  |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.81x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 67.2 ms: 1.76x faster                                                 |
| djangocms                | 38.4 us                                                | 22.1 us: 1.74x faster                                                 |
| pyflate                  | 716 ms                                                 | 412 ms: 1.74x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 75.6 ms: 1.69x faster                                                 |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                                 |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.69x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 199 us: 1.66x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.89 sec: 1.66x faster                                                |
| nbody                    | 154 ms                                                 | 93.1 ms: 1.65x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.45 ms: 1.61x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                 |
| mako                     | 16.3 ms                                                | 10.7 ms: 1.52x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 323 us: 1.50x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.3 ms: 1.50x faster                                                 |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                  |
| django_template          | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                 |
| html5lib                 | 88.9 ms                                                | 61.7 ms: 1.44x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 59.7 ms: 1.41x faster                                                 |
| scimark_fft              | 466 ms                                                 | 330 ms: 1.41x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 56.3 ms: 1.41x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                                |
| thrift                   | 1.07 ms                                                | 777 us: 1.38x faster                                                  |
| coroutines               | 35.1 ms                                                | 25.6 ms: 1.37x faster                                                 |
| logging_simple           | 8.30 us                                                | 6.11 us: 1.36x faster                                                 |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                                  |
| logging_format           | 9.09 us                                                | 6.78 us: 1.34x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 19.4 ms: 1.33x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.90 ms: 1.32x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 50.0 ms: 1.32x faster                                                 |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                  |
| fannkuch                 | 532 ms                                                 | 409 ms: 1.30x faster                                                  |
| sympy_str                | 346 ms                                                 | 270 ms: 1.28x faster                                                  |
| nqueens                  | 106 ms                                                 | 82.7 ms: 1.28x faster                                                 |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.64 sec: 1.25x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 80.5 ms: 1.23x faster                                                 |
| sympy_expand             | 566 ms                                                 | 463 ms: 1.22x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                  |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.20x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 23.1 ms: 1.20x faster                                                 |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 97.1 ms: 1.19x faster                                                 |
| regex_dna                | 227 ms                                                 | 197 ms: 1.15x faster                                                  |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.12x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.29 ms: 1.10x faster                                                 |
| json_loads               | 31.2 us                                                | 28.3 us: 1.10x faster                                                 |
| json                     | 5.69 ms                                                | 5.22 ms: 1.09x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.07x faster                                                 |
| async_generators         | 444 ms                                                 | 428 ms: 1.04x faster                                                  |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                  |
| telco                    | 7.27 ms                                                | 7.72 ms: 1.06x slower                                                 |
| coverage                 | 79.4 ms                                                | 87.0 ms: 1.10x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 6.94 ms: 1.17x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 5.08 ms: 1.40x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.59 ms: 1.60x slower                                                 |
| logging_silent           | 190 ns                                                 | 472 ns: 2.49x slower                                                  |
| Geometric mean           | (ref)                                                  | 2.07x faster                                                          |
Ignored benchmarks (24) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 2.127x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.38x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.32x