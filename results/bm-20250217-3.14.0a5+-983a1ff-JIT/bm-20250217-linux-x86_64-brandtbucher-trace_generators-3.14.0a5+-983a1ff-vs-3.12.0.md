# Results vs. 3.12.0

- fork: brandtbucher
- ref: trace_generators
- machine: linux-x86_64
- commit hash: 983a1ff
- commit date: 2025-02-17
- overall geometric mean: 1.106x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-983a1ff |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 265 ms: 1.04x faster                                                     |
| docutils       | 2.77 sec                                               | 2.65 sec: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-983a1ff |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 625 ms: 1.85x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.80x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 326 ms: 1.77x faster                                                     |
| async_tree_none            | 472 ms                                                 | 268 ms: 1.76x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 261 ms: 1.72x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 494 ms: 1.47x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 502 ms: 1.45x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.71x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-983a1ff |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.7 ms: 1.20x faster                                                    |
| nbody          | 97.0 ms                                                | 89.4 ms: 1.08x faster                                                    |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.09x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-983a1ff |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.04 ms: 1.19x faster                                                    |
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                     |
| regex_dna      | 212 ms                                                 | 203 ms: 1.04x faster                                                     |
| regex_v8       | 23.1 ms                                                | 24.1 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                  | 1.09x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-983a1ff |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.86 sec: 1.26x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 205 us: 1.12x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 80.0 ms: 1.11x faster                                                    |
| xml_etree_process    | 61.7 ms                                                | 56.5 ms: 1.09x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 98.3 ms: 1.09x faster                                                    |
| pickle_pure_python   | 324 us                                                 | 321 us: 1.01x faster                                                     |
| json_loads           | 28.5 us                                                | 28.6 us: 1.00x slower                                                    |
| json_dumps           | 10.4 ms                                                | 11.7 ms: 1.13x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-983a1ff |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                    |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-983a1ff |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.3 ms: 1.16x faster                                                    |
| django_template | 34.6 ms                                                | 31.7 ms: 1.09x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-983a1ff |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 625 ms: 1.85x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.80x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 326 ms: 1.77x faster                                                     |
| async_tree_none            | 472 ms                                                 | 268 ms: 1.76x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 261 ms: 1.72x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 494 ms: 1.47x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 502 ms: 1.45x faster                                                     |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                     |
| deepcopy_memo              | 40.7 us                                                | 30.7 us: 1.33x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                | 2.64 us: 1.27x faster                                                    |
| tomli_loads                | 2.33 sec                                               | 1.86 sec: 1.26x faster                                                   |
| comprehensions             | 21.8 us                                                | 17.4 us: 1.25x faster                                                    |
| scimark_fft                | 382 ms                                                 | 313 ms: 1.22x faster                                                     |
| spectral_norm              | 115 ms                                                 | 95.3 ms: 1.21x faster                                                    |
| float                      | 84.7 ms                                                | 70.7 ms: 1.20x faster                                                    |
| regex_effbot               | 3.61 ms                                                | 3.04 ms: 1.19x faster                                                    |
| logging_format             | 7.23 us                                                | 6.10 us: 1.18x faster                                                    |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.18x faster                                                    |
| logging_simple             | 6.46 us                                                | 5.53 us: 1.17x faster                                                    |
| mako                       | 11.9 ms                                                | 10.3 ms: 1.16x faster                                                    |
| crypto_pyaes               | 81.9 ms                                                | 71.3 ms: 1.15x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                     |
| chaos                      | 67.0 ms                                                | 58.9 ms: 1.14x faster                                                    |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                                     |
| async_generators           | 463 ms                                                 | 412 ms: 1.12x faster                                                     |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                     |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 205 us: 1.12x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 67.1 ms: 1.12x faster                                                    |
| pyflate                    | 482 ms                                                 | 432 ms: 1.12x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 80.0 ms: 1.11x faster                                                    |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.55 ms: 1.11x faster                                                    |
| go                         | 139 ms                                                 | 126 ms: 1.11x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.35 ms: 1.11x faster                                                    |
| sympy_str                  | 300 ms                                                 | 274 ms: 1.10x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 56.5 ms: 1.09x faster                                                    |
| django_template            | 34.6 ms                                                | 31.7 ms: 1.09x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 98.3 ms: 1.09x faster                                                    |
| nbody                      | 97.0 ms                                                | 89.4 ms: 1.08x faster                                                    |
| pprint_safe_repr           | 776 ms                                                 | 724 ms: 1.07x faster                                                     |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.07x faster                                                     |
| sympy_integrate            | 21.4 ms                                                | 20.1 ms: 1.07x faster                                                    |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                    |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.05x faster                                                    |
| mdp                        | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.70 us: 1.05x faster                                                    |
| fannkuch                   | 417 ms                                                 | 399 ms: 1.04x faster                                                     |
| docutils                   | 2.77 sec                                               | 2.65 sec: 1.04x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.04x faster                                                   |
| regex_dna                  | 212 ms                                                 | 203 ms: 1.04x faster                                                     |
| richards                   | 45.8 ms                                                | 44.1 ms: 1.04x faster                                                    |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                     |
| 2to3                       | 274 ms                                                 | 265 ms: 1.04x faster                                                     |
| nqueens                    | 83.3 ms                                                | 81.0 ms: 1.03x faster                                                    |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                     |
| richards_super             | 51.5 ms                                                | 50.3 ms: 1.02x faster                                                    |
| json                       | 5.26 ms                                                | 5.14 ms: 1.02x faster                                                    |
| sympy_expand               | 478 ms                                                 | 468 ms: 1.02x faster                                                     |
| sqlglot_optimize           | 54.8 ms                                                | 53.7 ms: 1.02x faster                                                    |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 67.8 ms: 1.01x faster                                                    |
| pickle_pure_python         | 324 us                                                 | 321 us: 1.01x faster                                                     |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                     |
| json_loads                 | 28.5 us                                                | 28.6 us: 1.00x slower                                                    |
| coroutines                 | 23.2 ms                                                | 23.6 ms: 1.02x slower                                                    |
| python_startup_no_site     | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                    |
| hexiom                     | 6.41 ms                                                | 6.64 ms: 1.04x slower                                                    |
| regex_v8                   | 23.1 ms                                                | 24.1 ms: 1.04x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                     |
| bench_thread_pool          | 842 us                                                 | 885 us: 1.05x slower                                                     |
| telco                      | 7.10 ms                                                | 7.67 ms: 1.08x slower                                                    |
| json_dumps                 | 10.4 ms                                                | 11.7 ms: 1.13x slower                                                    |
| coverage                   | 72.7 ms                                                | 92.1 ms: 1.27x slower                                                    |
| gc_traversal               | 3.79 ms                                                | 4.96 ms: 1.31x slower                                                    |
| generators                 | 31.2 ms                                                | 41.9 ms: 1.34x slower                                                    |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                    |
| create_gc_cycles           | 1.48 ms                                                | 2.49 ms: 1.68x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 81.2 ms: 3.38x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                             |

Benchmark hidden because not significant (3): logging_silent, asyncio_websockets, scimark_lu
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250217-3.14.0a5+-983a1ff-JIT/bm-20250217-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-983a1ff.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.106x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.11x