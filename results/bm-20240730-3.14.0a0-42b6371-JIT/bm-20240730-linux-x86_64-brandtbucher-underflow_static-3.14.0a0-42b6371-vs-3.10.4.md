# Results vs. 3.10.4

- fork: brandtbucher
- ref: underflow_static
- machine: linux-x86_64
- commit hash: 42b6371
- commit date: 2024-07-30
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 277 ms: 1.26x faster                                                    |
| docutils       | 3.30 sec                                               | 2.97 sec: 1.11x faster                                                  |
| html5lib       | 88.9 ms                                                | 62.7 ms: 1.42x faster                                                   |
| tornado_http   | 136 ms                                                 | 94.0 ms: 1.45x faster                                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 325 ms: 2.24x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 400 ms: 2.17x faster                                                    |
| async_tree_io           | 1.77 sec                                               | 913 ms: 1.94x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 563 ms: 1.81x faster                                                    |
| Geometric mean          | (ref)                                                  | 2.03x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.2 ms: 1.94x faster                                                   |
| float          | 117 ms                                                 | 70.9 ms: 1.65x faster                                                   |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.49x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 137 ms: 1.37x faster                                                    |
| regex_v8       | 27.8 ms                                                | 24.5 ms: 1.14x faster                                                   |
| regex_dna      | 227 ms                                                 | 231 ms: 1.02x slower                                                    |
| regex_effbot   | 3.63 ms                                                | 3.79 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 207 us: 1.59x faster                                                    |
| tomli_loads          | 3.14 sec                                               | 1.98 sec: 1.59x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 315 us: 1.54x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 55.9 ms: 1.42x faster                                                   |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 79.1 ms: 1.26x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 99.5 ms: 1.16x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.14x faster                                                    |
| json_loads           | 31.2 us                                                | 28.0 us: 1.12x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 7.14 ms: 1.20x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.91 ms: 1.65x faster                                                   |
| django_template | 48.2 ms                                                | 36.6 ms: 1.32x faster                                                   |
| genshi_text     | 31.8 ms                                                | 25.7 ms: 1.24x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 57.2 ms: 1.16x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 172 us: 3.16x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.26 ms: 2.43x faster                                                   |
| generators               | 80.1 ms                                                | 33.8 ms: 2.37x faster                                                   |
| async_tree_none          | 728 ms                                                 | 325 ms: 2.24x faster                                                    |
| deepcopy_memo            | 58.5 us                                                | 26.8 us: 2.18x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 400 ms: 2.17x faster                                                    |
| richards_super           | 94.7 ms                                                | 44.9 ms: 2.11x faster                                                   |
| richards                 | 79.3 ms                                                | 39.3 ms: 2.01x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 59.6 ms: 1.98x faster                                                   |
| nbody                    | 154 ms                                                 | 79.2 ms: 1.94x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 913 ms: 1.94x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 67.8 ms: 1.88x faster                                                   |
| chaos                    | 115 ms                                                 | 62.4 ms: 1.85x faster                                                   |
| raytrace                 | 507 ms                                                 | 275 ms: 1.84x faster                                                    |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                                    |
| asyncio_tcp              | 922 ms                                                 | 507 ms: 1.82x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 563 ms: 1.81x faster                                                    |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.75x faster                                                   |
| deepcopy                 | 479 us                                                 | 277 us: 1.73x faster                                                    |
| scimark_sor              | 220 ms                                                 | 130 ms: 1.69x faster                                                    |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.66x faster                                                    |
| float                    | 117 ms                                                 | 70.9 ms: 1.65x faster                                                   |
| mako                     | 16.3 ms                                                | 9.91 ms: 1.65x faster                                                   |
| pyflate                  | 716 ms                                                 | 436 ms: 1.64x faster                                                    |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.64x faster                                                   |
| go                       | 240 ms                                                 | 148 ms: 1.62x faster                                                    |
| unpickle_pure_python     | 331 us                                                 | 207 us: 1.59x faster                                                    |
| tomli_loads              | 3.14 sec                                               | 1.98 sec: 1.59x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.65 ms: 1.56x faster                                                   |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.55x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 315 us: 1.54x faster                                                    |
| scimark_fft              | 466 ms                                                 | 303 ms: 1.54x faster                                                    |
| hexiom                   | 10.4 ms                                                | 6.82 ms: 1.52x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.27 ms: 1.51x faster                                                   |
| pylint                   | 551 ms                                                 | 365 ms: 1.51x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 2.81 us: 1.48x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.71 us: 1.46x faster                                                   |
| tornado_http             | 136 ms                                                 | 94.0 ms: 1.45x faster                                                   |
| logging_format           | 9.09 us                                                | 6.28 us: 1.45x faster                                                   |
| fannkuch                 | 532 ms                                                 | 368 ms: 1.45x faster                                                    |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                  |
| html5lib                 | 88.9 ms                                                | 62.7 ms: 1.42x faster                                                   |
| scimark_lu               | 176 ms                                                 | 124 ms: 1.42x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 55.9 ms: 1.42x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                  |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 737 ms: 1.38x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                   |
| regex_compile            | 188 ms                                                 | 137 ms: 1.37x faster                                                    |
| thrift                   | 1.07 ms                                                | 787 us: 1.36x faster                                                    |
| django_template          | 48.2 ms                                                | 36.6 ms: 1.32x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.27x faster                                                   |
| 2to3                     | 348 ms                                                 | 277 ms: 1.26x faster                                                    |
| nqueens                  | 106 ms                                                 | 84.1 ms: 1.26x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 79.1 ms: 1.26x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.26x faster                                                    |
| genshi_text              | 31.8 ms                                                | 25.7 ms: 1.24x faster                                                   |
| dask                     | 441 ms                                                 | 365 ms: 1.21x faster                                                    |
| sqlglot_optimize         | 69.2 ms                                                | 57.4 ms: 1.20x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 822 us: 1.20x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 99.5 ms: 1.16x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 57.2 ms: 1.16x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.14x faster                                                    |
| sympy_str                | 346 ms                                                 | 304 ms: 1.14x faster                                                    |
| sympy_sum                | 196 ms                                                 | 173 ms: 1.14x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 24.5 ms: 1.14x faster                                                   |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.13x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 22.8 ms: 1.13x faster                                                   |
| json_loads               | 31.2 us                                                | 28.0 us: 1.12x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.97 sec: 1.11x faster                                                  |
| json                     | 5.69 ms                                                | 5.13 ms: 1.11x faster                                                   |
| sympy_expand             | 566 ms                                                 | 515 ms: 1.10x faster                                                    |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.78 sec: 1.02x faster                                                  |
| gc_traversal             | 3.62 ms                                                | 3.55 ms: 1.02x faster                                                   |
| regex_dna                | 227 ms                                                 | 231 ms: 1.02x slower                                                    |
| regex_effbot             | 3.63 ms                                                | 3.79 ms: 1.04x slower                                                   |
| async_generators         | 444 ms                                                 | 465 ms: 1.05x slower                                                    |
| telco                    | 7.27 ms                                                | 7.82 ms: 1.08x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.08x slower                                                   |
| coverage                 | 79.4 ms                                                | 91.2 ms: 1.15x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.14 ms: 1.20x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240730-3.14.0a0-42b6371-JIT/bm-20240730-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-42b6371.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.20x