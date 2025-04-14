# Results vs. 3.12.0

- fork: python
- ref: 94cd2e0ddeff83dee325
- machine: linux-x86_64
- commit hash: 94cd2e0
- commit date: 2025-02-10
- overall geometric mean: 1.108x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 258 ms: 1.06x faster                                                   |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 622 ms: 1.90x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 627 ms: 1.84x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 319 ms: 1.80x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 328 ms: 1.76x faster                                                   |
| async_tree_none            | 472 ms                                                 | 269 ms: 1.75x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 260 ms: 1.73x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 484 ms: 1.50x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.71x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.9 ms: 1.21x faster                                                  |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| nbody          | 97.0 ms                                                | 96.6 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.09 ms: 1.17x faster                                                  |
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                   |
| regex_dna      | 212 ms                                                 | 209 ms: 1.02x faster                                                   |
| regex_v8       | 23.1 ms                                                | 24.1 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.85 sec: 1.26x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 137 ms: 1.17x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 201 us: 1.14x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 79.1 ms: 1.13x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 95.0 ms: 1.12x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 56.1 ms: 1.10x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 318 us: 1.02x faster                                                   |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                                  |
| json_dumps           | 10.4 ms                                                | 11.8 ms: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.83 ms: 1.21x faster                                                  |
| django_template | 34.6 ms                                                | 32.1 ms: 1.08x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 622 ms: 1.90x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 627 ms: 1.84x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 319 ms: 1.80x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 328 ms: 1.76x faster                                                   |
| async_tree_none            | 472 ms                                                 | 269 ms: 1.75x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 260 ms: 1.73x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 484 ms: 1.50x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                   |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 30.7 us: 1.33x faster                                                  |
| comprehensions             | 21.8 us                                                | 17.2 us: 1.26x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.85 sec: 1.26x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                                  |
| scimark_fft                | 382 ms                                                 | 315 ms: 1.21x faster                                                   |
| float                      | 84.7 ms                                                | 69.9 ms: 1.21x faster                                                  |
| mako                       | 11.9 ms                                                | 9.83 ms: 1.21x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 69.6 ms: 1.18x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.09 ms: 1.17x faster                                                  |
| spectral_norm              | 115 ms                                                 | 98.5 ms: 1.17x faster                                                  |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 137 ms: 1.17x faster                                                   |
| logging_format             | 7.23 us                                                | 6.24 us: 1.16x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.7 ms: 1.16x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.63 us: 1.15x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 201 us: 1.14x faster                                                   |
| chaos                      | 67.0 ms                                                | 58.8 ms: 1.14x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 66.4 ms: 1.13x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 79.1 ms: 1.13x faster                                                  |
| async_generators           | 463 ms                                                 | 411 ms: 1.13x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 95.0 ms: 1.12x faster                                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                   |
| raytrace                   | 312 ms                                                 | 281 ms: 1.11x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.57 ms: 1.11x faster                                                  |
| generators                 | 31.2 ms                                                | 28.3 ms: 1.10x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.10x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 56.1 ms: 1.10x faster                                                  |
| sympy_str                  | 300 ms                                                 | 276 ms: 1.09x faster                                                   |
| pyflate                    | 482 ms                                                 | 444 ms: 1.09x faster                                                   |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.44 ms: 1.08x faster                                                  |
| django_template            | 34.6 ms                                                | 32.1 ms: 1.08x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                  |
| go                         | 139 ms                                                 | 131 ms: 1.06x faster                                                   |
| 2to3                       | 274 ms                                                 | 258 ms: 1.06x faster                                                   |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 20.3 ms: 1.06x faster                                                  |
| fannkuch                   | 417 ms                                                 | 397 ms: 1.05x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.73 us: 1.04x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 748 ms: 1.04x faster                                                   |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.04x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 66.2 ms: 1.03x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                   |
| mdp                        | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.02x faster                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 53.7 ms: 1.02x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 318 us: 1.02x faster                                                   |
| json                       | 5.26 ms                                                | 5.18 ms: 1.02x faster                                                  |
| regex_dna                  | 212 ms                                                 | 209 ms: 1.02x faster                                                   |
| sympy_expand               | 478 ms                                                 | 472 ms: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| richards                   | 45.8 ms                                                | 45.5 ms: 1.01x faster                                                  |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                  |
| nbody                      | 97.0 ms                                                | 96.6 ms: 1.00x faster                                                  |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.04x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 24.1 ms: 1.04x slower                                                  |
| logging_silent             | 104 ns                                                 | 110 ns: 1.05x slower                                                   |
| bench_thread_pool          | 842 us                                                 | 888 us: 1.05x slower                                                   |
| nqueens                    | 83.3 ms                                                | 89.4 ms: 1.07x slower                                                  |
| telco                      | 7.10 ms                                                | 7.63 ms: 1.07x slower                                                  |
| hexiom                     | 6.41 ms                                                | 6.95 ms: 1.08x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.8 ms: 1.14x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.63 ms: 1.22x slower                                                  |
| coverage                   | 72.7 ms                                                | 90.2 ms: 1.24x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.45 ms: 1.66x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.2 ms: 3.38x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (2): asyncio_websockets, richards_super
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250210-3.14.0a4+-94cd2e0-JIT/bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.108x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.11x