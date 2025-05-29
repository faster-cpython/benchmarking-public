# Results vs. 3.10.4

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-x86_64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.336x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 253 ms: 1.38x faster                                                  |
| docutils       | 3.30 sec                                               | 2.63 sec: 1.25x faster                                                |
| html5lib       | 88.9 ms                                                | 57.6 ms: 1.54x faster                                                 |
| Geometric mean | (ref)                                                  | 1.39x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 585 ms: 3.02x faster                                                  |
| async_tree_none         | 728 ms                                                 | 257 ms: 2.83x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 308 ms: 2.83x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 505 ms: 2.01x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.64x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.4 ms: 1.78x faster                                                 |
| float          | 117 ms                                                 | 67.5 ms: 1.74x faster                                                 |
| pidigits       | 191 ms                                                 | 210 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                  | 1.41x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 124 ms: 1.52x faster                                                  |
| regex_v8       | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                 |
| regex_dna      | 227 ms                                                 | 206 ms: 1.10x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.54 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.17x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                |
| pickle_pure_python   | 484 us                                                 | 308 us: 1.57x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 212 us: 1.56x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 60.1 ms: 1.32x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 88.6 ms: 1.12x faster                                                 |
| unpickle_list        | 5.20 us                                                | 4.67 us: 1.11x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 104 ms: 1.11x faster                                                  |
| json_dumps           | 14.2 ms                                                | 12.9 ms: 1.10x faster                                                 |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 164 ms: 1.02x faster                                                  |
| pickle_list          | 5.08 us                                                | 5.31 us: 1.05x slower                                                 |
| pickle_dict          | 29.6 us                                                | 34.4 us: 1.16x slower                                                 |
| pickle               | 10.7 us                                                | 13.2 us: 1.24x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                          |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.1 ms: 1.20x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 6.92 ms: 1.17x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.4 ms: 1.53x faster                                                 |
| genshi_text     | 31.8 ms                                                | 20.9 ms: 1.53x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 48.0 ms: 1.38x faster                                                 |
| mako            | 16.3 ms                                                | 12.2 ms: 1.34x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 160 us: 3.40x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 585 ms: 3.02x faster                                                  |
| async_tree_none          | 728 ms                                                 | 257 ms: 2.83x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 308 ms: 2.83x faster                                                  |
| generators               | 80.1 ms                                                | 28.9 ms: 2.77x faster                                                 |
| deltablue                | 7.91 ms                                                | 2.98 ms: 2.65x faster                                                 |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.34x faster                                                |
| go                       | 240 ms                                                 | 107 ms: 2.24x faster                                                  |
| chaos                    | 115 ms                                                 | 53.9 ms: 2.14x faster                                                 |
| scimark_sor              | 220 ms                                                 | 108 ms: 2.04x faster                                                  |
| raytrace                 | 507 ms                                                 | 249 ms: 2.03x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 28.8 us: 2.03x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 505 ms: 2.01x faster                                                  |
| richards_super           | 94.7 ms                                                | 47.3 ms: 2.00x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 59.7 ms: 1.98x faster                                                 |
| pylint                   | 551 ms                                                 | 279 ms: 1.97x faster                                                  |
| deepcopy                 | 479 us                                                 | 246 us: 1.95x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 477 ms: 1.93x faster                                                  |
| richards                 | 79.3 ms                                                | 41.0 ms: 1.93x faster                                                 |
| hexiom                   | 10.4 ms                                                | 5.76 ms: 1.81x faster                                                 |
| spectral_norm            | 170 ms                                                 | 94.5 ms: 1.80x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.0 us: 1.79x faster                                                 |
| nbody                    | 154 ms                                                 | 86.4 ms: 1.78x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 73.1 ms: 1.75x faster                                                 |
| float                    | 117 ms                                                 | 67.5 ms: 1.74x faster                                                 |
| pyflate                  | 716 ms                                                 | 423 ms: 1.69x faster                                                  |
| scimark_lu               | 176 ms                                                 | 106 ms: 1.65x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.60 us: 1.61x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                |
| pickle_pure_python       | 484 us                                                 | 308 us: 1.57x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 212 us: 1.56x faster                                                  |
| html5lib                 | 88.9 ms                                                | 57.6 ms: 1.54x faster                                                 |
| django_template          | 48.2 ms                                                | 31.4 ms: 1.53x faster                                                 |
| genshi_text              | 31.8 ms                                                | 20.9 ms: 1.53x faster                                                 |
| scimark_fft              | 466 ms                                                 | 305 ms: 1.52x faster                                                  |
| regex_compile            | 188 ms                                                 | 124 ms: 1.52x faster                                                  |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.29 ms: 1.51x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 58.0 ms: 1.45x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 18.4 ms: 1.40x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                                |
| 2to3                     | 348 ms                                                 | 253 ms: 1.38x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 48.0 ms: 1.38x faster                                                 |
| logging_simple           | 8.30 us                                                | 6.04 us: 1.37x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.37x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 751 ms: 1.36x faster                                                  |
| nqueens                  | 106 ms                                                 | 78.1 ms: 1.36x faster                                                 |
| sympy_sum                | 196 ms                                                 | 146 ms: 1.34x faster                                                  |
| logging_format           | 9.09 us                                                | 6.79 us: 1.34x faster                                                 |
| mako                     | 16.3 ms                                                | 12.2 ms: 1.34x faster                                                 |
| pathlib                  | 20.5 ms                                                | 15.4 ms: 1.33x faster                                                 |
| sympy_str                | 346 ms                                                 | 262 ms: 1.32x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 60.1 ms: 1.32x faster                                                 |
| fannkuch                 | 532 ms                                                 | 412 ms: 1.29x faster                                                  |
| sympy_expand             | 566 ms                                                 | 446 ms: 1.27x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.63 sec: 1.25x faster                                                |
| python_startup           | 14.6 ms                                                | 12.1 ms: 1.20x faster                                                 |
| unpack_sequence          | 60.0 ns                                                | 51.3 ns: 1.17x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 852 us: 1.16x faster                                                  |
| async_generators         | 444 ms                                                 | 394 ms: 1.13x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 88.6 ms: 1.12x faster                                                 |
| unpickle_list            | 5.20 us                                                | 4.67 us: 1.11x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 104 ms: 1.11x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                 |
| json_dumps               | 14.2 ms                                                | 12.9 ms: 1.10x faster                                                 |
| regex_dna                | 227 ms                                                 | 206 ms: 1.10x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.75 us: 1.10x faster                                                 |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                                 |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                                 |
| meteor_contest           | 120 ms                                                 | 115 ms: 1.04x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.54 ms: 1.02x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 164 ms: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                  |
| telco                    | 7.27 ms                                                | 7.33 ms: 1.01x slower                                                 |
| pickle_list              | 5.08 us                                                | 5.31 us: 1.05x slower                                                 |
| pidigits                 | 191 ms                                                 | 210 ms: 1.10x slower                                                  |
| pickle_dict              | 29.6 us                                                | 34.4 us: 1.16x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 6.92 ms: 1.17x slower                                                 |
| pickle                   | 10.7 us                                                | 13.2 us: 1.24x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 4.88 ms: 1.35x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.64 ms: 1.63x slower                                                 |
| dask                     | 441 ms                                                 | 895 ms: 2.03x slower                                                  |
| logging_silent           | 190 ns                                                 | 508 ns: 2.68x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 92.5 ms: 3.85x slower                                                 |
| coverage                 | 79.4 ms                                                | 413 ms: 5.19x slower                                                  |
| thrift                   | 1.07 ms                                                | 148 ms: 138.46x slower                                                |
| Geometric mean           | (ref)                                                  | 1.27x faster                                                          |

Benchmark hidden because not significant (1): unpickle
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (23) of results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.336x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.32x