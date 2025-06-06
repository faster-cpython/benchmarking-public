# Results vs. 3.10.4

- fork: iritkatriel
- ref: list_subscr
- machine: linux-x86_64
- commit hash: a054a83
- commit date: 2025-04-30
- overall geometric mean: 1.453x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-a054a83 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 256 ms: 1.36x faster                                               |
| docutils       | 3.30 sec                                               | 2.62 sec: 1.26x faster                                             |
| html5lib       | 88.9 ms                                                | 62.4 ms: 1.43x faster                                              |
| Geometric mean | (ref)                                                  | 1.35x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-a054a83 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 600 ms: 2.95x faster                                               |
| async_tree_none         | 728 ms                                                 | 263 ms: 2.77x faster                                               |
| async_tree_memoization  | 870 ms                                                 | 317 ms: 2.75x faster                                               |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 494 ms: 2.06x faster                                               |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-a054a83 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 117 ms                                                 | 67.6 ms: 1.73x faster                                              |
| nbody          | 154 ms                                                 | 96.6 ms: 1.59x faster                                              |
| pidigits       | 191 ms                                                 | 195 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                  | 1.39x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-a054a83 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.51x faster                                               |
| regex_v8       | 27.8 ms                                                | 23.9 ms: 1.16x faster                                              |
| regex_effbot   | 3.63 ms                                                | 3.26 ms: 1.11x faster                                              |
| regex_dna      | 227 ms                                                 | 208 ms: 1.09x faster                                               |
| Geometric mean | (ref)                                                  | 1.21x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-a054a83 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.98 sec: 1.59x faster                                             |
| pickle_pure_python   | 484 us                                                 | 314 us: 1.54x faster                                               |
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                               |
| xml_etree_process    | 79.1 ms                                                | 60.6 ms: 1.30x faster                                              |
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.21x faster                                              |
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.18x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 99.1 ms: 1.16x faster                                              |
| xml_etree_generate   | 99.4 ms                                                | 87.0 ms: 1.14x faster                                              |
| json_loads           | 31.2 us                                                | 29.7 us: 1.05x faster                                              |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-a054a83 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                              |
| python_startup_no_site | 5.93 ms                                                | 6.91 ms: 1.17x slower                                              |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-a054a83 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.2 ms: 1.49x faster                                              |
| genshi_text     | 31.8 ms                                                | 21.3 ms: 1.49x faster                                              |
| mako            | 16.3 ms                                                | 11.6 ms: 1.41x faster                                              |
| genshi_xml      | 66.0 ms                                                | 49.4 ms: 1.34x faster                                              |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-a054a83 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.27x faster                                               |
| async_tree_io            | 1.77 sec                                               | 600 ms: 2.95x faster                                               |
| async_tree_none          | 728 ms                                                 | 263 ms: 2.77x faster                                               |
| async_tree_memoization   | 870 ms                                                 | 317 ms: 2.75x faster                                               |
| generators               | 80.1 ms                                                | 29.7 ms: 2.70x faster                                              |
| deltablue                | 7.91 ms                                                | 3.30 ms: 2.40x faster                                              |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.33x faster                                             |
| go                       | 240 ms                                                 | 113 ms: 2.12x faster                                               |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 494 ms: 2.06x faster                                               |
| deepcopy_memo            | 58.5 us                                                | 28.6 us: 2.04x faster                                              |
| chaos                    | 115 ms                                                 | 56.9 ms: 2.03x faster                                              |
| pylint                   | 551 ms                                                 | 279 ms: 1.98x faster                                               |
| logging_silent           | 190 ns                                                 | 97.1 ns: 1.95x faster                                              |
| raytrace                 | 507 ms                                                 | 261 ms: 1.94x faster                                               |
| richards_super           | 94.7 ms                                                | 49.8 ms: 1.90x faster                                              |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.85x faster                                               |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                               |
| richards                 | 79.3 ms                                                | 43.5 ms: 1.82x faster                                              |
| scimark_monte_carlo      | 118 ms                                                 | 67.0 ms: 1.76x faster                                              |
| crypto_pyaes             | 128 ms                                                 | 73.0 ms: 1.75x faster                                              |
| float                    | 117 ms                                                 | 67.6 ms: 1.73x faster                                              |
| comprehensions           | 28.8 us                                                | 16.9 us: 1.70x faster                                              |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.67x faster                                               |
| hexiom                   | 10.4 ms                                                | 6.33 ms: 1.64x faster                                              |
| pyflate                  | 716 ms                                                 | 442 ms: 1.62x faster                                               |
| nbody                    | 154 ms                                                 | 96.6 ms: 1.59x faster                                              |
| tomli_loads              | 3.14 sec                                               | 1.98 sec: 1.59x faster                                             |
| pickle_pure_python       | 484 us                                                 | 314 us: 1.54x faster                                               |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                              |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                               |
| regex_compile            | 188 ms                                                 | 125 ms: 1.51x faster                                               |
| django_template          | 48.2 ms                                                | 32.2 ms: 1.49x faster                                              |
| genshi_text              | 31.8 ms                                                | 21.3 ms: 1.49x faster                                              |
| logging_simple           | 8.30 us                                                | 5.60 us: 1.48x faster                                              |
| scimark_lu               | 176 ms                                                 | 121 ms: 1.46x faster                                               |
| logging_format           | 9.09 us                                                | 6.26 us: 1.45x faster                                              |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                             |
| dulwich_log              | 84.3 ms                                                | 58.7 ms: 1.44x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 709 ms: 1.44x faster                                               |
| html5lib                 | 88.9 ms                                                | 62.4 ms: 1.43x faster                                              |
| mako                     | 16.3 ms                                                | 11.6 ms: 1.41x faster                                              |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                             |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.1 ms: 1.37x faster                                              |
| coroutines               | 35.1 ms                                                | 25.7 ms: 1.37x faster                                              |
| 2to3                     | 348 ms                                                 | 256 ms: 1.36x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 19.1 ms: 1.35x faster                                              |
| genshi_xml               | 66.0 ms                                                | 49.4 ms: 1.34x faster                                              |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                               |
| scimark_fft              | 466 ms                                                 | 352 ms: 1.32x faster                                               |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.31x faster                                               |
| fannkuch                 | 532 ms                                                 | 407 ms: 1.31x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 60.6 ms: 1.30x faster                                              |
| nqueens                  | 106 ms                                                 | 82.0 ms: 1.29x faster                                              |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                               |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.03 ms: 1.29x faster                                              |
| docutils                 | 3.30 sec                                               | 2.62 sec: 1.26x faster                                             |
| sympy_expand             | 566 ms                                                 | 454 ms: 1.25x faster                                               |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                              |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.21x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.18x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 99.1 ms: 1.16x faster                                              |
| regex_v8                 | 27.8 ms                                                | 23.9 ms: 1.16x faster                                              |
| xml_etree_generate       | 99.4 ms                                                | 87.0 ms: 1.14x faster                                              |
| async_generators         | 444 ms                                                 | 395 ms: 1.12x faster                                               |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                               |
| regex_effbot             | 3.63 ms                                                | 3.26 ms: 1.11x faster                                              |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                              |
| bench_thread_pool        | 986 us                                                 | 888 us: 1.11x faster                                               |
| regex_dna                | 227 ms                                                 | 208 ms: 1.09x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                              |
| json_loads               | 31.2 us                                                | 29.7 us: 1.05x faster                                              |
| json                     | 5.69 ms                                                | 5.60 ms: 1.02x faster                                              |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                               |
| pidigits                 | 191 ms                                                 | 195 ms: 1.02x slower                                               |
| telco                    | 7.27 ms                                                | 7.78 ms: 1.07x slower                                              |
| python_startup_no_site   | 5.93 ms                                                | 6.91 ms: 1.17x slower                                              |
| coverage                 | 79.4 ms                                                | 93.7 ms: 1.18x slower                                              |
| gc_traversal             | 3.62 ms                                                | 4.80 ms: 1.32x slower                                              |
| create_gc_cycles         | 1.62 ms                                                | 2.49 ms: 1.54x slower                                              |
| bench_mp_pool            | 24.0 ms                                                | 82.5 ms: 3.44x slower                                              |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                       |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250430-3.14.0a7+-a054a83/bm-20250430-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-a054a83.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.453x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.28x