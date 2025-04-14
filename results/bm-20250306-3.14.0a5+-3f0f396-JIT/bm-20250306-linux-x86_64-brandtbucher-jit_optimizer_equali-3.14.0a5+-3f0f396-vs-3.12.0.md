# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_optimizer_equali
- machine: linux-x86_64
- commit hash: 3f0f396
- commit date: 2025-03-06
- overall geometric mean: 1.107x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 261 ms: 1.05x faster                                                         |
| docutils       | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 622 ms: 1.90x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 618 ms: 1.87x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 320 ms: 1.80x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                         |
| async_tree_none            | 472 ms                                                 | 267 ms: 1.77x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 332 ms: 1.74x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 478 ms: 1.52x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.0 ms: 1.21x faster                                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| nbody          | 97.0 ms                                                | 98.9 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                         |
| regex_effbot   | 3.61 ms                                                | 3.40 ms: 1.06x faster                                                        |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                         |
| regex_v8       | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.85 sec: 1.26x faster                                                       |
| xml_etree_generate   | 89.2 ms                                                | 79.6 ms: 1.12x faster                                                        |
| unpickle_pure_python | 230 us                                                 | 207 us: 1.11x faster                                                         |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                         |
| xml_etree_process    | 61.7 ms                                                | 56.9 ms: 1.09x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 98.7 ms: 1.08x faster                                                        |
| json_loads           | 28.5 us                                                | 29.7 us: 1.04x slower                                                        |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                                 |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.15 ms: 1.03x slower                                                        |
| python_startup         | 9.55 ms                                                | 13.0 ms: 1.36x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.18x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.6 ms: 1.12x faster                                                        |
| django_template | 34.6 ms                                                | 31.9 ms: 1.08x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 622 ms: 1.90x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 618 ms: 1.87x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 320 ms: 1.80x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                         |
| async_tree_none            | 472 ms                                                 | 267 ms: 1.77x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 332 ms: 1.74x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 478 ms: 1.52x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                                         |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 29.7 us: 1.37x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.85 sec: 1.26x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                        |
| comprehensions             | 21.8 us                                                | 17.6 us: 1.24x faster                                                        |
| scimark_fft                | 382 ms                                                 | 313 ms: 1.22x faster                                                         |
| spectral_norm              | 115 ms                                                 | 94.4 ms: 1.22x faster                                                        |
| float                      | 84.7 ms                                                | 70.0 ms: 1.21x faster                                                        |
| logging_format             | 7.23 us                                                | 6.08 us: 1.19x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.45 us: 1.19x faster                                                        |
| go                         | 139 ms                                                 | 120 ms: 1.17x faster                                                         |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                         |
| async_generators           | 463 ms                                                 | 404 ms: 1.14x faster                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.44 ms: 1.14x faster                                                        |
| pyflate                    | 482 ms                                                 | 427 ms: 1.13x faster                                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                         |
| pathlib                    | 19.3 ms                                                | 17.1 ms: 1.13x faster                                                        |
| raytrace                   | 312 ms                                                 | 277 ms: 1.13x faster                                                         |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.12x faster                                                         |
| chaos                      | 67.0 ms                                                | 59.6 ms: 1.12x faster                                                        |
| mako                       | 11.9 ms                                                | 10.6 ms: 1.12x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.7 ms: 1.12x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 79.6 ms: 1.12x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.34 ms: 1.11x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 207 us: 1.11x faster                                                         |
| generators                 | 31.2 ms                                                | 28.2 ms: 1.11x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 74.1 ms: 1.11x faster                                                        |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 68.8 ms: 1.09x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                         |
| xml_etree_process          | 61.7 ms                                                | 56.9 ms: 1.09x faster                                                        |
| django_template            | 34.6 ms                                                | 31.9 ms: 1.08x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 98.7 ms: 1.08x faster                                                        |
| sympy_integrate            | 21.4 ms                                                | 20.1 ms: 1.06x faster                                                        |
| regex_effbot               | 3.61 ms                                                | 3.40 ms: 1.06x faster                                                        |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                                         |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                        |
| mdp                        | 2.63 sec                                               | 2.49 sec: 1.06x faster                                                       |
| 2to3                       | 274 ms                                                 | 261 ms: 1.05x faster                                                         |
| pprint_safe_repr           | 776 ms                                                 | 737 ms: 1.05x faster                                                         |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                                         |
| richards                   | 45.8 ms                                                | 44.1 ms: 1.04x faster                                                        |
| sqlite_synth               | 2.83 us                                                | 2.73 us: 1.04x faster                                                        |
| docutils                   | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                       |
| fannkuch                   | 417 ms                                                 | 403 ms: 1.03x faster                                                         |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                         |
| sympy_expand               | 478 ms                                                 | 466 ms: 1.03x faster                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.03x faster                                                       |
| richards_super             | 51.5 ms                                                | 50.4 ms: 1.02x faster                                                        |
| sqlglot_optimize           | 54.8 ms                                                | 53.6 ms: 1.02x faster                                                        |
| dulwich_log                | 68.5 ms                                                | 67.1 ms: 1.02x faster                                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| nqueens                    | 83.3 ms                                                | 82.8 ms: 1.01x faster                                                        |
| hexiom                     | 6.41 ms                                                | 6.40 ms: 1.00x faster                                                        |
| json                       | 5.26 ms                                                | 5.33 ms: 1.01x slower                                                        |
| logging_silent             | 104 ns                                                 | 106 ns: 1.02x slower                                                         |
| nbody                      | 97.0 ms                                                | 98.9 ms: 1.02x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.15 ms: 1.03x slower                                                        |
| bench_thread_pool          | 842 us                                                 | 876 us: 1.04x slower                                                         |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                         |
| json_loads                 | 28.5 us                                                | 29.7 us: 1.04x slower                                                        |
| coroutines                 | 23.2 ms                                                | 24.4 ms: 1.05x slower                                                        |
| telco                      | 7.10 ms                                                | 7.66 ms: 1.08x slower                                                        |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                        |
| coverage                   | 72.7 ms                                                | 83.8 ms: 1.15x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 5.00 ms: 1.32x slower                                                        |
| python_startup             | 9.55 ms                                                | 13.0 ms: 1.36x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.44 ms: 1.65x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.7 ms: 3.40x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                 |

Benchmark hidden because not significant (4): pickle_pure_python, asyncio_websockets, pycparser, scimark_lu
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250306-3.14.0a5+-3f0f396-JIT/bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.107x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.10x