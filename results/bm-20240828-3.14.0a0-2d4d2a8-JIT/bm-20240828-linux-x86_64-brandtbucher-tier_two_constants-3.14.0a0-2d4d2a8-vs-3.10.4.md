# Results vs. 3.10.4

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: 2d4d2a8
- commit date: 2024-08-28
- overall geometric mean: 1.429x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 277 ms: 1.26x faster                                                      |
| docutils       | 3.30 sec                                               | 3.04 sec: 1.08x faster                                                    |
| html5lib       | 88.9 ms                                                | 64.2 ms: 1.38x faster                                                     |
| tornado_http   | 136 ms                                                 | 94.4 ms: 1.44x faster                                                     |
| Geometric mean | (ref)                                                  | 1.29x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 328 ms: 2.22x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 417 ms: 2.09x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 938 ms: 1.89x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 560 ms: 1.81x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.00x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.6 ms: 1.93x faster                                                     |
| float          | 117 ms                                                 | 70.8 ms: 1.65x faster                                                     |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.49x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 141 ms: 1.34x faster                                                      |
| regex_v8       | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                     |
| regex_dna      | 227 ms                                                 | 213 ms: 1.06x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.56 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.13x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 302 us: 1.60x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 54.5 ms: 1.45x faster                                                     |
| json_dumps           | 14.2 ms                                                | 9.96 ms: 1.42x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 77.6 ms: 1.28x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 98.6 ms: 1.17x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                      |
| json_loads           | 31.2 us                                                | 28.8 us: 1.08x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.17 ms: 1.21x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.67 ms: 1.69x faster                                                     |
| genshi_text     | 31.8 ms                                                | 24.1 ms: 1.32x faster                                                     |
| django_template | 48.2 ms                                                | 36.7 ms: 1.31x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 56.7 ms: 1.17x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.36x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.32x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.22 ms: 2.46x faster                                                     |
| generators               | 80.1 ms                                                | 32.6 ms: 2.45x faster                                                     |
| async_tree_none          | 728 ms                                                 | 328 ms: 2.22x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 26.9 us: 2.18x faster                                                     |
| richards_super           | 94.7 ms                                                | 45.0 ms: 2.10x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 417 ms: 2.09x faster                                                      |
| richards                 | 79.3 ms                                                | 39.3 ms: 2.02x faster                                                     |
| chaos                    | 115 ms                                                 | 58.5 ms: 1.97x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 65.6 ms: 1.95x faster                                                     |
| nbody                    | 154 ms                                                 | 79.6 ms: 1.93x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 938 ms: 1.89x faster                                                      |
| asyncio_tcp              | 922 ms                                                 | 492 ms: 1.87x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 63.2 ms: 1.87x faster                                                     |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                                      |
| deepcopy                 | 479 us                                                 | 261 us: 1.84x faster                                                      |
| raytrace                 | 507 ms                                                 | 277 ms: 1.83x faster                                                      |
| logging_silent           | 190 ns                                                 | 104 ns: 1.82x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 560 ms: 1.81x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                     |
| spectral_norm            | 170 ms                                                 | 98.5 ms: 1.72x faster                                                     |
| mako                     | 16.3 ms                                                | 9.67 ms: 1.69x faster                                                     |
| float                    | 117 ms                                                 | 70.8 ms: 1.65x faster                                                     |
| pyflate                  | 716 ms                                                 | 435 ms: 1.65x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                    |
| sqlglot_parse            | 2.17 ms                                                | 1.35 ms: 1.61x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.60x faster                                                      |
| scimark_lu               | 176 ms                                                 | 110 ms: 1.59x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.63 us: 1.58x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.69 ms: 1.52x faster                                                     |
| scimark_fft              | 466 ms                                                 | 307 ms: 1.52x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.86 ms: 1.52x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.30 ms: 1.51x faster                                                     |
| coroutines               | 35.1 ms                                                | 23.6 ms: 1.49x faster                                                     |
| pylint                   | 551 ms                                                 | 372 ms: 1.48x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.61 us: 1.48x faster                                                     |
| logging_format           | 9.09 us                                                | 6.21 us: 1.46x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 54.5 ms: 1.45x faster                                                     |
| tornado_http             | 136 ms                                                 | 94.4 ms: 1.44x faster                                                     |
| fannkuch                 | 532 ms                                                 | 370 ms: 1.44x faster                                                      |
| json_dumps               | 14.2 ms                                                | 9.96 ms: 1.42x faster                                                     |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                    |
| go                       | 240 ms                                                 | 170 ms: 1.41x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 730 ms: 1.39x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                                    |
| html5lib                 | 88.9 ms                                                | 64.2 ms: 1.38x faster                                                     |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                     |
| regex_compile            | 188 ms                                                 | 141 ms: 1.34x faster                                                      |
| thrift                   | 1.07 ms                                                | 803 us: 1.33x faster                                                      |
| genshi_text              | 31.8 ms                                                | 24.1 ms: 1.32x faster                                                     |
| django_template          | 48.2 ms                                                | 36.7 ms: 1.31x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                                    |
| pathlib                  | 20.5 ms                                                | 15.8 ms: 1.29x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 77.6 ms: 1.28x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.27x faster                                                      |
| 2to3                     | 348 ms                                                 | 277 ms: 1.26x faster                                                      |
| nqueens                  | 106 ms                                                 | 84.3 ms: 1.26x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 816 us: 1.21x faster                                                      |
| sqlglot_optimize         | 69.2 ms                                                | 58.1 ms: 1.19x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 98.6 ms: 1.17x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 56.7 ms: 1.17x faster                                                     |
| sympy_str                | 346 ms                                                 | 299 ms: 1.16x faster                                                      |
| sympy_sum                | 196 ms                                                 | 171 ms: 1.15x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 22.8 ms: 1.13x faster                                                     |
| sympy_expand             | 566 ms                                                 | 504 ms: 1.12x faster                                                      |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.56 sec: 1.11x faster                                                    |
| docutils                 | 3.30 sec                                               | 3.04 sec: 1.08x faster                                                    |
| json_loads               | 31.2 us                                                | 28.8 us: 1.08x faster                                                     |
| regex_dna                | 227 ms                                                 | 213 ms: 1.06x faster                                                      |
| json                     | 5.69 ms                                                | 5.38 ms: 1.06x faster                                                     |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| regex_effbot             | 3.63 ms                                                | 3.56 ms: 1.02x faster                                                     |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                      |
| gc_traversal             | 3.62 ms                                                | 3.67 ms: 1.01x slower                                                     |
| async_generators         | 444 ms                                                 | 459 ms: 1.03x slower                                                      |
| telco                    | 7.27 ms                                                | 7.62 ms: 1.05x slower                                                     |
| coverage                 | 79.4 ms                                                | 87.1 ms: 1.10x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 1.79 ms: 1.11x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.17 ms: 1.21x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240828-3.14.0a0-2d4d2a8-JIT/bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.429x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.22x