# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: f2327f4
- commit date: 2024-09-18
- overall geometric mean: 1.37x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 282 ms: 1.23x faster                                                        |
| docutils       | 3.30 sec                                               | 3.20 sec: 1.03x faster                                                      |
| html5lib       | 88.9 ms                                                | 66.5 ms: 1.34x faster                                                       |
| tornado_http   | 136 ms                                                 | 95.0 ms: 1.43x faster                                                       |
| Geometric mean | (ref)                                                  | 1.25x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 360 ms: 2.02x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 455 ms: 1.91x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 941 ms: 1.88x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 605 ms: 1.68x faster                                                        |
| Geometric mean          | (ref)                                                  | 1.87x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.1 ms: 1.89x faster                                                       |
| float          | 117 ms                                                 | 72.1 ms: 1.63x faster                                                       |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.47x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 138 ms: 1.37x faster                                                        |
| regex_v8       | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                       |
| regex_dna      | 227 ms                                                 | 221 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.92 sec: 1.63x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 305 us: 1.59x faster                                                        |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.54x faster                                                        |
| xml_etree_process    | 79.1 ms                                                | 54.2 ms: 1.46x faster                                                       |
| json_dumps           | 14.2 ms                                                | 10.2 ms: 1.39x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 77.4 ms: 1.28x faster                                                       |
| json_loads           | 31.2 us                                                | 27.0 us: 1.15x faster                                                       |
| xml_etree_parse      | 168 ms                                                 | 150 ms: 1.12x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 104 ms: 1.11x faster                                                        |
| unpickle             | 14.4 us                                                | 14.8 us: 1.03x slower                                                       |
| unpickle_list        | 5.20 us                                                | 5.41 us: 1.04x slower                                                       |
| pickle               | 10.7 us                                                | 11.5 us: 1.08x slower                                                       |
| pickle_dict          | 29.6 us                                                | 35.1 us: 1.19x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                                |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 7.09 ms: 1.19x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.0 ms: 1.63x faster                                                       |
| django_template | 48.2 ms                                                | 35.7 ms: 1.35x faster                                                       |
| genshi_text     | 31.8 ms                                                | 26.0 ms: 1.23x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 58.8 ms: 1.12x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.31x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.21 ms: 2.46x faster                                                       |
| generators               | 80.1 ms                                                | 32.6 ms: 2.45x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 26.9 us: 2.17x faster                                                       |
| richards_super           | 94.7 ms                                                | 45.6 ms: 2.08x faster                                                       |
| async_tree_none          | 728 ms                                                 | 360 ms: 2.02x faster                                                        |
| richards                 | 79.3 ms                                                | 39.5 ms: 2.01x faster                                                       |
| chaos                    | 115 ms                                                 | 58.9 ms: 1.96x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 66.5 ms: 1.92x faster                                                       |
| deepcopy                 | 479 us                                                 | 250 us: 1.91x faster                                                        |
| async_tree_memoization   | 870 ms                                                 | 455 ms: 1.91x faster                                                        |
| go                       | 240 ms                                                 | 126 ms: 1.91x faster                                                        |
| nbody                    | 154 ms                                                 | 81.1 ms: 1.89x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 62.6 ms: 1.89x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 941 ms: 1.88x faster                                                        |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.87x faster                                                        |
| raytrace                 | 507 ms                                                 | 277 ms: 1.83x faster                                                        |
| asyncio_tcp              | 922 ms                                                 | 505 ms: 1.83x faster                                                        |
| logging_silent           | 190 ns                                                 | 105 ns: 1.80x faster                                                        |
| pylint                   | 551 ms                                                 | 314 ms: 1.76x faster                                                        |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                       |
| spectral_norm            | 170 ms                                                 | 98.6 ms: 1.72x faster                                                       |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 605 ms: 1.68x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.92 sec: 1.63x faster                                                      |
| mako                     | 16.3 ms                                                | 10.0 ms: 1.63x faster                                                       |
| float                    | 117 ms                                                 | 72.1 ms: 1.63x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.35 ms: 1.61x faster                                                       |
| scimark_lu               | 176 ms                                                 | 111 ms: 1.59x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 305 us: 1.59x faster                                                        |
| pyflate                  | 716 ms                                                 | 452 ms: 1.59x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.57x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.54x faster                                                        |
| hexiom                   | 10.4 ms                                                | 6.83 ms: 1.52x faster                                                       |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                       |
| scimark_fft              | 466 ms                                                 | 308 ms: 1.51x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.73 ms: 1.48x faster                                                       |
| logging_simple           | 8.30 us                                                | 5.64 us: 1.47x faster                                                       |
| logging_format           | 9.09 us                                                | 6.20 us: 1.47x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.42 ms: 1.47x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 54.2 ms: 1.46x faster                                                       |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                      |
| tornado_http             | 136 ms                                                 | 95.0 ms: 1.43x faster                                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                      |
| fannkuch                 | 532 ms                                                 | 377 ms: 1.41x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 725 ms: 1.40x faster                                                        |
| json_dumps               | 14.2 ms                                                | 10.2 ms: 1.39x faster                                                       |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                       |
| regex_compile            | 188 ms                                                 | 138 ms: 1.37x faster                                                        |
| thrift                   | 1.07 ms                                                | 791 us: 1.35x faster                                                        |
| django_template          | 48.2 ms                                                | 35.7 ms: 1.35x faster                                                       |
| html5lib                 | 88.9 ms                                                | 66.5 ms: 1.34x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.21 sec: 1.30x faster                                                      |
| pathlib                  | 20.5 ms                                                | 15.8 ms: 1.29x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 77.4 ms: 1.28x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 111 ms: 1.28x faster                                                        |
| nqueens                  | 106 ms                                                 | 84.6 ms: 1.25x faster                                                       |
| dulwich_log              | 84.3 ms                                                | 67.6 ms: 1.25x faster                                                       |
| 2to3                     | 348 ms                                                 | 282 ms: 1.23x faster                                                        |
| genshi_text              | 31.8 ms                                                | 26.0 ms: 1.23x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 57.1 ms: 1.21x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 837 us: 1.18x faster                                                        |
| sympy_str                | 346 ms                                                 | 296 ms: 1.17x faster                                                        |
| json_loads               | 31.2 us                                                | 27.0 us: 1.15x faster                                                       |
| sympy_sum                | 196 ms                                                 | 171 ms: 1.15x faster                                                        |
| json                     | 5.69 ms                                                | 4.99 ms: 1.14x faster                                                       |
| sympy_integrate          | 25.8 ms                                                | 22.7 ms: 1.14x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.52 sec: 1.13x faster                                                      |
| sympy_expand             | 566 ms                                                 | 503 ms: 1.13x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 58.8 ms: 1.12x faster                                                       |
| xml_etree_parse          | 168 ms                                                 | 150 ms: 1.12x faster                                                        |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 104 ms: 1.11x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                       |
| sqlite_synth             | 3.02 us                                                | 2.76 us: 1.10x faster                                                       |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                        |
| docutils                 | 3.30 sec                                               | 3.20 sec: 1.03x faster                                                      |
| regex_dna                | 227 ms                                                 | 221 ms: 1.03x faster                                                        |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.00x faster                                                        |
| async_generators         | 444 ms                                                 | 457 ms: 1.03x slower                                                        |
| unpickle                 | 14.4 us                                                | 14.8 us: 1.03x slower                                                       |
| unpickle_list            | 5.20 us                                                | 5.41 us: 1.04x slower                                                       |
| coverage                 | 79.4 ms                                                | 85.9 ms: 1.08x slower                                                       |
| pickle                   | 10.7 us                                                | 11.5 us: 1.08x slower                                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.77 ms: 1.09x slower                                                       |
| telco                    | 7.27 ms                                                | 8.07 ms: 1.11x slower                                                       |
| gc_traversal             | 3.62 ms                                                | 4.04 ms: 1.11x slower                                                       |
| pickle_dict              | 29.6 us                                                | 35.1 us: 1.19x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.09 ms: 1.19x slower                                                       |
| unpack_sequence          | 60.0 ns                                                | 107 ns: 1.78x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                                |

Benchmark hidden because not significant (3): bench_mp_pool, pickle_list, regex_effbot
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240918-3.14.0a0-f2327f4-JIT/bm-20240918-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a0-f2327f4.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.21x