# Results vs. 3.10.4

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-x86_64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.329x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 290 ms: 1.21x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.95 sec: 1.16x faster                                                       |
| html5lib       | 94.6 ms                                                      | 67.9 ms: 1.39x faster                                                        |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 650 ms: 2.46x faster                                                         |
| async_tree_none         | 692 ms                                                       | 289 ms: 2.39x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 352 ms: 2.33x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 522 ms: 1.79x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.23x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 70.1 ms: 1.58x faster                                                        |
| nbody          | 134 ms                                                       | 101 ms: 1.33x faster                                                         |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 137 ms: 1.38x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.0 ms: 1.09x faster                                                        |
| regex_dna      | 261 ms                                                       | 241 ms: 1.08x faster                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.11 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 206 us: 1.52x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.07 sec: 1.41x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 55.5 ms: 1.37x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 334 us: 1.36x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 11.8 ms: 1.24x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.18x faster                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 79.3 ms: 1.16x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 95.9 ms: 1.15x faster                                                        |
| json_loads           | 30.3 us                                                      | 26.6 us: 1.14x faster                                                        |
| unpickle_list        | 4.65 us                                                      | 4.83 us: 1.04x slower                                                        |
| unpickle             | 13.5 us                                                      | 14.2 us: 1.05x slower                                                        |
| pickle               | 9.89 us                                                      | 12.1 us: 1.23x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 37.3 us: 1.26x slower                                                        |
| pickle_list          | 4.12 us                                                      | 5.36 us: 1.30x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.10x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.01 ms: 1.23x slower                                                        |
| python_startup         | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.79 ms: 1.50x faster                                                        |
| django_template | 50.2 ms                                                      | 36.1 ms: 1.39x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 24.2 ms: 1.30x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 56.6 ms: 1.12x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.32x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 180 us: 2.98x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 650 ms: 2.46x faster                                                         |
| async_tree_none          | 692 ms                                                       | 289 ms: 2.39x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 352 ms: 2.33x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.45 ms: 2.18x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 364 ms: 2.14x faster                                                         |
| generators               | 57.3 ms                                                      | 29.1 ms: 1.97x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 522 ms: 1.79x faster                                                         |
| chaos                    | 109 ms                                                       | 61.0 ms: 1.78x faster                                                        |
| scimark_lu               | 167 ms                                                       | 94.6 ms: 1.76x faster                                                        |
| pylint                   | 566 ms                                                       | 322 ms: 1.76x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 61.1 ms: 1.76x faster                                                        |
| richards_super           | 90.6 ms                                                      | 52.1 ms: 1.74x faster                                                        |
| go                       | 262 ms                                                       | 151 ms: 1.73x faster                                                         |
| logging_silent           | 167 ns                                                       | 97.4 ns: 1.72x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 29.4 us: 1.69x faster                                                        |
| raytrace                 | 489 ms                                                       | 296 ms: 1.65x faster                                                         |
| scimark_sor              | 180 ms                                                       | 109 ms: 1.65x faster                                                         |
| spectral_norm            | 139 ms                                                       | 84.8 ms: 1.64x faster                                                        |
| richards                 | 75.1 ms                                                      | 45.8 ms: 1.64x faster                                                        |
| pyflate                  | 733 ms                                                       | 447 ms: 1.64x faster                                                         |
| deepcopy                 | 468 us                                                       | 286 us: 1.64x faster                                                         |
| sqlglot_parse            | 2.24 ms                                                      | 1.40 ms: 1.59x faster                                                        |
| float                    | 111 ms                                                       | 70.1 ms: 1.58x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 77.5 ms: 1.54x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 206 us: 1.52x faster                                                         |
| mako                     | 14.7 ms                                                      | 9.79 ms: 1.50x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.79 ms: 1.50x faster                                                        |
| coroutines               | 30.3 ms                                                      | 20.8 ms: 1.46x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.23 us: 1.42x faster                                                        |
| logging_format           | 9.64 us                                                      | 6.77 us: 1.42x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.07 sec: 1.41x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 67.9 ms: 1.39x faster                                                        |
| comprehensions           | 26.7 us                                                      | 19.2 us: 1.39x faster                                                        |
| django_template          | 50.2 ms                                                      | 36.1 ms: 1.39x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.89 us: 1.39x faster                                                        |
| regex_compile            | 190 ms                                                       | 137 ms: 1.38x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 55.5 ms: 1.37x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 334 us: 1.36x faster                                                         |
| thrift                   | 1.18 ms                                                      | 872 us: 1.35x faster                                                         |
| hexiom                   | 9.42 ms                                                      | 7.05 ms: 1.34x faster                                                        |
| nbody                    | 134 ms                                                       | 101 ms: 1.33x faster                                                         |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                                       |
| sqlalchemy_declarative   | 190 ms                                                       | 146 ms: 1.30x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 24.2 ms: 1.30x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.68 sec: 1.28x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 819 ms: 1.28x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 16.7 ms: 1.28x faster                                                        |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.0 ms: 1.26x faster                                                        |
| sympy_sum                | 193 ms                                                       | 154 ms: 1.25x faster                                                         |
| fannkuch                 | 483 ms                                                       | 387 ms: 1.25x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 11.8 ms: 1.24x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 119 ms: 1.21x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 67.1 ms: 1.21x faster                                                        |
| sympy_str                | 360 ms                                                       | 298 ms: 1.21x faster                                                         |
| 2to3                     | 350 ms                                                       | 290 ms: 1.21x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 23.6 ms: 1.19x faster                                                        |
| scimark_fft              | 361 ms                                                       | 304 ms: 1.19x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.18x faster                                                         |
| sympy_expand             | 600 ms                                                       | 512 ms: 1.17x faster                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 975 us: 1.17x faster                                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 60.0 ms: 1.17x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 79.3 ms: 1.16x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.59 sec: 1.16x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.95 sec: 1.16x faster                                                       |
| nqueens                  | 115 ms                                                       | 99.6 ms: 1.15x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 95.9 ms: 1.15x faster                                                        |
| json_loads               | 30.3 us                                                      | 26.6 us: 1.14x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 56.6 ms: 1.12x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.0 ms: 1.09x faster                                                        |
| regex_dna                | 261 ms                                                       | 241 ms: 1.08x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.77 us: 1.08x faster                                                        |
| json                     | 5.86 ms                                                      | 5.48 ms: 1.07x faster                                                        |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.82 ms: 1.05x faster                                                        |
| meteor_contest           | 138 ms                                                       | 133 ms: 1.04x faster                                                         |
| unpack_sequence          | 59.9 ns                                                      | 58.3 ns: 1.03x faster                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.11 ms: 1.01x slower                                                        |
| asyncio_websockets       | 390 ms                                                       | 394 ms: 1.01x slower                                                         |
| async_generators         | 421 ms                                                       | 434 ms: 1.03x slower                                                         |
| unpickle_list            | 4.65 us                                                      | 4.83 us: 1.04x slower                                                        |
| unpickle                 | 13.5 us                                                      | 14.2 us: 1.05x slower                                                        |
| telco                    | 7.23 ms                                                      | 7.59 ms: 1.05x slower                                                        |
| pickle                   | 9.89 us                                                      | 12.1 us: 1.23x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.01 ms: 1.23x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 37.3 us: 1.26x slower                                                        |
| coverage                 | 63.3 ms                                                      | 80.8 ms: 1.28x slower                                                        |
| pickle_list              | 4.12 us                                                      | 5.36 us: 1.30x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.67 ms: 1.51x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.29 ms: 1.84x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.23 sec: 193.60x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                                 |
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (11) of results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.329x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.29x