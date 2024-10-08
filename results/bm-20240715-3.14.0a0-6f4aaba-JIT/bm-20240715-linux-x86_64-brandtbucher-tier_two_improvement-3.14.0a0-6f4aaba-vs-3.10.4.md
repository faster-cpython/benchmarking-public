# Results vs. 3.10.4

- fork: brandtbucher
- ref: tier_two_improvement
- machine: linux-x86_64
- commit hash: 6f4aaba
- commit date: 2024-07-15
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 272 ms: 1.28x faster                                                        |
| docutils       | 3.30 sec                                               | 2.88 sec: 1.14x faster                                                      |
| html5lib       | 88.9 ms                                                | 63.2 ms: 1.41x faster                                                       |
| tornado_http   | 136 ms                                                 | 93.5 ms: 1.46x faster                                                       |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 327 ms: 2.23x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 408 ms: 2.13x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 845 ms: 2.09x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 571 ms: 1.78x faster                                                        |
| Geometric mean          | (ref)                                                  | 2.05x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.2 ms: 1.89x faster                                                       |
| float          | 117 ms                                                 | 70.4 ms: 1.66x faster                                                       |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.48x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 134 ms: 1.40x faster                                                        |
| regex_v8       | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                       |
| regex_dna      | 227 ms                                                 | 229 ms: 1.01x slower                                                        |
| regex_effbot   | 3.63 ms                                                | 3.81 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.91 sec: 1.65x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 298 us: 1.63x faster                                                        |
| unpickle_pure_python | 331 us                                                 | 226 us: 1.46x faster                                                        |
| xml_etree_process    | 79.1 ms                                                | 56.9 ms: 1.39x faster                                                       |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 81.0 ms: 1.23x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 98.9 ms: 1.17x faster                                                       |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.14x faster                                                        |
| json_loads           | 31.2 us                                                | 27.9 us: 1.12x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 7.13 ms: 1.20x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.74 ms: 1.68x faster                                                       |
| django_template | 48.2 ms                                                | 35.8 ms: 1.34x faster                                                       |
| genshi_text     | 31.8 ms                                                | 25.8 ms: 1.24x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 57.4 ms: 1.15x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 172 us: 3.17x faster                                                        |
| generators               | 80.1 ms                                                | 29.9 ms: 2.68x faster                                                       |
| async_tree_none          | 728 ms                                                 | 327 ms: 2.23x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.65 ms: 2.17x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 408 ms: 2.13x faster                                                        |
| async_tree_io            | 1.77 sec                                               | 845 ms: 2.09x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 28.8 us: 2.03x faster                                                       |
| richards_super           | 94.7 ms                                                | 47.3 ms: 2.00x faster                                                       |
| chaos                    | 115 ms                                                 | 58.3 ms: 1.98x faster                                                       |
| richards                 | 79.3 ms                                                | 41.1 ms: 1.93x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 61.3 ms: 1.93x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 67.0 ms: 1.91x faster                                                       |
| nbody                    | 154 ms                                                 | 81.2 ms: 1.89x faster                                                       |
| raytrace                 | 507 ms                                                 | 269 ms: 1.88x faster                                                        |
| asyncio_tcp              | 922 ms                                                 | 509 ms: 1.81x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 571 ms: 1.78x faster                                                        |
| logging_silent           | 190 ns                                                 | 108 ns: 1.76x faster                                                        |
| deepcopy                 | 479 us                                                 | 274 us: 1.75x faster                                                        |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                                       |
| mako                     | 16.3 ms                                                | 9.74 ms: 1.68x faster                                                       |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.68x faster                                                        |
| scimark_sor              | 220 ms                                                 | 131 ms: 1.67x faster                                                        |
| float                    | 117 ms                                                 | 70.4 ms: 1.66x faster                                                       |
| pyflate                  | 716 ms                                                 | 433 ms: 1.66x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.91 sec: 1.65x faster                                                      |
| go                       | 240 ms                                                 | 146 ms: 1.64x faster                                                        |
| pylint                   | 551 ms                                                 | 336 ms: 1.64x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 298 us: 1.63x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.61 ms: 1.60x faster                                                       |
| coroutines               | 35.1 ms                                                | 22.2 ms: 1.58x faster                                                       |
| hexiom                   | 10.4 ms                                                | 6.59 ms: 1.58x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.75 us: 1.52x faster                                                       |
| logging_simple           | 8.30 us                                                | 5.53 us: 1.50x faster                                                       |
| scimark_fft              | 466 ms                                                 | 310 ms: 1.50x faster                                                        |
| logging_format           | 9.09 us                                                | 6.15 us: 1.48x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 694 ms: 1.47x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 226 us: 1.46x faster                                                        |
| tornado_http             | 136 ms                                                 | 93.5 ms: 1.46x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.44 ms: 1.46x faster                                                       |
| fannkuch                 | 532 ms                                                 | 367 ms: 1.45x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                      |
| html5lib                 | 88.9 ms                                                | 63.2 ms: 1.41x faster                                                       |
| regex_compile            | 188 ms                                                 | 134 ms: 1.40x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 56.9 ms: 1.39x faster                                                       |
| scimark_lu               | 176 ms                                                 | 127 ms: 1.38x faster                                                        |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                       |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                       |
| django_template          | 48.2 ms                                                | 35.8 ms: 1.34x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                                      |
| thrift                   | 1.07 ms                                                | 808 us: 1.33x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                       |
| 2to3                     | 348 ms                                                 | 272 ms: 1.28x faster                                                        |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.27x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 67.5 ms: 1.25x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 56.0 ms: 1.24x faster                                                       |
| genshi_text              | 31.8 ms                                                | 25.8 ms: 1.24x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 81.0 ms: 1.23x faster                                                       |
| nqueens                  | 106 ms                                                 | 86.5 ms: 1.22x faster                                                       |
| dask                     | 441 ms                                                 | 364 ms: 1.21x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 834 us: 1.18x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 98.9 ms: 1.17x faster                                                       |
| sympy_sum                | 196 ms                                                 | 169 ms: 1.16x faster                                                        |
| sympy_str                | 346 ms                                                 | 298 ms: 1.16x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 22.3 ms: 1.16x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 57.4 ms: 1.15x faster                                                       |
| docutils                 | 3.30 sec                                               | 2.88 sec: 1.14x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.14x faster                                                        |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                        |
| mdp                      | 2.85 sec                                               | 2.53 sec: 1.12x faster                                                      |
| sympy_expand             | 566 ms                                                 | 503 ms: 1.12x faster                                                        |
| json_loads               | 31.2 us                                                | 27.9 us: 1.12x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                       |
| json                     | 5.69 ms                                                | 5.21 ms: 1.09x faster                                                       |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                        |
| gc_traversal             | 3.62 ms                                                | 3.58 ms: 1.01x faster                                                       |
| regex_dna                | 227 ms                                                 | 229 ms: 1.01x slower                                                        |
| async_generators         | 444 ms                                                 | 455 ms: 1.02x slower                                                        |
| regex_effbot             | 3.63 ms                                                | 3.81 ms: 1.05x slower                                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.08x slower                                                       |
| telco                    | 7.27 ms                                                | 7.96 ms: 1.10x slower                                                       |
| coverage                 | 79.4 ms                                                | 94.5 ms: 1.19x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.13 ms: 1.20x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                                |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240715-3.14.0a0-6f4aaba-JIT/bm-20240715-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-6f4aaba.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.19x