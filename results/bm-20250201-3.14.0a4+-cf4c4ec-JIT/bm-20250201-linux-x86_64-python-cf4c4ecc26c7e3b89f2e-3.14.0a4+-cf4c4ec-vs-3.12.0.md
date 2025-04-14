# Results vs. 3.12.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: linux-x86_64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.108x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.06x faster                                                   |
| docutils       | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 626 ms: 1.85x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.81x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 255 ms: 1.77x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 328 ms: 1.76x faster                                                   |
| async_tree_none            | 472 ms                                                 | 270 ms: 1.75x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 477 ms: 1.52x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.48x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 67.0 ms: 1.26x faster                                                  |
| nbody          | 97.0 ms                                                | 88.0 ms: 1.10x faster                                                  |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.15x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.17 ms: 1.14x faster                                                  |
| regex_dna      | 212 ms                                                 | 208 ms: 1.02x faster                                                   |
| regex_v8       | 23.1 ms                                                | 23.5 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.84 sec: 1.27x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 196 us: 1.17x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.15x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 79.4 ms: 1.12x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 95.0 ms: 1.12x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 55.3 ms: 1.12x faster                                                  |
| unpickle             | 15.9 us                                                | 14.4 us: 1.10x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 309 us: 1.05x faster                                                   |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                                  |
| pickle_dict          | 35.5 us                                                | 36.6 us: 1.03x slower                                                  |
| unpickle_list        | 5.29 us                                                | 5.60 us: 1.06x slower                                                  |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                  |
| pickle               | 11.6 us                                                | 12.7 us: 1.10x slower                                                  |
| pickle_list          | 5.08 us                                                | 5.70 us: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.0 ms: 1.19x faster                                                  |
| django_template | 34.6 ms                                                | 33.8 ms: 1.02x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 626 ms: 1.85x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.81x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 255 ms: 1.77x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 328 ms: 1.76x faster                                                   |
| async_tree_none            | 472 ms                                                 | 270 ms: 1.75x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 477 ms: 1.52x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.48x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 30.4 us: 1.34x faster                                                  |
| deepcopy                   | 371 us                                                 | 279 us: 1.33x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.84 sec: 1.27x faster                                                 |
| comprehensions             | 21.8 us                                                | 17.2 us: 1.26x faster                                                  |
| float                      | 84.7 ms                                                | 67.0 ms: 1.26x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                                  |
| scimark_fft                | 382 ms                                                 | 310 ms: 1.23x faster                                                   |
| spectral_norm              | 115 ms                                                 | 94.4 ms: 1.22x faster                                                  |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 62.7 ms: 1.20x faster                                                  |
| mako                       | 11.9 ms                                                | 10.0 ms: 1.19x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 196 us: 1.17x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 70.0 ms: 1.17x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.33 ms: 1.17x faster                                                  |
| regex_compile              | 148 ms                                                 | 128 ms: 1.15x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.15x faster                                                   |
| chaos                      | 67.0 ms                                                | 58.6 ms: 1.14x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.17 ms: 1.14x faster                                                  |
| async_generators           | 463 ms                                                 | 407 ms: 1.14x faster                                                   |
| logging_format             | 7.23 us                                                | 6.38 us: 1.13x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 79.4 ms: 1.12x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 95.0 ms: 1.12x faster                                                  |
| scimark_sor                | 129 ms                                                 | 115 ms: 1.12x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                   |
| go                         | 139 ms                                                 | 124 ms: 1.12x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 55.3 ms: 1.12x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.81 us: 1.11x faster                                                  |
| nbody                      | 97.0 ms                                                | 88.0 ms: 1.10x faster                                                  |
| unpickle                   | 15.9 us                                                | 14.4 us: 1.10x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 155 ms: 1.09x faster                                                   |
| raytrace                   | 312 ms                                                 | 288 ms: 1.08x faster                                                   |
| fannkuch                   | 417 ms                                                 | 390 ms: 1.07x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.47 ms: 1.07x faster                                                  |
| sympy_str                  | 300 ms                                                 | 280 ms: 1.07x faster                                                   |
| richards                   | 45.8 ms                                                | 43.0 ms: 1.07x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                  |
| 2to3                       | 274 ms                                                 | 260 ms: 1.06x faster                                                   |
| pickle_pure_python         | 324 us                                                 | 309 us: 1.05x faster                                                   |
| richards_super             | 51.5 ms                                                | 49.2 ms: 1.05x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.72 us: 1.04x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 20.5 ms: 1.04x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 744 ms: 1.04x faster                                                   |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                 |
| pyflate                    | 482 ms                                                 | 465 ms: 1.04x faster                                                   |
| docutils                   | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                 |
| mdp                        | 2.63 sec                                               | 2.56 sec: 1.03x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 66.7 ms: 1.03x faster                                                  |
| django_template            | 34.6 ms                                                | 33.8 ms: 1.02x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                   |
| regex_dna                  | 212 ms                                                 | 208 ms: 1.02x faster                                                   |
| sympy_expand               | 478 ms                                                 | 471 ms: 1.01x faster                                                   |
| json                       | 5.26 ms                                                | 5.19 ms: 1.01x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                                  |
| coroutines                 | 23.2 ms                                                | 23.5 ms: 1.01x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 23.5 ms: 1.01x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.82 sec: 1.02x slower                                                 |
| pickle_dict                | 35.5 us                                                | 36.6 us: 1.03x slower                                                  |
| logging_silent             | 104 ns                                                 | 109 ns: 1.04x slower                                                   |
| bench_thread_pool          | 842 us                                                 | 891 us: 1.06x slower                                                   |
| unpickle_list              | 5.29 us                                                | 5.60 us: 1.06x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                   |
| nqueens                    | 83.3 ms                                                | 89.2 ms: 1.07x slower                                                  |
| telco                      | 7.10 ms                                                | 7.62 ms: 1.07x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                  |
| pickle                     | 11.6 us                                                | 12.7 us: 1.10x slower                                                  |
| pickle_list                | 5.08 us                                                | 5.70 us: 1.12x slower                                                  |
| hexiom                     | 6.41 ms                                                | 7.40 ms: 1.15x slower                                                  |
| generators                 | 31.2 ms                                                | 37.4 ms: 1.20x slower                                                  |
| coverage                   | 72.7 ms                                                | 89.6 ms: 1.23x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.72 ms: 1.24x slower                                                  |
| unpack_sequence            | 54.0 ns                                                | 70.4 ns: 1.30x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 80.8 ms: 3.36x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                           |

Benchmark hidden because not significant (4): pycparser, asyncio_tcp, asyncio_websockets, sqlglot_optimize
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250201-3.14.0a4+-cf4c4ec-JIT/bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.108x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.10x