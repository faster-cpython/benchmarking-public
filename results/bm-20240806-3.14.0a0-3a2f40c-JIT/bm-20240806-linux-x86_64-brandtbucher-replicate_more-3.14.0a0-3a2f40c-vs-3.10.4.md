# Results vs. 3.10.4

- fork: brandtbucher
- ref: replicate_more
- machine: linux-x86_64
- commit hash: 3a2f40c
- commit date: 2024-08-06
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 274 ms: 1.27x faster                                                  |
| docutils       | 3.30 sec                                               | 2.91 sec: 1.13x faster                                                |
| html5lib       | 88.9 ms                                                | 64.3 ms: 1.38x faster                                                 |
| tornado_http   | 136 ms                                                 | 92.9 ms: 1.47x faster                                                 |
| Geometric mean | (ref)                                                  | 1.31x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.24x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 430 ms: 2.02x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 909 ms: 1.95x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 563 ms: 1.80x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.00x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 85.7 ms: 1.79x faster                                                 |
| float          | 117 ms                                                 | 72.9 ms: 1.61x faster                                                 |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.43x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 133 ms: 1.42x faster                                                  |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.10x faster                                                 |
| regex_dna      | 227 ms                                                 | 229 ms: 1.01x slower                                                  |
| regex_effbot   | 3.63 ms                                                | 3.90 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 293 us: 1.65x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 1.92 sec: 1.64x faster                                                |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.54x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 56.2 ms: 1.41x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 79.8 ms: 1.25x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 99.5 ms: 1.16x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                  |
| json_loads           | 31.2 us                                                | 28.3 us: 1.10x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.15 ms: 1.21x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.79 ms: 1.67x faster                                                 |
| django_template | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                 |
| genshi_text     | 31.8 ms                                                | 24.2 ms: 1.32x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 52.9 ms: 1.25x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.21x faster                                                  |
| generators               | 80.1 ms                                                | 32.8 ms: 2.44x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.52 ms: 2.25x faster                                                 |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.24x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 28.7 us: 2.04x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 430 ms: 2.02x faster                                                  |
| richards_super           | 94.7 ms                                                | 47.2 ms: 2.01x faster                                                 |
| chaos                    | 115 ms                                                 | 58.3 ms: 1.98x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 60.7 ms: 1.95x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 909 ms: 1.95x faster                                                  |
| richards                 | 79.3 ms                                                | 41.0 ms: 1.93x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 67.1 ms: 1.91x faster                                                 |
| scimark_sor              | 220 ms                                                 | 115 ms: 1.90x faster                                                  |
| raytrace                 | 507 ms                                                 | 267 ms: 1.90x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 497 ms: 1.86x faster                                                  |
| logging_silent           | 190 ns                                                 | 104 ns: 1.82x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 563 ms: 1.80x faster                                                  |
| nbody                    | 154 ms                                                 | 85.7 ms: 1.79x faster                                                 |
| deepcopy                 | 479 us                                                 | 271 us: 1.77x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.75x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.67x faster                                                 |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.67x faster                                                  |
| mako                     | 16.3 ms                                                | 9.79 ms: 1.67x faster                                                 |
| go                       | 240 ms                                                 | 145 ms: 1.65x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 293 us: 1.65x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.92 sec: 1.64x faster                                                |
| pyflate                  | 716 ms                                                 | 439 ms: 1.63x faster                                                  |
| scimark_lu               | 176 ms                                                 | 108 ms: 1.63x faster                                                  |
| float                    | 117 ms                                                 | 72.9 ms: 1.61x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.58x faster                                                 |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.55x faster                                                 |
| pylint                   | 551 ms                                                 | 356 ms: 1.55x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.72 ms: 1.55x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.54x faster                                                 |
| scimark_fft              | 466 ms                                                 | 302 ms: 1.54x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.54x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.54 us: 1.50x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.33 ms: 1.49x faster                                                 |
| logging_format           | 9.09 us                                                | 6.11 us: 1.49x faster                                                 |
| tornado_http             | 136 ms                                                 | 92.9 ms: 1.47x faster                                                 |
| fannkuch                 | 532 ms                                                 | 366 ms: 1.45x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 711 ms: 1.43x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                |
| regex_compile            | 188 ms                                                 | 133 ms: 1.42x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 56.2 ms: 1.41x faster                                                 |
| html5lib                 | 88.9 ms                                                | 64.3 ms: 1.38x faster                                                 |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                 |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                 |
| thrift                   | 1.07 ms                                                | 796 us: 1.35x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                |
| django_template          | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                 |
| genshi_text              | 31.8 ms                                                | 24.2 ms: 1.32x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.27x faster                                                  |
| 2to3                     | 348 ms                                                 | 274 ms: 1.27x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.26x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 52.9 ms: 1.25x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 79.8 ms: 1.25x faster                                                 |
| nqueens                  | 106 ms                                                 | 85.1 ms: 1.24x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 55.8 ms: 1.24x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 819 us: 1.20x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 99.5 ms: 1.16x faster                                                 |
| sympy_str                | 346 ms                                                 | 298 ms: 1.16x faster                                                  |
| sympy_sum                | 196 ms                                                 | 170 ms: 1.16x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 22.4 ms: 1.15x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                  |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.91 sec: 1.13x faster                                                |
| json                     | 5.69 ms                                                | 5.09 ms: 1.12x faster                                                 |
| sympy_expand             | 566 ms                                                 | 507 ms: 1.11x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.57 sec: 1.11x faster                                                |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.10x faster                                                 |
| json_loads               | 31.2 us                                                | 28.3 us: 1.10x faster                                                 |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                  |
| regex_dna                | 227 ms                                                 | 229 ms: 1.01x slower                                                  |
| async_generators         | 444 ms                                                 | 461 ms: 1.04x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 3.77 ms: 1.04x slower                                                 |
| regex_effbot             | 3.63 ms                                                | 3.90 ms: 1.07x slower                                                 |
| telco                    | 7.27 ms                                                | 7.81 ms: 1.07x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.77 ms: 1.09x slower                                                 |
| coverage                 | 79.4 ms                                                | 91.4 ms: 1.15x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.15 ms: 1.21x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240806-3.14.0a0-3a2f40c-JIT/bm-20240806-linux-x86_64-brandtbucher-replicate_more-3.14.0a0-3a2f40c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.19x