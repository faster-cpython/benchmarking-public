# Results vs. 3.10.4

- fork: python
- ref: 3.14
- machine: linux-aarch64
- commit hash: 964c29d
- commit date: 2025-06-16
- overall geometric mean: 1.349x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.36x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250616-arminc-aarch64-python-3.14-3.14.0b2+-964c29d |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 302 ms: 1.26x faster                                     |
| docutils       | 3.53 sec                                                              | 2.94 sec: 1.20x faster                                   |
| html5lib       | 86.5 ms                                                               | 63.1 ms: 1.37x faster                                    |
| Geometric mean | (ref)                                                                 | 1.28x faster                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250616-arminc-aarch64-python-3.14-3.14.0b2+-964c29d |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 882 ms: 2.59x faster                                     |
| async_tree_memoization  | 1.13 sec                                                              | 465 ms: 2.44x faster                                     |
| async_tree_none         | 950 ms                                                                | 391 ms: 2.43x faster                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 658 ms: 1.94x faster                                     |
| Geometric mean          | (ref)                                                                 | 2.33x faster                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250616-arminc-aarch64-python-3.14-3.14.0b2+-964c29d |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| float          | 135 ms                                                                | 85.0 ms: 1.58x faster                                    |
| nbody          | 166 ms                                                                | 120 ms: 1.38x faster                                     |
| Geometric mean | (ref)                                                                 | 1.29x faster                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250616-arminc-aarch64-python-3.14-3.14.0b2+-964c29d |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 121 ms: 1.46x faster                                     |
| regex_v8       | 32.2 ms                                                               | 27.0 ms: 1.19x faster                                    |
| regex_dna      | 257 ms                                                                | 220 ms: 1.17x faster                                     |
| regex_effbot   | 4.25 ms                                                               | 3.88 ms: 1.10x faster                                    |
| Geometric mean | (ref)                                                                 | 1.22x faster                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250616-arminc-aarch64-python-3.14-3.14.0b2+-964c29d |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 267 us: 1.37x faster                                     |
| tomli_loads          | 3.36 sec                                                              | 2.47 sec: 1.36x faster                                   |
| pickle_pure_python   | 529 us                                                                | 396 us: 1.34x faster                                     |
| json_dumps           | 16.7 ms                                                               | 13.6 ms: 1.23x faster                                    |
| xml_etree_process    | 99.5 ms                                                               | 81.7 ms: 1.22x faster                                    |
| xml_etree_parse      | 212 ms                                                                | 181 ms: 1.17x faster                                     |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.08x faster                                     |
| xml_etree_iterparse  | 156 ms                                                                | 144 ms: 1.08x faster                                     |
| json_loads           | 30.9 us                                                               | 35.7 us: 1.16x slower                                    |
| Geometric mean       | (ref)                                                                 | 1.18x faster                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250616-arminc-aarch64-python-3.14-3.14.0b2+-964c29d |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.60 ms: 1.25x slower                                    |
| python_startup         | 11.2 ms                                                               | 16.0 ms: 1.43x slower                                    |
| Geometric mean         | (ref)                                                                 | 1.34x slower                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250616-arminc-aarch64-python-3.14-3.14.0b2+-964c29d |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.1 ms: 1.34x faster                                    |
| django_template | 53.3 ms                                                               | 39.9 ms: 1.34x faster                                    |
| genshi_text     | 35.2 ms                                                               | 27.2 ms: 1.29x faster                                    |
| genshi_xml      | 69.8 ms                                                               | 59.7 ms: 1.17x faster                                    |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250616-arminc-aarch64-python-3.14-3.14.0b2+-964c29d |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 197 us: 3.35x faster                                     |
| async_tree_io            | 2.28 sec                                                              | 882 ms: 2.59x faster                                     |
| async_tree_memoization   | 1.13 sec                                                              | 465 ms: 2.44x faster                                     |
| async_tree_none          | 950 ms                                                                | 391 ms: 2.43x faster                                     |
| deltablue                | 8.94 ms                                                               | 3.86 ms: 2.32x faster                                    |
| mdp                      | 3.70 sec                                                              | 1.69 sec: 2.19x faster                                   |
| go                       | 264 ms                                                                | 130 ms: 2.03x faster                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 658 ms: 1.94x faster                                     |
| generators               | 68.1 ms                                                               | 35.6 ms: 1.91x faster                                    |
| richards_super           | 107 ms                                                                | 58.3 ms: 1.84x faster                                    |
| richards                 | 91.7 ms                                                               | 50.4 ms: 1.82x faster                                    |
| raytrace                 | 573 ms                                                                | 327 ms: 1.75x faster                                     |
| chaos                    | 121 ms                                                                | 69.3 ms: 1.75x faster                                    |
| scimark_sor              | 246 ms                                                                | 146 ms: 1.69x faster                                     |
| deepcopy_memo            | 61.7 us                                                               | 37.8 us: 1.63x faster                                    |
| scimark_monte_carlo      | 128 ms                                                                | 78.9 ms: 1.62x faster                                    |
| crypto_pyaes             | 134 ms                                                                | 83.2 ms: 1.61x faster                                    |
| float                    | 135 ms                                                                | 85.0 ms: 1.58x faster                                    |
| comprehensions           | 33.1 us                                                               | 21.1 us: 1.57x faster                                    |
| pylint                   | 485 ms                                                                | 312 ms: 1.56x faster                                     |
| hexiom                   | 10.9 ms                                                               | 7.02 ms: 1.55x faster                                    |
| deepcopy                 | 511 us                                                                | 330 us: 1.55x faster                                     |
| pyflate                  | 795 ms                                                                | 529 ms: 1.50x faster                                     |
| scimark_lu               | 227 ms                                                                | 152 ms: 1.49x faster                                     |
| spectral_norm            | 186 ms                                                                | 127 ms: 1.47x faster                                     |
| regex_compile            | 177 ms                                                                | 121 ms: 1.46x faster                                     |
| nbody                    | 166 ms                                                                | 120 ms: 1.38x faster                                     |
| unpickle_pure_python     | 366 us                                                                | 267 us: 1.37x faster                                     |
| html5lib                 | 86.5 ms                                                               | 63.1 ms: 1.37x faster                                    |
| tomli_loads              | 3.36 sec                                                              | 2.47 sec: 1.36x faster                                   |
| pycparser                | 1.69 sec                                                              | 1.25 sec: 1.36x faster                                   |
| dulwich_log              | 73.5 ms                                                               | 54.2 ms: 1.36x faster                                    |
| mako                     | 18.9 ms                                                               | 14.1 ms: 1.34x faster                                    |
| django_template          | 53.3 ms                                                               | 39.9 ms: 1.34x faster                                    |
| pickle_pure_python       | 529 us                                                                | 396 us: 1.34x faster                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 150 ms: 1.32x faster                                     |
| sympy_integrate          | 26.5 ms                                                               | 20.3 ms: 1.31x faster                                    |
| genshi_text              | 35.2 ms                                                               | 27.2 ms: 1.29x faster                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.84 sec: 1.28x faster                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.60 us: 1.28x faster                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.1 ms: 1.27x faster                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 903 ms: 1.27x faster                                     |
| logging_simple           | 9.78 us                                                               | 7.69 us: 1.27x faster                                    |
| 2to3                     | 381 ms                                                                | 302 ms: 1.26x faster                                     |
| logging_format           | 10.6 us                                                               | 8.49 us: 1.25x faster                                    |
| sympy_str                | 329 ms                                                                | 267 ms: 1.23x faster                                     |
| json_dumps               | 16.7 ms                                                               | 13.6 ms: 1.23x faster                                    |
| xml_etree_process        | 99.5 ms                                                               | 81.7 ms: 1.22x faster                                    |
| sympy_sum                | 184 ms                                                                | 152 ms: 1.21x faster                                     |
| coroutines               | 37.2 ms                                                               | 30.8 ms: 1.21x faster                                    |
| docutils                 | 3.53 sec                                                              | 2.94 sec: 1.20x faster                                   |
| regex_v8                 | 32.2 ms                                                               | 27.0 ms: 1.19x faster                                    |
| nqueens                  | 117 ms                                                                | 99.6 ms: 1.18x faster                                    |
| pathlib                  | 26.3 ms                                                               | 22.4 ms: 1.18x faster                                    |
| sympy_expand             | 543 ms                                                                | 463 ms: 1.17x faster                                     |
| regex_dna                | 257 ms                                                                | 220 ms: 1.17x faster                                     |
| genshi_xml               | 69.8 ms                                                               | 59.7 ms: 1.17x faster                                    |
| xml_etree_parse          | 212 ms                                                                | 181 ms: 1.17x faster                                     |
| meteor_contest           | 126 ms                                                                | 110 ms: 1.15x faster                                     |
| fannkuch                 | 546 ms                                                                | 475 ms: 1.15x faster                                     |
| scimark_fft              | 500 ms                                                                | 439 ms: 1.14x faster                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.93 ms: 1.10x faster                                    |
| regex_effbot             | 4.25 ms                                                               | 3.88 ms: 1.10x faster                                    |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.08x faster                                     |
| xml_etree_iterparse      | 156 ms                                                                | 144 ms: 1.08x faster                                     |
| sqlite_synth             | 4.12 us                                                               | 3.85 us: 1.07x faster                                    |
| asyncio_websockets       | 657 ms                                                                | 667 ms: 1.02x slower                                     |
| json                     | 5.88 ms                                                               | 6.12 ms: 1.04x slower                                    |
| telco                    | 8.49 ms                                                               | 9.43 ms: 1.11x slower                                    |
| json_loads               | 30.9 us                                                               | 35.7 us: 1.16x slower                                    |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.22x slower                                     |
| python_startup_no_site   | 6.89 ms                                                               | 8.60 ms: 1.25x slower                                    |
| python_startup           | 11.2 ms                                                               | 16.0 ms: 1.43x slower                                    |
| gc_traversal             | 4.15 ms                                                               | 6.89 ms: 1.66x slower                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.76 ms: 1.66x slower                                    |
| logging_silent           | 222 ns                                                                | 613 ns: 2.76x slower                                     |
| Geometric mean           | (ref)                                                                 | 1.31x faster                                             |

Benchmark hidden because not significant (2): async_generators, pidigits
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250616-3.14.0b2+-964c29d/bm-20250616-arminc-aarch64-python-3.14-3.14.0b2+-964c29d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.349x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.36x