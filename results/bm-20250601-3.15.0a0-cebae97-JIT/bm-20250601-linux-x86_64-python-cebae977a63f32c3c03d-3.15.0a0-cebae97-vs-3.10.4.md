# Results vs. 3.10.4

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-x86_64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.662x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 297 ms: 1.17x faster                                                  |
| docutils       | 3.30 sec                                               | 2.91 sec: 1.13x faster                                                |
| html5lib       | 88.9 ms                                                | 65.4 ms: 1.36x faster                                                 |
| Geometric mean | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 665 ms: 2.66x faster                                                  |
| async_tree_none         | 728 ms                                                 | 289 ms: 2.52x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 345 ms: 2.52x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 592 ms: 1.72x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.32x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 69.2 ms: 1.69x faster                                                 |
| nbody          | 154 ms                                                 | 98.5 ms: 1.56x faster                                                 |
| pidigits       | 191 ms                                                 | 206 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.63 ms                                                | 3.20 ms: 1.14x faster                                                 |
| regex_dna      | 227 ms                                                 | 201 ms: 1.13x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.9 ms: 1.12x faster                                                 |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.09 sec: 1.50x faster                                                |
| unpickle_pure_python | 331 us                                                 | 234 us: 1.42x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 372 us: 1.30x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 69.2 ms: 1.14x faster                                                 |
| json_dumps           | 14.2 ms                                                | 13.4 ms: 1.06x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 110 ms: 1.05x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 162 ms: 1.04x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 102 ms: 1.02x slower                                                  |
| json_loads           | 31.2 us                                                | 33.6 us: 1.08x slower                                                 |
| unpickle_list        | 5.20 us                                                | 5.86 us: 1.13x slower                                                 |
| pickle_list          | 5.08 us                                                | 6.01 us: 1.18x slower                                                 |
| pickle_dict          | 29.6 us                                                | 37.8 us: 1.28x slower                                                 |
| unpickle             | 14.4 us                                                | 19.1 us: 1.33x slower                                                 |
| pickle               | 10.7 us                                                | 14.9 us: 1.40x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.40 ms: 1.25x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 25.3 ms: 1.26x faster                                                 |
| mako            | 16.3 ms                                                | 13.3 ms: 1.23x faster                                                 |
| django_template | 48.2 ms                                                | 39.9 ms: 1.21x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 58.2 ms: 1.13x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.20x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pprint_pformat           | 2.10 sec                                               | 1.86 us: 1131468.79x faster                                           |
| pprint_safe_repr         | 1.02 sec                                               | 1.12 us: 905822.47x faster                                            |
| typing_runtime_protocols | 544 us                                                 | 201 us: 2.71x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 665 ms: 2.66x faster                                                  |
| async_tree_none          | 728 ms                                                 | 289 ms: 2.52x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 345 ms: 2.52x faster                                                  |
| generators               | 80.1 ms                                                | 33.1 ms: 2.42x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.37 ms: 2.35x faster                                                 |
| richards_super           | 94.7 ms                                                | 46.3 ms: 2.04x faster                                                 |
| richards                 | 79.3 ms                                                | 39.6 ms: 2.00x faster                                                 |
| mdp                      | 2.85 sec                                               | 1.48 sec: 1.92x faster                                                |
| asyncio_tcp              | 922 ms                                                 | 491 ms: 1.88x faster                                                  |
| go                       | 240 ms                                                 | 130 ms: 1.84x faster                                                  |
| pylint                   | 551 ms                                                 | 315 ms: 1.75x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 592 ms: 1.72x faster                                                  |
| float                    | 117 ms                                                 | 69.2 ms: 1.69x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 34.8 us: 1.68x faster                                                 |
| chaos                    | 115 ms                                                 | 70.1 ms: 1.65x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 73.1 ms: 1.62x faster                                                 |
| scimark_sor              | 220 ms                                                 | 137 ms: 1.61x faster                                                  |
| pyflate                  | 716 ms                                                 | 450 ms: 1.59x faster                                                  |
| raytrace                 | 507 ms                                                 | 322 ms: 1.57x faster                                                  |
| nbody                    | 154 ms                                                 | 98.5 ms: 1.56x faster                                                 |
| spectral_norm            | 170 ms                                                 | 110 ms: 1.55x faster                                                  |
| deepcopy                 | 479 us                                                 | 315 us: 1.52x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.09 sec: 1.50x faster                                                |
| hexiom                   | 10.4 ms                                                | 6.94 ms: 1.50x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 85.8 ms: 1.49x faster                                                 |
| comprehensions           | 28.8 us                                                | 20.1 us: 1.43x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 234 us: 1.42x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.82 sec: 1.41x faster                                                |
| html5lib                 | 88.9 ms                                                | 65.4 ms: 1.36x faster                                                 |
| scimark_fft              | 466 ms                                                 | 353 ms: 1.32x faster                                                  |
| scimark_lu               | 176 ms                                                 | 135 ms: 1.31x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 372 us: 1.30x faster                                                  |
| coroutines               | 35.1 ms                                                | 27.4 ms: 1.28x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 66.1 ms: 1.28x faster                                                 |
| genshi_text              | 31.8 ms                                                | 25.3 ms: 1.26x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.26 sec: 1.25x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 3.38 us: 1.23x faster                                                 |
| mako                     | 16.3 ms                                                | 13.3 ms: 1.23x faster                                                 |
| django_template          | 48.2 ms                                                | 39.9 ms: 1.21x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 21.4 ms: 1.20x faster                                                 |
| sympy_sum                | 196 ms                                                 | 167 ms: 1.17x faster                                                  |
| 2to3                     | 348 ms                                                 | 297 ms: 1.17x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 69.2 ms: 1.14x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.20 ms: 1.14x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 58.2 ms: 1.13x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.91 sec: 1.13x faster                                                |
| regex_dna                | 227 ms                                                 | 201 ms: 1.13x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.74 ms: 1.13x faster                                                 |
| logging_simple           | 8.30 us                                                | 7.41 us: 1.12x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 24.9 ms: 1.12x faster                                                 |
| pathlib                  | 20.5 ms                                                | 18.4 ms: 1.11x faster                                                 |
| fannkuch                 | 532 ms                                                 | 479 ms: 1.11x faster                                                  |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                 |
| sympy_str                | 346 ms                                                 | 314 ms: 1.10x faster                                                  |
| logging_format           | 9.09 us                                                | 8.43 us: 1.08x faster                                                 |
| json_dumps               | 14.2 ms                                                | 13.4 ms: 1.06x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 110 ms: 1.05x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 162 ms: 1.04x faster                                                  |
| meteor_contest           | 120 ms                                                 | 115 ms: 1.04x faster                                                  |
| sympy_expand             | 566 ms                                                 | 548 ms: 1.03x faster                                                  |
| nqueens                  | 106 ms                                                 | 103 ms: 1.03x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 965 us: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                  |
| async_generators         | 444 ms                                                 | 439 ms: 1.01x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 3.08 us: 1.02x slower                                                 |
| xml_etree_generate       | 99.4 ms                                                | 102 ms: 1.02x slower                                                  |
| json                     | 5.69 ms                                                | 6.01 ms: 1.06x slower                                                 |
| json_loads               | 31.2 us                                                | 33.6 us: 1.08x slower                                                 |
| pidigits                 | 191 ms                                                 | 206 ms: 1.08x slower                                                  |
| unpickle_list            | 5.20 us                                                | 5.86 us: 1.13x slower                                                 |
| pickle_list              | 5.08 us                                                | 6.01 us: 1.18x slower                                                 |
| telco                    | 7.27 ms                                                | 9.04 ms: 1.24x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.40 ms: 1.25x slower                                                 |
| unpack_sequence          | 60.0 ns                                                | 75.6 ns: 1.26x slower                                                 |
| pickle_dict              | 29.6 us                                                | 37.8 us: 1.28x slower                                                 |
| unpickle                 | 14.4 us                                                | 19.1 us: 1.33x slower                                                 |
| pickle                   | 10.7 us                                                | 14.9 us: 1.40x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 5.11 ms: 1.41x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.61 ms: 1.61x slower                                                 |
| logging_silent           | 190 ns                                                 | 623 ns: 3.28x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 105 ms: 4.35x slower                                                  |
| coverage                 | 79.4 ms                                                | 529 ms: 6.66x slower                                                  |
| thrift                   | 1.07 ms                                                | 149 ms: 138.97x slower                                                |
| Geometric mean           | (ref)                                                  | 1.54x faster                                                          |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (15) of results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.662x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: 1.31x