# Results vs. 3.12.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-x86_64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.029x faster
- HPT reliability: 73.35%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 290 ms: 1.02x slower                                                         |
| docutils       | 2.87 sec                                                     | 2.95 sec: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 651 ms: 1.62x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 650 ms: 1.60x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 339 ms: 1.59x faster                                                         |
| async_tree_none            | 452 ms                                                       | 289 ms: 1.56x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 352 ms: 1.55x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 280 ms: 1.54x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 522 ms: 1.33x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.52x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 70.1 ms: 1.09x faster                                                        |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| nbody          | 88.0 ms                                                      | 101 ms: 1.15x slower                                                         |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.11 ms: 1.15x faster                                                        |
| regex_compile  | 144 ms                                                       | 137 ms: 1.05x faster                                                         |
| regex_dna      | 239 ms                                                       | 241 ms: 1.01x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 25.0 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 79.3 ms: 1.09x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 95.9 ms: 1.07x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| xml_etree_process    | 58.4 ms                                                      | 55.5 ms: 1.05x faster                                                        |
| unpickle             | 14.8 us                                                      | 14.2 us: 1.05x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.07 sec: 1.04x faster                                                       |
| unpickle_pure_python | 210 us                                                       | 206 us: 1.02x faster                                                         |
| unpickle_list        | 4.66 us                                                      | 4.83 us: 1.04x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 334 us: 1.05x slower                                                         |
| json_loads           | 24.4 us                                                      | 26.6 us: 1.09x slower                                                        |
| pickle_dict          | 32.5 us                                                      | 37.3 us: 1.14x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.8 ms: 1.15x slower                                                        |
| pickle               | 10.5 us                                                      | 12.1 us: 1.15x slower                                                        |
| pickle_list          | 4.43 us                                                      | 5.36 us: 1.21x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.01 ms: 1.04x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 36.1 ms: 1.06x faster                                                        |
| mako            | 10.0 ms                                                      | 9.79 ms: 1.02x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 651 ms: 1.62x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 650 ms: 1.60x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 339 ms: 1.59x faster                                                         |
| async_tree_none            | 452 ms                                                       | 289 ms: 1.56x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 352 ms: 1.55x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 280 ms: 1.54x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 522 ms: 1.33x faster                                                         |
| deepcopy                   | 368 us                                                       | 286 us: 1.29x faster                                                         |
| generators                 | 37.4 ms                                                      | 29.1 ms: 1.29x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 29.4 us: 1.25x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.89 us: 1.17x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.11 ms: 1.15x faster                                                        |
| comprehensions             | 21.9 us                                                      | 19.2 us: 1.14x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 16.7 ms: 1.13x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 61.1 ms: 1.13x faster                                                        |
| logging_format             | 7.48 us                                                      | 6.77 us: 1.10x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 20.8 ms: 1.10x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 146 ms: 1.09x faster                                                         |
| float                      | 76.6 ms                                                      | 70.1 ms: 1.09x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 79.3 ms: 1.09x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 84.8 ms: 1.08x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.23 us: 1.08x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 95.9 ms: 1.07x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| django_template            | 38.2 ms                                                      | 36.1 ms: 1.06x faster                                                        |
| xml_etree_process          | 58.4 ms                                                      | 55.5 ms: 1.05x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 154 ms: 1.05x faster                                                         |
| chaos                      | 64.0 ms                                                      | 61.0 ms: 1.05x faster                                                        |
| regex_compile              | 144 ms                                                       | 137 ms: 1.05x faster                                                         |
| unpickle                   | 14.8 us                                                      | 14.2 us: 1.05x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 94.6 ms: 1.04x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.07 sec: 1.04x faster                                                       |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.0 ms: 1.04x faster                                                        |
| asyncio_tcp                | 378 ms                                                       | 364 ms: 1.04x faster                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 77.5 ms: 1.04x faster                                                        |
| mako                       | 10.0 ms                                                      | 9.79 ms: 1.02x faster                                                        |
| unpickle_pure_python       | 210 us                                                       | 206 us: 1.02x faster                                                         |
| sympy_integrate            | 23.9 ms                                                      | 23.6 ms: 1.01x faster                                                        |
| sympy_str                  | 302 ms                                                       | 298 ms: 1.01x faster                                                         |
| scimark_sor                | 109 ms                                                       | 109 ms: 1.00x slower                                                         |
| go                         | 150 ms                                                       | 151 ms: 1.01x slower                                                         |
| mdp                        | 2.57 sec                                                     | 2.59 sec: 1.01x slower                                                       |
| scimark_fft                | 301 ms                                                       | 304 ms: 1.01x slower                                                         |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.01x slower                                                        |
| regex_dna                  | 239 ms                                                       | 241 ms: 1.01x slower                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.68 sec: 1.01x slower                                                       |
| pprint_safe_repr           | 807 ms                                                       | 819 ms: 1.01x slower                                                         |
| richards_super             | 51.3 ms                                                      | 52.1 ms: 1.01x slower                                                        |
| 2to3                       | 285 ms                                                       | 290 ms: 1.02x slower                                                         |
| asyncio_websockets         | 387 ms                                                       | 394 ms: 1.02x slower                                                         |
| pyflate                    | 439 ms                                                       | 447 ms: 1.02x slower                                                         |
| sqlglot_parse              | 1.38 ms                                                      | 1.40 ms: 1.02x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                                       |
| dulwich_log                | 65.4 ms                                                      | 67.1 ms: 1.03x slower                                                        |
| bench_thread_pool          | 950 us                                                       | 975 us: 1.03x slower                                                         |
| sqlglot_normalize          | 116 ms                                                       | 119 ms: 1.03x slower                                                         |
| docutils                   | 2.87 sec                                                     | 2.95 sec: 1.03x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 97.4 ns: 1.03x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 4.83 us: 1.04x slower                                                        |
| meteor_contest             | 128 ms                                                       | 133 ms: 1.04x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 60.0 ms: 1.04x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.01 ms: 1.04x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 334 us: 1.05x slower                                                         |
| regex_v8                   | 23.6 ms                                                      | 25.0 ms: 1.06x slower                                                        |
| sympy_expand               | 484 ms                                                       | 512 ms: 1.06x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 3.45 ms: 1.07x slower                                                        |
| json                       | 5.12 ms                                                      | 5.48 ms: 1.07x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.59 ms: 1.09x slower                                                        |
| json_loads                 | 24.4 us                                                      | 26.6 us: 1.09x slower                                                        |
| unpack_sequence            | 53.2 ns                                                      | 58.3 ns: 1.10x slower                                                        |
| fannkuch                   | 350 ms                                                       | 387 ms: 1.10x slower                                                         |
| nqueens                    | 89.9 ms                                                      | 99.6 ms: 1.11x slower                                                        |
| async_generators           | 390 ms                                                       | 434 ms: 1.11x slower                                                         |
| pickle_dict                | 32.5 us                                                      | 37.3 us: 1.14x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.82 ms: 1.15x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.8 ms: 1.15x slower                                                        |
| nbody                      | 88.0 ms                                                      | 101 ms: 1.15x slower                                                         |
| pickle                     | 10.5 us                                                      | 12.1 us: 1.15x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 7.05 ms: 1.18x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 180 us: 1.19x slower                                                         |
| pickle_list                | 4.43 us                                                      | 5.36 us: 1.21x slower                                                        |
| coverage                   | 66.7 ms                                                      | 80.8 ms: 1.21x slower                                                        |
| python_startup             | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.67 ms: 1.68x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.29 ms: 1.81x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.23 sec: 259.00x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                 |

Benchmark hidden because not significant (4): raytrace, asyncio_tcp_ssl, sqlite_synth, richards
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-pythonperf2-x86_64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.029x faster

# HPT report

- Reliability score: 73.35% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x