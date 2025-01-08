# Results vs. 3.12.0

- fork: brandtbucher
- ref: nojit
- machine: linux-x86_64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.110x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.05x faster                                          |
| docutils       | 2.77 sec                                               | 2.70 sec: 1.03x faster                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 586 ms: 2.02x faster                                          |
| async_tree_io              | 1.16 sec                                               | 608 ms: 1.90x faster                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 305 ms: 1.88x faster                                          |
| async_tree_none_tg         | 450 ms                                                 | 245 ms: 1.83x faster                                          |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                          |
| async_tree_memoization     | 578 ms                                                 | 326 ms: 1.77x faster                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 468 ms: 1.55x faster                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                          |
| Geometric mean             | (ref)                                                  | 1.77x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 84.7 ms                                                | 68.1 ms: 1.24x faster                                         |
| nbody          | 97.0 ms                                                | 85.0 ms: 1.14x faster                                         |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                  | 1.12x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                          |
| regex_effbot   | 3.61 ms                                                | 3.41 ms: 1.06x faster                                         |
| regex_dna      | 212 ms                                                 | 214 ms: 1.01x slower                                          |
| regex_v8       | 23.1 ms                                                | 24.9 ms: 1.08x slower                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.85 sec: 1.26x faster                                        |
| unpickle_pure_python | 230 us                                                 | 193 us: 1.19x faster                                          |
| xml_etree_parse      | 159 ms                                                 | 137 ms: 1.16x faster                                          |
| xml_etree_generate   | 89.2 ms                                                | 77.8 ms: 1.15x faster                                         |
| xml_etree_iterparse  | 107 ms                                                 | 94.8 ms: 1.13x faster                                         |
| xml_etree_process    | 61.7 ms                                                | 54.9 ms: 1.12x faster                                         |
| json_loads           | 28.5 us                                                | 27.1 us: 1.05x faster                                         |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                         |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                  |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                         |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                         |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.1 ms: 1.17x faster                                         |
| django_template | 34.6 ms                                                | 32.8 ms: 1.05x faster                                         |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 586 ms: 2.02x faster                                          |
| async_tree_io              | 1.16 sec                                               | 608 ms: 1.90x faster                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 305 ms: 1.88x faster                                          |
| async_tree_none_tg         | 450 ms                                                 | 245 ms: 1.83x faster                                          |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                          |
| async_tree_memoization     | 578 ms                                                 | 326 ms: 1.77x faster                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 468 ms: 1.55x faster                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                          |
| deepcopy_memo              | 40.7 us                                                | 27.8 us: 1.46x faster                                         |
| deepcopy                   | 371 us                                                 | 265 us: 1.40x faster                                          |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                         |
| tomli_loads                | 2.33 sec                                               | 1.85 sec: 1.26x faster                                        |
| float                      | 84.7 ms                                                | 68.1 ms: 1.24x faster                                         |
| scimark_fft                | 382 ms                                                 | 308 ms: 1.24x faster                                          |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.23x faster                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 61.8 ms: 1.22x faster                                         |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                         |
| crypto_pyaes               | 81.9 ms                                                | 68.3 ms: 1.20x faster                                         |
| unpickle_pure_python       | 230 us                                                 | 193 us: 1.19x faster                                          |
| mako                       | 11.9 ms                                                | 10.1 ms: 1.17x faster                                         |
| xml_etree_parse            | 159 ms                                                 | 137 ms: 1.16x faster                                          |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                          |
| xml_etree_generate         | 89.2 ms                                                | 77.8 ms: 1.15x faster                                         |
| nbody                      | 97.0 ms                                                | 85.0 ms: 1.14x faster                                         |
| logging_format             | 7.23 us                                                | 6.38 us: 1.13x faster                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.46 ms: 1.13x faster                                         |
| scimark_sor                | 129 ms                                                 | 115 ms: 1.13x faster                                          |
| xml_etree_iterparse        | 107 ms                                                 | 94.8 ms: 1.13x faster                                         |
| xml_etree_process          | 61.7 ms                                                | 54.9 ms: 1.12x faster                                         |
| go                         | 139 ms                                                 | 124 ms: 1.12x faster                                          |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.11x faster                                          |
| raytrace                   | 312 ms                                                 | 282 ms: 1.11x faster                                          |
| logging_simple             | 6.46 us                                                | 5.83 us: 1.11x faster                                         |
| chaos                      | 67.0 ms                                                | 60.6 ms: 1.11x faster                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.0 ms: 1.10x faster                                         |
| fannkuch                   | 417 ms                                                 | 379 ms: 1.10x faster                                          |
| spectral_norm              | 115 ms                                                 | 105 ms: 1.10x faster                                          |
| pprint_safe_repr           | 776 ms                                                 | 709 ms: 1.09x faster                                          |
| sympy_sum                  | 169 ms                                                 | 156 ms: 1.08x faster                                          |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.08x faster                                         |
| pyflate                    | 482 ms                                                 | 449 ms: 1.07x faster                                          |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.06x faster                                         |
| richards                   | 45.8 ms                                                | 43.1 ms: 1.06x faster                                         |
| deltablue                  | 3.72 ms                                                | 3.50 ms: 1.06x faster                                         |
| sympy_str                  | 300 ms                                                 | 282 ms: 1.06x faster                                          |
| regex_effbot               | 3.61 ms                                                | 3.41 ms: 1.06x faster                                         |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.06x faster                                        |
| 2to3                       | 274 ms                                                 | 260 ms: 1.05x faster                                          |
| django_template            | 34.6 ms                                                | 32.8 ms: 1.05x faster                                         |
| json_loads                 | 28.5 us                                                | 27.1 us: 1.05x faster                                         |
| scimark_lu                 | 118 ms                                                 | 112 ms: 1.05x faster                                          |
| json                       | 5.26 ms                                                | 5.03 ms: 1.05x faster                                         |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                          |
| sympy_integrate            | 21.4 ms                                                | 20.6 ms: 1.04x faster                                         |
| richards_super             | 51.5 ms                                                | 49.7 ms: 1.04x faster                                         |
| async_generators           | 463 ms                                                 | 447 ms: 1.04x faster                                          |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.03x faster                                        |
| sqlite_synth               | 2.83 us                                                | 2.76 us: 1.03x faster                                         |
| dulwich_log                | 68.5 ms                                                | 66.8 ms: 1.03x faster                                         |
| docutils                   | 2.77 sec                                               | 2.70 sec: 1.03x faster                                        |
| mdp                        | 2.63 sec                                               | 2.57 sec: 1.02x faster                                        |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                          |
| sqlglot_optimize           | 54.8 ms                                                | 54.2 ms: 1.01x faster                                         |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                          |
| regex_dna                  | 212 ms                                                 | 214 ms: 1.01x slower                                          |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                          |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                         |
| coroutines                 | 23.2 ms                                                | 23.9 ms: 1.03x slower                                         |
| logging_silent             | 104 ns                                                 | 108 ns: 1.03x slower                                          |
| nqueens                    | 83.3 ms                                                | 87.4 ms: 1.05x slower                                         |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                          |
| bench_thread_pool          | 842 us                                                 | 891 us: 1.06x slower                                          |
| telco                      | 7.10 ms                                                | 7.54 ms: 1.06x slower                                         |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                         |
| regex_v8                   | 23.1 ms                                                | 24.9 ms: 1.08x slower                                         |
| hexiom                     | 6.41 ms                                                | 7.24 ms: 1.13x slower                                         |
| mypy2                      | 830 ms                                                 | 959 ms: 1.15x slower                                          |
| coverage                   | 72.7 ms                                                | 85.1 ms: 1.17x slower                                         |
| generators                 | 31.2 ms                                                | 36.7 ms: 1.18x slower                                         |
| gc_traversal               | 3.79 ms                                                | 4.79 ms: 1.26x slower                                         |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                         |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                         |
| bench_mp_pool              | 24.0 ms                                                | 81.5 ms: 3.39x slower                                         |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                  |

Benchmark hidden because not significant (2): sympy_expand, pickle_pure_python
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250107-3.14.0a3+-f098037-JIT/bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.110x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.12x