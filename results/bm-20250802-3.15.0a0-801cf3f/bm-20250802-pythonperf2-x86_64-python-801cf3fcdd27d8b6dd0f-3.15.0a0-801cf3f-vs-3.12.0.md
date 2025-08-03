# Results vs. 3.12.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: linux-x86_64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.029x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 280 ms: 1.02x faster                                                        |
| docutils       | 2.87 sec                                                     | 2.88 sec: 1.00x slower                                                      |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 628 ms: 1.66x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 328 ms: 1.66x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 640 ms: 1.65x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 331 ms: 1.63x faster                                                        |
| async_tree_none            | 452 ms                                                       | 278 ms: 1.62x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 268 ms: 1.61x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 503 ms: 1.39x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 502 ms: 1.39x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.57x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 67.7 ms: 1.13x faster                                                       |
| pidigits       | 265 ms                                                       | 256 ms: 1.04x faster                                                        |
| nbody          | 88.0 ms                                                      | 92.0 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 131 ms: 1.10x faster                                                        |
| regex_dna      | 239 ms                                                       | 219 ms: 1.09x faster                                                        |
| regex_effbot   | 3.57 ms                                                      | 3.54 ms: 1.01x faster                                                       |
| regex_v8       | 23.6 ms                                                      | 23.9 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 2.02 sec: 1.07x faster                                                      |
| xml_etree_iterparse  | 103 ms                                                       | 96.9 ms: 1.06x faster                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 84.6 ms: 1.02x faster                                                       |
| xml_etree_parse      | 144 ms                                                       | 142 ms: 1.02x faster                                                        |
| unpickle_pure_python | 210 us                                                       | 207 us: 1.01x faster                                                        |
| unpickle             | 14.8 us                                                      | 15.0 us: 1.02x slower                                                       |
| pickle_dict          | 32.5 us                                                      | 33.7 us: 1.03x slower                                                       |
| pickle_pure_python   | 318 us                                                       | 331 us: 1.04x slower                                                        |
| json_loads           | 24.4 us                                                      | 26.4 us: 1.08x slower                                                       |
| json_dumps           | 10.2 ms                                                      | 11.1 ms: 1.08x slower                                                       |
| pickle_list          | 4.43 us                                                      | 4.86 us: 1.10x slower                                                       |
| unpickle_list        | 4.66 us                                                      | 5.16 us: 1.11x slower                                                       |
| pickle               | 10.5 us                                                      | 12.4 us: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.80 ms: 1.02x slower                                                       |
| python_startup         | 11.6 ms                                                      | 15.4 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.2 ms: 1.08x faster                                                       |
| mako            | 10.0 ms                                                      | 10.6 ms: 1.06x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.29 sec: 1.99x faster                                                      |
| async_tree_io              | 1.04 sec                                                     | 628 ms: 1.66x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 328 ms: 1.66x faster                                                        |
| async_tree_io_tg           | 1.05 sec                                                     | 640 ms: 1.65x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 331 ms: 1.63x faster                                                        |
| async_tree_none            | 452 ms                                                       | 278 ms: 1.62x faster                                                        |
| async_tree_none_tg         | 431 ms                                                       | 268 ms: 1.61x faster                                                        |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 503 ms: 1.39x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 502 ms: 1.39x faster                                                        |
| deepcopy                   | 368 us                                                       | 271 us: 1.36x faster                                                        |
| comprehensions             | 21.9 us                                                      | 16.2 us: 1.36x faster                                                       |
| deepcopy_memo              | 36.8 us                                                      | 27.4 us: 1.34x faster                                                       |
| generators                 | 37.4 ms                                                      | 28.2 ms: 1.33x faster                                                       |
| unpack_sequence            | 53.2 ns                                                      | 41.7 ns: 1.28x faster                                                       |
| go                         | 150 ms                                                       | 118 ms: 1.27x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.90 us: 1.16x faster                                                       |
| pathlib                    | 18.9 ms                                                      | 16.6 ms: 1.14x faster                                                       |
| float                      | 76.6 ms                                                      | 67.7 ms: 1.13x faster                                                       |
| logging_format             | 7.48 us                                                      | 6.61 us: 1.13x faster                                                       |
| logging_simple             | 6.71 us                                                      | 5.98 us: 1.12x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 61.6 ms: 1.12x faster                                                       |
| chaos                      | 64.0 ms                                                      | 58.0 ms: 1.10x faster                                                       |
| dulwich_log                | 65.4 ms                                                      | 59.5 ms: 1.10x faster                                                       |
| regex_compile              | 144 ms                                                       | 131 ms: 1.10x faster                                                        |
| regex_dna                  | 239 ms                                                       | 219 ms: 1.09x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 22.0 ms: 1.09x faster                                                       |
| raytrace                   | 298 ms                                                       | 275 ms: 1.09x faster                                                        |
| django_template            | 38.2 ms                                                      | 35.2 ms: 1.08x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.54 sec: 1.08x faster                                                      |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.07x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 85.8 ms: 1.07x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.02 sec: 1.07x faster                                                      |
| meteor_contest             | 128 ms                                                       | 120 ms: 1.07x faster                                                        |
| scimark_sor                | 109 ms                                                       | 102 ms: 1.06x faster                                                        |
| sympy_str                  | 302 ms                                                       | 284 ms: 1.06x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 760 ms: 1.06x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 96.9 ms: 1.06x faster                                                       |
| scimark_lu                 | 98.8 ms                                                      | 93.3 ms: 1.06x faster                                                       |
| crypto_pyaes               | 80.3 ms                                                      | 76.6 ms: 1.05x faster                                                       |
| coroutines                 | 23.0 ms                                                      | 22.1 ms: 1.04x faster                                                       |
| pidigits                   | 265 ms                                                       | 256 ms: 1.04x faster                                                        |
| pyflate                    | 439 ms                                                       | 424 ms: 1.03x faster                                                        |
| deltablue                  | 3.24 ms                                                      | 3.15 ms: 1.03x faster                                                       |
| asyncio_tcp                | 378 ms                                                       | 368 ms: 1.03x faster                                                        |
| richards                   | 45.7 ms                                                      | 44.9 ms: 1.02x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 84.6 ms: 1.02x faster                                                       |
| logging_silent             | 94.4 ns                                                      | 92.7 ns: 1.02x faster                                                       |
| 2to3                       | 285 ms                                                       | 280 ms: 1.02x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 142 ms: 1.02x faster                                                        |
| unpickle_pure_python       | 210 us                                                       | 207 us: 1.01x faster                                                        |
| richards_super             | 51.3 ms                                                      | 50.8 ms: 1.01x faster                                                       |
| regex_effbot               | 3.57 ms                                                      | 3.54 ms: 1.01x faster                                                       |
| docutils                   | 2.87 sec                                                     | 2.88 sec: 1.00x slower                                                      |
| hexiom                     | 5.96 ms                                                      | 6.01 ms: 1.01x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 23.9 ms: 1.01x slower                                                       |
| unpickle                   | 14.8 us                                                      | 15.0 us: 1.02x slower                                                       |
| scimark_fft                | 301 ms                                                       | 306 ms: 1.02x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                                      |
| python_startup_no_site     | 8.64 ms                                                      | 8.80 ms: 1.02x slower                                                       |
| nqueens                    | 89.9 ms                                                      | 91.9 ms: 1.02x slower                                                       |
| bench_thread_pool          | 950 us                                                       | 973 us: 1.03x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.85 us: 1.03x slower                                                       |
| pickle_dict                | 32.5 us                                                      | 33.7 us: 1.03x slower                                                       |
| pickle_pure_python         | 318 us                                                       | 331 us: 1.04x slower                                                        |
| nbody                      | 88.0 ms                                                      | 92.0 ms: 1.05x slower                                                       |
| json                       | 5.12 ms                                                      | 5.37 ms: 1.05x slower                                                       |
| mako                       | 10.0 ms                                                      | 10.6 ms: 1.06x slower                                                       |
| fannkuch                   | 350 ms                                                       | 375 ms: 1.07x slower                                                        |
| async_generators           | 390 ms                                                       | 422 ms: 1.08x slower                                                        |
| json_loads                 | 24.4 us                                                      | 26.4 us: 1.08x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 11.1 ms: 1.08x slower                                                       |
| typing_runtime_protocols   | 152 us                                                       | 165 us: 1.09x slower                                                        |
| pickle_list                | 4.43 us                                                      | 4.86 us: 1.10x slower                                                       |
| unpickle_list              | 4.66 us                                                      | 5.16 us: 1.11x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.70 ms: 1.12x slower                                                       |
| pickle                     | 10.5 us                                                      | 12.4 us: 1.18x slower                                                       |
| coverage                   | 66.7 ms                                                      | 82.0 ms: 1.23x slower                                                       |
| python_startup             | 11.6 ms                                                      | 15.4 ms: 1.32x slower                                                       |
| create_gc_cycles           | 1.59 ms                                                      | 2.93 ms: 1.84x slower                                                       |
| gc_traversal               | 3.48 ms                                                      | 6.67 ms: 1.92x slower                                                       |
| telco                      | 6.96 ms                                                      | 161 ms: 23.10x slower                                                       |
| bench_mp_pool              | 4.76 ms                                                      | 1.37 sec: 288.04x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (4): asyncio_tcp_ssl, sympy_expand, asyncio_websockets, xml_etree_process
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf2-x86_64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.029x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.13x