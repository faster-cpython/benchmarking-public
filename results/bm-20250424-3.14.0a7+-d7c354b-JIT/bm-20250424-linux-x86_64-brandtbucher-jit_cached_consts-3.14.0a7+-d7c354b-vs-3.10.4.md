# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_cached_consts
- machine: linux-x86_64
- commit hash: d7c354b
- commit date: 2025-04-24
- overall geometric mean: 1.460x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-d7c354b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                                      |
| docutils       | 3.30 sec                                               | 2.67 sec: 1.24x faster                                                    |
| html5lib       | 88.9 ms                                                | 60.2 ms: 1.47x faster                                                     |
| Geometric mean | (ref)                                                  | 1.35x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-d7c354b |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 614 ms: 2.88x faster                                                      |
| async_tree_none         | 728 ms                                                 | 260 ms: 2.80x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 314 ms: 2.77x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 495 ms: 2.05x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-d7c354b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 87.1 ms: 1.76x faster                                                     |
| float          | 117 ms                                                 | 70.3 ms: 1.67x faster                                                     |
| pidigits       | 191 ms                                                 | 191 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.43x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-d7c354b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.49x faster                                                      |
| regex_v8       | 27.8 ms                                                | 23.8 ms: 1.17x faster                                                     |
| regex_effbot   | 3.63 ms                                                | 3.16 ms: 1.15x faster                                                     |
| regex_dna      | 227 ms                                                 | 202 ms: 1.12x faster                                                      |
| Geometric mean | (ref)                                                  | 1.22x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-d7c354b |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.85 sec: 1.69x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 209 us: 1.58x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 323 us: 1.50x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 56.3 ms: 1.40x faster                                                     |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.24x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 80.5 ms: 1.23x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 98.6 ms: 1.17x faster                                                     |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-d7c354b |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 8.21 ms: 1.38x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-d7c354b |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                     |
| django_template | 48.2 ms                                                | 32.5 ms: 1.48x faster                                                     |
| mako            | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 50.1 ms: 1.32x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-d7c354b |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 173 us: 3.15x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 614 ms: 2.88x faster                                                      |
| async_tree_none          | 728 ms                                                 | 260 ms: 2.80x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 314 ms: 2.77x faster                                                      |
| generators               | 80.1 ms                                                | 29.7 ms: 2.70x faster                                                     |
| deltablue                | 7.91 ms                                                | 2.99 ms: 2.65x faster                                                     |
| mdp                      | 2.85 sec                                               | 1.21 sec: 2.35x faster                                                    |
| richards_super           | 94.7 ms                                                | 40.8 ms: 2.32x faster                                                     |
| richards                 | 79.3 ms                                                | 35.6 ms: 2.23x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 495 ms: 2.05x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 29.3 us: 1.99x faster                                                     |
| chaos                    | 115 ms                                                 | 59.1 ms: 1.95x faster                                                     |
| pylint                   | 551 ms                                                 | 284 ms: 1.94x faster                                                      |
| go                       | 240 ms                                                 | 126 ms: 1.90x faster                                                      |
| deepcopy                 | 479 us                                                 | 252 us: 1.90x faster                                                      |
| logging_silent           | 190 ns                                                 | 100 ns: 1.89x faster                                                      |
| raytrace                 | 507 ms                                                 | 270 ms: 1.88x faster                                                      |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                      |
| nbody                    | 154 ms                                                 | 87.1 ms: 1.76x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 67.2 ms: 1.76x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 74.5 ms: 1.72x faster                                                     |
| pyflate                  | 716 ms                                                 | 422 ms: 1.70x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 1.85 sec: 1.69x faster                                                    |
| float                    | 117 ms                                                 | 70.3 ms: 1.67x faster                                                     |
| spectral_norm            | 170 ms                                                 | 105 ms: 1.62x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 209 us: 1.58x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.64 ms: 1.57x faster                                                     |
| comprehensions           | 28.8 us                                                | 18.5 us: 1.55x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                     |
| genshi_text              | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 323 us: 1.50x faster                                                      |
| regex_compile            | 188 ms                                                 | 126 ms: 1.49x faster                                                      |
| django_template          | 48.2 ms                                                | 32.5 ms: 1.48x faster                                                     |
| scimark_fft              | 466 ms                                                 | 315 ms: 1.48x faster                                                      |
| html5lib                 | 88.9 ms                                                | 60.2 ms: 1.47x faster                                                     |
| scimark_lu               | 176 ms                                                 | 120 ms: 1.47x faster                                                      |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.68 us: 1.46x faster                                                     |
| logging_format           | 9.09 us                                                | 6.25 us: 1.45x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 56.3 ms: 1.40x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 726 ms: 1.40x faster                                                      |
| coroutines               | 35.1 ms                                                | 25.4 ms: 1.38x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 61.0 ms: 1.38x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                                    |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.1 ms: 1.37x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.75 ms: 1.36x faster                                                     |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 19.3 ms: 1.33x faster                                                     |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 50.1 ms: 1.32x faster                                                     |
| fannkuch                 | 532 ms                                                 | 411 ms: 1.29x faster                                                      |
| nqueens                  | 106 ms                                                 | 81.8 ms: 1.29x faster                                                     |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.29x faster                                                      |
| sympy_str                | 346 ms                                                 | 270 ms: 1.28x faster                                                      |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.24x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.67 sec: 1.24x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 80.5 ms: 1.23x faster                                                     |
| sympy_expand             | 566 ms                                                 | 468 ms: 1.21x faster                                                      |
| pathlib                  | 20.5 ms                                                | 17.1 ms: 1.20x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 98.6 ms: 1.17x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 23.8 ms: 1.17x faster                                                     |
| regex_effbot             | 3.63 ms                                                | 3.16 ms: 1.15x faster                                                     |
| regex_dna                | 227 ms                                                 | 202 ms: 1.12x faster                                                      |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 895 us: 1.10x faster                                                      |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.78 us: 1.09x faster                                                     |
| async_generators         | 444 ms                                                 | 417 ms: 1.06x faster                                                      |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                                     |
| json                     | 5.69 ms                                                | 5.54 ms: 1.03x faster                                                     |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                      |
| pidigits                 | 191 ms                                                 | 191 ms: 1.00x faster                                                      |
| telco                    | 7.27 ms                                                | 7.65 ms: 1.05x slower                                                     |
| coverage                 | 79.4 ms                                                | 93.4 ms: 1.18x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 4.82 ms: 1.33x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 8.21 ms: 1.38x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.52x slower                                                     |
| bench_mp_pool            | 24.0 ms                                                | 81.4 ms: 3.39x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                              |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250424-3.14.0a7+-d7c354b-JIT/bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a7+-d7c354b.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.460x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.37x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.30x