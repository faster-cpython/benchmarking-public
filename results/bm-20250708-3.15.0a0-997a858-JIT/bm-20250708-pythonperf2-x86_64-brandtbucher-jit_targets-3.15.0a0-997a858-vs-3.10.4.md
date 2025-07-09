# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_targets
- machine: linux-x86_64
- commit hash: 997a858
- commit date: 2025-07-08
- overall geometric mean: 1.327x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.41x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 287 ms: 1.22x faster                                                     |
| docutils       | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                   |
| html5lib       | 94.6 ms                                                      | 66.4 ms: 1.43x faster                                                    |
| Geometric mean | (ref)                                                        | 1.27x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 626 ms: 2.55x faster                                                     |
| async_tree_none         | 692 ms                                                       | 276 ms: 2.50x faster                                                     |
| async_tree_memoization  | 819 ms                                                       | 330 ms: 2.48x faster                                                     |
| async_tree_cpu_io_mixed | 936 ms                                                       | 503 ms: 1.86x faster                                                     |
| Geometric mean          | (ref)                                                        | 2.33x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 63.6 ms: 1.75x faster                                                    |
| nbody          | 134 ms                                                       | 101 ms: 1.33x faster                                                     |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                     |
| Geometric mean | (ref)                                                        | 1.35x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 133 ms: 1.43x faster                                                     |
| regex_v8       | 27.2 ms                                                      | 23.3 ms: 1.16x faster                                                    |
| regex_dna      | 261 ms                                                       | 227 ms: 1.15x faster                                                     |
| regex_effbot   | 3.09 ms                                                      | 3.65 ms: 1.18x slower                                                    |
| Geometric mean | (ref)                                                        | 1.13x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 196 us: 1.60x faster                                                     |
| tomli_loads          | 2.92 sec                                                     | 1.93 sec: 1.51x faster                                                   |
| pickle_pure_python   | 455 us                                                       | 331 us: 1.38x faster                                                     |
| xml_etree_process    | 75.9 ms                                                      | 55.7 ms: 1.36x faster                                                    |
| json_dumps           | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                    |
| json_loads           | 30.3 us                                                      | 25.3 us: 1.20x faster                                                    |
| xml_etree_generate   | 92.3 ms                                                      | 79.4 ms: 1.16x faster                                                    |
| xml_etree_parse      | 160 ms                                                       | 141 ms: 1.13x faster                                                     |
| xml_etree_iterparse  | 110 ms                                                       | 98.9 ms: 1.12x faster                                                    |
| Geometric mean       | (ref)                                                        | 1.30x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.87 ms: 1.21x slower                                                    |
| python_startup         | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                                    |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.94 ms: 1.48x faster                                                    |
| django_template | 50.2 ms                                                      | 35.0 ms: 1.43x faster                                                    |
| genshi_text     | 31.4 ms                                                      | 23.3 ms: 1.35x faster                                                    |
| genshi_xml      | 63.3 ms                                                      | 54.4 ms: 1.16x faster                                                    |
| Geometric mean  | (ref)                                                        | 1.35x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 170 us: 3.16x faster                                                     |
| deltablue                | 7.50 ms                                                      | 2.89 ms: 2.59x faster                                                    |
| async_tree_io            | 1.60 sec                                                     | 626 ms: 2.55x faster                                                     |
| async_tree_none          | 692 ms                                                       | 276 ms: 2.50x faster                                                     |
| async_tree_memoization   | 819 ms                                                       | 330 ms: 2.48x faster                                                     |
| mdp                      | 3.01 sec                                                     | 1.29 sec: 2.33x faster                                                   |
| richards_super           | 90.6 ms                                                      | 40.8 ms: 2.22x faster                                                    |
| richards                 | 75.1 ms                                                      | 34.4 ms: 2.18x faster                                                    |
| go                       | 262 ms                                                       | 128 ms: 2.04x faster                                                     |
| generators               | 57.3 ms                                                      | 29.7 ms: 1.93x faster                                                    |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 503 ms: 1.86x faster                                                     |
| chaos                    | 109 ms                                                       | 60.1 ms: 1.81x faster                                                    |
| logging_silent           | 167 ns                                                       | 93.4 ns: 1.79x faster                                                    |
| deepcopy_memo            | 49.8 us                                                      | 27.9 us: 1.79x faster                                                    |
| scimark_sor              | 180 ms                                                       | 102 ms: 1.76x faster                                                     |
| float                    | 111 ms                                                       | 63.6 ms: 1.75x faster                                                    |
| pylint                   | 566 ms                                                       | 326 ms: 1.74x faster                                                     |
| scimark_lu               | 167 ms                                                       | 96.2 ms: 1.73x faster                                                    |
| pyflate                  | 733 ms                                                       | 427 ms: 1.72x faster                                                     |
| raytrace                 | 489 ms                                                       | 289 ms: 1.69x faster                                                     |
| scimark_monte_carlo      | 107 ms                                                       | 63.7 ms: 1.69x faster                                                    |
| deepcopy                 | 468 us                                                       | 279 us: 1.68x faster                                                     |
| spectral_norm            | 139 ms                                                       | 83.0 ms: 1.68x faster                                                    |
| unpickle_pure_python     | 312 us                                                       | 196 us: 1.60x faster                                                     |
| crypto_pyaes             | 119 ms                                                       | 77.3 ms: 1.54x faster                                                    |
| comprehensions           | 26.7 us                                                      | 17.3 us: 1.54x faster                                                    |
| hexiom                   | 9.42 ms                                                      | 6.17 ms: 1.53x faster                                                    |
| tomli_loads              | 2.92 sec                                                     | 1.93 sec: 1.51x faster                                                   |
| mako                     | 14.7 ms                                                      | 9.94 ms: 1.48x faster                                                    |
| django_template          | 50.2 ms                                                      | 35.0 ms: 1.43x faster                                                    |
| regex_compile            | 190 ms                                                       | 133 ms: 1.43x faster                                                     |
| html5lib                 | 94.6 ms                                                      | 66.4 ms: 1.43x faster                                                    |
| logging_simple           | 8.88 us                                                      | 6.24 us: 1.42x faster                                                    |
| thrift                   | 1.18 ms                                                      | 837 us: 1.40x faster                                                     |
| pprint_pformat           | 2.15 sec                                                     | 1.54 sec: 1.40x faster                                                   |
| logging_format           | 9.64 us                                                      | 6.89 us: 1.40x faster                                                    |
| dulwich_log              | 81.1 ms                                                      | 58.6 ms: 1.38x faster                                                    |
| pickle_pure_python       | 455 us                                                       | 331 us: 1.38x faster                                                     |
| pprint_safe_repr         | 1.05 sec                                                     | 766 ms: 1.37x faster                                                     |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.36x faster                                                   |
| coroutines               | 30.3 ms                                                      | 22.2 ms: 1.36x faster                                                    |
| xml_etree_process        | 75.9 ms                                                      | 55.7 ms: 1.36x faster                                                    |
| genshi_text              | 31.4 ms                                                      | 23.3 ms: 1.35x faster                                                    |
| deepcopy_reduce          | 4.01 us                                                      | 3.00 us: 1.34x faster                                                    |
| nbody                    | 134 ms                                                       | 101 ms: 1.33x faster                                                     |
| json_dumps               | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                    |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.28x faster                                                     |
| fannkuch                 | 483 ms                                                       | 384 ms: 1.26x faster                                                     |
| sympy_integrate          | 28.2 ms                                                      | 22.4 ms: 1.26x faster                                                    |
| pathlib                  | 21.4 ms                                                      | 17.1 ms: 1.25x faster                                                    |
| sympy_str                | 360 ms                                                       | 291 ms: 1.24x faster                                                     |
| nqueens                  | 115 ms                                                       | 93.2 ms: 1.23x faster                                                    |
| 2to3                     | 350 ms                                                       | 287 ms: 1.22x faster                                                     |
| json_loads               | 30.3 us                                                      | 25.3 us: 1.20x faster                                                    |
| sympy_expand             | 600 ms                                                       | 502 ms: 1.20x faster                                                     |
| docutils                 | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                   |
| regex_v8                 | 27.2 ms                                                      | 23.3 ms: 1.16x faster                                                    |
| genshi_xml               | 63.3 ms                                                      | 54.4 ms: 1.16x faster                                                    |
| xml_etree_generate       | 92.3 ms                                                      | 79.4 ms: 1.16x faster                                                    |
| scimark_fft              | 361 ms                                                       | 313 ms: 1.16x faster                                                     |
| regex_dna                | 261 ms                                                       | 227 ms: 1.15x faster                                                     |
| xml_etree_parse          | 160 ms                                                       | 141 ms: 1.13x faster                                                     |
| meteor_contest           | 138 ms                                                       | 123 ms: 1.12x faster                                                     |
| xml_etree_iterparse      | 110 ms                                                       | 98.9 ms: 1.12x faster                                                    |
| json                     | 5.86 ms                                                      | 5.37 ms: 1.09x faster                                                    |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                     |
| sqlite_synth             | 2.99 us                                                      | 2.86 us: 1.05x faster                                                    |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.18 ms: 1.02x slower                                                    |
| async_generators         | 421 ms                                                       | 445 ms: 1.06x slower                                                     |
| regex_effbot             | 3.09 ms                                                      | 3.65 ms: 1.18x slower                                                    |
| python_startup_no_site   | 7.33 ms                                                      | 8.87 ms: 1.21x slower                                                    |
| coverage                 | 63.3 ms                                                      | 77.9 ms: 1.23x slower                                                    |
| python_startup           | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                                    |
| create_gc_cycles         | 1.76 ms                                                      | 2.90 ms: 1.64x slower                                                    |
| gc_traversal             | 3.42 ms                                                      | 6.49 ms: 1.90x slower                                                    |
| telco                    | 7.23 ms                                                      | 161 ms: 22.25x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.33x faster                                                             |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250708-3.15.0a0-997a858-JIT/bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.327x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.41x