# Results vs. 3.12.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: linux-x86_64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.144x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 250 ms: 1.10x faster                                                   |
| docutils       | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 594 ms: 1.99x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 597 ms: 1.94x faster                                                   |
| async_tree_none            | 472 ms                                                 | 251 ms: 1.88x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 308 ms: 1.87x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 307 ms: 1.87x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 241 ms: 1.86x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 474 ms: 1.53x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 482 ms: 1.51x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.80x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 67.6 ms: 1.25x faster                                                  |
| nbody          | 97.0 ms                                                | 89.3 ms: 1.09x faster                                                  |
| pidigits       | 187 ms                                                 | 202 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 124 ms: 1.19x faster                                                   |
| regex_dna      | 212 ms                                                 | 194 ms: 1.09x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.40 ms: 1.06x faster                                                  |
| regex_v8       | 23.1 ms                                                | 26.1 ms: 1.13x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.90 sec: 1.23x faster                                                 |
| unpickle_list        | 5.29 us                                                | 4.46 us: 1.19x faster                                                  |
| unpickle             | 15.9 us                                                | 14.0 us: 1.13x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 58.5 ms: 1.06x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 85.1 ms: 1.05x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 102 ms: 1.04x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 312 us: 1.04x faster                                                   |
| pickle_dict          | 35.5 us                                                | 35.1 us: 1.01x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 162 ms: 1.02x slower                                                   |
| pickle_list          | 5.08 us                                                | 5.19 us: 1.02x slower                                                  |
| json_loads           | 28.5 us                                                | 30.0 us: 1.05x slower                                                  |
| json_dumps           | 10.4 ms                                                | 12.1 ms: 1.16x slower                                                  |
| pickle               | 11.6 us                                                | 13.6 us: 1.17x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.99 ms: 1.01x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 30.3 ms: 1.14x faster                                                  |
| mako            | 11.9 ms                                                | 11.7 ms: 1.01x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 594 ms: 1.99x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 597 ms: 1.94x faster                                                   |
| async_tree_none            | 472 ms                                                 | 251 ms: 1.88x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 308 ms: 1.87x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 307 ms: 1.87x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 241 ms: 1.86x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 474 ms: 1.53x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 482 ms: 1.51x faster                                                   |
| deepcopy                   | 371 us                                                 | 247 us: 1.50x faster                                                   |
| comprehensions             | 21.8 us                                                | 15.5 us: 1.41x faster                                                  |
| spectral_norm              | 115 ms                                                 | 82.3 ms: 1.40x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.7 us: 1.37x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.50 us: 1.34x faster                                                  |
| scimark_fft                | 382 ms                                                 | 295 ms: 1.30x faster                                                   |
| pathlib                    | 19.3 ms                                                | 15.1 ms: 1.28x faster                                                  |
| float                      | 84.7 ms                                                | 67.6 ms: 1.25x faster                                                  |
| deltablue                  | 3.72 ms                                                | 2.98 ms: 1.25x faster                                                  |
| go                         | 139 ms                                                 | 113 ms: 1.24x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.11 ms: 1.23x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.90 sec: 1.23x faster                                                 |
| chaos                      | 67.0 ms                                                | 54.6 ms: 1.23x faster                                                  |
| async_generators           | 463 ms                                                 | 378 ms: 1.22x faster                                                   |
| logging_format             | 7.23 us                                                | 5.94 us: 1.22x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 61.8 ms: 1.22x faster                                                  |
| raytrace                   | 312 ms                                                 | 259 ms: 1.21x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.37 us: 1.20x faster                                                  |
| regex_compile              | 148 ms                                                 | 124 ms: 1.19x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 142 ms: 1.19x faster                                                   |
| unpickle_list              | 5.29 us                                                | 4.46 us: 1.19x faster                                                  |
| scimark_sor                | 129 ms                                                 | 109 ms: 1.18x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 125 ms: 1.17x faster                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.1 ms: 1.16x faster                                                  |
| sympy_str                  | 300 ms                                                 | 258 ms: 1.16x faster                                                   |
| logging_silent             | 104 ns                                                 | 90.3 ns: 1.16x faster                                                  |
| pyflate                    | 482 ms                                                 | 420 ms: 1.15x faster                                                   |
| django_template            | 34.6 ms                                                | 30.3 ms: 1.14x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 71.9 ms: 1.14x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 18.9 ms: 1.13x faster                                                  |
| unpickle                   | 15.9 us                                                | 14.0 us: 1.13x faster                                                  |
| nqueens                    | 83.3 ms                                                | 73.9 ms: 1.13x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.21 ms: 1.13x faster                                                  |
| richards                   | 45.8 ms                                                | 40.8 ms: 1.12x faster                                                  |
| generators                 | 31.2 ms                                                | 27.9 ms: 1.12x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.51 ms: 1.12x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 62.2 ms: 1.10x faster                                                  |
| 2to3                       | 274 ms                                                 | 250 ms: 1.10x faster                                                   |
| regex_dna                  | 212 ms                                                 | 194 ms: 1.09x faster                                                   |
| nbody                      | 97.0 ms                                                | 89.3 ms: 1.09x faster                                                  |
| sympy_expand               | 478 ms                                                 | 441 ms: 1.08x faster                                                   |
| richards_super             | 51.5 ms                                                | 47.6 ms: 1.08x faster                                                  |
| typing_runtime_protocols   | 158 us                                                 | 146 us: 1.08x faster                                                   |
| hexiom                     | 6.41 ms                                                | 5.94 ms: 1.08x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                 |
| unpack_sequence            | 54.0 ns                                                | 50.1 ns: 1.08x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 103 ms: 1.07x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.65 us: 1.07x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 110 ms: 1.07x faster                                                   |
| coroutines                 | 23.2 ms                                                | 21.8 ms: 1.06x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.40 ms: 1.06x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 51.8 ms: 1.06x faster                                                  |
| fannkuch                   | 417 ms                                                 | 395 ms: 1.06x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 58.5 ms: 1.06x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 737 ms: 1.05x faster                                                   |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 85.1 ms: 1.05x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.04x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 102 ms: 1.04x faster                                                   |
| asyncio_tcp                | 491 ms                                                 | 471 ms: 1.04x faster                                                   |
| pickle_pure_python         | 324 us                                                 | 312 us: 1.04x faster                                                   |
| bench_thread_pool          | 842 us                                                 | 821 us: 1.03x faster                                                   |
| mako                       | 11.9 ms                                                | 11.7 ms: 1.01x faster                                                  |
| meteor_contest             | 112 ms                                                 | 111 ms: 1.01x faster                                                   |
| pickle_dict                | 35.5 us                                                | 35.1 us: 1.01x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.00x faster                                                 |
| python_startup_no_site     | 6.94 ms                                                | 6.99 ms: 1.01x slower                                                  |
| xml_etree_parse            | 159 ms                                                 | 162 ms: 1.02x slower                                                   |
| pickle_list                | 5.08 us                                                | 5.19 us: 1.02x slower                                                  |
| telco                      | 7.10 ms                                                | 7.31 ms: 1.03x slower                                                  |
| json                       | 5.26 ms                                                | 5.45 ms: 1.04x slower                                                  |
| mdp                        | 2.63 sec                                               | 2.77 sec: 1.05x slower                                                 |
| json_loads                 | 28.5 us                                                | 30.0 us: 1.05x slower                                                  |
| pidigits                   | 187 ms                                                 | 202 ms: 1.08x slower                                                   |
| coverage                   | 72.7 ms                                                | 79.8 ms: 1.10x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 26.1 ms: 1.13x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 12.1 ms: 1.16x slower                                                  |
| pickle                     | 11.6 us                                                | 13.6 us: 1.17x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 5.01 ms: 1.32x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.50 ms: 1.69x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 80.0 ms: 3.33x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.12x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.144x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.10x