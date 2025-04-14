# Results vs. 3.12.0

- fork: brandtbucher
- ref: non_methods
- machine: linux-x86_64
- commit hash: fe5b174
- commit date: 2025-04-07
- overall geometric mean: 1.141x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 250 ms: 1.10x faster                                                |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                              |
| Geometric mean | (ref)                                                  | 1.08x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 608 ms: 1.95x faster                                                |
| async_tree_io              | 1.16 sec                                               | 609 ms: 1.90x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 308 ms: 1.88x faster                                                |
| async_tree_none            | 472 ms                                                 | 255 ms: 1.85x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 245 ms: 1.84x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 477 ms: 1.52x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 483 ms: 1.50x faster                                                |
| Geometric mean             | (ref)                                                  | 1.78x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.8 ms: 1.29x faster                                               |
| nbody          | 97.0 ms                                                | 90.9 ms: 1.07x faster                                               |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                  | 1.11x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 123 ms: 1.21x faster                                                |
| regex_effbot   | 3.61 ms                                                | 3.19 ms: 1.13x faster                                               |
| regex_dna      | 212 ms                                                 | 214 ms: 1.01x slower                                                |
| regex_v8       | 23.1 ms                                                | 24.1 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.89 sec: 1.24x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 98.7 ms: 1.08x faster                                               |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 83.2 ms: 1.07x faster                                               |
| xml_etree_process    | 61.7 ms                                                | 58.0 ms: 1.07x faster                                               |
| pickle_pure_python   | 324 us                                                 | 310 us: 1.04x faster                                                |
| json_loads           | 28.5 us                                                | 29.8 us: 1.05x slower                                               |
| json_dumps           | 10.4 ms                                                | 11.7 ms: 1.12x slower                                               |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.21 ms: 1.18x slower                                               |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                               |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.5 ms: 1.10x faster                                               |
| mako            | 11.9 ms                                                | 11.0 ms: 1.08x faster                                               |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.14x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 608 ms: 1.95x faster                                                |
| async_tree_io              | 1.16 sec                                               | 609 ms: 1.90x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 308 ms: 1.88x faster                                                |
| async_tree_none            | 472 ms                                                 | 255 ms: 1.85x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 245 ms: 1.84x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 477 ms: 1.52x faster                                                |
| deepcopy                   | 371 us                                                 | 246 us: 1.51x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 483 ms: 1.50x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 28.4 us: 1.43x faster                                               |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                               |
| float                      | 84.7 ms                                                | 65.8 ms: 1.29x faster                                               |
| deepcopy_reduce            | 3.35 us                                                | 2.60 us: 1.29x faster                                               |
| go                         | 139 ms                                                 | 109 ms: 1.27x faster                                                |
| tomli_loads                | 2.33 sec                                               | 1.89 sec: 1.24x faster                                              |
| raytrace                   | 312 ms                                                 | 256 ms: 1.22x faster                                                |
| chaos                      | 67.0 ms                                                | 55.3 ms: 1.21x faster                                               |
| regex_compile              | 148 ms                                                 | 123 ms: 1.21x faster                                                |
| logging_format             | 7.23 us                                                | 6.07 us: 1.19x faster                                               |
| async_generators           | 463 ms                                                 | 389 ms: 1.19x faster                                                |
| spectral_norm              | 115 ms                                                 | 97.7 ms: 1.18x faster                                               |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                               |
| scimark_monte_carlo        | 75.1 ms                                                | 64.1 ms: 1.17x faster                                               |
| logging_simple             | 6.46 us                                                | 5.53 us: 1.17x faster                                               |
| dulwich_log                | 68.5 ms                                                | 59.4 ms: 1.15x faster                                               |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                |
| scimark_fft                | 382 ms                                                 | 336 ms: 1.14x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.27 ms: 1.14x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 72.3 ms: 1.13x faster                                               |
| regex_effbot               | 3.61 ms                                                | 3.19 ms: 1.13x faster                                               |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 19.0 ms: 1.12x faster                                               |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.7 ms: 1.12x faster                                               |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                |
| scimark_sor                | 129 ms                                                 | 115 ms: 1.12x faster                                                |
| logging_silent             | 104 ns                                                 | 93.5 ns: 1.12x faster                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.60 ms: 1.10x faster                                               |
| django_template            | 34.6 ms                                                | 31.5 ms: 1.10x faster                                               |
| 2to3                       | 274 ms                                                 | 250 ms: 1.10x faster                                                |
| pyflate                    | 482 ms                                                 | 443 ms: 1.09x faster                                                |
| richards                   | 45.8 ms                                                | 42.2 ms: 1.09x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 715 ms: 1.08x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 98.7 ms: 1.08x faster                                               |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                                |
| richards_super             | 51.5 ms                                                | 47.8 ms: 1.08x faster                                               |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                              |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 83.2 ms: 1.07x faster                                               |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                              |
| nbody                      | 97.0 ms                                                | 90.9 ms: 1.07x faster                                               |
| xml_etree_process          | 61.7 ms                                                | 58.0 ms: 1.07x faster                                               |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.06x faster                                              |
| sympy_expand               | 478 ms                                                 | 453 ms: 1.05x faster                                                |
| nqueens                    | 83.3 ms                                                | 79.8 ms: 1.04x faster                                               |
| pickle_pure_python         | 324 us                                                 | 310 us: 1.04x faster                                                |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.04x faster                                                |
| hexiom                     | 6.41 ms                                                | 6.18 ms: 1.04x faster                                               |
| generators                 | 31.2 ms                                                | 30.1 ms: 1.04x faster                                               |
| fannkuch                   | 417 ms                                                 | 407 ms: 1.02x faster                                                |
| sqlite_synth               | 2.83 us                                                | 2.78 us: 1.02x faster                                               |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                                |
| regex_dna                  | 212 ms                                                 | 214 ms: 1.01x slower                                                |
| json                       | 5.26 ms                                                | 5.37 ms: 1.02x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                |
| bench_thread_pool          | 842 us                                                 | 877 us: 1.04x slower                                                |
| regex_v8                   | 23.1 ms                                                | 24.1 ms: 1.04x slower                                               |
| json_loads                 | 28.5 us                                                | 29.8 us: 1.05x slower                                               |
| telco                      | 7.10 ms                                                | 7.65 ms: 1.08x slower                                               |
| json_dumps                 | 10.4 ms                                                | 11.7 ms: 1.12x slower                                               |
| coverage                   | 72.7 ms                                                | 85.1 ms: 1.17x slower                                               |
| python_startup_no_site     | 6.94 ms                                                | 8.21 ms: 1.18x slower                                               |
| gc_traversal               | 3.79 ms                                                | 4.64 ms: 1.22x slower                                               |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 82.0 ms: 3.42x slower                                               |
| Geometric mean             | (ref)                                                  | 1.12x faster                                                        |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250407-3.14.0a6+-fe5b174/bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.141x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.10x