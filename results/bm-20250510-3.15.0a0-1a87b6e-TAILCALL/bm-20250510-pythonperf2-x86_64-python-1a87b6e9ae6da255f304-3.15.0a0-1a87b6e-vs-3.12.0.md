# Results vs. 3.12.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-x86_64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.058x faster
- HPT reliability: 99.73%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 279 ms: 1.02x faster                                                        |
| docutils       | 2.87 sec                                                     | 2.89 sec: 1.01x slower                                                      |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization  | 544 ms                                                       | 313 ms: 1.74x faster                                                        |
| async_tree_io           | 1.04 sec                                                     | 604 ms: 1.73x faster                                                        |
| async_tree_none         | 452 ms                                                       | 272 ms: 1.66x faster                                                        |
| async_tree_cpu_io_mixed | 696 ms                                                       | 518 ms: 1.34x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.61x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 65.8 ms: 1.17x faster                                                       |
| nbody          | 88.0 ms                                                      | 94.6 ms: 1.08x slower                                                       |
| pidigits       | 265 ms                                                       | 292 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 131 ms: 1.10x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.52 ms: 1.02x faster                                                       |
| regex_dna      | 239 ms                                                       | 242 ms: 1.01x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 28.3 ms: 1.20x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle             | 14.8 us                                                      | 13.7 us: 1.08x faster                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 80.0 ms: 1.08x faster                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.01 sec: 1.07x faster                                                      |
| pickle_dict          | 32.5 us                                                      | 31.3 us: 1.04x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 56.3 ms: 1.04x faster                                                       |
| unpickle_pure_python | 210 us                                                       | 202 us: 1.04x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 313 us: 1.02x faster                                                        |
| pickle_list          | 4.43 us                                                      | 4.48 us: 1.01x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 4.92 us: 1.06x slower                                                       |
| json_loads           | 24.4 us                                                      | 26.3 us: 1.08x slower                                                       |
| pickle               | 10.5 us                                                      | 12.0 us: 1.14x slower                                                       |
| xml_etree_parse      | 144 ms                                                       | 167 ms: 1.16x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 12.0 ms: 1.17x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.90 ms: 1.03x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.7 ms: 1.18x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 34.4 ms: 1.11x faster                                                       |
| mako            | 10.0 ms                                                      | 11.1 ms: 1.11x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.00x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                      | 2.57 sec                                                     | 1.27 sec: 2.02x faster                                                      |
| async_tree_memoization   | 544 ms                                                       | 313 ms: 1.74x faster                                                        |
| async_tree_io            | 1.04 sec                                                     | 604 ms: 1.73x faster                                                        |
| async_tree_none          | 452 ms                                                       | 272 ms: 1.66x faster                                                        |
| deepcopy                 | 368 us                                                       | 257 us: 1.44x faster                                                        |
| deepcopy_memo            | 36.8 us                                                      | 26.2 us: 1.40x faster                                                       |
| async_tree_cpu_io_mixed  | 696 ms                                                       | 518 ms: 1.34x faster                                                        |
| comprehensions           | 21.9 us                                                      | 16.5 us: 1.33x faster                                                       |
| deepcopy_reduce          | 3.37 us                                                      | 2.70 us: 1.25x faster                                                       |
| go                       | 150 ms                                                       | 121 ms: 1.24x faster                                                        |
| generators               | 37.4 ms                                                      | 30.4 ms: 1.23x faster                                                       |
| scimark_monte_carlo      | 69.0 ms                                                      | 57.5 ms: 1.20x faster                                                       |
| scimark_sor              | 109 ms                                                       | 91.5 ms: 1.19x faster                                                       |
| raytrace                 | 298 ms                                                       | 253 ms: 1.18x faster                                                        |
| float                    | 76.6 ms                                                      | 65.8 ms: 1.17x faster                                                       |
| pathlib                  | 18.9 ms                                                      | 16.6 ms: 1.14x faster                                                       |
| chaos                    | 64.0 ms                                                      | 56.9 ms: 1.12x faster                                                       |
| scimark_lu               | 98.8 ms                                                      | 88.1 ms: 1.12x faster                                                       |
| dulwich_log              | 65.4 ms                                                      | 58.9 ms: 1.11x faster                                                       |
| django_template          | 38.2 ms                                                      | 34.4 ms: 1.11x faster                                                       |
| coroutines               | 23.0 ms                                                      | 20.9 ms: 1.10x faster                                                       |
| sympy_integrate          | 23.9 ms                                                      | 21.8 ms: 1.10x faster                                                       |
| regex_compile            | 144 ms                                                       | 131 ms: 1.10x faster                                                        |
| sympy_sum                | 162 ms                                                       | 149 ms: 1.08x faster                                                        |
| pyflate                  | 439 ms                                                       | 405 ms: 1.08x faster                                                        |
| richards                 | 45.7 ms                                                      | 42.3 ms: 1.08x faster                                                       |
| scimark_fft              | 301 ms                                                       | 279 ms: 1.08x faster                                                        |
| unpickle                 | 14.8 us                                                      | 13.7 us: 1.08x faster                                                       |
| xml_etree_generate       | 86.1 ms                                                      | 80.0 ms: 1.08x faster                                                       |
| tomli_loads              | 2.16 sec                                                     | 2.01 sec: 1.07x faster                                                      |
| pprint_pformat           | 1.65 sec                                                     | 1.54 sec: 1.07x faster                                                      |
| spectral_norm            | 91.6 ms                                                      | 86.0 ms: 1.07x faster                                                       |
| pprint_safe_repr         | 807 ms                                                       | 758 ms: 1.06x faster                                                        |
| sympy_str                | 302 ms                                                       | 285 ms: 1.06x faster                                                        |
| hexiom                   | 5.96 ms                                                      | 5.62 ms: 1.06x faster                                                       |
| deltablue                | 3.24 ms                                                      | 3.05 ms: 1.06x faster                                                       |
| richards_super           | 51.3 ms                                                      | 48.5 ms: 1.06x faster                                                       |
| crypto_pyaes             | 80.3 ms                                                      | 76.3 ms: 1.05x faster                                                       |
| pickle_dict              | 32.5 us                                                      | 31.3 us: 1.04x faster                                                       |
| logging_format           | 7.48 us                                                      | 7.19 us: 1.04x faster                                                       |
| logging_simple           | 6.71 us                                                      | 6.45 us: 1.04x faster                                                       |
| xml_etree_process        | 58.4 ms                                                      | 56.3 ms: 1.04x faster                                                       |
| unpickle_pure_python     | 210 us                                                       | 202 us: 1.04x faster                                                        |
| 2to3                     | 285 ms                                                       | 279 ms: 1.02x faster                                                        |
| asyncio_tcp              | 378 ms                                                       | 371 ms: 1.02x faster                                                        |
| pickle_pure_python       | 318 us                                                       | 313 us: 1.02x faster                                                        |
| regex_effbot             | 3.57 ms                                                      | 3.52 ms: 1.02x faster                                                       |
| asyncio_tcp_ssl          | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                      |
| nqueens                  | 89.9 ms                                                      | 89.4 ms: 1.01x faster                                                       |
| sympy_expand             | 484 ms                                                       | 485 ms: 1.00x slower                                                        |
| sqlite_synth             | 2.77 us                                                      | 2.80 us: 1.01x slower                                                       |
| docutils                 | 2.87 sec                                                     | 2.89 sec: 1.01x slower                                                      |
| pickle_list              | 4.43 us                                                      | 4.48 us: 1.01x slower                                                       |
| regex_dna                | 239 ms                                                       | 242 ms: 1.01x slower                                                        |
| pycparser                | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                                      |
| scimark_sparse_mat_mult  | 4.21 ms                                                      | 4.30 ms: 1.02x slower                                                       |
| python_startup_no_site   | 8.64 ms                                                      | 8.90 ms: 1.03x slower                                                       |
| json                     | 5.12 ms                                                      | 5.32 ms: 1.04x slower                                                       |
| telco                    | 6.96 ms                                                      | 7.30 ms: 1.05x slower                                                       |
| meteor_contest           | 128 ms                                                       | 135 ms: 1.06x slower                                                        |
| unpickle_list            | 4.66 us                                                      | 4.92 us: 1.06x slower                                                       |
| nbody                    | 88.0 ms                                                      | 94.6 ms: 1.08x slower                                                       |
| typing_runtime_protocols | 152 us                                                       | 164 us: 1.08x slower                                                        |
| json_loads               | 24.4 us                                                      | 26.3 us: 1.08x slower                                                       |
| fannkuch                 | 350 ms                                                       | 379 ms: 1.08x slower                                                        |
| pidigits                 | 265 ms                                                       | 292 ms: 1.10x slower                                                        |
| mako                     | 10.0 ms                                                      | 11.1 ms: 1.11x slower                                                       |
| unpack_sequence          | 53.2 ns                                                      | 59.9 ns: 1.13x slower                                                       |
| pickle                   | 10.5 us                                                      | 12.0 us: 1.14x slower                                                       |
| async_generators         | 390 ms                                                       | 447 ms: 1.15x slower                                                        |
| xml_etree_parse          | 144 ms                                                       | 167 ms: 1.16x slower                                                        |
| coverage                 | 66.7 ms                                                      | 77.6 ms: 1.16x slower                                                       |
| json_dumps               | 10.2 ms                                                      | 12.0 ms: 1.17x slower                                                       |
| python_startup           | 11.6 ms                                                      | 13.7 ms: 1.18x slower                                                       |
| regex_v8                 | 23.6 ms                                                      | 28.3 ms: 1.20x slower                                                       |
| gc_traversal             | 3.48 ms                                                      | 5.42 ms: 1.56x slower                                                       |
| create_gc_cycles         | 1.59 ms                                                      | 2.90 ms: 1.82x slower                                                       |
| logging_silent           | 94.4 ns                                                      | 504 ns: 5.34x slower                                                        |
| bench_mp_pool            | 4.76 ms                                                      | 1.22 sec: 256.88x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (3): bench_thread_pool, asyncio_websockets, xml_etree_iterparse
Ignored benchmarks (16) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: bpe_tokeniser, djangocms, genshi_text, genshi_xml, html5lib, many_optionals, pylint, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.058x faster

# HPT report

- Reliability score: 99.73% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x