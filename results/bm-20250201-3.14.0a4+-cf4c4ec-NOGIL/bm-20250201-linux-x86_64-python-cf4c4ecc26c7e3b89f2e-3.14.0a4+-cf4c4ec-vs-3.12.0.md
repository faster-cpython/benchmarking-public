# Results vs. 3.12.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: linux-x86_64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.019x slower
- HPT reliability: 99.86%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 305 ms: 1.11x slower                                                   |
| docutils       | 2.77 sec                                               | 2.80 sec: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 549 ms: 2.15x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 597 ms: 1.94x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 243 ms: 1.85x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 323 ms: 1.78x faster                                                   |
| async_tree_none            | 472 ms                                                 | 286 ms: 1.65x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 364 ms: 1.59x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 475 ms: 1.53x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 523 ms: 1.39x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 78.7 ms: 1.08x faster                                                  |
| pidigits       | 187 ms                                                 | 182 ms: 1.03x faster                                                   |
| nbody          | 97.0 ms                                                | 139 ms: 1.44x slower                                                   |
| Geometric mean | (ref)                                                  | 1.09x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.50 ms: 1.03x faster                                                  |
| regex_compile  | 148 ms                                                 | 147 ms: 1.01x faster                                                   |
| regex_dna      | 212 ms                                                 | 225 ms: 1.06x slower                                                   |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                 | 94.6 ms: 1.13x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                                   |
| pickle_dict          | 35.5 us                                                | 34.5 us: 1.03x faster                                                  |
| unpickle             | 15.9 us                                                | 16.1 us: 1.02x slower                                                  |
| pickle_list          | 5.08 us                                                | 5.19 us: 1.02x slower                                                  |
| tomli_loads          | 2.33 sec                                               | 2.38 sec: 1.02x slower                                                 |
| xml_etree_generate   | 89.2 ms                                                | 95.0 ms: 1.07x slower                                                  |
| pickle               | 11.6 us                                                | 12.4 us: 1.07x slower                                                  |
| unpickle_list        | 5.29 us                                                | 5.74 us: 1.09x slower                                                  |
| xml_etree_process    | 61.7 ms                                                | 67.7 ms: 1.10x slower                                                  |
| unpickle_pure_python | 230 us                                                 | 254 us: 1.11x slower                                                   |
| pickle_pure_python   | 324 us                                                 | 368 us: 1.13x slower                                                   |
| json_loads           | 28.5 us                                                | 33.2 us: 1.17x slower                                                  |
| json_dumps           | 10.4 ms                                                | 12.7 ms: 1.22x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 9.36 ms: 1.35x slower                                                  |
| python_startup         | 9.55 ms                                                | 15.0 ms: 1.57x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.46x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 40.1 ms: 1.16x slower                                                  |
| mako            | 11.9 ms                                                | 16.3 ms: 1.37x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.26x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 549 ms: 2.15x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 597 ms: 1.94x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 243 ms: 1.85x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 323 ms: 1.78x faster                                                   |
| gc_traversal               | 3.79 ms                                                | 2.25 ms: 1.69x faster                                                  |
| async_tree_none            | 472 ms                                                 | 286 ms: 1.65x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 364 ms: 1.59x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 475 ms: 1.53x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 523 ms: 1.39x faster                                                   |
| deepcopy                   | 371 us                                                 | 310 us: 1.20x faster                                                   |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 94.6 ms: 1.13x faster                                                  |
| comprehensions             | 21.8 us                                                | 20.0 us: 1.09x faster                                                  |
| float                      | 84.7 ms                                                | 78.7 ms: 1.08x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                                   |
| async_generators           | 463 ms                                                 | 435 ms: 1.06x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 39.1 us: 1.04x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.72 us: 1.04x faster                                                  |
| generators                 | 31.2 ms                                                | 30.2 ms: 1.03x faster                                                  |
| pidigits                   | 187 ms                                                 | 182 ms: 1.03x faster                                                   |
| regex_effbot               | 3.61 ms                                                | 3.50 ms: 1.03x faster                                                  |
| pickle_dict                | 35.5 us                                                | 34.5 us: 1.03x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 3.25 us: 1.03x faster                                                  |
| unpack_sequence            | 54.0 ns                                                | 52.5 ns: 1.03x faster                                                  |
| regex_compile              | 148 ms                                                 | 147 ms: 1.01x faster                                                   |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                   |
| dulwich_log                | 68.5 ms                                                | 68.9 ms: 1.00x slower                                                  |
| docutils                   | 2.77 sec                                               | 2.80 sec: 1.01x slower                                                 |
| go                         | 139 ms                                                 | 141 ms: 1.01x slower                                                   |
| unpickle                   | 15.9 us                                                | 16.1 us: 1.02x slower                                                  |
| pickle_list                | 5.08 us                                                | 5.19 us: 1.02x slower                                                  |
| logging_format             | 7.23 us                                                | 7.38 us: 1.02x slower                                                  |
| tomli_loads                | 2.33 sec                                               | 2.38 sec: 1.02x slower                                                 |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                                 |
| logging_simple             | 6.46 us                                                | 6.60 us: 1.02x slower                                                  |
| sympy_sum                  | 169 ms                                                 | 174 ms: 1.03x slower                                                   |
| sympy_str                  | 300 ms                                                 | 315 ms: 1.05x slower                                                   |
| pyflate                    | 482 ms                                                 | 510 ms: 1.06x slower                                                   |
| coroutines                 | 23.2 ms                                                | 24.6 ms: 1.06x slower                                                  |
| regex_dna                  | 212 ms                                                 | 225 ms: 1.06x slower                                                   |
| xml_etree_generate         | 89.2 ms                                                | 95.0 ms: 1.07x slower                                                  |
| logging_silent             | 104 ns                                                 | 111 ns: 1.07x slower                                                   |
| scimark_sor                | 129 ms                                                 | 138 ms: 1.07x slower                                                   |
| pickle                     | 11.6 us                                                | 12.4 us: 1.07x slower                                                  |
| sqlglot_normalize          | 110 ms                                                 | 118 ms: 1.07x slower                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 159 ms: 1.08x slower                                                   |
| mdp                        | 2.63 sec                                               | 2.84 sec: 1.08x slower                                                 |
| sqlalchemy_imperative      | 18.7 ms                                                | 20.3 ms: 1.08x slower                                                  |
| crypto_pyaes               | 81.9 ms                                                | 88.7 ms: 1.08x slower                                                  |
| json                       | 5.26 ms                                                | 5.70 ms: 1.08x slower                                                  |
| pprint_safe_repr           | 776 ms                                                 | 841 ms: 1.08x slower                                                   |
| unpickle_list              | 5.29 us                                                | 5.74 us: 1.09x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 25.1 ms: 1.09x slower                                                  |
| sympy_expand               | 478 ms                                                 | 521 ms: 1.09x slower                                                   |
| sympy_integrate            | 21.4 ms                                                | 23.4 ms: 1.09x slower                                                  |
| scimark_fft                | 382 ms                                                 | 419 ms: 1.10x slower                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 60.1 ms: 1.10x slower                                                  |
| xml_etree_process          | 61.7 ms                                                | 67.7 ms: 1.10x slower                                                  |
| asyncio_tcp                | 491 ms                                                 | 539 ms: 1.10x slower                                                   |
| unpickle_pure_python       | 230 us                                                 | 254 us: 1.11x slower                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.73 sec: 1.11x slower                                                 |
| 2to3                       | 274 ms                                                 | 305 ms: 1.11x slower                                                   |
| chaos                      | 67.0 ms                                                | 74.6 ms: 1.11x slower                                                  |
| raytrace                   | 312 ms                                                 | 349 ms: 1.12x slower                                                   |
| sqlglot_transpile          | 1.68 ms                                                | 1.90 ms: 1.13x slower                                                  |
| pickle_pure_python         | 324 us                                                 | 368 us: 1.13x slower                                                   |
| asyncio_tcp_ssl            | 1.79 sec                                               | 2.05 sec: 1.15x slower                                                 |
| sqlglot_parse              | 1.36 ms                                                | 1.57 ms: 1.15x slower                                                  |
| django_template            | 34.6 ms                                                | 40.1 ms: 1.16x slower                                                  |
| meteor_contest             | 112 ms                                                 | 131 ms: 1.16x slower                                                   |
| json_loads                 | 28.5 us                                                | 33.2 us: 1.17x slower                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 87.6 ms: 1.17x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 1.75 ms: 1.19x slower                                                  |
| richards                   | 45.8 ms                                                | 54.4 ms: 1.19x slower                                                  |
| scimark_lu                 | 118 ms                                                 | 140 ms: 1.19x slower                                                   |
| nqueens                    | 83.3 ms                                                | 99.6 ms: 1.20x slower                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 6.09 ms: 1.20x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 12.7 ms: 1.22x slower                                                  |
| hexiom                     | 6.41 ms                                                | 7.85 ms: 1.22x slower                                                  |
| richards_super             | 51.5 ms                                                | 63.3 ms: 1.23x slower                                                  |
| fannkuch                   | 417 ms                                                 | 519 ms: 1.25x slower                                                   |
| deltablue                  | 3.72 ms                                                | 4.73 ms: 1.27x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 202 us: 1.28x slower                                                   |
| telco                      | 7.10 ms                                                | 9.18 ms: 1.29x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 9.36 ms: 1.35x slower                                                  |
| mako                       | 11.9 ms                                                | 16.3 ms: 1.37x slower                                                  |
| nbody                      | 97.0 ms                                                | 139 ms: 1.44x slower                                                   |
| coverage                   | 72.7 ms                                                | 107 ms: 1.48x slower                                                   |
| python_startup             | 9.55 ms                                                | 15.0 ms: 1.57x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 84.8 ms: 3.53x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 3.48 ms: 4.14x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.05x slower                                                           |

Benchmark hidden because not significant (1): spectral_norm
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250201-3.14.0a4+-cf4c4ec-NOGIL/bm-20250201-linux-x86_64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.019x slower

# HPT report

- Reliability score: 99.86% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.30x