# Results vs. 3.10.4

- fork: savannahostrowski
- ref: jit_inv_mem_1m
- machine: linux-x86_64
- commit hash: 062c54f
- commit date: 2024-09-23
- overall geometric mean: 1.37x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 277 ms: 1.26x faster                                                       |
| docutils       | 3.30 sec                                               | 2.93 sec: 1.12x faster                                                     |
| html5lib       | 88.9 ms                                                | 64.3 ms: 1.38x faster                                                      |
| tornado_http   | 136 ms                                                 | 95.0 ms: 1.44x faster                                                      |
| Geometric mean | (ref)                                                  | 1.29x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 313 ms: 2.32x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 396 ms: 2.20x faster                                                       |
| async_tree_io           | 1.77 sec                                               | 858 ms: 2.06x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 570 ms: 1.78x faster                                                       |
| Geometric mean          | (ref)                                                  | 2.08x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 84.1 ms: 1.83x faster                                                      |
| float          | 117 ms                                                 | 69.6 ms: 1.68x faster                                                      |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.47x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 143 ms: 1.32x faster                                                       |
| regex_v8       | 27.8 ms                                                | 24.6 ms: 1.13x faster                                                      |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                                       |
| regex_effbot   | 3.63 ms                                                | 3.80 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                  | 1.10x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                     |
| pickle_pure_python   | 484 us                                                 | 304 us: 1.59x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 54.5 ms: 1.45x faster                                                      |
| json_dumps           | 14.2 ms                                                | 9.93 ms: 1.43x faster                                                      |
| xml_etree_generate   | 99.4 ms                                                | 77.8 ms: 1.28x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 98.4 ms: 1.17x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                       |
| json_loads           | 31.2 us                                                | 27.6 us: 1.13x faster                                                      |
| pickle_list          | 5.08 us                                                | 5.10 us: 1.00x slower                                                      |
| unpickle             | 14.4 us                                                | 14.5 us: 1.01x slower                                                      |
| unpickle_list        | 5.20 us                                                | 5.29 us: 1.02x slower                                                      |
| pickle               | 10.7 us                                                | 11.5 us: 1.08x slower                                                      |
| pickle_dict          | 29.6 us                                                | 34.5 us: 1.17x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                      |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.87 ms: 1.65x faster                                                      |
| django_template | 48.2 ms                                                | 36.7 ms: 1.31x faster                                                      |
| genshi_text     | 31.8 ms                                                | 24.9 ms: 1.28x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 58.7 ms: 1.13x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.28x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.23 ms: 2.45x faster                                                      |
| async_tree_none          | 728 ms                                                 | 313 ms: 2.32x faster                                                       |
| generators               | 80.1 ms                                                | 34.9 ms: 2.29x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 396 ms: 2.20x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 27.1 us: 2.16x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 858 ms: 2.06x faster                                                       |
| richards_super           | 94.7 ms                                                | 46.7 ms: 2.03x faster                                                      |
| chaos                    | 115 ms                                                 | 58.9 ms: 1.96x faster                                                      |
| richards                 | 79.3 ms                                                | 40.7 ms: 1.95x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 66.7 ms: 1.92x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 63.3 ms: 1.87x faster                                                      |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                                       |
| asyncio_tcp              | 922 ms                                                 | 496 ms: 1.86x faster                                                       |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                                       |
| raytrace                 | 507 ms                                                 | 276 ms: 1.84x faster                                                       |
| nbody                    | 154 ms                                                 | 84.1 ms: 1.83x faster                                                      |
| deepcopy                 | 479 us                                                 | 263 us: 1.82x faster                                                       |
| go                       | 240 ms                                                 | 134 ms: 1.80x faster                                                       |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 570 ms: 1.78x faster                                                       |
| comprehensions           | 28.8 us                                                | 16.9 us: 1.71x faster                                                      |
| float                    | 117 ms                                                 | 69.6 ms: 1.68x faster                                                      |
| mako                     | 16.3 ms                                                | 9.87 ms: 1.65x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                     |
| spectral_norm            | 170 ms                                                 | 105 ms: 1.62x faster                                                       |
| scimark_lu               | 176 ms                                                 | 111 ms: 1.59x faster                                                       |
| pickle_pure_python       | 484 us                                                 | 304 us: 1.59x faster                                                       |
| pyflate                  | 716 ms                                                 | 454 ms: 1.58x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.56x faster                                                      |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.26 ms: 1.52x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.70 ms: 1.52x faster                                                      |
| scimark_fft              | 466 ms                                                 | 312 ms: 1.49x faster                                                       |
| hexiom                   | 10.4 ms                                                | 6.97 ms: 1.49x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.59 us: 1.49x faster                                                      |
| logging_format           | 9.09 us                                                | 6.15 us: 1.48x faster                                                      |
| pylint                   | 551 ms                                                 | 378 ms: 1.46x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 54.5 ms: 1.45x faster                                                      |
| tornado_http             | 136 ms                                                 | 95.0 ms: 1.44x faster                                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                     |
| json_dumps               | 14.2 ms                                                | 9.93 ms: 1.43x faster                                                      |
| fannkuch                 | 532 ms                                                 | 379 ms: 1.40x faster                                                       |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.38x faster                                                     |
| html5lib                 | 88.9 ms                                                | 64.3 ms: 1.38x faster                                                      |
| thrift                   | 1.07 ms                                                | 782 us: 1.37x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 745 ms: 1.37x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                                     |
| regex_compile            | 188 ms                                                 | 143 ms: 1.32x faster                                                       |
| django_template          | 48.2 ms                                                | 36.7 ms: 1.31x faster                                                      |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                      |
| genshi_text              | 31.8 ms                                                | 24.9 ms: 1.28x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 77.8 ms: 1.28x faster                                                      |
| 2to3                     | 348 ms                                                 | 277 ms: 1.26x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.26x faster                                                       |
| dulwich_log              | 84.3 ms                                                | 68.2 ms: 1.24x faster                                                      |
| nqueens                  | 106 ms                                                 | 89.0 ms: 1.19x faster                                                      |
| sqlglot_optimize         | 69.2 ms                                                | 58.6 ms: 1.18x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 839 us: 1.18x faster                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 98.4 ms: 1.17x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                       |
| sympy_str                | 346 ms                                                 | 305 ms: 1.13x faster                                                       |
| json_loads               | 31.2 us                                                | 27.6 us: 1.13x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 24.6 ms: 1.13x faster                                                      |
| sympy_sum                | 196 ms                                                 | 174 ms: 1.13x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 58.7 ms: 1.13x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.93 sec: 1.12x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 23.0 ms: 1.12x faster                                                      |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.59 sec: 1.10x faster                                                     |
| sympy_expand             | 566 ms                                                 | 514 ms: 1.10x faster                                                       |
| sqlite_synth             | 3.02 us                                                | 2.75 us: 1.10x faster                                                      |
| json                     | 5.69 ms                                                | 5.21 ms: 1.09x faster                                                      |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                                       |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                       |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                       |
| pickle_list              | 5.08 us                                                | 5.10 us: 1.00x slower                                                      |
| unpickle                 | 14.4 us                                                | 14.5 us: 1.01x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 3.66 ms: 1.01x slower                                                      |
| unpickle_list            | 5.20 us                                                | 5.29 us: 1.02x slower                                                      |
| async_generators         | 444 ms                                                 | 459 ms: 1.03x slower                                                       |
| regex_effbot             | 3.63 ms                                                | 3.80 ms: 1.05x slower                                                      |
| coverage                 | 79.4 ms                                                | 85.0 ms: 1.07x slower                                                      |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.07x slower                                                      |
| pickle                   | 10.7 us                                                | 11.5 us: 1.08x slower                                                      |
| telco                    | 7.27 ms                                                | 8.08 ms: 1.11x slower                                                      |
| pickle_dict              | 29.6 us                                                | 34.5 us: 1.17x slower                                                      |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                      |
| unpack_sequence          | 60.0 ns                                                | 105 ns: 1.75x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                               |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240923-3.14.0a0-062c54f-JIT/bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.19x