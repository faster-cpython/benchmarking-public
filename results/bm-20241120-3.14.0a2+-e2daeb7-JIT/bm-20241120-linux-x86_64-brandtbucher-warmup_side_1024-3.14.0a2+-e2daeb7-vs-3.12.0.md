# Results vs. 3.12.0

- fork: brandtbucher
- ref: warmup_side_1024
- machine: linux-x86_64
- commit hash: e2daeb7
- commit date: 2024-11-20
- overall geometric mean: 1.075x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 261 ms: 1.05x faster                                                     |
| docutils       | 2.77 sec                                               | 2.81 sec: 1.02x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 397 ms: 1.45x faster                                                     |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 316 ms: 1.42x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 410 ms: 1.41x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 562 ms: 1.29x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 921 ms: 1.28x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 914 ms: 1.26x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.35x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 84.8 ms: 1.14x faster                                                    |
| float          | 84.7 ms                                                | 78.2 ms: 1.08x faster                                                    |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.08x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                     |
| regex_effbot   | 3.61 ms                                                | 3.38 ms: 1.07x faster                                                    |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                                     |
| regex_v8       | 23.1 ms                                                | 25.7 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 230 us                                                 | 191 us: 1.21x faster                                                     |
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 79.5 ms: 1.12x faster                                                    |
| xml_etree_process    | 61.7 ms                                                | 56.2 ms: 1.10x faster                                                    |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                     |
| json_loads           | 28.5 us                                                | 26.4 us: 1.08x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                     |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                             |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                    |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.2 ms: 1.16x faster                                                    |
| django_template | 34.6 ms                                                | 33.0 ms: 1.05x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 397 ms: 1.45x faster                                                     |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 316 ms: 1.42x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 410 ms: 1.41x faster                                                     |
| deepcopy_memo              | 40.7 us                                                | 29.3 us: 1.39x faster                                                    |
| deepcopy                   | 371 us                                                 | 268 us: 1.39x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 562 ms: 1.29x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 921 ms: 1.28x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 914 ms: 1.26x faster                                                     |
| comprehensions             | 21.8 us                                                | 17.3 us: 1.26x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                                    |
| scimark_fft                | 382 ms                                                 | 315 ms: 1.21x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 67.7 ms: 1.21x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 191 us: 1.21x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                   |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                    |
| logging_format             | 7.23 us                                                | 6.10 us: 1.18x faster                                                    |
| logging_simple             | 6.46 us                                                | 5.49 us: 1.18x faster                                                    |
| mako                       | 11.9 ms                                                | 10.2 ms: 1.16x faster                                                    |
| deltablue                  | 3.72 ms                                                | 3.20 ms: 1.16x faster                                                    |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 65.3 ms: 1.15x faster                                                    |
| nbody                      | 97.0 ms                                                | 84.8 ms: 1.14x faster                                                    |
| chaos                      | 67.0 ms                                                | 58.6 ms: 1.14x faster                                                    |
| sqlalchemy_declarative     | 147 ms                                                 | 129 ms: 1.13x faster                                                     |
| richards                   | 45.8 ms                                                | 40.6 ms: 1.13x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 79.5 ms: 1.12x faster                                                    |
| richards_super             | 51.5 ms                                                | 46.4 ms: 1.11x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 56.2 ms: 1.10x faster                                                    |
| json                       | 5.26 ms                                                | 4.82 ms: 1.09x faster                                                    |
| fannkuch                   | 417 ms                                                 | 384 ms: 1.09x faster                                                     |
| raytrace                   | 312 ms                                                 | 287 ms: 1.09x faster                                                     |
| float                      | 84.7 ms                                                | 78.2 ms: 1.08x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                     |
| go                         | 139 ms                                                 | 129 ms: 1.08x faster                                                     |
| json_loads                 | 28.5 us                                                | 26.4 us: 1.08x faster                                                    |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                                     |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.4 ms: 1.07x faster                                                    |
| sympy_sum                  | 169 ms                                                 | 158 ms: 1.07x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 724 ms: 1.07x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.74 ms: 1.07x faster                                                    |
| regex_effbot               | 3.61 ms                                                | 3.38 ms: 1.07x faster                                                    |
| pyflate                    | 482 ms                                                 | 455 ms: 1.06x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                     |
| sympy_str                  | 300 ms                                                 | 284 ms: 1.05x faster                                                     |
| 2to3                       | 274 ms                                                 | 261 ms: 1.05x faster                                                     |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                   |
| django_template            | 34.6 ms                                                | 33.0 ms: 1.05x faster                                                    |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                     |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.03x faster                                                    |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 20.8 ms: 1.03x faster                                                    |
| async_generators           | 463 ms                                                 | 451 ms: 1.03x faster                                                     |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.02x faster                                                     |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.02x faster                                                    |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.02x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 67.2 ms: 1.02x faster                                                    |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.02x faster                                                    |
| coroutines                 | 23.2 ms                                                | 22.8 ms: 1.01x faster                                                    |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                                     |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.01x faster                                                     |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                     |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                     |
| sqlglot_optimize           | 54.8 ms                                                | 55.5 ms: 1.01x slower                                                    |
| docutils                   | 2.77 sec                                               | 2.81 sec: 1.02x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                    |
| mdp                        | 2.63 sec                                               | 2.71 sec: 1.03x slower                                                   |
| bench_thread_pool          | 842 us                                                 | 872 us: 1.04x slower                                                     |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                                     |
| telco                      | 7.10 ms                                                | 7.46 ms: 1.05x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                    |
| nqueens                    | 83.3 ms                                                | 89.5 ms: 1.07x slower                                                    |
| regex_v8                   | 23.1 ms                                                | 25.7 ms: 1.11x slower                                                    |
| hexiom                     | 6.41 ms                                                | 7.13 ms: 1.11x slower                                                    |
| generators                 | 31.2 ms                                                | 35.6 ms: 1.14x slower                                                    |
| coverage                   | 72.7 ms                                                | 84.8 ms: 1.17x slower                                                    |
| gc_traversal               | 3.79 ms                                                | 4.45 ms: 1.17x slower                                                    |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                    |
| create_gc_cycles           | 1.48 ms                                                | 2.66 ms: 1.80x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 79.4 ms: 3.31x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                             |

Benchmark hidden because not significant (2): pickle_pure_python, sympy_expand
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241120-3.14.0a2+-e2daeb7-JIT/bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.075x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.10x