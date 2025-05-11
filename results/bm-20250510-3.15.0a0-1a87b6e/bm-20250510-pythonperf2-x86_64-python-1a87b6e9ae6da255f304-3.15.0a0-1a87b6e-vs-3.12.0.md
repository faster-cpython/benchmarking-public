# Results vs. 3.12.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-x86_64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.033x faster
- HPT reliability: 97.55%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 281 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.04 sec                                                     | 629 ms: 1.66x faster                                                        |
| async_tree_memoization  | 544 ms                                                       | 329 ms: 1.65x faster                                                        |
| async_tree_none         | 452 ms                                                       | 286 ms: 1.58x faster                                                        |
| async_tree_cpu_io_mixed | 696 ms                                                       | 503 ms: 1.38x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.56x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 70.1 ms: 1.09x faster                                                       |
| pidigits       | 265 ms                                                       | 257 ms: 1.03x faster                                                        |
| nbody          | 88.0 ms                                                      | 95.1 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 134 ms: 1.07x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.43 ms: 1.04x faster                                                       |
| regex_dna      | 239 ms                                                       | 240 ms: 1.01x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 24.6 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 98.2 ms: 1.05x faster                                                       |
| tomli_loads          | 2.16 sec                                                     | 2.09 sec: 1.03x faster                                                      |
| unpickle             | 14.8 us                                                      | 14.4 us: 1.03x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| xml_etree_generate   | 86.1 ms                                                      | 85.0 ms: 1.01x faster                                                       |
| xml_etree_process    | 58.4 ms                                                      | 58.8 ms: 1.01x slower                                                       |
| unpickle_pure_python | 210 us                                                       | 215 us: 1.03x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 330 us: 1.04x slower                                                        |
| unpickle_list        | 4.66 us                                                      | 4.91 us: 1.05x slower                                                       |
| pickle_dict          | 32.5 us                                                      | 34.6 us: 1.06x slower                                                       |
| json_loads           | 24.4 us                                                      | 26.4 us: 1.08x slower                                                       |
| pickle_list          | 4.43 us                                                      | 4.96 us: 1.12x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 11.9 ms: 1.16x slower                                                       |
| pickle               | 10.5 us                                                      | 12.2 us: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.77 ms: 1.02x slower                                                       |
| python_startup         | 11.6 ms                                                      | 13.6 ms: 1.17x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.8 ms: 1.07x faster                                                       |
| mako            | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                      | 2.57 sec                                                     | 1.29 sec: 1.99x faster                                                      |
| async_tree_io            | 1.04 sec                                                     | 629 ms: 1.66x faster                                                        |
| async_tree_memoization   | 544 ms                                                       | 329 ms: 1.65x faster                                                        |
| async_tree_none          | 452 ms                                                       | 286 ms: 1.58x faster                                                        |
| async_tree_cpu_io_mixed  | 696 ms                                                       | 503 ms: 1.38x faster                                                        |
| deepcopy_memo            | 36.8 us                                                      | 27.6 us: 1.33x faster                                                       |
| deepcopy                 | 368 us                                                       | 278 us: 1.32x faster                                                        |
| generators               | 37.4 ms                                                      | 28.3 ms: 1.32x faster                                                       |
| comprehensions           | 21.9 us                                                      | 17.1 us: 1.28x faster                                                       |
| go                       | 150 ms                                                       | 125 ms: 1.20x faster                                                        |
| unpack_sequence          | 53.2 ns                                                      | 45.7 ns: 1.16x faster                                                       |
| scimark_monte_carlo      | 69.0 ms                                                      | 60.0 ms: 1.15x faster                                                       |
| deepcopy_reduce          | 3.37 us                                                      | 2.96 us: 1.14x faster                                                       |
| float                    | 76.6 ms                                                      | 70.1 ms: 1.09x faster                                                       |
| dulwich_log              | 65.4 ms                                                      | 60.0 ms: 1.09x faster                                                       |
| pathlib                  | 18.9 ms                                                      | 17.4 ms: 1.09x faster                                                       |
| sympy_integrate          | 23.9 ms                                                      | 22.1 ms: 1.08x faster                                                       |
| regex_compile            | 144 ms                                                       | 134 ms: 1.07x faster                                                        |
| chaos                    | 64.0 ms                                                      | 60.0 ms: 1.07x faster                                                       |
| django_template          | 38.2 ms                                                      | 35.8 ms: 1.07x faster                                                       |
| sympy_sum                | 162 ms                                                       | 152 ms: 1.06x faster                                                        |
| raytrace                 | 298 ms                                                       | 282 ms: 1.06x faster                                                        |
| logging_format           | 7.48 us                                                      | 7.13 us: 1.05x faster                                                       |
| xml_etree_iterparse      | 103 ms                                                       | 98.2 ms: 1.05x faster                                                       |
| sympy_str                | 302 ms                                                       | 289 ms: 1.05x faster                                                        |
| pprint_pformat           | 1.65 sec                                                     | 1.59 sec: 1.04x faster                                                      |
| regex_effbot             | 3.57 ms                                                      | 3.43 ms: 1.04x faster                                                       |
| coroutines               | 23.0 ms                                                      | 22.1 ms: 1.04x faster                                                       |
| scimark_lu               | 98.8 ms                                                      | 95.2 ms: 1.04x faster                                                       |
| deltablue                | 3.24 ms                                                      | 3.13 ms: 1.04x faster                                                       |
| tomli_loads              | 2.16 sec                                                     | 2.09 sec: 1.03x faster                                                      |
| scimark_sor              | 109 ms                                                       | 105 ms: 1.03x faster                                                        |
| pprint_safe_repr         | 807 ms                                                       | 782 ms: 1.03x faster                                                        |
| pidigits                 | 265 ms                                                       | 257 ms: 1.03x faster                                                        |
| unpickle                 | 14.8 us                                                      | 14.4 us: 1.03x faster                                                       |
| xml_etree_parse          | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| richards                 | 45.7 ms                                                      | 44.9 ms: 1.02x faster                                                       |
| logging_simple           | 6.71 us                                                      | 6.59 us: 1.02x faster                                                       |
| 2to3                     | 285 ms                                                       | 281 ms: 1.01x faster                                                        |
| asyncio_tcp              | 378 ms                                                       | 373 ms: 1.01x faster                                                        |
| xml_etree_generate       | 86.1 ms                                                      | 85.0 ms: 1.01x faster                                                       |
| crypto_pyaes             | 80.3 ms                                                      | 79.8 ms: 1.01x faster                                                       |
| meteor_contest           | 128 ms                                                       | 128 ms: 1.00x faster                                                        |
| regex_dna                | 239 ms                                                       | 240 ms: 1.01x slower                                                        |
| xml_etree_process        | 58.4 ms                                                      | 58.8 ms: 1.01x slower                                                       |
| spectral_norm            | 91.6 ms                                                      | 92.6 ms: 1.01x slower                                                       |
| python_startup_no_site   | 8.64 ms                                                      | 8.77 ms: 1.02x slower                                                       |
| hexiom                   | 5.96 ms                                                      | 6.08 ms: 1.02x slower                                                       |
| pycparser                | 1.23 sec                                                     | 1.27 sec: 1.03x slower                                                      |
| sympy_expand             | 484 ms                                                       | 497 ms: 1.03x slower                                                        |
| nqueens                  | 89.9 ms                                                      | 92.2 ms: 1.03x slower                                                       |
| unpickle_pure_python     | 210 us                                                       | 215 us: 1.03x slower                                                        |
| pyflate                  | 439 ms                                                       | 452 ms: 1.03x slower                                                        |
| pickle_pure_python       | 318 us                                                       | 330 us: 1.04x slower                                                        |
| scimark_fft              | 301 ms                                                       | 313 ms: 1.04x slower                                                        |
| bench_thread_pool        | 950 us                                                       | 986 us: 1.04x slower                                                        |
| regex_v8                 | 23.6 ms                                                      | 24.6 ms: 1.04x slower                                                       |
| sqlite_synth             | 2.77 us                                                      | 2.89 us: 1.04x slower                                                       |
| json                     | 5.12 ms                                                      | 5.39 ms: 1.05x slower                                                       |
| fannkuch                 | 350 ms                                                       | 369 ms: 1.05x slower                                                        |
| unpickle_list            | 4.66 us                                                      | 4.91 us: 1.05x slower                                                       |
| pickle_dict              | 32.5 us                                                      | 34.6 us: 1.06x slower                                                       |
| nbody                    | 88.0 ms                                                      | 95.1 ms: 1.08x slower                                                       |
| mako                     | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                       |
| json_loads               | 24.4 us                                                      | 26.4 us: 1.08x slower                                                       |
| async_generators         | 390 ms                                                       | 429 ms: 1.10x slower                                                        |
| pickle_list              | 4.43 us                                                      | 4.96 us: 1.12x slower                                                       |
| scimark_sparse_mat_mult  | 4.21 ms                                                      | 4.75 ms: 1.13x slower                                                       |
| typing_runtime_protocols | 152 us                                                       | 171 us: 1.13x slower                                                        |
| telco                    | 6.96 ms                                                      | 7.91 ms: 1.14x slower                                                       |
| json_dumps               | 10.2 ms                                                      | 11.9 ms: 1.16x slower                                                       |
| pickle                   | 10.5 us                                                      | 12.2 us: 1.16x slower                                                       |
| python_startup           | 11.6 ms                                                      | 13.6 ms: 1.17x slower                                                       |
| coverage                 | 66.7 ms                                                      | 84.6 ms: 1.27x slower                                                       |
| create_gc_cycles         | 1.59 ms                                                      | 2.80 ms: 1.76x slower                                                       |
| gc_traversal             | 3.48 ms                                                      | 6.42 ms: 1.85x slower                                                       |
| logging_silent           | 94.4 ns                                                      | 517 ns: 5.48x slower                                                        |
| bench_mp_pool            | 4.76 ms                                                      | 1.32 sec: 277.35x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.07x slower                                                                |

Benchmark hidden because not significant (4): richards_super, asyncio_tcp_ssl, docutils, asyncio_websockets
Ignored benchmarks (16) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: bpe_tokeniser, djangocms, genshi_text, genshi_xml, html5lib, many_optionals, pylint, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.033x faster

# HPT report

- Reliability score: 97.55% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x