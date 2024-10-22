# Results vs. 3.10.4

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: 85c5a08
- commit date: 2024-08-21
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 283 ms: 1.23x faster                                                      |
| docutils       | 3.30 sec                                               | 3.06 sec: 1.08x faster                                                    |
| html5lib       | 88.9 ms                                                | 66.4 ms: 1.34x faster                                                     |
| tornado_http   | 136 ms                                                 | 94.1 ms: 1.45x faster                                                     |
| Geometric mean | (ref)                                                  | 1.27x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 329 ms: 2.22x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 429 ms: 2.03x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 903 ms: 1.96x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 571 ms: 1.78x faster                                                      |
| Geometric mean          | (ref)                                                  | 1.99x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.2 ms: 1.87x faster                                                     |
| float          | 117 ms                                                 | 71.1 ms: 1.65x faster                                                     |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.47x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 143 ms: 1.32x faster                                                      |
| regex_v8       | 27.8 ms                                                | 23.8 ms: 1.17x faster                                                     |
| regex_dna      | 227 ms                                                 | 215 ms: 1.06x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.55 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.14x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 306 us: 1.59x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.54x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 55.9 ms: 1.42x faster                                                     |
| json_dumps           | 14.2 ms                                                | 10.2 ms: 1.39x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 78.1 ms: 1.27x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 98.9 ms: 1.17x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                      |
| json_loads           | 31.2 us                                                | 28.3 us: 1.10x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.12 ms: 1.20x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.74 ms: 1.68x faster                                                     |
| django_template | 48.2 ms                                                | 36.8 ms: 1.31x faster                                                     |
| genshi_text     | 31.8 ms                                                | 25.6 ms: 1.24x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 60.0 ms: 1.10x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.20x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.14 ms: 2.52x faster                                                     |
| generators               | 80.1 ms                                                | 32.6 ms: 2.45x faster                                                     |
| async_tree_none          | 728 ms                                                 | 329 ms: 2.22x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 27.3 us: 2.15x faster                                                     |
| richards_super           | 94.7 ms                                                | 44.7 ms: 2.12x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 429 ms: 2.03x faster                                                      |
| richards                 | 79.3 ms                                                | 39.4 ms: 2.01x faster                                                     |
| chaos                    | 115 ms                                                 | 58.9 ms: 1.96x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 903 ms: 1.96x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 65.3 ms: 1.96x faster                                                     |
| scimark_sor              | 220 ms                                                 | 116 ms: 1.90x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 62.6 ms: 1.89x faster                                                     |
| nbody                    | 154 ms                                                 | 82.2 ms: 1.87x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 496 ms: 1.86x faster                                                      |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                                      |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                                      |
| deepcopy                 | 479 us                                                 | 266 us: 1.80x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 571 ms: 1.78x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                     |
| spectral_norm            | 170 ms                                                 | 99.6 ms: 1.70x faster                                                     |
| mako                     | 16.3 ms                                                | 9.74 ms: 1.68x faster                                                     |
| float                    | 117 ms                                                 | 71.1 ms: 1.65x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.64x faster                                                     |
| pyflate                  | 716 ms                                                 | 438 ms: 1.63x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                    |
| go                       | 240 ms                                                 | 148 ms: 1.63x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 306 us: 1.59x faster                                                      |
| scimark_lu               | 176 ms                                                 | 111 ms: 1.58x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.64 us: 1.58x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.54x faster                                                      |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.54x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.70 ms: 1.52x faster                                                     |
| logging_format           | 9.09 us                                                | 6.00 us: 1.51x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.87 ms: 1.51x faster                                                     |
| scimark_fft              | 466 ms                                                 | 308 ms: 1.51x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.51 us: 1.51x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.37 ms: 1.48x faster                                                     |
| pylint                   | 551 ms                                                 | 373 ms: 1.48x faster                                                      |
| tornado_http             | 136 ms                                                 | 94.1 ms: 1.45x faster                                                     |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                    |
| fannkuch                 | 532 ms                                                 | 373 ms: 1.43x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 55.9 ms: 1.42x faster                                                     |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                     |
| json_dumps               | 14.2 ms                                                | 10.2 ms: 1.39x faster                                                     |
| thrift                   | 1.07 ms                                                | 787 us: 1.36x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.55 sec: 1.35x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 755 ms: 1.35x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                                    |
| html5lib                 | 88.9 ms                                                | 66.4 ms: 1.34x faster                                                     |
| regex_compile            | 188 ms                                                 | 143 ms: 1.32x faster                                                      |
| django_template          | 48.2 ms                                                | 36.8 ms: 1.31x faster                                                     |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 78.1 ms: 1.27x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 115 ms: 1.25x faster                                                      |
| genshi_text              | 31.8 ms                                                | 25.6 ms: 1.24x faster                                                     |
| 2to3                     | 348 ms                                                 | 283 ms: 1.23x faster                                                      |
| nqueens                  | 106 ms                                                 | 86.1 ms: 1.23x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 822 us: 1.20x faster                                                      |
| sqlglot_optimize         | 69.2 ms                                                | 58.2 ms: 1.19x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 23.8 ms: 1.17x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 98.9 ms: 1.17x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                      |
| sympy_str                | 346 ms                                                 | 306 ms: 1.13x faster                                                      |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 23.3 ms: 1.11x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.57 sec: 1.11x faster                                                    |
| sympy_sum                | 196 ms                                                 | 178 ms: 1.10x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 60.0 ms: 1.10x faster                                                     |
| json_loads               | 31.2 us                                                | 28.3 us: 1.10x faster                                                     |
| sympy_expand             | 566 ms                                                 | 514 ms: 1.10x faster                                                      |
| docutils                 | 3.30 sec                                               | 3.06 sec: 1.08x faster                                                    |
| json                     | 5.69 ms                                                | 5.34 ms: 1.07x faster                                                     |
| regex_dna                | 227 ms                                                 | 215 ms: 1.06x faster                                                      |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| regex_effbot             | 3.63 ms                                                | 3.55 ms: 1.02x faster                                                     |
| gc_traversal             | 3.62 ms                                                | 3.56 ms: 1.02x faster                                                     |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                      |
| async_generators         | 444 ms                                                 | 461 ms: 1.04x slower                                                      |
| telco                    | 7.27 ms                                                | 7.69 ms: 1.06x slower                                                     |
| coverage                 | 79.4 ms                                                | 85.1 ms: 1.07x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.07x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.12 ms: 1.20x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240821-3.14.0a0-85c5a08-JIT/bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.21x