# Results vs. 3.10.4

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: c482bbf
- commit date: 2024-08-07
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 274 ms: 1.27x faster                                                      |
| docutils       | 3.30 sec                                               | 2.91 sec: 1.13x faster                                                    |
| html5lib       | 88.9 ms                                                | 66.1 ms: 1.35x faster                                                     |
| tornado_http   | 136 ms                                                 | 92.7 ms: 1.47x faster                                                     |
| Geometric mean | (ref)                                                  | 1.30x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 324 ms: 2.25x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 420 ms: 2.07x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 901 ms: 1.96x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 567 ms: 1.79x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 78.1 ms: 1.97x faster                                                     |
| float          | 117 ms                                                 | 70.0 ms: 1.67x faster                                                     |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.50x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 134 ms: 1.40x faster                                                      |
| regex_v8       | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                     |
| regex_dna      | 227 ms                                                 | 228 ms: 1.01x slower                                                      |
| regex_effbot   | 3.63 ms                                                | 3.84 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                  | 1.10x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 295 us: 1.64x faster                                                      |
| tomli_loads          | 3.14 sec                                               | 1.92 sec: 1.64x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 55.8 ms: 1.42x faster                                                     |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 79.4 ms: 1.25x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 99.2 ms: 1.16x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                      |
| json_loads           | 31.2 us                                                | 28.0 us: 1.11x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.20 ms: 1.21x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.70 ms: 1.68x faster                                                     |
| django_template | 48.2 ms                                                | 36.0 ms: 1.34x faster                                                     |
| genshi_text     | 31.8 ms                                                | 24.0 ms: 1.33x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 53.4 ms: 1.24x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.25x faster                                                      |
| generators               | 80.1 ms                                                | 33.1 ms: 2.42x faster                                                     |
| deltablue                | 7.91 ms                                                | 3.48 ms: 2.27x faster                                                     |
| async_tree_none          | 728 ms                                                 | 324 ms: 2.25x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 420 ms: 2.07x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 28.6 us: 2.05x faster                                                     |
| richards_super           | 94.7 ms                                                | 47.0 ms: 2.02x faster                                                     |
| chaos                    | 115 ms                                                 | 58.2 ms: 1.98x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 60.1 ms: 1.97x faster                                                     |
| nbody                    | 154 ms                                                 | 78.1 ms: 1.97x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 901 ms: 1.96x faster                                                      |
| richards                 | 79.3 ms                                                | 41.1 ms: 1.93x faster                                                     |
| raytrace                 | 507 ms                                                 | 263 ms: 1.93x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 66.9 ms: 1.91x faster                                                     |
| logging_silent           | 190 ns                                                 | 102 ns: 1.87x faster                                                      |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                                      |
| asyncio_tcp              | 922 ms                                                 | 500 ms: 1.84x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 567 ms: 1.79x faster                                                      |
| deepcopy                 | 479 us                                                 | 274 us: 1.75x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                     |
| pyflate                  | 716 ms                                                 | 421 ms: 1.70x faster                                                      |
| mako                     | 16.3 ms                                                | 9.70 ms: 1.68x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                     |
| go                       | 240 ms                                                 | 143 ms: 1.68x faster                                                      |
| float                    | 117 ms                                                 | 70.0 ms: 1.67x faster                                                     |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.65x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 295 us: 1.64x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 1.92 sec: 1.64x faster                                                    |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                                     |
| scimark_lu               | 176 ms                                                 | 112 ms: 1.57x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.64 ms: 1.57x faster                                                     |
| pylint                   | 551 ms                                                 | 355 ms: 1.55x faster                                                      |
| coroutines               | 35.1 ms                                                | 22.8 ms: 1.54x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                                     |
| scimark_fft              | 466 ms                                                 | 306 ms: 1.52x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.31 ms: 1.50x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.61 us: 1.48x faster                                                     |
| fannkuch                 | 532 ms                                                 | 361 ms: 1.47x faster                                                      |
| tornado_http             | 136 ms                                                 | 92.7 ms: 1.47x faster                                                     |
| logging_format           | 9.09 us                                                | 6.18 us: 1.47x faster                                                     |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 55.8 ms: 1.42x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 720 ms: 1.41x faster                                                      |
| regex_compile            | 188 ms                                                 | 134 ms: 1.40x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                    |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                     |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                     |
| html5lib                 | 88.9 ms                                                | 66.1 ms: 1.35x faster                                                     |
| thrift                   | 1.07 ms                                                | 798 us: 1.34x faster                                                      |
| django_template          | 48.2 ms                                                | 36.0 ms: 1.34x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.33x faster                                                    |
| genshi_text              | 31.8 ms                                                | 24.0 ms: 1.33x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.28x faster                                                      |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                     |
| 2to3                     | 348 ms                                                 | 274 ms: 1.27x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 79.4 ms: 1.25x faster                                                     |
| nqueens                  | 106 ms                                                 | 84.8 ms: 1.25x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 55.7 ms: 1.24x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 53.4 ms: 1.24x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 819 us: 1.20x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 99.2 ms: 1.16x faster                                                     |
| sympy_str                | 346 ms                                                 | 298 ms: 1.16x faster                                                      |
| sympy_sum                | 196 ms                                                 | 170 ms: 1.16x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 22.5 ms: 1.15x faster                                                     |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.91 sec: 1.13x faster                                                    |
| sympy_expand             | 566 ms                                                 | 508 ms: 1.11x faster                                                      |
| json_loads               | 31.2 us                                                | 28.0 us: 1.11x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.57 sec: 1.11x faster                                                    |
| json                     | 5.69 ms                                                | 5.16 ms: 1.10x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                     |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                      |
| regex_dna                | 227 ms                                                 | 228 ms: 1.01x slower                                                      |
| async_generators         | 444 ms                                                 | 459 ms: 1.04x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 3.77 ms: 1.04x slower                                                     |
| regex_effbot             | 3.63 ms                                                | 3.84 ms: 1.06x slower                                                     |
| telco                    | 7.27 ms                                                | 7.90 ms: 1.09x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 1.77 ms: 1.09x slower                                                     |
| coverage                 | 79.4 ms                                                | 90.9 ms: 1.14x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.20 ms: 1.21x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240807-3.14.0a0-c482bbf-JIT/bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.20x