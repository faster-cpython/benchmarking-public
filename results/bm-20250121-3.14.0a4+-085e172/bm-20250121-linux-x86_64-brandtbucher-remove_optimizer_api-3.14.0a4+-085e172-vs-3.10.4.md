# Results vs. 3.10.4

- fork: brandtbucher
- ref: remove_optimizer_api
- machine: linux-x86_64
- commit hash: 085e172
- commit date: 2025-01-21
- overall geometric mean: 1.445x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 256 ms: 1.36x faster                                                         |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                       |
| html5lib       | 88.9 ms                                                | 60.8 ms: 1.46x faster                                                        |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 603 ms: 2.93x faster                                                         |
| async_tree_none         | 728 ms                                                 | 258 ms: 2.83x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 324 ms: 2.69x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 491 ms: 2.07x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.7 ms: 1.66x faster                                                        |
| nbody          | 154 ms                                                 | 92.9 ms: 1.65x faster                                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.41x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.48x faster                                                         |
| regex_effbot   | 3.63 ms                                                | 3.15 ms: 1.15x faster                                                        |
| regex_v8       | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                        |
| regex_dna      | 227 ms                                                 | 208 ms: 1.09x faster                                                         |
| Geometric mean | (ref)                                                  | 1.20x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.99 sec: 1.58x faster                                                       |
| pickle_pure_python   | 484 us                                                 | 331 us: 1.47x faster                                                         |
| unpickle_pure_python | 331 us                                                 | 226 us: 1.46x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 61.4 ms: 1.29x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                         |
| json_dumps           | 14.2 ms                                                | 11.9 ms: 1.19x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 97.2 ms: 1.19x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 83.8 ms: 1.19x faster                                                        |
| json_loads           | 31.2 us                                                | 29.0 us: 1.08x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.28x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.8 ms: 1.51x faster                                                        |
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                        |
| genshi_text     | 31.8 ms                                                | 22.2 ms: 1.44x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 50.4 ms: 1.31x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.34x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 603 ms: 2.93x faster                                                         |
| generators               | 80.1 ms                                                | 28.2 ms: 2.84x faster                                                        |
| async_tree_none          | 728 ms                                                 | 258 ms: 2.83x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 324 ms: 2.69x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.16 ms: 2.50x faster                                                        |
| go                       | 240 ms                                                 | 116 ms: 2.07x faster                                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 491 ms: 2.07x faster                                                         |
| pylint                   | 551 ms                                                 | 274 ms: 2.01x faster                                                         |
| chaos                    | 115 ms                                                 | 59.4 ms: 1.94x faster                                                        |
| logging_silent           | 190 ns                                                 | 100.0 ns: 1.90x faster                                                       |
| richards_super           | 94.7 ms                                                | 50.2 ms: 1.89x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 31.2 us: 1.87x faster                                                        |
| raytrace                 | 507 ms                                                 | 272 ms: 1.87x faster                                                         |
| deepcopy                 | 479 us                                                 | 257 us: 1.86x faster                                                         |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                                         |
| richards                 | 79.3 ms                                                | 43.8 ms: 1.81x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 73.0 ms: 1.75x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 68.3 ms: 1.73x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.25 ms: 1.73x faster                                                        |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                        |
| hexiom                   | 10.4 ms                                                | 6.23 ms: 1.67x faster                                                        |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.66x faster                                                         |
| float                    | 117 ms                                                 | 70.7 ms: 1.66x faster                                                        |
| nbody                    | 154 ms                                                 | 92.9 ms: 1.65x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.56 ms: 1.65x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.99 sec: 1.58x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.57x faster                                                        |
| pyflate                  | 716 ms                                                 | 466 ms: 1.54x faster                                                         |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.54x faster                                                         |
| django_template          | 48.2 ms                                                | 31.8 ms: 1.51x faster                                                        |
| coroutines               | 35.1 ms                                                | 23.6 ms: 1.49x faster                                                        |
| regex_compile            | 188 ms                                                 | 128 ms: 1.48x faster                                                         |
| logging_simple           | 8.30 us                                                | 5.65 us: 1.47x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 331 us: 1.47x faster                                                         |
| html5lib                 | 88.9 ms                                                | 60.8 ms: 1.46x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 226 us: 1.46x faster                                                         |
| logging_format           | 9.09 us                                                | 6.25 us: 1.45x faster                                                        |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                        |
| genshi_text              | 31.8 ms                                                | 22.2 ms: 1.44x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.61 ms: 1.40x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 727 ms: 1.40x faster                                                         |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.7 ms: 1.40x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                                       |
| scimark_fft              | 466 ms                                                 | 340 ms: 1.37x faster                                                         |
| thrift                   | 1.07 ms                                                | 784 us: 1.37x faster                                                         |
| sqlglot_normalize        | 143 ms                                                 | 105 ms: 1.36x faster                                                         |
| 2to3                     | 348 ms                                                 | 256 ms: 1.36x faster                                                         |
| nqueens                  | 106 ms                                                 | 78.7 ms: 1.34x faster                                                        |
| sympy_sum                | 196 ms                                                 | 146 ms: 1.34x faster                                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.31x faster                                                         |
| sympy_integrate          | 25.8 ms                                                | 19.6 ms: 1.31x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 50.4 ms: 1.31x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 64.5 ms: 1.31x faster                                                        |
| fannkuch                 | 532 ms                                                 | 407 ms: 1.31x faster                                                         |
| sqlglot_optimize         | 69.2 ms                                                | 53.0 ms: 1.30x faster                                                        |
| sympy_str                | 346 ms                                                 | 265 ms: 1.30x faster                                                         |
| xml_etree_process        | 79.1 ms                                                | 61.4 ms: 1.29x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                       |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                        |
| sympy_expand             | 566 ms                                                 | 453 ms: 1.25x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                         |
| json_dumps               | 14.2 ms                                                | 11.9 ms: 1.19x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 97.2 ms: 1.19x faster                                                        |
| xml_etree_generate       | 99.4 ms                                                | 83.8 ms: 1.19x faster                                                        |
| regex_effbot             | 3.63 ms                                                | 3.15 ms: 1.15x faster                                                        |
| mdp                      | 2.85 sec                                               | 2.49 sec: 1.14x faster                                                       |
| async_generators         | 444 ms                                                 | 388 ms: 1.14x faster                                                         |
| bench_thread_pool        | 986 us                                                 | 864 us: 1.14x faster                                                         |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                        |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                         |
| regex_v8                 | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                        |
| json                     | 5.69 ms                                                | 5.18 ms: 1.10x faster                                                        |
| regex_dna                | 227 ms                                                 | 208 ms: 1.09x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.08x faster                                                        |
| json_loads               | 31.2 us                                                | 29.0 us: 1.08x faster                                                        |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                         |
| telco                    | 7.27 ms                                                | 7.86 ms: 1.08x slower                                                        |
| coverage                 | 79.4 ms                                                | 89.8 ms: 1.13x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 4.77 ms: 1.32x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.45 ms: 1.51x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 81.7 ms: 3.40x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                                 |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250121-3.14.0a4+-085e172/bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.445x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.26x