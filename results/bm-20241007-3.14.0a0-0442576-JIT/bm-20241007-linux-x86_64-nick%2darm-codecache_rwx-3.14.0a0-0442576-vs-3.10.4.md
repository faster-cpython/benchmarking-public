# Results vs. 3.10.4

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-x86_64
- commit hash: 0442576
- commit date: 2024-10-07
- overall geometric mean: 1.432x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 274 ms: 1.27x faster                                               |
| docutils       | 3.30 sec                                               | 2.89 sec: 1.14x faster                                             |
| html5lib       | 88.9 ms                                                | 64.3 ms: 1.38x faster                                              |
| tornado_http   | 136 ms                                                 | 94.6 ms: 1.44x faster                                              |
| Geometric mean | (ref)                                                  | 1.30x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 319 ms: 2.29x faster                                               |
| async_tree_memoization  | 870 ms                                                 | 409 ms: 2.13x faster                                               |
| async_tree_io           | 1.77 sec                                               | 891 ms: 1.99x faster                                               |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 572 ms: 1.78x faster                                               |
| Geometric mean          | (ref)                                                  | 2.03x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.0 ms: 1.87x faster                                              |
| float          | 117 ms                                                 | 71.3 ms: 1.64x faster                                              |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.47x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 139 ms: 1.35x faster                                               |
| regex_v8       | 27.8 ms                                                | 24.5 ms: 1.13x faster                                              |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                  | 1.13x faster                                                       |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.63x faster                                             |
| pickle_pure_python   | 484 us                                                 | 304 us: 1.59x faster                                               |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                               |
| xml_etree_process    | 79.1 ms                                                | 54.6 ms: 1.45x faster                                              |
| json_dumps           | 14.2 ms                                                | 9.98 ms: 1.42x faster                                              |
| xml_etree_generate   | 99.4 ms                                                | 77.8 ms: 1.28x faster                                              |
| xml_etree_iterparse  | 115 ms                                                 | 98.2 ms: 1.18x faster                                              |
| json_loads           | 31.2 us                                                | 26.8 us: 1.17x faster                                              |
| xml_etree_parse      | 168 ms                                                 | 145 ms: 1.16x faster                                               |
| pickle_list          | 5.08 us                                                | 4.96 us: 1.02x faster                                              |
| unpickle             | 14.4 us                                                | 14.5 us: 1.01x slower                                              |
| unpickle_list        | 5.20 us                                                | 5.30 us: 1.02x slower                                              |
| pickle               | 10.7 us                                                | 11.7 us: 1.09x slower                                              |
| pickle_dict          | 29.6 us                                                | 34.1 us: 1.15x slower                                              |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                              |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                              |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.83 ms: 1.66x faster                                              |
| django_template | 48.2 ms                                                | 35.1 ms: 1.37x faster                                              |
| genshi_text     | 31.8 ms                                                | 24.9 ms: 1.28x faster                                              |
| genshi_xml      | 66.0 ms                                                | 57.9 ms: 1.14x faster                                              |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.29x faster                                               |
| deltablue                | 7.91 ms                                                | 3.20 ms: 2.48x faster                                              |
| generators               | 80.1 ms                                                | 34.6 ms: 2.32x faster                                              |
| async_tree_none          | 728 ms                                                 | 319 ms: 2.29x faster                                               |
| richards_super           | 94.7 ms                                                | 42.6 ms: 2.22x faster                                              |
| deepcopy_memo            | 58.5 us                                                | 26.5 us: 2.20x faster                                              |
| async_tree_memoization   | 870 ms                                                 | 409 ms: 2.13x faster                                               |
| richards                 | 79.3 ms                                                | 37.6 ms: 2.11x faster                                              |
| async_tree_io            | 1.77 sec                                               | 891 ms: 1.99x faster                                               |
| chaos                    | 115 ms                                                 | 59.1 ms: 1.95x faster                                              |
| logging_silent           | 190 ns                                                 | 97.7 ns: 1.94x faster                                              |
| crypto_pyaes             | 128 ms                                                 | 66.6 ms: 1.92x faster                                              |
| scimark_monte_carlo      | 118 ms                                                 | 62.7 ms: 1.89x faster                                              |
| nbody                    | 154 ms                                                 | 82.0 ms: 1.87x faster                                              |
| asyncio_tcp              | 922 ms                                                 | 494 ms: 1.87x faster                                               |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                               |
| raytrace                 | 507 ms                                                 | 277 ms: 1.83x faster                                               |
| go                       | 240 ms                                                 | 132 ms: 1.82x faster                                               |
| deepcopy                 | 479 us                                                 | 266 us: 1.80x faster                                               |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 572 ms: 1.78x faster                                               |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                              |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.67x faster                                               |
| mako                     | 16.3 ms                                                | 9.83 ms: 1.66x faster                                              |
| float                    | 117 ms                                                 | 71.3 ms: 1.64x faster                                              |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                              |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.63x faster                                             |
| pickle_pure_python       | 484 us                                                 | 304 us: 1.59x faster                                               |
| scimark_lu               | 176 ms                                                 | 111 ms: 1.59x faster                                               |
| pyflate                  | 716 ms                                                 | 451 ms: 1.59x faster                                               |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.56x faster                                              |
| coroutines               | 35.1 ms                                                | 22.6 ms: 1.55x faster                                              |
| sqlglot_transpile        | 2.57 ms                                                | 1.67 ms: 1.54x faster                                              |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                               |
| hexiom                   | 10.4 ms                                                | 6.79 ms: 1.53x faster                                              |
| scimark_fft              | 466 ms                                                 | 309 ms: 1.51x faster                                               |
| pylint                   | 551 ms                                                 | 366 ms: 1.51x faster                                               |
| logging_format           | 9.09 us                                                | 6.07 us: 1.50x faster                                              |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.32 ms: 1.50x faster                                              |
| logging_simple           | 8.30 us                                                | 5.56 us: 1.49x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 686 ms: 1.48x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 54.6 ms: 1.45x faster                                              |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                             |
| tornado_http             | 136 ms                                                 | 94.6 ms: 1.44x faster                                              |
| fannkuch                 | 532 ms                                                 | 372 ms: 1.43x faster                                               |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                             |
| json_dumps               | 14.2 ms                                                | 9.98 ms: 1.42x faster                                              |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                              |
| html5lib                 | 88.9 ms                                                | 64.3 ms: 1.38x faster                                              |
| django_template          | 48.2 ms                                                | 35.1 ms: 1.37x faster                                              |
| thrift                   | 1.07 ms                                                | 786 us: 1.36x faster                                               |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                             |
| regex_compile            | 188 ms                                                 | 139 ms: 1.35x faster                                               |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                              |
| genshi_text              | 31.8 ms                                                | 24.9 ms: 1.28x faster                                              |
| xml_etree_generate       | 99.4 ms                                                | 77.8 ms: 1.28x faster                                              |
| 2to3                     | 348 ms                                                 | 274 ms: 1.27x faster                                               |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.26x faster                                               |
| dulwich_log              | 84.3 ms                                                | 67.8 ms: 1.24x faster                                              |
| nqueens                  | 106 ms                                                 | 87.1 ms: 1.22x faster                                              |
| sqlglot_optimize         | 69.2 ms                                                | 58.7 ms: 1.18x faster                                              |
| xml_etree_iterparse      | 115 ms                                                 | 98.2 ms: 1.18x faster                                              |
| json_loads               | 31.2 us                                                | 26.8 us: 1.17x faster                                              |
| sympy_str                | 346 ms                                                 | 297 ms: 1.17x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 145 ms: 1.16x faster                                               |
| json                     | 5.69 ms                                                | 4.97 ms: 1.15x faster                                              |
| sympy_expand             | 566 ms                                                 | 495 ms: 1.14x faster                                               |
| docutils                 | 3.30 sec                                               | 2.89 sec: 1.14x faster                                             |
| genshi_xml               | 66.0 ms                                                | 57.9 ms: 1.14x faster                                              |
| sympy_sum                | 196 ms                                                 | 173 ms: 1.13x faster                                               |
| regex_v8                 | 27.8 ms                                                | 24.5 ms: 1.13x faster                                              |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 23.1 ms: 1.12x faster                                              |
| sqlite_synth             | 3.02 us                                                | 2.74 us: 1.11x faster                                              |
| bench_thread_pool        | 986 us                                                 | 892 us: 1.11x faster                                               |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                               |
| mdp                      | 2.85 sec                                               | 2.72 sec: 1.05x faster                                             |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                               |
| pickle_list              | 5.08 us                                                | 4.96 us: 1.02x faster                                              |
| unpickle                 | 14.4 us                                                | 14.5 us: 1.01x slower                                              |
| unpickle_list            | 5.20 us                                                | 5.30 us: 1.02x slower                                              |
| telco                    | 7.27 ms                                                | 7.58 ms: 1.04x slower                                              |
| async_generators         | 444 ms                                                 | 463 ms: 1.04x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 1.73 ms: 1.07x slower                                              |
| gc_traversal             | 3.62 ms                                                | 3.88 ms: 1.07x slower                                              |
| coverage                 | 79.4 ms                                                | 86.0 ms: 1.08x slower                                              |
| pickle                   | 10.7 us                                                | 11.7 us: 1.09x slower                                              |
| pickle_dict              | 29.6 us                                                | 34.1 us: 1.15x slower                                              |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                              |
| unpack_sequence          | 60.0 ns                                                | 106 ns: 1.76x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 60.3 ms: 2.51x slower                                              |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                       |

Benchmark hidden because not significant (2): asyncio_websockets, regex_effbot
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241007-3.14.0a0-0442576-JIT/bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.432x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.19x