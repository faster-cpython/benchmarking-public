# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_warmup_1024
- machine: linux-x86_64
- commit hash: 39791ef
- commit date: 2025-03-04
- overall geometric mean: 1.110x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 262 ms: 1.05x faster                                                    |
| docutils       | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.90x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 608 ms: 1.90x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                    |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 328 ms: 1.76x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 484 ms: 1.50x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.9 ms: 1.21x faster                                                   |
| nbody          | 97.0 ms                                                | 91.4 ms: 1.06x faster                                                   |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                  | 1.09x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                    |
| regex_effbot   | 3.61 ms                                                | 3.46 ms: 1.04x faster                                                   |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                    |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.85 sec: 1.26x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 203 us: 1.13x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 78.9 ms: 1.13x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 55.5 ms: 1.11x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.09x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 100 ms: 1.07x faster                                                    |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.01x faster                                                    |
| json_loads           | 28.5 us                                                | 30.0 us: 1.05x slower                                                   |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.09x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.14 ms: 1.03x slower                                                   |
| python_startup         | 9.55 ms                                                | 13.0 ms: 1.36x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.18x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                   |
| django_template | 34.6 ms                                                | 31.5 ms: 1.10x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.90x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 608 ms: 1.90x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                    |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 328 ms: 1.76x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 484 ms: 1.50x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                    |
| deepcopy                   | 371 us                                                 | 263 us: 1.41x faster                                                    |
| deepcopy_memo              | 40.7 us                                                | 28.8 us: 1.41x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.85 sec: 1.26x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                   |
| scimark_fft                | 382 ms                                                 | 310 ms: 1.23x faster                                                    |
| comprehensions             | 21.8 us                                                | 17.8 us: 1.23x faster                                                   |
| float                      | 84.7 ms                                                | 69.9 ms: 1.21x faster                                                   |
| spectral_norm              | 115 ms                                                 | 96.0 ms: 1.20x faster                                                   |
| mako                       | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                   |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                    |
| logging_format             | 7.23 us                                                | 6.18 us: 1.17x faster                                                   |
| go                         | 139 ms                                                 | 120 ms: 1.17x faster                                                    |
| logging_simple             | 6.46 us                                                | 5.56 us: 1.16x faster                                                   |
| raytrace                   | 312 ms                                                 | 270 ms: 1.16x faster                                                    |
| async_generators           | 463 ms                                                 | 404 ms: 1.15x faster                                                    |
| pathlib                    | 19.3 ms                                                | 16.9 ms: 1.14x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 71.8 ms: 1.14x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.27 ms: 1.14x faster                                                   |
| unpickle_pure_python       | 230 us                                                 | 203 us: 1.13x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 78.9 ms: 1.13x faster                                                   |
| chaos                      | 67.0 ms                                                | 59.5 ms: 1.13x faster                                                   |
| pyflate                    | 482 ms                                                 | 431 ms: 1.12x faster                                                    |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 55.5 ms: 1.11x faster                                                   |
| generators                 | 31.2 ms                                                | 28.1 ms: 1.11x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.56 ms: 1.11x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.11x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 68.4 ms: 1.10x faster                                                   |
| django_template            | 34.6 ms                                                | 31.5 ms: 1.10x faster                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.1 ms: 1.09x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.09x faster                                                    |
| sympy_str                  | 300 ms                                                 | 276 ms: 1.08x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 100 ms: 1.07x faster                                                    |
| nbody                      | 97.0 ms                                                | 91.4 ms: 1.06x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 20.3 ms: 1.06x faster                                                   |
| mdp                        | 2.63 sec                                               | 2.49 sec: 1.06x faster                                                  |
| scimark_sor                | 129 ms                                                 | 123 ms: 1.05x faster                                                    |
| pprint_safe_repr           | 776 ms                                                 | 738 ms: 1.05x faster                                                    |
| 2to3                       | 274 ms                                                 | 262 ms: 1.05x faster                                                    |
| fannkuch                   | 417 ms                                                 | 399 ms: 1.05x faster                                                    |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.04x faster                                                  |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                    |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                   |
| richards                   | 45.8 ms                                                | 44.0 ms: 1.04x faster                                                   |
| regex_effbot               | 3.61 ms                                                | 3.46 ms: 1.04x faster                                                   |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                                   |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.04x faster                                                    |
| docutils                   | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                  |
| nqueens                    | 83.3 ms                                                | 80.8 ms: 1.03x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                                   |
| hexiom                     | 6.41 ms                                                | 6.24 ms: 1.03x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 66.7 ms: 1.03x faster                                                   |
| richards_super             | 51.5 ms                                                | 50.4 ms: 1.02x faster                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 53.7 ms: 1.02x faster                                                   |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.01x faster                                                    |
| sympy_expand               | 478 ms                                                 | 475 ms: 1.01x faster                                                    |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                    |
| scimark_lu                 | 118 ms                                                 | 118 ms: 1.00x slower                                                    |
| logging_silent             | 104 ns                                                 | 105 ns: 1.01x slower                                                    |
| json                       | 5.26 ms                                                | 5.33 ms: 1.01x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 7.14 ms: 1.03x slower                                                   |
| coroutines                 | 23.2 ms                                                | 24.0 ms: 1.04x slower                                                   |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                    |
| bench_thread_pool          | 842 us                                                 | 880 us: 1.05x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                    |
| json_loads                 | 28.5 us                                                | 30.0 us: 1.05x slower                                                   |
| telco                      | 7.10 ms                                                | 7.70 ms: 1.08x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 25.1 ms: 1.09x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.09x slower                                                   |
| coverage                   | 72.7 ms                                                | 84.8 ms: 1.17x slower                                                   |
| gc_traversal               | 3.79 ms                                                | 4.58 ms: 1.21x slower                                                   |
| python_startup             | 9.55 ms                                                | 13.0 ms: 1.36x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 2.42 ms: 1.64x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 81.8 ms: 3.41x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                            |

Benchmark hidden because not significant (2): pycparser, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250304-3.14.0a5+-39791ef-JIT/bm-20250304-linux-x86_64-brandtbucher-jit_warmup_1024-3.14.0a5+-39791ef.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.110x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.11x