# Results vs. 3.10.4

- fork: iritkatriel
- ref: list_subscr
- machine: linux-x86_64
- commit hash: 3074926
- commit date: 2025-04-17
- overall geometric mean: 1.459x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250417-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-3074926 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 252 ms: 1.38x faster                                               |
| docutils       | 3.30 sec                                               | 2.62 sec: 1.26x faster                                             |
| html5lib       | 88.9 ms                                                | 62.5 ms: 1.42x faster                                              |
| Geometric mean | (ref)                                                  | 1.35x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250417-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-3074926 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 610 ms: 2.90x faster                                               |
| async_tree_none         | 728 ms                                                 | 257 ms: 2.84x faster                                               |
| async_tree_memoization  | 870 ms                                                 | 310 ms: 2.81x faster                                               |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 480 ms: 2.12x faster                                               |
| Geometric mean          | (ref)                                                  | 2.64x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250417-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-3074926 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 117 ms                                                 | 67.7 ms: 1.73x faster                                              |
| nbody          | 154 ms                                                 | 95.4 ms: 1.61x faster                                              |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.42x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250417-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-3074926 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.50x faster                                               |
| regex_v8       | 27.8 ms                                                | 23.0 ms: 1.21x faster                                              |
| regex_effbot   | 3.63 ms                                                | 3.25 ms: 1.12x faster                                              |
| regex_dna      | 227 ms                                                 | 211 ms: 1.07x faster                                               |
| Geometric mean | (ref)                                                  | 1.21x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250417-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-3074926 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.98 sec: 1.59x faster                                             |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                               |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.51x faster                                               |
| xml_etree_process    | 79.1 ms                                                | 58.6 ms: 1.35x faster                                              |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                              |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.20x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 84.2 ms: 1.18x faster                                              |
| xml_etree_iterparse  | 115 ms                                                 | 98.8 ms: 1.17x faster                                              |
| json_loads           | 31.2 us                                                | 30.2 us: 1.03x faster                                              |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250417-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-3074926 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.3 ms: 1.10x faster                                              |
| python_startup_no_site | 5.93 ms                                                | 8.26 ms: 1.39x slower                                              |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250417-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-3074926 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 20.8 ms: 1.53x faster                                              |
| django_template | 48.2 ms                                                | 31.4 ms: 1.53x faster                                              |
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                              |
| genshi_xml      | 66.0 ms                                                | 49.1 ms: 1.34x faster                                              |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250417-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-3074926 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.28x faster                                               |
| async_tree_io            | 1.77 sec                                               | 610 ms: 2.90x faster                                               |
| async_tree_none          | 728 ms                                                 | 257 ms: 2.84x faster                                               |
| async_tree_memoization   | 870 ms                                                 | 310 ms: 2.81x faster                                               |
| generators               | 80.1 ms                                                | 30.4 ms: 2.64x faster                                              |
| deltablue                | 7.91 ms                                                | 3.37 ms: 2.35x faster                                              |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.33x faster                                             |
| go                       | 240 ms                                                 | 111 ms: 2.16x faster                                               |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 480 ms: 2.12x faster                                               |
| chaos                    | 115 ms                                                 | 56.0 ms: 2.06x faster                                              |
| deepcopy_memo            | 58.5 us                                                | 28.5 us: 2.05x faster                                              |
| logging_silent           | 190 ns                                                 | 95.8 ns: 1.98x faster                                              |
| pylint                   | 551 ms                                                 | 279 ms: 1.98x faster                                               |
| raytrace                 | 507 ms                                                 | 263 ms: 1.92x faster                                               |
| richards_super           | 94.7 ms                                                | 49.3 ms: 1.92x faster                                              |
| deepcopy                 | 479 us                                                 | 250 us: 1.92x faster                                               |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                               |
| richards                 | 79.3 ms                                                | 43.6 ms: 1.82x faster                                              |
| scimark_monte_carlo      | 118 ms                                                 | 66.2 ms: 1.78x faster                                              |
| crypto_pyaes             | 128 ms                                                 | 72.4 ms: 1.76x faster                                              |
| float                    | 117 ms                                                 | 67.7 ms: 1.73x faster                                              |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                              |
| hexiom                   | 10.4 ms                                                | 6.19 ms: 1.68x faster                                              |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.64x faster                                               |
| nbody                    | 154 ms                                                 | 95.4 ms: 1.61x faster                                              |
| tomli_loads              | 3.14 sec                                               | 1.98 sec: 1.59x faster                                             |
| pyflate                  | 716 ms                                                 | 452 ms: 1.58x faster                                               |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                              |
| genshi_text              | 31.8 ms                                                | 20.8 ms: 1.53x faster                                              |
| django_template          | 48.2 ms                                                | 31.4 ms: 1.53x faster                                              |
| logging_simple           | 8.30 us                                                | 5.43 us: 1.53x faster                                              |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                               |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.51x faster                                               |
| logging_format           | 9.09 us                                                | 6.01 us: 1.51x faster                                              |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                               |
| regex_compile            | 188 ms                                                 | 125 ms: 1.50x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.44 sec: 1.46x faster                                             |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                              |
| coroutines               | 35.1 ms                                                | 24.4 ms: 1.44x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 710 ms: 1.43x faster                                               |
| html5lib                 | 88.9 ms                                                | 62.5 ms: 1.42x faster                                              |
| dulwich_log              | 84.3 ms                                                | 59.9 ms: 1.41x faster                                              |
| 2to3                     | 348 ms                                                 | 252 ms: 1.38x faster                                               |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.0 ms: 1.37x faster                                              |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.75 ms: 1.36x faster                                              |
| sympy_integrate          | 25.8 ms                                                | 19.0 ms: 1.36x faster                                              |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.35x faster                                             |
| xml_etree_process        | 79.1 ms                                                | 58.6 ms: 1.35x faster                                              |
| genshi_xml               | 66.0 ms                                                | 49.1 ms: 1.34x faster                                              |
| scimark_fft              | 466 ms                                                 | 352 ms: 1.32x faster                                               |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.31x faster                                               |
| nqueens                  | 106 ms                                                 | 80.7 ms: 1.31x faster                                              |
| fannkuch                 | 532 ms                                                 | 406 ms: 1.31x faster                                               |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.30x faster                                               |
| sympy_str                | 346 ms                                                 | 267 ms: 1.30x faster                                               |
| docutils                 | 3.30 sec                                               | 2.62 sec: 1.26x faster                                             |
| sympy_expand             | 566 ms                                                 | 452 ms: 1.25x faster                                               |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                              |
| regex_v8                 | 27.8 ms                                                | 23.0 ms: 1.21x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.20x faster                                               |
| pathlib                  | 20.5 ms                                                | 17.2 ms: 1.19x faster                                              |
| xml_etree_generate       | 99.4 ms                                                | 84.2 ms: 1.18x faster                                              |
| xml_etree_iterparse      | 115 ms                                                 | 98.8 ms: 1.17x faster                                              |
| regex_effbot             | 3.63 ms                                                | 3.25 ms: 1.12x faster                                              |
| async_generators         | 444 ms                                                 | 399 ms: 1.11x faster                                               |
| bench_thread_pool        | 986 us                                                 | 888 us: 1.11x faster                                               |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                               |
| python_startup           | 14.6 ms                                                | 13.3 ms: 1.10x faster                                              |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.09x faster                                              |
| regex_dna                | 227 ms                                                 | 211 ms: 1.07x faster                                               |
| json                     | 5.69 ms                                                | 5.41 ms: 1.05x faster                                              |
| json_loads               | 31.2 us                                                | 30.2 us: 1.03x faster                                              |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                               |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                               |
| telco                    | 7.27 ms                                                | 7.71 ms: 1.06x slower                                              |
| coverage                 | 79.4 ms                                                | 87.7 ms: 1.10x slower                                              |
| python_startup_no_site   | 5.93 ms                                                | 8.26 ms: 1.39x slower                                              |
| gc_traversal             | 3.62 ms                                                | 5.05 ms: 1.39x slower                                              |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                              |
| bench_mp_pool            | 24.0 ms                                                | 82.2 ms: 3.42x slower                                              |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                       |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250417-3.14.0a7+-3074926/bm-20250417-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-3074926.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.459x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.27x