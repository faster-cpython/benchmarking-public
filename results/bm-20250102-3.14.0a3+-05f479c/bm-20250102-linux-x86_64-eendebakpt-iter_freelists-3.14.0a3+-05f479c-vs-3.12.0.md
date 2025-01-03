# Results vs. 3.12.0

- fork: eendebakpt
- ref: iter_freelists
- machine: linux-x86_64
- commit hash: 05f479c
- commit date: 2025-01-02
- overall geometric mean: 1.114x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 253 ms: 1.09x faster                                                 |
| docutils       | 2.77 sec                                               | 2.57 sec: 1.08x faster                                               |
| Geometric mean | (ref)                                                  | 1.08x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 585 ms: 2.02x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 301 ms: 1.91x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 607 ms: 1.90x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 242 ms: 1.86x faster                                                 |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 323 ms: 1.79x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 467 ms: 1.55x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 480 ms: 1.51x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.79x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 72.8 ms: 1.16x faster                                                |
| nbody          | 97.0 ms                                                | 94.1 ms: 1.03x faster                                                |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.18x faster                                                 |
| regex_effbot   | 3.61 ms                                                | 3.32 ms: 1.09x faster                                                |
| regex_dna      | 212 ms                                                 | 204 ms: 1.04x faster                                                 |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.08x slower                                                |
| Geometric mean | (ref)                                                  | 1.05x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                               |
| xml_etree_parse      | 159 ms                                                 | 137 ms: 1.16x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 96.0 ms: 1.11x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 83.2 ms: 1.07x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 58.0 ms: 1.06x faster                                                |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                 |
| json_loads           | 28.5 us                                                | 26.9 us: 1.06x faster                                                |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                         |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.4 ms: 1.10x faster                                                |
| mako            | 11.9 ms                                                | 11.8 ms: 1.01x faster                                                |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 585 ms: 2.02x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 301 ms: 1.91x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 607 ms: 1.90x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 242 ms: 1.86x faster                                                 |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 323 ms: 1.79x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 467 ms: 1.55x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 480 ms: 1.51x faster                                                 |
| deepcopy                   | 371 us                                                 | 257 us: 1.44x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 30.9 us: 1.32x faster                                                |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 2.61 us: 1.28x faster                                                |
| pathlib                    | 19.3 ms                                                | 15.8 ms: 1.22x faster                                                |
| go                         | 139 ms                                                 | 115 ms: 1.21x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                               |
| regex_compile              | 148 ms                                                 | 125 ms: 1.18x faster                                                 |
| logging_format             | 7.23 us                                                | 6.19 us: 1.17x faster                                                |
| float                      | 84.7 ms                                                | 72.8 ms: 1.16x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 137 ms: 1.16x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.21 ms: 1.16x faster                                                |
| raytrace                   | 312 ms                                                 | 270 ms: 1.15x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 71.2 ms: 1.15x faster                                                |
| sqlalchemy_declarative     | 147 ms                                                 | 128 ms: 1.15x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.66 us: 1.14x faster                                                |
| generators                 | 31.2 ms                                                | 27.4 ms: 1.14x faster                                                |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.4 ms: 1.14x faster                                                |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                 |
| chaos                      | 67.0 ms                                                | 59.8 ms: 1.12x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 96.0 ms: 1.11x faster                                                |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.11x faster                                                 |
| async_generators           | 463 ms                                                 | 419 ms: 1.11x faster                                                 |
| django_template            | 34.6 ms                                                | 31.4 ms: 1.10x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 68.3 ms: 1.10x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 19.5 ms: 1.10x faster                                                |
| sqlglot_normalize          | 110 ms                                                 | 101 ms: 1.09x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.32 ms: 1.09x faster                                                |
| 2to3                       | 274 ms                                                 | 253 ms: 1.09x faster                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 50.8 ms: 1.08x faster                                                |
| docutils                   | 2.77 sec                                               | 2.57 sec: 1.08x faster                                               |
| scimark_fft                | 382 ms                                                 | 355 ms: 1.08x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 63.7 ms: 1.08x faster                                                |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 83.2 ms: 1.07x faster                                                |
| sympy_expand               | 478 ms                                                 | 447 ms: 1.07x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 726 ms: 1.07x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.07x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 58.0 ms: 1.06x faster                                                |
| mdp                        | 2.63 sec                                               | 2.48 sec: 1.06x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                 |
| json_loads                 | 28.5 us                                                | 26.9 us: 1.06x faster                                                |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                               |
| json                       | 5.26 ms                                                | 4.98 ms: 1.06x faster                                                |
| nqueens                    | 83.3 ms                                                | 78.9 ms: 1.06x faster                                                |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                               |
| regex_dna                  | 212 ms                                                 | 204 ms: 1.04x faster                                                 |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                 |
| richards                   | 45.8 ms                                                | 44.2 ms: 1.04x faster                                                |
| fannkuch                   | 417 ms                                                 | 403 ms: 1.03x faster                                                 |
| nbody                      | 97.0 ms                                                | 94.1 ms: 1.03x faster                                                |
| hexiom                     | 6.41 ms                                                | 6.24 ms: 1.03x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.94 ms: 1.02x faster                                                |
| pyflate                    | 482 ms                                                 | 472 ms: 1.02x faster                                                 |
| richards_super             | 51.5 ms                                                | 50.6 ms: 1.02x faster                                                |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                 |
| mako                       | 11.9 ms                                                | 11.8 ms: 1.01x faster                                                |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                                |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.01x slower                                                |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                |
| bench_thread_pool          | 842 us                                                 | 859 us: 1.02x slower                                                 |
| logging_silent             | 104 ns                                                 | 107 ns: 1.02x slower                                                 |
| telco                      | 7.10 ms                                                | 7.64 ms: 1.08x slower                                                |
| regex_v8                   | 23.1 ms                                                | 25.1 ms: 1.08x slower                                                |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                |
| mypy2                      | 830 ms                                                 | 938 ms: 1.13x slower                                                 |
| coverage                   | 72.7 ms                                                | 84.6 ms: 1.16x slower                                                |
| gc_traversal               | 3.79 ms                                                | 4.78 ms: 1.26x slower                                                |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.66x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 81.6 ms: 3.40x slower                                                |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                         |

Benchmark hidden because not significant (3): pickle_pure_python, typing_runtime_protocols, asyncio_websockets
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250102-3.14.0a3+-05f479c/bm-20250102-linux-x86_64-eendebakpt-iter_freelists-3.14.0a3+-05f479c.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.114x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.10x