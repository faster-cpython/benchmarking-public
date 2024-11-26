# Results vs. 3.10.4

- fork: brandtbucher
- ref: warmup_4096
- machine: linux-x86_64
- commit hash: a2be6fd
- commit date: 2024-11-11
- overall geometric mean: 1.401x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 262 ms: 1.33x faster                                                |
| docutils       | 3.30 sec                                               | 2.89 sec: 1.14x faster                                              |
| html5lib       | 88.9 ms                                                | 66.7 ms: 1.33x faster                                               |
| Geometric mean | (ref)                                                  | 1.26x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 329 ms: 2.21x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 414 ms: 2.10x faster                                                |
| async_tree_io           | 1.77 sec                                               | 860 ms: 2.06x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 567 ms: 1.79x faster                                                |
| Geometric mean          | (ref)                                                  | 2.03x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 83.4 ms: 1.84x faster                                               |
| float          | 117 ms                                                 | 76.3 ms: 1.54x faster                                               |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.43x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 134 ms: 1.41x faster                                                |
| regex_v8       | 27.8 ms                                                | 24.6 ms: 1.13x faster                                               |
| regex_dna      | 227 ms                                                 | 211 ms: 1.07x faster                                                |
| Geometric mean | (ref)                                                  | 1.14x faster                                                        |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 193 us: 1.72x faster                                                |
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                              |
| pickle_pure_python   | 484 us                                                 | 323 us: 1.50x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 56.9 ms: 1.39x faster                                               |
| json_dumps           | 14.2 ms                                                | 10.9 ms: 1.31x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 81.7 ms: 1.22x faster                                               |
| json_loads           | 31.2 us                                                | 26.7 us: 1.17x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.14x faster                                                |
| xml_etree_parse      | 168 ms                                                 | 157 ms: 1.07x faster                                                |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.7 ms: 1.15x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                               |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.3 ms: 1.58x faster                                               |
| django_template | 48.2 ms                                                | 36.2 ms: 1.33x faster                                               |
| genshi_text     | 31.8 ms                                                | 24.8 ms: 1.28x faster                                               |
| genshi_xml      | 66.0 ms                                                | 58.4 ms: 1.13x faster                                               |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.23x faster                                                |
| deltablue                | 7.91 ms                                                | 3.29 ms: 2.41x faster                                               |
| richards_super           | 94.7 ms                                                | 42.2 ms: 2.24x faster                                               |
| generators               | 80.1 ms                                                | 36.0 ms: 2.23x faster                                               |
| async_tree_none          | 728 ms                                                 | 329 ms: 2.21x faster                                                |
| richards                 | 79.3 ms                                                | 37.3 ms: 2.12x faster                                               |
| async_tree_memoization   | 870 ms                                                 | 414 ms: 2.10x faster                                                |
| async_tree_io            | 1.77 sec                                               | 860 ms: 2.06x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 29.5 us: 1.98x faster                                               |
| chaos                    | 115 ms                                                 | 60.1 ms: 1.92x faster                                               |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 68.3 ms: 1.87x faster                                               |
| nbody                    | 154 ms                                                 | 83.4 ms: 1.84x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 64.4 ms: 1.84x faster                                               |
| raytrace                 | 507 ms                                                 | 276 ms: 1.84x faster                                                |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                |
| go                       | 240 ms                                                 | 133 ms: 1.81x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 567 ms: 1.79x faster                                                |
| deepcopy                 | 479 us                                                 | 268 us: 1.79x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 193 us: 1.72x faster                                                |
| comprehensions           | 28.8 us                                                | 17.5 us: 1.65x faster                                               |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.64x faster                                               |
| pylint                   | 551 ms                                                 | 342 ms: 1.61x faster                                                |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                              |
| pyflate                  | 716 ms                                                 | 451 ms: 1.59x faster                                                |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.58x faster                                               |
| mako                     | 16.3 ms                                                | 10.3 ms: 1.58x faster                                               |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.54x faster                                                |
| float                    | 117 ms                                                 | 76.3 ms: 1.54x faster                                               |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                               |
| deepcopy_reduce          | 4.17 us                                                | 2.73 us: 1.53x faster                                               |
| pickle_pure_python       | 484 us                                                 | 323 us: 1.50x faster                                                |
| logging_format           | 9.09 us                                                | 6.16 us: 1.48x faster                                               |
| logging_simple           | 8.30 us                                                | 5.67 us: 1.47x faster                                               |
| hexiom                   | 10.4 ms                                                | 7.10 ms: 1.46x faster                                               |
| scimark_fft              | 466 ms                                                 | 320 ms: 1.46x faster                                                |
| spectral_norm            | 170 ms                                                 | 117 ms: 1.45x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                              |
| regex_compile            | 188 ms                                                 | 134 ms: 1.41x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 728 ms: 1.40x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 56.9 ms: 1.39x faster                                               |
| fannkuch                 | 532 ms                                                 | 383 ms: 1.39x faster                                                |
| thrift                   | 1.07 ms                                                | 780 us: 1.37x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.73 ms: 1.37x faster                                               |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.4 ms: 1.34x faster                                               |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                              |
| html5lib                 | 88.9 ms                                                | 66.7 ms: 1.33x faster                                               |
| 2to3                     | 348 ms                                                 | 262 ms: 1.33x faster                                                |
| django_template          | 48.2 ms                                                | 36.2 ms: 1.33x faster                                               |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.32x faster                                                |
| json_dumps               | 14.2 ms                                                | 10.9 ms: 1.31x faster                                               |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.30x faster                                                |
| genshi_text              | 31.8 ms                                                | 24.8 ms: 1.28x faster                                               |
| sqlglot_optimize         | 69.2 ms                                                | 55.4 ms: 1.25x faster                                               |
| dulwich_log              | 84.3 ms                                                | 67.8 ms: 1.24x faster                                               |
| sympy_sum                | 196 ms                                                 | 159 ms: 1.23x faster                                                |
| pathlib                  | 20.5 ms                                                | 16.6 ms: 1.23x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 21.0 ms: 1.23x faster                                               |
| xml_etree_generate       | 99.4 ms                                                | 81.7 ms: 1.22x faster                                               |
| nqueens                  | 106 ms                                                 | 87.1 ms: 1.21x faster                                               |
| sympy_str                | 346 ms                                                 | 292 ms: 1.18x faster                                                |
| json_loads               | 31.2 us                                                | 26.7 us: 1.17x faster                                               |
| json                     | 5.69 ms                                                | 4.90 ms: 1.16x faster                                               |
| python_startup           | 14.6 ms                                                | 12.7 ms: 1.15x faster                                               |
| docutils                 | 3.30 sec                                               | 2.89 sec: 1.14x faster                                              |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.14x faster                                                |
| bench_thread_pool        | 986 us                                                 | 869 us: 1.13x faster                                                |
| genshi_xml               | 66.0 ms                                                | 58.4 ms: 1.13x faster                                               |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                |
| sympy_expand             | 566 ms                                                 | 502 ms: 1.13x faster                                                |
| regex_v8                 | 27.8 ms                                                | 24.6 ms: 1.13x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.08x faster                                               |
| regex_dna                | 227 ms                                                 | 211 ms: 1.07x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 157 ms: 1.07x faster                                                |
| mdp                      | 2.85 sec                                               | 2.75 sec: 1.04x faster                                              |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                |
| async_generators         | 444 ms                                                 | 456 ms: 1.03x slower                                                |
| telco                    | 7.27 ms                                                | 7.68 ms: 1.06x slower                                               |
| coverage                 | 79.4 ms                                                | 85.2 ms: 1.07x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.36 ms: 1.20x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.67 ms: 1.65x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 78.4 ms: 3.26x slower                                               |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                        |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241111-3.14.0a1+-a2be6fd-JIT/bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.401x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.28x