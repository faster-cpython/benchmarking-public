# Results vs. 3.10.4

- fork: savannahostrowski
- ref: jit_inv_cold_10k
- machine: linux-x86_64
- commit hash: 14c70a7
- commit date: 2024-09-19
- overall geometric mean: 1.36x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 285 ms: 1.22x faster                                                         |
| docutils       | 3.30 sec                                               | 2.88 sec: 1.15x faster                                                       |
| html5lib       | 88.9 ms                                                | 63.9 ms: 1.39x faster                                                        |
| tornado_http   | 136 ms                                                 | 95.5 ms: 1.43x faster                                                        |
| Geometric mean | (ref)                                                  | 1.29x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 321 ms: 2.27x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 395 ms: 2.20x faster                                                         |
| async_tree_io           | 1.77 sec                                               | 883 ms: 2.00x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 558 ms: 1.82x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.07x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.7 ms: 1.93x faster                                                        |
| float          | 117 ms                                                 | 71.5 ms: 1.64x faster                                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.48x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 139 ms: 1.35x faster                                                         |
| regex_v8       | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                        |
| regex_dna      | 227 ms                                                 | 215 ms: 1.05x faster                                                         |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                       |
| pickle_pure_python   | 484 us                                                 | 306 us: 1.58x faster                                                         |
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 55.5 ms: 1.43x faster                                                        |
| json_dumps           | 14.2 ms                                                | 10.1 ms: 1.40x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 79.8 ms: 1.25x faster                                                        |
| json_loads           | 31.2 us                                                | 26.8 us: 1.17x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 99.4 ms: 1.16x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 145 ms: 1.16x faster                                                         |
| pickle_list          | 5.08 us                                                | 5.00 us: 1.02x faster                                                        |
| unpickle             | 14.4 us                                                | 14.7 us: 1.02x slower                                                        |
| unpickle_list        | 5.20 us                                                | 5.31 us: 1.02x slower                                                        |
| pickle               | 10.7 us                                                | 11.7 us: 1.10x slower                                                        |
| pickle_dict          | 29.6 us                                                | 33.4 us: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.0 ms: 1.63x faster                                                        |
| django_template | 48.2 ms                                                | 35.4 ms: 1.36x faster                                                        |
| genshi_text     | 31.8 ms                                                | 25.5 ms: 1.25x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 61.0 ms: 1.08x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.31x faster                                                         |
| async_tree_none          | 728 ms                                                 | 321 ms: 2.27x faster                                                         |
| generators               | 80.1 ms                                                | 36.2 ms: 2.21x faster                                                        |
| async_tree_memoization   | 870 ms                                                 | 395 ms: 2.20x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 27.1 us: 2.16x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.68 ms: 2.15x faster                                                        |
| richards_super           | 94.7 ms                                                | 47.0 ms: 2.02x faster                                                        |
| async_tree_io            | 1.77 sec                                               | 883 ms: 2.00x faster                                                         |
| chaos                    | 115 ms                                                 | 59.6 ms: 1.94x faster                                                        |
| nbody                    | 154 ms                                                 | 79.7 ms: 1.93x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 61.9 ms: 1.91x faster                                                        |
| asyncio_tcp              | 922 ms                                                 | 491 ms: 1.88x faster                                                         |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 68.2 ms: 1.87x faster                                                        |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                                         |
| richards                 | 79.3 ms                                                | 43.5 ms: 1.82x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 558 ms: 1.82x faster                                                         |
| deepcopy                 | 479 us                                                 | 265 us: 1.81x faster                                                         |
| raytrace                 | 507 ms                                                 | 281 ms: 1.80x faster                                                         |
| go                       | 240 ms                                                 | 137 ms: 1.75x faster                                                         |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.72x faster                                                        |
| float                    | 117 ms                                                 | 71.5 ms: 1.64x faster                                                        |
| mako                     | 16.3 ms                                                | 10.0 ms: 1.63x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.34 ms: 1.62x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.63 us: 1.59x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 306 us: 1.58x faster                                                         |
| pyflate                  | 716 ms                                                 | 456 ms: 1.57x faster                                                         |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                         |
| sqlglot_transpile        | 2.57 ms                                                | 1.69 ms: 1.52x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                                         |
| scimark_fft              | 466 ms                                                 | 309 ms: 1.51x faster                                                         |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.50x faster                                                         |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.67 us: 1.46x faster                                                        |
| logging_format           | 9.09 us                                                | 6.28 us: 1.45x faster                                                        |
| pylint                   | 551 ms                                                 | 382 ms: 1.44x faster                                                         |
| tornado_http             | 136 ms                                                 | 95.5 ms: 1.43x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 55.5 ms: 1.43x faster                                                        |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.42x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.56 ms: 1.42x faster                                                        |
| json_dumps               | 14.2 ms                                                | 10.1 ms: 1.40x faster                                                        |
| html5lib                 | 88.9 ms                                                | 63.9 ms: 1.39x faster                                                        |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                        |
| fannkuch                 | 532 ms                                                 | 386 ms: 1.38x faster                                                         |
| pprint_safe_repr         | 1.02 sec                                               | 742 ms: 1.37x faster                                                         |
| django_template          | 48.2 ms                                                | 35.4 ms: 1.36x faster                                                        |
| thrift                   | 1.07 ms                                                | 790 us: 1.36x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.55 sec: 1.36x faster                                                       |
| regex_compile            | 188 ms                                                 | 139 ms: 1.35x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.33x faster                                                       |
| hexiom                   | 10.4 ms                                                | 7.89 ms: 1.32x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                        |
| genshi_text              | 31.8 ms                                                | 25.5 ms: 1.25x faster                                                        |
| xml_etree_generate       | 99.4 ms                                                | 79.8 ms: 1.25x faster                                                        |
| sqlglot_normalize        | 143 ms                                                 | 116 ms: 1.23x faster                                                         |
| 2to3                     | 348 ms                                                 | 285 ms: 1.22x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 68.9 ms: 1.22x faster                                                        |
| nqueens                  | 106 ms                                                 | 88.1 ms: 1.20x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 841 us: 1.17x faster                                                         |
| json_loads               | 31.2 us                                                | 26.8 us: 1.17x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 99.4 ms: 1.16x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 145 ms: 1.16x faster                                                         |
| docutils                 | 3.30 sec                                               | 2.88 sec: 1.15x faster                                                       |
| sympy_sum                | 196 ms                                                 | 173 ms: 1.14x faster                                                         |
| json                     | 5.69 ms                                                | 5.02 ms: 1.13x faster                                                        |
| sympy_str                | 346 ms                                                 | 306 ms: 1.13x faster                                                         |
| sympy_expand             | 566 ms                                                 | 505 ms: 1.12x faster                                                         |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.74 us: 1.10x faster                                                        |
| mdp                      | 2.85 sec                                               | 2.62 sec: 1.09x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                        |
| sqlglot_optimize         | 69.2 ms                                                | 63.7 ms: 1.09x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 61.0 ms: 1.08x faster                                                        |
| regex_dna                | 227 ms                                                 | 215 ms: 1.05x faster                                                         |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| pickle_list              | 5.08 us                                                | 5.00 us: 1.02x faster                                                        |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.01x faster                                                         |
| unpickle                 | 14.4 us                                                | 14.7 us: 1.02x slower                                                        |
| unpickle_list            | 5.20 us                                                | 5.31 us: 1.02x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 3.71 ms: 1.02x slower                                                        |
| sympy_integrate          | 25.8 ms                                                | 26.5 ms: 1.03x slower                                                        |
| async_generators         | 444 ms                                                 | 460 ms: 1.04x slower                                                         |
| create_gc_cycles         | 1.62 ms                                                | 1.72 ms: 1.06x slower                                                        |
| coverage                 | 79.4 ms                                                | 85.3 ms: 1.07x slower                                                        |
| pickle                   | 10.7 us                                                | 11.7 us: 1.10x slower                                                        |
| telco                    | 7.27 ms                                                | 8.10 ms: 1.11x slower                                                        |
| pickle_dict              | 29.6 us                                                | 33.4 us: 1.13x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                        |
| unpack_sequence          | 60.0 ns                                                | 109 ns: 1.82x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.36x faster                                                                 |

Benchmark hidden because not significant (2): bench_mp_pool, regex_effbot
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240919-3.14.0a0-14c70a7-JIT/bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-14c70a7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.16x