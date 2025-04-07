# Results vs. 3.10.4

- fork: iritkatriel
- ref: stats
- machine: linux-x86_64
- commit hash: 8475f64
- commit date: 2025-04-07
- overall geometric mean: 1.478x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.34x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 250 ms: 1.39x faster                                         |
| docutils       | 3.30 sec                                               | 2.57 sec: 1.28x faster                                       |
| html5lib       | 88.9 ms                                                | 60.4 ms: 1.47x faster                                        |
| Geometric mean | (ref)                                                  | 1.38x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 608 ms: 2.91x faster                                         |
| async_tree_none         | 728 ms                                                 | 255 ms: 2.86x faster                                         |
| async_tree_memoization  | 870 ms                                                 | 307 ms: 2.83x faster                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 476 ms: 2.14x faster                                         |
| Geometric mean          | (ref)                                                  | 2.66x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.4 ms: 1.78x faster                                        |
| float          | 117 ms                                                 | 66.3 ms: 1.77x faster                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                         |
| Geometric mean | (ref)                                                  | 1.48x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 124 ms: 1.52x faster                                         |
| regex_v8       | 27.8 ms                                                | 22.5 ms: 1.23x faster                                        |
| regex_effbot   | 3.63 ms                                                | 3.45 ms: 1.05x faster                                        |
| regex_dna      | 227 ms                                                 | 217 ms: 1.04x faster                                         |
| Geometric mean | (ref)                                                  | 1.20x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.92 sec: 1.64x faster                                       |
| pickle_pure_python   | 484 us                                                 | 313 us: 1.55x faster                                         |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.53x faster                                         |
| xml_etree_process    | 79.1 ms                                                | 58.6 ms: 1.35x faster                                        |
| json_dumps           | 14.2 ms                                                | 11.8 ms: 1.20x faster                                        |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                         |
| xml_etree_generate   | 99.4 ms                                                | 83.8 ms: 1.19x faster                                        |
| xml_etree_iterparse  | 115 ms                                                 | 98.6 ms: 1.17x faster                                        |
| json_loads           | 31.2 us                                                | 29.9 us: 1.04x faster                                        |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.10x faster                                        |
| python_startup_no_site | 5.93 ms                                                | 8.21 ms: 1.38x slower                                        |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 20.7 ms: 1.54x faster                                        |
| django_template | 48.2 ms                                                | 31.3 ms: 1.54x faster                                        |
| mako            | 16.3 ms                                                | 11.0 ms: 1.48x faster                                        |
| genshi_xml      | 66.0 ms                                                | 48.6 ms: 1.36x faster                                        |
| Geometric mean  | (ref)                                                  | 1.48x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.31x faster                                         |
| async_tree_io            | 1.77 sec                                               | 608 ms: 2.91x faster                                         |
| async_tree_none          | 728 ms                                                 | 255 ms: 2.86x faster                                         |
| async_tree_memoization   | 870 ms                                                 | 307 ms: 2.83x faster                                         |
| generators               | 80.1 ms                                                | 29.8 ms: 2.69x faster                                        |
| deltablue                | 7.91 ms                                                | 3.32 ms: 2.38x faster                                        |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.34x faster                                       |
| go                       | 240 ms                                                 | 110 ms: 2.19x faster                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 476 ms: 2.14x faster                                         |
| chaos                    | 115 ms                                                 | 55.6 ms: 2.08x faster                                        |
| deepcopy_memo            | 58.5 us                                                | 28.6 us: 2.04x faster                                        |
| raytrace                 | 507 ms                                                 | 254 ms: 2.00x faster                                         |
| pylint                   | 551 ms                                                 | 276 ms: 2.00x faster                                         |
| deepcopy                 | 479 us                                                 | 245 us: 1.95x faster                                         |
| richards_super           | 94.7 ms                                                | 48.5 ms: 1.95x faster                                        |
| logging_silent           | 190 ns                                                 | 97.2 ns: 1.95x faster                                        |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.87x faster                                         |
| richards                 | 79.3 ms                                                | 42.9 ms: 1.85x faster                                        |
| scimark_monte_carlo      | 118 ms                                                 | 64.0 ms: 1.85x faster                                        |
| nbody                    | 154 ms                                                 | 86.4 ms: 1.78x faster                                        |
| crypto_pyaes             | 128 ms                                                 | 72.0 ms: 1.77x faster                                        |
| float                    | 117 ms                                                 | 66.3 ms: 1.77x faster                                        |
| spectral_norm            | 170 ms                                                 | 97.0 ms: 1.75x faster                                        |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.73x faster                                        |
| hexiom                   | 10.4 ms                                                | 6.21 ms: 1.67x faster                                        |
| tomli_loads              | 3.14 sec                                               | 1.92 sec: 1.64x faster                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.57 us: 1.62x faster                                        |
| pyflate                  | 716 ms                                                 | 446 ms: 1.61x faster                                         |
| pickle_pure_python       | 484 us                                                 | 313 us: 1.55x faster                                         |
| genshi_text              | 31.8 ms                                                | 20.7 ms: 1.54x faster                                        |
| django_template          | 48.2 ms                                                | 31.3 ms: 1.54x faster                                        |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                        |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.53x faster                                         |
| regex_compile            | 188 ms                                                 | 124 ms: 1.52x faster                                         |
| logging_simple           | 8.30 us                                                | 5.48 us: 1.52x faster                                        |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.51x faster                                         |
| logging_format           | 9.09 us                                                | 6.07 us: 1.50x faster                                        |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.48x faster                                        |
| html5lib                 | 88.9 ms                                                | 60.4 ms: 1.47x faster                                        |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                       |
| pprint_safe_repr         | 1.02 sec                                               | 712 ms: 1.43x faster                                         |
| dulwich_log              | 84.3 ms                                                | 59.0 ms: 1.43x faster                                        |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.6 ms: 1.40x faster                                        |
| scimark_fft              | 466 ms                                                 | 332 ms: 1.40x faster                                         |
| 2to3                     | 348 ms                                                 | 250 ms: 1.39x faster                                         |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.38x faster                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.73 ms: 1.37x faster                                        |
| genshi_xml               | 66.0 ms                                                | 48.6 ms: 1.36x faster                                        |
| sympy_integrate          | 25.8 ms                                                | 19.0 ms: 1.36x faster                                        |
| xml_etree_process        | 79.1 ms                                                | 58.6 ms: 1.35x faster                                        |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.32x faster                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.32x faster                                         |
| nqueens                  | 106 ms                                                 | 80.4 ms: 1.32x faster                                        |
| fannkuch                 | 532 ms                                                 | 409 ms: 1.30x faster                                         |
| sympy_str                | 346 ms                                                 | 267 ms: 1.30x faster                                         |
| docutils                 | 3.30 sec                                               | 2.57 sec: 1.28x faster                                       |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.25x faster                                        |
| sympy_expand             | 566 ms                                                 | 455 ms: 1.24x faster                                         |
| regex_v8                 | 27.8 ms                                                | 22.5 ms: 1.23x faster                                        |
| json_dumps               | 14.2 ms                                                | 11.8 ms: 1.20x faster                                        |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                         |
| xml_etree_generate       | 99.4 ms                                                | 83.8 ms: 1.19x faster                                        |
| xml_etree_iterparse      | 115 ms                                                 | 98.6 ms: 1.17x faster                                        |
| async_generators         | 444 ms                                                 | 390 ms: 1.14x faster                                         |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                         |
| bench_thread_pool        | 986 us                                                 | 875 us: 1.13x faster                                         |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.10x faster                                        |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                        |
| json                     | 5.69 ms                                                | 5.36 ms: 1.06x faster                                        |
| regex_effbot             | 3.63 ms                                                | 3.45 ms: 1.05x faster                                        |
| regex_dna                | 227 ms                                                 | 217 ms: 1.04x faster                                         |
| json_loads               | 31.2 us                                                | 29.9 us: 1.04x faster                                        |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                         |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                         |
| telco                    | 7.27 ms                                                | 7.79 ms: 1.07x slower                                        |
| coverage                 | 79.4 ms                                                | 85.4 ms: 1.08x slower                                        |
| gc_traversal             | 3.62 ms                                                | 4.60 ms: 1.27x slower                                        |
| python_startup_no_site   | 5.93 ms                                                | 8.21 ms: 1.38x slower                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.52x slower                                        |
| bench_mp_pool            | 24.0 ms                                                | 82.3 ms: 3.43x slower                                        |
| Geometric mean           | (ref)                                                  | 1.45x faster                                                 |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250407-3.14.0a6+-8475f64/bm-20250407-linux-x86_64-iritkatriel-stats-3.14.0a6+-8475f64.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.478x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.39x
- 95% likely to have a speedup of 1.37x
- 99% likely to have a speedup of 1.34x

# Memory
- memory change: 1.27x