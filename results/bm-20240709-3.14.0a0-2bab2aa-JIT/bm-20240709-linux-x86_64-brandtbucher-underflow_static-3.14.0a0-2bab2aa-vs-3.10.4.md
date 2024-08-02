# Results vs. 3.10.4

- fork: brandtbucher
- ref: underflow_static
- machine: linux-x86_64
- commit hash: 2bab2aa
- commit date: 2024-07-09
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240709-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-2bab2aa |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 274 ms: 1.27x faster                                                    |
| docutils       | 3.30 sec                                               | 2.90 sec: 1.14x faster                                                  |
| html5lib       | 88.9 ms                                                | 65.1 ms: 1.37x faster                                                   |
| tornado_http   | 136 ms                                                 | 92.6 ms: 1.47x faster                                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240709-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-2bab2aa |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 325 ms: 2.24x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 406 ms: 2.14x faster                                                    |
| async_tree_io           | 1.77 sec                                               | 852 ms: 2.08x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 568 ms: 1.79x faster                                                    |
| Geometric mean          | (ref)                                                  | 2.05x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240709-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-2bab2aa |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.2 ms: 1.92x faster                                                   |
| float          | 117 ms                                                 | 69.9 ms: 1.68x faster                                                   |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.49x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240709-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-2bab2aa |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 137 ms: 1.38x faster                                                    |
| regex_v8       | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                   |
| regex_dna      | 227 ms                                                 | 229 ms: 1.01x slower                                                    |
| regex_effbot   | 3.63 ms                                                | 3.74 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240709-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-2bab2aa |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 297 us: 1.63x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 206 us: 1.60x faster                                                    |
| tomli_loads          | 3.14 sec                                               | 1.97 sec: 1.60x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 57.7 ms: 1.37x faster                                                   |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 82.3 ms: 1.21x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 99.0 ms: 1.17x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.14x faster                                                    |
| json_loads           | 31.2 us                                                | 27.4 us: 1.14x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240709-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-2bab2aa |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240709-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-2bab2aa |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.82 ms: 1.66x faster                                                   |
| django_template | 48.2 ms                                                | 35.8 ms: 1.35x faster                                                   |
| genshi_text     | 31.8 ms                                                | 26.0 ms: 1.22x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 59.4 ms: 1.11x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240709-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-2bab2aa |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.20x faster                                                    |
| generators               | 80.1 ms                                                | 29.7 ms: 2.70x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.52 ms: 2.25x faster                                                   |
| async_tree_none          | 728 ms                                                 | 325 ms: 2.24x faster                                                    |
| deepcopy_memo            | 58.5 us                                                | 27.3 us: 2.14x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 406 ms: 2.14x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 852 ms: 2.08x faster                                                    |
| richards_super           | 94.7 ms                                                | 45.7 ms: 2.07x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 58.2 ms: 2.03x faster                                                   |
| richards                 | 79.3 ms                                                | 39.8 ms: 1.99x faster                                                   |
| logging_silent           | 190 ns                                                 | 98.0 ns: 1.93x faster                                                   |
| nbody                    | 154 ms                                                 | 80.2 ms: 1.92x faster                                                   |
| chaos                    | 115 ms                                                 | 61.0 ms: 1.89x faster                                                   |
| raytrace                 | 507 ms                                                 | 272 ms: 1.87x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 68.8 ms: 1.86x faster                                                   |
| asyncio_tcp              | 922 ms                                                 | 501 ms: 1.84x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 568 ms: 1.79x faster                                                    |
| deepcopy                 | 479 us                                                 | 271 us: 1.77x faster                                                    |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                   |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                   |
| scimark_sor              | 220 ms                                                 | 131 ms: 1.68x faster                                                    |
| float                    | 117 ms                                                 | 69.9 ms: 1.68x faster                                                   |
| go                       | 240 ms                                                 | 143 ms: 1.68x faster                                                    |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.67x faster                                                    |
| pyflate                  | 716 ms                                                 | 429 ms: 1.67x faster                                                    |
| mako                     | 16.3 ms                                                | 9.82 ms: 1.66x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 297 us: 1.63x faster                                                    |
| pylint                   | 551 ms                                                 | 339 ms: 1.63x faster                                                    |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 206 us: 1.60x faster                                                    |
| tomli_loads              | 3.14 sec                                               | 1.97 sec: 1.60x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.58 ms: 1.58x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.57x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.46 us: 1.52x faster                                                   |
| logging_format           | 9.09 us                                                | 6.04 us: 1.51x faster                                                   |
| scimark_fft              | 466 ms                                                 | 310 ms: 1.50x faster                                                    |
| coroutines               | 35.1 ms                                                | 23.5 ms: 1.49x faster                                                   |
| fannkuch                 | 532 ms                                                 | 357 ms: 1.49x faster                                                    |
| tornado_http             | 136 ms                                                 | 92.6 ms: 1.47x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 694 ms: 1.47x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.44 sec: 1.46x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.46 ms: 1.45x faster                                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                  |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                   |
| regex_compile            | 188 ms                                                 | 137 ms: 1.38x faster                                                    |
| scimark_lu               | 176 ms                                                 | 128 ms: 1.37x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 57.7 ms: 1.37x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                  |
| html5lib                 | 88.9 ms                                                | 65.1 ms: 1.37x faster                                                   |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                   |
| django_template          | 48.2 ms                                                | 35.8 ms: 1.35x faster                                                   |
| thrift                   | 1.07 ms                                                | 799 us: 1.34x faster                                                    |
| sqlglot_normalize        | 143 ms                                                 | 111 ms: 1.29x faster                                                    |
| 2to3                     | 348 ms                                                 | 274 ms: 1.27x faster                                                    |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 67.4 ms: 1.25x faster                                                   |
| nqueens                  | 106 ms                                                 | 84.6 ms: 1.25x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 55.6 ms: 1.24x faster                                                   |
| genshi_text              | 31.8 ms                                                | 26.0 ms: 1.22x faster                                                   |
| dask                     | 441 ms                                                 | 362 ms: 1.22x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 82.3 ms: 1.21x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 831 us: 1.19x faster                                                    |
| sympy_sum                | 196 ms                                                 | 166 ms: 1.18x faster                                                    |
| sympy_str                | 346 ms                                                 | 294 ms: 1.18x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 22.0 ms: 1.17x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 99.0 ms: 1.17x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.14x faster                                                    |
| json_loads               | 31.2 us                                                | 27.4 us: 1.14x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.90 sec: 1.14x faster                                                  |
| sympy_expand             | 566 ms                                                 | 498 ms: 1.14x faster                                                    |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                    |
| json                     | 5.69 ms                                                | 5.11 ms: 1.11x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 59.4 ms: 1.11x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.75 sec: 1.04x faster                                                  |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                    |
| gc_traversal             | 3.62 ms                                                | 3.52 ms: 1.03x faster                                                   |
| regex_dna                | 227 ms                                                 | 229 ms: 1.01x slower                                                    |
| async_generators         | 444 ms                                                 | 450 ms: 1.01x slower                                                    |
| regex_effbot             | 3.63 ms                                                | 3.74 ms: 1.03x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                   |
| telco                    | 7.27 ms                                                | 7.94 ms: 1.09x slower                                                   |
| coverage                 | 79.4 ms                                                | 93.9 ms: 1.18x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240709-3.14.0a0-2bab2aa-JIT/bm-20240709-linux-x86_64-brandtbucher-underflow_static-3.14.0a0-2bab2aa.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.19x