# Results vs. 3.10.4

- fork: python
- ref: 9f9b00d52ceafab6c183
- machine: linux-x86_64
- commit hash: 9f9b00d
- commit date: 2024-08-26
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 277 ms: 1.26x faster                                                  |
| docutils       | 3.30 sec                                               | 3.06 sec: 1.08x faster                                                |
| html5lib       | 88.9 ms                                                | 67.2 ms: 1.32x faster                                                 |
| tornado_http   | 136 ms                                                 | 94.7 ms: 1.44x faster                                                 |
| Geometric mean | (ref)                                                  | 1.27x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 325 ms: 2.24x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 400 ms: 2.18x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 938 ms: 1.88x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 561 ms: 1.81x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.02x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.7 ms: 1.86x faster                                                 |
| float          | 117 ms                                                 | 70.2 ms: 1.67x faster                                                 |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.46x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 141 ms: 1.33x faster                                                  |
| regex_v8       | 27.8 ms                                                | 25.3 ms: 1.10x faster                                                 |
| regex_dna      | 227 ms                                                 | 219 ms: 1.03x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.72 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.92 sec: 1.63x faster                                                |
| pickle_pure_python   | 484 us                                                 | 302 us: 1.60x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 54.9 ms: 1.44x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.1 ms: 1.40x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 77.4 ms: 1.28x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 98.4 ms: 1.17x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                  |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.16 ms: 1.21x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.87 ms: 1.65x faster                                                 |
| django_template | 48.2 ms                                                | 36.6 ms: 1.31x faster                                                 |
| genshi_text     | 31.8 ms                                                | 24.4 ms: 1.30x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 55.9 ms: 1.18x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.31x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.20 ms: 2.47x faster                                                 |
| generators               | 80.1 ms                                                | 33.1 ms: 2.42x faster                                                 |
| async_tree_none          | 728 ms                                                 | 325 ms: 2.24x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 26.9 us: 2.18x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 400 ms: 2.18x faster                                                  |
| richards_super           | 94.7 ms                                                | 45.5 ms: 2.08x faster                                                 |
| richards                 | 79.3 ms                                                | 39.3 ms: 2.02x faster                                                 |
| chaos                    | 115 ms                                                 | 58.3 ms: 1.98x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 65.9 ms: 1.94x faster                                                 |
| scimark_sor              | 220 ms                                                 | 115 ms: 1.90x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 938 ms: 1.88x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 63.0 ms: 1.88x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 493 ms: 1.87x faster                                                  |
| logging_silent           | 190 ns                                                 | 102 ns: 1.87x faster                                                  |
| nbody                    | 154 ms                                                 | 82.7 ms: 1.86x faster                                                 |
| raytrace                 | 507 ms                                                 | 277 ms: 1.83x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 561 ms: 1.81x faster                                                  |
| deepcopy                 | 479 us                                                 | 266 us: 1.80x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                 |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.68x faster                                                  |
| float                    | 117 ms                                                 | 70.2 ms: 1.67x faster                                                 |
| mako                     | 16.3 ms                                                | 9.87 ms: 1.65x faster                                                 |
| pyflate                  | 716 ms                                                 | 436 ms: 1.64x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.92 sec: 1.63x faster                                                |
| scimark_lu               | 176 ms                                                 | 109 ms: 1.62x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.34 ms: 1.61x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.60x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.55x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.16 ms: 1.55x faster                                                 |
| scimark_fft              | 466 ms                                                 | 305 ms: 1.53x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                  |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.85 ms: 1.52x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.70 ms: 1.51x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.56 us: 1.49x faster                                                 |
| logging_format           | 9.09 us                                                | 6.11 us: 1.49x faster                                                 |
| pylint                   | 551 ms                                                 | 374 ms: 1.47x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 54.9 ms: 1.44x faster                                                 |
| tornado_http             | 136 ms                                                 | 94.7 ms: 1.44x faster                                                 |
| fannkuch                 | 532 ms                                                 | 370 ms: 1.44x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                |
| go                       | 240 ms                                                 | 171 ms: 1.40x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.1 ms: 1.40x faster                                                 |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 738 ms: 1.38x faster                                                  |
| thrift                   | 1.07 ms                                                | 789 us: 1.36x faster                                                  |
| regex_compile            | 188 ms                                                 | 141 ms: 1.33x faster                                                  |
| html5lib                 | 88.9 ms                                                | 67.2 ms: 1.32x faster                                                 |
| django_template          | 48.2 ms                                                | 36.6 ms: 1.31x faster                                                 |
| pathlib                  | 20.5 ms                                                | 15.7 ms: 1.30x faster                                                 |
| genshi_text              | 31.8 ms                                                | 24.4 ms: 1.30x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.22 sec: 1.29x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 77.4 ms: 1.28x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.26x faster                                                  |
| 2to3                     | 348 ms                                                 | 277 ms: 1.26x faster                                                  |
| nqueens                  | 106 ms                                                 | 86.7 ms: 1.22x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 822 us: 1.20x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 58.3 ms: 1.19x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 55.9 ms: 1.18x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 98.4 ms: 1.17x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                  |
| sympy_str                | 346 ms                                                 | 300 ms: 1.15x faster                                                  |
| meteor_contest           | 120 ms                                                 | 104 ms: 1.15x faster                                                  |
| sympy_sum                | 196 ms                                                 | 173 ms: 1.13x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 22.9 ms: 1.13x faster                                                 |
| sympy_expand             | 566 ms                                                 | 507 ms: 1.11x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 25.3 ms: 1.10x faster                                                 |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                 |
| docutils                 | 3.30 sec                                               | 3.06 sec: 1.08x faster                                                |
| json                     | 5.69 ms                                                | 5.31 ms: 1.07x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.69 sec: 1.06x faster                                                |
| regex_dna                | 227 ms                                                 | 219 ms: 1.03x faster                                                  |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.72 ms: 1.03x slower                                                 |
| async_generators         | 444 ms                                                 | 459 ms: 1.03x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 3.87 ms: 1.07x slower                                                 |
| coverage                 | 79.4 ms                                                | 85.2 ms: 1.07x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.77 ms: 1.09x slower                                                 |
| telco                    | 7.27 ms                                                | 8.01 ms: 1.10x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.16 ms: 1.21x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240826-3.14.0a0-9f9b00d-JIT/bm-20240826-linux-x86_64-python-9f9b00d52ceafab6c183-3.14.0a0-9f9b00d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.22x