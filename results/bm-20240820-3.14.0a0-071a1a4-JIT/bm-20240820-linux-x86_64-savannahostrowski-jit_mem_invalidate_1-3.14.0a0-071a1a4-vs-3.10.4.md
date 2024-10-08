# Results vs. 3.10.4

- fork: savannahostrowski
- ref: jit_mem_invalidate_1
- machine: linux-x86_64
- commit hash: 071a1a4
- commit date: 2024-08-20
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 280 ms: 1.25x faster                                                             |
| docutils       | 3.30 sec                                               | 2.97 sec: 1.11x faster                                                           |
| html5lib       | 88.9 ms                                                | 67.2 ms: 1.32x faster                                                            |
| tornado_http   | 136 ms                                                 | 93.2 ms: 1.46x faster                                                            |
| Geometric mean | (ref)                                                  | 1.28x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 321 ms: 2.27x faster                                                             |
| async_tree_memoization  | 870 ms                                                 | 427 ms: 2.04x faster                                                             |
| async_tree_io           | 1.77 sec                                               | 900 ms: 1.97x faster                                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 562 ms: 1.81x faster                                                             |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.9 ms: 1.92x faster                                                            |
| float          | 117 ms                                                 | 72.1 ms: 1.62x faster                                                            |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                  | 1.47x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 141 ms: 1.33x faster                                                             |
| regex_v8       | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                            |
| regex_dna      | 227 ms                                                 | 218 ms: 1.04x faster                                                             |
| regex_effbot   | 3.63 ms                                                | 3.56 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.88 sec: 1.67x faster                                                           |
| pickle_pure_python   | 484 us                                                 | 302 us: 1.60x faster                                                             |
| unpickle_pure_python | 331 us                                                 | 212 us: 1.56x faster                                                             |
| xml_etree_process    | 79.1 ms                                                | 58.0 ms: 1.36x faster                                                            |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 82.6 ms: 1.20x faster                                                            |
| xml_etree_iterparse  | 115 ms                                                 | 98.4 ms: 1.17x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.13x faster                                                             |
| json_loads           | 31.2 us                                                | 28.7 us: 1.09x faster                                                            |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                            |
| python_startup_no_site | 5.93 ms                                                | 7.13 ms: 1.20x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.88 ms: 1.65x faster                                                            |
| django_template | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                            |
| genshi_text     | 31.8 ms                                                | 26.2 ms: 1.22x faster                                                            |
| genshi_xml      | 66.0 ms                                                | 62.0 ms: 1.07x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.30x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 171 us: 3.18x faster                                                             |
| deltablue                | 7.91 ms                                                | 3.14 ms: 2.52x faster                                                            |
| generators               | 80.1 ms                                                | 33.6 ms: 2.38x faster                                                            |
| async_tree_none          | 728 ms                                                 | 321 ms: 2.27x faster                                                             |
| deepcopy_memo            | 58.5 us                                                | 26.3 us: 2.22x faster                                                            |
| richards_super           | 94.7 ms                                                | 45.4 ms: 2.09x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 427 ms: 2.04x faster                                                             |
| richards                 | 79.3 ms                                                | 39.1 ms: 2.03x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 900 ms: 1.97x faster                                                             |
| crypto_pyaes             | 128 ms                                                 | 65.7 ms: 1.95x faster                                                            |
| chaos                    | 115 ms                                                 | 59.4 ms: 1.94x faster                                                            |
| logging_silent           | 190 ns                                                 | 98.5 ns: 1.93x faster                                                            |
| nbody                    | 154 ms                                                 | 79.9 ms: 1.92x faster                                                            |
| scimark_sor              | 220 ms                                                 | 115 ms: 1.91x faster                                                             |
| raytrace                 | 507 ms                                                 | 266 ms: 1.91x faster                                                             |
| scimark_monte_carlo      | 118 ms                                                 | 62.1 ms: 1.90x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 495 ms: 1.86x faster                                                             |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                                             |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 562 ms: 1.81x faster                                                             |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.73x faster                                                            |
| spectral_norm            | 170 ms                                                 | 100 ms: 1.69x faster                                                             |
| tomli_loads              | 3.14 sec                                               | 1.88 sec: 1.67x faster                                                           |
| go                       | 240 ms                                                 | 144 ms: 1.66x faster                                                             |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.65x faster                                                            |
| mako                     | 16.3 ms                                                | 9.88 ms: 1.65x faster                                                            |
| pyflate                  | 716 ms                                                 | 434 ms: 1.65x faster                                                             |
| float                    | 117 ms                                                 | 72.1 ms: 1.62x faster                                                            |
| scimark_lu               | 176 ms                                                 | 109 ms: 1.62x faster                                                             |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.60x faster                                                             |
| deepcopy_reduce          | 4.17 us                                                | 2.64 us: 1.58x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 212 us: 1.56x faster                                                             |
| sqlglot_transpile        | 2.57 ms                                                | 1.67 ms: 1.54x faster                                                            |
| logging_simple           | 8.30 us                                                | 5.41 us: 1.53x faster                                                            |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                                            |
| scimark_fft              | 466 ms                                                 | 308 ms: 1.51x faster                                                             |
| logging_format           | 9.09 us                                                | 6.03 us: 1.51x faster                                                            |
| hexiom                   | 10.4 ms                                                | 6.90 ms: 1.51x faster                                                            |
| pylint                   | 551 ms                                                 | 367 ms: 1.50x faster                                                             |
| tornado_http             | 136 ms                                                 | 93.2 ms: 1.46x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.46 ms: 1.45x faster                                                            |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.43x faster                                                           |
| fannkuch                 | 532 ms                                                 | 377 ms: 1.41x faster                                                             |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                           |
| pprint_safe_repr         | 1.02 sec                                               | 733 ms: 1.39x faster                                                             |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                            |
| thrift                   | 1.07 ms                                                | 785 us: 1.36x faster                                                             |
| xml_etree_process        | 79.1 ms                                                | 58.0 ms: 1.36x faster                                                            |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                            |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                           |
| regex_compile            | 188 ms                                                 | 141 ms: 1.33x faster                                                             |
| django_template          | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                            |
| html5lib                 | 88.9 ms                                                | 67.2 ms: 1.32x faster                                                            |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                            |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.26x faster                                                             |
| 2to3                     | 348 ms                                                 | 280 ms: 1.25x faster                                                             |
| nqueens                  | 106 ms                                                 | 85.2 ms: 1.24x faster                                                            |
| genshi_text              | 31.8 ms                                                | 26.2 ms: 1.22x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 816 us: 1.21x faster                                                             |
| xml_etree_generate       | 99.4 ms                                                | 82.6 ms: 1.20x faster                                                            |
| sqlglot_optimize         | 69.2 ms                                                | 57.8 ms: 1.20x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 98.4 ms: 1.17x faster                                                            |
| sympy_str                | 346 ms                                                 | 304 ms: 1.14x faster                                                             |
| regex_v8                 | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.13x faster                                                             |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                             |
| sympy_integrate          | 25.8 ms                                                | 23.1 ms: 1.12x faster                                                            |
| sympy_sum                | 196 ms                                                 | 177 ms: 1.11x faster                                                             |
| docutils                 | 3.30 sec                                               | 2.97 sec: 1.11x faster                                                           |
| sympy_expand             | 566 ms                                                 | 510 ms: 1.11x faster                                                             |
| json_loads               | 31.2 us                                                | 28.7 us: 1.09x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 62.0 ms: 1.07x faster                                                            |
| json                     | 5.69 ms                                                | 5.34 ms: 1.07x faster                                                            |
| mdp                      | 2.85 sec                                               | 2.68 sec: 1.06x faster                                                           |
| regex_dna                | 227 ms                                                 | 218 ms: 1.04x faster                                                             |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                             |
| regex_effbot             | 3.63 ms                                                | 3.56 ms: 1.02x faster                                                            |
| async_generators         | 444 ms                                                 | 456 ms: 1.03x slower                                                             |
| gc_traversal             | 3.62 ms                                                | 3.75 ms: 1.03x slower                                                            |
| telco                    | 7.27 ms                                                | 7.76 ms: 1.07x slower                                                            |
| create_gc_cycles         | 1.62 ms                                                | 1.73 ms: 1.07x slower                                                            |
| coverage                 | 79.4 ms                                                | 86.0 ms: 1.08x slower                                                            |
| python_startup_no_site   | 5.93 ms                                                | 7.13 ms: 1.20x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                                     |

Benchmark hidden because not significant (2): bench_mp_pool, asyncio_websockets
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240820-3.14.0a0-071a1a4-JIT/bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_1-3.14.0a0-071a1a4.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.19x