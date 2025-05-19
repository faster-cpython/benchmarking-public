# Results vs. 3.10.4

- fork: python
- ref: 009e7b36981fd07f7cca
- machine: linux-aarch64
- commit hash: 009e7b3
- commit date: 2025-05-18
- overall geometric mean: 1.180x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.64x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 352 ms: 1.08x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.24 sec: 1.09x faster                                                  |
| html5lib       | 86.5 ms                                                               | 68.6 ms: 1.26x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 870 ms: 2.63x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 482 ms: 2.35x faster                                                    |
| async_tree_none         | 950 ms                                                                | 409 ms: 2.32x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 684 ms: 1.86x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.27x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 95.5 ms: 1.41x faster                                                   |
| pidigits       | 235 ms                                                                | 231 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                            |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 151 ms: 1.17x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 27.5 ms: 1.17x faster                                                   |
| regex_dna      | 257 ms                                                                | 238 ms: 1.08x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.96 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 428 us: 1.24x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 128 ms: 1.22x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 302 us: 1.21x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.84 sec: 1.18x faster                                                  |
| xml_etree_parse      | 212 ms                                                                | 182 ms: 1.16x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 14.7 ms: 1.14x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 101 ms: 1.01x slower                                                    |
| pickle_list          | 5.24 us                                                               | 5.61 us: 1.07x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 40.5 us: 1.15x slower                                                   |
| xml_etree_generate   | 123 ms                                                                | 142 ms: 1.15x slower                                                    |
| unpickle             | 17.5 us                                                               | 21.0 us: 1.20x slower                                                   |
| pickle               | 12.5 us                                                               | 15.4 us: 1.24x slower                                                   |
| json_loads           | 30.9 us                                                               | 39.0 us: 1.26x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 12.2 ms: 1.77x slower                                                   |
| python_startup         | 11.2 ms                                                               | 20.1 ms: 1.80x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.79x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 50.6 ms: 1.05x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 72.1 ms: 1.03x slower                                                   |
| mako            | 18.9 ms                                                               | 21.3 ms: 1.13x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io            | 2.28 sec                                                              | 870 ms: 2.63x faster                                                    |
| typing_runtime_protocols | 661 us                                                                | 271 us: 2.44x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 482 ms: 2.35x faster                                                    |
| async_tree_none          | 950 ms                                                                | 409 ms: 2.32x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.68 ms: 1.91x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.97 sec: 1.87x faster                                                  |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 684 ms: 1.86x faster                                                    |
| generators               | 68.1 ms                                                               | 40.3 ms: 1.69x faster                                                   |
| go                       | 264 ms                                                                | 158 ms: 1.68x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 582 ms: 1.62x faster                                                    |
| scimark_sor              | 246 ms                                                                | 159 ms: 1.55x faster                                                    |
| chaos                    | 121 ms                                                                | 78.9 ms: 1.54x faster                                                   |
| raytrace                 | 573 ms                                                                | 383 ms: 1.50x faster                                                    |
| gc_traversal             | 4.15 ms                                                               | 2.88 ms: 1.44x faster                                                   |
| float                    | 135 ms                                                                | 95.5 ms: 1.41x faster                                                   |
| richards_super           | 107 ms                                                                | 78.3 ms: 1.37x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.41 sec: 1.36x faster                                                  |
| richards                 | 91.7 ms                                                               | 68.3 ms: 1.34x faster                                                   |
| spectral_norm            | 186 ms                                                                | 140 ms: 1.33x faster                                                    |
| pyflate                  | 795 ms                                                                | 600 ms: 1.32x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 8.24 ms: 1.32x faster                                                   |
| deepcopy                 | 511 us                                                                | 386 us: 1.32x faster                                                    |
| scimark_lu               | 227 ms                                                                | 175 ms: 1.30x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 48.1 us: 1.28x faster                                                   |
| pylint                   | 485 ms                                                                | 383 ms: 1.27x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 68.6 ms: 1.26x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.35 sec: 1.25x faster                                                  |
| scimark_monte_carlo      | 128 ms                                                                | 103 ms: 1.24x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 428 us: 1.24x faster                                                    |
| comprehensions           | 33.1 us                                                               | 27.0 us: 1.23x faster                                                   |
| coroutines               | 37.2 ms                                                               | 30.3 ms: 1.23x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 110 ms: 1.22x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 128 ms: 1.22x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 302 us: 1.21x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 61.1 ms: 1.20x faster                                                   |
| sqlite_synth             | 4.12 us                                                               | 3.46 us: 1.19x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.84 sec: 1.18x faster                                                  |
| regex_compile            | 177 ms                                                                | 151 ms: 1.17x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 27.5 ms: 1.17x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 182 ms: 1.16x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.7 ms: 1.14x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 23.6 ms: 1.12x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 4.18 us: 1.10x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.24 sec: 1.09x faster                                                  |
| scimark_fft              | 500 ms                                                                | 460 ms: 1.09x faster                                                    |
| thrift                   | 1.26 ms                                                               | 1.16 ms: 1.08x faster                                                   |
| 2to3                     | 381 ms                                                                | 352 ms: 1.08x faster                                                    |
| regex_dna                | 257 ms                                                                | 238 ms: 1.08x faster                                                    |
| logging_simple           | 9.78 us                                                               | 9.07 us: 1.08x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.07 sec: 1.08x faster                                                  |
| regex_effbot             | 4.25 ms                                                               | 3.96 ms: 1.07x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.20 sec: 1.07x faster                                                  |
| django_template          | 53.3 ms                                                               | 50.6 ms: 1.05x faster                                                   |
| logging_format           | 10.6 us                                                               | 10.1 us: 1.05x faster                                                   |
| pidigits                 | 235 ms                                                                | 231 ms: 1.02x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 101 ms: 1.01x slower                                                    |
| asyncio_websockets       | 657 ms                                                                | 670 ms: 1.02x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 72.1 ms: 1.03x slower                                                   |
| sympy_str                | 329 ms                                                                | 343 ms: 1.04x slower                                                    |
| pickle_list              | 5.24 us                                                               | 5.61 us: 1.07x slower                                                   |
| sympy_expand             | 543 ms                                                                | 581 ms: 1.07x slower                                                    |
| async_generators         | 452 ms                                                                | 498 ms: 1.10x slower                                                    |
| mako                     | 18.9 ms                                                               | 21.3 ms: 1.13x slower                                                   |
| json                     | 5.88 ms                                                               | 6.63 ms: 1.13x slower                                                   |
| fannkuch                 | 546 ms                                                                | 618 ms: 1.13x slower                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.81 ms: 1.14x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 40.5 us: 1.15x slower                                                   |
| xml_etree_generate       | 123 ms                                                                | 142 ms: 1.15x slower                                                    |
| meteor_contest           | 126 ms                                                                | 151 ms: 1.20x slower                                                    |
| unpickle                 | 17.5 us                                                               | 21.0 us: 1.20x slower                                                   |
| pickle                   | 12.5 us                                                               | 15.4 us: 1.24x slower                                                   |
| json_loads               | 30.9 us                                                               | 39.0 us: 1.26x slower                                                   |
| telco                    | 8.49 ms                                                               | 11.3 ms: 1.33x slower                                                   |
| coverage                 | 83.6 ms                                                               | 146 ms: 1.75x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 12.2 ms: 1.77x slower                                                   |
| python_startup           | 11.2 ms                                                               | 20.1 ms: 1.80x slower                                                   |
| logging_silent           | 222 ns                                                                | 765 ns: 3.45x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 62.3 ms: 4.29x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.11x faster                                                            |

Benchmark hidden because not significant (8): sympy_integrate, nqueens, genshi_text, unpickle_list, scimark_sparse_mat_mult, create_gc_cycles, sympy_sum, nbody
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250518-3.15.0a0-009e7b3-NOGIL/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.180x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.64x