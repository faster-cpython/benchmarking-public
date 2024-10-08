# Results vs. 3.10.4

- fork: brandtbucher
- ref: confidence
- machine: linux-x86_64
- commit hash: d06074b
- commit date: 2024-09-12
- overall geometric mean: 1.38x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 273 ms: 1.28x faster                                              |
| docutils       | 3.30 sec                                               | 2.96 sec: 1.11x faster                                            |
| html5lib       | 88.9 ms                                                | 64.6 ms: 1.38x faster                                             |
| tornado_http   | 136 ms                                                 | 94.9 ms: 1.44x faster                                             |
| Geometric mean | (ref)                                                  | 1.29x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 315 ms: 2.31x faster                                              |
| async_tree_memoization  | 870 ms                                                 | 393 ms: 2.21x faster                                              |
| async_tree_io           | 1.77 sec                                               | 858 ms: 2.06x faster                                              |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 568 ms: 1.79x faster                                              |
| Geometric mean          | (ref)                                                  | 2.08x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.9 ms: 1.92x faster                                             |
| float          | 117 ms                                                 | 69.9 ms: 1.67x faster                                             |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                  | 1.49x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 140 ms: 1.35x faster                                              |
| regex_v8       | 27.8 ms                                                | 24.4 ms: 1.14x faster                                             |
| regex_dna      | 227 ms                                                 | 221 ms: 1.02x faster                                              |
| regex_effbot   | 3.63 ms                                                | 3.82 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                  | 1.10x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                            |
| pickle_pure_python   | 484 us                                                 | 304 us: 1.59x faster                                              |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                              |
| xml_etree_process    | 79.1 ms                                                | 54.6 ms: 1.45x faster                                             |
| json_dumps           | 14.2 ms                                                | 10.1 ms: 1.40x faster                                             |
| xml_etree_generate   | 99.4 ms                                                | 76.9 ms: 1.29x faster                                             |
| xml_etree_iterparse  | 115 ms                                                 | 98.3 ms: 1.17x faster                                             |
| xml_etree_parse      | 168 ms                                                 | 145 ms: 1.16x faster                                              |
| json_loads           | 31.2 us                                                | 27.0 us: 1.16x faster                                             |
| unpickle_list        | 5.20 us                                                | 5.07 us: 1.03x faster                                             |
| pickle_list          | 5.08 us                                                | 5.24 us: 1.03x slower                                             |
| pickle               | 10.7 us                                                | 11.7 us: 1.10x slower                                             |
| pickle_dict          | 29.6 us                                                | 34.9 us: 1.18x slower                                             |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                      |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                             |
| python_startup_no_site | 5.93 ms                                                | 7.04 ms: 1.19x slower                                             |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.85 ms: 1.66x faster                                             |
| django_template | 48.2 ms                                                | 35.9 ms: 1.34x faster                                             |
| genshi_text     | 31.8 ms                                                | 24.8 ms: 1.28x faster                                             |
| genshi_xml      | 66.0 ms                                                | 56.4 ms: 1.17x faster                                             |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.35x faster                                              |
| deltablue                | 7.91 ms                                                | 3.24 ms: 2.44x faster                                             |
| generators               | 80.1 ms                                                | 32.9 ms: 2.44x faster                                             |
| async_tree_none          | 728 ms                                                 | 315 ms: 2.31x faster                                              |
| async_tree_memoization   | 870 ms                                                 | 393 ms: 2.21x faster                                              |
| richards_super           | 94.7 ms                                                | 43.3 ms: 2.19x faster                                             |
| deepcopy_memo            | 58.5 us                                                | 27.0 us: 2.17x faster                                             |
| async_tree_io            | 1.77 sec                                               | 858 ms: 2.06x faster                                              |
| richards                 | 79.3 ms                                                | 39.3 ms: 2.02x faster                                             |
| chaos                    | 115 ms                                                 | 59.2 ms: 1.95x faster                                             |
| crypto_pyaes             | 128 ms                                                 | 66.0 ms: 1.94x faster                                             |
| nbody                    | 154 ms                                                 | 79.9 ms: 1.92x faster                                             |
| scimark_monte_carlo      | 118 ms                                                 | 62.3 ms: 1.90x faster                                             |
| scimark_sor              | 220 ms                                                 | 116 ms: 1.89x faster                                              |
| asyncio_tcp              | 922 ms                                                 | 494 ms: 1.87x faster                                              |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                              |
| raytrace                 | 507 ms                                                 | 276 ms: 1.84x faster                                              |
| go                       | 240 ms                                                 | 131 ms: 1.83x faster                                              |
| logging_silent           | 190 ns                                                 | 105 ns: 1.81x faster                                              |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 568 ms: 1.79x faster                                              |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                             |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.69x faster                                              |
| float                    | 117 ms                                                 | 69.9 ms: 1.67x faster                                             |
| pyflate                  | 716 ms                                                 | 430 ms: 1.66x faster                                              |
| mako                     | 16.3 ms                                                | 9.85 ms: 1.66x faster                                             |
| sqlglot_parse            | 2.17 ms                                                | 1.34 ms: 1.62x faster                                             |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                            |
| pickle_pure_python       | 484 us                                                 | 304 us: 1.59x faster                                              |
| scimark_lu               | 176 ms                                                 | 111 ms: 1.59x faster                                              |
| deepcopy_reduce          | 4.17 us                                                | 2.64 us: 1.58x faster                                             |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.11 ms: 1.58x faster                                             |
| coroutines               | 35.1 ms                                                | 22.6 ms: 1.55x faster                                             |
| sqlglot_transpile        | 2.57 ms                                                | 1.68 ms: 1.53x faster                                             |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                              |
| hexiom                   | 10.4 ms                                                | 6.88 ms: 1.51x faster                                             |
| scimark_fft              | 466 ms                                                 | 308 ms: 1.51x faster                                              |
| logging_format           | 9.09 us                                                | 6.11 us: 1.49x faster                                             |
| logging_simple           | 8.30 us                                                | 5.61 us: 1.48x faster                                             |
| pylint                   | 551 ms                                                 | 375 ms: 1.47x faster                                              |
| xml_etree_process        | 79.1 ms                                                | 54.6 ms: 1.45x faster                                             |
| tornado_http             | 136 ms                                                 | 94.9 ms: 1.44x faster                                             |
| pprint_safe_repr         | 1.02 sec                                               | 710 ms: 1.43x faster                                              |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                            |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                            |
| fannkuch                 | 532 ms                                                 | 375 ms: 1.42x faster                                              |
| json_dumps               | 14.2 ms                                                | 10.1 ms: 1.40x faster                                             |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                             |
| html5lib                 | 88.9 ms                                                | 64.6 ms: 1.38x faster                                             |
| thrift                   | 1.07 ms                                                | 789 us: 1.36x faster                                              |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.35x faster                                            |
| regex_compile            | 188 ms                                                 | 140 ms: 1.35x faster                                              |
| django_template          | 48.2 ms                                                | 35.9 ms: 1.34x faster                                             |
| xml_etree_generate       | 99.4 ms                                                | 76.9 ms: 1.29x faster                                             |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                             |
| genshi_text              | 31.8 ms                                                | 24.8 ms: 1.28x faster                                             |
| 2to3                     | 348 ms                                                 | 273 ms: 1.28x faster                                              |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.27x faster                                              |
| nqueens                  | 106 ms                                                 | 84.1 ms: 1.26x faster                                             |
| dulwich_log              | 84.3 ms                                                | 67.3 ms: 1.25x faster                                             |
| sqlglot_optimize         | 69.2 ms                                                | 58.2 ms: 1.19x faster                                             |
| bench_thread_pool        | 986 us                                                 | 838 us: 1.18x faster                                              |
| xml_etree_iterparse      | 115 ms                                                 | 98.3 ms: 1.17x faster                                             |
| genshi_xml               | 66.0 ms                                                | 56.4 ms: 1.17x faster                                             |
| sympy_str                | 346 ms                                                 | 298 ms: 1.16x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 145 ms: 1.16x faster                                              |
| json_loads               | 31.2 us                                                | 27.0 us: 1.16x faster                                             |
| sympy_sum                | 196 ms                                                 | 172 ms: 1.14x faster                                              |
| regex_v8                 | 27.8 ms                                                | 24.4 ms: 1.14x faster                                             |
| json                     | 5.69 ms                                                | 5.01 ms: 1.13x faster                                             |
| sympy_integrate          | 25.8 ms                                                | 22.8 ms: 1.13x faster                                             |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                              |
| sympy_expand             | 566 ms                                                 | 500 ms: 1.13x faster                                              |
| docutils                 | 3.30 sec                                               | 2.96 sec: 1.11x faster                                            |
| sqlite_synth             | 3.02 us                                                | 2.78 us: 1.09x faster                                             |
| mdp                      | 2.85 sec                                               | 2.66 sec: 1.07x faster                                            |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                              |
| unpickle_list            | 5.20 us                                                | 5.07 us: 1.03x faster                                             |
| regex_dna                | 227 ms                                                 | 221 ms: 1.02x faster                                              |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                              |
| async_generators         | 444 ms                                                 | 455 ms: 1.02x slower                                              |
| pickle_list              | 5.08 us                                                | 5.24 us: 1.03x slower                                             |
| regex_effbot             | 3.63 ms                                                | 3.82 ms: 1.05x slower                                             |
| coverage                 | 79.4 ms                                                | 84.4 ms: 1.06x slower                                             |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                             |
| pickle                   | 10.7 us                                                | 11.7 us: 1.10x slower                                             |
| gc_traversal             | 3.62 ms                                                | 3.98 ms: 1.10x slower                                             |
| telco                    | 7.27 ms                                                | 8.00 ms: 1.10x slower                                             |
| pickle_dict              | 29.6 us                                                | 34.9 us: 1.18x slower                                             |
| python_startup_no_site   | 5.93 ms                                                | 7.04 ms: 1.19x slower                                             |
| unpack_sequence          | 60.0 ns                                                | 111 ns: 1.85x slower                                              |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                      |

Benchmark hidden because not significant (2): bench_mp_pool, unpickle
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240912-3.14.0a0-d06074b-JIT/bm-20240912-linux-x86_64-brandtbucher-confidence-3.14.0a0-d06074b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.21x