# Results vs. 3.10.4

- fork: iritkatriel
- ref: array_subscr
- machine: linux-x86_64
- commit hash: 454bfc5
- commit date: 2025-05-05
- overall geometric mean: 1.452x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 258 ms: 1.35x faster                                                |
| docutils       | 3.30 sec                                               | 2.67 sec: 1.23x faster                                              |
| html5lib       | 88.9 ms                                                | 60.6 ms: 1.47x faster                                               |
| Geometric mean | (ref)                                                  | 1.35x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 599 ms: 2.95x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 313 ms: 2.78x faster                                                |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.78x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 503 ms: 2.02x faster                                                |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.9 ms: 1.78x faster                                               |
| nbody          | 154 ms                                                 | 98.1 ms: 1.56x faster                                               |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.42x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                                |
| regex_v8       | 27.8 ms                                                | 23.9 ms: 1.16x faster                                               |
| regex_dna      | 227 ms                                                 | 208 ms: 1.09x faster                                                |
| regex_effbot   | 3.63 ms                                                | 3.35 ms: 1.08x faster                                               |
| Geometric mean | (ref)                                                  | 1.19x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.90 sec: 1.65x faster                                              |
| unpickle_pure_python | 331 us                                                 | 207 us: 1.59x faster                                                |
| pickle_pure_python   | 484 us                                                 | 323 us: 1.50x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 56.2 ms: 1.41x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 80.7 ms: 1.23x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                |
| json_dumps           | 14.2 ms                                                | 12.0 ms: 1.19x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 98.2 ms: 1.18x faster                                               |
| json_loads           | 31.2 us                                                | 30.2 us: 1.03x faster                                               |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 6.94 ms: 1.17x slower                                               |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.1 ms: 1.51x faster                                               |
| django_template | 48.2 ms                                                | 32.3 ms: 1.49x faster                                               |
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                               |
| genshi_xml      | 66.0 ms                                                | 49.1 ms: 1.35x faster                                               |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 171 us: 3.19x faster                                                |
| async_tree_io            | 1.77 sec                                               | 599 ms: 2.95x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 313 ms: 2.78x faster                                                |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.78x faster                                                |
| generators               | 80.1 ms                                                | 29.8 ms: 2.69x faster                                               |
| deltablue                | 7.91 ms                                                | 3.07 ms: 2.58x faster                                               |
| richards_super           | 94.7 ms                                                | 40.6 ms: 2.33x faster                                               |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.32x faster                                              |
| richards                 | 79.3 ms                                                | 35.2 ms: 2.25x faster                                               |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 503 ms: 2.02x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 29.1 us: 2.01x faster                                               |
| go                       | 240 ms                                                 | 123 ms: 1.96x faster                                                |
| pylint                   | 551 ms                                                 | 283 ms: 1.95x faster                                                |
| logging_silent           | 190 ns                                                 | 99.8 ns: 1.90x faster                                               |
| deepcopy                 | 479 us                                                 | 255 us: 1.88x faster                                                |
| chaos                    | 115 ms                                                 | 61.6 ms: 1.87x faster                                               |
| raytrace                 | 507 ms                                                 | 282 ms: 1.80x faster                                                |
| float                    | 117 ms                                                 | 65.9 ms: 1.78x faster                                               |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.75x faster                                                |
| tomli_loads              | 3.14 sec                                               | 1.90 sec: 1.65x faster                                              |
| crypto_pyaes             | 128 ms                                                 | 77.9 ms: 1.64x faster                                               |
| pyflate                  | 716 ms                                                 | 438 ms: 1.63x faster                                                |
| spectral_norm            | 170 ms                                                 | 106 ms: 1.61x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 207 us: 1.59x faster                                                |
| comprehensions           | 28.8 us                                                | 18.1 us: 1.59x faster                                               |
| nbody                    | 154 ms                                                 | 98.1 ms: 1.56x faster                                               |
| hexiom                   | 10.4 ms                                                | 6.70 ms: 1.55x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 76.3 ms: 1.55x faster                                               |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                               |
| genshi_text              | 31.8 ms                                                | 21.1 ms: 1.51x faster                                               |
| pickle_pure_python       | 484 us                                                 | 323 us: 1.50x faster                                                |
| django_template          | 48.2 ms                                                | 32.3 ms: 1.49x faster                                               |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                                |
| html5lib                 | 88.9 ms                                                | 60.6 ms: 1.47x faster                                               |
| logging_simple           | 8.30 us                                                | 5.72 us: 1.45x faster                                               |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                               |
| logging_format           | 9.09 us                                                | 6.36 us: 1.43x faster                                               |
| scimark_lu               | 176 ms                                                 | 124 ms: 1.42x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 56.2 ms: 1.41x faster                                               |
| dulwich_log              | 84.3 ms                                                | 60.6 ms: 1.39x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 735 ms: 1.38x faster                                                |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                              |
| pprint_pformat           | 2.10 sec                                               | 1.53 sec: 1.38x faster                                              |
| coroutines               | 35.1 ms                                                | 25.7 ms: 1.36x faster                                               |
| 2to3                     | 348 ms                                                 | 258 ms: 1.35x faster                                                |
| genshi_xml               | 66.0 ms                                                | 49.1 ms: 1.35x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 19.3 ms: 1.34x faster                                               |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                |
| fannkuch                 | 532 ms                                                 | 411 ms: 1.29x faster                                                |
| nqueens                  | 106 ms                                                 | 82.1 ms: 1.29x faster                                               |
| sympy_str                | 346 ms                                                 | 270 ms: 1.28x faster                                                |
| docutils                 | 3.30 sec                                               | 2.67 sec: 1.23x faster                                              |
| xml_etree_generate       | 99.4 ms                                                | 80.7 ms: 1.23x faster                                               |
| sympy_expand             | 566 ms                                                 | 469 ms: 1.21x faster                                                |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.20x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                |
| json_dumps               | 14.2 ms                                                | 12.0 ms: 1.19x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 98.2 ms: 1.18x faster                                               |
| regex_v8                 | 27.8 ms                                                | 23.9 ms: 1.16x faster                                               |
| scimark_fft              | 466 ms                                                 | 419 ms: 1.11x faster                                                |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                               |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.09x faster                                                |
| regex_dna                | 227 ms                                                 | 208 ms: 1.09x faster                                                |
| bench_thread_pool        | 986 us                                                 | 908 us: 1.09x faster                                                |
| regex_effbot             | 3.63 ms                                                | 3.35 ms: 1.08x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.08x faster                                               |
| json                     | 5.69 ms                                                | 5.39 ms: 1.06x faster                                               |
| json_loads               | 31.2 us                                                | 30.2 us: 1.03x faster                                               |
| async_generators         | 444 ms                                                 | 431 ms: 1.03x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 6.29 ms: 1.03x faster                                               |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                |
| telco                    | 7.27 ms                                                | 8.03 ms: 1.11x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 6.94 ms: 1.17x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.99 ms: 1.38x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.49 ms: 1.54x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 82.8 ms: 3.45x slower                                               |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                        |
Ignored benchmarks (24) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, coverage, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250505-3.14.0a7+-454bfc5-JIT/bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.452x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.31x