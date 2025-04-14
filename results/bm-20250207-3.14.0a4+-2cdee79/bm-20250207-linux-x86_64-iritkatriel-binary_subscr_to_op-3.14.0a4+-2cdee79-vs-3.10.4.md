# Results vs. 3.10.4

- fork: iritkatriel
- ref: binary_subscr_to_op
- machine: linux-x86_64
- commit hash: 2cdee79
- commit date: 2025-02-07
- overall geometric mean: 1.457x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 252 ms: 1.38x faster                                                       |
| docutils       | 3.30 sec                                               | 2.57 sec: 1.28x faster                                                     |
| html5lib       | 88.9 ms                                                | 61.2 ms: 1.45x faster                                                      |
| Geometric mean | (ref)                                                  | 1.37x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 621 ms: 2.85x faster                                                       |
| async_tree_none         | 728 ms                                                 | 263 ms: 2.77x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 324 ms: 2.68x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 501 ms: 2.03x faster                                                       |
| Geometric mean          | (ref)                                                  | 2.56x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.0 ms: 1.67x faster                                                      |
| nbody          | 154 ms                                                 | 91.9 ms: 1.67x faster                                                      |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.42x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.49x faster                                                       |
| regex_v8       | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.25 ms: 1.12x faster                                                      |
| regex_dna      | 227 ms                                                 | 215 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                  | 1.19x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.97 sec: 1.60x faster                                                     |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                                       |
| pickle_pure_python   | 484 us                                                 | 320 us: 1.51x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 58.1 ms: 1.36x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                       |
| json_dumps           | 14.2 ms                                                | 11.8 ms: 1.20x faster                                                      |
| xml_etree_generate   | 99.4 ms                                                | 83.2 ms: 1.20x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 97.1 ms: 1.19x faster                                                      |
| json_loads           | 31.2 us                                                | 28.7 us: 1.09x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                      |
| python_startup_no_site | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                      |
| django_template | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                      |
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 48.0 ms: 1.38x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 156 us: 3.48x faster                                                       |
| generators               | 80.1 ms                                                | 27.6 ms: 2.90x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 621 ms: 2.85x faster                                                       |
| async_tree_none          | 728 ms                                                 | 263 ms: 2.77x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 324 ms: 2.68x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.17 ms: 2.50x faster                                                      |
| go                       | 240 ms                                                 | 118 ms: 2.03x faster                                                       |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 501 ms: 2.03x faster                                                       |
| pylint                   | 551 ms                                                 | 272 ms: 2.03x faster                                                       |
| chaos                    | 115 ms                                                 | 58.6 ms: 1.97x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 30.7 us: 1.90x faster                                                      |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                                       |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                       |
| richards_super           | 94.7 ms                                                | 51.2 ms: 1.85x faster                                                      |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.81x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 70.8 ms: 1.80x faster                                                      |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                                       |
| comprehensions           | 28.8 us                                                | 16.2 us: 1.78x faster                                                      |
| richards                 | 79.3 ms                                                | 44.6 ms: 1.78x faster                                                      |
| spectral_norm            | 170 ms                                                 | 96.0 ms: 1.77x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 67.9 ms: 1.74x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.25 ms: 1.74x faster                                                      |
| float                    | 117 ms                                                 | 70.0 ms: 1.67x faster                                                      |
| nbody                    | 154 ms                                                 | 91.9 ms: 1.67x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.26 ms: 1.66x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.55 ms: 1.66x faster                                                      |
| pyflate                  | 716 ms                                                 | 446 ms: 1.61x faster                                                       |
| tomli_loads              | 3.14 sec                                               | 1.97 sec: 1.60x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                                      |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                                       |
| pickle_pure_python       | 484 us                                                 | 320 us: 1.51x faster                                                       |
| genshi_text              | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.50 us: 1.51x faster                                                      |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                       |
| logging_format           | 9.09 us                                                | 6.07 us: 1.50x faster                                                      |
| django_template          | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                      |
| regex_compile            | 188 ms                                                 | 127 ms: 1.49x faster                                                       |
| html5lib                 | 88.9 ms                                                | 61.2 ms: 1.45x faster                                                      |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.2 ms: 1.44x faster                                                      |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 722 ms: 1.41x faster                                                       |
| thrift                   | 1.07 ms                                                | 762 us: 1.41x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.40x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 103 ms: 1.39x faster                                                       |
| 2to3                     | 348 ms                                                 | 252 ms: 1.38x faster                                                       |
| scimark_fft              | 466 ms                                                 | 337 ms: 1.38x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 48.0 ms: 1.38x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 58.1 ms: 1.36x faster                                                      |
| sqlalchemy_declarative   | 172 ms                                                 | 128 ms: 1.35x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.81 ms: 1.35x faster                                                      |
| sympy_sum                | 196 ms                                                 | 146 ms: 1.34x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 51.8 ms: 1.34x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 63.8 ms: 1.32x faster                                                      |
| nqueens                  | 106 ms                                                 | 80.1 ms: 1.32x faster                                                      |
| fannkuch                 | 532 ms                                                 | 405 ms: 1.31x faster                                                       |
| sympy_integrate          | 25.8 ms                                                | 19.7 ms: 1.31x faster                                                      |
| pathlib                  | 20.5 ms                                                | 15.6 ms: 1.31x faster                                                      |
| sympy_str                | 346 ms                                                 | 266 ms: 1.30x faster                                                       |
| docutils                 | 3.30 sec                                               | 2.57 sec: 1.28x faster                                                     |
| sympy_expand             | 566 ms                                                 | 451 ms: 1.26x faster                                                       |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                       |
| json_dumps               | 14.2 ms                                                | 11.8 ms: 1.20x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 83.2 ms: 1.20x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 97.1 ms: 1.19x faster                                                      |
| async_generators         | 444 ms                                                 | 384 ms: 1.16x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.47 sec: 1.15x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 860 us: 1.15x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                      |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                       |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                      |
| regex_effbot             | 3.63 ms                                                | 3.25 ms: 1.12x faster                                                      |
| json                     | 5.69 ms                                                | 5.12 ms: 1.11x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.75 us: 1.10x faster                                                      |
| json_loads               | 31.2 us                                                | 28.7 us: 1.09x faster                                                      |
| regex_dna                | 227 ms                                                 | 215 ms: 1.05x faster                                                       |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                       |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                       |
| telco                    | 7.27 ms                                                | 7.81 ms: 1.07x slower                                                      |
| coverage                 | 79.4 ms                                                | 92.4 ms: 1.16x slower                                                      |
| python_startup_no_site   | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 4.80 ms: 1.32x slower                                                      |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                      |
| bench_mp_pool            | 24.0 ms                                                | 80.5 ms: 3.35x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                               |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250207-3.14.0a4+-2cdee79/bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.457x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.26x