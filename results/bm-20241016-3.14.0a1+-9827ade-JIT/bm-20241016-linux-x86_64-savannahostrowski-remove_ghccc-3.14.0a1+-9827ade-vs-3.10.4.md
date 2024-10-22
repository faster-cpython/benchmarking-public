# Results vs. 3.10.4

- fork: savannahostrowski
- ref: remove_ghccc
- machine: linux-x86_64
- commit hash: 9827ade
- commit date: 2024-10-16
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 278 ms: 1.25x faster                                                      |
| docutils       | 3.30 sec                                               | 2.91 sec: 1.13x faster                                                    |
| html5lib       | 88.9 ms                                                | 65.5 ms: 1.36x faster                                                     |
| tornado_http   | 136 ms                                                 | 93.2 ms: 1.46x faster                                                     |
| Geometric mean | (ref)                                                  | 1.30x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.24x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 414 ms: 2.10x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 848 ms: 2.09x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 577 ms: 1.76x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.04x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.1 ms: 1.87x faster                                                     |
| float          | 117 ms                                                 | 75.9 ms: 1.54x faster                                                     |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.44x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 141 ms: 1.34x faster                                                      |
| regex_v8       | 27.8 ms                                                | 24.1 ms: 1.15x faster                                                     |
| regex_dna      | 227 ms                                                 | 208 ms: 1.09x faster                                                      |
| Geometric mean | (ref)                                                  | 1.14x faster                                                              |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 309 us: 1.57x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 55.5 ms: 1.42x faster                                                     |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.27x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 79.0 ms: 1.26x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 99.8 ms: 1.16x faster                                                     |
| json_loads           | 31.2 us                                                | 27.0 us: 1.16x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                                      |
| unpickle             | 14.4 us                                                | 14.7 us: 1.02x slower                                                     |
| pickle_list          | 5.08 us                                                | 5.28 us: 1.04x slower                                                     |
| unpickle_list        | 5.20 us                                                | 5.47 us: 1.05x slower                                                     |
| pickle               | 10.7 us                                                | 12.0 us: 1.13x slower                                                     |
| pickle_dict          | 29.6 us                                                | 35.9 us: 1.21x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.9 ms: 1.23x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.3 ms: 1.58x faster                                                     |
| django_template | 48.2 ms                                                | 36.3 ms: 1.33x faster                                                     |
| genshi_text     | 31.8 ms                                                | 26.1 ms: 1.22x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 61.7 ms: 1.07x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.29x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.27 ms: 2.42x faster                                                     |
| generators               | 80.1 ms                                                | 35.7 ms: 2.24x faster                                                     |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.24x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 414 ms: 2.10x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 848 ms: 2.09x faster                                                      |
| richards_super           | 94.7 ms                                                | 47.5 ms: 1.99x faster                                                     |
| chaos                    | 115 ms                                                 | 58.9 ms: 1.96x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 29.8 us: 1.96x faster                                                     |
| logging_silent           | 190 ns                                                 | 97.7 ns: 1.94x faster                                                     |
| richards                 | 79.3 ms                                                | 41.2 ms: 1.92x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 67.1 ms: 1.90x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 493 ms: 1.87x faster                                                      |
| nbody                    | 154 ms                                                 | 82.1 ms: 1.87x faster                                                     |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 65.1 ms: 1.81x faster                                                     |
| raytrace                 | 507 ms                                                 | 283 ms: 1.79x faster                                                      |
| go                       | 240 ms                                                 | 134 ms: 1.79x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 577 ms: 1.76x faster                                                      |
| deepcopy                 | 479 us                                                 | 274 us: 1.75x faster                                                      |
| comprehensions           | 28.8 us                                                | 17.3 us: 1.67x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.65x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                    |
| pyflate                  | 716 ms                                                 | 449 ms: 1.60x faster                                                      |
| mako                     | 16.3 ms                                                | 10.3 ms: 1.58x faster                                                     |
| scimark_lu               | 176 ms                                                 | 111 ms: 1.58x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 309 us: 1.57x faster                                                      |
| float                    | 117 ms                                                 | 75.9 ms: 1.54x faster                                                     |
| coroutines               | 35.1 ms                                                | 22.8 ms: 1.54x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.67 ms: 1.54x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.51 us: 1.51x faster                                                     |
| logging_format           | 9.09 us                                                | 6.09 us: 1.49x faster                                                     |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.48x faster                                                      |
| hexiom                   | 10.4 ms                                                | 7.06 ms: 1.47x faster                                                     |
| scimark_fft              | 466 ms                                                 | 317 ms: 1.47x faster                                                      |
| pylint                   | 551 ms                                                 | 376 ms: 1.47x faster                                                      |
| tornado_http             | 136 ms                                                 | 93.2 ms: 1.46x faster                                                     |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 55.5 ms: 1.42x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.41x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.61 ms: 1.40x faster                                                     |
| fannkuch                 | 532 ms                                                 | 385 ms: 1.38x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 739 ms: 1.38x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                    |
| html5lib                 | 88.9 ms                                                | 65.5 ms: 1.36x faster                                                     |
| regex_compile            | 188 ms                                                 | 141 ms: 1.34x faster                                                      |
| thrift                   | 1.07 ms                                                | 799 us: 1.34x faster                                                      |
| django_template          | 48.2 ms                                                | 36.3 ms: 1.33x faster                                                     |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                     |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.27x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 66.6 ms: 1.27x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 79.0 ms: 1.26x faster                                                     |
| 2to3                     | 348 ms                                                 | 278 ms: 1.25x faster                                                      |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.25x faster                                                      |
| python_startup           | 14.6 ms                                                | 11.9 ms: 1.23x faster                                                     |
| genshi_text              | 31.8 ms                                                | 26.1 ms: 1.22x faster                                                     |
| nqueens                  | 106 ms                                                 | 90.7 ms: 1.17x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 59.7 ms: 1.16x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 99.8 ms: 1.16x faster                                                     |
| json_loads               | 31.2 us                                                | 27.0 us: 1.16x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 24.1 ms: 1.15x faster                                                     |
| json                     | 5.69 ms                                                | 4.96 ms: 1.15x faster                                                     |
| sympy_str                | 346 ms                                                 | 302 ms: 1.14x faster                                                      |
| sympy_expand             | 566 ms                                                 | 498 ms: 1.14x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.91 sec: 1.13x faster                                                    |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 877 us: 1.13x faster                                                      |
| sympy_sum                | 196 ms                                                 | 175 ms: 1.12x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.59 sec: 1.10x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 23.5 ms: 1.10x faster                                                     |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.09x faster                                                      |
| regex_dna                | 227 ms                                                 | 208 ms: 1.09x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.78 us: 1.09x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 61.7 ms: 1.07x faster                                                     |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                      |
| unpickle                 | 14.4 us                                                | 14.7 us: 1.02x slower                                                     |
| async_generators         | 444 ms                                                 | 458 ms: 1.03x slower                                                      |
| pickle_list              | 5.08 us                                                | 5.28 us: 1.04x slower                                                     |
| telco                    | 7.27 ms                                                | 7.61 ms: 1.05x slower                                                     |
| unpickle_list            | 5.20 us                                                | 5.47 us: 1.05x slower                                                     |
| coverage                 | 79.4 ms                                                | 84.5 ms: 1.06x slower                                                     |
| pickle                   | 10.7 us                                                | 12.0 us: 1.13x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                     |
| pickle_dict              | 29.6 us                                                | 35.9 us: 1.21x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 4.80 ms: 1.32x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 2.68 ms: 1.65x slower                                                     |
| unpack_sequence          | 60.0 ns                                                | 110 ns: 1.83x slower                                                      |
| bench_mp_pool            | 24.0 ms                                                | 83.8 ms: 3.49x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.33x faster                                                              |

Benchmark hidden because not significant (2): asyncio_websockets, regex_effbot
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241016-3.14.0a1+-9827ade-JIT/bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.32x