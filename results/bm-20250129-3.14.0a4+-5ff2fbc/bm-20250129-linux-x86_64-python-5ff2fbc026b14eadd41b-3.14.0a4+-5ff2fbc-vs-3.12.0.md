# Results vs. 3.12.0

- fork: python
- ref: 5ff2fbc026b14eadd41b
- machine: linux-x86_64
- commit hash: 5ff2fbc
- commit date: 2025-01-29
- overall geometric mean: 1.113x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 253 ms: 1.08x faster                                                   |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 624 ms: 1.89x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 620 ms: 1.87x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 319 ms: 1.80x faster                                                   |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 324 ms: 1.79x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 477 ms: 1.52x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 72.3 ms: 1.17x faster                                                  |
| nbody          | 97.0 ms                                                | 94.3 ms: 1.03x faster                                                  |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.27 ms: 1.11x faster                                                  |
| regex_dna      | 212 ms                                                 | 218 ms: 1.03x slower                                                   |
| regex_v8       | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.97 sec: 1.18x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 138 ms: 1.16x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 96.4 ms: 1.11x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 83.6 ms: 1.07x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 58.4 ms: 1.06x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.05x faster                                                   |
| json_loads           | 28.5 us                                                | 28.6 us: 1.00x slower                                                  |
| json_dumps           | 10.4 ms                                                | 11.9 ms: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.3 ms: 1.10x faster                                                  |
| mako            | 11.9 ms                                                | 11.6 ms: 1.02x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 624 ms: 1.89x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 620 ms: 1.87x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 319 ms: 1.80x faster                                                   |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 324 ms: 1.79x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 477 ms: 1.52x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                   |
| deepcopy                   | 371 us                                                 | 255 us: 1.45x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 30.3 us: 1.34x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.25x faster                                                  |
| async_generators           | 463 ms                                                 | 380 ms: 1.22x faster                                                   |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                  |
| spectral_norm              | 115 ms                                                 | 96.6 ms: 1.19x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.44 us: 1.19x faster                                                  |
| logging_format             | 7.23 us                                                | 6.11 us: 1.18x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.97 sec: 1.18x faster                                                 |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                   |
| float                      | 84.7 ms                                                | 72.3 ms: 1.17x faster                                                  |
| go                         | 139 ms                                                 | 119 ms: 1.17x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 146 ms: 1.16x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 138 ms: 1.16x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.22 ms: 1.15x faster                                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 128 ms: 1.14x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 71.7 ms: 1.14x faster                                                  |
| chaos                      | 67.0 ms                                                | 58.7 ms: 1.14x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.4 ms: 1.14x faster                                                  |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                                   |
| sympy_str                  | 300 ms                                                 | 264 ms: 1.13x faster                                                   |
| scimark_fft                | 382 ms                                                 | 344 ms: 1.11x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 96.4 ms: 1.11x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.27 ms: 1.11x faster                                                  |
| django_template            | 34.6 ms                                                | 31.3 ms: 1.10x faster                                                  |
| generators                 | 31.2 ms                                                | 28.5 ms: 1.09x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.7 ms: 1.09x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 712 ms: 1.09x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 69.3 ms: 1.08x faster                                                  |
| 2to3                       | 274 ms                                                 | 253 ms: 1.08x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.68 ms: 1.08x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 102 ms: 1.08x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 63.7 ms: 1.08x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                  |
| pyflate                    | 482 ms                                                 | 450 ms: 1.07x faster                                                   |
| sqlglot_transpile          | 1.68 ms                                                | 1.57 ms: 1.07x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                 |
| sympy_expand               | 478 ms                                                 | 447 ms: 1.07x faster                                                   |
| mdp                        | 2.63 sec                                               | 2.46 sec: 1.07x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 83.6 ms: 1.07x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 51.5 ms: 1.06x faster                                                  |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 58.4 ms: 1.06x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.05x faster                                                   |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.05x faster                                                   |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                 |
| nqueens                    | 83.3 ms                                                | 80.3 ms: 1.04x faster                                                  |
| fannkuch                   | 417 ms                                                 | 404 ms: 1.03x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                                  |
| nbody                      | 97.0 ms                                                | 94.3 ms: 1.03x faster                                                  |
| json                       | 5.26 ms                                                | 5.14 ms: 1.02x faster                                                  |
| mako                       | 11.9 ms                                                | 11.6 ms: 1.02x faster                                                  |
| richards                   | 45.8 ms                                                | 44.9 ms: 1.02x faster                                                  |
| richards_super             | 51.5 ms                                                | 50.8 ms: 1.01x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.32 ms: 1.01x faster                                                  |
| typing_runtime_protocols   | 158 us                                                 | 156 us: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 118 ms: 1.00x faster                                                   |
| json_loads                 | 28.5 us                                                | 28.6 us: 1.00x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 860 us: 1.02x slower                                                   |
| regex_dna                  | 212 ms                                                 | 218 ms: 1.03x slower                                                   |
| coroutines                 | 23.2 ms                                                | 24.0 ms: 1.03x slower                                                  |
| logging_silent             | 104 ns                                                 | 110 ns: 1.05x slower                                                   |
| telco                      | 7.10 ms                                                | 7.78 ms: 1.10x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.9 ms: 1.15x slower                                                  |
| coverage                   | 72.7 ms                                                | 92.0 ms: 1.27x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.94 ms: 1.30x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.1 ms: 3.38x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (2): pickle_pure_python, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250129-3.14.0a4+-5ff2fbc/bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.113x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.09x