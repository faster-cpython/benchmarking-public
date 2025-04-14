# Results vs. 3.12.0

- fork: brandtbucher
- ref: trace_generators
- machine: linux-x86_64
- commit hash: d740bda
- commit date: 2025-02-13
- overall geometric mean: 1.110x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d740bda |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 262 ms: 1.05x faster                                                     |
| docutils       | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d740bda |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 620 ms: 1.91x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 624 ms: 1.85x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 325 ms: 1.78x faster                                                     |
| async_tree_none            | 472 ms                                                 | 269 ms: 1.76x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 258 ms: 1.74x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 489 ms: 1.49x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d740bda |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.4 ms: 1.22x faster                                                    |
| nbody          | 97.0 ms                                                | 90.6 ms: 1.07x faster                                                    |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.10x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d740bda |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                     |
| regex_effbot   | 3.61 ms                                                | 3.09 ms: 1.17x faster                                                    |
| regex_dna      | 212 ms                                                 | 210 ms: 1.01x faster                                                     |
| regex_v8       | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                  | 1.08x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d740bda |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.86 sec: 1.26x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 137 ms: 1.16x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 78.7 ms: 1.13x faster                                                    |
| unpickle_pure_python | 230 us                                                 | 207 us: 1.11x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 96.9 ms: 1.10x faster                                                    |
| xml_etree_process    | 61.7 ms                                                | 56.1 ms: 1.10x faster                                                    |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                                    |
| json_dumps           | 10.4 ms                                                | 11.8 ms: 1.14x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                             |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d740bda |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                    |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d740bda |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.2 ms: 1.17x faster                                                    |
| django_template | 34.6 ms                                                | 31.7 ms: 1.09x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250213-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d740bda |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 620 ms: 1.91x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 624 ms: 1.85x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 325 ms: 1.78x faster                                                     |
| async_tree_none            | 472 ms                                                 | 269 ms: 1.76x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 258 ms: 1.74x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 489 ms: 1.49x faster                                                     |
| deepcopy                   | 371 us                                                 | 262 us: 1.42x faster                                                     |
| deepcopy_memo              | 40.7 us                                                | 30.5 us: 1.33x faster                                                    |
| tomli_loads                | 2.33 sec                                               | 1.86 sec: 1.26x faster                                                   |
| comprehensions             | 21.8 us                                                | 17.4 us: 1.25x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                                    |
| scimark_fft                | 382 ms                                                 | 312 ms: 1.22x faster                                                     |
| float                      | 84.7 ms                                                | 69.4 ms: 1.22x faster                                                    |
| logging_format             | 7.23 us                                                | 6.08 us: 1.19x faster                                                    |
| spectral_norm              | 115 ms                                                 | 96.7 ms: 1.19x faster                                                    |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.47 us: 1.18x faster                                                    |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.18x faster                                                    |
| mako                       | 11.9 ms                                                | 10.2 ms: 1.17x faster                                                    |
| regex_effbot               | 3.61 ms                                                | 3.09 ms: 1.17x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 137 ms: 1.16x faster                                                     |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 71.8 ms: 1.14x faster                                                    |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                                     |
| chaos                      | 67.0 ms                                                | 59.0 ms: 1.13x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 78.7 ms: 1.13x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.49 ms: 1.13x faster                                                    |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 67.4 ms: 1.11x faster                                                    |
| go                         | 139 ms                                                 | 125 ms: 1.11x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 207 us: 1.11x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.34 ms: 1.11x faster                                                    |
| async_generators           | 463 ms                                                 | 416 ms: 1.11x faster                                                     |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 96.9 ms: 1.10x faster                                                    |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 56.1 ms: 1.10x faster                                                    |
| django_template            | 34.6 ms                                                | 31.7 ms: 1.09x faster                                                    |
| pyflate                    | 482 ms                                                 | 444 ms: 1.09x faster                                                     |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                                     |
| nbody                      | 97.0 ms                                                | 90.6 ms: 1.07x faster                                                    |
| sympy_integrate            | 21.4 ms                                                | 20.1 ms: 1.07x faster                                                    |
| mdp                        | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.05x faster                                                    |
| pprint_safe_repr           | 776 ms                                                 | 740 ms: 1.05x faster                                                     |
| sqlglot_transpile          | 1.68 ms                                                | 1.61 ms: 1.05x faster                                                    |
| 2to3                       | 274 ms                                                 | 262 ms: 1.05x faster                                                     |
| docutils                   | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.72 us: 1.04x faster                                                    |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                     |
| richards                   | 45.8 ms                                                | 44.2 ms: 1.04x faster                                                    |
| nqueens                    | 83.3 ms                                                | 80.4 ms: 1.04x faster                                                    |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                   |
| fannkuch                   | 417 ms                                                 | 404 ms: 1.03x faster                                                     |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                     |
| sympy_expand               | 478 ms                                                 | 466 ms: 1.02x faster                                                     |
| sqlglot_optimize           | 54.8 ms                                                | 53.6 ms: 1.02x faster                                                    |
| json                       | 5.26 ms                                                | 5.15 ms: 1.02x faster                                                    |
| richards_super             | 51.5 ms                                                | 50.7 ms: 1.02x faster                                                    |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 67.8 ms: 1.01x faster                                                    |
| regex_dna                  | 212 ms                                                 | 210 ms: 1.01x faster                                                     |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                     |
| logging_silent             | 104 ns                                                 | 104 ns: 1.00x faster                                                     |
| coroutines                 | 23.2 ms                                                | 23.4 ms: 1.01x slower                                                    |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                                    |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                     |
| hexiom                     | 6.41 ms                                                | 6.64 ms: 1.04x slower                                                    |
| regex_v8                   | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                    |
| bench_thread_pool          | 842 us                                                 | 882 us: 1.05x slower                                                     |
| telco                      | 7.10 ms                                                | 7.79 ms: 1.10x slower                                                    |
| generators                 | 31.2 ms                                                | 34.9 ms: 1.12x slower                                                    |
| json_dumps                 | 10.4 ms                                                | 11.8 ms: 1.14x slower                                                    |
| coverage                   | 72.7 ms                                                | 90.1 ms: 1.24x slower                                                    |
| gc_traversal               | 3.79 ms                                                | 4.96 ms: 1.31x slower                                                    |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                    |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 81.4 ms: 3.39x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                             |

Benchmark hidden because not significant (3): pickle_pure_python, asyncio_websockets, pycparser
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250213-3.14.0a5+-d740bda-JIT/bm-20250213-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d740bda.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.110x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.11x