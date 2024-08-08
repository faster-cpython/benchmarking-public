# Results vs. 3.10.4

- fork: brandtbucher
- ref: tier_two_constants_i
- machine: linux-x86_64
- commit hash: 8756bc0
- commit date: 2024-08-07
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 274 ms: 1.27x faster                                                        |
| docutils       | 3.30 sec                                               | 2.90 sec: 1.14x faster                                                      |
| html5lib       | 88.9 ms                                                | 65.9 ms: 1.35x faster                                                       |
| tornado_http   | 136 ms                                                 | 92.6 ms: 1.47x faster                                                       |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.23x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 418 ms: 2.08x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 904 ms: 1.96x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 562 ms: 1.81x faster                                                        |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.0 ms: 1.94x faster                                                       |
| float          | 117 ms                                                 | 70.6 ms: 1.66x faster                                                       |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.49x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 134 ms: 1.41x faster                                                        |
| regex_v8       | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                       |
| regex_dna      | 227 ms                                                 | 224 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 295 us: 1.64x faster                                                        |
| tomli_loads          | 3.14 sec                                               | 1.92 sec: 1.64x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.54x faster                                                        |
| xml_etree_process    | 79.1 ms                                                | 56.3 ms: 1.41x faster                                                       |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 79.7 ms: 1.25x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 99.0 ms: 1.17x faster                                                       |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.14x faster                                                        |
| json_loads           | 31.2 us                                                | 28.8 us: 1.08x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 7.15 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.71 ms: 1.68x faster                                                       |
| django_template | 48.2 ms                                                | 35.9 ms: 1.34x faster                                                       |
| genshi_text     | 31.8 ms                                                | 24.0 ms: 1.33x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 53.2 ms: 1.24x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.20x faster                                                        |
| generators               | 80.1 ms                                                | 32.6 ms: 2.46x faster                                                       |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.23x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.54 ms: 2.23x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 418 ms: 2.08x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 28.8 us: 2.03x faster                                                       |
| richards_super           | 94.7 ms                                                | 47.2 ms: 2.01x faster                                                       |
| chaos                    | 115 ms                                                 | 58.1 ms: 1.99x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 904 ms: 1.96x faster                                                        |
| nbody                    | 154 ms                                                 | 79.0 ms: 1.94x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 66.2 ms: 1.93x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 61.4 ms: 1.93x faster                                                       |
| richards                 | 79.3 ms                                                | 41.2 ms: 1.92x faster                                                       |
| scimark_sor              | 220 ms                                                 | 115 ms: 1.91x faster                                                        |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                                        |
| asyncio_tcp              | 922 ms                                                 | 499 ms: 1.85x faster                                                        |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 562 ms: 1.81x faster                                                        |
| comprehensions           | 28.8 us                                                | 16.2 us: 1.77x faster                                                       |
| deepcopy                 | 479 us                                                 | 271 us: 1.77x faster                                                        |
| mako                     | 16.3 ms                                                | 9.71 ms: 1.68x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.67x faster                                                       |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.66x faster                                                        |
| float                    | 117 ms                                                 | 70.6 ms: 1.66x faster                                                       |
| pyflate                  | 716 ms                                                 | 435 ms: 1.64x faster                                                        |
| go                       | 240 ms                                                 | 146 ms: 1.64x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 295 us: 1.64x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.92 sec: 1.64x faster                                                      |
| scimark_lu               | 176 ms                                                 | 108 ms: 1.62x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                                       |
| hexiom                   | 10.4 ms                                                | 6.66 ms: 1.56x faster                                                       |
| pylint                   | 551 ms                                                 | 355 ms: 1.55x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.54x faster                                                        |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.76 us: 1.51x faster                                                       |
| scimark_fft              | 466 ms                                                 | 310 ms: 1.50x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.55 us: 1.50x faster                                                       |
| logging_format           | 9.09 us                                                | 6.13 us: 1.48x faster                                                       |
| tornado_http             | 136 ms                                                 | 92.6 ms: 1.47x faster                                                       |
| fannkuch                 | 532 ms                                                 | 371 ms: 1.43x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.54 ms: 1.42x faster                                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                      |
| regex_compile            | 188 ms                                                 | 134 ms: 1.41x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 56.3 ms: 1.41x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 729 ms: 1.40x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                                      |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                       |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                       |
| thrift                   | 1.07 ms                                                | 787 us: 1.36x faster                                                        |
| html5lib                 | 88.9 ms                                                | 65.9 ms: 1.35x faster                                                       |
| django_template          | 48.2 ms                                                | 35.9 ms: 1.34x faster                                                       |
| genshi_text              | 31.8 ms                                                | 24.0 ms: 1.33x faster                                                       |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                       |
| 2to3                     | 348 ms                                                 | 274 ms: 1.27x faster                                                        |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.27x faster                                                        |
| nqueens                  | 106 ms                                                 | 83.9 ms: 1.26x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 79.7 ms: 1.25x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 55.6 ms: 1.24x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 53.2 ms: 1.24x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 819 us: 1.20x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 99.0 ms: 1.17x faster                                                       |
| sympy_sum                | 196 ms                                                 | 170 ms: 1.16x faster                                                        |
| sympy_str                | 346 ms                                                 | 299 ms: 1.15x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 22.5 ms: 1.15x faster                                                       |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.14x faster                                                        |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.90 sec: 1.14x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                       |
| json                     | 5.69 ms                                                | 5.12 ms: 1.11x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.56 sec: 1.11x faster                                                      |
| sympy_expand             | 566 ms                                                 | 510 ms: 1.11x faster                                                        |
| json_loads               | 31.2 us                                                | 28.8 us: 1.08x faster                                                       |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                        |
| regex_dna                | 227 ms                                                 | 224 ms: 1.01x faster                                                        |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                        |
| gc_traversal             | 3.62 ms                                                | 3.67 ms: 1.01x slower                                                       |
| async_generators         | 444 ms                                                 | 456 ms: 1.03x slower                                                        |
| telco                    | 7.27 ms                                                | 7.80 ms: 1.07x slower                                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.09x slower                                                       |
| coverage                 | 79.4 ms                                                | 92.0 ms: 1.16x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.15 ms: 1.21x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                                |

Benchmark hidden because not significant (2): regex_effbot, bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240807-3.14.0a0-8756bc0-JIT/bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.20x