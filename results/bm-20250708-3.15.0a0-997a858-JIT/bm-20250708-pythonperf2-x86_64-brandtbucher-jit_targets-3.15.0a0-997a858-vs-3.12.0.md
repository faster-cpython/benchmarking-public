# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_targets
- machine: linux-x86_64
- commit hash: 997a858
- commit date: 2025-07-08
- overall geometric mean: 1.030x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 287 ms: 1.01x slower                                                     |
| docutils       | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 631 ms: 1.67x faster                                                     |
| async_tree_io              | 1.04 sec                                                     | 626 ms: 1.67x faster                                                     |
| async_tree_memoization     | 544 ms                                                       | 330 ms: 1.65x faster                                                     |
| async_tree_none            | 452 ms                                                       | 276 ms: 1.64x faster                                                     |
| async_tree_memoization_tg  | 540 ms                                                       | 333 ms: 1.62x faster                                                     |
| async_tree_none_tg         | 431 ms                                                       | 273 ms: 1.58x faster                                                     |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 503 ms: 1.38x faster                                                     |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                     |
| Geometric mean             | (ref)                                                        | 1.57x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 63.6 ms: 1.21x faster                                                    |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                     |
| nbody          | 88.0 ms                                                      | 101 ms: 1.15x slower                                                     |
| Geometric mean | (ref)                                                        | 1.03x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 133 ms: 1.09x faster                                                     |
| regex_dna      | 239 ms                                                       | 227 ms: 1.05x faster                                                     |
| regex_v8       | 23.6 ms                                                      | 23.3 ms: 1.01x faster                                                    |
| regex_effbot   | 3.57 ms                                                      | 3.65 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                        | 1.03x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.93 sec: 1.12x faster                                                   |
| xml_etree_generate   | 86.1 ms                                                      | 79.4 ms: 1.08x faster                                                    |
| unpickle_pure_python | 210 us                                                       | 196 us: 1.07x faster                                                     |
| xml_etree_process    | 58.4 ms                                                      | 55.7 ms: 1.05x faster                                                    |
| xml_etree_iterparse  | 103 ms                                                       | 98.9 ms: 1.04x faster                                                    |
| xml_etree_parse      | 144 ms                                                       | 141 ms: 1.02x faster                                                     |
| json_loads           | 24.4 us                                                      | 25.3 us: 1.04x slower                                                    |
| pickle_pure_python   | 318 us                                                       | 331 us: 1.04x slower                                                     |
| json_dumps           | 10.2 ms                                                      | 11.2 ms: 1.09x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.87 ms: 1.03x slower                                                    |
| python_startup         | 11.6 ms                                                      | 15.4 ms: 1.32x slower                                                    |
| Geometric mean         | (ref)                                                        | 1.17x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.0 ms: 1.09x faster                                                    |
| mako            | 10.0 ms                                                      | 9.94 ms: 1.01x faster                                                    |
| Geometric mean  | (ref)                                                        | 1.05x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.29 sec: 1.99x faster                                                   |
| async_tree_io_tg           | 1.05 sec                                                     | 631 ms: 1.67x faster                                                     |
| async_tree_io              | 1.04 sec                                                     | 626 ms: 1.67x faster                                                     |
| async_tree_memoization     | 544 ms                                                       | 330 ms: 1.65x faster                                                     |
| async_tree_none            | 452 ms                                                       | 276 ms: 1.64x faster                                                     |
| async_tree_memoization_tg  | 540 ms                                                       | 333 ms: 1.62x faster                                                     |
| async_tree_none_tg         | 431 ms                                                       | 273 ms: 1.58x faster                                                     |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 503 ms: 1.38x faster                                                     |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                     |
| richards                   | 45.7 ms                                                      | 34.4 ms: 1.33x faster                                                    |
| deepcopy_memo              | 36.8 us                                                      | 27.9 us: 1.32x faster                                                    |
| deepcopy                   | 368 us                                                       | 279 us: 1.32x faster                                                     |
| comprehensions             | 21.9 us                                                      | 17.3 us: 1.26x faster                                                    |
| richards_super             | 51.3 ms                                                      | 40.8 ms: 1.26x faster                                                    |
| generators                 | 37.4 ms                                                      | 29.7 ms: 1.26x faster                                                    |
| float                      | 76.6 ms                                                      | 63.6 ms: 1.21x faster                                                    |
| go                         | 150 ms                                                       | 128 ms: 1.17x faster                                                     |
| deepcopy_reduce            | 3.37 us                                                      | 3.00 us: 1.12x faster                                                    |
| deltablue                  | 3.24 ms                                                      | 2.89 ms: 1.12x faster                                                    |
| tomli_loads                | 2.16 sec                                                     | 1.93 sec: 1.12x faster                                                   |
| dulwich_log                | 65.4 ms                                                      | 58.6 ms: 1.12x faster                                                    |
| pathlib                    | 18.9 ms                                                      | 17.1 ms: 1.10x faster                                                    |
| spectral_norm              | 91.6 ms                                                      | 83.0 ms: 1.10x faster                                                    |
| django_template            | 38.2 ms                                                      | 35.0 ms: 1.09x faster                                                    |
| regex_compile              | 144 ms                                                       | 133 ms: 1.09x faster                                                     |
| logging_format             | 7.48 us                                                      | 6.89 us: 1.09x faster                                                    |
| xml_etree_generate         | 86.1 ms                                                      | 79.4 ms: 1.08x faster                                                    |
| scimark_monte_carlo        | 69.0 ms                                                      | 63.7 ms: 1.08x faster                                                    |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.07x faster                                                     |
| pprint_pformat             | 1.65 sec                                                     | 1.54 sec: 1.07x faster                                                   |
| logging_simple             | 6.71 us                                                      | 6.24 us: 1.07x faster                                                    |
| unpickle_pure_python       | 210 us                                                       | 196 us: 1.07x faster                                                     |
| sympy_integrate            | 23.9 ms                                                      | 22.4 ms: 1.07x faster                                                    |
| scimark_sor                | 109 ms                                                       | 102 ms: 1.07x faster                                                     |
| chaos                      | 64.0 ms                                                      | 60.1 ms: 1.07x faster                                                    |
| pprint_safe_repr           | 807 ms                                                       | 766 ms: 1.05x faster                                                     |
| regex_dna                  | 239 ms                                                       | 227 ms: 1.05x faster                                                     |
| xml_etree_process          | 58.4 ms                                                      | 55.7 ms: 1.05x faster                                                    |
| xml_etree_iterparse        | 103 ms                                                       | 98.9 ms: 1.04x faster                                                    |
| meteor_contest             | 128 ms                                                       | 123 ms: 1.04x faster                                                     |
| crypto_pyaes               | 80.3 ms                                                      | 77.3 ms: 1.04x faster                                                    |
| sympy_str                  | 302 ms                                                       | 291 ms: 1.04x faster                                                     |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                     |
| coroutines                 | 23.0 ms                                                      | 22.2 ms: 1.03x faster                                                    |
| raytrace                   | 298 ms                                                       | 289 ms: 1.03x faster                                                     |
| pyflate                    | 439 ms                                                       | 427 ms: 1.03x faster                                                     |
| scimark_lu                 | 98.8 ms                                                      | 96.2 ms: 1.03x faster                                                    |
| xml_etree_parse            | 144 ms                                                       | 141 ms: 1.02x faster                                                     |
| regex_v8                   | 23.6 ms                                                      | 23.3 ms: 1.01x faster                                                    |
| logging_silent             | 94.4 ns                                                      | 93.4 ns: 1.01x faster                                                    |
| mako                       | 10.0 ms                                                      | 9.94 ms: 1.01x faster                                                    |
| 2to3                       | 285 ms                                                       | 287 ms: 1.01x slower                                                     |
| docutils                   | 2.87 sec                                                     | 2.90 sec: 1.01x slower                                                   |
| regex_effbot               | 3.57 ms                                                      | 3.65 ms: 1.02x slower                                                    |
| python_startup_no_site     | 8.64 ms                                                      | 8.87 ms: 1.03x slower                                                    |
| sqlite_synth               | 2.77 us                                                      | 2.86 us: 1.03x slower                                                    |
| hexiom                     | 5.96 ms                                                      | 6.17 ms: 1.04x slower                                                    |
| nqueens                    | 89.9 ms                                                      | 93.2 ms: 1.04x slower                                                    |
| sympy_expand               | 484 ms                                                       | 502 ms: 1.04x slower                                                     |
| scimark_fft                | 301 ms                                                       | 313 ms: 1.04x slower                                                     |
| json_loads                 | 24.4 us                                                      | 25.3 us: 1.04x slower                                                    |
| pickle_pure_python         | 318 us                                                       | 331 us: 1.04x slower                                                     |
| json                       | 5.12 ms                                                      | 5.37 ms: 1.05x slower                                                    |
| json_dumps                 | 10.2 ms                                                      | 11.2 ms: 1.09x slower                                                    |
| fannkuch                   | 350 ms                                                       | 384 ms: 1.10x slower                                                     |
| typing_runtime_protocols   | 152 us                                                       | 170 us: 1.12x slower                                                     |
| async_generators           | 390 ms                                                       | 445 ms: 1.14x slower                                                     |
| nbody                      | 88.0 ms                                                      | 101 ms: 1.15x slower                                                     |
| coverage                   | 66.7 ms                                                      | 77.9 ms: 1.17x slower                                                    |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.18 ms: 1.23x slower                                                    |
| python_startup             | 11.6 ms                                                      | 15.4 ms: 1.32x slower                                                    |
| create_gc_cycles           | 1.59 ms                                                      | 2.90 ms: 1.82x slower                                                    |
| gc_traversal               | 3.48 ms                                                      | 6.49 ms: 1.87x slower                                                    |
| telco                      | 6.96 ms                                                      | 161 ms: 23.10x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                             |

Benchmark hidden because not significant (2): pycparser, asyncio_websockets
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250708-3.15.0a0-997a858-JIT/bm-20250708-pythonperf2-x86_64-brandtbucher-jit_targets-3.15.0a0-997a858.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.030x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.14x