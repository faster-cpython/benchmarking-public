# Results vs. 3.12.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-x86_64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.057x slower
- HPT reliability: 99.87%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 317 ms: 1.11x slower                                                        |
| docutils       | 2.87 sec                                                     | 2.91 sec: 1.02x slower                                                      |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.04 sec                                                     | 560 ms: 1.86x faster                                                        |
| async_tree_none         | 452 ms                                                       | 265 ms: 1.71x faster                                                        |
| async_tree_memoization  | 544 ms                                                       | 321 ms: 1.69x faster                                                        |
| async_tree_cpu_io_mixed | 696 ms                                                       | 502 ms: 1.39x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.65x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 71.6 ms: 1.07x faster                                                       |
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                                        |
| nbody          | 88.0 ms                                                      | 128 ms: 1.45x slower                                                        |
| Geometric mean | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.37 ms: 1.06x faster                                                       |
| regex_dna      | 239 ms                                                       | 236 ms: 1.01x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 23.8 ms: 1.01x slower                                                       |
| regex_compile  | 144 ms                                                       | 156 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 88.4 ms: 1.16x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.28 sec: 1.06x slower                                                      |
| pickle_dict          | 32.5 us                                                      | 36.1 us: 1.11x slower                                                       |
| unpickle             | 14.8 us                                                      | 16.4 us: 1.11x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 234 us: 1.11x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 359 us: 1.13x slower                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 99.6 ms: 1.16x slower                                                       |
| pickle               | 10.5 us                                                      | 12.5 us: 1.19x slower                                                       |
| pickle_list          | 4.43 us                                                      | 5.27 us: 1.19x slower                                                       |
| json_loads           | 24.4 us                                                      | 29.1 us: 1.19x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 69.9 ms: 1.20x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 5.68 us: 1.22x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 13.7 ms: 1.34x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.12x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 11.8 ms: 1.36x slower                                                       |
| python_startup         | 11.6 ms                                                      | 17.7 ms: 1.52x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.44x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 42.6 ms: 1.12x slower                                                       |
| mako            | 10.0 ms                                                      | 17.4 ms: 1.73x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.39x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io            | 1.04 sec                                                     | 560 ms: 1.86x faster                                                        |
| mdp                      | 2.57 sec                                                     | 1.49 sec: 1.73x faster                                                      |
| async_tree_none          | 452 ms                                                       | 265 ms: 1.71x faster                                                        |
| async_tree_memoization   | 544 ms                                                       | 321 ms: 1.69x faster                                                        |
| gc_traversal             | 3.48 ms                                                      | 2.22 ms: 1.57x faster                                                       |
| async_tree_cpu_io_mixed  | 696 ms                                                       | 502 ms: 1.39x faster                                                        |
| xml_etree_iterparse      | 103 ms                                                       | 88.4 ms: 1.16x faster                                                       |
| generators               | 37.4 ms                                                      | 32.2 ms: 1.16x faster                                                       |
| deepcopy                 | 368 us                                                       | 319 us: 1.16x faster                                                        |
| pathlib                  | 18.9 ms                                                      | 17.3 ms: 1.09x faster                                                       |
| comprehensions           | 21.9 us                                                      | 20.2 us: 1.09x faster                                                       |
| deepcopy_memo            | 36.8 us                                                      | 34.1 us: 1.08x faster                                                       |
| float                    | 76.6 ms                                                      | 71.6 ms: 1.07x faster                                                       |
| regex_effbot             | 3.57 ms                                                      | 3.37 ms: 1.06x faster                                                       |
| pidigits                 | 265 ms                                                       | 252 ms: 1.05x faster                                                        |
| sqlite_synth             | 2.77 us                                                      | 2.65 us: 1.05x faster                                                       |
| coroutines               | 23.0 ms                                                      | 22.0 ms: 1.05x faster                                                       |
| go                       | 150 ms                                                       | 143 ms: 1.05x faster                                                        |
| xml_etree_parse          | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| dulwich_log              | 65.4 ms                                                      | 62.7 ms: 1.04x faster                                                       |
| asyncio_websockets       | 387 ms                                                       | 379 ms: 1.02x faster                                                        |
| regex_dna                | 239 ms                                                       | 236 ms: 1.01x faster                                                        |
| regex_v8                 | 23.6 ms                                                      | 23.8 ms: 1.01x slower                                                       |
| docutils                 | 2.87 sec                                                     | 2.91 sec: 1.02x slower                                                      |
| deepcopy_reduce          | 3.37 us                                                      | 3.42 us: 1.02x slower                                                       |
| pycparser                | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                                      |
| chaos                    | 64.0 ms                                                      | 67.4 ms: 1.05x slower                                                       |
| tomli_loads              | 2.16 sec                                                     | 2.28 sec: 1.06x slower                                                      |
| sympy_integrate          | 23.9 ms                                                      | 25.4 ms: 1.06x slower                                                       |
| sympy_sum                | 162 ms                                                       | 172 ms: 1.06x slower                                                        |
| unpack_sequence          | 53.2 ns                                                      | 57.0 ns: 1.07x slower                                                       |
| scimark_sor              | 109 ms                                                       | 117 ms: 1.07x slower                                                        |
| regex_compile            | 144 ms                                                       | 156 ms: 1.08x slower                                                        |
| pyflate                  | 439 ms                                                       | 475 ms: 1.08x slower                                                        |
| raytrace                 | 298 ms                                                       | 323 ms: 1.09x slower                                                        |
| sympy_str                | 302 ms                                                       | 328 ms: 1.09x slower                                                        |
| logging_format           | 7.48 us                                                      | 8.21 us: 1.10x slower                                                       |
| logging_simple           | 6.71 us                                                      | 7.41 us: 1.10x slower                                                       |
| pprint_safe_repr         | 807 ms                                                       | 893 ms: 1.11x slower                                                        |
| pickle_dict              | 32.5 us                                                      | 36.1 us: 1.11x slower                                                       |
| unpickle                 | 14.8 us                                                      | 16.4 us: 1.11x slower                                                       |
| pprint_pformat           | 1.65 sec                                                     | 1.84 sec: 1.11x slower                                                      |
| 2to3                     | 285 ms                                                       | 317 ms: 1.11x slower                                                        |
| unpickle_pure_python     | 210 us                                                       | 234 us: 1.11x slower                                                        |
| json                     | 5.12 ms                                                      | 5.71 ms: 1.12x slower                                                       |
| django_template          | 38.2 ms                                                      | 42.6 ms: 1.12x slower                                                       |
| scimark_lu               | 98.8 ms                                                      | 111 ms: 1.12x slower                                                        |
| asyncio_tcp              | 378 ms                                                       | 423 ms: 1.12x slower                                                        |
| spectral_norm            | 91.6 ms                                                      | 103 ms: 1.12x slower                                                        |
| pickle_pure_python       | 318 us                                                       | 359 us: 1.13x slower                                                        |
| deltablue                | 3.24 ms                                                      | 3.65 ms: 1.13x slower                                                       |
| hexiom                   | 5.96 ms                                                      | 6.83 ms: 1.15x slower                                                       |
| nqueens                  | 89.9 ms                                                      | 104 ms: 1.15x slower                                                        |
| sympy_expand             | 484 ms                                                       | 559 ms: 1.16x slower                                                        |
| xml_etree_generate       | 86.1 ms                                                      | 99.6 ms: 1.16x slower                                                       |
| crypto_pyaes             | 80.3 ms                                                      | 94.8 ms: 1.18x slower                                                       |
| scimark_fft              | 301 ms                                                       | 356 ms: 1.18x slower                                                        |
| asyncio_tcp_ssl          | 1.59 sec                                                     | 1.88 sec: 1.18x slower                                                      |
| richards                 | 45.7 ms                                                      | 54.2 ms: 1.19x slower                                                       |
| scimark_monte_carlo      | 69.0 ms                                                      | 81.9 ms: 1.19x slower                                                       |
| pickle                   | 10.5 us                                                      | 12.5 us: 1.19x slower                                                       |
| pickle_list              | 4.43 us                                                      | 5.27 us: 1.19x slower                                                       |
| json_loads               | 24.4 us                                                      | 29.1 us: 1.19x slower                                                       |
| xml_etree_process        | 58.4 ms                                                      | 69.9 ms: 1.20x slower                                                       |
| meteor_contest           | 128 ms                                                       | 154 ms: 1.20x slower                                                        |
| richards_super           | 51.3 ms                                                      | 62.2 ms: 1.21x slower                                                       |
| unpickle_list            | 4.66 us                                                      | 5.68 us: 1.22x slower                                                       |
| async_generators         | 390 ms                                                       | 484 ms: 1.24x slower                                                        |
| create_gc_cycles         | 1.59 ms                                                      | 2.04 ms: 1.28x slower                                                       |
| telco                    | 6.96 ms                                                      | 9.20 ms: 1.32x slower                                                       |
| fannkuch                 | 350 ms                                                       | 463 ms: 1.32x slower                                                        |
| json_dumps               | 10.2 ms                                                      | 13.7 ms: 1.34x slower                                                       |
| python_startup_no_site   | 8.64 ms                                                      | 11.8 ms: 1.36x slower                                                       |
| scimark_sparse_mat_mult  | 4.21 ms                                                      | 5.93 ms: 1.41x slower                                                       |
| typing_runtime_protocols | 152 us                                                       | 218 us: 1.44x slower                                                        |
| nbody                    | 88.0 ms                                                      | 128 ms: 1.45x slower                                                        |
| bench_thread_pool        | 950 us                                                       | 1.42 ms: 1.49x slower                                                       |
| python_startup           | 11.6 ms                                                      | 17.7 ms: 1.52x slower                                                       |
| mako                     | 10.0 ms                                                      | 17.4 ms: 1.73x slower                                                       |
| coverage                 | 66.7 ms                                                      | 122 ms: 1.84x slower                                                        |
| logging_silent           | 94.4 ns                                                      | 608 ns: 6.45x slower                                                        |
| bench_mp_pool            | 4.76 ms                                                      | 57.1 ms: 11.99x slower                                                      |
| Geometric mean           | (ref)                                                        | 1.13x slower                                                                |
Ignored benchmarks (16) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, many_optionals, pylint, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.057x slower

# HPT report

- Reliability score: 99.87% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.33x