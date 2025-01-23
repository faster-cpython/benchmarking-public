# Results vs. 3.10.4

- fork: mdboom
- ref: aa_test_2025_2
- machine: linux-aarch64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.086x faster
- HPT reliability: 99.51%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.56x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| docutils       | 3.53 sec                                                              | 3.41 sec: 1.03x faster                                             |
| html5lib       | 86.5 ms                                                               | 78.8 ms: 1.10x faster                                              |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                       |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 954 ms: 2.40x faster                                               |
| async_tree_none         | 950 ms                                                                | 428 ms: 2.22x faster                                               |
| async_tree_memoization  | 1.13 sec                                                              | 531 ms: 2.14x faster                                               |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 722 ms: 1.76x faster                                               |
| Geometric mean          | (ref)                                                                 | 2.12x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 135 ms                                                                | 107 ms: 1.26x faster                                               |
| nbody          | 166 ms                                                                | 189 ms: 1.14x slower                                               |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 164 ms: 1.07x faster                                               |
| regex_dna      | 257 ms                                                                | 274 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                       |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_iterparse  | 156 ms                                                                | 132 ms: 1.18x faster                                               |
| xml_etree_parse      | 212 ms                                                                | 187 ms: 1.14x faster                                               |
| unpickle_pure_python | 366 us                                                                | 341 us: 1.07x faster                                               |
| pickle_pure_python   | 529 us                                                                | 499 us: 1.06x faster                                               |
| tomli_loads          | 3.36 sec                                                              | 3.26 sec: 1.03x faster                                             |
| xml_etree_process    | 99.5 ms                                                               | 108 ms: 1.09x slower                                               |
| xml_etree_generate   | 123 ms                                                                | 141 ms: 1.15x slower                                               |
| json_loads           | 30.9 us                                                               | 37.0 us: 1.19x slower                                              |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 12.1 ms: 1.76x slower                                              |
| python_startup         | 11.2 ms                                                               | 20.1 ms: 1.80x slower                                              |
| Geometric mean         | (ref)                                                                 | 1.78x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 57.3 ms: 1.07x slower                                              |
| genshi_text     | 35.2 ms                                                               | 38.4 ms: 1.09x slower                                              |
| genshi_xml      | 69.8 ms                                                               | 80.5 ms: 1.15x slower                                              |
| mako            | 18.9 ms                                                               | 23.0 ms: 1.22x slower                                              |
| Geometric mean  | (ref)                                                                 | 1.13x slower                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io            | 2.28 sec                                                              | 954 ms: 2.40x faster                                               |
| async_tree_none          | 950 ms                                                                | 428 ms: 2.22x faster                                               |
| typing_runtime_protocols | 661 us                                                                | 305 us: 2.17x faster                                               |
| async_tree_memoization   | 1.13 sec                                                              | 531 ms: 2.14x faster                                               |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 722 ms: 1.76x faster                                               |
| generators               | 68.1 ms                                                               | 44.7 ms: 1.52x faster                                              |
| go                       | 264 ms                                                                | 181 ms: 1.46x faster                                               |
| deltablue                | 8.94 ms                                                               | 6.16 ms: 1.45x faster                                              |
| logging_silent           | 222 ns                                                                | 157 ns: 1.42x faster                                               |
| scimark_sor              | 246 ms                                                                | 179 ms: 1.38x faster                                               |
| raytrace                 | 573 ms                                                                | 425 ms: 1.35x faster                                               |
| chaos                    | 121 ms                                                                | 90.1 ms: 1.34x faster                                              |
| richards_super           | 107 ms                                                                | 85.0 ms: 1.26x faster                                              |
| float                    | 135 ms                                                                | 107 ms: 1.26x faster                                               |
| pylint                   | 485 ms                                                                | 389 ms: 1.25x faster                                               |
| spectral_norm            | 186 ms                                                                | 151 ms: 1.23x faster                                               |
| crypto_pyaes             | 134 ms                                                                | 111 ms: 1.21x faster                                               |
| deepcopy                 | 511 us                                                                | 426 us: 1.20x faster                                               |
| scimark_lu               | 227 ms                                                                | 189 ms: 1.20x faster                                               |
| pyflate                  | 795 ms                                                                | 665 ms: 1.20x faster                                               |
| richards                 | 91.7 ms                                                               | 77.1 ms: 1.19x faster                                              |
| sqlglot_parse            | 2.40 ms                                                               | 2.02 ms: 1.19x faster                                              |
| xml_etree_iterparse      | 156 ms                                                                | 132 ms: 1.18x faster                                               |
| deepcopy_memo            | 61.7 us                                                               | 53.1 us: 1.16x faster                                              |
| comprehensions           | 33.1 us                                                               | 28.6 us: 1.16x faster                                              |
| pycparser                | 1.69 sec                                                              | 1.47 sec: 1.15x faster                                             |
| scimark_monte_carlo      | 128 ms                                                                | 112 ms: 1.14x faster                                               |
| sqlite_synth             | 4.12 us                                                               | 3.60 us: 1.14x faster                                              |
| xml_etree_parse          | 212 ms                                                                | 187 ms: 1.14x faster                                               |
| pathlib                  | 26.3 ms                                                               | 23.2 ms: 1.13x faster                                              |
| coroutines               | 37.2 ms                                                               | 32.8 ms: 1.13x faster                                              |
| hexiom                   | 10.9 ms                                                               | 9.66 ms: 1.13x faster                                              |
| sqlglot_transpile        | 2.84 ms                                                               | 2.52 ms: 1.13x faster                                              |
| html5lib                 | 86.5 ms                                                               | 78.8 ms: 1.10x faster                                              |
| regex_compile            | 177 ms                                                                | 164 ms: 1.07x faster                                               |
| unpickle_pure_python     | 366 us                                                                | 341 us: 1.07x faster                                               |
| pickle_pure_python       | 529 us                                                                | 499 us: 1.06x faster                                               |
| logging_simple           | 9.78 us                                                               | 9.22 us: 1.06x faster                                              |
| logging_format           | 10.6 us                                                               | 10.1 us: 1.05x faster                                              |
| dulwich_log              | 73.5 ms                                                               | 70.5 ms: 1.04x faster                                              |
| create_gc_cycles         | 2.26 ms                                                               | 2.17 ms: 1.04x faster                                              |
| docutils                 | 3.53 sec                                                              | 3.41 sec: 1.03x faster                                             |
| tomli_loads              | 3.36 sec                                                              | 3.26 sec: 1.03x faster                                             |
| pprint_pformat           | 2.36 sec                                                              | 2.41 sec: 1.02x slower                                             |
| sympy_sum                | 184 ms                                                                | 190 ms: 1.03x slower                                               |
| sqlglot_optimize         | 75.4 ms                                                               | 77.8 ms: 1.03x slower                                              |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.95 ms: 1.04x slower                                              |
| mdp                      | 3.70 sec                                                              | 3.87 sec: 1.05x slower                                             |
| asyncio_websockets       | 657 ms                                                                | 689 ms: 1.05x slower                                               |
| sqlalchemy_declarative   | 197 ms                                                                | 208 ms: 1.05x slower                                               |
| regex_dna                | 257 ms                                                                | 274 ms: 1.07x slower                                               |
| django_template          | 53.3 ms                                                               | 57.3 ms: 1.07x slower                                              |
| xml_etree_process        | 99.5 ms                                                               | 108 ms: 1.09x slower                                               |
| genshi_text              | 35.2 ms                                                               | 38.4 ms: 1.09x slower                                              |
| json                     | 5.88 ms                                                               | 6.44 ms: 1.10x slower                                              |
| sympy_integrate          | 26.5 ms                                                               | 29.2 ms: 1.10x slower                                              |
| sympy_str                | 329 ms                                                                | 370 ms: 1.13x slower                                               |
| sympy_expand             | 543 ms                                                                | 617 ms: 1.14x slower                                               |
| nbody                    | 166 ms                                                                | 189 ms: 1.14x slower                                               |
| xml_etree_generate       | 123 ms                                                                | 141 ms: 1.15x slower                                               |
| nqueens                  | 117 ms                                                                | 135 ms: 1.15x slower                                               |
| genshi_xml               | 69.8 ms                                                               | 80.5 ms: 1.15x slower                                              |
| sqlalchemy_imperative    | 20.5 ms                                                               | 23.9 ms: 1.16x slower                                              |
| async_generators         | 452 ms                                                                | 537 ms: 1.19x slower                                               |
| json_loads               | 30.9 us                                                               | 37.0 us: 1.19x slower                                              |
| bench_thread_pool        | 1.59 ms                                                               | 1.91 ms: 1.20x slower                                              |
| mako                     | 18.9 ms                                                               | 23.0 ms: 1.22x slower                                              |
| fannkuch                 | 546 ms                                                                | 677 ms: 1.24x slower                                               |
| meteor_contest           | 126 ms                                                                | 158 ms: 1.25x slower                                               |
| gc_traversal             | 4.15 ms                                                               | 5.36 ms: 1.29x slower                                              |
| telco                    | 8.49 ms                                                               | 11.8 ms: 1.39x slower                                              |
| coverage                 | 83.6 ms                                                               | 129 ms: 1.55x slower                                               |
| python_startup_no_site   | 6.89 ms                                                               | 12.1 ms: 1.76x slower                                              |
| python_startup           | 11.2 ms                                                               | 20.1 ms: 1.80x slower                                              |
| bench_mp_pool            | 14.5 ms                                                               | 59.7 ms: 4.11x slower                                              |
| Geometric mean           | (ref)                                                                 | 1.04x faster                                                       |

Benchmark hidden because not significant (10): regex_effbot, regex_v8, scimark_fft, thrift, pidigits, sqlglot_normalize, 2to3, pprint_safe_repr, json_dumps, deepcopy_reduce
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250123-3.14.0a4+-8ffb2c1-NOGIL/bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.086x faster

# HPT report

- Reliability score: 99.51% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.56x