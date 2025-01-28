# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: py_likely_unlikely
- machine: linux-x86_64
- commit hash: 2b26797
- commit date: 2025-01-29
- overall geometric mean: 1.422x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 262 ms: 1.33x faster                                                           |
| docutils       | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                         |
| html5lib       | 88.9 ms                                                | 63.1 ms: 1.41x faster                                                          |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 625 ms: 2.83x faster                                                           |
| async_tree_none         | 728 ms                                                 | 273 ms: 2.66x faster                                                           |
| async_tree_memoization  | 870 ms                                                 | 341 ms: 2.55x faster                                                           |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 493 ms: 2.06x faster                                                           |
| Geometric mean          | (ref)                                                  | 2.51x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.6 ms: 1.77x faster                                                          |
| float          | 117 ms                                                 | 66.4 ms: 1.76x faster                                                          |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                  | 1.48x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 131 ms: 1.44x faster                                                           |
| regex_v8       | 27.8 ms                                                | 24.1 ms: 1.15x faster                                                          |
| regex_effbot   | 3.63 ms                                                | 3.23 ms: 1.13x faster                                                          |
| regex_dna      | 227 ms                                                 | 208 ms: 1.09x faster                                                           |
| Geometric mean | (ref)                                                  | 1.19x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.86 sec: 1.69x faster                                                         |
| unpickle_pure_python | 331 us                                                 | 202 us: 1.64x faster                                                           |
| pickle_pure_python   | 484 us                                                 | 317 us: 1.53x faster                                                           |
| xml_etree_process    | 79.1 ms                                                | 55.6 ms: 1.42x faster                                                          |
| xml_etree_generate   | 99.4 ms                                                | 81.5 ms: 1.22x faster                                                          |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 95.9 ms: 1.20x faster                                                          |
| json_dumps           | 14.2 ms                                                | 11.8 ms: 1.20x faster                                                          |
| json_loads           | 31.2 us                                                | 29.3 us: 1.07x faster                                                          |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.0 ms: 1.12x faster                                                          |
| python_startup_no_site | 5.93 ms                                                | 7.12 ms: 1.20x slower                                                          |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.2 ms: 1.61x faster                                                          |
| django_template | 48.2 ms                                                | 33.6 ms: 1.43x faster                                                          |
| genshi_text     | 31.8 ms                                                | 23.9 ms: 1.33x faster                                                          |
| genshi_xml      | 66.0 ms                                                | 60.1 ms: 1.10x faster                                                          |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.28x faster                                                           |
| async_tree_io            | 1.77 sec                                               | 625 ms: 2.83x faster                                                           |
| async_tree_none          | 728 ms                                                 | 273 ms: 2.66x faster                                                           |
| async_tree_memoization   | 870 ms                                                 | 341 ms: 2.55x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.28 ms: 2.41x faster                                                          |
| generators               | 80.1 ms                                                | 37.3 ms: 2.15x faster                                                          |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 493 ms: 2.06x faster                                                           |
| chaos                    | 115 ms                                                 | 59.0 ms: 1.96x faster                                                          |
| richards_super           | 94.7 ms                                                | 48.8 ms: 1.94x faster                                                          |
| pylint                   | 551 ms                                                 | 289 ms: 1.90x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 67.7 ms: 1.89x faster                                                          |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 63.5 ms: 1.86x faster                                                          |
| deepcopy_memo            | 58.5 us                                                | 31.5 us: 1.86x faster                                                          |
| deepcopy                 | 479 us                                                 | 270 us: 1.78x faster                                                           |
| nbody                    | 154 ms                                                 | 86.6 ms: 1.77x faster                                                          |
| go                       | 240 ms                                                 | 136 ms: 1.77x faster                                                           |
| raytrace                 | 507 ms                                                 | 287 ms: 1.77x faster                                                           |
| float                    | 117 ms                                                 | 66.4 ms: 1.76x faster                                                          |
| spectral_norm            | 170 ms                                                 | 97.1 ms: 1.75x faster                                                          |
| richards                 | 79.3 ms                                                | 45.6 ms: 1.74x faster                                                          |
| logging_silent           | 190 ns                                                 | 111 ns: 1.72x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 1.86 sec: 1.69x faster                                                         |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.69x faster                                                          |
| unpickle_pure_python     | 331 us                                                 | 202 us: 1.64x faster                                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                          |
| mako                     | 16.3 ms                                                | 10.2 ms: 1.61x faster                                                          |
| pyflate                  | 716 ms                                                 | 449 ms: 1.60x faster                                                           |
| comprehensions           | 28.8 us                                                | 18.1 us: 1.59x faster                                                          |
| pickle_pure_python       | 484 us                                                 | 317 us: 1.53x faster                                                           |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                                          |
| deepcopy_reduce          | 4.17 us                                                | 2.75 us: 1.52x faster                                                          |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.51x faster                                                           |
| scimark_fft              | 466 ms                                                 | 314 ms: 1.48x faster                                                           |
| regex_compile            | 188 ms                                                 | 131 ms: 1.44x faster                                                           |
| logging_simple           | 8.30 us                                                | 5.78 us: 1.44x faster                                                          |
| django_template          | 48.2 ms                                                | 33.6 ms: 1.43x faster                                                          |
| logging_format           | 9.09 us                                                | 6.34 us: 1.43x faster                                                          |
| xml_etree_process        | 79.1 ms                                                | 55.6 ms: 1.42x faster                                                          |
| hexiom                   | 10.4 ms                                                | 7.31 ms: 1.42x faster                                                          |
| html5lib                 | 88.9 ms                                                | 63.1 ms: 1.41x faster                                                          |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.71 ms: 1.37x faster                                                          |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.0 ms: 1.37x faster                                                          |
| thrift                   | 1.07 ms                                                | 783 us: 1.37x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.55 sec: 1.36x faster                                                         |
| fannkuch                 | 532 ms                                                 | 397 ms: 1.34x faster                                                           |
| pprint_safe_repr         | 1.02 sec                                               | 762 ms: 1.34x faster                                                           |
| 2to3                     | 348 ms                                                 | 262 ms: 1.33x faster                                                           |
| genshi_text              | 31.8 ms                                                | 23.9 ms: 1.33x faster                                                          |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.31x faster                                                           |
| sqlalchemy_declarative   | 172 ms                                                 | 132 ms: 1.30x faster                                                           |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                          |
| sqlglot_optimize         | 69.2 ms                                                | 55.1 ms: 1.25x faster                                                          |
| sympy_sum                | 196 ms                                                 | 157 ms: 1.25x faster                                                           |
| sympy_integrate          | 25.8 ms                                                | 20.8 ms: 1.24x faster                                                          |
| dulwich_log              | 84.3 ms                                                | 67.9 ms: 1.24x faster                                                          |
| sympy_str                | 346 ms                                                 | 282 ms: 1.23x faster                                                           |
| docutils                 | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 81.5 ms: 1.22x faster                                                          |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 95.9 ms: 1.20x faster                                                          |
| json_dumps               | 14.2 ms                                                | 11.8 ms: 1.20x faster                                                          |
| sympy_expand             | 566 ms                                                 | 476 ms: 1.19x faster                                                           |
| nqueens                  | 106 ms                                                 | 91.3 ms: 1.16x faster                                                          |
| regex_v8                 | 27.8 ms                                                | 24.1 ms: 1.15x faster                                                          |
| regex_effbot             | 3.63 ms                                                | 3.23 ms: 1.13x faster                                                          |
| python_startup           | 14.6 ms                                                | 13.0 ms: 1.12x faster                                                          |
| mdp                      | 2.85 sec                                               | 2.57 sec: 1.11x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.74 us: 1.11x faster                                                          |
| bench_thread_pool        | 986 us                                                 | 898 us: 1.10x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 60.1 ms: 1.10x faster                                                          |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.09x faster                                                           |
| async_generators         | 444 ms                                                 | 406 ms: 1.09x faster                                                           |
| json                     | 5.69 ms                                                | 5.21 ms: 1.09x faster                                                          |
| regex_dna                | 227 ms                                                 | 208 ms: 1.09x faster                                                           |
| json_loads               | 31.2 us                                                | 29.3 us: 1.07x faster                                                          |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                           |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                           |
| telco                    | 7.27 ms                                                | 7.70 ms: 1.06x slower                                                          |
| coverage                 | 79.4 ms                                                | 90.5 ms: 1.14x slower                                                          |
| python_startup_no_site   | 5.93 ms                                                | 7.12 ms: 1.20x slower                                                          |
| gc_traversal             | 3.62 ms                                                | 4.73 ms: 1.30x slower                                                          |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                          |
| bench_mp_pool            | 24.0 ms                                                | 81.6 ms: 3.40x slower                                                          |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                                   |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250129-3.14.0a4+-2b26797-JIT/bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.422x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.28x