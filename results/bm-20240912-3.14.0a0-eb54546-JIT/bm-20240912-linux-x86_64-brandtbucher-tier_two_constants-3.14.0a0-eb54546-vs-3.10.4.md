# Results vs. 3.10.4

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: eb54546
- commit date: 2024-09-12
- overall geometric mean: 1.38x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 276 ms: 1.26x faster                                                      |
| docutils       | 3.30 sec                                               | 2.95 sec: 1.12x faster                                                    |
| html5lib       | 88.9 ms                                                | 64.5 ms: 1.38x faster                                                     |
| tornado_http   | 136 ms                                                 | 94.4 ms: 1.44x faster                                                     |
| Geometric mean | (ref)                                                  | 1.29x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 316 ms: 2.31x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 394 ms: 2.21x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 887 ms: 1.99x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 569 ms: 1.78x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.06x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.9 ms: 1.90x faster                                                     |
| float          | 117 ms                                                 | 69.9 ms: 1.68x faster                                                     |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.48x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 140 ms: 1.35x faster                                                      |
| regex_v8       | 27.8 ms                                                | 24.1 ms: 1.15x faster                                                     |
| regex_dna      | 227 ms                                                 | 224 ms: 1.01x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.86 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                  | 1.10x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.91 sec: 1.65x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 306 us: 1.58x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 54.4 ms: 1.46x faster                                                     |
| json_dumps           | 14.2 ms                                                | 9.96 ms: 1.42x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 77.0 ms: 1.29x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 99.1 ms: 1.17x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                      |
| json_loads           | 31.2 us                                                | 27.1 us: 1.15x faster                                                     |
| unpickle_list        | 5.20 us                                                | 5.34 us: 1.03x slower                                                     |
| pickle               | 10.7 us                                                | 11.4 us: 1.07x slower                                                     |
| pickle_dict          | 29.6 us                                                | 33.8 us: 1.14x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                              |

Benchmark hidden because not significant (2): pickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.78 ms: 1.67x faster                                                     |
| django_template | 48.2 ms                                                | 36.0 ms: 1.34x faster                                                     |
| genshi_text     | 31.8 ms                                                | 24.3 ms: 1.31x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 56.8 ms: 1.16x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.36x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.37x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.20 ms: 2.48x faster                                                     |
| generators               | 80.1 ms                                                | 32.9 ms: 2.44x faster                                                     |
| async_tree_none          | 728 ms                                                 | 316 ms: 2.31x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 394 ms: 2.21x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 26.9 us: 2.17x faster                                                     |
| richards_super           | 94.7 ms                                                | 45.1 ms: 2.10x faster                                                     |
| richards                 | 79.3 ms                                                | 39.7 ms: 2.00x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 887 ms: 1.99x faster                                                      |
| chaos                    | 115 ms                                                 | 58.8 ms: 1.96x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 66.2 ms: 1.93x faster                                                     |
| scimark_sor              | 220 ms                                                 | 116 ms: 1.90x faster                                                      |
| nbody                    | 154 ms                                                 | 80.9 ms: 1.90x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 63.2 ms: 1.87x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 496 ms: 1.86x faster                                                      |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                      |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                                      |
| raytrace                 | 507 ms                                                 | 277 ms: 1.83x faster                                                      |
| go                       | 240 ms                                                 | 132 ms: 1.82x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 569 ms: 1.78x faster                                                      |
| spectral_norm            | 170 ms                                                 | 97.4 ms: 1.74x faster                                                     |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                     |
| float                    | 117 ms                                                 | 69.9 ms: 1.68x faster                                                     |
| mako                     | 16.3 ms                                                | 9.78 ms: 1.67x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.91 sec: 1.65x faster                                                    |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                                     |
| pyflate                  | 716 ms                                                 | 449 ms: 1.60x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 306 us: 1.58x faster                                                      |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.67 ms: 1.54x faster                                                     |
| coroutines               | 35.1 ms                                                | 22.8 ms: 1.54x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.78 ms: 1.53x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                      |
| scimark_fft              | 466 ms                                                 | 311 ms: 1.50x faster                                                      |
| logging_format           | 9.09 us                                                | 6.12 us: 1.49x faster                                                     |
| pylint                   | 551 ms                                                 | 372 ms: 1.48x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.61 us: 1.48x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 54.4 ms: 1.46x faster                                                     |
| tornado_http             | 136 ms                                                 | 94.4 ms: 1.44x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.49 ms: 1.44x faster                                                     |
| fannkuch                 | 532 ms                                                 | 373 ms: 1.43x faster                                                      |
| json_dumps               | 14.2 ms                                                | 9.96 ms: 1.42x faster                                                     |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                    |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                     |
| html5lib                 | 88.9 ms                                                | 64.5 ms: 1.38x faster                                                     |
| thrift                   | 1.07 ms                                                | 784 us: 1.37x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.55 sec: 1.36x faster                                                    |
| regex_compile            | 188 ms                                                 | 140 ms: 1.35x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 757 ms: 1.35x faster                                                      |
| django_template          | 48.2 ms                                                | 36.0 ms: 1.34x faster                                                     |
| genshi_text              | 31.8 ms                                                | 24.3 ms: 1.31x faster                                                     |
| pathlib                  | 20.5 ms                                                | 15.8 ms: 1.29x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 77.0 ms: 1.29x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.28x faster                                                      |
| 2to3                     | 348 ms                                                 | 276 ms: 1.26x faster                                                      |
| nqueens                  | 106 ms                                                 | 85.1 ms: 1.24x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 68.3 ms: 1.24x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 57.8 ms: 1.20x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 837 us: 1.18x faster                                                      |
| sympy_str                | 346 ms                                                 | 296 ms: 1.17x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 99.1 ms: 1.17x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 56.8 ms: 1.16x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 24.1 ms: 1.15x faster                                                     |
| json_loads               | 31.2 us                                                | 27.1 us: 1.15x faster                                                     |
| sympy_sum                | 196 ms                                                 | 171 ms: 1.15x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 22.6 ms: 1.14x faster                                                     |
| sympy_expand             | 566 ms                                                 | 500 ms: 1.13x faster                                                      |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.95 sec: 1.12x faster                                                    |
| json                     | 5.69 ms                                                | 5.13 ms: 1.11x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.58 sec: 1.10x faster                                                    |
| sqlite_synth             | 3.02 us                                                | 2.76 us: 1.10x faster                                                     |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| regex_dna                | 227 ms                                                 | 224 ms: 1.01x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                      |
| unpickle_list            | 5.20 us                                                | 5.34 us: 1.03x slower                                                     |
| async_generators         | 444 ms                                                 | 456 ms: 1.03x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 3.79 ms: 1.05x slower                                                     |
| coverage                 | 79.4 ms                                                | 84.4 ms: 1.06x slower                                                     |
| regex_effbot             | 3.63 ms                                                | 3.86 ms: 1.06x slower                                                     |
| pickle                   | 10.7 us                                                | 11.4 us: 1.07x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.08x slower                                                     |
| telco                    | 7.27 ms                                                | 8.06 ms: 1.11x slower                                                     |
| pickle_dict              | 29.6 us                                                | 33.8 us: 1.14x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                     |
| unpack_sequence          | 60.0 ns                                                | 110 ns: 1.84x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                              |

Benchmark hidden because not significant (3): bench_mp_pool, pickle_list, unpickle
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240912-3.14.0a0-eb54546-JIT/bm-20240912-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-eb54546.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.20x