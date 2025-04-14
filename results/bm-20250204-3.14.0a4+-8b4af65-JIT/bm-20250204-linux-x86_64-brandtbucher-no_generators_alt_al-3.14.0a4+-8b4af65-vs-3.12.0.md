# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_generators_alt_al
- machine: linux-x86_64
- commit hash: 8b4af65
- commit date: 2025-02-04
- overall geometric mean: 1.115x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 258 ms: 1.06x faster                                                         |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 618 ms: 1.91x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 627 ms: 1.84x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 255 ms: 1.77x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 330 ms: 1.75x faster                                                         |
| async_tree_none            | 472 ms                                                 | 270 ms: 1.75x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.52x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 67.6 ms: 1.25x faster                                                        |
| nbody          | 97.0 ms                                                | 90.8 ms: 1.07x faster                                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 2.99 ms: 1.21x faster                                                        |
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                         |
| regex_dna      | 212 ms                                                 | 195 ms: 1.09x faster                                                         |
| regex_v8       | 23.1 ms                                                | 23.8 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.81 sec: 1.28x faster                                                       |
| xml_etree_parse      | 159 ms                                                 | 138 ms: 1.16x faster                                                         |
| xml_etree_generate   | 89.2 ms                                                | 77.7 ms: 1.15x faster                                                        |
| unpickle_pure_python | 230 us                                                 | 202 us: 1.14x faster                                                         |
| xml_etree_process    | 61.7 ms                                                | 55.0 ms: 1.12x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 95.6 ms: 1.12x faster                                                        |
| json_loads           | 28.5 us                                                | 28.7 us: 1.01x slower                                                        |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                                 |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                        |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.98 ms: 1.19x faster                                                        |
| django_template | 34.6 ms                                                | 33.1 ms: 1.05x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 618 ms: 1.91x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 627 ms: 1.84x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 255 ms: 1.77x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 330 ms: 1.75x faster                                                         |
| async_tree_none            | 472 ms                                                 | 270 ms: 1.75x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.52x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                                         |
| deepcopy                   | 371 us                                                 | 271 us: 1.37x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 30.5 us: 1.33x faster                                                        |
| comprehensions             | 21.8 us                                                | 16.9 us: 1.29x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.81 sec: 1.28x faster                                                       |
| float                      | 84.7 ms                                                | 67.6 ms: 1.25x faster                                                        |
| scimark_fft                | 382 ms                                                 | 310 ms: 1.23x faster                                                         |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.76 us: 1.21x faster                                                        |
| regex_effbot               | 3.61 ms                                                | 2.99 ms: 1.21x faster                                                        |
| spectral_norm              | 115 ms                                                 | 95.2 ms: 1.21x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 62.8 ms: 1.20x faster                                                        |
| mako                       | 11.9 ms                                                | 9.98 ms: 1.19x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 138 ms: 1.16x faster                                                         |
| crypto_pyaes               | 81.9 ms                                                | 71.0 ms: 1.15x faster                                                        |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                         |
| xml_etree_generate         | 89.2 ms                                                | 77.7 ms: 1.15x faster                                                        |
| async_generators           | 463 ms                                                 | 405 ms: 1.14x faster                                                         |
| unpickle_pure_python       | 230 us                                                 | 202 us: 1.14x faster                                                         |
| scimark_sor                | 129 ms                                                 | 115 ms: 1.13x faster                                                         |
| xml_etree_process          | 61.7 ms                                                | 55.0 ms: 1.12x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.76 us: 1.12x faster                                                        |
| logging_format             | 7.23 us                                                | 6.46 us: 1.12x faster                                                        |
| chaos                      | 67.0 ms                                                | 59.8 ms: 1.12x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 95.6 ms: 1.12x faster                                                        |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.11x faster                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.55 ms: 1.11x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.11x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.11x faster                                                        |
| go                         | 139 ms                                                 | 126 ms: 1.10x faster                                                         |
| generators                 | 31.2 ms                                                | 28.4 ms: 1.10x faster                                                        |
| regex_dna                  | 212 ms                                                 | 195 ms: 1.09x faster                                                         |
| raytrace                   | 312 ms                                                 | 287 ms: 1.09x faster                                                         |
| sympy_str                  | 300 ms                                                 | 277 ms: 1.08x faster                                                         |
| fannkuch                   | 417 ms                                                 | 390 ms: 1.07x faster                                                         |
| nbody                      | 97.0 ms                                                | 90.8 ms: 1.07x faster                                                        |
| 2to3                       | 274 ms                                                 | 258 ms: 1.06x faster                                                         |
| deltablue                  | 3.72 ms                                                | 3.50 ms: 1.06x faster                                                        |
| pyflate                    | 482 ms                                                 | 454 ms: 1.06x faster                                                         |
| mdp                        | 2.63 sec                                               | 2.49 sec: 1.06x faster                                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                        |
| nqueens                    | 83.3 ms                                                | 79.6 ms: 1.05x faster                                                        |
| sympy_integrate            | 21.4 ms                                                | 20.5 ms: 1.05x faster                                                        |
| django_template            | 34.6 ms                                                | 33.1 ms: 1.05x faster                                                        |
| sqlglot_normalize          | 110 ms                                                 | 105 ms: 1.05x faster                                                         |
| richards                   | 45.8 ms                                                | 43.9 ms: 1.05x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 745 ms: 1.04x faster                                                         |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                         |
| sqlite_synth               | 2.83 us                                                | 2.73 us: 1.04x faster                                                        |
| dulwich_log                | 68.5 ms                                                | 66.3 ms: 1.03x faster                                                        |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                                         |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                       |
| coroutines                 | 23.2 ms                                                | 22.5 ms: 1.03x faster                                                        |
| richards_super             | 51.5 ms                                                | 50.1 ms: 1.03x faster                                                        |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.03x faster                                                       |
| sqlglot_optimize           | 54.8 ms                                                | 53.4 ms: 1.03x faster                                                        |
| sympy_expand               | 478 ms                                                 | 472 ms: 1.01x faster                                                         |
| json                       | 5.26 ms                                                | 5.19 ms: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| json_loads                 | 28.5 us                                                | 28.7 us: 1.01x slower                                                        |
| pycparser                  | 1.18 sec                                               | 1.19 sec: 1.01x slower                                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 23.8 ms: 1.03x slower                                                        |
| bench_thread_pool          | 842 us                                                 | 874 us: 1.04x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.04x slower                                                         |
| logging_silent             | 104 ns                                                 | 110 ns: 1.06x slower                                                         |
| telco                      | 7.10 ms                                                | 7.61 ms: 1.07x slower                                                        |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.08x slower                                                        |
| hexiom                     | 6.41 ms                                                | 7.26 ms: 1.13x slower                                                        |
| coverage                   | 72.7 ms                                                | 89.6 ms: 1.23x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 4.93 ms: 1.30x slower                                                        |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.66x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 80.3 ms: 3.34x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                 |

Benchmark hidden because not significant (2): pickle_pure_python, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250204-3.14.0a4+-8b4af65-JIT/bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-8b4af65.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.115x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.10x