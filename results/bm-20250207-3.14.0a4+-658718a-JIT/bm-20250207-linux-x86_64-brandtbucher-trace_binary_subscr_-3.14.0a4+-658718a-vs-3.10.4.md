# Results vs. 3.10.4

- fork: brandtbucher
- ref: trace_binary_subscr_
- machine: linux-x86_64
- commit hash: 658718a
- commit date: 2025-02-07
- overall geometric mean: 1.447x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 261 ms: 1.33x faster                                                         |
| docutils       | 3.30 sec                                               | 2.71 sec: 1.22x faster                                                       |
| html5lib       | 88.9 ms                                                | 61.6 ms: 1.44x faster                                                        |
| Geometric mean | (ref)                                                  | 1.33x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 624 ms: 2.83x faster                                                         |
| async_tree_none         | 728 ms                                                 | 270 ms: 2.70x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 327 ms: 2.66x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 501 ms: 2.03x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.53x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 71.0 ms: 1.65x faster                                                        |
| nbody          | 154 ms                                                 | 96.7 ms: 1.59x faster                                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.39x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.48x faster                                                         |
| regex_effbot   | 3.63 ms                                                | 2.99 ms: 1.21x faster                                                        |
| regex_v8       | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                        |
| regex_dna      | 227 ms                                                 | 199 ms: 1.14x faster                                                         |
| Geometric mean | (ref)                                                  | 1.24x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.84 sec: 1.70x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 200 us: 1.65x faster                                                         |
| pickle_pure_python   | 484 us                                                 | 318 us: 1.53x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 55.8 ms: 1.42x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 79.5 ms: 1.25x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 95.5 ms: 1.21x faster                                                        |
| json_dumps           | 14.2 ms                                                | 11.8 ms: 1.20x faster                                                        |
| json_loads           | 31.2 us                                                | 28.9 us: 1.08x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.2 ms: 1.61x faster                                                        |
| django_template | 48.2 ms                                                | 32.1 ms: 1.50x faster                                                        |
| genshi_text     | 31.8 ms                                                | 21.8 ms: 1.46x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 50.2 ms: 1.32x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.47x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.32x faster                                                         |
| generators               | 80.1 ms                                                | 28.1 ms: 2.85x faster                                                        |
| async_tree_io            | 1.77 sec                                               | 624 ms: 2.83x faster                                                         |
| async_tree_none          | 728 ms                                                 | 270 ms: 2.70x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 327 ms: 2.66x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.31 ms: 2.39x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 501 ms: 2.03x faster                                                         |
| go                       | 240 ms                                                 | 120 ms: 2.00x faster                                                         |
| pylint                   | 551 ms                                                 | 280 ms: 1.97x faster                                                         |
| chaos                    | 115 ms                                                 | 58.7 ms: 1.97x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 30.8 us: 1.90x faster                                                        |
| richards_super           | 94.7 ms                                                | 50.4 ms: 1.88x faster                                                        |
| deepcopy                 | 479 us                                                 | 261 us: 1.84x faster                                                         |
| raytrace                 | 507 ms                                                 | 276 ms: 1.84x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 69.8 ms: 1.83x faster                                                        |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                         |
| spectral_norm            | 170 ms                                                 | 93.4 ms: 1.82x faster                                                        |
| richards                 | 79.3 ms                                                | 44.2 ms: 1.79x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 66.5 ms: 1.78x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                        |
| logging_silent           | 190 ns                                                 | 111 ns: 1.71x faster                                                         |
| tomli_loads              | 3.14 sec                                               | 1.84 sec: 1.70x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 200 us: 1.65x faster                                                         |
| float                    | 117 ms                                                 | 71.0 ms: 1.65x faster                                                        |
| comprehensions           | 28.8 us                                                | 17.6 us: 1.63x faster                                                        |
| pyflate                  | 716 ms                                                 | 439 ms: 1.63x faster                                                         |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.62x faster                                                        |
| mako                     | 16.3 ms                                                | 10.2 ms: 1.61x faster                                                        |
| nbody                    | 154 ms                                                 | 96.7 ms: 1.59x faster                                                        |
| hexiom                   | 10.4 ms                                                | 6.66 ms: 1.56x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                        |
| coroutines               | 35.1 ms                                                | 22.8 ms: 1.54x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 318 us: 1.53x faster                                                         |
| logging_simple           | 8.30 us                                                | 5.47 us: 1.52x faster                                                        |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.51x faster                                                         |
| django_template          | 48.2 ms                                                | 32.1 ms: 1.50x faster                                                        |
| logging_format           | 9.09 us                                                | 6.10 us: 1.49x faster                                                        |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                                         |
| regex_compile            | 188 ms                                                 | 128 ms: 1.48x faster                                                         |
| genshi_text              | 31.8 ms                                                | 21.8 ms: 1.46x faster                                                        |
| html5lib                 | 88.9 ms                                                | 61.6 ms: 1.44x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 55.8 ms: 1.42x faster                                                        |
| thrift                   | 1.07 ms                                                | 767 us: 1.40x faster                                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.63 ms: 1.40x faster                                                        |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.37x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 750 ms: 1.36x faster                                                         |
| fannkuch                 | 532 ms                                                 | 392 ms: 1.36x faster                                                         |
| 2to3                     | 348 ms                                                 | 261 ms: 1.33x faster                                                         |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.33x faster                                                         |
| genshi_xml               | 66.0 ms                                                | 50.2 ms: 1.32x faster                                                        |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.31x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.21 sec: 1.31x faster                                                       |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                         |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 20.2 ms: 1.28x faster                                                        |
| sqlglot_optimize         | 69.2 ms                                                | 54.1 ms: 1.28x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 66.0 ms: 1.28x faster                                                        |
| sympy_str                | 346 ms                                                 | 275 ms: 1.26x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 79.5 ms: 1.25x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.71 sec: 1.22x faster                                                       |
| regex_effbot             | 3.63 ms                                                | 2.99 ms: 1.21x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 95.5 ms: 1.21x faster                                                        |
| json_dumps               | 14.2 ms                                                | 11.8 ms: 1.20x faster                                                        |
| sympy_expand             | 566 ms                                                 | 473 ms: 1.20x faster                                                         |
| regex_v8                 | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                        |
| nqueens                  | 106 ms                                                 | 91.1 ms: 1.16x faster                                                        |
| regex_dna                | 227 ms                                                 | 199 ms: 1.14x faster                                                         |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 884 us: 1.12x faster                                                         |
| mdp                      | 2.85 sec                                               | 2.56 sec: 1.11x faster                                                       |
| sqlite_synth             | 3.02 us                                                | 2.73 us: 1.11x faster                                                        |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                         |
| json                     | 5.69 ms                                                | 5.17 ms: 1.10x faster                                                        |
| json_loads               | 31.2 us                                                | 28.9 us: 1.08x faster                                                        |
| async_generators         | 444 ms                                                 | 413 ms: 1.08x faster                                                         |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                         |
| telco                    | 7.27 ms                                                | 7.68 ms: 1.06x slower                                                        |
| coverage                 | 79.4 ms                                                | 90.0 ms: 1.13x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 4.77 ms: 1.31x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 80.7 ms: 3.36x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                                 |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250207-3.14.0a4+-658718a-JIT/bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.447x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.28x