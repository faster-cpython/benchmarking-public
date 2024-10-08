# Results vs. 3.10.4

- fork: brandtbucher
- ref: tier_two_improvement
- machine: linux-x86_64
- commit hash: bbb07e8
- commit date: 2024-07-13
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 272 ms: 1.28x faster                                                        |
| docutils       | 3.30 sec                                               | 2.87 sec: 1.15x faster                                                      |
| html5lib       | 88.9 ms                                                | 66.0 ms: 1.35x faster                                                       |
| tornado_http   | 136 ms                                                 | 93.0 ms: 1.47x faster                                                       |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 321 ms: 2.27x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 403 ms: 2.16x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 840 ms: 2.10x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 561 ms: 1.81x faster                                                        |
| Geometric mean          | (ref)                                                  | 2.08x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.2 ms: 1.94x faster                                                       |
| float          | 117 ms                                                 | 69.3 ms: 1.69x faster                                                       |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.50x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 135 ms: 1.40x faster                                                        |
| regex_v8       | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                       |
| regex_dna      | 227 ms                                                 | 229 ms: 1.01x slower                                                        |
| regex_effbot   | 3.63 ms                                                | 3.73 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 297 us: 1.63x faster                                                        |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                        |
| xml_etree_process    | 79.1 ms                                                | 57.0 ms: 1.39x faster                                                       |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 80.6 ms: 1.23x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 99.1 ms: 1.16x faster                                                       |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.14x faster                                                        |
| json_loads           | 31.2 us                                                | 27.9 us: 1.12x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.86 ms: 1.66x faster                                                       |
| django_template | 48.2 ms                                                | 34.9 ms: 1.38x faster                                                       |
| genshi_text     | 31.8 ms                                                | 24.6 ms: 1.29x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 56.3 ms: 1.17x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.36x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.25x faster                                                        |
| generators               | 80.1 ms                                                | 30.4 ms: 2.63x faster                                                       |
| async_tree_none          | 728 ms                                                 | 321 ms: 2.27x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.54 ms: 2.24x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 403 ms: 2.16x faster                                                        |
| async_tree_io            | 1.77 sec                                               | 840 ms: 2.10x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 28.9 us: 2.02x faster                                                       |
| richards_super           | 94.7 ms                                                | 47.6 ms: 1.99x faster                                                       |
| chaos                    | 115 ms                                                 | 58.1 ms: 1.99x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 60.9 ms: 1.94x faster                                                       |
| nbody                    | 154 ms                                                 | 79.2 ms: 1.94x faster                                                       |
| richards                 | 79.3 ms                                                | 41.3 ms: 1.92x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 67.5 ms: 1.89x faster                                                       |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                                        |
| asyncio_tcp              | 922 ms                                                 | 502 ms: 1.84x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 561 ms: 1.81x faster                                                        |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                                        |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.74x faster                                                       |
| deepcopy                 | 479 us                                                 | 278 us: 1.72x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.70x faster                                                       |
| scimark_sor              | 220 ms                                                 | 130 ms: 1.69x faster                                                        |
| float                    | 117 ms                                                 | 69.3 ms: 1.69x faster                                                       |
| pyflate                  | 716 ms                                                 | 426 ms: 1.68x faster                                                        |
| go                       | 240 ms                                                 | 144 ms: 1.67x faster                                                        |
| mako                     | 16.3 ms                                                | 9.86 ms: 1.66x faster                                                       |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.65x faster                                                        |
| pylint                   | 551 ms                                                 | 335 ms: 1.65x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 297 us: 1.63x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.61 ms: 1.60x faster                                                       |
| hexiom                   | 10.4 ms                                                | 6.58 ms: 1.58x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.49 us: 1.51x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.78 us: 1.50x faster                                                       |
| logging_format           | 9.09 us                                                | 6.07 us: 1.50x faster                                                       |
| coroutines               | 35.1 ms                                                | 23.5 ms: 1.49x faster                                                       |
| scimark_fft              | 466 ms                                                 | 315 ms: 1.48x faster                                                        |
| tornado_http             | 136 ms                                                 | 93.0 ms: 1.47x faster                                                       |
| fannkuch                 | 532 ms                                                 | 363 ms: 1.46x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.50 ms: 1.44x faster                                                       |
| scimark_lu               | 176 ms                                                 | 123 ms: 1.43x faster                                                        |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 720 ms: 1.41x faster                                                        |
| regex_compile            | 188 ms                                                 | 135 ms: 1.40x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                                      |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 57.0 ms: 1.39x faster                                                       |
| django_template          | 48.2 ms                                                | 34.9 ms: 1.38x faster                                                       |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                       |
| html5lib                 | 88.9 ms                                                | 66.0 ms: 1.35x faster                                                       |
| thrift                   | 1.07 ms                                                | 800 us: 1.34x faster                                                        |
| genshi_text              | 31.8 ms                                                | 24.6 ms: 1.29x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 111 ms: 1.29x faster                                                        |
| 2to3                     | 348 ms                                                 | 272 ms: 1.28x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                       |
| dulwich_log              | 84.3 ms                                                | 67.2 ms: 1.26x faster                                                       |
| nqueens                  | 106 ms                                                 | 84.3 ms: 1.25x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 55.3 ms: 1.25x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 80.6 ms: 1.23x faster                                                       |
| dask                     | 441 ms                                                 | 364 ms: 1.21x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 834 us: 1.18x faster                                                        |
| sympy_str                | 346 ms                                                 | 294 ms: 1.18x faster                                                        |
| sympy_sum                | 196 ms                                                 | 167 ms: 1.17x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 56.3 ms: 1.17x faster                                                       |
| sympy_integrate          | 25.8 ms                                                | 22.1 ms: 1.17x faster                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 99.1 ms: 1.16x faster                                                       |
| docutils                 | 3.30 sec                                               | 2.87 sec: 1.15x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.14x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                       |
| sympy_expand             | 566 ms                                                 | 497 ms: 1.14x faster                                                        |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                        |
| json_loads               | 31.2 us                                                | 27.9 us: 1.12x faster                                                       |
| json                     | 5.69 ms                                                | 5.15 ms: 1.10x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.74 sec: 1.04x faster                                                      |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                        |
| gc_traversal             | 3.62 ms                                                | 3.55 ms: 1.02x faster                                                       |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                        |
| async_generators         | 444 ms                                                 | 449 ms: 1.01x slower                                                        |
| regex_dna                | 227 ms                                                 | 229 ms: 1.01x slower                                                        |
| regex_effbot             | 3.63 ms                                                | 3.73 ms: 1.03x slower                                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                       |
| telco                    | 7.27 ms                                                | 8.04 ms: 1.11x slower                                                       |
| coverage                 | 79.4 ms                                                | 93.4 ms: 1.18x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240713-3.14.0a0-bbb07e8-JIT/bm-20240713-linux-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.18x