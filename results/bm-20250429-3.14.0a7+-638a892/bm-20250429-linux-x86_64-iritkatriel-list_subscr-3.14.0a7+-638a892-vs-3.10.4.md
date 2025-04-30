# Results vs. 3.10.4

- fork: iritkatriel
- ref: list_subscr
- machine: linux-x86_64
- commit hash: 638a892
- commit date: 2025-04-29
- overall geometric mean: 1.454x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                               |
| docutils       | 3.30 sec                                               | 2.61 sec: 1.26x faster                                             |
| html5lib       | 88.9 ms                                                | 62.2 ms: 1.43x faster                                              |
| Geometric mean | (ref)                                                  | 1.35x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 597 ms: 2.96x faster                                               |
| async_tree_none         | 728 ms                                                 | 263 ms: 2.77x faster                                               |
| async_tree_memoization  | 870 ms                                                 | 315 ms: 2.76x faster                                               |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 492 ms: 2.07x faster                                               |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 117 ms                                                 | 69.2 ms: 1.69x faster                                              |
| nbody          | 154 ms                                                 | 96.3 ms: 1.59x faster                                              |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.40x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.50x faster                                               |
| regex_v8       | 27.8 ms                                                | 22.1 ms: 1.26x faster                                              |
| regex_effbot   | 3.63 ms                                                | 3.14 ms: 1.16x faster                                              |
| regex_dna      | 227 ms                                                 | 209 ms: 1.08x faster                                               |
| Geometric mean | (ref)                                                  | 1.24x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.98 sec: 1.59x faster                                             |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                               |
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                               |
| xml_etree_process    | 79.1 ms                                                | 60.5 ms: 1.31x faster                                              |
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.21x faster                                              |
| xml_etree_parse      | 168 ms                                                 | 143 ms: 1.18x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 100 ms: 1.15x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 87.6 ms: 1.13x faster                                              |
| json_loads           | 31.2 us                                                | 30.0 us: 1.04x faster                                              |
| Geometric mean       | (ref)                                                  | 1.28x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.0 ms: 1.12x faster                                              |
| python_startup_no_site | 5.93 ms                                                | 6.87 ms: 1.16x slower                                              |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.7 ms: 1.52x faster                                              |
| genshi_text     | 31.8 ms                                                | 21.1 ms: 1.51x faster                                              |
| mako            | 16.3 ms                                                | 11.7 ms: 1.40x faster                                              |
| genshi_xml      | 66.0 ms                                                | 49.2 ms: 1.34x faster                                              |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                               |
| async_tree_io            | 1.77 sec                                               | 597 ms: 2.96x faster                                               |
| async_tree_none          | 728 ms                                                 | 263 ms: 2.77x faster                                               |
| async_tree_memoization   | 870 ms                                                 | 315 ms: 2.76x faster                                               |
| generators               | 80.1 ms                                                | 29.6 ms: 2.70x faster                                              |
| deltablue                | 7.91 ms                                                | 3.38 ms: 2.34x faster                                              |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.32x faster                                             |
| go                       | 240 ms                                                 | 112 ms: 2.15x faster                                               |
| deepcopy_memo            | 58.5 us                                                | 28.3 us: 2.07x faster                                              |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 492 ms: 2.07x faster                                               |
| chaos                    | 115 ms                                                 | 56.9 ms: 2.03x faster                                              |
| pylint                   | 551 ms                                                 | 277 ms: 1.99x faster                                               |
| raytrace                 | 507 ms                                                 | 261 ms: 1.94x faster                                               |
| logging_silent           | 190 ns                                                 | 98.2 ns: 1.93x faster                                              |
| richards_super           | 94.7 ms                                                | 49.7 ms: 1.90x faster                                              |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                               |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                               |
| richards                 | 79.3 ms                                                | 43.4 ms: 1.83x faster                                              |
| scimark_monte_carlo      | 118 ms                                                 | 66.8 ms: 1.77x faster                                              |
| crypto_pyaes             | 128 ms                                                 | 73.6 ms: 1.74x faster                                              |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                              |
| float                    | 117 ms                                                 | 69.2 ms: 1.69x faster                                              |
| pyflate                  | 716 ms                                                 | 433 ms: 1.65x faster                                               |
| hexiom                   | 10.4 ms                                                | 6.30 ms: 1.65x faster                                              |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.63x faster                                               |
| nbody                    | 154 ms                                                 | 96.3 ms: 1.59x faster                                              |
| tomli_loads              | 3.14 sec                                               | 1.98 sec: 1.59x faster                                             |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.53x faster                                              |
| django_template          | 48.2 ms                                                | 31.7 ms: 1.52x faster                                              |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                               |
| genshi_text              | 31.8 ms                                                | 21.1 ms: 1.51x faster                                              |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                               |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                               |
| regex_compile            | 188 ms                                                 | 126 ms: 1.50x faster                                               |
| logging_simple           | 8.30 us                                                | 5.55 us: 1.50x faster                                              |
| logging_format           | 9.09 us                                                | 6.11 us: 1.49x faster                                              |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                             |
| html5lib                 | 88.9 ms                                                | 62.2 ms: 1.43x faster                                              |
| dulwich_log              | 84.3 ms                                                | 59.7 ms: 1.41x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 723 ms: 1.41x faster                                               |
| coroutines               | 35.1 ms                                                | 25.0 ms: 1.41x faster                                              |
| mako                     | 16.3 ms                                                | 11.7 ms: 1.40x faster                                              |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 19.0 ms: 1.36x faster                                              |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.3 ms: 1.35x faster                                              |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                             |
| genshi_xml               | 66.0 ms                                                | 49.2 ms: 1.34x faster                                              |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.32x faster                                               |
| nqueens                  | 106 ms                                                 | 80.4 ms: 1.32x faster                                              |
| scimark_fft              | 466 ms                                                 | 356 ms: 1.31x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 60.5 ms: 1.31x faster                                              |
| sqlalchemy_declarative   | 172 ms                                                 | 132 ms: 1.30x faster                                               |
| fannkuch                 | 532 ms                                                 | 408 ms: 1.30x faster                                               |
| sympy_str                | 346 ms                                                 | 266 ms: 1.30x faster                                               |
| docutils                 | 3.30 sec                                               | 2.61 sec: 1.26x faster                                             |
| regex_v8                 | 27.8 ms                                                | 22.1 ms: 1.26x faster                                              |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.16 ms: 1.25x faster                                              |
| sympy_expand             | 566 ms                                                 | 453 ms: 1.25x faster                                               |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.21x faster                                              |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.20x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 143 ms: 1.18x faster                                               |
| regex_effbot             | 3.63 ms                                                | 3.14 ms: 1.16x faster                                              |
| xml_etree_iterparse      | 115 ms                                                 | 100 ms: 1.15x faster                                               |
| xml_etree_generate       | 99.4 ms                                                | 87.6 ms: 1.13x faster                                              |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                               |
| python_startup           | 14.6 ms                                                | 13.0 ms: 1.12x faster                                              |
| bench_thread_pool        | 986 us                                                 | 885 us: 1.11x faster                                               |
| async_generators         | 444 ms                                                 | 401 ms: 1.11x faster                                               |
| regex_dna                | 227 ms                                                 | 209 ms: 1.08x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.88 us: 1.05x faster                                              |
| json_loads               | 31.2 us                                                | 30.0 us: 1.04x faster                                              |
| json                     | 5.69 ms                                                | 5.50 ms: 1.03x faster                                              |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                               |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                               |
| telco                    | 7.27 ms                                                | 7.80 ms: 1.07x slower                                              |
| python_startup_no_site   | 5.93 ms                                                | 6.87 ms: 1.16x slower                                              |
| coverage                 | 79.4 ms                                                | 92.8 ms: 1.17x slower                                              |
| gc_traversal             | 3.62 ms                                                | 4.85 ms: 1.34x slower                                              |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                              |
| bench_mp_pool            | 24.0 ms                                                | 82.0 ms: 3.41x slower                                              |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                       |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250429-3.14.0a7+-638a892/bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.454x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.28x