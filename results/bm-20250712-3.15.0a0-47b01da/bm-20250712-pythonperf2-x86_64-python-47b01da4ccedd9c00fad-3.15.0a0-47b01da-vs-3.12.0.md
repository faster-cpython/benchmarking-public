# Results vs. 3.12.0

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: linux-x86_64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.024x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 281 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 630 ms: 1.65x faster                                                        |
| async_tree_none            | 452 ms                                                       | 273 ms: 1.65x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 638 ms: 1.65x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 332 ms: 1.64x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 333 ms: 1.62x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 272 ms: 1.58x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 505 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.56x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 70.8 ms: 1.08x faster                                                       |
| pidigits       | 265 ms                                                       | 256 ms: 1.03x faster                                                        |
| nbody          | 88.0 ms                                                      | 93.0 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 133 ms: 1.08x faster                                                        |
| regex_dna      | 239 ms                                                       | 229 ms: 1.04x faster                                                        |
| regex_v8       | 23.6 ms                                                      | 23.3 ms: 1.01x faster                                                       |
| regex_effbot   | 3.57 ms                                                      | 3.56 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 2.02 sec: 1.07x faster                                                      |
| xml_etree_iterparse  | 103 ms                                                       | 97.4 ms: 1.06x faster                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 81.9 ms: 1.05x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 139 ms: 1.03x faster                                                        |
| unpickle_pure_python | 210 us                                                       | 206 us: 1.02x faster                                                        |
| xml_etree_process    | 58.4 ms                                                      | 59.3 ms: 1.02x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 333 us: 1.05x slower                                                        |
| json_loads           | 24.4 us                                                      | 25.6 us: 1.05x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 5.02 us: 1.08x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 11.3 ms: 1.10x slower                                                       |
| pickle_dict          | 32.5 us                                                      | 36.6 us: 1.12x slower                                                       |
| pickle_list          | 4.43 us                                                      | 5.03 us: 1.14x slower                                                       |
| pickle               | 10.5 us                                                      | 12.7 us: 1.20x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.83 ms: 1.02x slower                                                       |
| python_startup         | 11.6 ms                                                      | 15.3 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.3 ms: 1.08x faster                                                       |
| mako            | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.00x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.27 sec: 2.02x faster                                                      |
| async_tree_io              | 1.04 sec                                                     | 630 ms: 1.65x faster                                                        |
| async_tree_none            | 452 ms                                                       | 273 ms: 1.65x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 638 ms: 1.65x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 332 ms: 1.64x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 333 ms: 1.62x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 272 ms: 1.58x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 505 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                        |
| comprehensions             | 21.9 us                                                      | 16.4 us: 1.34x faster                                                       |
| deepcopy                   | 368 us                                                       | 276 us: 1.34x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 28.8 us: 1.28x faster                                                       |
| generators                 | 37.4 ms                                                      | 29.5 ms: 1.27x faster                                                       |
| go                         | 150 ms                                                       | 119 ms: 1.26x faster                                                        |
| unpack_sequence            | 53.2 ns                                                      | 45.0 ns: 1.18x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.57 us: 1.14x faster                                                       |
| deepcopy_reduce            | 3.37 us                                                      | 2.97 us: 1.14x faster                                                       |
| logging_simple             | 6.71 us                                                      | 5.94 us: 1.13x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 58.5 ms: 1.12x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 61.8 ms: 1.12x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 17.1 ms: 1.11x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 21.9 ms: 1.09x faster                                                       |
| sympy_sum                  | 162 ms                                                       | 149 ms: 1.09x faster                                                        |
| chaos                      | 64.0 ms                                                      | 59.0 ms: 1.08x faster                                                       |
| float                      | 76.6 ms                                                      | 70.8 ms: 1.08x faster                                                       |
| django_template            | 38.2 ms                                                      | 35.3 ms: 1.08x faster                                                       |
| regex_compile              | 144 ms                                                       | 133 ms: 1.08x faster                                                        |
| meteor_contest             | 128 ms                                                       | 120 ms: 1.07x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.02 sec: 1.07x faster                                                      |
| sympy_str                  | 302 ms                                                       | 284 ms: 1.06x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 86.8 ms: 1.06x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 97.4 ms: 1.06x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 76.1 ms: 1.06x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 81.9 ms: 1.05x faster                                                       |
| raytrace                   | 298 ms                                                       | 284 ms: 1.05x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.58 sec: 1.05x faster                                                      |
| regex_dna                  | 239 ms                                                       | 229 ms: 1.04x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 775 ms: 1.04x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 364 ms: 1.04x faster                                                        |
| scimark_sor                | 109 ms                                                       | 105 ms: 1.04x faster                                                        |
| pidigits                   | 265 ms                                                       | 256 ms: 1.03x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 139 ms: 1.03x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 22.3 ms: 1.03x faster                                                       |
| pyflate                    | 439 ms                                                       | 427 ms: 1.03x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 96.6 ms: 1.02x faster                                                       |
| unpickle_pure_python       | 210 us                                                       | 206 us: 1.02x faster                                                        |
| regex_v8                   | 23.6 ms                                                      | 23.3 ms: 1.01x faster                                                       |
| 2to3                       | 285 ms                                                       | 281 ms: 1.01x faster                                                        |
| asyncio_websockets         | 387 ms                                                       | 382 ms: 1.01x faster                                                        |
| pycparser                  | 1.23 sec                                                     | 1.22 sec: 1.01x faster                                                      |
| deltablue                  | 3.24 ms                                                      | 3.20 ms: 1.01x faster                                                       |
| hexiom                     | 5.96 ms                                                      | 5.91 ms: 1.01x faster                                                       |
| logging_silent             | 94.4 ns                                                      | 94.1 ns: 1.00x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.56 ms: 1.00x faster                                                       |
| sympy_expand               | 484 ms                                                       | 486 ms: 1.00x slower                                                        |
| richards_super             | 51.3 ms                                                      | 51.8 ms: 1.01x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 91.1 ms: 1.01x slower                                                       |
| xml_etree_process          | 58.4 ms                                                      | 59.3 ms: 1.02x slower                                                       |
| python_startup_no_site     | 8.64 ms                                                      | 8.83 ms: 1.02x slower                                                       |
| sqlite_synth               | 2.77 us                                                      | 2.84 us: 1.02x slower                                                       |
| bench_thread_pool          | 950 us                                                       | 974 us: 1.03x slower                                                        |
| fannkuch                   | 350 ms                                                       | 360 ms: 1.03x slower                                                        |
| scimark_fft                | 301 ms                                                       | 311 ms: 1.03x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 333 us: 1.05x slower                                                        |
| json                       | 5.12 ms                                                      | 5.38 ms: 1.05x slower                                                       |
| json_loads                 | 24.4 us                                                      | 25.6 us: 1.05x slower                                                       |
| nbody                      | 88.0 ms                                                      | 93.0 ms: 1.06x slower                                                       |
| unpickle_list              | 4.66 us                                                      | 5.02 us: 1.08x slower                                                       |
| async_generators           | 390 ms                                                       | 422 ms: 1.08x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.8 ms: 1.08x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 11.3 ms: 1.10x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 167 us: 1.10x slower                                                        |
| pickle_dict                | 32.5 us                                                      | 36.6 us: 1.12x slower                                                       |
| pickle_list                | 4.43 us                                                      | 5.03 us: 1.14x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.86 ms: 1.16x slower                                                       |
| pickle                     | 10.5 us                                                      | 12.7 us: 1.20x slower                                                       |
| coverage                   | 66.7 ms                                                      | 84.4 ms: 1.27x slower                                                       |
| python_startup             | 11.6 ms                                                      | 15.3 ms: 1.32x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.93 ms: 1.84x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 6.47 ms: 1.86x slower                                                       |
| telco                      | 6.96 ms                                                      | 161 ms: 23.08x slower                                                       |
| bench_mp_pool              | 4.76 ms                                                      | 1.55 sec: 324.79x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                                |

Benchmark hidden because not significant (4): richards, unpickle, asyncio_tcp_ssl, docutils
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.024x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.13x