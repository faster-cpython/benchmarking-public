# Results vs. 3.10.4

- fork: faster-cpython
- ref: make_opcode_static
- machine: linux-x86_64
- commit hash: 536ee25
- commit date: 2025-01-31
- overall geometric mean: 1.364x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 279 ms: 1.26x faster                                                                 |
| docutils       | 3.41 sec                                                     | 2.84 sec: 1.20x faster                                                               |
| html5lib       | 94.6 ms                                                      | 65.7 ms: 1.44x faster                                                                |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 652 ms: 2.45x faster                                                                 |
| async_tree_none         | 692 ms                                                       | 288 ms: 2.40x faster                                                                 |
| async_tree_memoization  | 819 ms                                                       | 351 ms: 2.33x faster                                                                 |
| async_tree_cpu_io_mixed | 936 ms                                                       | 520 ms: 1.80x faster                                                                 |
| Geometric mean          | (ref)                                                        | 2.23x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 69.5 ms: 1.60x faster                                                                |
| nbody          | 134 ms                                                       | 88.1 ms: 1.52x faster                                                                |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                                 |
| Geometric mean | (ref)                                                        | 1.38x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 133 ms: 1.42x faster                                                                 |
| regex_dna      | 261 ms                                                       | 230 ms: 1.13x faster                                                                 |
| regex_v8       | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                                                |
| regex_effbot   | 3.09 ms                                                      | 3.13 ms: 1.02x slower                                                                |
| Geometric mean | (ref)                                                        | 1.14x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 205 us: 1.52x faster                                                                 |
| tomli_loads          | 2.92 sec                                                     | 2.04 sec: 1.43x faster                                                               |
| pickle_pure_python   | 455 us                                                       | 322 us: 1.41x faster                                                                 |
| xml_etree_process    | 75.9 ms                                                      | 59.8 ms: 1.27x faster                                                                |
| json_dumps           | 14.5 ms                                                      | 11.6 ms: 1.25x faster                                                                |
| xml_etree_parse      | 160 ms                                                       | 138 ms: 1.16x faster                                                                 |
| xml_etree_iterparse  | 110 ms                                                       | 96.3 ms: 1.15x faster                                                                |
| json_loads           | 30.3 us                                                      | 26.5 us: 1.15x faster                                                                |
| xml_etree_generate   | 92.3 ms                                                      | 84.7 ms: 1.09x faster                                                                |
| Geometric mean       | (ref)                                                        | 1.26x faster                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.00 ms: 1.23x slower                                                                |
| python_startup         | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                                |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.1 ms: 1.43x faster                                                                |
| genshi_text     | 31.4 ms                                                      | 23.0 ms: 1.37x faster                                                                |
| mako            | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                                |
| genshi_xml      | 63.3 ms                                                      | 51.8 ms: 1.22x faster                                                                |
| Geometric mean  | (ref)                                                        | 1.34x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 165 us: 3.25x faster                                                                 |
| async_tree_io            | 1.60 sec                                                     | 652 ms: 2.45x faster                                                                 |
| async_tree_none          | 692 ms                                                       | 288 ms: 2.40x faster                                                                 |
| async_tree_memoization   | 819 ms                                                       | 351 ms: 2.33x faster                                                                 |
| deltablue                | 7.50 ms                                                      | 3.24 ms: 2.31x faster                                                                |
| go                       | 262 ms                                                       | 124 ms: 2.10x faster                                                                 |
| generators               | 57.3 ms                                                      | 28.2 ms: 2.03x faster                                                                |
| raytrace                 | 489 ms                                                       | 264 ms: 1.85x faster                                                                 |
| chaos                    | 109 ms                                                       | 59.8 ms: 1.82x faster                                                                |
| pylint                   | 566 ms                                                       | 313 ms: 1.81x faster                                                                 |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 520 ms: 1.80x faster                                                                 |
| scimark_lu               | 167 ms                                                       | 95.3 ms: 1.75x faster                                                                |
| logging_silent           | 167 ns                                                       | 96.4 ns: 1.74x faster                                                                |
| richards_super           | 90.6 ms                                                      | 52.4 ms: 1.73x faster                                                                |
| spectral_norm            | 139 ms                                                       | 81.3 ms: 1.71x faster                                                                |
| deepcopy_memo            | 49.8 us                                                      | 29.4 us: 1.69x faster                                                                |
| deepcopy                 | 468 us                                                       | 277 us: 1.69x faster                                                                 |
| sqlglot_parse            | 2.24 ms                                                      | 1.33 ms: 1.68x faster                                                                |
| scimark_monte_carlo      | 107 ms                                                       | 64.5 ms: 1.67x faster                                                                |
| pyflate                  | 733 ms                                                       | 442 ms: 1.66x faster                                                                 |
| crypto_pyaes             | 119 ms                                                       | 72.7 ms: 1.64x faster                                                                |
| richards                 | 75.1 ms                                                      | 46.1 ms: 1.63x faster                                                                |
| float                    | 111 ms                                                       | 69.5 ms: 1.60x faster                                                                |
| comprehensions           | 26.7 us                                                      | 16.7 us: 1.60x faster                                                                |
| scimark_sor              | 180 ms                                                       | 113 ms: 1.59x faster                                                                 |
| hexiom                   | 9.42 ms                                                      | 5.98 ms: 1.57x faster                                                                |
| sqlglot_transpile        | 2.68 ms                                                      | 1.71 ms: 1.56x faster                                                                |
| nbody                    | 134 ms                                                       | 88.1 ms: 1.52x faster                                                                |
| unpickle_pure_python     | 312 us                                                       | 205 us: 1.52x faster                                                                 |
| coroutines               | 30.3 ms                                                      | 20.8 ms: 1.46x faster                                                                |
| html5lib                 | 94.6 ms                                                      | 65.7 ms: 1.44x faster                                                                |
| logging_simple           | 8.88 us                                                      | 6.21 us: 1.43x faster                                                                |
| django_template          | 50.2 ms                                                      | 35.1 ms: 1.43x faster                                                                |
| tomli_loads              | 2.92 sec                                                     | 2.04 sec: 1.43x faster                                                               |
| regex_compile            | 190 ms                                                       | 133 ms: 1.42x faster                                                                 |
| logging_format           | 9.64 us                                                      | 6.82 us: 1.41x faster                                                                |
| pickle_pure_python       | 455 us                                                       | 322 us: 1.41x faster                                                                 |
| deepcopy_reduce          | 4.01 us                                                      | 2.86 us: 1.40x faster                                                                |
| pprint_pformat           | 2.15 sec                                                     | 1.56 sec: 1.38x faster                                                               |
| pprint_safe_repr         | 1.05 sec                                                     | 762 ms: 1.38x faster                                                                 |
| thrift                   | 1.18 ms                                                      | 853 us: 1.38x faster                                                                 |
| genshi_text              | 31.4 ms                                                      | 23.0 ms: 1.37x faster                                                                |
| mako                     | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                                |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                                               |
| pathlib                  | 21.4 ms                                                      | 15.9 ms: 1.34x faster                                                                |
| sqlalchemy_declarative   | 190 ms                                                       | 141 ms: 1.34x faster                                                                 |
| fannkuch                 | 483 ms                                                       | 362 ms: 1.33x faster                                                                 |
| nqueens                  | 115 ms                                                       | 86.6 ms: 1.33x faster                                                                |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.6 ms: 1.29x faster                                                                |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.28x faster                                                                 |
| xml_etree_process        | 75.9 ms                                                      | 59.8 ms: 1.27x faster                                                                |
| sympy_str                | 360 ms                                                       | 286 ms: 1.26x faster                                                                 |
| 2to3                     | 350 ms                                                       | 279 ms: 1.26x faster                                                                 |
| sqlglot_normalize        | 144 ms                                                       | 115 ms: 1.25x faster                                                                 |
| json_dumps               | 14.5 ms                                                      | 11.6 ms: 1.25x faster                                                                |
| sqlglot_optimize         | 70.1 ms                                                      | 56.8 ms: 1.23x faster                                                                |
| sympy_expand             | 600 ms                                                       | 488 ms: 1.23x faster                                                                 |
| bench_thread_pool        | 1.14 ms                                                      | 928 us: 1.23x faster                                                                 |
| sympy_integrate          | 28.2 ms                                                      | 23.0 ms: 1.23x faster                                                                |
| genshi_xml               | 63.3 ms                                                      | 51.8 ms: 1.22x faster                                                                |
| mdp                      | 3.01 sec                                                     | 2.46 sec: 1.22x faster                                                               |
| dulwich_log              | 81.1 ms                                                      | 66.9 ms: 1.21x faster                                                                |
| docutils                 | 3.41 sec                                                     | 2.84 sec: 1.20x faster                                                               |
| scimark_fft              | 361 ms                                                       | 309 ms: 1.17x faster                                                                 |
| xml_etree_parse          | 160 ms                                                       | 138 ms: 1.16x faster                                                                 |
| xml_etree_iterparse      | 110 ms                                                       | 96.3 ms: 1.15x faster                                                                |
| json_loads               | 30.3 us                                                      | 26.5 us: 1.15x faster                                                                |
| regex_dna                | 261 ms                                                       | 230 ms: 1.13x faster                                                                 |
| meteor_contest           | 138 ms                                                       | 124 ms: 1.11x faster                                                                 |
| xml_etree_generate       | 92.3 ms                                                      | 84.7 ms: 1.09x faster                                                                |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.67 ms: 1.09x faster                                                                |
| regex_v8                 | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                                                |
| json                     | 5.86 ms                                                      | 5.45 ms: 1.08x faster                                                                |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                                 |
| sqlite_synth             | 2.99 us                                                      | 2.82 us: 1.06x faster                                                                |
| async_generators         | 421 ms                                                       | 411 ms: 1.02x faster                                                                 |
| asyncio_websockets       | 390 ms                                                       | 384 ms: 1.02x faster                                                                 |
| regex_effbot             | 3.09 ms                                                      | 3.13 ms: 1.02x slower                                                                |
| telco                    | 7.23 ms                                                      | 8.07 ms: 1.12x slower                                                                |
| python_startup_no_site   | 7.33 ms                                                      | 9.00 ms: 1.23x slower                                                                |
| coverage                 | 63.3 ms                                                      | 78.6 ms: 1.24x slower                                                                |
| python_startup           | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                                |
| create_gc_cycles         | 1.76 ms                                                      | 2.76 ms: 1.57x slower                                                                |
| gc_traversal             | 3.42 ms                                                      | 6.35 ms: 1.86x slower                                                                |
| bench_mp_pool            | 6.37 ms                                                      | 1.04 sec: 163.69x slower                                                             |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                                         |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250131-3.14.0a4+-536ee25/bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.364x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.27x