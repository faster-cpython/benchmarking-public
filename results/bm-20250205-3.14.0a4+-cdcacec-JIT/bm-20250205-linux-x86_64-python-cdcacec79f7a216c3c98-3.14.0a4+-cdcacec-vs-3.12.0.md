# Results vs. 3.12.0

- fork: python
- ref: cdcacec79f7a216c3c98
- machine: linux-x86_64
- commit hash: cdcacec
- commit date: 2025-02-05
- overall geometric mean: 1.102x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 261 ms: 1.05x faster                                                   |
| docutils       | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.90x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 627 ms: 1.84x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 319 ms: 1.80x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 255 ms: 1.76x faster                                                   |
| async_tree_none            | 472 ms                                                 | 268 ms: 1.76x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 329 ms: 1.76x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 487 ms: 1.49x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 501 ms: 1.45x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.71x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 67.1 ms: 1.26x faster                                                  |
| nbody          | 97.0 ms                                                | 93.6 ms: 1.04x faster                                                  |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.31 ms: 1.09x faster                                                  |
| regex_dna      | 212 ms                                                 | 215 ms: 1.01x slower                                                   |
| regex_v8       | 23.1 ms                                                | 24.1 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.84 sec: 1.27x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 138 ms: 1.15x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 201 us: 1.14x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 95.9 ms: 1.11x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 56.7 ms: 1.09x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 83.3 ms: 1.07x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 314 us: 1.03x faster                                                   |
| json_loads           | 28.5 us                                                | 29.1 us: 1.02x slower                                                  |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.04 ms: 1.01x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.86 ms: 1.21x faster                                                  |
| django_template | 34.6 ms                                                | 33.0 ms: 1.05x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.90x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 627 ms: 1.84x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 319 ms: 1.80x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 255 ms: 1.76x faster                                                   |
| async_tree_none            | 472 ms                                                 | 268 ms: 1.76x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 329 ms: 1.76x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 487 ms: 1.49x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 501 ms: 1.45x faster                                                   |
| deepcopy                   | 371 us                                                 | 272 us: 1.37x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 30.3 us: 1.34x faster                                                  |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.28x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.84 sec: 1.27x faster                                                 |
| float                      | 84.7 ms                                                | 67.1 ms: 1.26x faster                                                  |
| scimark_fft                | 382 ms                                                 | 315 ms: 1.21x faster                                                   |
| mako                       | 11.9 ms                                                | 9.86 ms: 1.21x faster                                                  |
| spectral_norm              | 115 ms                                                 | 95.4 ms: 1.20x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.81 us: 1.19x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 63.5 ms: 1.18x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 69.9 ms: 1.17x faster                                                  |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 138 ms: 1.15x faster                                                   |
| unpickle_pure_python       | 230 us                                                 | 201 us: 1.14x faster                                                   |
| logging_format             | 7.23 us                                                | 6.32 us: 1.14x faster                                                  |
| scimark_sor                | 129 ms                                                 | 114 ms: 1.13x faster                                                   |
| async_generators           | 463 ms                                                 | 411 ms: 1.13x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.51 ms: 1.12x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.77 us: 1.12x faster                                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                   |
| chaos                      | 67.0 ms                                                | 60.0 ms: 1.12x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 95.9 ms: 1.11x faster                                                  |
| go                         | 139 ms                                                 | 126 ms: 1.11x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 155 ms: 1.09x faster                                                   |
| regex_effbot               | 3.61 ms                                                | 3.31 ms: 1.09x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 56.7 ms: 1.09x faster                                                  |
| fannkuch                   | 417 ms                                                 | 386 ms: 1.08x faster                                                   |
| pyflate                    | 482 ms                                                 | 448 ms: 1.08x faster                                                   |
| sympy_str                  | 300 ms                                                 | 280 ms: 1.07x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 83.3 ms: 1.07x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.48 ms: 1.07x faster                                                  |
| raytrace                   | 312 ms                                                 | 292 ms: 1.07x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                                  |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                   |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                  |
| 2to3                       | 274 ms                                                 | 261 ms: 1.05x faster                                                   |
| richards                   | 45.8 ms                                                | 43.7 ms: 1.05x faster                                                  |
| django_template            | 34.6 ms                                                | 33.0 ms: 1.05x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.71 us: 1.05x faster                                                  |
| nbody                      | 97.0 ms                                                | 93.6 ms: 1.04x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 20.7 ms: 1.03x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 314 us: 1.03x faster                                                   |
| richards_super             | 51.5 ms                                                | 50.1 ms: 1.03x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.56 sec: 1.03x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 66.9 ms: 1.02x faster                                                  |
| coroutines                 | 23.2 ms                                                | 22.7 ms: 1.02x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.02x faster                                                   |
| json                       | 5.26 ms                                                | 5.15 ms: 1.02x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                                   |
| sympy_expand               | 478 ms                                                 | 469 ms: 1.02x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 763 ms: 1.02x faster                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 54.3 ms: 1.01x faster                                                  |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| regex_dna                  | 212 ms                                                 | 215 ms: 1.01x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 7.04 ms: 1.01x slower                                                  |
| json_loads                 | 28.5 us                                                | 29.1 us: 1.02x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.02x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 24.1 ms: 1.04x slower                                                  |
| telco                      | 7.10 ms                                                | 7.53 ms: 1.06x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 897 us: 1.07x slower                                                   |
| logging_silent             | 104 ns                                                 | 112 ns: 1.07x slower                                                   |
| nqueens                    | 83.3 ms                                                | 90.5 ms: 1.09x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                  |
| hexiom                     | 6.41 ms                                                | 7.43 ms: 1.16x slower                                                  |
| generators                 | 31.2 ms                                                | 37.5 ms: 1.20x slower                                                  |
| coverage                   | 72.7 ms                                                | 90.6 ms: 1.25x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.89 ms: 1.29x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.45 ms: 1.66x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 80.4 ms: 3.35x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (3): pprint_pformat, asyncio_websockets, pycparser
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250205-3.14.0a4+-cdcacec-JIT/bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.102x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.10x