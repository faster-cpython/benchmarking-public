# Results vs. 3.10.4

- fork: savannahostrowski
- ref: jit_mem_2
- machine: linux-x86_64
- commit hash: 6a9d428
- commit date: 2024-08-14
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 282 ms: 1.24x faster                                                  |
| docutils       | 3.30 sec                                               | 2.96 sec: 1.11x faster                                                |
| html5lib       | 88.9 ms                                                | 67.0 ms: 1.33x faster                                                 |
| tornado_http   | 136 ms                                                 | 94.5 ms: 1.44x faster                                                 |
| Geometric mean | (ref)                                                  | 1.27x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 330 ms: 2.21x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 432 ms: 2.01x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 917 ms: 1.93x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 572 ms: 1.78x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.97x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.3 ms: 1.91x faster                                                 |
| float          | 117 ms                                                 | 71.7 ms: 1.63x faster                                                 |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.48x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 142 ms: 1.33x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                 |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.69 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 298 us: 1.63x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                |
| unpickle_pure_python | 331 us                                                 | 211 us: 1.57x faster                                                  |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 98.7 ms: 1.17x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 85.3 ms: 1.17x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.14x faster                                                  |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.4 ms: 1.40x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.0 ms: 1.63x faster                                                 |
| django_template | 48.2 ms                                                | 36.8 ms: 1.31x faster                                                 |
| genshi_text     | 31.8 ms                                                | 24.6 ms: 1.29x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 56.3 ms: 1.17x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.21x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.11 ms: 2.54x faster                                                 |
| generators               | 80.1 ms                                                | 34.6 ms: 2.32x faster                                                 |
| async_tree_none          | 728 ms                                                 | 330 ms: 2.21x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 27.0 us: 2.16x faster                                                 |
| richards_super           | 94.7 ms                                                | 46.1 ms: 2.06x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 432 ms: 2.01x faster                                                  |
| chaos                    | 115 ms                                                 | 57.9 ms: 1.99x faster                                                 |
| richards                 | 79.3 ms                                                | 41.1 ms: 1.93x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 917 ms: 1.93x faster                                                  |
| raytrace                 | 507 ms                                                 | 264 ms: 1.92x faster                                                  |
| nbody                    | 154 ms                                                 | 80.3 ms: 1.91x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 62.1 ms: 1.90x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 493 ms: 1.87x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 68.6 ms: 1.86x faster                                                 |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                                  |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                                  |
| deepcopy                 | 479 us                                                 | 263 us: 1.82x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 572 ms: 1.78x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                 |
| spectral_norm            | 170 ms                                                 | 99.2 ms: 1.71x faster                                                 |
| go                       | 240 ms                                                 | 145 ms: 1.66x faster                                                  |
| float                    | 117 ms                                                 | 71.7 ms: 1.63x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                                 |
| mako                     | 16.3 ms                                                | 10.0 ms: 1.63x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 298 us: 1.63x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                |
| scimark_lu               | 176 ms                                                 | 110 ms: 1.60x faster                                                  |
| pyflate                  | 716 ms                                                 | 451 ms: 1.59x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 211 us: 1.57x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.54x faster                                                 |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                 |
| scimark_fft              | 466 ms                                                 | 305 ms: 1.53x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.24 ms: 1.52x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.70 ms: 1.52x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.86 ms: 1.52x faster                                                 |
| pylint                   | 551 ms                                                 | 365 ms: 1.51x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.62 us: 1.48x faster                                                 |
| logging_format           | 9.09 us                                                | 6.21 us: 1.46x faster                                                 |
| tornado_http             | 136 ms                                                 | 94.5 ms: 1.44x faster                                                 |
| fannkuch                 | 532 ms                                                 | 371 ms: 1.43x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                |
| python_startup           | 14.6 ms                                                | 10.4 ms: 1.40x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 729 ms: 1.40x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                                |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                 |
| thrift                   | 1.07 ms                                                | 788 us: 1.36x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                 |
| regex_compile            | 188 ms                                                 | 142 ms: 1.33x faster                                                  |
| html5lib                 | 88.9 ms                                                | 67.0 ms: 1.33x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                                |
| django_template          | 48.2 ms                                                | 36.8 ms: 1.31x faster                                                 |
| genshi_text              | 31.8 ms                                                | 24.6 ms: 1.29x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.27x faster                                                  |
| 2to3                     | 348 ms                                                 | 282 ms: 1.24x faster                                                  |
| nqueens                  | 106 ms                                                 | 87.7 ms: 1.21x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 821 us: 1.20x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 58.5 ms: 1.18x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 56.3 ms: 1.17x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 98.7 ms: 1.17x faster                                                 |
| sympy_str                | 346 ms                                                 | 296 ms: 1.17x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 85.3 ms: 1.17x faster                                                 |
| sympy_sum                | 196 ms                                                 | 171 ms: 1.15x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.14x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 22.7 ms: 1.14x faster                                                 |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                  |
| sympy_expand             | 566 ms                                                 | 501 ms: 1.13x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.55 sec: 1.12x faster                                                |
| docutils                 | 3.30 sec                                               | 2.96 sec: 1.11x faster                                                |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                 |
| json                     | 5.69 ms                                                | 5.33 ms: 1.07x faster                                                 |
| gc_traversal             | 3.62 ms                                                | 3.51 ms: 1.03x faster                                                 |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                  |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.69 ms: 1.02x slower                                                 |
| async_generators         | 444 ms                                                 | 457 ms: 1.03x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 1.73 ms: 1.07x slower                                                 |
| coverage                 | 79.4 ms                                                | 85.0 ms: 1.07x slower                                                 |
| telco                    | 7.27 ms                                                | 7.84 ms: 1.08x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240814-3.14.0a0-6a9d428-JIT/bm-20240814-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-6a9d428.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.18x