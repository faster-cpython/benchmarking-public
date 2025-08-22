# Results vs. 3.10.4

- fork: python
- ref: f278afcabf1a1c4162a0
- machine: linux-x86_64
- commit hash: f278afc
- commit date: 2025-08-22
- overall geometric mean: 1.337x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf2-x86_64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 287 ms: 1.22x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.93 sec: 1.16x faster                                                      |
| html5lib       | 94.6 ms                                                      | 67.4 ms: 1.40x faster                                                       |
| Geometric mean | (ref)                                                        | 1.26x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf2-x86_64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 618 ms: 2.59x faster                                                        |
| async_tree_none         | 692 ms                                                       | 270 ms: 2.56x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 324 ms: 2.53x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 497 ms: 1.88x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.37x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf2-x86_64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 65.0 ms: 1.71x faster                                                       |
| nbody          | 134 ms                                                       | 105 ms: 1.27x faster                                                        |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.32x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf2-x86_64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 134 ms: 1.42x faster                                                        |
| regex_dna      | 261 ms                                                       | 223 ms: 1.17x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 24.2 ms: 1.12x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.72 ms: 1.21x slower                                                       |
| Geometric mean | (ref)                                                        | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf2-x86_64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 195 us: 1.60x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 1.96 sec: 1.49x faster                                                      |
| json_dumps           | 14.5 ms                                                      | 10.2 ms: 1.42x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 55.2 ms: 1.38x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 333 us: 1.37x faster                                                        |
| json_loads           | 30.3 us                                                      | 25.2 us: 1.21x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 138 ms: 1.16x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 80.3 ms: 1.15x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 96.5 ms: 1.15x faster                                                       |
| Geometric mean       | (ref)                                                        | 1.31x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf2-x86_64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.81 ms: 1.20x slower                                                       |
| python_startup         | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf2-x86_64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.85 ms: 1.49x faster                                                       |
| django_template | 50.2 ms                                                      | 35.6 ms: 1.41x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 23.1 ms: 1.36x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 55.5 ms: 1.14x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.35x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf2-x86_64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 172 us: 3.12x faster                                                        |
| deltablue                | 7.50 ms                                                      | 2.89 ms: 2.59x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 618 ms: 2.59x faster                                                        |
| async_tree_none          | 692 ms                                                       | 270 ms: 2.56x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 324 ms: 2.53x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.29 sec: 2.33x faster                                                      |
| richards_super           | 90.6 ms                                                      | 39.4 ms: 2.30x faster                                                       |
| richards                 | 75.1 ms                                                      | 34.0 ms: 2.21x faster                                                       |
| go                       | 262 ms                                                       | 127 ms: 2.06x faster                                                        |
| generators               | 57.3 ms                                                      | 29.0 ms: 1.98x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 497 ms: 1.88x faster                                                        |
| chaos                    | 109 ms                                                       | 59.2 ms: 1.83x faster                                                       |
| pyflate                  | 733 ms                                                       | 402 ms: 1.83x faster                                                        |
| logging_silent           | 167 ns                                                       | 93.1 ns: 1.80x faster                                                       |
| scimark_lu               | 167 ms                                                       | 94.4 ms: 1.77x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 28.3 us: 1.76x faster                                                       |
| spectral_norm            | 139 ms                                                       | 79.6 ms: 1.75x faster                                                       |
| pylint                   | 566 ms                                                       | 324 ms: 1.75x faster                                                        |
| scimark_sor              | 180 ms                                                       | 104 ms: 1.73x faster                                                        |
| raytrace                 | 489 ms                                                       | 283 ms: 1.73x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 62.4 ms: 1.72x faster                                                       |
| float                    | 111 ms                                                       | 65.0 ms: 1.71x faster                                                       |
| deepcopy                 | 468 us                                                       | 280 us: 1.67x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 195 us: 1.60x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.13 ms: 1.54x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.5 us: 1.53x faster                                                       |
| logging_simple           | 8.88 us                                                      | 5.85 us: 1.52x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 78.8 ms: 1.51x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.42 us: 1.50x faster                                                       |
| mako                     | 14.7 ms                                                      | 9.85 ms: 1.49x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 1.96 sec: 1.49x faster                                                      |
| regex_compile            | 190 ms                                                       | 134 ms: 1.42x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.52 sec: 1.42x faster                                                      |
| json_dumps               | 14.5 ms                                                      | 10.2 ms: 1.42x faster                                                       |
| django_template          | 50.2 ms                                                      | 35.6 ms: 1.41x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 67.4 ms: 1.40x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 748 ms: 1.40x faster                                                        |
| thrift                   | 1.18 ms                                                      | 845 us: 1.39x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 55.2 ms: 1.38x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 59.1 ms: 1.37x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 333 us: 1.37x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 23.1 ms: 1.36x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.36x faster                                                      |
| coroutines               | 30.3 ms                                                      | 22.3 ms: 1.36x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.05 us: 1.31x faster                                                       |
| fannkuch                 | 483 ms                                                       | 369 ms: 1.31x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 16.8 ms: 1.27x faster                                                       |
| nbody                    | 134 ms                                                       | 105 ms: 1.27x faster                                                        |
| sympy_sum                | 193 ms                                                       | 153 ms: 1.26x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 22.4 ms: 1.26x faster                                                       |
| nqueens                  | 115 ms                                                       | 92.5 ms: 1.24x faster                                                       |
| sympy_str                | 360 ms                                                       | 291 ms: 1.24x faster                                                        |
| 2to3                     | 350 ms                                                       | 287 ms: 1.22x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.2 us: 1.21x faster                                                       |
| sympy_expand             | 600 ms                                                       | 500 ms: 1.20x faster                                                        |
| scimark_fft              | 361 ms                                                       | 302 ms: 1.20x faster                                                        |
| regex_dna                | 261 ms                                                       | 223 ms: 1.17x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 138 ms: 1.16x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.93 sec: 1.16x faster                                                      |
| xml_etree_generate       | 92.3 ms                                                      | 80.3 ms: 1.15x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 96.5 ms: 1.15x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 55.5 ms: 1.14x faster                                                       |
| meteor_contest           | 138 ms                                                       | 122 ms: 1.14x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 24.2 ms: 1.12x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.80 us: 1.07x faster                                                       |
| json                     | 5.86 ms                                                      | 5.53 ms: 1.06x faster                                                       |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 382 ms: 1.02x faster                                                        |
| async_generators         | 421 ms                                                       | 434 ms: 1.03x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 8.81 ms: 1.20x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.72 ms: 1.21x slower                                                       |
| coverage                 | 63.3 ms                                                      | 81.4 ms: 1.29x slower                                                       |
| python_startup           | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.84 ms: 1.61x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 6.49 ms: 1.90x slower                                                       |
| telco                    | 7.23 ms                                                      | 162 ms: 22.43x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.34x faster                                                                |

Benchmark hidden because not significant (1): scimark_sparse_mat_mult
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250822-3.15.0a0-f278afc-JIT/bm-20250822-pythonperf2-x86_64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.337x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.40x