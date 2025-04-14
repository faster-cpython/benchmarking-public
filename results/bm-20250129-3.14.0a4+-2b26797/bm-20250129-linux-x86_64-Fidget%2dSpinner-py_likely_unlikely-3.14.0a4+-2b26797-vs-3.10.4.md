# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: py_likely_unlikely
- machine: linux-x86_64
- commit hash: 2b26797
- commit date: 2025-01-29
- overall geometric mean: 1.448x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 252 ms: 1.38x faster                                                           |
| docutils       | 3.30 sec                                               | 2.58 sec: 1.28x faster                                                         |
| html5lib       | 88.9 ms                                                | 61.1 ms: 1.45x faster                                                          |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 617 ms: 2.86x faster                                                           |
| async_tree_none         | 728 ms                                                 | 266 ms: 2.74x faster                                                           |
| async_tree_memoization  | 870 ms                                                 | 331 ms: 2.63x faster                                                           |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 496 ms: 2.05x faster                                                           |
| Geometric mean          | (ref)                                                  | 2.55x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.6 ms: 1.66x faster                                                          |
| nbody          | 154 ms                                                 | 93.0 ms: 1.65x faster                                                          |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                  | 1.41x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.49x faster                                                           |
| regex_effbot   | 3.63 ms                                                | 3.38 ms: 1.07x faster                                                          |
| regex_v8       | 27.8 ms                                                | 26.0 ms: 1.07x faster                                                          |
| regex_dna      | 227 ms                                                 | 213 ms: 1.06x faster                                                           |
| Geometric mean | (ref)                                                  | 1.16x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.98 sec: 1.59x faster                                                         |
| pickle_pure_python   | 484 us                                                 | 314 us: 1.54x faster                                                           |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                           |
| xml_etree_process    | 79.1 ms                                                | 59.0 ms: 1.34x faster                                                          |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                           |
| json_dumps           | 14.2 ms                                                | 11.9 ms: 1.19x faster                                                          |
| xml_etree_generate   | 99.4 ms                                                | 83.9 ms: 1.18x faster                                                          |
| xml_etree_iterparse  | 115 ms                                                 | 98.2 ms: 1.18x faster                                                          |
| json_loads           | 31.2 us                                                | 29.1 us: 1.07x faster                                                          |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                          |
| python_startup_no_site | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                          |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.0 ms: 1.50x faster                                                          |
| genshi_text     | 31.8 ms                                                | 21.7 ms: 1.47x faster                                                          |
| mako            | 16.3 ms                                                | 11.4 ms: 1.44x faster                                                          |
| genshi_xml      | 66.0 ms                                                | 48.4 ms: 1.36x faster                                                          |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.36x faster                                                           |
| generators               | 80.1 ms                                                | 27.7 ms: 2.89x faster                                                          |
| async_tree_io            | 1.77 sec                                               | 617 ms: 2.86x faster                                                           |
| async_tree_none          | 728 ms                                                 | 266 ms: 2.74x faster                                                           |
| async_tree_memoization   | 870 ms                                                 | 331 ms: 2.63x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.22 ms: 2.46x faster                                                          |
| go                       | 240 ms                                                 | 117 ms: 2.05x faster                                                           |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 496 ms: 2.05x faster                                                           |
| pylint                   | 551 ms                                                 | 274 ms: 2.01x faster                                                           |
| chaos                    | 115 ms                                                 | 58.3 ms: 1.98x faster                                                          |
| deepcopy_memo            | 58.5 us                                                | 30.8 us: 1.90x faster                                                          |
| richards_super           | 94.7 ms                                                | 50.2 ms: 1.89x faster                                                          |
| deepcopy                 | 479 us                                                 | 256 us: 1.87x faster                                                           |
| raytrace                 | 507 ms                                                 | 272 ms: 1.86x faster                                                           |
| richards                 | 79.3 ms                                                | 43.8 ms: 1.81x faster                                                          |
| logging_silent           | 190 ns                                                 | 105 ns: 1.80x faster                                                           |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.79x faster                                                           |
| spectral_norm            | 170 ms                                                 | 94.9 ms: 1.79x faster                                                          |
| crypto_pyaes             | 128 ms                                                 | 71.4 ms: 1.79x faster                                                          |
| scimark_monte_carlo      | 118 ms                                                 | 67.4 ms: 1.75x faster                                                          |
| sqlglot_parse            | 2.17 ms                                                | 1.25 ms: 1.73x faster                                                          |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                          |
| hexiom                   | 10.4 ms                                                | 6.19 ms: 1.68x faster                                                          |
| float                    | 117 ms                                                 | 70.6 ms: 1.66x faster                                                          |
| nbody                    | 154 ms                                                 | 93.0 ms: 1.65x faster                                                          |
| sqlglot_transpile        | 2.57 ms                                                | 1.56 ms: 1.65x faster                                                          |
| deepcopy_reduce          | 4.17 us                                                | 2.62 us: 1.59x faster                                                          |
| tomli_loads              | 3.14 sec                                               | 1.98 sec: 1.59x faster                                                         |
| pyflate                  | 716 ms                                                 | 458 ms: 1.56x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 314 us: 1.54x faster                                                           |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                           |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.51x faster                                                           |
| logging_simple           | 8.30 us                                                | 5.51 us: 1.51x faster                                                          |
| django_template          | 48.2 ms                                                | 32.0 ms: 1.50x faster                                                          |
| regex_compile            | 188 ms                                                 | 127 ms: 1.49x faster                                                           |
| logging_format           | 9.09 us                                                | 6.13 us: 1.48x faster                                                          |
| genshi_text              | 31.8 ms                                                | 21.7 ms: 1.47x faster                                                          |
| coroutines               | 35.1 ms                                                | 23.9 ms: 1.47x faster                                                          |
| html5lib                 | 88.9 ms                                                | 61.1 ms: 1.45x faster                                                          |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                         |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.44x faster                                                          |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.3 ms: 1.43x faster                                                          |
| pprint_safe_repr         | 1.02 sec                                               | 717 ms: 1.42x faster                                                           |
| thrift                   | 1.07 ms                                                | 771 us: 1.39x faster                                                           |
| 2to3                     | 348 ms                                                 | 252 ms: 1.38x faster                                                           |
| sqlglot_normalize        | 143 ms                                                 | 104 ms: 1.37x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 48.4 ms: 1.36x faster                                                          |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                         |
| scimark_fft              | 466 ms                                                 | 347 ms: 1.34x faster                                                           |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                           |
| xml_etree_process        | 79.1 ms                                                | 59.0 ms: 1.34x faster                                                          |
| sqlalchemy_declarative   | 172 ms                                                 | 129 ms: 1.34x faster                                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.86 ms: 1.33x faster                                                          |
| fannkuch                 | 532 ms                                                 | 402 ms: 1.32x faster                                                           |
| dulwich_log              | 84.3 ms                                                | 64.0 ms: 1.32x faster                                                          |
| sympy_integrate          | 25.8 ms                                                | 19.6 ms: 1.32x faster                                                          |
| sqlglot_optimize         | 69.2 ms                                                | 52.7 ms: 1.31x faster                                                          |
| nqueens                  | 106 ms                                                 | 81.1 ms: 1.31x faster                                                          |
| sympy_str                | 346 ms                                                 | 265 ms: 1.30x faster                                                           |
| docutils                 | 3.30 sec                                               | 2.58 sec: 1.28x faster                                                         |
| sympy_expand             | 566 ms                                                 | 451 ms: 1.25x faster                                                           |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                          |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                           |
| json_dumps               | 14.2 ms                                                | 11.9 ms: 1.19x faster                                                          |
| xml_etree_generate       | 99.4 ms                                                | 83.9 ms: 1.18x faster                                                          |
| xml_etree_iterparse      | 115 ms                                                 | 98.2 ms: 1.18x faster                                                          |
| mdp                      | 2.85 sec                                               | 2.47 sec: 1.15x faster                                                         |
| async_generators         | 444 ms                                                 | 387 ms: 1.15x faster                                                           |
| bench_thread_pool        | 986 us                                                 | 863 us: 1.14x faster                                                           |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                          |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                           |
| json                     | 5.69 ms                                                | 5.26 ms: 1.08x faster                                                          |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                                          |
| regex_effbot             | 3.63 ms                                                | 3.38 ms: 1.07x faster                                                          |
| json_loads               | 31.2 us                                                | 29.1 us: 1.07x faster                                                          |
| regex_v8                 | 27.8 ms                                                | 26.0 ms: 1.07x faster                                                          |
| regex_dna                | 227 ms                                                 | 213 ms: 1.06x faster                                                           |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                           |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                           |
| telco                    | 7.27 ms                                                | 7.80 ms: 1.07x slower                                                          |
| coverage                 | 79.4 ms                                                | 90.9 ms: 1.14x slower                                                          |
| python_startup_no_site   | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                          |
| gc_traversal             | 3.62 ms                                                | 4.57 ms: 1.26x slower                                                          |
| create_gc_cycles         | 1.62 ms                                                | 2.44 ms: 1.51x slower                                                          |
| bench_mp_pool            | 24.0 ms                                                | 80.9 ms: 3.37x slower                                                          |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                                   |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250129-3.14.0a4+-2b26797/bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.448x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.26x