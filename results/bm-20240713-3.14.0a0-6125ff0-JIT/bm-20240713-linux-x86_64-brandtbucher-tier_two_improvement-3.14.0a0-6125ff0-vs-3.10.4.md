# Results vs. 3.10.4

- fork: brandtbucher
- ref: tier_two_improvement
- machine: linux-x86_64
- commit hash: 6125ff0
- commit date: 2024-07-13
- overall geometric mean: 1.41x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 275 ms: 1.27x faster                                                        |
| docutils       | 3.30 sec                                               | 2.89 sec: 1.14x faster                                                      |
| html5lib       | 88.9 ms                                                | 65.2 ms: 1.36x faster                                                       |
| tornado_http   | 136 ms                                                 | 93.3 ms: 1.46x faster                                                       |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 325 ms: 2.24x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 412 ms: 2.11x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 846 ms: 2.09x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 565 ms: 1.80x faster                                                        |
| Geometric mean          | (ref)                                                  | 2.05x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.9 ms: 1.92x faster                                                       |
| float          | 117 ms                                                 | 70.2 ms: 1.67x faster                                                       |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.49x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 136 ms: 1.39x faster                                                        |
| regex_v8       | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                       |
| regex_dna      | 227 ms                                                 | 219 ms: 1.03x faster                                                        |
| regex_effbot   | 3.63 ms                                                | 3.80 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 298 us: 1.63x faster                                                        |
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.61x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                        |
| xml_etree_process    | 79.1 ms                                                | 57.0 ms: 1.39x faster                                                       |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 81.5 ms: 1.22x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 99.1 ms: 1.17x faster                                                       |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.13x faster                                                        |
| json_loads           | 31.2 us                                                | 27.9 us: 1.12x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.79 ms: 1.67x faster                                                       |
| django_template | 48.2 ms                                                | 35.7 ms: 1.35x faster                                                       |
| genshi_text     | 31.8 ms                                                | 26.2 ms: 1.22x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 59.3 ms: 1.11x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 172 us: 3.17x faster                                                        |
| async_tree_none          | 728 ms                                                 | 325 ms: 2.24x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.59 ms: 2.21x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 412 ms: 2.11x faster                                                        |
| async_tree_io            | 1.77 sec                                               | 846 ms: 2.09x faster                                                        |
| generators               | 80.1 ms                                                | 38.6 ms: 2.07x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 28.5 us: 2.05x faster                                                       |
| chaos                    | 115 ms                                                 | 58.6 ms: 1.97x faster                                                       |
| nbody                    | 154 ms                                                 | 79.9 ms: 1.92x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 61.6 ms: 1.92x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 66.6 ms: 1.92x faster                                                       |
| richards_super           | 94.7 ms                                                | 50.2 ms: 1.89x faster                                                       |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                                        |
| asyncio_tcp              | 922 ms                                                 | 503 ms: 1.83x faster                                                        |
| richards                 | 79.3 ms                                                | 43.9 ms: 1.80x faster                                                       |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 565 ms: 1.80x faster                                                        |
| logging_silent           | 190 ns                                                 | 107 ns: 1.78x faster                                                        |
| deepcopy                 | 479 us                                                 | 275 us: 1.74x faster                                                        |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                       |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.70x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.69x faster                                                       |
| float                    | 117 ms                                                 | 70.2 ms: 1.67x faster                                                       |
| mako                     | 16.3 ms                                                | 9.79 ms: 1.67x faster                                                       |
| go                       | 240 ms                                                 | 147 ms: 1.64x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 298 us: 1.63x faster                                                        |
| pyflate                  | 716 ms                                                 | 442 ms: 1.62x faster                                                        |
| spectral_norm            | 170 ms                                                 | 105 ms: 1.62x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.61x faster                                                      |
| pylint                   | 551 ms                                                 | 342 ms: 1.61x faster                                                        |
| hexiom                   | 10.4 ms                                                | 6.55 ms: 1.59x faster                                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.53x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                        |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                                       |
| logging_simple           | 8.30 us                                                | 5.56 us: 1.49x faster                                                       |
| logging_format           | 9.09 us                                                | 6.12 us: 1.49x faster                                                       |
| tornado_http             | 136 ms                                                 | 93.3 ms: 1.46x faster                                                       |
| scimark_fft              | 466 ms                                                 | 319 ms: 1.46x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 701 ms: 1.45x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                                      |
| fannkuch                 | 532 ms                                                 | 368 ms: 1.45x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.49 ms: 1.44x faster                                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.42x faster                                                      |
| regex_compile            | 188 ms                                                 | 136 ms: 1.39x faster                                                        |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 57.0 ms: 1.39x faster                                                       |
| scimark_lu               | 176 ms                                                 | 127 ms: 1.39x faster                                                        |
| html5lib                 | 88.9 ms                                                | 65.2 ms: 1.36x faster                                                       |
| django_template          | 48.2 ms                                                | 35.7 ms: 1.35x faster                                                       |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                       |
| thrift                   | 1.07 ms                                                | 799 us: 1.34x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.33x faster                                                      |
| 2to3                     | 348 ms                                                 | 275 ms: 1.27x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 67.5 ms: 1.25x faster                                                       |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 115 ms: 1.24x faster                                                        |
| nqueens                  | 106 ms                                                 | 85.7 ms: 1.24x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 56.3 ms: 1.23x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 81.5 ms: 1.22x faster                                                       |
| genshi_text              | 31.8 ms                                                | 26.2 ms: 1.22x faster                                                       |
| dask                     | 441 ms                                                 | 363 ms: 1.21x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 832 us: 1.19x faster                                                        |
| sympy_str                | 346 ms                                                 | 296 ms: 1.17x faster                                                        |
| sympy_sum                | 196 ms                                                 | 168 ms: 1.17x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 99.1 ms: 1.17x faster                                                       |
| sympy_integrate          | 25.8 ms                                                | 22.4 ms: 1.15x faster                                                       |
| docutils                 | 3.30 sec                                               | 2.89 sec: 1.14x faster                                                      |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.13x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.13x faster                                                        |
| sympy_expand             | 566 ms                                                 | 502 ms: 1.13x faster                                                        |
| json_loads               | 31.2 us                                                | 27.9 us: 1.12x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 59.3 ms: 1.11x faster                                                       |
| json                     | 5.69 ms                                                | 5.12 ms: 1.11x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.68 sec: 1.06x faster                                                      |
| regex_dna                | 227 ms                                                 | 219 ms: 1.03x faster                                                        |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                        |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                        |
| gc_traversal             | 3.62 ms                                                | 3.73 ms: 1.03x slower                                                       |
| async_generators         | 444 ms                                                 | 459 ms: 1.03x slower                                                        |
| regex_effbot             | 3.63 ms                                                | 3.80 ms: 1.05x slower                                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.09x slower                                                       |
| telco                    | 7.27 ms                                                | 8.01 ms: 1.10x slower                                                       |
| coverage                 | 79.4 ms                                                | 93.0 ms: 1.17x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240713-3.14.0a0-6125ff0-JIT/bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6125ff0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.19x