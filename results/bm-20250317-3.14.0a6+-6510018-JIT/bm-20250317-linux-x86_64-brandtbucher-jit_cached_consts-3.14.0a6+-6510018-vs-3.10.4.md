# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_cached_consts
- machine: linux-x86_64
- commit hash: 6510018
- commit date: 2025-03-17
- overall geometric mean: 1.451x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 261 ms: 1.34x faster                                                      |
| docutils       | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                    |
| html5lib       | 88.9 ms                                                | 62.6 ms: 1.42x faster                                                     |
| Geometric mean | (ref)                                                  | 1.33x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 609 ms: 2.90x faster                                                      |
| async_tree_none         | 728 ms                                                 | 255 ms: 2.85x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 314 ms: 2.77x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 490 ms: 2.07x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.63x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 64.8 ms: 1.81x faster                                                     |
| nbody          | 154 ms                                                 | 88.5 ms: 1.73x faster                                                     |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.48x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.49x faster                                                      |
| regex_v8       | 27.8 ms                                                | 23.2 ms: 1.20x faster                                                     |
| regex_effbot   | 3.63 ms                                                | 3.47 ms: 1.04x faster                                                     |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.18x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.86 sec: 1.69x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 212 us: 1.56x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 320 us: 1.52x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 55.5 ms: 1.43x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 79.2 ms: 1.26x faster                                                     |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 97.6 ms: 1.18x faster                                                     |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 8.20 ms: 1.38x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.6 ms: 1.52x faster                                                     |
| genshi_text     | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                     |
| mako            | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 50.3 ms: 1.31x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.24x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 609 ms: 2.90x faster                                                      |
| generators               | 80.1 ms                                                | 27.9 ms: 2.87x faster                                                     |
| async_tree_none          | 728 ms                                                 | 255 ms: 2.85x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 314 ms: 2.77x faster                                                      |
| deltablue                | 7.91 ms                                                | 2.97 ms: 2.66x faster                                                     |
| richards_super           | 94.7 ms                                                | 39.7 ms: 2.39x faster                                                     |
| richards                 | 79.3 ms                                                | 34.6 ms: 2.29x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 490 ms: 2.07x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 28.5 us: 2.05x faster                                                     |
| pylint                   | 551 ms                                                 | 281 ms: 1.96x faster                                                      |
| logging_silent           | 190 ns                                                 | 96.7 ns: 1.96x faster                                                     |
| chaos                    | 115 ms                                                 | 59.0 ms: 1.96x faster                                                     |
| raytrace                 | 507 ms                                                 | 265 ms: 1.91x faster                                                      |
| deepcopy                 | 479 us                                                 | 254 us: 1.89x faster                                                      |
| scimark_sor              | 220 ms                                                 | 116 ms: 1.89x faster                                                      |
| go                       | 240 ms                                                 | 129 ms: 1.87x faster                                                      |
| float                    | 117 ms                                                 | 64.8 ms: 1.81x faster                                                     |
| spectral_norm            | 170 ms                                                 | 94.3 ms: 1.80x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 66.9 ms: 1.77x faster                                                     |
| nbody                    | 154 ms                                                 | 88.5 ms: 1.73x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.86 sec: 1.69x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 78.1 ms: 1.64x faster                                                     |
| pyflate                  | 716 ms                                                 | 449 ms: 1.60x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 212 us: 1.56x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.77 ms: 1.54x faster                                                     |
| comprehensions           | 28.8 us                                                | 18.8 us: 1.53x faster                                                     |
| django_template          | 48.2 ms                                                | 31.6 ms: 1.52x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 320 us: 1.52x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.48 us: 1.51x faster                                                     |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                      |
| genshi_text              | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                     |
| logging_format           | 9.09 us                                                | 6.05 us: 1.50x faster                                                     |
| scimark_fft              | 466 ms                                                 | 310 ms: 1.50x faster                                                      |
| regex_compile            | 188 ms                                                 | 126 ms: 1.49x faster                                                      |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                     |
| coroutines               | 35.1 ms                                                | 24.0 ms: 1.46x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 55.5 ms: 1.43x faster                                                     |
| html5lib                 | 88.9 ms                                                | 62.6 ms: 1.42x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 60.0 ms: 1.40x faster                                                     |
| thrift                   | 1.07 ms                                                | 765 us: 1.40x faster                                                      |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.71 ms: 1.37x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 745 ms: 1.37x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.57 sec: 1.34x faster                                                    |
| 2to3                     | 348 ms                                                 | 261 ms: 1.34x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 50.3 ms: 1.31x faster                                                     |
| sqlalchemy_declarative   | 172 ms                                                 | 132 ms: 1.30x faster                                                      |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 20.1 ms: 1.28x faster                                                     |
| sympy_str                | 346 ms                                                 | 274 ms: 1.26x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 79.2 ms: 1.26x faster                                                     |
| nqueens                  | 106 ms                                                 | 84.4 ms: 1.25x faster                                                     |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.24x faster                                                     |
| fannkuch                 | 532 ms                                                 | 430 ms: 1.24x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                    |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                      |
| sympy_expand             | 566 ms                                                 | 471 ms: 1.20x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 23.2 ms: 1.20x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 97.6 ms: 1.18x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.46 sec: 1.16x faster                                                    |
| bench_thread_pool        | 986 us                                                 | 874 us: 1.13x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.70 us: 1.12x faster                                                     |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                     |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                      |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                                     |
| async_generators         | 444 ms                                                 | 415 ms: 1.07x faster                                                      |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                                     |
| regex_effbot             | 3.63 ms                                                | 3.47 ms: 1.04x faster                                                     |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                                      |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                      |
| coverage                 | 79.4 ms                                                | 84.5 ms: 1.06x slower                                                     |
| telco                    | 7.27 ms                                                | 7.80 ms: 1.07x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 4.91 ms: 1.36x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 8.20 ms: 1.38x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 2.49 ms: 1.54x slower                                                     |
| bench_mp_pool            | 24.0 ms                                                | 82.9 ms: 3.45x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                              |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250317-3.14.0a6+-6510018-JIT/bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.451x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.29x