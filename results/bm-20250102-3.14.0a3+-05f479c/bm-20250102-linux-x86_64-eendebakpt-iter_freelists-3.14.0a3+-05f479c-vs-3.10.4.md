# Results vs. 3.10.4

- fork: eendebakpt
- ref: iter_freelists
- machine: linux-x86_64
- commit hash: 05f479c
- commit date: 2025-01-02
- overall geometric mean: 1.448x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 253 ms: 1.38x faster                                                 |
| docutils       | 3.30 sec                                               | 2.57 sec: 1.28x faster                                               |
| html5lib       | 88.9 ms                                                | 60.6 ms: 1.47x faster                                                |
| Geometric mean | (ref)                                                  | 1.37x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 607 ms: 2.91x faster                                                 |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 323 ms: 2.69x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 480 ms: 2.12x faster                                                 |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 94.1 ms: 1.63x faster                                                |
| float          | 117 ms                                                 | 72.8 ms: 1.61x faster                                                |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.38x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.50x faster                                                 |
| regex_dna      | 227 ms                                                 | 204 ms: 1.11x faster                                                 |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                |
| regex_effbot   | 3.63 ms                                                | 3.32 ms: 1.09x faster                                                |
| Geometric mean | (ref)                                                  | 1.19x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                               |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 322 us: 1.50x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 58.0 ms: 1.36x faster                                                |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                |
| xml_etree_parse      | 168 ms                                                 | 137 ms: 1.22x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 96.0 ms: 1.20x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 83.2 ms: 1.19x faster                                                |
| json_loads           | 31.2 us                                                | 26.9 us: 1.16x faster                                                |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.4 ms: 1.53x faster                                                |
| genshi_text     | 31.8 ms                                                | 21.9 ms: 1.45x faster                                                |
| mako            | 16.3 ms                                                | 11.8 ms: 1.39x faster                                                |
| genshi_xml      | 66.0 ms                                                | 49.4 ms: 1.34x faster                                                |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 158 us: 3.45x faster                                                 |
| generators               | 80.1 ms                                                | 27.4 ms: 2.92x faster                                                |
| async_tree_io            | 1.77 sec                                               | 607 ms: 2.91x faster                                                 |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 323 ms: 2.69x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.21 ms: 2.47x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 480 ms: 2.12x faster                                                 |
| go                       | 240 ms                                                 | 115 ms: 2.08x faster                                                 |
| pylint                   | 551 ms                                                 | 274 ms: 2.01x faster                                                 |
| chaos                    | 115 ms                                                 | 59.8 ms: 1.93x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 30.9 us: 1.89x faster                                                |
| raytrace                 | 507 ms                                                 | 270 ms: 1.87x faster                                                 |
| richards_super           | 94.7 ms                                                | 50.6 ms: 1.87x faster                                                |
| deepcopy                 | 479 us                                                 | 257 us: 1.86x faster                                                 |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.80x faster                                                 |
| richards                 | 79.3 ms                                                | 44.2 ms: 1.79x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 71.2 ms: 1.79x faster                                                |
| logging_silent           | 190 ns                                                 | 107 ns: 1.77x faster                                                 |
| djangocms                | 38.4 us                                                | 22.1 us: 1.74x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 68.3 ms: 1.73x faster                                                |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                |
| hexiom                   | 10.4 ms                                                | 6.24 ms: 1.67x faster                                                |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.64x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                                |
| nbody                    | 154 ms                                                 | 94.1 ms: 1.63x faster                                                |
| float                    | 117 ms                                                 | 72.8 ms: 1.61x faster                                                |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                               |
| deepcopy_reduce          | 4.17 us                                                | 2.61 us: 1.60x faster                                                |
| django_template          | 48.2 ms                                                | 31.4 ms: 1.53x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                 |
| pyflate                  | 716 ms                                                 | 472 ms: 1.52x faster                                                 |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 322 us: 1.50x faster                                                 |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.50x faster                                                |
| regex_compile            | 188 ms                                                 | 125 ms: 1.50x faster                                                 |
| logging_format           | 9.09 us                                                | 6.19 us: 1.47x faster                                                |
| logging_simple           | 8.30 us                                                | 5.66 us: 1.47x faster                                                |
| html5lib                 | 88.9 ms                                                | 60.6 ms: 1.47x faster                                                |
| genshi_text              | 31.8 ms                                                | 21.9 ms: 1.45x faster                                                |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.4 ms: 1.42x faster                                                |
| sqlglot_normalize        | 143 ms                                                 | 101 ms: 1.42x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                               |
| thrift                   | 1.07 ms                                                | 763 us: 1.40x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 726 ms: 1.40x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                               |
| mako                     | 16.3 ms                                                | 11.8 ms: 1.39x faster                                                |
| 2to3                     | 348 ms                                                 | 253 ms: 1.38x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 58.0 ms: 1.36x faster                                                |
| sqlglot_optimize         | 69.2 ms                                                | 50.8 ms: 1.36x faster                                                |
| sqlalchemy_declarative   | 172 ms                                                 | 128 ms: 1.34x faster                                                 |
| nqueens                  | 106 ms                                                 | 78.9 ms: 1.34x faster                                                |
| genshi_xml               | 66.0 ms                                                | 49.4 ms: 1.34x faster                                                |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 63.7 ms: 1.32x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.32x faster                                                |
| fannkuch                 | 532 ms                                                 | 403 ms: 1.32x faster                                                 |
| scimark_fft              | 466 ms                                                 | 355 ms: 1.31x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.94 ms: 1.31x faster                                                |
| sympy_str                | 346 ms                                                 | 267 ms: 1.30x faster                                                 |
| pathlib                  | 20.5 ms                                                | 15.8 ms: 1.29x faster                                                |
| docutils                 | 3.30 sec                                               | 2.57 sec: 1.28x faster                                               |
| sympy_expand             | 566 ms                                                 | 447 ms: 1.26x faster                                                 |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 137 ms: 1.22x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 96.0 ms: 1.20x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 83.2 ms: 1.19x faster                                                |
| json_loads               | 31.2 us                                                | 26.9 us: 1.16x faster                                                |
| mdp                      | 2.85 sec                                               | 2.48 sec: 1.15x faster                                               |
| bench_thread_pool        | 986 us                                                 | 859 us: 1.15x faster                                                 |
| json                     | 5.69 ms                                                | 4.98 ms: 1.14x faster                                                |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                |
| regex_dna                | 227 ms                                                 | 204 ms: 1.11x faster                                                 |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                |
| regex_effbot             | 3.63 ms                                                | 3.32 ms: 1.09x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                                |
| async_generators         | 444 ms                                                 | 419 ms: 1.06x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                 |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                 |
| mypy2                    | 894 ms                                                 | 938 ms: 1.05x slower                                                 |
| telco                    | 7.27 ms                                                | 7.64 ms: 1.05x slower                                                |
| coverage                 | 79.4 ms                                                | 84.6 ms: 1.06x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                |
| gc_traversal             | 3.62 ms                                                | 4.78 ms: 1.32x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                |
| bench_mp_pool            | 24.0 ms                                                | 81.6 ms: 3.40x slower                                                |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                         |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250102-3.14.0a3+-05f479c/bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.448x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.27x