# Results vs. 3.10.4

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: linux-aarch64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.295x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.41x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 314 ms: 1.21x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.12 sec: 1.13x faster                                                  |
| html5lib       | 86.5 ms                                                               | 63.4 ms: 1.36x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.23x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 884 ms: 2.58x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 472 ms: 2.40x faster                                                    |
| async_tree_none         | 950 ms                                                                | 399 ms: 2.38x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 672 ms: 1.89x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.30x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 82.3 ms: 1.64x faster                                                   |
| nbody          | 166 ms                                                                | 127 ms: 1.30x faster                                                    |
| pidigits       | 235 ms                                                                | 236 ms: 1.00x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 123 ms: 1.43x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 26.3 ms: 1.22x faster                                                   |
| regex_dna      | 257 ms                                                                | 223 ms: 1.15x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.89 ms: 1.09x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.22x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 250 us: 1.46x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.33 sec: 1.44x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 12.0 ms: 1.39x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 389 us: 1.36x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 77.2 ms: 1.29x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 177 ms: 1.20x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 109 ms: 1.13x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.43 us: 1.09x faster                                                   |
| xml_etree_iterparse  | 156 ms                                                                | 146 ms: 1.06x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.5 us: 1.05x slower                                                   |
| unpickle             | 17.5 us                                                               | 18.4 us: 1.05x slower                                                   |
| pickle_list          | 5.24 us                                                               | 5.69 us: 1.09x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 38.6 us: 1.10x slower                                                   |
| pickle               | 12.5 us                                                               | 15.8 us: 1.27x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.12x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.64 ms: 1.25x slower                                                   |
| python_startup         | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.31x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 12.7 ms: 1.49x faster                                                   |
| django_template | 53.3 ms                                                               | 40.8 ms: 1.31x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.2 ms: 1.29x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 62.9 ms: 1.11x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.29x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 204 us: 3.25x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 884 ms: 2.58x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 472 ms: 2.40x faster                                                    |
| async_tree_none          | 950 ms                                                                | 399 ms: 2.38x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.79 ms: 2.36x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.63 sec: 2.27x faster                                                  |
| richards_super           | 107 ms                                                                | 53.4 ms: 2.01x faster                                                   |
| richards                 | 91.7 ms                                                               | 46.3 ms: 1.98x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 672 ms: 1.89x faster                                                    |
| generators               | 68.1 ms                                                               | 36.5 ms: 1.87x faster                                                   |
| chaos                    | 121 ms                                                                | 67.1 ms: 1.80x faster                                                   |
| raytrace                 | 573 ms                                                                | 327 ms: 1.75x faster                                                    |
| go                       | 264 ms                                                                | 151 ms: 1.75x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 548 ms: 1.72x faster                                                    |
| logging_silent           | 222 ns                                                                | 129 ns: 1.72x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 36.7 us: 1.68x faster                                                   |
| scimark_sor              | 246 ms                                                                | 147 ms: 1.68x faster                                                    |
| float                    | 135 ms                                                                | 82.3 ms: 1.64x faster                                                   |
| spectral_norm            | 186 ms                                                                | 116 ms: 1.60x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 81.1 ms: 1.58x faster                                                   |
| deepcopy                 | 511 us                                                                | 324 us: 1.57x faster                                                    |
| pyflate                  | 795 ms                                                                | 513 ms: 1.55x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 89.2 ms: 1.50x faster                                                   |
| scimark_lu               | 227 ms                                                                | 151 ms: 1.50x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.20 sec: 1.49x faster                                                  |
| mako                     | 18.9 ms                                                               | 12.7 ms: 1.49x faster                                                   |
| pylint                   | 485 ms                                                                | 326 ms: 1.49x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.35 ms: 1.48x faster                                                   |
| comprehensions           | 33.1 us                                                               | 22.6 us: 1.47x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 250 us: 1.46x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.33 sec: 1.44x faster                                                  |
| regex_compile            | 177 ms                                                                | 123 ms: 1.43x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.04 us: 1.39x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 12.0 ms: 1.39x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.65 us: 1.39x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 63.4 ms: 1.36x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 389 us: 1.36x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 54.5 ms: 1.35x faster                                                   |
| django_template          | 53.3 ms                                                               | 40.8 ms: 1.31x faster                                                   |
| nbody                    | 166 ms                                                                | 127 ms: 1.30x faster                                                    |
| thrift                   | 1.26 ms                                                               | 970 us: 1.30x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.56 us: 1.29x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 27.2 ms: 1.29x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 77.2 ms: 1.29x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 20.9 ms: 1.27x faster                                                   |
| sympy_sum                | 184 ms                                                                | 148 ms: 1.24x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.36 sec: 1.24x faster                                                  |
| scimark_fft              | 500 ms                                                                | 406 ms: 1.23x faster                                                    |
| coroutines               | 37.2 ms                                                               | 30.2 ms: 1.23x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 26.3 ms: 1.22x faster                                                   |
| sympy_str                | 329 ms                                                                | 271 ms: 1.21x faster                                                    |
| 2to3                     | 381 ms                                                                | 314 ms: 1.21x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 177 ms: 1.20x faster                                                    |
| fannkuch                 | 546 ms                                                                | 460 ms: 1.19x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 22.5 ms: 1.17x faster                                                   |
| nqueens                  | 117 ms                                                                | 100 ms: 1.17x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.37 ms: 1.16x faster                                                   |
| regex_dna                | 257 ms                                                                | 223 ms: 1.15x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 109 ms: 1.13x faster                                                    |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.13x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.12 sec: 1.13x faster                                                  |
| sympy_expand             | 543 ms                                                                | 486 ms: 1.12x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.70 us: 1.11x faster                                                   |
| genshi_xml               | 69.8 ms                                                               | 62.9 ms: 1.11x faster                                                   |
| regex_effbot             | 4.25 ms                                                               | 3.89 ms: 1.09x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 6.43 us: 1.09x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.03 ms: 1.09x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 146 ms: 1.06x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.09 sec: 1.05x faster                                                  |
| pprint_pformat           | 2.36 sec                                                              | 2.25 sec: 1.05x faster                                                  |
| json                     | 5.88 ms                                                               | 5.71 ms: 1.03x faster                                                   |
| pidigits                 | 235 ms                                                                | 236 ms: 1.00x slower                                                    |
| asyncio_websockets       | 657 ms                                                                | 668 ms: 1.02x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.5 us: 1.05x slower                                                   |
| unpickle                 | 17.5 us                                                               | 18.4 us: 1.05x slower                                                   |
| async_generators         | 452 ms                                                                | 487 ms: 1.08x slower                                                    |
| pickle_list              | 5.24 us                                                               | 5.69 us: 1.09x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 38.6 us: 1.10x slower                                                   |
| coverage                 | 83.6 ms                                                               | 104 ms: 1.25x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.64 ms: 1.25x slower                                                   |
| pickle                   | 12.5 us                                                               | 15.8 us: 1.27x slower                                                   |
| python_startup           | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 6.77 ms: 1.63x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.72 ms: 1.64x slower                                                   |
| telco                    | 8.49 ms                                                               | 163 ms: 19.19x slower                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 1.23 sec: 84.71x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.20x faster                                                            |
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-arminc-aarch64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.295x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.41x