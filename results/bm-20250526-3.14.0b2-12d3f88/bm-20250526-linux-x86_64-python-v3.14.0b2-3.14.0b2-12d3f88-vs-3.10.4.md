# Results vs. 3.10.4

- fork: python
- ref: v3.14.0b2
- machine: linux-x86_64
- commit hash: 12d3f88
- commit date: 2025-05-26
- overall geometric mean: 1.441x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 258 ms: 1.35x faster                                       |
| docutils       | 3.30 sec                                               | 2.58 sec: 1.28x faster                                     |
| html5lib       | 88.9 ms                                                | 61.6 ms: 1.44x faster                                      |
| Geometric mean | (ref)                                                  | 1.35x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 595 ms: 2.97x faster                                       |
| async_tree_memoization  | 870 ms                                                 | 312 ms: 2.79x faster                                       |
| async_tree_none         | 728 ms                                                 | 265 ms: 2.75x faster                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 491 ms: 2.07x faster                                       |
| Geometric mean          | (ref)                                                  | 2.62x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 117 ms                                                 | 70.7 ms: 1.66x faster                                      |
| nbody          | 154 ms                                                 | 101 ms: 1.52x faster                                       |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                       |
| Geometric mean | (ref)                                                  | 1.37x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.48x faster                                       |
| regex_effbot   | 3.63 ms                                                | 2.93 ms: 1.24x faster                                      |
| regex_v8       | 27.8 ms                                                | 22.5 ms: 1.24x faster                                      |
| regex_dna      | 227 ms                                                 | 194 ms: 1.17x faster                                       |
| Geometric mean | (ref)                                                  | 1.27x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.02 sec: 1.56x faster                                     |
| pickle_pure_python   | 484 us                                                 | 322 us: 1.50x faster                                       |
| unpickle_pure_python | 331 us                                                 | 223 us: 1.48x faster                                       |
| xml_etree_process    | 79.1 ms                                                | 61.0 ms: 1.30x faster                                      |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.27x faster                                      |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                       |
| xml_etree_iterparse  | 115 ms                                                 | 98.9 ms: 1.17x faster                                      |
| xml_etree_generate   | 99.4 ms                                                | 85.2 ms: 1.17x faster                                      |
| json_loads           | 31.2 us                                                | 30.2 us: 1.03x faster                                      |
| Geometric mean       | (ref)                                                  | 1.28x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                      |
| python_startup_no_site | 5.93 ms                                                | 6.91 ms: 1.17x slower                                      |
| Geometric mean         | (ref)                                                  | 1.02x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.5 ms: 1.48x faster                                      |
| genshi_text     | 31.8 ms                                                | 21.6 ms: 1.47x faster                                      |
| mako            | 16.3 ms                                                | 11.4 ms: 1.44x faster                                      |
| genshi_xml      | 66.0 ms                                                | 49.9 ms: 1.32x faster                                      |
| Geometric mean  | (ref)                                                  | 1.43x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                       |
| async_tree_io            | 1.77 sec                                               | 595 ms: 2.97x faster                                       |
| async_tree_memoization   | 870 ms                                                 | 312 ms: 2.79x faster                                       |
| async_tree_none          | 728 ms                                                 | 265 ms: 2.75x faster                                       |
| generators               | 80.1 ms                                                | 31.3 ms: 2.56x faster                                      |
| deltablue                | 7.91 ms                                                | 3.44 ms: 2.30x faster                                      |
| mdp                      | 2.85 sec                                               | 1.24 sec: 2.29x faster                                     |
| go                       | 240 ms                                                 | 115 ms: 2.09x faster                                       |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 491 ms: 2.07x faster                                       |
| deepcopy_memo            | 58.5 us                                                | 29.6 us: 1.98x faster                                      |
| pylint                   | 551 ms                                                 | 280 ms: 1.97x faster                                       |
| chaos                    | 115 ms                                                 | 60.1 ms: 1.92x faster                                      |
| richards_super           | 94.7 ms                                                | 49.4 ms: 1.92x faster                                      |
| deepcopy                 | 479 us                                                 | 255 us: 1.88x faster                                       |
| raytrace                 | 507 ms                                                 | 273 ms: 1.86x faster                                       |
| richards                 | 79.3 ms                                                | 43.1 ms: 1.84x faster                                      |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.82x faster                                       |
| scimark_monte_carlo      | 118 ms                                                 | 68.6 ms: 1.72x faster                                      |
| crypto_pyaes             | 128 ms                                                 | 75.0 ms: 1.70x faster                                      |
| hexiom                   | 10.4 ms                                                | 6.16 ms: 1.69x faster                                      |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.68x faster                                      |
| float                    | 117 ms                                                 | 70.7 ms: 1.66x faster                                      |
| pyflate                  | 716 ms                                                 | 451 ms: 1.59x faster                                       |
| spectral_norm            | 170 ms                                                 | 107 ms: 1.58x faster                                       |
| tomli_loads              | 3.14 sec                                               | 2.02 sec: 1.56x faster                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                      |
| nbody                    | 154 ms                                                 | 101 ms: 1.52x faster                                       |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                       |
| pickle_pure_python       | 484 us                                                 | 322 us: 1.50x faster                                       |
| django_template          | 48.2 ms                                                | 32.5 ms: 1.48x faster                                      |
| unpickle_pure_python     | 331 us                                                 | 223 us: 1.48x faster                                       |
| regex_compile            | 188 ms                                                 | 128 ms: 1.48x faster                                       |
| genshi_text              | 31.8 ms                                                | 21.6 ms: 1.47x faster                                      |
| html5lib                 | 88.9 ms                                                | 61.6 ms: 1.44x faster                                      |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.44x faster                                      |
| dulwich_log              | 84.3 ms                                                | 59.6 ms: 1.41x faster                                      |
| coroutines               | 35.1 ms                                                | 25.0 ms: 1.40x faster                                      |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                     |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                     |
| pprint_safe_repr         | 1.02 sec                                               | 738 ms: 1.38x faster                                       |
| logging_simple           | 8.30 us                                                | 6.09 us: 1.36x faster                                      |
| 2to3                     | 348 ms                                                 | 258 ms: 1.35x faster                                       |
| sympy_integrate          | 25.8 ms                                                | 19.1 ms: 1.35x faster                                      |
| logging_format           | 9.09 us                                                | 6.74 us: 1.35x faster                                      |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.5 ms: 1.33x faster                                      |
| genshi_xml               | 66.0 ms                                                | 49.9 ms: 1.32x faster                                      |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                       |
| xml_etree_process        | 79.1 ms                                                | 61.0 ms: 1.30x faster                                      |
| nqueens                  | 106 ms                                                 | 81.8 ms: 1.29x faster                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.01 ms: 1.29x faster                                      |
| sympy_str                | 346 ms                                                 | 269 ms: 1.28x faster                                       |
| sqlalchemy_declarative   | 172 ms                                                 | 135 ms: 1.28x faster                                       |
| fannkuch                 | 532 ms                                                 | 417 ms: 1.28x faster                                       |
| docutils                 | 3.30 sec                                               | 2.58 sec: 1.28x faster                                     |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.27x faster                                      |
| scimark_fft              | 466 ms                                                 | 369 ms: 1.26x faster                                       |
| regex_effbot             | 3.63 ms                                                | 2.93 ms: 1.24x faster                                      |
| regex_v8                 | 27.8 ms                                                | 22.5 ms: 1.24x faster                                      |
| sympy_expand             | 566 ms                                                 | 463 ms: 1.22x faster                                       |
| pathlib                  | 20.5 ms                                                | 17.1 ms: 1.20x faster                                      |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                       |
| regex_dna                | 227 ms                                                 | 194 ms: 1.17x faster                                       |
| xml_etree_iterparse      | 115 ms                                                 | 98.9 ms: 1.17x faster                                      |
| xml_etree_generate       | 99.4 ms                                                | 85.2 ms: 1.17x faster                                      |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                       |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                      |
| async_generators         | 444 ms                                                 | 413 ms: 1.07x faster                                       |
| json                     | 5.69 ms                                                | 5.39 ms: 1.06x faster                                      |
| sqlite_synth             | 3.02 us                                                | 2.88 us: 1.05x faster                                      |
| json_loads               | 31.2 us                                                | 30.2 us: 1.03x faster                                      |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                       |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                       |
| telco                    | 7.27 ms                                                | 7.92 ms: 1.09x slower                                      |
| coverage                 | 79.4 ms                                                | 88.0 ms: 1.11x slower                                      |
| python_startup_no_site   | 5.93 ms                                                | 6.91 ms: 1.17x slower                                      |
| gc_traversal             | 3.62 ms                                                | 4.96 ms: 1.37x slower                                      |
| create_gc_cycles         | 1.62 ms                                                | 2.58 ms: 1.59x slower                                      |
| logging_silent           | 190 ns                                                 | 473 ns: 2.50x slower                                       |
| Geometric mean           | (ref)                                                  | 1.42x faster                                               |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250526-3.14.0b2-12d3f88/bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.441x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.31x