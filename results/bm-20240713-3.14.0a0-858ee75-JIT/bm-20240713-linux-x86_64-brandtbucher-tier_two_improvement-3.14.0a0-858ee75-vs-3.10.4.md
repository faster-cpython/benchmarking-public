# Results vs. 3.10.4

- fork: brandtbucher
- ref: tier_two_improvement
- machine: linux-x86_64
- commit hash: 858ee75
- commit date: 2024-07-13
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 273 ms: 1.28x faster                                                        |
| docutils       | 3.30 sec                                               | 2.89 sec: 1.14x faster                                                      |
| html5lib       | 88.9 ms                                                | 63.6 ms: 1.40x faster                                                       |
| tornado_http   | 136 ms                                                 | 93.0 ms: 1.47x faster                                                       |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 325 ms: 2.24x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 407 ms: 2.14x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 837 ms: 2.11x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 562 ms: 1.81x faster                                                        |
| Geometric mean          | (ref)                                                  | 2.07x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.5 ms: 1.93x faster                                                       |
| float          | 117 ms                                                 | 70.9 ms: 1.65x faster                                                       |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.49x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 134 ms: 1.41x faster                                                        |
| regex_v8       | 27.8 ms                                                | 26.3 ms: 1.06x faster                                                       |
| regex_dna      | 227 ms                                                 | 238 ms: 1.05x slower                                                        |
| regex_effbot   | 3.63 ms                                                | 4.03 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 297 us: 1.63x faster                                                        |
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                        |
| xml_etree_process    | 79.1 ms                                                | 57.3 ms: 1.38x faster                                                       |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 81.4 ms: 1.22x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 98.5 ms: 1.17x faster                                                       |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                        |
| json_loads           | 31.2 us                                                | 28.5 us: 1.10x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.4 ms: 1.40x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.73 ms: 1.68x faster                                                       |
| django_template | 48.2 ms                                                | 35.5 ms: 1.36x faster                                                       |
| genshi_text     | 31.8 ms                                                | 25.1 ms: 1.27x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 58.8 ms: 1.12x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.20x faster                                                        |
| generators               | 80.1 ms                                                | 30.2 ms: 2.66x faster                                                       |
| async_tree_none          | 728 ms                                                 | 325 ms: 2.24x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.54 ms: 2.23x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 407 ms: 2.14x faster                                                        |
| async_tree_io            | 1.77 sec                                               | 837 ms: 2.11x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 28.3 us: 2.07x faster                                                       |
| chaos                    | 115 ms                                                 | 57.9 ms: 2.00x faster                                                       |
| richards_super           | 94.7 ms                                                | 47.7 ms: 1.99x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 60.4 ms: 1.96x faster                                                       |
| nbody                    | 154 ms                                                 | 79.5 ms: 1.93x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 66.9 ms: 1.91x faster                                                       |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                                        |
| richards                 | 79.3 ms                                                | 42.0 ms: 1.89x faster                                                       |
| asyncio_tcp              | 922 ms                                                 | 503 ms: 1.83x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 562 ms: 1.81x faster                                                        |
| logging_silent           | 190 ns                                                 | 106 ns: 1.78x faster                                                        |
| deepcopy                 | 479 us                                                 | 272 us: 1.76x faster                                                        |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.70x faster                                                       |
| scimark_sor              | 220 ms                                                 | 131 ms: 1.68x faster                                                        |
| mako                     | 16.3 ms                                                | 9.73 ms: 1.68x faster                                                       |
| go                       | 240 ms                                                 | 144 ms: 1.67x faster                                                        |
| float                    | 117 ms                                                 | 70.9 ms: 1.65x faster                                                       |
| pylint                   | 551 ms                                                 | 335 ms: 1.64x faster                                                        |
| pyflate                  | 716 ms                                                 | 439 ms: 1.63x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 297 us: 1.63x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                      |
| spectral_norm            | 170 ms                                                 | 105 ms: 1.62x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.61 ms: 1.60x faster                                                       |
| hexiom                   | 10.4 ms                                                | 6.54 ms: 1.59x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.43 us: 1.53x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                                       |
| logging_format           | 9.09 us                                                | 6.08 us: 1.50x faster                                                       |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                                        |
| coroutines               | 35.1 ms                                                | 23.7 ms: 1.48x faster                                                       |
| tornado_http             | 136 ms                                                 | 93.0 ms: 1.47x faster                                                       |
| fannkuch                 | 532 ms                                                 | 366 ms: 1.45x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 713 ms: 1.43x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.54 ms: 1.42x faster                                                       |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                      |
| regex_compile            | 188 ms                                                 | 134 ms: 1.41x faster                                                        |
| html5lib                 | 88.9 ms                                                | 63.6 ms: 1.40x faster                                                       |
| python_startup           | 14.6 ms                                                | 10.4 ms: 1.40x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 57.3 ms: 1.38x faster                                                       |
| scimark_lu               | 176 ms                                                 | 129 ms: 1.37x faster                                                        |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                       |
| django_template          | 48.2 ms                                                | 35.5 ms: 1.36x faster                                                       |
| thrift                   | 1.07 ms                                                | 793 us: 1.35x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.32x faster                                                      |
| sqlglot_normalize        | 143 ms                                                 | 111 ms: 1.28x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                       |
| 2to3                     | 348 ms                                                 | 273 ms: 1.28x faster                                                        |
| genshi_text              | 31.8 ms                                                | 25.1 ms: 1.27x faster                                                       |
| dulwich_log              | 84.3 ms                                                | 67.3 ms: 1.25x faster                                                       |
| nqueens                  | 106 ms                                                 | 85.2 ms: 1.24x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 55.7 ms: 1.24x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 81.4 ms: 1.22x faster                                                       |
| dask                     | 441 ms                                                 | 362 ms: 1.22x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 833 us: 1.18x faster                                                        |
| sympy_sum                | 196 ms                                                 | 167 ms: 1.18x faster                                                        |
| sympy_str                | 346 ms                                                 | 294 ms: 1.18x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 98.5 ms: 1.17x faster                                                       |
| sympy_integrate          | 25.8 ms                                                | 22.1 ms: 1.17x faster                                                       |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                        |
| sympy_expand             | 566 ms                                                 | 495 ms: 1.14x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.89 sec: 1.14x faster                                                      |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 58.8 ms: 1.12x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.53 sec: 1.12x faster                                                      |
| json                     | 5.69 ms                                                | 5.12 ms: 1.11x faster                                                       |
| json_loads               | 31.2 us                                                | 28.5 us: 1.10x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 26.3 ms: 1.06x faster                                                       |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                        |
| gc_traversal             | 3.62 ms                                                | 3.55 ms: 1.02x faster                                                       |
| async_generators         | 444 ms                                                 | 451 ms: 1.02x slower                                                        |
| regex_dna                | 227 ms                                                 | 238 ms: 1.05x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.07x slower                                                       |
| regex_effbot             | 3.63 ms                                                | 4.03 ms: 1.11x slower                                                       |
| telco                    | 7.27 ms                                                | 8.08 ms: 1.11x slower                                                       |
| coverage                 | 79.4 ms                                                | 93.9 ms: 1.18x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                                |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240713-3.14.0a0-858ee75-JIT/bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-858ee75.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.19x