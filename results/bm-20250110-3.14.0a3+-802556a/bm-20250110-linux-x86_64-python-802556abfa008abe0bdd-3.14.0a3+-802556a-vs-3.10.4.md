# Results vs. 3.10.4

- fork: python
- ref: 802556abfa008abe0bdd
- machine: linux-x86_64
- commit hash: 802556a
- commit date: 2025-01-10
- overall geometric mean: 1.439x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                   |
| docutils       | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                 |
| html5lib       | 88.9 ms                                                | 61.9 ms: 1.44x faster                                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 602 ms: 2.94x faster                                                   |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 324 ms: 2.68x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 485 ms: 2.10x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 93.8 ms: 1.64x faster                                                  |
| float          | 117 ms                                                 | 72.7 ms: 1.61x faster                                                  |
| pidigits       | 191 ms                                                 | 190 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.38x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                   |
| regex_v8       | 27.8 ms                                                | 25.8 ms: 1.08x faster                                                  |
| regex_dna      | 227 ms                                                 | 213 ms: 1.06x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.43 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.01 sec: 1.56x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 324 us: 1.50x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 60.2 ms: 1.31x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.3 ms: 1.25x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 96.9 ms: 1.19x faster                                                  |
| json_loads           | 31.2 us                                                | 26.7 us: 1.17x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 86.0 ms: 1.16x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.7 ms: 1.52x faster                                                  |
| genshi_text     | 31.8 ms                                                | 22.2 ms: 1.44x faster                                                  |
| mako            | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 49.4 ms: 1.34x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.36x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 602 ms: 2.94x faster                                                   |
| generators               | 80.1 ms                                                | 27.4 ms: 2.92x faster                                                  |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 324 ms: 2.68x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.27 ms: 2.42x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 485 ms: 2.10x faster                                                   |
| go                       | 240 ms                                                 | 118 ms: 2.04x faster                                                   |
| pylint                   | 551 ms                                                 | 277 ms: 1.99x faster                                                   |
| chaos                    | 115 ms                                                 | 61.1 ms: 1.89x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 31.0 us: 1.88x faster                                                  |
| raytrace                 | 507 ms                                                 | 273 ms: 1.85x faster                                                   |
| richards_super           | 94.7 ms                                                | 51.2 ms: 1.85x faster                                                  |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                   |
| logging_silent           | 190 ns                                                 | 106 ns: 1.80x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 72.1 ms: 1.77x faster                                                  |
| scimark_sor              | 220 ms                                                 | 125 ms: 1.76x faster                                                   |
| richards                 | 79.3 ms                                                | 45.2 ms: 1.76x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 67.5 ms: 1.75x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.72x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.70x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.35 ms: 1.64x faster                                                  |
| nbody                    | 154 ms                                                 | 93.8 ms: 1.64x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                                  |
| float                    | 117 ms                                                 | 72.7 ms: 1.61x faster                                                  |
| spectral_norm            | 170 ms                                                 | 107 ms: 1.59x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.57x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.01 sec: 1.56x faster                                                 |
| django_template          | 48.2 ms                                                | 31.7 ms: 1.52x faster                                                  |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 324 us: 1.50x faster                                                   |
| pyflate                  | 716 ms                                                 | 480 ms: 1.49x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.59 us: 1.49x faster                                                  |
| logging_format           | 9.09 us                                                | 6.15 us: 1.48x faster                                                  |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                   |
| coroutines               | 35.1 ms                                                | 24.3 ms: 1.44x faster                                                  |
| html5lib                 | 88.9 ms                                                | 61.9 ms: 1.44x faster                                                  |
| genshi_text              | 31.8 ms                                                | 22.2 ms: 1.44x faster                                                  |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                 |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.6 ms: 1.41x faster                                                  |
| thrift                   | 1.07 ms                                                | 763 us: 1.40x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 732 ms: 1.39x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 104 ms: 1.37x faster                                                   |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 49.4 ms: 1.34x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 129 ms: 1.34x faster                                                   |
| scimark_fft              | 466 ms                                                 | 349 ms: 1.33x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.87 ms: 1.33x faster                                                  |
| nqueens                  | 106 ms                                                 | 79.7 ms: 1.33x faster                                                  |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.32x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 63.9 ms: 1.32x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 52.5 ms: 1.32x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 60.2 ms: 1.31x faster                                                  |
| pathlib                  | 20.5 ms                                                | 15.6 ms: 1.31x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.29x faster                                                  |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                   |
| fannkuch                 | 532 ms                                                 | 412 ms: 1.29x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                 |
| json_dumps               | 14.2 ms                                                | 11.3 ms: 1.25x faster                                                  |
| sympy_expand             | 566 ms                                                 | 455 ms: 1.24x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 96.9 ms: 1.19x faster                                                  |
| json_loads               | 31.2 us                                                | 26.7 us: 1.17x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 86.0 ms: 1.16x faster                                                  |
| json                     | 5.69 ms                                                | 4.93 ms: 1.15x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 863 us: 1.14x faster                                                   |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                  |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.61 sec: 1.09x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 25.8 ms: 1.08x faster                                                  |
| regex_dna                | 227 ms                                                 | 213 ms: 1.06x faster                                                   |
| async_generators         | 444 ms                                                 | 418 ms: 1.06x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.43 ms: 1.06x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                   |
| pidigits                 | 191 ms                                                 | 190 ms: 1.01x faster                                                   |
| coverage                 | 79.4 ms                                                | 83.6 ms: 1.05x slower                                                  |
| telco                    | 7.27 ms                                                | 7.74 ms: 1.07x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.95 ms: 1.37x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.52x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 81.5 ms: 3.39x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                           |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250110-3.14.0a3+-802556a/bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.439x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.26x