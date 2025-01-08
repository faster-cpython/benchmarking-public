# Results vs. 3.12.0

- fork: brandtbucher
- ref: nojit
- machine: linux-x86_64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.108x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.08x faster                                          |
| docutils       | 2.77 sec                                               | 2.60 sec: 1.06x faster                                        |
| Geometric mean | (ref)                                                  | 1.07x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 586 ms: 2.02x faster                                          |
| async_tree_io              | 1.16 sec                                               | 600 ms: 1.93x faster                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 305 ms: 1.88x faster                                          |
| async_tree_none            | 472 ms                                                 | 256 ms: 1.84x faster                                          |
| async_tree_none_tg         | 450 ms                                                 | 245 ms: 1.84x faster                                          |
| async_tree_memoization     | 578 ms                                                 | 325 ms: 1.78x faster                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 468 ms: 1.55x faster                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 491 ms: 1.48x faster                                          |
| Geometric mean             | (ref)                                                  | 1.78x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 84.7 ms                                                | 72.5 ms: 1.17x faster                                         |
| nbody          | 97.0 ms                                                | 93.1 ms: 1.04x faster                                         |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                          |
| Geometric mean | (ref)                                                  | 1.07x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.17x faster                                          |
| regex_effbot   | 3.61 ms                                                | 3.43 ms: 1.05x faster                                         |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                          |
| regex_v8       | 23.1 ms                                                | 25.5 ms: 1.10x slower                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                        |
| xml_etree_parse      | 159 ms                                                 | 138 ms: 1.15x faster                                          |
| xml_etree_iterparse  | 107 ms                                                 | 97.4 ms: 1.10x faster                                         |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.06x faster                                          |
| json_loads           | 28.5 us                                                | 27.0 us: 1.06x faster                                         |
| xml_etree_generate   | 89.2 ms                                                | 84.8 ms: 1.05x faster                                         |
| xml_etree_process    | 61.7 ms                                                | 59.1 ms: 1.05x faster                                         |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.01x faster                                          |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.09x slower                                         |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                         |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                         |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.9 ms: 1.09x faster                                         |
| mako            | 11.9 ms                                                | 11.5 ms: 1.03x faster                                         |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 586 ms: 2.02x faster                                          |
| async_tree_io              | 1.16 sec                                               | 600 ms: 1.93x faster                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 305 ms: 1.88x faster                                          |
| async_tree_none            | 472 ms                                                 | 256 ms: 1.84x faster                                          |
| async_tree_none_tg         | 450 ms                                                 | 245 ms: 1.84x faster                                          |
| async_tree_memoization     | 578 ms                                                 | 325 ms: 1.78x faster                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 468 ms: 1.55x faster                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 491 ms: 1.48x faster                                          |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                          |
| deepcopy_memo              | 40.7 us                                                | 30.5 us: 1.34x faster                                         |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.29x faster                                         |
| deepcopy_reduce            | 3.35 us                                                | 2.65 us: 1.26x faster                                         |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                         |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                        |
| go                         | 139 ms                                                 | 118 ms: 1.19x faster                                          |
| regex_compile              | 148 ms                                                 | 126 ms: 1.17x faster                                          |
| logging_format             | 7.23 us                                                | 6.19 us: 1.17x faster                                         |
| float                      | 84.7 ms                                                | 72.5 ms: 1.17x faster                                         |
| logging_simple             | 6.46 us                                                | 5.58 us: 1.16x faster                                         |
| xml_etree_parse            | 159 ms                                                 | 138 ms: 1.15x faster                                          |
| deltablue                  | 3.72 ms                                                | 3.26 ms: 1.14x faster                                         |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                          |
| crypto_pyaes               | 81.9 ms                                                | 72.2 ms: 1.13x faster                                         |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                          |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                          |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.6 ms: 1.12x faster                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 66.9 ms: 1.12x faster                                         |
| generators                 | 31.2 ms                                                | 27.9 ms: 1.12x faster                                         |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.11x faster                                          |
| scimark_fft                | 382 ms                                                 | 344 ms: 1.11x faster                                          |
| chaos                      | 67.0 ms                                                | 60.6 ms: 1.11x faster                                         |
| async_generators           | 463 ms                                                 | 421 ms: 1.10x faster                                          |
| xml_etree_iterparse        | 107 ms                                                 | 97.4 ms: 1.10x faster                                         |
| pprint_safe_repr           | 776 ms                                                 | 710 ms: 1.09x faster                                          |
| pyflate                    | 482 ms                                                 | 443 ms: 1.09x faster                                          |
| django_template            | 34.6 ms                                                | 31.9 ms: 1.09x faster                                         |
| 2to3                       | 274 ms                                                 | 255 ms: 1.08x faster                                          |
| spectral_norm              | 115 ms                                                 | 107 ms: 1.08x faster                                          |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.07x faster                                         |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.07x faster                                        |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                         |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.07x faster                                         |
| json                       | 5.26 ms                                                | 4.94 ms: 1.06x faster                                         |
| docutils                   | 2.77 sec                                               | 2.60 sec: 1.06x faster                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.77 ms: 1.06x faster                                         |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                          |
| sqlglot_normalize          | 110 ms                                                 | 104 ms: 1.06x faster                                          |
| dulwich_log                | 68.5 ms                                                | 64.8 ms: 1.06x faster                                         |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.06x faster                                          |
| json_loads                 | 28.5 us                                                | 27.0 us: 1.06x faster                                         |
| xml_etree_generate         | 89.2 ms                                                | 84.8 ms: 1.05x faster                                         |
| regex_effbot               | 3.61 ms                                                | 3.43 ms: 1.05x faster                                         |
| sympy_expand               | 478 ms                                                 | 455 ms: 1.05x faster                                          |
| nqueens                    | 83.3 ms                                                | 79.3 ms: 1.05x faster                                         |
| scimark_sor                | 129 ms                                                 | 123 ms: 1.05x faster                                          |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.05x faster                                        |
| xml_etree_process          | 61.7 ms                                                | 59.1 ms: 1.05x faster                                         |
| sqlglot_optimize           | 54.8 ms                                                | 52.5 ms: 1.04x faster                                         |
| nbody                      | 97.0 ms                                                | 93.1 ms: 1.04x faster                                         |
| fannkuch                   | 417 ms                                                 | 403 ms: 1.03x faster                                          |
| mako                       | 11.9 ms                                                | 11.5 ms: 1.03x faster                                         |
| richards                   | 45.8 ms                                                | 44.4 ms: 1.03x faster                                         |
| hexiom                     | 6.41 ms                                                | 6.27 ms: 1.02x faster                                         |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.01x faster                                          |
| richards_super             | 51.5 ms                                                | 51.0 ms: 1.01x faster                                         |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                          |
| mdp                        | 2.63 sec                                               | 2.62 sec: 1.00x faster                                        |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                          |
| logging_silent             | 104 ns                                                 | 105 ns: 1.01x slower                                          |
| coroutines                 | 23.2 ms                                                | 23.4 ms: 1.01x slower                                         |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                          |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                         |
| typing_runtime_protocols   | 158 us                                                 | 161 us: 1.02x slower                                          |
| bench_thread_pool          | 842 us                                                 | 867 us: 1.03x slower                                          |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.09x slower                                         |
| telco                      | 7.10 ms                                                | 7.77 ms: 1.10x slower                                         |
| regex_v8                   | 23.1 ms                                                | 25.5 ms: 1.10x slower                                         |
| mypy2                      | 830 ms                                                 | 946 ms: 1.14x slower                                          |
| coverage                   | 72.7 ms                                                | 84.3 ms: 1.16x slower                                         |
| gc_traversal               | 3.79 ms                                                | 4.94 ms: 1.30x slower                                         |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                         |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.66x slower                                         |
| bench_mp_pool              | 24.0 ms                                                | 81.9 ms: 3.41x slower                                         |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                  |

Benchmark hidden because not significant (2): sqlite_synth, asyncio_websockets
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250107-3.14.0a3+-f098037/bm-20250107-linux-x86_64-brandtbucher-nojit-3.14.0a3+-f098037.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.108x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.11x