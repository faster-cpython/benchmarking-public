# Results vs. 3.10.4

- fork: python
- ref: f278afcabf1a1c4162a0
- machine: linux-aarch64
- commit hash: f278afc
- commit date: 2025-08-22
- overall geometric mean: 1.303x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 310 ms: 1.23x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.03 sec: 1.16x faster                                                  |
| html5lib       | 86.5 ms                                                               | 61.1 ms: 1.41x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 880 ms: 2.60x faster                                                    |
| async_tree_none         | 950 ms                                                                | 381 ms: 2.49x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 481 ms: 2.36x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 660 ms: 1.93x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.33x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 81.3 ms: 1.66x faster                                                   |
| nbody          | 166 ms                                                                | 127 ms: 1.30x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 121 ms: 1.46x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 27.0 ms: 1.19x faster                                                   |
| regex_dna      | 257 ms                                                                | 223 ms: 1.15x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.78 ms: 1.12x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.22x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.31 sec: 1.46x faster                                                  |
| unpickle_pure_python | 366 us                                                                | 253 us: 1.45x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 12.1 ms: 1.38x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 390 us: 1.36x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 76.7 ms: 1.30x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 183 ms: 1.16x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 107 ms: 1.15x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 147 ms: 1.06x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.9 us: 1.06x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.24x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.59 ms: 1.25x slower                                                   |
| python_startup         | 11.2 ms                                                               | 15.0 ms: 1.34x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.29x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 12.8 ms: 1.47x faster                                                   |
| django_template | 53.3 ms                                                               | 40.1 ms: 1.33x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 26.8 ms: 1.31x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 62.1 ms: 1.12x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.30x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 207 us: 3.20x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 880 ms: 2.60x faster                                                    |
| async_tree_none          | 950 ms                                                                | 381 ms: 2.49x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 481 ms: 2.36x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.80 ms: 2.35x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.65 sec: 2.25x faster                                                  |
| richards_super           | 107 ms                                                                | 49.5 ms: 2.17x faster                                                   |
| richards                 | 91.7 ms                                                               | 43.0 ms: 2.13x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 660 ms: 1.93x faster                                                    |
| generators               | 68.1 ms                                                               | 36.9 ms: 1.85x faster                                                   |
| go                       | 264 ms                                                                | 150 ms: 1.77x faster                                                    |
| chaos                    | 121 ms                                                                | 68.8 ms: 1.76x faster                                                   |
| raytrace                 | 573 ms                                                                | 329 ms: 1.74x faster                                                    |
| logging_silent           | 222 ns                                                                | 128 ns: 1.74x faster                                                    |
| scimark_sor              | 246 ms                                                                | 143 ms: 1.72x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 35.9 us: 1.72x faster                                                   |
| float                    | 135 ms                                                                | 81.3 ms: 1.66x faster                                                   |
| spectral_norm            | 186 ms                                                                | 115 ms: 1.62x faster                                                    |
| scimark_lu               | 227 ms                                                                | 141 ms: 1.61x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 81.9 ms: 1.56x faster                                                   |
| deepcopy                 | 511 us                                                                | 330 us: 1.55x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.21 ms: 1.51x faster                                                   |
| pylint                   | 485 ms                                                                | 323 ms: 1.50x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 89.3 ms: 1.50x faster                                                   |
| comprehensions           | 33.1 us                                                               | 22.2 us: 1.49x faster                                                   |
| pyflate                  | 795 ms                                                                | 535 ms: 1.49x faster                                                    |
| mako                     | 18.9 ms                                                               | 12.8 ms: 1.47x faster                                                   |
| logging_simple           | 9.78 us                                                               | 6.65 us: 1.47x faster                                                   |
| regex_compile            | 177 ms                                                                | 121 ms: 1.46x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.31 sec: 1.46x faster                                                  |
| unpickle_pure_python     | 366 us                                                                | 253 us: 1.45x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.34 us: 1.44x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 61.1 ms: 1.41x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 52.5 ms: 1.40x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 12.1 ms: 1.38x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 390 us: 1.36x faster                                                    |
| django_template          | 53.3 ms                                                               | 40.1 ms: 1.33x faster                                                   |
| thrift                   | 1.26 ms                                                               | 952 us: 1.32x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 26.8 ms: 1.31x faster                                                   |
| nbody                    | 166 ms                                                                | 127 ms: 1.30x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 76.7 ms: 1.30x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.63 us: 1.27x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 21.1 ms: 1.26x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.35 sec: 1.26x faster                                                  |
| 2to3                     | 381 ms                                                                | 310 ms: 1.23x faster                                                    |
| sympy_sum                | 184 ms                                                                | 150 ms: 1.23x faster                                                    |
| scimark_fft              | 500 ms                                                                | 409 ms: 1.22x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 22.0 ms: 1.19x faster                                                   |
| fannkuch                 | 546 ms                                                                | 457 ms: 1.19x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 27.0 ms: 1.19x faster                                                   |
| coroutines               | 37.2 ms                                                               | 31.5 ms: 1.18x faster                                                   |
| sympy_str                | 329 ms                                                                | 279 ms: 1.18x faster                                                    |
| nqueens                  | 117 ms                                                                | 101 ms: 1.17x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.03 sec: 1.16x faster                                                  |
| xml_etree_parse          | 212 ms                                                                | 183 ms: 1.16x faster                                                    |
| regex_dna                | 257 ms                                                                | 223 ms: 1.15x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 107 ms: 1.15x faster                                                    |
| meteor_contest           | 126 ms                                                                | 111 ms: 1.14x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 3.78 ms: 1.12x faster                                                   |
| genshi_xml               | 69.8 ms                                                               | 62.1 ms: 1.12x faster                                                   |
| sympy_expand             | 543 ms                                                                | 487 ms: 1.12x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.79 us: 1.09x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.10 ms: 1.07x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 147 ms: 1.06x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.11 sec: 1.04x faster                                                  |
| pprint_pformat           | 2.36 sec                                                              | 2.30 sec: 1.02x faster                                                  |
| asyncio_websockets       | 657 ms                                                                | 667 ms: 1.02x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.9 us: 1.06x slower                                                   |
| async_generators         | 452 ms                                                                | 481 ms: 1.06x slower                                                    |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.22x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.59 ms: 1.25x slower                                                   |
| python_startup           | 11.2 ms                                                               | 15.0 ms: 1.34x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 6.81 ms: 1.64x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.81 ms: 1.68x slower                                                   |
| telco                    | 8.49 ms                                                               | 163 ms: 19.15x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.29x faster                                                            |

Benchmark hidden because not significant (2): json, pidigits
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250822-3.15.0a0-f278afc-JIT/bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.303x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.40x