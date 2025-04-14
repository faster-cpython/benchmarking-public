# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_generators_alt
- machine: linux-x86_64
- commit hash: 1593845
- commit date: 2025-02-04
- overall geometric mean: 1.109x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 261 ms: 1.05x faster                                                      |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 625 ms: 1.89x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 628 ms: 1.84x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 329 ms: 1.75x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 256 ms: 1.75x faster                                                      |
| async_tree_none            | 472 ms                                                 | 269 ms: 1.75x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 487 ms: 1.49x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 499 ms: 1.46x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.71x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 67.6 ms: 1.25x faster                                                     |
| nbody          | 97.0 ms                                                | 90.0 ms: 1.08x faster                                                     |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.11x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 2.98 ms: 1.21x faster                                                     |
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                      |
| regex_dna      | 212 ms                                                 | 194 ms: 1.09x faster                                                      |
| regex_v8       | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.10x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.82 sec: 1.28x faster                                                    |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.15x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 201 us: 1.14x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 79.3 ms: 1.12x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 95.2 ms: 1.12x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 56.4 ms: 1.09x faster                                                     |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.02x faster                                                      |
| json_loads           | 28.5 us                                                | 28.7 us: 1.01x slower                                                     |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.09x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                     |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.00 ms: 1.19x faster                                                    |
| django_template | 34.6 ms                                                | 33.1 ms: 1.05x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 625 ms: 1.89x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 628 ms: 1.84x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 329 ms: 1.75x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 256 ms: 1.75x faster                                                      |
| async_tree_none            | 472 ms                                                 | 269 ms: 1.75x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 487 ms: 1.49x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 499 ms: 1.46x faster                                                      |
| deepcopy                   | 371 us                                                 | 271 us: 1.37x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 30.2 us: 1.35x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.82 sec: 1.28x faster                                                    |
| comprehensions             | 21.8 us                                                | 17.2 us: 1.27x faster                                                     |
| float                      | 84.7 ms                                                | 67.6 ms: 1.25x faster                                                     |
| scimark_fft                | 382 ms                                                 | 310 ms: 1.23x faster                                                      |
| spectral_norm              | 115 ms                                                 | 93.4 ms: 1.23x faster                                                     |
| regex_effbot               | 3.61 ms                                                | 2.98 ms: 1.21x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 2.77 us: 1.21x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                     |
| mako                       | 11.9 ms                                                | 10.00 ms: 1.19x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 63.3 ms: 1.19x faster                                                     |
| logging_format             | 7.23 us                                                | 6.13 us: 1.18x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 70.1 ms: 1.17x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.60 us: 1.15x faster                                                     |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.15x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 201 us: 1.14x faster                                                      |
| chaos                      | 67.0 ms                                                | 59.3 ms: 1.13x faster                                                     |
| scimark_sor                | 129 ms                                                 | 115 ms: 1.13x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 79.3 ms: 1.12x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 95.2 ms: 1.12x faster                                                     |
| async_generators           | 463 ms                                                 | 413 ms: 1.12x faster                                                      |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                      |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                     |
| go                         | 139 ms                                                 | 126 ms: 1.11x faster                                                      |
| sympy_sum                  | 169 ms                                                 | 154 ms: 1.10x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 56.4 ms: 1.09x faster                                                     |
| regex_dna                  | 212 ms                                                 | 194 ms: 1.09x faster                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.63 ms: 1.09x faster                                                     |
| nbody                      | 97.0 ms                                                | 90.0 ms: 1.08x faster                                                     |
| sympy_str                  | 300 ms                                                 | 278 ms: 1.08x faster                                                      |
| raytrace                   | 312 ms                                                 | 290 ms: 1.08x faster                                                      |
| fannkuch                   | 417 ms                                                 | 391 ms: 1.07x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                                     |
| generators                 | 31.2 ms                                                | 29.6 ms: 1.06x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.52 ms: 1.06x faster                                                     |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                     |
| 2to3                       | 274 ms                                                 | 261 ms: 1.05x faster                                                      |
| pyflate                    | 482 ms                                                 | 460 ms: 1.05x faster                                                      |
| sympy_integrate            | 21.4 ms                                                | 20.4 ms: 1.05x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 740 ms: 1.05x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.05x faster                                                    |
| django_template            | 34.6 ms                                                | 33.1 ms: 1.05x faster                                                     |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                      |
| richards                   | 45.8 ms                                                | 44.2 ms: 1.04x faster                                                     |
| mdp                        | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                    |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                      |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                    |
| sqlite_synth               | 2.83 us                                                | 2.76 us: 1.03x faster                                                     |
| richards_super             | 51.5 ms                                                | 50.2 ms: 1.03x faster                                                     |
| json                       | 5.26 ms                                                | 5.13 ms: 1.03x faster                                                     |
| sympy_expand               | 478 ms                                                 | 469 ms: 1.02x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.02x faster                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 54.0 ms: 1.02x faster                                                     |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                      |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| json_loads                 | 28.5 us                                                | 28.7 us: 1.01x slower                                                     |
| dulwich_log                | 68.5 ms                                                | 69.2 ms: 1.01x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                     |
| coroutines                 | 23.2 ms                                                | 23.7 ms: 1.02x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                      |
| pycparser                  | 1.18 sec                                               | 1.22 sec: 1.03x slower                                                    |
| regex_v8                   | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                     |
| bench_thread_pool          | 842 us                                                 | 894 us: 1.06x slower                                                      |
| logging_silent             | 104 ns                                                 | 111 ns: 1.06x slower                                                      |
| nqueens                    | 83.3 ms                                                | 88.7 ms: 1.07x slower                                                     |
| telco                      | 7.10 ms                                                | 7.59 ms: 1.07x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.09x slower                                                     |
| hexiom                     | 6.41 ms                                                | 7.39 ms: 1.15x slower                                                     |
| coverage                   | 72.7 ms                                                | 89.6 ms: 1.23x slower                                                     |
| gc_traversal               | 3.79 ms                                                | 4.94 ms: 1.30x slower                                                     |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 81.2 ms: 3.38x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250204-3.14.0a4+-1593845-JIT/bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.109x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.10x