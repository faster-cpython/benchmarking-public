# Results vs. 3.12.0

- fork: faster-cpython
- ref: make_opcode_static
- machine: linux-x86_64
- commit hash: 536ee25
- commit date: 2025-01-31
- overall geometric mean: 1.055x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 279 ms: 1.02x faster                                                                 |
| docutils       | 2.87 sec                                                     | 2.84 sec: 1.01x faster                                                               |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 645 ms: 1.63x faster                                                                 |
| async_tree_memoization_tg  | 540 ms                                                       | 335 ms: 1.61x faster                                                                 |
| async_tree_io              | 1.04 sec                                                     | 652 ms: 1.60x faster                                                                 |
| async_tree_none            | 452 ms                                                       | 288 ms: 1.57x faster                                                                 |
| async_tree_none_tg         | 431 ms                                                       | 276 ms: 1.56x faster                                                                 |
| async_tree_memoization     | 544 ms                                                       | 351 ms: 1.55x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 507 ms: 1.37x faster                                                                 |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 520 ms: 1.34x faster                                                                 |
| Geometric mean             | (ref)                                                        | 1.53x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 69.5 ms: 1.10x faster                                                                |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                                 |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                         |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.13 ms: 1.14x faster                                                                |
| regex_compile  | 144 ms                                                       | 133 ms: 1.08x faster                                                                 |
| regex_dna      | 239 ms                                                       | 230 ms: 1.04x faster                                                                 |
| regex_v8       | 23.6 ms                                                      | 25.2 ms: 1.07x slower                                                                |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 96.3 ms: 1.07x faster                                                                |
| tomli_loads          | 2.16 sec                                                     | 2.04 sec: 1.06x faster                                                               |
| xml_etree_parse      | 144 ms                                                       | 138 ms: 1.04x faster                                                                 |
| unpickle_pure_python | 210 us                                                       | 205 us: 1.02x faster                                                                 |
| xml_etree_generate   | 86.1 ms                                                      | 84.7 ms: 1.02x faster                                                                |
| pickle_pure_python   | 318 us                                                       | 322 us: 1.01x slower                                                                 |
| xml_etree_process    | 58.4 ms                                                      | 59.8 ms: 1.02x slower                                                                |
| json_loads           | 24.4 us                                                      | 26.5 us: 1.09x slower                                                                |
| json_dumps           | 10.2 ms                                                      | 11.6 ms: 1.14x slower                                                                |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.00 ms: 1.04x slower                                                                |
| python_startup         | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                                                |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.1 ms: 1.09x faster                                                                |
| mako            | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                                                |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 645 ms: 1.63x faster                                                                 |
| async_tree_memoization_tg  | 540 ms                                                       | 335 ms: 1.61x faster                                                                 |
| async_tree_io              | 1.04 sec                                                     | 652 ms: 1.60x faster                                                                 |
| async_tree_none            | 452 ms                                                       | 288 ms: 1.57x faster                                                                 |
| async_tree_none_tg         | 431 ms                                                       | 276 ms: 1.56x faster                                                                 |
| async_tree_memoization     | 544 ms                                                       | 351 ms: 1.55x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 507 ms: 1.37x faster                                                                 |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 520 ms: 1.34x faster                                                                 |
| deepcopy                   | 368 us                                                       | 277 us: 1.33x faster                                                                 |
| generators                 | 37.4 ms                                                      | 28.2 ms: 1.33x faster                                                                |
| comprehensions             | 21.9 us                                                      | 16.7 us: 1.31x faster                                                                |
| deepcopy_memo              | 36.8 us                                                      | 29.4 us: 1.25x faster                                                                |
| go                         | 150 ms                                                       | 124 ms: 1.20x faster                                                                 |
| pathlib                    | 18.9 ms                                                      | 15.9 ms: 1.19x faster                                                                |
| deepcopy_reduce            | 3.37 us                                                      | 2.86 us: 1.18x faster                                                                |
| regex_effbot               | 3.57 ms                                                      | 3.13 ms: 1.14x faster                                                                |
| raytrace                   | 298 ms                                                       | 264 ms: 1.13x faster                                                                 |
| spectral_norm              | 91.6 ms                                                      | 81.3 ms: 1.13x faster                                                                |
| sqlalchemy_declarative     | 159 ms                                                       | 141 ms: 1.13x faster                                                                 |
| coroutines                 | 23.0 ms                                                      | 20.8 ms: 1.11x faster                                                                |
| crypto_pyaes               | 80.3 ms                                                      | 72.7 ms: 1.11x faster                                                                |
| float                      | 76.6 ms                                                      | 69.5 ms: 1.10x faster                                                                |
| logging_format             | 7.48 us                                                      | 6.82 us: 1.10x faster                                                                |
| django_template            | 38.2 ms                                                      | 35.1 ms: 1.09x faster                                                                |
| logging_simple             | 6.71 us                                                      | 6.21 us: 1.08x faster                                                                |
| regex_compile              | 144 ms                                                       | 133 ms: 1.08x faster                                                                 |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.08x faster                                                                 |
| chaos                      | 64.0 ms                                                      | 59.8 ms: 1.07x faster                                                                |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.5 ms: 1.07x faster                                                                |
| xml_etree_iterparse        | 103 ms                                                       | 96.3 ms: 1.07x faster                                                                |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.6 ms: 1.06x faster                                                                |
| pprint_pformat             | 1.65 sec                                                     | 1.56 sec: 1.06x faster                                                               |
| pprint_safe_repr           | 807 ms                                                       | 762 ms: 1.06x faster                                                                 |
| tomli_loads                | 2.16 sec                                                     | 2.04 sec: 1.06x faster                                                               |
| sympy_str                  | 302 ms                                                       | 286 ms: 1.06x faster                                                                 |
| mdp                        | 2.57 sec                                                     | 2.46 sec: 1.05x faster                                                               |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                                 |
| sympy_integrate            | 23.9 ms                                                      | 23.0 ms: 1.04x faster                                                                |
| xml_etree_parse            | 144 ms                                                       | 138 ms: 1.04x faster                                                                 |
| nqueens                    | 89.9 ms                                                      | 86.6 ms: 1.04x faster                                                                |
| sqlglot_parse              | 1.38 ms                                                      | 1.33 ms: 1.04x faster                                                                |
| scimark_lu                 | 98.8 ms                                                      | 95.3 ms: 1.04x faster                                                                |
| sqlglot_transpile          | 1.78 ms                                                      | 1.71 ms: 1.04x faster                                                                |
| regex_dna                  | 239 ms                                                       | 230 ms: 1.04x faster                                                                 |
| meteor_contest             | 128 ms                                                       | 124 ms: 1.03x faster                                                                 |
| bench_thread_pool          | 950 us                                                       | 928 us: 1.02x faster                                                                 |
| 2to3                       | 285 ms                                                       | 279 ms: 1.02x faster                                                                 |
| unpickle_pure_python       | 210 us                                                       | 205 us: 1.02x faster                                                                 |
| xml_etree_generate         | 86.1 ms                                                      | 84.7 ms: 1.02x faster                                                                |
| sqlglot_optimize           | 57.5 ms                                                      | 56.8 ms: 1.01x faster                                                                |
| docutils                   | 2.87 sec                                                     | 2.84 sec: 1.01x faster                                                               |
| sqlglot_normalize          | 116 ms                                                       | 115 ms: 1.01x faster                                                                 |
| asyncio_websockets         | 387 ms                                                       | 384 ms: 1.01x faster                                                                 |
| hexiom                     | 5.96 ms                                                      | 5.98 ms: 1.00x slower                                                                |
| sympy_expand               | 484 ms                                                       | 488 ms: 1.01x slower                                                                 |
| pyflate                    | 439 ms                                                       | 442 ms: 1.01x slower                                                                 |
| richards                   | 45.7 ms                                                      | 46.1 ms: 1.01x slower                                                                |
| pickle_pure_python         | 318 us                                                       | 322 us: 1.01x slower                                                                 |
| sqlite_synth               | 2.77 us                                                      | 2.82 us: 1.01x slower                                                                |
| richards_super             | 51.3 ms                                                      | 52.4 ms: 1.02x slower                                                                |
| logging_silent             | 94.4 ns                                                      | 96.4 ns: 1.02x slower                                                                |
| dulwich_log                | 65.4 ms                                                      | 66.9 ms: 1.02x slower                                                                |
| xml_etree_process          | 58.4 ms                                                      | 59.8 ms: 1.02x slower                                                                |
| scimark_fft                | 301 ms                                                       | 309 ms: 1.02x slower                                                                 |
| fannkuch                   | 350 ms                                                       | 362 ms: 1.03x slower                                                                 |
| scimark_sor                | 109 ms                                                       | 113 ms: 1.04x slower                                                                 |
| python_startup_no_site     | 8.64 ms                                                      | 9.00 ms: 1.04x slower                                                                |
| async_generators           | 390 ms                                                       | 411 ms: 1.05x slower                                                                 |
| json                       | 5.12 ms                                                      | 5.45 ms: 1.06x slower                                                                |
| regex_v8                   | 23.6 ms                                                      | 25.2 ms: 1.07x slower                                                                |
| json_loads                 | 24.4 us                                                      | 26.5 us: 1.09x slower                                                                |
| mako                       | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                                                |
| typing_runtime_protocols   | 152 us                                                       | 165 us: 1.09x slower                                                                 |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.67 ms: 1.11x slower                                                                |
| json_dumps                 | 10.2 ms                                                      | 11.6 ms: 1.14x slower                                                                |
| telco                      | 6.96 ms                                                      | 8.07 ms: 1.16x slower                                                                |
| coverage                   | 66.7 ms                                                      | 78.6 ms: 1.18x slower                                                                |
| python_startup             | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                                                |
| create_gc_cycles           | 1.59 ms                                                      | 2.76 ms: 1.74x slower                                                                |
| gc_traversal               | 3.48 ms                                                      | 6.35 ms: 1.83x slower                                                                |
| bench_mp_pool              | 4.76 ms                                                      | 1.04 sec: 218.99x slower                                                             |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                                         |

Benchmark hidden because not significant (3): nbody, deltablue, pycparser
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250131-3.14.0a4+-536ee25/bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.055x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x