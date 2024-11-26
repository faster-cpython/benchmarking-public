# Results vs. 3.10.4

- fork: brandtbucher
- ref: jb0_backoff
- machine: linux-x86_64
- commit hash: 50d9e07
- commit date: 2024-10-24
- overall geometric mean: 1.325x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.38x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 286 ms: 1.22x faster                                                |
| docutils       | 3.30 sec                                               | 3.40 sec: 1.03x slower                                              |
| html5lib       | 88.9 ms                                                | 68.6 ms: 1.29x faster                                               |
| tornado_http   | 136 ms                                                 | 112 ms: 1.22x faster                                                |
| Geometric mean | (ref)                                                  | 1.17x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 347 ms: 2.10x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 434 ms: 2.00x faster                                                |
| async_tree_io           | 1.77 sec                                               | 941 ms: 1.88x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 599 ms: 1.70x faster                                                |
| Geometric mean          | (ref)                                                  | 1.91x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.7 ms: 1.88x faster                                               |
| float          | 117 ms                                                 | 75.0 ms: 1.56x faster                                               |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.44x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 146 ms: 1.29x faster                                                |
| regex_v8       | 27.8 ms                                                | 25.8 ms: 1.08x faster                                               |
| regex_dna      | 227 ms                                                 | 215 ms: 1.05x faster                                                |
| regex_effbot   | 3.63 ms                                                | 3.71 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                  | 1.09x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 294 us: 1.65x faster                                                |
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                              |
| unpickle_pure_python | 331 us                                                 | 226 us: 1.46x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 60.1 ms: 1.32x faster                                               |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.27x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 83.3 ms: 1.19x faster                                               |
| json_loads           | 31.2 us                                                | 26.7 us: 1.17x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 100 ms: 1.15x faster                                                |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.9 ms: 1.23x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 7.11 ms: 1.20x slower                                               |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.2 ms: 1.61x faster                                               |
| genshi_text     | 31.8 ms                                                | 25.7 ms: 1.24x faster                                               |
| django_template | 48.2 ms                                                | 40.5 ms: 1.19x faster                                               |
| genshi_xml      | 66.0 ms                                                | 62.6 ms: 1.06x faster                                               |
| Geometric mean  | (ref)                                                  | 1.26x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                                |
| generators               | 80.1 ms                                                | 36.6 ms: 2.19x faster                                               |
| async_tree_none          | 728 ms                                                 | 347 ms: 2.10x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 434 ms: 2.00x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 29.7 us: 1.97x faster                                               |
| deltablue                | 7.91 ms                                                | 4.04 ms: 1.96x faster                                               |
| chaos                    | 115 ms                                                 | 59.8 ms: 1.93x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 61.7 ms: 1.92x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 67.9 ms: 1.88x faster                                               |
| async_tree_io            | 1.77 sec                                               | 941 ms: 1.88x faster                                                |
| nbody                    | 154 ms                                                 | 81.7 ms: 1.88x faster                                               |
| go                       | 240 ms                                                 | 129 ms: 1.85x faster                                                |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.80x faster                                                |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                                |
| richards_super           | 94.7 ms                                                | 54.7 ms: 1.73x faster                                               |
| deepcopy                 | 479 us                                                 | 277 us: 1.73x faster                                                |
| raytrace                 | 507 ms                                                 | 296 ms: 1.71x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 599 ms: 1.70x faster                                                |
| pickle_pure_python       | 484 us                                                 | 294 us: 1.65x faster                                                |
| comprehensions           | 28.8 us                                                | 17.4 us: 1.65x faster                                               |
| richards                 | 79.3 ms                                                | 48.8 ms: 1.62x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                              |
| mako                     | 16.3 ms                                                | 10.2 ms: 1.61x faster                                               |
| pyflate                  | 716 ms                                                 | 446 ms: 1.60x faster                                                |
| float                    | 117 ms                                                 | 75.0 ms: 1.56x faster                                               |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.55x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.43 ms: 1.51x faster                                               |
| unpickle_pure_python     | 331 us                                                 | 226 us: 1.46x faster                                                |
| scimark_fft              | 466 ms                                                 | 321 ms: 1.45x faster                                                |
| spectral_norm            | 170 ms                                                 | 118 ms: 1.44x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.91 us: 1.43x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 726 ms: 1.40x faster                                                |
| hexiom                   | 10.4 ms                                                | 7.44 ms: 1.40x faster                                               |
| sqlglot_transpile        | 2.57 ms                                                | 1.85 ms: 1.39x faster                                               |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.66 ms: 1.39x faster                                               |
| fannkuch                 | 532 ms                                                 | 384 ms: 1.39x faster                                                |
| coroutines               | 35.1 ms                                                | 26.4 ms: 1.33x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 60.1 ms: 1.32x faster                                               |
| thrift                   | 1.07 ms                                                | 825 us: 1.30x faster                                                |
| html5lib                 | 88.9 ms                                                | 68.6 ms: 1.29x faster                                               |
| regex_compile            | 188 ms                                                 | 146 ms: 1.29x faster                                                |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.27x faster                                               |
| pycparser                | 1.58 sec                                               | 1.27 sec: 1.24x faster                                              |
| genshi_text              | 31.8 ms                                                | 25.7 ms: 1.24x faster                                               |
| pathlib                  | 20.5 ms                                                | 16.6 ms: 1.23x faster                                               |
| python_startup           | 14.6 ms                                                | 11.9 ms: 1.23x faster                                               |
| tornado_http             | 136 ms                                                 | 112 ms: 1.22x faster                                                |
| 2to3                     | 348 ms                                                 | 286 ms: 1.22x faster                                                |
| dulwich_log              | 84.3 ms                                                | 70.0 ms: 1.20x faster                                               |
| logging_format           | 9.09 us                                                | 7.57 us: 1.20x faster                                               |
| xml_etree_generate       | 99.4 ms                                                | 83.3 ms: 1.19x faster                                               |
| sqlglot_normalize        | 143 ms                                                 | 120 ms: 1.19x faster                                                |
| django_template          | 48.2 ms                                                | 40.5 ms: 1.19x faster                                               |
| logging_simple           | 8.30 us                                                | 7.01 us: 1.18x faster                                               |
| nqueens                  | 106 ms                                                 | 89.3 ms: 1.18x faster                                               |
| pylint                   | 551 ms                                                 | 466 ms: 1.18x faster                                                |
| json_loads               | 31.2 us                                                | 26.7 us: 1.17x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 100 ms: 1.15x faster                                                |
| json                     | 5.69 ms                                                | 4.99 ms: 1.14x faster                                               |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                |
| regex_v8                 | 27.8 ms                                                | 25.8 ms: 1.08x faster                                               |
| sympy_expand             | 566 ms                                                 | 533 ms: 1.06x faster                                                |
| mdp                      | 2.85 sec                                               | 2.69 sec: 1.06x faster                                              |
| genshi_xml               | 66.0 ms                                                | 62.6 ms: 1.06x faster                                               |
| regex_dna                | 227 ms                                                 | 215 ms: 1.05x faster                                                |
| sqlglot_optimize         | 69.2 ms                                                | 66.7 ms: 1.04x faster                                               |
| sqlalchemy_imperative    | 23.3 ms                                                | 22.5 ms: 1.04x faster                                               |
| sympy_str                | 346 ms                                                 | 334 ms: 1.04x faster                                                |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                |
| bench_thread_pool        | 986 us                                                 | 969 us: 1.02x faster                                                |
| sqlalchemy_declarative   | 172 ms                                                 | 175 ms: 1.02x slower                                                |
| regex_effbot             | 3.63 ms                                                | 3.71 ms: 1.02x slower                                               |
| docutils                 | 3.30 sec                                               | 3.40 sec: 1.03x slower                                              |
| telco                    | 7.27 ms                                                | 7.61 ms: 1.05x slower                                               |
| sympy_sum                | 196 ms                                                 | 206 ms: 1.05x slower                                                |
| async_generators         | 444 ms                                                 | 467 ms: 1.05x slower                                                |
| sympy_integrate          | 25.8 ms                                                | 27.3 ms: 1.06x slower                                               |
| coverage                 | 79.4 ms                                                | 86.4 ms: 1.09x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 7.11 ms: 1.20x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.74 ms: 1.31x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.66 ms: 1.64x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 89.0 ms: 3.71x slower                                               |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                        |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241024-3.14.0a1+-50d9e07-JIT/bm-20241024-linux-x86_64-brandtbucher-jb0_backoff-3.14.0a1+-50d9e07.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.325x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.38x