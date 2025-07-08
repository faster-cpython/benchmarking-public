# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_targets
- machine: linux-aarch64
- commit hash: aa2b0df
- commit date: 2025-07-07
- overall geometric mean: 1.220x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 319 ms: 1.19x faster                                                 |
| docutils       | 3.53 sec                                                              | 3.17 sec: 1.11x faster                                               |
| html5lib       | 86.5 ms                                                               | 63.2 ms: 1.37x faster                                                |
| Geometric mean | (ref)                                                                 | 1.22x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 930 ms: 2.46x faster                                                 |
| async_tree_none         | 950 ms                                                                | 398 ms: 2.39x faster                                                 |
| async_tree_memoization  | 1.13 sec                                                              | 497 ms: 2.28x faster                                                 |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 685 ms: 1.86x faster                                                 |
| Geometric mean          | (ref)                                                                 | 2.23x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 135 ms                                                                | 89.0 ms: 1.51x faster                                                |
| nbody          | 166 ms                                                                | 143 ms: 1.16x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.20x faster                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 126 ms: 1.40x faster                                                 |
| regex_v8       | 32.2 ms                                                               | 26.2 ms: 1.23x faster                                                |
| regex_dna      | 257 ms                                                                | 220 ms: 1.17x faster                                                 |
| regex_effbot   | 4.25 ms                                                               | 3.76 ms: 1.13x faster                                                |
| Geometric mean | (ref)                                                                 | 1.23x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.57 sec: 1.31x faster                                               |
| pickle_pure_python   | 529 us                                                                | 427 us: 1.24x faster                                                 |
| json_dumps           | 16.7 ms                                                               | 13.5 ms: 1.23x faster                                                |
| unpickle_pure_python | 366 us                                                                | 299 us: 1.22x faster                                                 |
| xml_etree_process    | 99.5 ms                                                               | 81.9 ms: 1.22x faster                                                |
| xml_etree_parse      | 212 ms                                                                | 178 ms: 1.19x faster                                                 |
| xml_etree_iterparse  | 156 ms                                                                | 146 ms: 1.07x faster                                                 |
| xml_etree_generate   | 123 ms                                                                | 115 ms: 1.07x faster                                                 |
| json_loads           | 30.9 us                                                               | 33.0 us: 1.07x slower                                                |
| Geometric mean       | (ref)                                                                 | 1.16x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.78 ms: 1.27x slower                                                |
| python_startup         | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                                |
| Geometric mean         | (ref)                                                                 | 1.32x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 40.9 ms: 1.30x faster                                                |
| genshi_text     | 35.2 ms                                                               | 27.9 ms: 1.26x faster                                                |
| mako            | 18.9 ms                                                               | 15.2 ms: 1.24x faster                                                |
| genshi_xml      | 69.8 ms                                                               | 65.8 ms: 1.06x faster                                                |
| Geometric mean  | (ref)                                                                 | 1.21x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 221 us: 2.98x faster                                                 |
| async_tree_io            | 2.28 sec                                                              | 930 ms: 2.46x faster                                                 |
| async_tree_none          | 950 ms                                                                | 398 ms: 2.39x faster                                                 |
| async_tree_memoization   | 1.13 sec                                                              | 497 ms: 2.28x faster                                                 |
| mdp                      | 3.70 sec                                                              | 1.66 sec: 2.23x faster                                               |
| deltablue                | 8.94 ms                                                               | 4.55 ms: 1.97x faster                                                |
| generators               | 68.1 ms                                                               | 35.5 ms: 1.92x faster                                                |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 685 ms: 1.86x faster                                                 |
| richards_super           | 107 ms                                                                | 58.1 ms: 1.85x faster                                                |
| richards                 | 91.7 ms                                                               | 51.0 ms: 1.80x faster                                                |
| chaos                    | 121 ms                                                                | 69.7 ms: 1.74x faster                                                |
| logging_silent           | 222 ns                                                                | 130 ns: 1.70x faster                                                 |
| scimark_sor              | 246 ms                                                                | 145 ms: 1.70x faster                                                 |
| raytrace                 | 573 ms                                                                | 343 ms: 1.67x faster                                                 |
| deepcopy_memo            | 61.7 us                                                               | 37.8 us: 1.63x faster                                                |
| deepcopy                 | 511 us                                                                | 337 us: 1.51x faster                                                 |
| float                    | 135 ms                                                                | 89.0 ms: 1.51x faster                                                |
| scimark_lu               | 227 ms                                                                | 150 ms: 1.51x faster                                                 |
| pylint                   | 485 ms                                                                | 327 ms: 1.48x faster                                                 |
| scimark_monte_carlo      | 128 ms                                                                | 88.8 ms: 1.44x faster                                                |
| regex_compile            | 177 ms                                                                | 126 ms: 1.40x faster                                                 |
| logging_simple           | 9.78 us                                                               | 7.02 us: 1.39x faster                                                |
| logging_format           | 10.6 us                                                               | 7.62 us: 1.39x faster                                                |
| html5lib                 | 86.5 ms                                                               | 63.2 ms: 1.37x faster                                                |
| pyflate                  | 795 ms                                                                | 596 ms: 1.33x faster                                                 |
| go                       | 264 ms                                                                | 198 ms: 1.33x faster                                                 |
| dulwich_log              | 73.5 ms                                                               | 55.2 ms: 1.33x faster                                                |
| comprehensions           | 33.1 us                                                               | 25.3 us: 1.31x faster                                                |
| tomli_loads              | 3.36 sec                                                              | 2.57 sec: 1.31x faster                                               |
| spectral_norm            | 186 ms                                                                | 143 ms: 1.30x faster                                                 |
| django_template          | 53.3 ms                                                               | 40.9 ms: 1.30x faster                                                |
| thrift                   | 1.26 ms                                                               | 975 us: 1.29x faster                                                 |
| deepcopy_reduce          | 4.60 us                                                               | 3.59 us: 1.28x faster                                                |
| genshi_text              | 35.2 ms                                                               | 27.9 ms: 1.26x faster                                                |
| mako                     | 18.9 ms                                                               | 15.2 ms: 1.24x faster                                                |
| crypto_pyaes             | 134 ms                                                                | 108 ms: 1.24x faster                                                 |
| pickle_pure_python       | 529 us                                                                | 427 us: 1.24x faster                                                 |
| json_dumps               | 16.7 ms                                                               | 13.5 ms: 1.23x faster                                                |
| sympy_integrate          | 26.5 ms                                                               | 21.6 ms: 1.23x faster                                                |
| regex_v8                 | 32.2 ms                                                               | 26.2 ms: 1.23x faster                                                |
| unpickle_pure_python     | 366 us                                                                | 299 us: 1.22x faster                                                 |
| xml_etree_process        | 99.5 ms                                                               | 81.9 ms: 1.22x faster                                                |
| coroutines               | 37.2 ms                                                               | 30.6 ms: 1.21x faster                                                |
| sympy_sum                | 184 ms                                                                | 152 ms: 1.21x faster                                                 |
| 2to3                     | 381 ms                                                                | 319 ms: 1.19x faster                                                 |
| xml_etree_parse          | 212 ms                                                                | 178 ms: 1.19x faster                                                 |
| hexiom                   | 10.9 ms                                                               | 9.22 ms: 1.18x faster                                                |
| pycparser                | 1.69 sec                                                              | 1.44 sec: 1.17x faster                                               |
| regex_dna                | 257 ms                                                                | 220 ms: 1.17x faster                                                 |
| nbody                    | 166 ms                                                                | 143 ms: 1.16x faster                                                 |
| sympy_str                | 329 ms                                                                | 288 ms: 1.14x faster                                                 |
| pathlib                  | 26.3 ms                                                               | 23.2 ms: 1.13x faster                                                |
| regex_effbot             | 4.25 ms                                                               | 3.76 ms: 1.13x faster                                                |
| scimark_fft              | 500 ms                                                                | 447 ms: 1.12x faster                                                 |
| docutils                 | 3.53 sec                                                              | 3.17 sec: 1.11x faster                                               |
| nqueens                  | 117 ms                                                                | 106 ms: 1.11x faster                                                 |
| sympy_expand             | 543 ms                                                                | 507 ms: 1.07x faster                                                 |
| xml_etree_iterparse      | 156 ms                                                                | 146 ms: 1.07x faster                                                 |
| sqlite_synth             | 4.12 us                                                               | 3.85 us: 1.07x faster                                                |
| xml_etree_generate       | 123 ms                                                                | 115 ms: 1.07x faster                                                 |
| genshi_xml               | 69.8 ms                                                               | 65.8 ms: 1.06x faster                                                |
| json                     | 5.88 ms                                                               | 5.73 ms: 1.03x faster                                                |
| asyncio_websockets       | 657 ms                                                                | 665 ms: 1.01x slower                                                 |
| fannkuch                 | 546 ms                                                                | 567 ms: 1.04x slower                                                 |
| json_loads               | 30.9 us                                                               | 33.0 us: 1.07x slower                                                |
| async_generators         | 452 ms                                                                | 496 ms: 1.10x slower                                                 |
| pprint_pformat           | 2.36 sec                                                              | 2.84 sec: 1.21x slower                                               |
| pprint_safe_repr         | 1.15 sec                                                              | 1.39 sec: 1.21x slower                                               |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.23x slower                                                 |
| python_startup_no_site   | 6.89 ms                                                               | 8.78 ms: 1.27x slower                                                |
| python_startup           | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                                |
| gc_traversal             | 4.15 ms                                                               | 6.79 ms: 1.63x slower                                                |
| create_gc_cycles         | 2.26 ms                                                               | 3.79 ms: 1.68x slower                                                |
| telco                    | 8.49 ms                                                               | 166 ms: 19.59x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.21x faster                                                         |

Benchmark hidden because not significant (3): scimark_sparse_mat_mult, pidigits, meteor_contest
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250707-3.15.0a0-aa2b0df-JIT/bm-20250707-arminc-aarch64-brandtbucher-jit_targets-3.15.0a0-aa2b0df.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.220x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: 1.40x