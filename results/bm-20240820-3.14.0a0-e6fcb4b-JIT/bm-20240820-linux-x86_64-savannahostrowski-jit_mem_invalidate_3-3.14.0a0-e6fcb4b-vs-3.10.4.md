# Results vs. 3.10.4

- fork: savannahostrowski
- ref: jit_mem_invalidate_3
- machine: linux-x86_64
- commit hash: e6fcb4b
- commit date: 2024-08-20
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 280 ms: 1.24x faster                                                             |
| docutils       | 3.30 sec                                               | 2.97 sec: 1.11x faster                                                           |
| html5lib       | 88.9 ms                                                | 66.2 ms: 1.34x faster                                                            |
| tornado_http   | 136 ms                                                 | 93.6 ms: 1.46x faster                                                            |
| Geometric mean | (ref)                                                  | 1.28x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 324 ms: 2.25x faster                                                             |
| async_tree_memoization  | 870 ms                                                 | 422 ms: 2.06x faster                                                             |
| async_tree_io           | 1.77 sec                                               | 899 ms: 1.97x faster                                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 561 ms: 1.81x faster                                                             |
| Geometric mean          | (ref)                                                  | 2.02x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.7 ms: 1.88x faster                                                            |
| float          | 117 ms                                                 | 72.1 ms: 1.62x faster                                                            |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                  | 1.46x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 143 ms: 1.32x faster                                                             |
| regex_v8       | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                            |
| regex_dna      | 227 ms                                                 | 219 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.89 sec: 1.66x faster                                                           |
| pickle_pure_python   | 484 us                                                 | 302 us: 1.60x faster                                                             |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                                             |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 59.1 ms: 1.34x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 82.4 ms: 1.21x faster                                                            |
| xml_etree_iterparse  | 115 ms                                                 | 98.9 ms: 1.17x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                             |
| json_loads           | 31.2 us                                                | 28.4 us: 1.10x faster                                                            |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                            |
| python_startup_no_site | 5.93 ms                                                | 7.15 ms: 1.21x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.0 ms: 1.63x faster                                                            |
| django_template | 48.2 ms                                                | 36.0 ms: 1.34x faster                                                            |
| genshi_text     | 31.8 ms                                                | 26.8 ms: 1.19x faster                                                            |
| genshi_xml      | 66.0 ms                                                | 60.9 ms: 1.08x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.29x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 171 us: 3.19x faster                                                             |
| deltablue                | 7.91 ms                                                | 3.18 ms: 2.49x faster                                                            |
| generators               | 80.1 ms                                                | 33.5 ms: 2.39x faster                                                            |
| async_tree_none          | 728 ms                                                 | 324 ms: 2.25x faster                                                             |
| deepcopy_memo            | 58.5 us                                                | 26.6 us: 2.20x faster                                                            |
| richards_super           | 94.7 ms                                                | 45.1 ms: 2.10x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 422 ms: 2.06x faster                                                             |
| richards                 | 79.3 ms                                                | 39.0 ms: 2.03x faster                                                            |
| chaos                    | 115 ms                                                 | 58.2 ms: 1.98x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 899 ms: 1.97x faster                                                             |
| crypto_pyaes             | 128 ms                                                 | 65.3 ms: 1.96x faster                                                            |
| scimark_sor              | 220 ms                                                 | 114 ms: 1.92x faster                                                             |
| raytrace                 | 507 ms                                                 | 267 ms: 1.90x faster                                                             |
| logging_silent           | 190 ns                                                 | 100.0 ns: 1.90x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 62.5 ms: 1.89x faster                                                            |
| nbody                    | 154 ms                                                 | 81.7 ms: 1.88x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 496 ms: 1.86x faster                                                             |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 561 ms: 1.81x faster                                                             |
| deepcopy                 | 479 us                                                 | 266 us: 1.80x faster                                                             |
| spectral_norm            | 170 ms                                                 | 97.4 ms: 1.74x faster                                                            |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.74x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 1.89 sec: 1.66x faster                                                           |
| pyflate                  | 716 ms                                                 | 432 ms: 1.66x faster                                                             |
| go                       | 240 ms                                                 | 145 ms: 1.65x faster                                                             |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.64x faster                                                            |
| mako                     | 16.3 ms                                                | 10.0 ms: 1.63x faster                                                            |
| float                    | 117 ms                                                 | 72.1 ms: 1.62x faster                                                            |
| scimark_lu               | 176 ms                                                 | 109 ms: 1.62x faster                                                             |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.60x faster                                                             |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                                             |
| coroutines               | 35.1 ms                                                | 22.8 ms: 1.54x faster                                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.68 ms: 1.53x faster                                                            |
| logging_simple           | 8.30 us                                                | 5.46 us: 1.52x faster                                                            |
| scimark_fft              | 466 ms                                                 | 306 ms: 1.52x faster                                                             |
| hexiom                   | 10.4 ms                                                | 6.84 ms: 1.52x faster                                                            |
| logging_format           | 9.09 us                                                | 6.01 us: 1.51x faster                                                            |
| pylint                   | 551 ms                                                 | 368 ms: 1.50x faster                                                             |
| tornado_http             | 136 ms                                                 | 93.6 ms: 1.46x faster                                                            |
| fannkuch                 | 532 ms                                                 | 368 ms: 1.44x faster                                                             |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.50 ms: 1.44x faster                                                            |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.40x faster                                                           |
| pprint_safe_repr         | 1.02 sec                                               | 730 ms: 1.40x faster                                                             |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                            |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                            |
| thrift                   | 1.07 ms                                                | 793 us: 1.35x faster                                                             |
| html5lib                 | 88.9 ms                                                | 66.2 ms: 1.34x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 59.1 ms: 1.34x faster                                                            |
| django_template          | 48.2 ms                                                | 36.0 ms: 1.34x faster                                                            |
| regex_compile            | 188 ms                                                 | 143 ms: 1.32x faster                                                             |
| pycparser                | 1.58 sec                                               | 1.22 sec: 1.29x faster                                                           |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                            |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.27x faster                                                             |
| 2to3                     | 348 ms                                                 | 280 ms: 1.24x faster                                                             |
| nqueens                  | 106 ms                                                 | 86.3 ms: 1.23x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 817 us: 1.21x faster                                                             |
| xml_etree_generate       | 99.4 ms                                                | 82.4 ms: 1.21x faster                                                            |
| sqlglot_optimize         | 69.2 ms                                                | 57.7 ms: 1.20x faster                                                            |
| genshi_text              | 31.8 ms                                                | 26.8 ms: 1.19x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 98.9 ms: 1.17x faster                                                            |
| sympy_str                | 346 ms                                                 | 300 ms: 1.15x faster                                                             |
| regex_v8                 | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                             |
| sympy_sum                | 196 ms                                                 | 173 ms: 1.14x faster                                                             |
| sympy_integrate          | 25.8 ms                                                | 22.8 ms: 1.13x faster                                                            |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                             |
| sympy_expand             | 566 ms                                                 | 508 ms: 1.11x faster                                                             |
| docutils                 | 3.30 sec                                               | 2.97 sec: 1.11x faster                                                           |
| json_loads               | 31.2 us                                                | 28.4 us: 1.10x faster                                                            |
| mdp                      | 2.85 sec                                               | 2.60 sec: 1.09x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 60.9 ms: 1.08x faster                                                            |
| json                     | 5.69 ms                                                | 5.40 ms: 1.05x faster                                                            |
| regex_dna                | 227 ms                                                 | 219 ms: 1.03x faster                                                             |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                             |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                             |
| gc_traversal             | 3.62 ms                                                | 3.67 ms: 1.01x slower                                                            |
| async_generators         | 444 ms                                                 | 463 ms: 1.04x slower                                                             |
| create_gc_cycles         | 1.62 ms                                                | 1.72 ms: 1.06x slower                                                            |
| telco                    | 7.27 ms                                                | 7.84 ms: 1.08x slower                                                            |
| coverage                 | 79.4 ms                                                | 86.0 ms: 1.08x slower                                                            |
| python_startup_no_site   | 5.93 ms                                                | 7.15 ms: 1.21x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                                     |

Benchmark hidden because not significant (2): bench_mp_pool, regex_effbot
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240820-3.14.0a0-e6fcb4b-JIT/bm-20240820-linux-x86_64-savannahostrowski-jit_mem_invalidate_3-3.14.0a0-e6fcb4b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.20x