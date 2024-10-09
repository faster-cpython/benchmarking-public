# Results vs. 3.10.4

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-x86_64
- commit hash: 0442576
- commit date: 2024-10-07
- overall geometric mean: 1.37x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 274 ms: 1.27x faster                                               |
| docutils       | 3.30 sec                                               | 2.91 sec: 1.13x faster                                             |
| html5lib       | 88.9 ms                                                | 64.4 ms: 1.38x faster                                              |
| tornado_http   | 136 ms                                                 | 95.4 ms: 1.43x faster                                              |
| Geometric mean | (ref)                                                  | 1.30x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 317 ms: 2.30x faster                                               |
| async_tree_memoization  | 870 ms                                                 | 410 ms: 2.12x faster                                               |
| async_tree_io           | 1.77 sec                                               | 889 ms: 1.99x faster                                               |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 576 ms: 1.76x faster                                               |
| Geometric mean          | (ref)                                                  | 2.03x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.5 ms: 1.93x faster                                              |
| float          | 117 ms                                                 | 71.3 ms: 1.64x faster                                              |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.48x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 139 ms: 1.36x faster                                               |
| regex_v8       | 27.8 ms                                                | 26.0 ms: 1.07x faster                                              |
| regex_dna      | 227 ms                                                 | 227 ms: 1.00x slower                                               |
| regex_effbot   | 3.63 ms                                                | 3.78 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                  | 1.09x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.91 sec: 1.64x faster                                             |
| pickle_pure_python   | 484 us                                                 | 304 us: 1.59x faster                                               |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                               |
| xml_etree_process    | 79.1 ms                                                | 54.5 ms: 1.45x faster                                              |
| json_dumps           | 14.2 ms                                                | 9.97 ms: 1.42x faster                                              |
| xml_etree_generate   | 99.4 ms                                                | 76.5 ms: 1.30x faster                                              |
| xml_etree_iterparse  | 115 ms                                                 | 97.7 ms: 1.18x faster                                              |
| json_loads           | 31.2 us                                                | 26.6 us: 1.17x faster                                              |
| xml_etree_parse      | 168 ms                                                 | 144 ms: 1.16x faster                                               |
| unpickle             | 14.4 us                                                | 14.2 us: 1.01x faster                                              |
| unpickle_list        | 5.20 us                                                | 5.33 us: 1.03x slower                                              |
| pickle_list          | 5.08 us                                                | 5.26 us: 1.04x slower                                              |
| pickle               | 10.7 us                                                | 11.9 us: 1.12x slower                                              |
| pickle_dict          | 29.6 us                                                | 35.6 us: 1.20x slower                                              |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                              |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                              |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.79 ms: 1.67x faster                                              |
| django_template | 48.2 ms                                                | 35.5 ms: 1.36x faster                                              |
| genshi_text     | 31.8 ms                                                | 25.5 ms: 1.25x faster                                              |
| genshi_xml      | 66.0 ms                                                | 56.6 ms: 1.17x faster                                              |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.28x faster                                               |
| deltablue                | 7.91 ms                                                | 3.20 ms: 2.48x faster                                              |
| generators               | 80.1 ms                                                | 34.5 ms: 2.32x faster                                              |
| async_tree_none          | 728 ms                                                 | 317 ms: 2.30x faster                                               |
| richards_super           | 94.7 ms                                                | 42.7 ms: 2.22x faster                                              |
| deepcopy_memo            | 58.5 us                                                | 27.0 us: 2.17x faster                                              |
| richards                 | 79.3 ms                                                | 37.3 ms: 2.13x faster                                              |
| async_tree_memoization   | 870 ms                                                 | 410 ms: 2.12x faster                                               |
| async_tree_io            | 1.77 sec                                               | 889 ms: 1.99x faster                                               |
| chaos                    | 115 ms                                                 | 59.0 ms: 1.96x faster                                              |
| logging_silent           | 190 ns                                                 | 97.5 ns: 1.95x faster                                              |
| crypto_pyaes             | 128 ms                                                 | 65.8 ms: 1.94x faster                                              |
| nbody                    | 154 ms                                                 | 79.5 ms: 1.93x faster                                              |
| scimark_monte_carlo      | 118 ms                                                 | 62.4 ms: 1.89x faster                                              |
| asyncio_tcp              | 922 ms                                                 | 494 ms: 1.87x faster                                               |
| deepcopy                 | 479 us                                                 | 261 us: 1.84x faster                                               |
| raytrace                 | 507 ms                                                 | 276 ms: 1.83x faster                                               |
| go                       | 240 ms                                                 | 131 ms: 1.83x faster                                               |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.81x faster                                               |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 576 ms: 1.76x faster                                               |
| spectral_norm            | 170 ms                                                 | 99.3 ms: 1.71x faster                                              |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                              |
| mako                     | 16.3 ms                                                | 9.79 ms: 1.67x faster                                              |
| float                    | 117 ms                                                 | 71.3 ms: 1.64x faster                                              |
| tomli_loads              | 3.14 sec                                               | 1.91 sec: 1.64x faster                                             |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                              |
| scimark_lu               | 176 ms                                                 | 109 ms: 1.61x faster                                               |
| pyflate                  | 716 ms                                                 | 448 ms: 1.60x faster                                               |
| pickle_pure_python       | 484 us                                                 | 304 us: 1.59x faster                                               |
| coroutines               | 35.1 ms                                                | 22.6 ms: 1.55x faster                                              |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                               |
| sqlglot_transpile        | 2.57 ms                                                | 1.67 ms: 1.54x faster                                              |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.53x faster                                              |
| hexiom                   | 10.4 ms                                                | 6.82 ms: 1.53x faster                                              |
| scimark_fft              | 466 ms                                                 | 306 ms: 1.52x faster                                               |
| pylint                   | 551 ms                                                 | 367 ms: 1.50x faster                                               |
| logging_format           | 9.09 us                                                | 6.15 us: 1.48x faster                                              |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.39 ms: 1.47x faster                                              |
| logging_simple           | 8.30 us                                                | 5.64 us: 1.47x faster                                              |
| xml_etree_process        | 79.1 ms                                                | 54.5 ms: 1.45x faster                                              |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                             |
| pprint_safe_repr         | 1.02 sec                                               | 702 ms: 1.45x faster                                               |
| tornado_http             | 136 ms                                                 | 95.4 ms: 1.43x faster                                              |
| fannkuch                 | 532 ms                                                 | 373 ms: 1.43x faster                                               |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                             |
| json_dumps               | 14.2 ms                                                | 9.97 ms: 1.42x faster                                              |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                              |
| html5lib                 | 88.9 ms                                                | 64.4 ms: 1.38x faster                                              |
| thrift                   | 1.07 ms                                                | 785 us: 1.36x faster                                               |
| regex_compile            | 188 ms                                                 | 139 ms: 1.36x faster                                               |
| django_template          | 48.2 ms                                                | 35.5 ms: 1.36x faster                                              |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                             |
| xml_etree_generate       | 99.4 ms                                                | 76.5 ms: 1.30x faster                                              |
| pathlib                  | 20.5 ms                                                | 15.8 ms: 1.30x faster                                              |
| 2to3                     | 348 ms                                                 | 274 ms: 1.27x faster                                               |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.26x faster                                               |
| dulwich_log              | 84.3 ms                                                | 67.5 ms: 1.25x faster                                              |
| genshi_text              | 31.8 ms                                                | 25.5 ms: 1.25x faster                                              |
| nqueens                  | 106 ms                                                 | 85.9 ms: 1.23x faster                                              |
| xml_etree_iterparse      | 115 ms                                                 | 97.7 ms: 1.18x faster                                              |
| sqlglot_optimize         | 69.2 ms                                                | 58.5 ms: 1.18x faster                                              |
| json_loads               | 31.2 us                                                | 26.6 us: 1.17x faster                                              |
| genshi_xml               | 66.0 ms                                                | 56.6 ms: 1.17x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 144 ms: 1.16x faster                                               |
| sympy_str                | 346 ms                                                 | 298 ms: 1.16x faster                                               |
| sympy_expand             | 566 ms                                                 | 494 ms: 1.14x faster                                               |
| json                     | 5.69 ms                                                | 5.01 ms: 1.14x faster                                              |
| docutils                 | 3.30 sec                                               | 2.91 sec: 1.13x faster                                             |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 23.1 ms: 1.12x faster                                              |
| sympy_sum                | 196 ms                                                 | 176 ms: 1.11x faster                                               |
| bench_thread_pool        | 986 us                                                 | 892 us: 1.11x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.75 us: 1.10x faster                                              |
| regex_v8                 | 27.8 ms                                                | 26.0 ms: 1.07x faster                                              |
| mdp                      | 2.85 sec                                               | 2.73 sec: 1.04x faster                                             |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                               |
| gc_traversal             | 3.62 ms                                                | 3.56 ms: 1.02x faster                                              |
| unpickle                 | 14.4 us                                                | 14.2 us: 1.01x faster                                              |
| regex_dna                | 227 ms                                                 | 227 ms: 1.00x slower                                               |
| async_generators         | 444 ms                                                 | 449 ms: 1.01x slower                                               |
| unpickle_list            | 5.20 us                                                | 5.33 us: 1.03x slower                                              |
| pickle_list              | 5.08 us                                                | 5.26 us: 1.04x slower                                              |
| regex_effbot             | 3.63 ms                                                | 3.78 ms: 1.04x slower                                              |
| telco                    | 7.27 ms                                                | 7.58 ms: 1.04x slower                                              |
| create_gc_cycles         | 1.62 ms                                                | 1.72 ms: 1.06x slower                                              |
| coverage                 | 79.4 ms                                                | 87.7 ms: 1.10x slower                                              |
| pickle                   | 10.7 us                                                | 11.9 us: 1.12x slower                                              |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                              |
| pickle_dict              | 29.6 us                                                | 35.6 us: 1.20x slower                                              |
| unpack_sequence          | 60.0 ns                                                | 108 ns: 1.80x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 60.7 ms: 2.53x slower                                              |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241007-3.14.0a0-0442576-JIT/bm-20241007-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a0-0442576.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.19x