# Results vs. 3.12.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-x86_64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.033x faster
- HPT reliability: 98.47%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 286 ms: 1.00x slower                                                        |
| docutils       | 2.87 sec                                                     | 2.93 sec: 1.02x slower                                                      |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.04 sec                                                     | 615 ms: 1.69x faster                                                        |
| async_tree_memoization  | 544 ms                                                       | 326 ms: 1.67x faster                                                        |
| async_tree_none         | 452 ms                                                       | 285 ms: 1.59x faster                                                        |
| async_tree_cpu_io_mixed | 696 ms                                                       | 504 ms: 1.38x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.58x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 63.6 ms: 1.21x faster                                                       |
| pidigits       | 265 ms                                                       | 257 ms: 1.03x faster                                                        |
| nbody          | 88.0 ms                                                      | 96.5 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.33 ms: 1.07x faster                                                       |
| regex_compile  | 144 ms                                                       | 135 ms: 1.07x faster                                                        |
| regex_dna      | 239 ms                                                       | 227 ms: 1.05x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 23.7 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 2.02 sec: 1.07x faster                                                      |
| xml_etree_iterparse  | 103 ms                                                       | 98.1 ms: 1.05x faster                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 82.3 ms: 1.05x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 56.7 ms: 1.03x faster                                                       |
| unpickle             | 14.8 us                                                      | 14.5 us: 1.02x faster                                                       |
| unpickle_pure_python | 210 us                                                       | 208 us: 1.01x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 330 us: 1.04x slower                                                        |
| unpickle_list        | 4.66 us                                                      | 5.00 us: 1.07x slower                                                       |
| json_loads           | 24.4 us                                                      | 26.5 us: 1.09x slower                                                       |
| pickle_dict          | 32.5 us                                                      | 36.3 us: 1.12x slower                                                       |
| pickle_list          | 4.43 us                                                      | 5.10 us: 1.15x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 11.9 ms: 1.16x slower                                                       |
| pickle               | 10.5 us                                                      | 12.3 us: 1.17x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.80 ms: 1.02x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.6 ms: 1.17x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 36.2 ms: 1.05x faster                                                       |
| mako            | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                      | 2.57 sec                                                     | 1.31 sec: 1.97x faster                                                      |
| async_tree_io            | 1.04 sec                                                     | 615 ms: 1.69x faster                                                        |
| async_tree_memoization   | 544 ms                                                       | 326 ms: 1.67x faster                                                        |
| async_tree_none          | 452 ms                                                       | 285 ms: 1.59x faster                                                        |
| async_tree_cpu_io_mixed  | 696 ms                                                       | 504 ms: 1.38x faster                                                        |
| deepcopy                 | 368 us                                                       | 274 us: 1.34x faster                                                        |
| generators               | 37.4 ms                                                      | 28.5 ms: 1.31x faster                                                       |
| deepcopy_memo            | 36.8 us                                                      | 28.3 us: 1.30x faster                                                       |
| richards                 | 45.7 ms                                                      | 37.4 ms: 1.22x faster                                                       |
| float                    | 76.6 ms                                                      | 63.6 ms: 1.21x faster                                                       |
| richards_super           | 51.3 ms                                                      | 42.8 ms: 1.20x faster                                                       |
| deepcopy_reduce          | 3.37 us                                                      | 2.90 us: 1.16x faster                                                       |
| comprehensions           | 21.9 us                                                      | 19.2 us: 1.14x faster                                                       |
| deltablue                | 3.24 ms                                                      | 2.96 ms: 1.09x faster                                                       |
| dulwich_log              | 65.4 ms                                                      | 59.9 ms: 1.09x faster                                                       |
| pathlib                  | 18.9 ms                                                      | 17.4 ms: 1.09x faster                                                       |
| go                       | 150 ms                                                       | 138 ms: 1.08x faster                                                        |
| regex_effbot             | 3.57 ms                                                      | 3.33 ms: 1.07x faster                                                       |
| tomli_loads              | 2.16 sec                                                     | 2.02 sec: 1.07x faster                                                      |
| sympy_integrate          | 23.9 ms                                                      | 22.4 ms: 1.07x faster                                                       |
| regex_compile            | 144 ms                                                       | 135 ms: 1.07x faster                                                        |
| sympy_sum                | 162 ms                                                       | 152 ms: 1.06x faster                                                        |
| django_template          | 38.2 ms                                                      | 36.2 ms: 1.05x faster                                                       |
| regex_dna                | 239 ms                                                       | 227 ms: 1.05x faster                                                        |
| scimark_sor              | 109 ms                                                       | 104 ms: 1.05x faster                                                        |
| logging_format           | 7.48 us                                                      | 7.14 us: 1.05x faster                                                       |
| xml_etree_iterparse      | 103 ms                                                       | 98.1 ms: 1.05x faster                                                       |
| xml_etree_generate       | 86.1 ms                                                      | 82.3 ms: 1.05x faster                                                       |
| scimark_lu               | 98.8 ms                                                      | 94.7 ms: 1.04x faster                                                       |
| chaos                    | 64.0 ms                                                      | 61.4 ms: 1.04x faster                                                       |
| xml_etree_parse          | 144 ms                                                       | 138 ms: 1.04x faster                                                        |
| logging_simple           | 6.71 us                                                      | 6.49 us: 1.03x faster                                                       |
| sympy_str                | 302 ms                                                       | 292 ms: 1.03x faster                                                        |
| scimark_monte_carlo      | 69.0 ms                                                      | 66.7 ms: 1.03x faster                                                       |
| raytrace                 | 298 ms                                                       | 288 ms: 1.03x faster                                                        |
| coroutines               | 23.0 ms                                                      | 22.3 ms: 1.03x faster                                                       |
| pidigits                 | 265 ms                                                       | 257 ms: 1.03x faster                                                        |
| xml_etree_process        | 58.4 ms                                                      | 56.7 ms: 1.03x faster                                                       |
| unpickle                 | 14.8 us                                                      | 14.5 us: 1.02x faster                                                       |
| pprint_pformat           | 1.65 sec                                                     | 1.63 sec: 1.02x faster                                                      |
| asyncio_tcp              | 378 ms                                                       | 373 ms: 1.01x faster                                                        |
| pycparser                | 1.23 sec                                                     | 1.22 sec: 1.01x faster                                                      |
| unpickle_pure_python     | 210 us                                                       | 208 us: 1.01x faster                                                        |
| asyncio_tcp_ssl          | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| 2to3                     | 285 ms                                                       | 286 ms: 1.00x slower                                                        |
| regex_v8                 | 23.6 ms                                                      | 23.7 ms: 1.00x slower                                                       |
| pprint_safe_repr         | 807 ms                                                       | 815 ms: 1.01x slower                                                        |
| python_startup_no_site   | 8.64 ms                                                      | 8.80 ms: 1.02x slower                                                       |
| docutils                 | 2.87 sec                                                     | 2.93 sec: 1.02x slower                                                      |
| sqlite_synth             | 2.77 us                                                      | 2.86 us: 1.03x slower                                                       |
| nqueens                  | 89.9 ms                                                      | 92.7 ms: 1.03x slower                                                       |
| pickle_pure_python       | 318 us                                                       | 330 us: 1.04x slower                                                        |
| pyflate                  | 439 ms                                                       | 456 ms: 1.04x slower                                                        |
| bench_thread_pool        | 950 us                                                       | 988 us: 1.04x slower                                                        |
| meteor_contest           | 128 ms                                                       | 134 ms: 1.04x slower                                                        |
| mako                     | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                       |
| sympy_expand             | 484 ms                                                       | 505 ms: 1.04x slower                                                        |
| json                     | 5.12 ms                                                      | 5.38 ms: 1.05x slower                                                       |
| scimark_fft              | 301 ms                                                       | 319 ms: 1.06x slower                                                        |
| unpickle_list            | 4.66 us                                                      | 5.00 us: 1.07x slower                                                       |
| json_loads               | 24.4 us                                                      | 26.5 us: 1.09x slower                                                       |
| nbody                    | 88.0 ms                                                      | 96.5 ms: 1.10x slower                                                       |
| hexiom                   | 5.96 ms                                                      | 6.57 ms: 1.10x slower                                                       |
| pickle_dict              | 32.5 us                                                      | 36.3 us: 1.12x slower                                                       |
| telco                    | 6.96 ms                                                      | 7.94 ms: 1.14x slower                                                       |
| async_generators         | 390 ms                                                       | 446 ms: 1.14x slower                                                        |
| pickle_list              | 4.43 us                                                      | 5.10 us: 1.15x slower                                                       |
| json_dumps               | 10.2 ms                                                      | 11.9 ms: 1.16x slower                                                       |
| typing_runtime_protocols | 152 us                                                       | 177 us: 1.16x slower                                                        |
| pickle                   | 10.5 us                                                      | 12.3 us: 1.17x slower                                                       |
| python_startup           | 11.6 ms                                                      | 13.6 ms: 1.17x slower                                                       |
| fannkuch                 | 350 ms                                                       | 412 ms: 1.18x slower                                                        |
| unpack_sequence          | 53.2 ns                                                      | 63.3 ns: 1.19x slower                                                       |
| scimark_sparse_mat_mult  | 4.21 ms                                                      | 5.01 ms: 1.19x slower                                                       |
| coverage                 | 66.7 ms                                                      | 79.6 ms: 1.19x slower                                                       |
| create_gc_cycles         | 1.59 ms                                                      | 2.81 ms: 1.77x slower                                                       |
| gc_traversal             | 3.48 ms                                                      | 6.47 ms: 1.86x slower                                                       |
| logging_silent           | 94.4 ns                                                      | 507 ns: 5.37x slower                                                        |
| bench_mp_pool            | 4.76 ms                                                      | 1.28 sec: 269.50x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.07x slower                                                                |

Benchmark hidden because not significant (3): asyncio_websockets, spectral_norm, crypto_pyaes
Ignored benchmarks (16) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: bpe_tokeniser, djangocms, genshi_text, genshi_xml, html5lib, many_optionals, pylint, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.033x faster

# HPT report

- Reliability score: 98.47% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x