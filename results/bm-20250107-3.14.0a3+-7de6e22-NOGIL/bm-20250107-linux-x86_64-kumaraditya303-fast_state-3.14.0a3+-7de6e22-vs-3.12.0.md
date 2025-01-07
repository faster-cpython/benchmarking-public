# Results vs. 3.12.0

- fork: kumaraditya303
- ref: fast_state
- machine: linux-x86_64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.130x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 345 ms: 1.26x slower                                                 |
| docutils       | 2.77 sec                                               | 2.99 sec: 1.08x slower                                               |
| Geometric mean | (ref)                                                  | 1.17x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 675 ms: 1.75x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 726 ms: 1.59x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 292 ms: 1.54x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 385 ms: 1.49x faster                                                 |
| async_tree_none            | 472 ms                                                 | 339 ms: 1.39x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 529 ms: 1.37x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 430 ms: 1.34x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 580 ms: 1.25x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.46x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 187 ms                                                 | 181 ms: 1.03x faster                                                 |
| float          | 84.7 ms                                                | 105 ms: 1.25x slower                                                 |
| nbody          | 97.0 ms                                                | 136 ms: 1.41x slower                                                 |
| Geometric mean | (ref)                                                  | 1.19x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.59 ms: 1.01x faster                                                |
| regex_dna      | 212 ms                                                 | 231 ms: 1.09x slower                                                 |
| regex_v8       | 23.1 ms                                                | 25.2 ms: 1.09x slower                                                |
| regex_compile  | 148 ms                                                 | 162 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                 | 95.7 ms: 1.12x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                 |
| json_loads           | 28.5 us                                                | 30.3 us: 1.06x slower                                                |
| xml_etree_generate   | 89.2 ms                                                | 96.2 ms: 1.08x slower                                                |
| tomli_loads          | 2.33 sec                                               | 2.55 sec: 1.10x slower                                               |
| xml_etree_process    | 61.7 ms                                                | 72.3 ms: 1.17x slower                                                |
| json_dumps           | 10.4 ms                                                | 13.0 ms: 1.25x slower                                                |
| unpickle_pure_python | 230 us                                                 | 314 us: 1.37x slower                                                 |
| pickle_pure_python   | 324 us                                                 | 482 us: 1.49x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x slower                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 9.59 ms: 1.38x slower                                                |
| python_startup         | 9.55 ms                                                | 15.5 ms: 1.62x slower                                                |
| Geometric mean         | (ref)                                                  | 1.50x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 46.5 ms: 1.34x slower                                                |
| mako            | 11.9 ms                                                | 18.2 ms: 1.53x slower                                                |
| Geometric mean  | (ref)                                                  | 1.44x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 675 ms: 1.75x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 726 ms: 1.59x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 292 ms: 1.54x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 385 ms: 1.49x faster                                                 |
| async_tree_none            | 472 ms                                                 | 339 ms: 1.39x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 529 ms: 1.37x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 430 ms: 1.34x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 580 ms: 1.25x faster                                                 |
| deepcopy                   | 371 us                                                 | 319 us: 1.16x faster                                                 |
| pathlib                    | 19.3 ms                                                | 17.1 ms: 1.13x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 95.7 ms: 1.12x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                 |
| pidigits                   | 187 ms                                                 | 181 ms: 1.03x faster                                                 |
| gc_traversal               | 3.79 ms                                                | 3.75 ms: 1.01x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 40.3 us: 1.01x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 3.32 us: 1.01x faster                                                |
| regex_effbot               | 3.61 ms                                                | 3.59 ms: 1.01x faster                                                |
| json                       | 5.26 ms                                                | 5.31 ms: 1.01x slower                                                |
| json_loads                 | 28.5 us                                                | 30.3 us: 1.06x slower                                                |
| xml_etree_generate         | 89.2 ms                                                | 96.2 ms: 1.08x slower                                                |
| docutils                   | 2.77 sec                                               | 2.99 sec: 1.08x slower                                               |
| sympy_sum                  | 169 ms                                                 | 183 ms: 1.08x slower                                                 |
| async_generators           | 463 ms                                                 | 501 ms: 1.08x slower                                                 |
| mdp                        | 2.63 sec                                               | 2.86 sec: 1.09x slower                                               |
| regex_dna                  | 212 ms                                                 | 231 ms: 1.09x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 25.2 ms: 1.09x slower                                                |
| scimark_fft                | 382 ms                                                 | 417 ms: 1.09x slower                                                 |
| regex_compile              | 148 ms                                                 | 162 ms: 1.09x slower                                                 |
| tomli_loads                | 2.33 sec                                               | 2.55 sec: 1.10x slower                                               |
| dulwich_log                | 68.5 ms                                                | 75.5 ms: 1.10x slower                                                |
| spectral_norm              | 115 ms                                                 | 127 ms: 1.11x slower                                                 |
| sympy_str                  | 300 ms                                                 | 333 ms: 1.11x slower                                                 |
| crypto_pyaes               | 81.9 ms                                                | 92.3 ms: 1.13x slower                                                |
| sympy_integrate            | 21.4 ms                                                | 24.5 ms: 1.14x slower                                                |
| generators                 | 31.2 ms                                                | 35.9 ms: 1.15x slower                                                |
| coroutines                 | 23.2 ms                                                | 26.8 ms: 1.15x slower                                                |
| sympy_expand               | 478 ms                                                 | 555 ms: 1.16x slower                                                 |
| pycparser                  | 1.18 sec                                               | 1.37 sec: 1.16x slower                                               |
| comprehensions             | 21.8 us                                                | 25.4 us: 1.17x slower                                                |
| meteor_contest             | 112 ms                                                 | 131 ms: 1.17x slower                                                 |
| xml_etree_process          | 61.7 ms                                                | 72.3 ms: 1.17x slower                                                |
| sqlglot_normalize          | 110 ms                                                 | 129 ms: 1.17x slower                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 64.7 ms: 1.18x slower                                                |
| nqueens                    | 83.3 ms                                                | 99.8 ms: 1.20x slower                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 6.14 ms: 1.21x slower                                                |
| logging_format             | 7.23 us                                                | 8.81 us: 1.22x slower                                                |
| logging_simple             | 6.46 us                                                | 7.92 us: 1.23x slower                                                |
| sqlalchemy_declarative     | 147 ms                                                 | 180 ms: 1.23x slower                                                 |
| pprint_safe_repr           | 776 ms                                                 | 956 ms: 1.23x slower                                                 |
| float                      | 84.7 ms                                                | 105 ms: 1.25x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 13.0 ms: 1.25x slower                                                |
| 2to3                       | 274 ms                                                 | 345 ms: 1.26x slower                                                 |
| sqlalchemy_imperative      | 18.7 ms                                                | 23.5 ms: 1.26x slower                                                |
| pprint_pformat             | 1.57 sec                                               | 1.98 sec: 1.26x slower                                               |
| fannkuch                   | 417 ms                                                 | 526 ms: 1.26x slower                                                 |
| telco                      | 7.10 ms                                                | 9.21 ms: 1.30x slower                                                |
| scimark_lu                 | 118 ms                                                 | 154 ms: 1.31x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 206 us: 1.31x slower                                                 |
| django_template            | 34.6 ms                                                | 46.5 ms: 1.34x slower                                                |
| pyflate                    | 482 ms                                                 | 651 ms: 1.35x slower                                                 |
| richards_super             | 51.5 ms                                                | 70.3 ms: 1.37x slower                                                |
| unpickle_pure_python       | 230 us                                                 | 314 us: 1.37x slower                                                 |
| richards                   | 45.8 ms                                                | 63.1 ms: 1.38x slower                                                |
| python_startup_no_site     | 6.94 ms                                                | 9.59 ms: 1.38x slower                                                |
| chaos                      | 67.0 ms                                                | 92.7 ms: 1.38x slower                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 105 ms: 1.39x slower                                                 |
| nbody                      | 97.0 ms                                                | 136 ms: 1.41x slower                                                 |
| coverage                   | 72.7 ms                                                | 103 ms: 1.41x slower                                                 |
| mypy2                      | 830 ms                                                 | 1.20 sec: 1.45x slower                                               |
| hexiom                     | 6.41 ms                                                | 9.50 ms: 1.48x slower                                                |
| raytrace                   | 312 ms                                                 | 465 ms: 1.49x slower                                                 |
| pickle_pure_python         | 324 us                                                 | 482 us: 1.49x slower                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 2.55 ms: 1.52x slower                                                |
| mako                       | 11.9 ms                                                | 18.2 ms: 1.53x slower                                                |
| go                         | 139 ms                                                 | 218 ms: 1.57x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.33 ms: 1.58x slower                                                |
| python_startup             | 9.55 ms                                                | 15.5 ms: 1.62x slower                                                |
| sqlglot_parse              | 1.36 ms                                                | 2.21 ms: 1.62x slower                                                |
| logging_silent             | 104 ns                                                 | 176 ns: 1.68x slower                                                 |
| scimark_sor                | 129 ms                                                 | 223 ms: 1.73x slower                                                 |
| deltablue                  | 3.72 ms                                                | 7.05 ms: 1.90x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 95.0 ms: 3.96x slower                                                |
| bench_thread_pool          | 842 us                                                 | 3.56 ms: 4.23x slower                                                |
| Geometric mean             | (ref)                                                  | 1.19x slower                                                         |

Benchmark hidden because not significant (2): sqlite_synth, asyncio_websockets
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250107-3.14.0a3+-7de6e22-NOGIL/bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.130x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: 1.30x