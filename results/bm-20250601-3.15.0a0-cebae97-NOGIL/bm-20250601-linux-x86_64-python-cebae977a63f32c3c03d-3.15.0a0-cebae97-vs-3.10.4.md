# Results vs. 3.10.4

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-x86_64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.076x faster
- HPT reliability: 98.75%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.58x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 340 ms: 1.03x faster                                                  |
| docutils       | 3.30 sec                                               | 3.15 sec: 1.05x faster                                                |
| html5lib       | 88.9 ms                                                | 74.6 ms: 1.19x faster                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 637 ms: 2.78x faster                                                  |
| async_tree_none         | 728 ms                                                 | 300 ms: 2.43x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 377 ms: 2.31x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 621 ms: 1.64x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.25x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 80.4 ms: 1.46x faster                                                 |
| nbody          | 154 ms                                                 | 151 ms: 1.02x faster                                                  |
| pidigits       | 191 ms                                                 | 199 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                 |
| regex_dna      | 227 ms                                                 | 204 ms: 1.11x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.29 ms: 1.10x faster                                                 |
| regex_compile  | 188 ms                                                 | 172 ms: 1.10x faster                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.60 sec: 1.21x faster                                                |
| pickle_pure_python   | 484 us                                                 | 418 us: 1.16x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.09x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 304 us: 1.09x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 165 ms: 1.02x faster                                                  |
| json_dumps           | 14.2 ms                                                | 15.2 ms: 1.08x slower                                                 |
| xml_etree_process    | 79.1 ms                                                | 86.8 ms: 1.10x slower                                                 |
| pickle_list          | 5.08 us                                                | 5.77 us: 1.14x slower                                                 |
| json_loads           | 31.2 us                                                | 37.4 us: 1.20x slower                                                 |
| pickle_dict          | 29.6 us                                                | 36.0 us: 1.22x slower                                                 |
| unpickle_list        | 5.20 us                                                | 6.36 us: 1.22x slower                                                 |
| xml_etree_generate   | 99.4 ms                                                | 124 ms: 1.25x slower                                                  |
| pickle               | 10.7 us                                                | 15.1 us: 1.41x slower                                                 |
| unpickle             | 14.4 us                                                | 22.0 us: 1.53x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 17.1 ms: 1.17x slower                                                 |
| python_startup_no_site | 5.93 ms                                                | 10.00 ms: 1.69x slower                                                |
| Geometric mean         | (ref)                                                  | 1.41x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 34.1 ms: 1.07x slower                                                 |
| django_template | 48.2 ms                                                | 52.6 ms: 1.09x slower                                                 |
| genshi_xml      | 66.0 ms                                                | 73.1 ms: 1.11x slower                                                 |
| mako            | 16.3 ms                                                | 19.0 ms: 1.16x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.11x slower                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io            | 1.77 sec                                               | 637 ms: 2.78x faster                                                  |
| async_tree_none          | 728 ms                                                 | 300 ms: 2.43x faster                                                  |
| typing_runtime_protocols | 544 us                                                 | 235 us: 2.31x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 377 ms: 2.31x faster                                                  |
| generators               | 80.1 ms                                                | 35.0 ms: 2.29x faster                                                 |
| deltablue                | 7.91 ms                                                | 4.54 ms: 1.74x faster                                                 |
| go                       | 240 ms                                                 | 140 ms: 1.72x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 545 ms: 1.69x faster                                                  |
| mdp                      | 2.85 sec                                               | 1.73 sec: 1.65x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 621 ms: 1.64x faster                                                  |
| pylint                   | 551 ms                                                 | 358 ms: 1.54x faster                                                  |
| float                    | 117 ms                                                 | 80.4 ms: 1.46x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 40.9 us: 1.43x faster                                                 |
| scimark_sor              | 220 ms                                                 | 155 ms: 1.42x faster                                                  |
| chaos                    | 115 ms                                                 | 82.0 ms: 1.41x faster                                                 |
| gc_traversal             | 3.62 ms                                                | 2.74 ms: 1.32x faster                                                 |
| hexiom                   | 10.4 ms                                                | 7.95 ms: 1.31x faster                                                 |
| raytrace                 | 507 ms                                                 | 388 ms: 1.30x faster                                                  |
| pyflate                  | 716 ms                                                 | 552 ms: 1.30x faster                                                  |
| deepcopy                 | 479 us                                                 | 371 us: 1.29x faster                                                  |
| comprehensions           | 28.8 us                                                | 22.6 us: 1.27x faster                                                 |
| spectral_norm            | 170 ms                                                 | 134 ms: 1.27x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 2.04 sec: 1.26x faster                                                |
| pycparser                | 1.58 sec                                               | 1.30 sec: 1.21x faster                                                |
| tomli_loads              | 3.14 sec                                               | 2.60 sec: 1.21x faster                                                |
| html5lib                 | 88.9 ms                                                | 74.6 ms: 1.19x faster                                                 |
| coroutines               | 35.1 ms                                                | 29.5 ms: 1.19x faster                                                 |
| richards_super           | 94.7 ms                                                | 79.7 ms: 1.19x faster                                                 |
| richards                 | 79.3 ms                                                | 67.0 ms: 1.18x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 101 ms: 1.17x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 72.7 ms: 1.16x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 418 us: 1.16x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 112 ms: 1.14x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                 |
| regex_dna                | 227 ms                                                 | 204 ms: 1.11x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.29 ms: 1.10x faster                                                 |
| regex_compile            | 188 ms                                                 | 172 ms: 1.10x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.09x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 304 us: 1.09x faster                                                  |
| scimark_lu               | 176 ms                                                 | 167 ms: 1.06x faster                                                  |
| unpack_sequence          | 60.0 ns                                                | 57.3 ns: 1.05x faster                                                 |
| docutils                 | 3.30 sec                                               | 3.15 sec: 1.05x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 4.02 us: 1.04x faster                                                 |
| pathlib                  | 20.5 ms                                                | 19.7 ms: 1.04x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 25.0 ms: 1.03x faster                                                 |
| 2to3                     | 348 ms                                                 | 340 ms: 1.03x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 165 ms: 1.02x faster                                                  |
| nbody                    | 154 ms                                                 | 151 ms: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                  |
| sympy_sum                | 196 ms                                                 | 198 ms: 1.01x slower                                                  |
| async_generators         | 444 ms                                                 | 453 ms: 1.02x slower                                                  |
| scimark_fft              | 466 ms                                                 | 477 ms: 1.02x slower                                                  |
| pidigits                 | 191 ms                                                 | 199 ms: 1.04x slower                                                  |
| sympy_str                | 346 ms                                                 | 366 ms: 1.06x slower                                                  |
| sqlite_synth             | 3.02 us                                                | 3.21 us: 1.06x slower                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 6.89 ms: 1.07x slower                                                 |
| genshi_text              | 31.8 ms                                                | 34.1 ms: 1.07x slower                                                 |
| json_dumps               | 14.2 ms                                                | 15.2 ms: 1.08x slower                                                 |
| thrift                   | 1.07 ms                                                | 1.16 ms: 1.09x slower                                                 |
| logging_simple           | 8.30 us                                                | 9.07 us: 1.09x slower                                                 |
| fannkuch                 | 532 ms                                                 | 581 ms: 1.09x slower                                                  |
| django_template          | 48.2 ms                                                | 52.6 ms: 1.09x slower                                                 |
| xml_etree_process        | 79.1 ms                                                | 86.8 ms: 1.10x slower                                                 |
| sympy_expand             | 566 ms                                                 | 624 ms: 1.10x slower                                                  |
| genshi_xml               | 66.0 ms                                                | 73.1 ms: 1.11x slower                                                 |
| nqueens                  | 106 ms                                                 | 118 ms: 1.11x slower                                                  |
| logging_format           | 9.09 us                                                | 10.2 us: 1.12x slower                                                 |
| meteor_contest           | 120 ms                                                 | 135 ms: 1.13x slower                                                  |
| pickle_list              | 5.08 us                                                | 5.77 us: 1.14x slower                                                 |
| pprint_pformat           | 2.10 sec                                               | 2.41 sec: 1.15x slower                                                |
| pprint_safe_repr         | 1.02 sec                                               | 1.17 sec: 1.15x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 1.88 ms: 1.16x slower                                                 |
| mako                     | 16.3 ms                                                | 19.0 ms: 1.16x slower                                                 |
| json                     | 5.69 ms                                                | 6.62 ms: 1.16x slower                                                 |
| python_startup           | 14.6 ms                                                | 17.1 ms: 1.17x slower                                                 |
| json_loads               | 31.2 us                                                | 37.4 us: 1.20x slower                                                 |
| pickle_dict              | 29.6 us                                                | 36.0 us: 1.22x slower                                                 |
| unpickle_list            | 5.20 us                                                | 6.36 us: 1.22x slower                                                 |
| xml_etree_generate       | 99.4 ms                                                | 124 ms: 1.25x slower                                                  |
| pickle                   | 10.7 us                                                | 15.1 us: 1.41x slower                                                 |
| unpickle                 | 14.4 us                                                | 22.0 us: 1.53x slower                                                 |
| telco                    | 7.27 ms                                                | 11.8 ms: 1.62x slower                                                 |
| coverage                 | 79.4 ms                                                | 133 ms: 1.67x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 10.00 ms: 1.69x slower                                                |
| bench_thread_pool        | 986 us                                                 | 3.51 ms: 3.56x slower                                                 |
| logging_silent           | 190 ns                                                 | 720 ns: 3.80x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 112 ms: 4.66x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.05x faster                                                          |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (15) of results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.076x faster

# HPT report

- Reliability score: 98.75% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.58x