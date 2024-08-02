# Results vs. 3.10.4

- fork: brandtbucher
- ref: warmer_side_exits
- machine: linux-x86_64
- commit hash: 8423e72
- commit date: 2024-07-01
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 274 ms: 1.27x faster                                                     |
| docutils       | 3.30 sec                                               | 2.86 sec: 1.15x faster                                                   |
| html5lib       | 88.9 ms                                                | 65.7 ms: 1.35x faster                                                    |
| tornado_http   | 136 ms                                                 | 92.2 ms: 1.48x faster                                                    |
| Geometric mean | (ref)                                                  | 1.31x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 312 ms: 2.33x faster                                                     |
| async_tree_memoization  | 870 ms                                                 | 403 ms: 2.16x faster                                                     |
| async_tree_io           | 1.77 sec                                               | 867 ms: 2.04x faster                                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 555 ms: 1.83x faster                                                     |
| Geometric mean          | (ref)                                                  | 2.08x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.7 ms: 1.93x faster                                                    |
| float          | 117 ms                                                 | 70.7 ms: 1.66x faster                                                    |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.49x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 134 ms: 1.40x faster                                                     |
| regex_v8       | 27.8 ms                                                | 24.9 ms: 1.12x faster                                                    |
| regex_dna      | 227 ms                                                 | 226 ms: 1.00x faster                                                     |
| regex_effbot   | 3.63 ms                                                | 3.68 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                  | 1.12x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 201 us: 1.65x faster                                                     |
| tomli_loads          | 3.14 sec                                               | 1.91 sec: 1.64x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 299 us: 1.62x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 57.1 ms: 1.39x faster                                                    |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                    |
| xml_etree_generate   | 99.4 ms                                                | 81.1 ms: 1.23x faster                                                    |
| xml_etree_iterparse  | 115 ms                                                 | 99.1 ms: 1.16x faster                                                    |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                     |
| json_loads           | 31.2 us                                                | 27.6 us: 1.13x faster                                                    |
| Geometric mean       | (ref)                                                  | 1.36x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.4 ms: 1.40x faster                                                    |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.53 ms: 1.71x faster                                                    |
| django_template | 48.2 ms                                                | 35.3 ms: 1.36x faster                                                    |
| genshi_text     | 31.8 ms                                                | 25.0 ms: 1.27x faster                                                    |
| genshi_xml      | 66.0 ms                                                | 58.1 ms: 1.14x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.36x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.20x faster                                                     |
| generators               | 80.1 ms                                                | 30.1 ms: 2.66x faster                                                    |
| async_tree_none          | 728 ms                                                 | 312 ms: 2.33x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 403 ms: 2.16x faster                                                     |
| deltablue                | 7.91 ms                                                | 3.81 ms: 2.08x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 867 ms: 2.04x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 29.0 us: 2.02x faster                                                    |
| chaos                    | 115 ms                                                 | 57.9 ms: 1.99x faster                                                    |
| scimark_monte_carlo      | 118 ms                                                 | 60.7 ms: 1.95x faster                                                    |
| nbody                    | 154 ms                                                 | 79.7 ms: 1.93x faster                                                    |
| richards_super           | 94.7 ms                                                | 49.3 ms: 1.92x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 67.0 ms: 1.91x faster                                                    |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 499 ms: 1.85x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 555 ms: 1.83x faster                                                     |
| richards                 | 79.3 ms                                                | 43.6 ms: 1.82x faster                                                    |
| logging_silent           | 190 ns                                                 | 107 ns: 1.78x faster                                                     |
| deepcopy                 | 479 us                                                 | 271 us: 1.77x faster                                                     |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                    |
| mako                     | 16.3 ms                                                | 9.53 ms: 1.71x faster                                                    |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                                    |
| scimark_sor              | 220 ms                                                 | 131 ms: 1.68x faster                                                     |
| go                       | 240 ms                                                 | 143 ms: 1.67x faster                                                     |
| float                    | 117 ms                                                 | 70.7 ms: 1.66x faster                                                    |
| pyflate                  | 716 ms                                                 | 434 ms: 1.65x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 201 us: 1.65x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.91 sec: 1.64x faster                                                   |
| spectral_norm            | 170 ms                                                 | 105 ms: 1.62x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 299 us: 1.62x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.61x faster                                                    |
| pylint                   | 551 ms                                                 | 346 ms: 1.60x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.57 ms: 1.58x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 2.73 us: 1.53x faster                                                    |
| logging_format           | 9.09 us                                                | 6.00 us: 1.52x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.30 ms: 1.51x faster                                                    |
| logging_simple           | 8.30 us                                                | 5.52 us: 1.50x faster                                                    |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.50x faster                                                    |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                                     |
| fannkuch                 | 532 ms                                                 | 359 ms: 1.48x faster                                                     |
| tornado_http             | 136 ms                                                 | 92.2 ms: 1.48x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                   |
| scimark_lu               | 176 ms                                                 | 125 ms: 1.41x faster                                                     |
| regex_compile            | 188 ms                                                 | 134 ms: 1.40x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 726 ms: 1.40x faster                                                     |
| python_startup           | 14.6 ms                                                | 10.4 ms: 1.40x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 57.1 ms: 1.39x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                                   |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                    |
| django_template          | 48.2 ms                                                | 35.3 ms: 1.36x faster                                                    |
| html5lib                 | 88.9 ms                                                | 65.7 ms: 1.35x faster                                                    |
| thrift                   | 1.07 ms                                                | 798 us: 1.34x faster                                                     |
| pathlib                  | 20.5 ms                                                | 15.8 ms: 1.29x faster                                                    |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.28x faster                                                     |
| genshi_text              | 31.8 ms                                                | 25.0 ms: 1.27x faster                                                    |
| 2to3                     | 348 ms                                                 | 274 ms: 1.27x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 67.1 ms: 1.26x faster                                                    |
| sqlglot_optimize         | 69.2 ms                                                | 56.3 ms: 1.23x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 81.1 ms: 1.23x faster                                                    |
| dask                     | 441 ms                                                 | 363 ms: 1.21x faster                                                     |
| nqueens                  | 106 ms                                                 | 87.5 ms: 1.21x faster                                                    |
| bench_thread_pool        | 986 us                                                 | 833 us: 1.18x faster                                                     |
| sympy_sum                | 196 ms                                                 | 167 ms: 1.17x faster                                                     |
| sympy_str                | 346 ms                                                 | 295 ms: 1.17x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 22.1 ms: 1.17x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 99.1 ms: 1.16x faster                                                    |
| docutils                 | 3.30 sec                                               | 2.86 sec: 1.15x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 58.1 ms: 1.14x faster                                                    |
| sympy_expand             | 566 ms                                                 | 499 ms: 1.13x faster                                                     |
| json_loads               | 31.2 us                                                | 27.6 us: 1.13x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.53 sec: 1.13x faster                                                   |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.12x faster                                                     |
| json                     | 5.69 ms                                                | 5.10 ms: 1.12x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 24.9 ms: 1.12x faster                                                    |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                     |
| regex_dna                | 227 ms                                                 | 226 ms: 1.00x faster                                                     |
| gc_traversal             | 3.62 ms                                                | 3.68 ms: 1.01x slower                                                    |
| regex_effbot             | 3.63 ms                                                | 3.68 ms: 1.02x slower                                                    |
| async_generators         | 444 ms                                                 | 454 ms: 1.02x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                    |
| telco                    | 7.27 ms                                                | 7.90 ms: 1.09x slower                                                    |
| coverage                 | 79.4 ms                                                | 93.2 ms: 1.17x slower                                                    |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240701-3.14.0a0-8423e72-JIT/bm-20240701-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.20x