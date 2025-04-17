# Results vs. 3.10.4

- fork: brandtbucher
- ref: setlist
- machine: linux-x86_64
- commit hash: 7b2de0a
- commit date: 2025-04-17
- overall geometric mean: 1.461x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 249 ms: 1.40x faster                                            |
| docutils       | 3.30 sec                                               | 2.60 sec: 1.27x faster                                          |
| html5lib       | 88.9 ms                                                | 60.1 ms: 1.48x faster                                           |
| Geometric mean | (ref)                                                  | 1.38x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 613 ms: 2.89x faster                                            |
| async_tree_none         | 728 ms                                                 | 256 ms: 2.84x faster                                            |
| async_tree_memoization  | 870 ms                                                 | 309 ms: 2.82x faster                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 481 ms: 2.11x faster                                            |
| Geometric mean          | (ref)                                                  | 2.64x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 117 ms                                                 | 68.7 ms: 1.71x faster                                           |
| nbody          | 154 ms                                                 | 97.2 ms: 1.58x faster                                           |
| pidigits       | 191 ms                                                 | 190 ms: 1.00x faster                                            |
| Geometric mean | (ref)                                                  | 1.39x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.51x faster                                            |
| regex_v8       | 27.8 ms                                                | 22.6 ms: 1.23x faster                                           |
| regex_effbot   | 3.63 ms                                                | 3.27 ms: 1.11x faster                                           |
| regex_dna      | 227 ms                                                 | 206 ms: 1.10x faster                                            |
| Geometric mean | (ref)                                                  | 1.23x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                          |
| pickle_pure_python   | 484 us                                                 | 311 us: 1.56x faster                                            |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                            |
| xml_etree_process    | 79.1 ms                                                | 59.2 ms: 1.34x faster                                           |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.25x faster                                           |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                            |
| xml_etree_generate   | 99.4 ms                                                | 84.3 ms: 1.18x faster                                           |
| xml_etree_iterparse  | 115 ms                                                 | 99.7 ms: 1.16x faster                                           |
| json_loads           | 31.2 us                                                | 29.9 us: 1.04x faster                                           |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                           |
| python_startup_no_site | 5.93 ms                                                | 8.20 ms: 1.38x slower                                           |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 20.9 ms: 1.53x faster                                           |
| django_template | 48.2 ms                                                | 32.2 ms: 1.49x faster                                           |
| mako            | 16.3 ms                                                | 11.5 ms: 1.42x faster                                           |
| genshi_xml      | 66.0 ms                                                | 48.7 ms: 1.35x faster                                           |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.28x faster                                            |
| async_tree_io            | 1.77 sec                                               | 613 ms: 2.89x faster                                            |
| async_tree_none          | 728 ms                                                 | 256 ms: 2.84x faster                                            |
| async_tree_memoization   | 870 ms                                                 | 309 ms: 2.82x faster                                            |
| generators               | 80.1 ms                                                | 30.7 ms: 2.61x faster                                           |
| deltablue                | 7.91 ms                                                | 3.37 ms: 2.35x faster                                           |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.34x faster                                          |
| go                       | 240 ms                                                 | 110 ms: 2.18x faster                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 481 ms: 2.11x faster                                            |
| chaos                    | 115 ms                                                 | 56.0 ms: 2.06x faster                                           |
| deepcopy_memo            | 58.5 us                                                | 28.4 us: 2.06x faster                                           |
| logging_silent           | 190 ns                                                 | 93.3 ns: 2.03x faster                                           |
| pylint                   | 551 ms                                                 | 278 ms: 1.98x faster                                            |
| raytrace                 | 507 ms                                                 | 259 ms: 1.96x faster                                            |
| richards_super           | 94.7 ms                                                | 49.2 ms: 1.92x faster                                           |
| deepcopy                 | 479 us                                                 | 250 us: 1.92x faster                                            |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                            |
| richards                 | 79.3 ms                                                | 43.0 ms: 1.84x faster                                           |
| scimark_monte_carlo      | 118 ms                                                 | 66.6 ms: 1.78x faster                                           |
| crypto_pyaes             | 128 ms                                                 | 73.1 ms: 1.75x faster                                           |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                           |
| float                    | 117 ms                                                 | 68.7 ms: 1.71x faster                                           |
| hexiom                   | 10.4 ms                                                | 6.27 ms: 1.66x faster                                           |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.63x faster                                            |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                          |
| pyflate                  | 716 ms                                                 | 451 ms: 1.59x faster                                            |
| nbody                    | 154 ms                                                 | 97.2 ms: 1.58x faster                                           |
| pickle_pure_python       | 484 us                                                 | 311 us: 1.56x faster                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                           |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                            |
| genshi_text              | 31.8 ms                                                | 20.9 ms: 1.53x faster                                           |
| logging_simple           | 8.30 us                                                | 5.49 us: 1.51x faster                                           |
| regex_compile            | 188 ms                                                 | 125 ms: 1.51x faster                                            |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.50x faster                                            |
| django_template          | 48.2 ms                                                | 32.2 ms: 1.49x faster                                           |
| logging_format           | 9.09 us                                                | 6.14 us: 1.48x faster                                           |
| html5lib                 | 88.9 ms                                                | 60.1 ms: 1.48x faster                                           |
| coroutines               | 35.1 ms                                                | 24.0 ms: 1.46x faster                                           |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                          |
| pprint_safe_repr         | 1.02 sec                                               | 714 ms: 1.42x faster                                            |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.42x faster                                           |
| dulwich_log              | 84.3 ms                                                | 59.5 ms: 1.42x faster                                           |
| 2to3                     | 348 ms                                                 | 249 ms: 1.40x faster                                            |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                           |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                          |
| sympy_integrate          | 25.8 ms                                                | 19.0 ms: 1.36x faster                                           |
| genshi_xml               | 66.0 ms                                                | 48.7 ms: 1.35x faster                                           |
| xml_etree_process        | 79.1 ms                                                | 59.2 ms: 1.34x faster                                           |
| nqueens                  | 106 ms                                                 | 79.3 ms: 1.33x faster                                           |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.89 ms: 1.32x faster                                           |
| scimark_fft              | 466 ms                                                 | 356 ms: 1.31x faster                                            |
| sympy_str                | 346 ms                                                 | 265 ms: 1.31x faster                                            |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.30x faster                                            |
| fannkuch                 | 532 ms                                                 | 414 ms: 1.28x faster                                            |
| docutils                 | 3.30 sec                                               | 2.60 sec: 1.27x faster                                          |
| sympy_expand             | 566 ms                                                 | 450 ms: 1.26x faster                                            |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.25x faster                                           |
| regex_v8                 | 27.8 ms                                                | 22.6 ms: 1.23x faster                                           |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.22x faster                                           |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                            |
| xml_etree_generate       | 99.4 ms                                                | 84.3 ms: 1.18x faster                                           |
| xml_etree_iterparse      | 115 ms                                                 | 99.7 ms: 1.16x faster                                           |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                            |
| async_generators         | 444 ms                                                 | 398 ms: 1.12x faster                                            |
| regex_effbot             | 3.63 ms                                                | 3.27 ms: 1.11x faster                                           |
| bench_thread_pool        | 986 us                                                 | 889 us: 1.11x faster                                            |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                           |
| regex_dna                | 227 ms                                                 | 206 ms: 1.10x faster                                            |
| sqlite_synth             | 3.02 us                                                | 2.78 us: 1.09x faster                                           |
| json                     | 5.69 ms                                                | 5.33 ms: 1.07x faster                                           |
| json_loads               | 31.2 us                                                | 29.9 us: 1.04x faster                                           |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                            |
| pidigits                 | 191 ms                                                 | 190 ms: 1.00x faster                                            |
| telco                    | 7.27 ms                                                | 7.85 ms: 1.08x slower                                           |
| coverage                 | 79.4 ms                                                | 88.2 ms: 1.11x slower                                           |
| python_startup_no_site   | 5.93 ms                                                | 8.20 ms: 1.38x slower                                           |
| gc_traversal             | 3.62 ms                                                | 5.04 ms: 1.39x slower                                           |
| create_gc_cycles         | 1.62 ms                                                | 2.49 ms: 1.53x slower                                           |
| bench_mp_pool            | 24.0 ms                                                | 81.8 ms: 3.41x slower                                           |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                    |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250417-3.14.0a7+-7b2de0a/bm-20250417-linux-x86_64-brandtbucher-setlist-3.14.0a7+-7b2de0a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.461x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.28x