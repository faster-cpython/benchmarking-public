# Results vs. 3.12.0

- fork: python
- ref: v3.14.0b2
- machine: linux-x86_64
- commit hash: 12d3f88
- commit date: 2025-05-26
- overall geometric mean: 1.112x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 258 ms: 1.06x faster                                       |
| docutils       | 2.77 sec                                               | 2.58 sec: 1.07x faster                                     |
| Geometric mean | (ref)                                                  | 1.07x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 595 ms: 1.94x faster                                       |
| async_tree_io_tg           | 1.18 sec                                               | 613 ms: 1.93x faster                                       |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.84x faster                                       |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                       |
| async_tree_none            | 472 ms                                                 | 265 ms: 1.78x faster                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 482 ms: 1.50x faster                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 491 ms: 1.48x faster                                       |
| Geometric mean             | (ref)                                                  | 1.76x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.7 ms: 1.20x faster                                      |
| nbody          | 97.0 ms                                                | 101 ms: 1.04x slower                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 2.93 ms: 1.23x faster                                      |
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                       |
| regex_dna      | 212 ms                                                 | 194 ms: 1.09x faster                                       |
| regex_v8       | 23.1 ms                                                | 22.5 ms: 1.03x faster                                      |
| Geometric mean | (ref)                                                  | 1.13x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.02 sec: 1.15x faster                                     |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                       |
| xml_etree_iterparse  | 107 ms                                                 | 98.9 ms: 1.08x faster                                      |
| xml_etree_generate   | 89.2 ms                                                | 85.2 ms: 1.05x faster                                      |
| unpickle_pure_python | 230 us                                                 | 223 us: 1.03x faster                                       |
| xml_etree_process    | 61.7 ms                                                | 61.0 ms: 1.01x faster                                      |
| json_loads           | 28.5 us                                                | 30.2 us: 1.06x slower                                      |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                      |
| Geometric mean       | (ref)                                                  | 1.03x faster                                               |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.91 ms: 1.00x faster                                      |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                      |
| Geometric mean         | (ref)                                                  | 1.17x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.5 ms: 1.07x faster                                      |
| mako            | 11.9 ms                                                | 11.4 ms: 1.05x faster                                      |
| Geometric mean  | (ref)                                                  | 1.06x faster                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.12x faster                                     |
| async_tree_io              | 1.16 sec                                               | 595 ms: 1.94x faster                                       |
| async_tree_io_tg           | 1.18 sec                                               | 613 ms: 1.93x faster                                       |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.84x faster                                       |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                       |
| async_tree_none            | 472 ms                                                 | 265 ms: 1.78x faster                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 482 ms: 1.50x faster                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 491 ms: 1.48x faster                                       |
| deepcopy                   | 371 us                                                 | 255 us: 1.45x faster                                       |
| deepcopy_memo              | 40.7 us                                                | 29.6 us: 1.38x faster                                      |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.27x faster                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                      |
| regex_effbot               | 3.61 ms                                                | 2.93 ms: 1.23x faster                                      |
| go                         | 139 ms                                                 | 115 ms: 1.22x faster                                       |
| float                      | 84.7 ms                                                | 70.7 ms: 1.20x faster                                      |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                       |
| tomli_loads                | 2.33 sec                                               | 2.02 sec: 1.15x faster                                     |
| dulwich_log                | 68.5 ms                                                | 59.6 ms: 1.15x faster                                      |
| raytrace                   | 312 ms                                                 | 273 ms: 1.14x faster                                       |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                       |
| pathlib                    | 19.3 ms                                                | 17.1 ms: 1.13x faster                                      |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                       |
| sympy_integrate            | 21.4 ms                                                | 19.1 ms: 1.12x faster                                      |
| async_generators           | 463 ms                                                 | 413 ms: 1.12x faster                                       |
| chaos                      | 67.0 ms                                                | 60.1 ms: 1.11x faster                                      |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.11x faster                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 68.6 ms: 1.09x faster                                      |
| regex_dna                  | 212 ms                                                 | 194 ms: 1.09x faster                                       |
| crypto_pyaes               | 81.9 ms                                                | 75.0 ms: 1.09x faster                                      |
| sqlalchemy_declarative     | 147 ms                                                 | 135 ms: 1.09x faster                                       |
| deltablue                  | 3.72 ms                                                | 3.44 ms: 1.08x faster                                      |
| xml_etree_iterparse        | 107 ms                                                 | 98.9 ms: 1.08x faster                                      |
| logging_format             | 7.23 us                                                | 6.74 us: 1.07x faster                                      |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.07x faster                                       |
| docutils                   | 2.77 sec                                               | 2.58 sec: 1.07x faster                                     |
| pyflate                    | 482 ms                                                 | 451 ms: 1.07x faster                                       |
| spectral_norm              | 115 ms                                                 | 107 ms: 1.07x faster                                       |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.5 ms: 1.07x faster                                      |
| django_template            | 34.6 ms                                                | 32.5 ms: 1.07x faster                                      |
| 2to3                       | 274 ms                                                 | 258 ms: 1.06x faster                                       |
| richards                   | 45.8 ms                                                | 43.1 ms: 1.06x faster                                      |
| logging_simple             | 6.46 us                                                | 6.09 us: 1.06x faster                                      |
| pprint_safe_repr           | 776 ms                                                 | 738 ms: 1.05x faster                                       |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                       |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.05x faster                                      |
| xml_etree_generate         | 89.2 ms                                                | 85.2 ms: 1.05x faster                                      |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.04x faster                                     |
| richards_super             | 51.5 ms                                                | 49.4 ms: 1.04x faster                                      |
| hexiom                     | 6.41 ms                                                | 6.16 ms: 1.04x faster                                      |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                     |
| scimark_fft                | 382 ms                                                 | 369 ms: 1.03x faster                                       |
| sympy_expand               | 478 ms                                                 | 463 ms: 1.03x faster                                       |
| unpickle_pure_python       | 230 us                                                 | 223 us: 1.03x faster                                       |
| regex_v8                   | 23.1 ms                                                | 22.5 ms: 1.03x faster                                      |
| nqueens                    | 83.3 ms                                                | 81.8 ms: 1.02x faster                                      |
| xml_etree_process          | 61.7 ms                                                | 61.0 ms: 1.01x faster                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.01 ms: 1.01x faster                                      |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                       |
| python_startup_no_site     | 6.94 ms                                                | 6.91 ms: 1.00x faster                                      |
| sqlite_synth               | 2.83 us                                                | 2.88 us: 1.02x slower                                      |
| json                       | 5.26 ms                                                | 5.39 ms: 1.02x slower                                      |
| nbody                      | 97.0 ms                                                | 101 ms: 1.04x slower                                       |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                       |
| json_loads                 | 28.5 us                                                | 30.2 us: 1.06x slower                                      |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.08x slower                                      |
| coroutines                 | 23.2 ms                                                | 25.0 ms: 1.08x slower                                      |
| telco                      | 7.10 ms                                                | 7.92 ms: 1.12x slower                                      |
| coverage                   | 72.7 ms                                                | 88.0 ms: 1.21x slower                                      |
| gc_traversal               | 3.79 ms                                                | 4.96 ms: 1.31x slower                                      |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                      |
| create_gc_cycles           | 1.48 ms                                                | 2.58 ms: 1.75x slower                                      |
| logging_silent             | 104 ns                                                 | 473 ns: 4.53x slower                                       |
| Geometric mean             | (ref)                                                  | 1.09x faster                                               |

Benchmark hidden because not significant (5): pickle_pure_python, fannkuch, pidigits, generators, asyncio_websockets
Ignored benchmarks (20) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250526-3.14.0b2-12d3f88/bm-20250526-linux-x86_64-python-v3.14.0b2-3.14.0b2-12d3f88.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.112x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.13x