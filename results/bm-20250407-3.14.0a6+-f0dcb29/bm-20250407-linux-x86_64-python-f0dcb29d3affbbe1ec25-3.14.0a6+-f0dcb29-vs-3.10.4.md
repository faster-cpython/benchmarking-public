# Results vs. 3.10.4

- fork: python
- ref: f0dcb29d3affbbe1ec25
- machine: linux-x86_64
- commit hash: f0dcb29
- commit date: 2025-04-07
- overall geometric mean: 1.469x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-python-f0dcb29d3affbbe1ec25-3.14.0a6+-f0dcb29 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 251 ms: 1.39x faster                                                   |
| docutils       | 3.30 sec                                               | 2.58 sec: 1.28x faster                                                 |
| html5lib       | 88.9 ms                                                | 60.5 ms: 1.47x faster                                                  |
| Geometric mean | (ref)                                                  | 1.38x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-python-f0dcb29d3affbbe1ec25-3.14.0a6+-f0dcb29 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 612 ms: 2.89x faster                                                   |
| async_tree_none         | 728 ms                                                 | 255 ms: 2.86x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 310 ms: 2.80x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 478 ms: 2.12x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.65x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-python-f0dcb29d3affbbe1ec25-3.14.0a6+-f0dcb29 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 67.5 ms: 1.74x faster                                                  |
| nbody          | 154 ms                                                 | 93.2 ms: 1.65x faster                                                  |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.43x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-python-f0dcb29d3affbbe1ec25-3.14.0a6+-f0dcb29 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 124 ms: 1.52x faster                                                   |
| regex_v8       | 27.8 ms                                                | 21.6 ms: 1.29x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.26 ms: 1.11x faster                                                  |
| regex_dna      | 227 ms                                                 | 214 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                  | 1.23x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-python-f0dcb29d3affbbe1ec25-3.14.0a6+-f0dcb29 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 313 us: 1.55x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.53x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 58.6 ms: 1.35x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.23x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 84.3 ms: 1.18x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 98.4 ms: 1.17x faster                                                  |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-python-f0dcb29d3affbbe1ec25-3.14.0a6+-f0dcb29 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 8.21 ms: 1.38x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-python-f0dcb29d3affbbe1ec25-3.14.0a6+-f0dcb29 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 20.7 ms: 1.54x faster                                                  |
| django_template | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                  |
| mako            | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 49.8 ms: 1.33x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-python-f0dcb29d3affbbe1ec25-3.14.0a6+-f0dcb29 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.32x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 612 ms: 2.89x faster                                                   |
| async_tree_none          | 728 ms                                                 | 255 ms: 2.86x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 310 ms: 2.80x faster                                                   |
| generators               | 80.1 ms                                                | 29.5 ms: 2.71x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.37 ms: 2.35x faster                                                  |
| mdp                      | 2.85 sec                                               | 1.24 sec: 2.30x faster                                                 |
| go                       | 240 ms                                                 | 111 ms: 2.15x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 478 ms: 2.12x faster                                                   |
| chaos                    | 115 ms                                                 | 55.8 ms: 2.07x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 28.8 us: 2.03x faster                                                  |
| pylint                   | 551 ms                                                 | 277 ms: 1.99x faster                                                   |
| logging_silent           | 190 ns                                                 | 97.3 ns: 1.95x faster                                                  |
| raytrace                 | 507 ms                                                 | 260 ms: 1.95x faster                                                   |
| deepcopy                 | 479 us                                                 | 247 us: 1.94x faster                                                   |
| richards_super           | 94.7 ms                                                | 49.1 ms: 1.93x faster                                                  |
| richards                 | 79.3 ms                                                | 43.1 ms: 1.84x faster                                                  |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 66.8 ms: 1.77x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 72.9 ms: 1.75x faster                                                  |
| float                    | 117 ms                                                 | 67.5 ms: 1.74x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.9 us: 1.70x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.14 ms: 1.69x faster                                                  |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.68x faster                                                   |
| nbody                    | 154 ms                                                 | 93.2 ms: 1.65x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                 |
| pyflate                  | 716 ms                                                 | 442 ms: 1.62x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.62 us: 1.59x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 313 us: 1.55x faster                                                   |
| genshi_text              | 31.8 ms                                                | 20.7 ms: 1.54x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.53x faster                                                   |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.45 us: 1.52x faster                                                  |
| regex_compile            | 188 ms                                                 | 124 ms: 1.52x faster                                                   |
| django_template          | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                  |
| logging_format           | 9.09 us                                                | 6.08 us: 1.49x faster                                                  |
| html5lib                 | 88.9 ms                                                | 60.5 ms: 1.47x faster                                                  |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                  |
| coroutines               | 35.1 ms                                                | 24.4 ms: 1.44x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 58.8 ms: 1.44x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 718 ms: 1.42x faster                                                   |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                                  |
| 2to3                     | 348 ms                                                 | 251 ms: 1.39x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                                 |
| scimark_fft              | 466 ms                                                 | 342 ms: 1.36x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.77 ms: 1.36x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.1 ms: 1.35x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 58.6 ms: 1.35x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 49.8 ms: 1.33x faster                                                  |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.31x faster                                                   |
| nqueens                  | 106 ms                                                 | 81.4 ms: 1.30x faster                                                  |
| fannkuch                 | 532 ms                                                 | 411 ms: 1.29x faster                                                   |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 21.6 ms: 1.29x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.58 sec: 1.28x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                  |
| sympy_expand             | 566 ms                                                 | 458 ms: 1.24x faster                                                   |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.23x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 84.3 ms: 1.18x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 98.4 ms: 1.17x faster                                                  |
| async_generators         | 444 ms                                                 | 388 ms: 1.14x faster                                                   |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 879 us: 1.12x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.26 ms: 1.11x faster                                                  |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.08x faster                                                  |
| regex_dna                | 227 ms                                                 | 214 ms: 1.06x faster                                                   |
| json                     | 5.69 ms                                                | 5.37 ms: 1.06x faster                                                  |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                                  |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                   |
| telco                    | 7.27 ms                                                | 7.72 ms: 1.06x slower                                                  |
| coverage                 | 79.4 ms                                                | 86.3 ms: 1.09x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.73 ms: 1.31x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 8.21 ms: 1.38x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 82.2 ms: 3.42x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                           |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250407-3.14.0a6+-f0dcb29/bm-20250407-linux-x86_64-python-f0dcb29d3affbbe1ec25-3.14.0a6+-f0dcb29.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.469x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.37x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.27x