# Results vs. 3.10.4

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: linux-x86_64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.371x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 278 ms: 1.26x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.83 sec: 1.21x faster                                                       |
| html5lib       | 94.6 ms                                                      | 66.6 ms: 1.42x faster                                                        |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 639 ms: 2.50x faster                                                         |
| async_tree_none         | 692 ms                                                       | 283 ms: 2.45x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 344 ms: 2.38x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 514 ms: 1.82x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.27x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 69.5 ms: 1.60x faster                                                        |
| nbody          | 134 ms                                                       | 88.0 ms: 1.52x faster                                                        |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.38x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 132 ms: 1.44x faster                                                         |
| regex_dna      | 261 ms                                                       | 236 ms: 1.10x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 26.0 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 210 us: 1.49x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.03 sec: 1.43x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 325 us: 1.40x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 58.4 ms: 1.30x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.6 ms: 1.25x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 137 ms: 1.17x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 96.1 ms: 1.15x faster                                                        |
| json_loads           | 30.3 us                                                      | 26.5 us: 1.14x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 83.4 ms: 1.11x faster                                                        |
| unpickle             | 13.5 us                                                      | 14.1 us: 1.05x slower                                                        |
| unpickle_list        | 4.65 us                                                      | 4.92 us: 1.06x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 34.9 us: 1.18x slower                                                        |
| pickle               | 9.89 us                                                      | 12.4 us: 1.26x slower                                                        |
| pickle_list          | 4.12 us                                                      | 5.42 us: 1.31x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.10x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.02 ms: 1.23x slower                                                        |
| python_startup         | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 34.9 ms: 1.44x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 23.2 ms: 1.36x faster                                                        |
| mako            | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 52.4 ms: 1.21x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.34x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 169 us: 3.17x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 639 ms: 2.50x faster                                                         |
| async_tree_none          | 692 ms                                                       | 283 ms: 2.45x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 344 ms: 2.38x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.24 ms: 2.31x faster                                                        |
| go                       | 262 ms                                                       | 122 ms: 2.15x faster                                                         |
| asyncio_tcp              | 779 ms                                                       | 373 ms: 2.09x faster                                                         |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                       |
| generators               | 57.3 ms                                                      | 29.4 ms: 1.95x faster                                                        |
| raytrace                 | 489 ms                                                       | 264 ms: 1.85x faster                                                         |
| chaos                    | 109 ms                                                       | 59.3 ms: 1.83x faster                                                        |
| pylint                   | 566 ms                                                       | 310 ms: 1.82x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 514 ms: 1.82x faster                                                         |
| scimark_lu               | 167 ms                                                       | 93.4 ms: 1.79x faster                                                        |
| richards_super           | 90.6 ms                                                      | 51.9 ms: 1.75x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 61.7 ms: 1.74x faster                                                        |
| logging_silent           | 167 ns                                                       | 96.5 ns: 1.73x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.30 ms: 1.72x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 29.6 us: 1.68x faster                                                        |
| spectral_norm            | 139 ms                                                       | 83.2 ms: 1.67x faster                                                        |
| deepcopy                 | 468 us                                                       | 280 us: 1.67x faster                                                         |
| scimark_sor              | 180 ms                                                       | 109 ms: 1.66x faster                                                         |
| pyflate                  | 733 ms                                                       | 443 ms: 1.66x faster                                                         |
| richards                 | 75.1 ms                                                      | 45.4 ms: 1.65x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 72.2 ms: 1.65x faster                                                        |
| float                    | 111 ms                                                       | 69.5 ms: 1.60x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.68 ms: 1.59x faster                                                        |
| comprehensions           | 26.7 us                                                      | 16.9 us: 1.58x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.04 ms: 1.56x faster                                                        |
| nbody                    | 134 ms                                                       | 88.0 ms: 1.52x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 210 us: 1.49x faster                                                         |
| logging_simple           | 8.88 us                                                      | 6.02 us: 1.48x faster                                                        |
| logging_format           | 9.64 us                                                      | 6.59 us: 1.46x faster                                                        |
| coroutines               | 30.3 ms                                                      | 20.9 ms: 1.45x faster                                                        |
| django_template          | 50.2 ms                                                      | 34.9 ms: 1.44x faster                                                        |
| regex_compile            | 190 ms                                                       | 132 ms: 1.44x faster                                                         |
| tomli_loads              | 2.92 sec                                                     | 2.03 sec: 1.43x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 66.6 ms: 1.42x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 325 us: 1.40x faster                                                         |
| pycparser                | 1.67 sec                                                     | 1.20 sec: 1.39x faster                                                       |
| fannkuch                 | 483 ms                                                       | 349 ms: 1.38x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 2.91 us: 1.38x faster                                                        |
| thrift                   | 1.18 ms                                                      | 854 us: 1.38x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.57 sec: 1.37x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 15.6 ms: 1.37x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 771 ms: 1.36x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 23.2 ms: 1.36x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 141 ms: 1.34x faster                                                         |
| unpack_sequence          | 59.9 ns                                                      | 45.7 ns: 1.31x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 58.4 ms: 1.30x faster                                                        |
| nqueens                  | 115 ms                                                       | 89.0 ms: 1.29x faster                                                        |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.6 ms: 1.29x faster                                                        |
| sympy_sum                | 193 ms                                                       | 150 ms: 1.29x faster                                                         |
| sqlglot_normalize        | 144 ms                                                       | 114 ms: 1.27x faster                                                         |
| 2to3                     | 350 ms                                                       | 278 ms: 1.26x faster                                                         |
| sympy_str                | 360 ms                                                       | 287 ms: 1.26x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 11.6 ms: 1.25x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 56.1 ms: 1.25x faster                                                        |
| sympy_expand             | 600 ms                                                       | 486 ms: 1.23x faster                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 925 us: 1.23x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 65.8 ms: 1.23x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 22.9 ms: 1.23x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 52.4 ms: 1.21x faster                                                        |
| scimark_fft              | 361 ms                                                       | 300 ms: 1.21x faster                                                         |
| docutils                 | 3.41 sec                                                     | 2.83 sec: 1.21x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.50 sec: 1.20x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 137 ms: 1.17x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 96.1 ms: 1.15x faster                                                        |
| json_loads               | 30.3 us                                                      | 26.5 us: 1.14x faster                                                        |
| meteor_contest           | 138 ms                                                       | 123 ms: 1.13x faster                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.55 ms: 1.12x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 83.4 ms: 1.11x faster                                                        |
| regex_dna                | 261 ms                                                       | 236 ms: 1.10x faster                                                         |
| json                     | 5.86 ms                                                      | 5.45 ms: 1.08x faster                                                        |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.83 us: 1.06x faster                                                        |
| async_generators         | 421 ms                                                       | 401 ms: 1.05x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 26.0 ms: 1.04x faster                                                        |
| unpickle                 | 13.5 us                                                      | 14.1 us: 1.05x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 4.92 us: 1.06x slower                                                        |
| telco                    | 7.23 ms                                                      | 7.88 ms: 1.09x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 34.9 us: 1.18x slower                                                        |
| coverage                 | 63.3 ms                                                      | 76.8 ms: 1.21x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.02 ms: 1.23x slower                                                        |
| pickle                   | 9.89 us                                                      | 12.4 us: 1.26x slower                                                        |
| pickle_list              | 4.12 us                                                      | 5.42 us: 1.31x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.77 ms: 1.57x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.23 ms: 1.82x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.76 sec: 275.99x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.27x faster                                                                 |

Benchmark hidden because not significant (2): asyncio_websockets, regex_effbot
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (11) of results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-pythonperf2-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.371x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.27x