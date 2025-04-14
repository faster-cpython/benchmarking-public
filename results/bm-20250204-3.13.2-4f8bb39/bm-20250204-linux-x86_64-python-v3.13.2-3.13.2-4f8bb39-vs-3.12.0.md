# Results vs. 3.12.0

- fork: python
- ref: v3.13.2
- machine: linux-x86_64
- commit hash: 4f8bb39
- commit date: 2025-02-04
- overall geometric mean: 1.056x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 266 ms: 1.03x faster                                   |
| chameleon      | 7.41 ms                                                | 6.89 ms: 1.08x faster                                  |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                 |
| tornado_http   | 103 ms                                                 | 91.7 ms: 1.12x faster                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 312 ms: 1.44x faster                                   |
| async_tree_io              | 1.16 sec                                               | 843 ms: 1.37x faster                                   |
| async_tree_io_tg           | 1.18 sec                                               | 874 ms: 1.35x faster                                   |
| async_tree_none            | 472 ms                                                 | 352 ms: 1.34x faster                                   |
| async_tree_memoization     | 578 ms                                                 | 457 ms: 1.26x faster                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 455 ms: 1.26x faster                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 581 ms: 1.25x faster                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 599 ms: 1.21x faster                                   |
| Geometric mean             | (ref)                                                  | 1.31x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 87.8 ms: 1.10x faster                                  |
| float          | 84.7 ms                                                | 78.9 ms: 1.07x faster                                  |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 131 ms: 1.13x faster                                   |
| regex_effbot   | 3.61 ms                                                | 3.38 ms: 1.07x faster                                  |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                   |
| regex_v8       | 23.1 ms                                                | 26.4 ms: 1.14x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.11 sec: 1.10x faster                                 |
| json_loads           | 28.5 us                                                | 26.7 us: 1.07x faster                                  |
| pickle_pure_python   | 324 us                                                 | 304 us: 1.07x faster                                   |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                   |
| xml_etree_iterparse  | 107 ms                                                 | 103 ms: 1.04x faster                                   |
| xml_etree_generate   | 89.2 ms                                                | 86.2 ms: 1.03x faster                                  |
| xml_etree_parse      | 159 ms                                                 | 155 ms: 1.03x faster                                   |
| xml_etree_process    | 61.7 ms                                                | 60.5 ms: 1.02x faster                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.99 ms: 1.01x slower                                  |
| python_startup         | 9.55 ms                                                | 12.7 ms: 1.33x slower                                  |
| Geometric mean         | (ref)                                                  | 1.16x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.1 ms: 1.08x faster                                  |
| mako            | 11.9 ms                                                | 11.0 ms: 1.08x faster                                  |
| Geometric mean  | (ref)                                                  | 1.08x faster                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 312 ms: 1.44x faster                                   |
| async_tree_io              | 1.16 sec                                               | 843 ms: 1.37x faster                                   |
| async_tree_io_tg           | 1.18 sec                                               | 874 ms: 1.35x faster                                   |
| async_tree_none            | 472 ms                                                 | 352 ms: 1.34x faster                                   |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                  |
| async_tree_memoization     | 578 ms                                                 | 457 ms: 1.26x faster                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 455 ms: 1.26x faster                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 581 ms: 1.25x faster                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 599 ms: 1.21x faster                                   |
| async_generators           | 463 ms                                                 | 392 ms: 1.18x faster                                   |
| raytrace                   | 312 ms                                                 | 267 ms: 1.17x faster                                   |
| deltablue                  | 3.72 ms                                                | 3.18 ms: 1.17x faster                                  |
| chaos                      | 67.0 ms                                                | 59.0 ms: 1.13x faster                                  |
| regex_compile              | 148 ms                                                 | 131 ms: 1.13x faster                                   |
| logging_simple             | 6.46 us                                                | 5.72 us: 1.13x faster                                  |
| logging_format             | 7.23 us                                                | 6.43 us: 1.12x faster                                  |
| tornado_http               | 103 ms                                                 | 91.7 ms: 1.12x faster                                  |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.11x faster                                   |
| pathlib                    | 19.3 ms                                                | 17.4 ms: 1.11x faster                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.11x faster                                   |
| tomli_loads                | 2.33 sec                                               | 2.11 sec: 1.10x faster                                 |
| nbody                      | 97.0 ms                                                | 87.8 ms: 1.10x faster                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 68.2 ms: 1.10x faster                                  |
| crypto_pyaes               | 81.9 ms                                                | 74.6 ms: 1.10x faster                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.0 ms: 1.10x faster                                  |
| sympy_str                  | 300 ms                                                 | 273 ms: 1.10x faster                                   |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.08x faster                                  |
| django_template            | 34.6 ms                                                | 32.1 ms: 1.08x faster                                  |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                  |
| chameleon                  | 7.41 ms                                                | 6.89 ms: 1.08x faster                                  |
| float                      | 84.7 ms                                                | 78.9 ms: 1.07x faster                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                  |
| generators                 | 31.2 ms                                                | 29.2 ms: 1.07x faster                                  |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                 |
| regex_effbot               | 3.61 ms                                                | 3.38 ms: 1.07x faster                                  |
| json_loads                 | 28.5 us                                                | 26.7 us: 1.07x faster                                  |
| pickle_pure_python         | 324 us                                                 | 304 us: 1.07x faster                                   |
| nqueens                    | 83.3 ms                                                | 78.1 ms: 1.07x faster                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.07x faster                                  |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                   |
| scimark_fft                | 382 ms                                                 | 361 ms: 1.06x faster                                   |
| dulwich_log                | 68.5 ms                                                | 64.9 ms: 1.06x faster                                  |
| scimark_sor                | 129 ms                                                 | 123 ms: 1.05x faster                                   |
| pprint_safe_repr           | 776 ms                                                 | 737 ms: 1.05x faster                                   |
| deepcopy_memo              | 40.7 us                                                | 38.8 us: 1.05x faster                                  |
| logging_silent             | 104 ns                                                 | 100 ns: 1.04x faster                                   |
| fannkuch                   | 417 ms                                                 | 400 ms: 1.04x faster                                   |
| deepcopy_reduce            | 3.35 us                                                | 3.21 us: 1.04x faster                                  |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                 |
| xml_etree_iterparse        | 107 ms                                                 | 103 ms: 1.04x faster                                   |
| gunicorn                   | 1.24 ms                                                | 1.20 ms: 1.04x faster                                  |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.04x faster                                   |
| xml_etree_generate         | 89.2 ms                                                | 86.2 ms: 1.03x faster                                  |
| bench_thread_pool          | 842 us                                                 | 815 us: 1.03x faster                                   |
| hexiom                     | 6.41 ms                                                | 6.21 ms: 1.03x faster                                  |
| sympy_expand               | 478 ms                                                 | 463 ms: 1.03x faster                                   |
| coroutines                 | 23.2 ms                                                | 22.4 ms: 1.03x faster                                  |
| deepcopy                   | 371 us                                                 | 360 us: 1.03x faster                                   |
| 2to3                       | 274 ms                                                 | 266 ms: 1.03x faster                                   |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                   |
| mdp                        | 2.63 sec                                               | 2.56 sec: 1.03x faster                                 |
| xml_etree_parse            | 159 ms                                                 | 155 ms: 1.03x faster                                   |
| json                       | 5.26 ms                                                | 5.13 ms: 1.03x faster                                  |
| xml_etree_process          | 61.7 ms                                                | 60.5 ms: 1.02x faster                                  |
| pyflate                    | 482 ms                                                 | 474 ms: 1.02x faster                                   |
| sqlglot_optimize           | 54.8 ms                                                | 53.9 ms: 1.02x faster                                  |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.01x faster                                 |
| sqlglot_normalize          | 110 ms                                                 | 110 ms: 1.01x faster                                   |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                   |
| python_startup_no_site     | 6.94 ms                                                | 6.99 ms: 1.01x slower                                  |
| go                         | 139 ms                                                 | 141 ms: 1.01x slower                                   |
| typing_runtime_protocols   | 158 us                                                 | 161 us: 1.02x slower                                   |
| sqlite_synth               | 2.83 us                                                | 2.90 us: 1.02x slower                                  |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                   |
| richards                   | 45.8 ms                                                | 47.8 ms: 1.04x slower                                  |
| richards_super             | 51.5 ms                                                | 55.1 ms: 1.07x slower                                  |
| regex_v8                   | 23.1 ms                                                | 26.4 ms: 1.14x slower                                  |
| coverage                   | 72.7 ms                                                | 84.8 ms: 1.17x slower                                  |
| telco                      | 7.10 ms                                                | 8.62 ms: 1.21x slower                                  |
| gc_traversal               | 3.79 ms                                                | 4.65 ms: 1.22x slower                                  |
| python_startup             | 9.55 ms                                                | 12.7 ms: 1.33x slower                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.44 ms: 1.65x slower                                  |
| Geometric mean             | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (5): json_dumps, bench_mp_pool, asyncio_websockets, scimark_sparse_mat_mult, scimark_lu
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20250204-3.13.2-4f8bb39/bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, gevent_hub, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.056x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.07x