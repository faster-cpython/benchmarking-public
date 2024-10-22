# Results vs. 3.10.4

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: f135fa1
- commit date: 2024-08-06
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 274 ms: 1.27x faster                                                      |
| docutils       | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                    |
| html5lib       | 88.9 ms                                                | 65.8 ms: 1.35x faster                                                     |
| tornado_http   | 136 ms                                                 | 92.7 ms: 1.47x faster                                                     |
| Geometric mean | (ref)                                                  | 1.30x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 328 ms: 2.22x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 428 ms: 2.03x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 917 ms: 1.93x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 564 ms: 1.80x faster                                                      |
| Geometric mean          | (ref)                                                  | 1.99x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.2 ms: 1.94x faster                                                     |
| float          | 117 ms                                                 | 71.6 ms: 1.64x faster                                                     |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.48x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 135 ms: 1.40x faster                                                      |
| regex_v8       | 27.8 ms                                                | 23.7 ms: 1.17x faster                                                     |
| regex_dna      | 227 ms                                                 | 215 ms: 1.05x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.57 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.15x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 297 us: 1.63x faster                                                      |
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.53x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 56.6 ms: 1.40x faster                                                     |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 79.9 ms: 1.24x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 99.4 ms: 1.16x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                                      |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.20 ms: 1.21x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.87 ms: 1.65x faster                                                     |
| django_template | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                     |
| genshi_text     | 31.8 ms                                                | 24.0 ms: 1.33x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 53.6 ms: 1.23x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 173 us: 3.15x faster                                                      |
| generators               | 80.1 ms                                                | 32.9 ms: 2.43x faster                                                     |
| async_tree_none          | 728 ms                                                 | 328 ms: 2.22x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.60 ms: 2.20x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 428 ms: 2.03x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 29.2 us: 2.00x faster                                                     |
| richards_super           | 94.7 ms                                                | 47.4 ms: 2.00x faster                                                     |
| chaos                    | 115 ms                                                 | 58.5 ms: 1.97x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 60.4 ms: 1.96x faster                                                     |
| nbody                    | 154 ms                                                 | 79.2 ms: 1.94x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 917 ms: 1.93x faster                                                      |
| richards                 | 79.3 ms                                                | 41.7 ms: 1.90x faster                                                     |
| scimark_sor              | 220 ms                                                 | 116 ms: 1.89x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 68.0 ms: 1.88x faster                                                     |
| raytrace                 | 507 ms                                                 | 273 ms: 1.86x faster                                                      |
| asyncio_tcp              | 922 ms                                                 | 500 ms: 1.84x faster                                                      |
| logging_silent           | 190 ns                                                 | 104 ns: 1.82x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 564 ms: 1.80x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.76x faster                                                     |
| deepcopy                 | 479 us                                                 | 275 us: 1.74x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                                     |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.66x faster                                                      |
| go                       | 240 ms                                                 | 145 ms: 1.66x faster                                                      |
| mako                     | 16.3 ms                                                | 9.87 ms: 1.65x faster                                                     |
| pyflate                  | 716 ms                                                 | 435 ms: 1.65x faster                                                      |
| float                    | 117 ms                                                 | 71.6 ms: 1.64x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 297 us: 1.63x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                    |
| scimark_lu               | 176 ms                                                 | 108 ms: 1.62x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.58x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.71 ms: 1.55x faster                                                     |
| pylint                   | 551 ms                                                 | 357 ms: 1.54x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.53x faster                                                      |
| scimark_fft              | 466 ms                                                 | 304 ms: 1.53x faster                                                      |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.57 us: 1.49x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.80 us: 1.49x faster                                                     |
| logging_format           | 9.09 us                                                | 6.11 us: 1.49x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.36 ms: 1.48x faster                                                     |
| tornado_http             | 136 ms                                                 | 92.7 ms: 1.47x faster                                                     |
| fannkuch                 | 532 ms                                                 | 365 ms: 1.46x faster                                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.40x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                    |
| regex_compile            | 188 ms                                                 | 135 ms: 1.40x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 56.6 ms: 1.40x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 737 ms: 1.38x faster                                                      |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                     |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                     |
| html5lib                 | 88.9 ms                                                | 65.8 ms: 1.35x faster                                                     |
| thrift                   | 1.07 ms                                                | 803 us: 1.33x faster                                                      |
| django_template          | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                     |
| genshi_text              | 31.8 ms                                                | 24.0 ms: 1.33x faster                                                     |
| 2to3                     | 348 ms                                                 | 274 ms: 1.27x faster                                                      |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.26x faster                                                      |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.26x faster                                                     |
| nqueens                  | 106 ms                                                 | 84.9 ms: 1.25x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 79.9 ms: 1.24x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 53.6 ms: 1.23x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 56.4 ms: 1.23x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 823 us: 1.20x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 23.7 ms: 1.17x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 99.4 ms: 1.16x faster                                                     |
| sympy_sum                | 196 ms                                                 | 171 ms: 1.15x faster                                                      |
| sympy_str                | 346 ms                                                 | 302 ms: 1.14x faster                                                      |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 22.7 ms: 1.14x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                    |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.57 sec: 1.11x faster                                                    |
| json                     | 5.69 ms                                                | 5.16 ms: 1.10x faster                                                     |
| sympy_expand             | 566 ms                                                 | 515 ms: 1.10x faster                                                      |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                     |
| regex_dna                | 227 ms                                                 | 215 ms: 1.05x faster                                                      |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                      |
| regex_effbot             | 3.63 ms                                                | 3.57 ms: 1.02x faster                                                     |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.01x faster                                                      |
| gc_traversal             | 3.62 ms                                                | 3.61 ms: 1.00x faster                                                     |
| async_generators         | 444 ms                                                 | 469 ms: 1.06x slower                                                      |
| telco                    | 7.27 ms                                                | 7.91 ms: 1.09x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                                     |
| coverage                 | 79.4 ms                                                | 91.6 ms: 1.15x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.20 ms: 1.21x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240806-3.14.0a0-f135fa1-JIT/bm-20240806-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-f135fa1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.20x