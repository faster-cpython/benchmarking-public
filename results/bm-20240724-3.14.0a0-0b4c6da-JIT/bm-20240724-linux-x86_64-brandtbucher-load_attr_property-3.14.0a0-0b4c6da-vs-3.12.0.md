# Results vs. 3.12.0

- fork: brandtbucher
- ref: load_attr_property
- machine: linux-x86_64
- commit hash: 0b4c6da
- commit date: 2024-07-24
- overall geometric mean: 1.08x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 271 ms: 1.01x faster                                                      |
| docutils       | 2.77 sec                                               | 2.90 sec: 1.05x slower                                                    |
| tornado_http   | 103 ms                                                 | 92.9 ms: 1.10x faster                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 304 ms: 1.48x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                                      |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 528 ms: 1.37x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 875 ms: 1.35x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 428 ms: 1.35x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 560 ms: 1.30x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 905 ms: 1.28x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.7 ms: 1.20x faster                                                     |
| nbody          | 97.0 ms                                                | 81.0 ms: 1.20x faster                                                     |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.13x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 134 ms: 1.11x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.90 ms: 1.08x slower                                                     |
| regex_dna      | 212 ms                                                 | 230 ms: 1.08x slower                                                      |
| regex_v8       | 23.1 ms                                                | 26.3 ms: 1.14x slower                                                     |
| Geometric mean | (ref)                                                  | 1.05x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.20x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 80.6 ms: 1.11x faster                                                     |
| pickle_pure_python   | 324 us                                                 | 295 us: 1.10x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 56.9 ms: 1.08x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 98.6 ms: 1.08x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                              |

Benchmark hidden because not significant (2): json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.17 ms: 1.03x slower                                                     |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.96 ms: 1.19x faster                                                     |
| django_template | 34.6 ms                                                | 35.9 ms: 1.04x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 304 ms: 1.48x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 393 ms: 1.46x faster                                                      |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 28.4 us: 1.43x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 528 ms: 1.37x faster                                                      |
| deepcopy                   | 371 us                                                 | 274 us: 1.35x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 875 ms: 1.35x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 428 ms: 1.35x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 560 ms: 1.30x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 905 ms: 1.28x faster                                                      |
| scimark_fft                | 382 ms                                                 | 305 ms: 1.25x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 60.5 ms: 1.24x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 66.6 ms: 1.23x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 2.75 us: 1.22x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.20x faster                                                    |
| float                      | 84.7 ms                                                | 70.7 ms: 1.20x faster                                                     |
| nbody                      | 97.0 ms                                                | 81.0 ms: 1.20x faster                                                     |
| mako                       | 11.9 ms                                                | 9.96 ms: 1.19x faster                                                     |
| logging_format             | 7.23 us                                                | 6.08 us: 1.19x faster                                                     |
| raytrace                   | 312 ms                                                 | 266 ms: 1.17x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.54 us: 1.17x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.35 ms: 1.16x faster                                                     |
| richards                   | 45.8 ms                                                | 39.9 ms: 1.15x faster                                                     |
| chaos                      | 67.0 ms                                                | 58.3 ms: 1.15x faster                                                     |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.14x faster                                                      |
| fannkuch                   | 417 ms                                                 | 374 ms: 1.12x faster                                                      |
| regex_compile              | 148 ms                                                 | 134 ms: 1.11x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 80.6 ms: 1.11x faster                                                     |
| richards_super             | 51.5 ms                                                | 46.6 ms: 1.11x faster                                                     |
| tornado_http               | 103 ms                                                 | 92.9 ms: 1.10x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 702 ms: 1.10x faster                                                      |
| generators                 | 31.2 ms                                                | 28.3 ms: 1.10x faster                                                     |
| pyflate                    | 482 ms                                                 | 438 ms: 1.10x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 295 us: 1.10x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 56.9 ms: 1.08x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 98.6 ms: 1.08x faster                                                     |
| sqlglot_parse              | 1.36 ms                                                | 1.26 ms: 1.08x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                    |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.06x faster                                                     |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.54 ms: 1.05x faster                                                     |
| mdp                        | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                    |
| async_generators           | 463 ms                                                 | 450 ms: 1.03x faster                                                      |
| dask                       | 372 ms                                                 | 362 ms: 1.03x faster                                                      |
| logging_silent             | 104 ns                                                 | 102 ns: 1.03x faster                                                      |
| sympy_str                  | 300 ms                                                 | 293 ms: 1.02x faster                                                      |
| json                       | 5.26 ms                                                | 5.15 ms: 1.02x faster                                                     |
| bench_thread_pool          | 842 us                                                 | 825 us: 1.02x faster                                                      |
| scimark_sor                | 129 ms                                                 | 127 ms: 1.01x faster                                                      |
| dulwich_log                | 68.5 ms                                                | 67.7 ms: 1.01x faster                                                     |
| 2to3                       | 274 ms                                                 | 271 ms: 1.01x faster                                                      |
| sympy_sum                  | 169 ms                                                 | 167 ms: 1.01x faster                                                      |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                     |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                    |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                      |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 56.0 ms: 1.02x slower                                                     |
| hexiom                     | 6.41 ms                                                | 6.55 ms: 1.02x slower                                                     |
| gc_traversal               | 3.79 ms                                                | 3.89 ms: 1.02x slower                                                     |
| asyncio_tcp                | 491 ms                                                 | 504 ms: 1.03x slower                                                      |
| go                         | 139 ms                                                 | 144 ms: 1.03x slower                                                      |
| sympy_integrate            | 21.4 ms                                                | 22.1 ms: 1.03x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 7.17 ms: 1.03x slower                                                     |
| django_template            | 34.6 ms                                                | 35.9 ms: 1.04x slower                                                     |
| sympy_expand               | 478 ms                                                 | 498 ms: 1.04x slower                                                      |
| nqueens                    | 83.3 ms                                                | 87.0 ms: 1.05x slower                                                     |
| docutils                   | 2.77 sec                                               | 2.90 sec: 1.05x slower                                                    |
| scimark_lu                 | 118 ms                                                 | 125 ms: 1.06x slower                                                      |
| regex_effbot               | 3.61 ms                                                | 3.90 ms: 1.08x slower                                                     |
| regex_dna                  | 212 ms                                                 | 230 ms: 1.08x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 171 us: 1.09x slower                                                      |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                     |
| telco                      | 7.10 ms                                                | 7.89 ms: 1.11x slower                                                     |
| regex_v8                   | 23.1 ms                                                | 26.3 ms: 1.14x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                                     |
| coverage                   | 72.7 ms                                                | 92.3 ms: 1.27x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                              |

Benchmark hidden because not significant (4): json_loads, pycparser, bench_mp_pool, json_dumps
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240724-3.14.0a0-0b4c6da-JIT/bm-20240724-linux-x86_64-brandtbucher-load_attr_property-3.14.0a0-0b4c6da.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.05x