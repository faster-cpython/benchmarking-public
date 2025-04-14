# Results vs. 3.12.0

- fork: python
- ref: v3.14.0a5
- machine: linux-x86_64
- commit hash: 3ae9101
- commit date: 2025-02-11
- overall geometric mean: 1.108x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 257 ms: 1.07x faster                                       |
| docutils       | 2.77 sec                                               | 2.66 sec: 1.04x faster                                     |
| Geometric mean | (ref)                                                  | 1.05x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 619 ms: 1.91x faster                                       |
| async_tree_io              | 1.16 sec                                               | 623 ms: 1.86x faster                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 321 ms: 1.79x faster                                       |
| async_tree_memoization     | 578 ms                                                 | 328 ms: 1.76x faster                                       |
| async_tree_none            | 472 ms                                                 | 269 ms: 1.75x faster                                       |
| async_tree_none_tg         | 450 ms                                                 | 262 ms: 1.72x faster                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 493 ms: 1.47x faster                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 503 ms: 1.44x faster                                       |
| Geometric mean             | (ref)                                                  | 1.71x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.1 ms: 1.23x faster                                      |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                       |
| nbody          | 97.0 ms                                                | 97.7 ms: 1.01x slower                                      |
| Geometric mean | (ref)                                                  | 1.07x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.19x faster                                       |
| regex_effbot   | 3.61 ms                                                | 3.20 ms: 1.13x faster                                      |
| regex_dna      | 212 ms                                                 | 206 ms: 1.03x faster                                       |
| regex_v8       | 23.1 ms                                                | 23.5 ms: 1.02x slower                                      |
| Geometric mean | (ref)                                                  | 1.08x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.86 sec: 1.25x faster                                     |
| unpickle_pure_python | 230 us                                                 | 199 us: 1.16x faster                                       |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.14x faster                                       |
| xml_etree_generate   | 89.2 ms                                                | 78.7 ms: 1.13x faster                                      |
| xml_etree_iterparse  | 107 ms                                                 | 96.0 ms: 1.11x faster                                      |
| xml_etree_process    | 61.7 ms                                                | 55.6 ms: 1.11x faster                                      |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                      |
| json_dumps           | 10.4 ms                                                | 11.7 ms: 1.13x slower                                      |
| Geometric mean       | (ref)                                                  | 1.08x faster                                               |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                      |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                      |
| Geometric mean         | (ref)                                                  | 1.17x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.5 ms: 1.14x faster                                      |
| django_template | 34.6 ms                                                | 31.5 ms: 1.10x faster                                      |
| Geometric mean  | (ref)                                                  | 1.12x faster                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 619 ms: 1.91x faster                                       |
| async_tree_io              | 1.16 sec                                               | 623 ms: 1.86x faster                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 321 ms: 1.79x faster                                       |
| async_tree_memoization     | 578 ms                                                 | 328 ms: 1.76x faster                                       |
| async_tree_none            | 472 ms                                                 | 269 ms: 1.75x faster                                       |
| async_tree_none_tg         | 450 ms                                                 | 262 ms: 1.72x faster                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 493 ms: 1.47x faster                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 503 ms: 1.44x faster                                       |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                       |
| deepcopy_memo              | 40.7 us                                                | 30.5 us: 1.34x faster                                      |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.27x faster                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                      |
| tomli_loads                | 2.33 sec                                               | 1.86 sec: 1.25x faster                                     |
| float                      | 84.7 ms                                                | 69.1 ms: 1.23x faster                                      |
| scimark_fft                | 382 ms                                                 | 317 ms: 1.21x faster                                       |
| regex_compile              | 148 ms                                                 | 125 ms: 1.19x faster                                       |
| logging_format             | 7.23 us                                                | 6.08 us: 1.19x faster                                      |
| spectral_norm              | 115 ms                                                 | 96.7 ms: 1.19x faster                                      |
| crypto_pyaes               | 81.9 ms                                                | 69.5 ms: 1.18x faster                                      |
| logging_simple             | 6.46 us                                                | 5.50 us: 1.17x faster                                      |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.34 ms: 1.16x faster                                      |
| unpickle_pure_python       | 230 us                                                 | 199 us: 1.16x faster                                       |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.14x faster                                       |
| chaos                      | 67.0 ms                                                | 58.7 ms: 1.14x faster                                      |
| mako                       | 11.9 ms                                                | 10.5 ms: 1.14x faster                                      |
| async_generators           | 463 ms                                                 | 408 ms: 1.14x faster                                       |
| xml_etree_generate         | 89.2 ms                                                | 78.7 ms: 1.13x faster                                      |
| regex_effbot               | 3.61 ms                                                | 3.20 ms: 1.13x faster                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 66.7 ms: 1.13x faster                                      |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                       |
| raytrace                   | 312 ms                                                 | 279 ms: 1.12x faster                                       |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                      |
| xml_etree_iterparse        | 107 ms                                                 | 96.0 ms: 1.11x faster                                      |
| xml_etree_process          | 61.7 ms                                                | 55.6 ms: 1.11x faster                                      |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.11x faster                                       |
| deltablue                  | 3.72 ms                                                | 3.38 ms: 1.10x faster                                      |
| django_template            | 34.6 ms                                                | 31.5 ms: 1.10x faster                                      |
| pyflate                    | 482 ms                                                 | 441 ms: 1.09x faster                                       |
| sympy_str                  | 300 ms                                                 | 275 ms: 1.09x faster                                       |
| generators                 | 31.2 ms                                                | 28.9 ms: 1.08x faster                                      |
| go                         | 139 ms                                                 | 129 ms: 1.08x faster                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                      |
| 2to3                       | 274 ms                                                 | 257 ms: 1.07x faster                                       |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.06x faster                                      |
| pycparser                  | 1.18 sec                                               | 1.11 sec: 1.06x faster                                     |
| sympy_integrate            | 21.4 ms                                                | 20.2 ms: 1.06x faster                                      |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                       |
| fannkuch                   | 417 ms                                                 | 395 ms: 1.06x faster                                       |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                       |
| docutils                   | 2.77 sec                                               | 2.66 sec: 1.04x faster                                     |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                     |
| sqlite_synth               | 2.83 us                                                | 2.74 us: 1.04x faster                                      |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                       |
| dulwich_log                | 68.5 ms                                                | 66.4 ms: 1.03x faster                                      |
| regex_dna                  | 212 ms                                                 | 206 ms: 1.03x faster                                       |
| json                       | 5.26 ms                                                | 5.13 ms: 1.02x faster                                      |
| sqlglot_optimize           | 54.8 ms                                                | 53.7 ms: 1.02x faster                                      |
| sympy_expand               | 478 ms                                                 | 469 ms: 1.02x faster                                       |
| richards                   | 45.8 ms                                                | 45.0 ms: 1.02x faster                                      |
| pprint_safe_repr           | 776 ms                                                 | 764 ms: 1.01x faster                                       |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                       |
| pprint_pformat             | 1.57 sec                                               | 1.56 sec: 1.01x faster                                     |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                       |
| nbody                      | 97.0 ms                                                | 97.7 ms: 1.01x slower                                      |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                      |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                      |
| regex_v8                   | 23.1 ms                                                | 23.5 ms: 1.02x slower                                      |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                       |
| bench_thread_pool          | 842 us                                                 | 888 us: 1.06x slower                                       |
| nqueens                    | 83.3 ms                                                | 88.5 ms: 1.06x slower                                      |
| telco                      | 7.10 ms                                                | 7.67 ms: 1.08x slower                                      |
| hexiom                     | 6.41 ms                                                | 6.96 ms: 1.09x slower                                      |
| json_dumps                 | 10.4 ms                                                | 11.7 ms: 1.13x slower                                      |
| gc_traversal               | 3.79 ms                                                | 4.87 ms: 1.28x slower                                      |
| coverage                   | 72.7 ms                                                | 96.8 ms: 1.33x slower                                      |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                      |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                      |
| bench_mp_pool              | 24.0 ms                                                | 81.1 ms: 3.38x slower                                      |
| Geometric mean             | (ref)                                                  | 1.09x faster                                               |

Benchmark hidden because not significant (5): richards_super, scimark_lu, coroutines, pickle_pure_python, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250211-3.14.0a5-3ae9101-JIT/bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.108x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.11x