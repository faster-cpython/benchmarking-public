# Results vs. 3.10.4

- fork: iritkatriel
- ref: binary_subscr_to_op
- machine: linux-x86_64
- commit hash: dda3d1f
- commit date: 2025-02-06
- overall geometric mean: 1.461x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 251 ms: 1.39x faster                                                       |
| docutils       | 3.30 sec                                               | 2.57 sec: 1.28x faster                                                     |
| html5lib       | 88.9 ms                                                | 60.6 ms: 1.47x faster                                                      |
| Geometric mean | (ref)                                                  | 1.38x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 615 ms: 2.88x faster                                                       |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.78x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 322 ms: 2.70x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 488 ms: 2.08x faster                                                       |
| Geometric mean          | (ref)                                                  | 2.59x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 91.2 ms: 1.68x faster                                                      |
| float          | 117 ms                                                 | 70.3 ms: 1.66x faster                                                      |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.42x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.50x faster                                                       |
| regex_effbot   | 3.63 ms                                                | 3.32 ms: 1.09x faster                                                      |
| regex_v8       | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                      |
| regex_dna      | 227 ms                                                 | 209 ms: 1.09x faster                                                       |
| Geometric mean | (ref)                                                  | 1.18x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.97 sec: 1.60x faster                                                     |
| pickle_pure_python   | 484 us                                                 | 315 us: 1.54x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 58.4 ms: 1.35x faster                                                      |
| json_dumps           | 14.2 ms                                                | 11.8 ms: 1.21x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 83.7 ms: 1.19x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 98.6 ms: 1.17x faster                                                      |
| json_loads           | 31.2 us                                                | 29.3 us: 1.06x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.7 ms: 1.14x faster                                                      |
| python_startup_no_site | 5.93 ms                                                | 7.00 ms: 1.18x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.4 ms: 1.53x faster                                                      |
| genshi_text     | 31.8 ms                                                | 20.9 ms: 1.52x faster                                                      |
| mako            | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 47.7 ms: 1.38x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.48x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 156 us: 3.49x faster                                                       |
| generators               | 80.1 ms                                                | 27.6 ms: 2.90x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 615 ms: 2.88x faster                                                       |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.78x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 322 ms: 2.70x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.21 ms: 2.47x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 488 ms: 2.08x faster                                                       |
| pylint                   | 551 ms                                                 | 272 ms: 2.03x faster                                                       |
| go                       | 240 ms                                                 | 119 ms: 2.02x faster                                                       |
| chaos                    | 115 ms                                                 | 58.3 ms: 1.98x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 29.7 us: 1.97x faster                                                      |
| raytrace                 | 507 ms                                                 | 269 ms: 1.88x faster                                                       |
| richards_super           | 94.7 ms                                                | 50.7 ms: 1.87x faster                                                      |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                                       |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                       |
| logging_silent           | 190 ns                                                 | 104 ns: 1.83x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 69.9 ms: 1.83x faster                                                      |
| spectral_norm            | 170 ms                                                 | 94.5 ms: 1.80x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.2 us: 1.78x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 66.8 ms: 1.77x faster                                                      |
| richards                 | 79.3 ms                                                | 44.9 ms: 1.77x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.25 ms: 1.73x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.16 ms: 1.69x faster                                                      |
| nbody                    | 154 ms                                                 | 91.2 ms: 1.68x faster                                                      |
| float                    | 117 ms                                                 | 70.3 ms: 1.66x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.56 ms: 1.65x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 1.97 sec: 1.60x faster                                                     |
| pyflate                  | 716 ms                                                 | 449 ms: 1.60x faster                                                       |
| pickle_pure_python       | 484 us                                                 | 315 us: 1.54x faster                                                       |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.54x faster                                                       |
| django_template          | 48.2 ms                                                | 31.4 ms: 1.53x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.53x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                       |
| genshi_text              | 31.8 ms                                                | 20.9 ms: 1.52x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.47 us: 1.52x faster                                                      |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                                      |
| logging_format           | 9.09 us                                                | 6.07 us: 1.50x faster                                                      |
| regex_compile            | 188 ms                                                 | 126 ms: 1.50x faster                                                       |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                      |
| html5lib                 | 88.9 ms                                                | 60.6 ms: 1.47x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 709 ms: 1.44x faster                                                       |
| thrift                   | 1.07 ms                                                | 750 us: 1.43x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.53 ms: 1.43x faster                                                      |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.4 ms: 1.42x faster                                                      |
| 2to3                     | 348 ms                                                 | 251 ms: 1.39x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 103 ms: 1.39x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 47.7 ms: 1.38x faster                                                      |
| scimark_fft              | 466 ms                                                 | 341 ms: 1.37x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 58.4 ms: 1.35x faster                                                      |
| sqlalchemy_declarative   | 172 ms                                                 | 128 ms: 1.35x faster                                                       |
| fannkuch                 | 532 ms                                                 | 395 ms: 1.35x faster                                                       |
| sympy_sum                | 196 ms                                                 | 146 ms: 1.34x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 51.8 ms: 1.33x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.32x faster                                                      |
| nqueens                  | 106 ms                                                 | 80.1 ms: 1.32x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 63.9 ms: 1.32x faster                                                      |
| sympy_str                | 346 ms                                                 | 265 ms: 1.31x faster                                                       |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.28x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.57 sec: 1.28x faster                                                     |
| sympy_expand             | 566 ms                                                 | 448 ms: 1.26x faster                                                       |
| json_dumps               | 14.2 ms                                                | 11.8 ms: 1.21x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 83.7 ms: 1.19x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 98.6 ms: 1.17x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.48 sec: 1.15x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 861 us: 1.15x faster                                                       |
| python_startup           | 14.6 ms                                                | 12.7 ms: 1.14x faster                                                      |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                       |
| async_generators         | 444 ms                                                 | 390 ms: 1.14x faster                                                       |
| json                     | 5.69 ms                                                | 5.17 ms: 1.10x faster                                                      |
| regex_effbot             | 3.63 ms                                                | 3.32 ms: 1.09x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.78 us: 1.09x faster                                                      |
| regex_dna                | 227 ms                                                 | 209 ms: 1.09x faster                                                       |
| json_loads               | 31.2 us                                                | 29.3 us: 1.06x faster                                                      |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                       |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                       |
| telco                    | 7.27 ms                                                | 7.78 ms: 1.07x slower                                                      |
| coverage                 | 79.4 ms                                                | 92.7 ms: 1.17x slower                                                      |
| python_startup_no_site   | 5.93 ms                                                | 7.00 ms: 1.18x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 4.60 ms: 1.27x slower                                                      |
| create_gc_cycles         | 1.62 ms                                                | 2.44 ms: 1.51x slower                                                      |
| bench_mp_pool            | 24.0 ms                                                | 80.6 ms: 3.35x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                               |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250206-3.14.0a4+-dda3d1f/bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.461x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.26x