# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: linux-aarch64
- commit hash: fcc6f57
- commit date: 2024-12-16
- overall geometric mean: 1.254x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 313 ms: 1.22x faster                                                               |
| docutils       | 3.53 sec                                                              | 3.22 sec: 1.10x faster                                                             |
| html5lib       | 86.5 ms                                                               | 72.0 ms: 1.20x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.17x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 920 ms: 2.48x faster                                                               |
| async_tree_none         | 950 ms                                                                | 406 ms: 2.34x faster                                                               |
| async_tree_memoization  | 1.13 sec                                                              | 516 ms: 2.19x faster                                                               |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 698 ms: 1.82x faster                                                               |
| Geometric mean          | (ref)                                                                 | 2.20x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 114 ms: 1.45x faster                                                               |
| float          | 135 ms                                                                | 93.1 ms: 1.45x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 135 ms: 1.31x faster                                                               |
| regex_effbot   | 4.25 ms                                                               | 4.02 ms: 1.06x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                                       |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 267 us: 1.37x faster                                                               |
| tomli_loads          | 3.36 sec                                                              | 2.59 sec: 1.30x faster                                                             |
| xml_etree_process    | 99.5 ms                                                               | 78.0 ms: 1.28x faster                                                              |
| pickle_pure_python   | 529 us                                                                | 431 us: 1.23x faster                                                               |
| xml_etree_parse      | 212 ms                                                                | 179 ms: 1.18x faster                                                               |
| json_dumps           | 16.7 ms                                                               | 14.7 ms: 1.14x faster                                                              |
| xml_etree_generate   | 123 ms                                                                | 110 ms: 1.12x faster                                                               |
| xml_etree_iterparse  | 156 ms                                                                | 144 ms: 1.08x faster                                                               |
| Geometric mean       | (ref)                                                                 | 1.18x faster                                                                       |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.01 ms: 1.31x slower                                                              |
| python_startup         | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                              |
| Geometric mean         | (ref)                                                                 | 1.37x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.9 ms: 1.36x faster                                                              |
| django_template | 53.3 ms                                                               | 43.2 ms: 1.23x faster                                                              |
| genshi_text     | 35.2 ms                                                               | 28.8 ms: 1.22x faster                                                              |
| Geometric mean  | (ref)                                                                 | 1.20x faster                                                                       |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 220 us: 3.01x faster                                                               |
| async_tree_io            | 2.28 sec                                                              | 920 ms: 2.48x faster                                                               |
| async_tree_none          | 950 ms                                                                | 406 ms: 2.34x faster                                                               |
| async_tree_memoization   | 1.13 sec                                                              | 516 ms: 2.19x faster                                                               |
| deltablue                | 8.94 ms                                                               | 4.56 ms: 1.96x faster                                                              |
| generators               | 68.1 ms                                                               | 37.2 ms: 1.83x faster                                                              |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 698 ms: 1.82x faster                                                               |
| go                       | 264 ms                                                                | 150 ms: 1.76x faster                                                               |
| richards_super           | 107 ms                                                                | 62.6 ms: 1.71x faster                                                              |
| raytrace                 | 573 ms                                                                | 338 ms: 1.70x faster                                                               |
| richards                 | 91.7 ms                                                               | 55.4 ms: 1.66x faster                                                              |
| scimark_lu               | 227 ms                                                                | 140 ms: 1.62x faster                                                               |
| scimark_monte_carlo      | 128 ms                                                                | 80.4 ms: 1.59x faster                                                              |
| logging_silent           | 222 ns                                                                | 140 ns: 1.59x faster                                                               |
| pylint                   | 485 ms                                                                | 319 ms: 1.52x faster                                                               |
| scimark_sor              | 246 ms                                                                | 163 ms: 1.51x faster                                                               |
| deepcopy_memo            | 61.7 us                                                               | 41.4 us: 1.49x faster                                                              |
| sqlglot_parse            | 2.40 ms                                                               | 1.62 ms: 1.49x faster                                                              |
| deepcopy                 | 511 us                                                                | 350 us: 1.46x faster                                                               |
| nbody                    | 166 ms                                                                | 114 ms: 1.45x faster                                                               |
| float                    | 135 ms                                                                | 93.1 ms: 1.45x faster                                                              |
| sqlglot_transpile        | 2.84 ms                                                               | 1.98 ms: 1.43x faster                                                              |
| crypto_pyaes             | 134 ms                                                                | 94.0 ms: 1.43x faster                                                              |
| spectral_norm            | 186 ms                                                                | 132 ms: 1.41x faster                                                               |
| chaos                    | 121 ms                                                                | 87.9 ms: 1.38x faster                                                              |
| unpickle_pure_python     | 366 us                                                                | 267 us: 1.37x faster                                                               |
| mako                     | 18.9 ms                                                               | 13.9 ms: 1.36x faster                                                              |
| comprehensions           | 33.1 us                                                               | 24.7 us: 1.34x faster                                                              |
| pyflate                  | 795 ms                                                                | 597 ms: 1.33x faster                                                               |
| sqlalchemy_declarative   | 197 ms                                                                | 150 ms: 1.32x faster                                                               |
| regex_compile            | 177 ms                                                                | 135 ms: 1.31x faster                                                               |
| tomli_loads              | 3.36 sec                                                              | 2.59 sec: 1.30x faster                                                             |
| hexiom                   | 10.9 ms                                                               | 8.46 ms: 1.29x faster                                                              |
| logging_simple           | 9.78 us                                                               | 7.60 us: 1.29x faster                                                              |
| xml_etree_process        | 99.5 ms                                                               | 78.0 ms: 1.28x faster                                                              |
| coroutines               | 37.2 ms                                                               | 29.4 ms: 1.26x faster                                                              |
| deepcopy_reduce          | 4.60 us                                                               | 3.64 us: 1.26x faster                                                              |
| logging_format           | 10.6 us                                                               | 8.54 us: 1.24x faster                                                              |
| django_template          | 53.3 ms                                                               | 43.2 ms: 1.23x faster                                                              |
| pickle_pure_python       | 529 us                                                                | 431 us: 1.23x faster                                                               |
| thrift                   | 1.26 ms                                                               | 1.03 ms: 1.23x faster                                                              |
| genshi_text              | 35.2 ms                                                               | 28.8 ms: 1.22x faster                                                              |
| 2to3                     | 381 ms                                                                | 313 ms: 1.22x faster                                                               |
| html5lib                 | 86.5 ms                                                               | 72.0 ms: 1.20x faster                                                              |
| bench_thread_pool        | 1.59 ms                                                               | 1.33 ms: 1.20x faster                                                              |
| sympy_integrate          | 26.5 ms                                                               | 22.4 ms: 1.19x faster                                                              |
| xml_etree_parse          | 212 ms                                                                | 179 ms: 1.18x faster                                                               |
| scimark_fft              | 500 ms                                                                | 424 ms: 1.18x faster                                                               |
| pathlib                  | 26.3 ms                                                               | 22.8 ms: 1.15x faster                                                              |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.69 ms: 1.14x faster                                                              |
| json_dumps               | 16.7 ms                                                               | 14.7 ms: 1.14x faster                                                              |
| sympy_str                | 329 ms                                                                | 289 ms: 1.14x faster                                                               |
| pycparser                | 1.69 sec                                                              | 1.49 sec: 1.13x faster                                                             |
| sqlglot_normalize        | 156 ms                                                                | 139 ms: 1.13x faster                                                               |
| sqlalchemy_imperative    | 20.5 ms                                                               | 18.3 ms: 1.12x faster                                                              |
| xml_etree_generate       | 123 ms                                                                | 110 ms: 1.12x faster                                                               |
| sympy_sum                | 184 ms                                                                | 165 ms: 1.11x faster                                                               |
| docutils                 | 3.53 sec                                                              | 3.22 sec: 1.10x faster                                                             |
| xml_etree_iterparse      | 156 ms                                                                | 144 ms: 1.08x faster                                                               |
| mdp                      | 3.70 sec                                                              | 3.43 sec: 1.08x faster                                                             |
| sqlglot_optimize         | 75.4 ms                                                               | 70.2 ms: 1.07x faster                                                              |
| regex_effbot             | 4.25 ms                                                               | 4.02 ms: 1.06x faster                                                              |
| fannkuch                 | 546 ms                                                                | 517 ms: 1.06x faster                                                               |
| nqueens                  | 117 ms                                                                | 111 ms: 1.05x faster                                                               |
| json                     | 5.88 ms                                                               | 5.63 ms: 1.04x faster                                                              |
| sympy_expand             | 543 ms                                                                | 522 ms: 1.04x faster                                                               |
| asyncio_websockets       | 657 ms                                                                | 675 ms: 1.03x slower                                                               |
| pprint_safe_repr         | 1.15 sec                                                              | 1.23 sec: 1.08x slower                                                             |
| async_generators         | 452 ms                                                                | 495 ms: 1.09x slower                                                               |
| pprint_pformat           | 2.36 sec                                                              | 2.62 sec: 1.11x slower                                                             |
| mypy2                    | 936 ms                                                                | 1.07 sec: 1.15x slower                                                             |
| telco                    | 8.49 ms                                                               | 9.78 ms: 1.15x slower                                                              |
| dulwich_log              | 73.5 ms                                                               | 86.4 ms: 1.18x slower                                                              |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.21x slower                                                               |
| python_startup_no_site   | 6.89 ms                                                               | 9.01 ms: 1.31x slower                                                              |
| python_startup           | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                              |
| create_gc_cycles         | 2.26 ms                                                               | 3.71 ms: 1.64x slower                                                              |
| gc_traversal             | 4.15 ms                                                               | 6.90 ms: 1.66x slower                                                              |
| bench_mp_pool            | 14.5 ms                                                               | 984 ms: 67.69x slower                                                              |
| Geometric mean           | (ref)                                                                 | 1.17x faster                                                                       |

Benchmark hidden because not significant (7): meteor_contest, sqlite_synth, genshi_xml, regex_v8, pidigits, regex_dna, json_loads
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241216-3.14.0a2+-fcc6f57-JIT/bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.254x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: 1.33x