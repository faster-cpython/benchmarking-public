# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_recursion
- machine: linux-x86_64
- commit hash: 91d0090
- commit date: 2025-02-25
- overall geometric mean: 1.101x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 262 ms: 1.05x faster                                                  |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 622 ms: 1.90x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 617 ms: 1.87x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 319 ms: 1.80x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                  |
| async_tree_none            | 472 ms                                                 | 265 ms: 1.78x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 333 ms: 1.74x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 483 ms: 1.50x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 72.4 ms: 1.17x faster                                                 |
| nbody          | 97.0 ms                                                | 89.6 ms: 1.08x faster                                                 |
| pidigits       | 187 ms                                                 | 188 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.38 ms: 1.07x faster                                                 |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                                  |
| regex_v8       | 23.1 ms                                                | 25.6 ms: 1.11x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.86 sec: 1.26x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.15x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 79.6 ms: 1.12x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 207 us: 1.11x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 56.2 ms: 1.10x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 97.5 ms: 1.09x faster                                                 |
| json_loads           | 28.5 us                                                | 30.1 us: 1.06x slower                                                 |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.10x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.16 ms: 1.03x slower                                                 |
| python_startup         | 9.55 ms                                                | 13.0 ms: 1.36x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.19x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.6 ms: 1.12x faster                                                 |
| django_template | 34.6 ms                                                | 32.2 ms: 1.08x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 622 ms: 1.90x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 617 ms: 1.87x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 319 ms: 1.80x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                  |
| async_tree_none            | 472 ms                                                 | 265 ms: 1.78x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 333 ms: 1.74x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 483 ms: 1.50x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                                  |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 31.2 us: 1.31x faster                                                 |
| comprehensions             | 21.8 us                                                | 17.2 us: 1.26x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.86 sec: 1.26x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                 |
| scimark_fft                | 382 ms                                                 | 314 ms: 1.22x faster                                                  |
| spectral_norm              | 115 ms                                                 | 97.4 ms: 1.18x faster                                                 |
| float                      | 84.7 ms                                                | 72.4 ms: 1.17x faster                                                 |
| logging_format             | 7.23 us                                                | 6.20 us: 1.17x faster                                                 |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.15x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.62 us: 1.15x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.9 ms: 1.15x faster                                                 |
| async_generators           | 463 ms                                                 | 407 ms: 1.14x faster                                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                  |
| mako                       | 11.9 ms                                                | 10.6 ms: 1.12x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 79.6 ms: 1.12x faster                                                 |
| raytrace                   | 312 ms                                                 | 279 ms: 1.12x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 207 us: 1.11x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                 |
| chaos                      | 67.0 ms                                                | 60.4 ms: 1.11x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 56.2 ms: 1.10x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 97.5 ms: 1.09x faster                                                 |
| generators                 | 31.2 ms                                                | 28.5 ms: 1.09x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.40 ms: 1.09x faster                                                 |
| go                         | 139 ms                                                 | 128 ms: 1.09x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 68.9 ms: 1.09x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 75.1 ms: 1.09x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.65 ms: 1.09x faster                                                 |
| sympy_str                  | 300 ms                                                 | 276 ms: 1.09x faster                                                  |
| nbody                      | 97.0 ms                                                | 89.6 ms: 1.08x faster                                                 |
| django_template            | 34.6 ms                                                | 32.2 ms: 1.08x faster                                                 |
| pyflate                    | 482 ms                                                 | 450 ms: 1.07x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.38 ms: 1.07x faster                                                 |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.07x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 730 ms: 1.06x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 20.2 ms: 1.06x faster                                                 |
| mdp                        | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                |
| 2to3                       | 274 ms                                                 | 262 ms: 1.05x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.05x faster                                                 |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                                 |
| fannkuch                   | 417 ms                                                 | 401 ms: 1.04x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.73 us: 1.04x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                |
| sqlglot_optimize           | 54.8 ms                                                | 53.6 ms: 1.02x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 67.4 ms: 1.02x faster                                                 |
| sympy_expand               | 478 ms                                                 | 472 ms: 1.01x faster                                                  |
| nqueens                    | 83.3 ms                                                | 82.8 ms: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 188 ms: 1.01x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.16 ms: 1.03x slower                                                 |
| coroutines                 | 23.2 ms                                                | 23.9 ms: 1.03x slower                                                 |
| logging_silent             | 104 ns                                                 | 108 ns: 1.03x slower                                                  |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                                  |
| hexiom                     | 6.41 ms                                                | 6.67 ms: 1.04x slower                                                 |
| bench_thread_pool          | 842 us                                                 | 881 us: 1.05x slower                                                  |
| json_loads                 | 28.5 us                                                | 30.1 us: 1.06x slower                                                 |
| telco                      | 7.10 ms                                                | 7.51 ms: 1.06x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.10x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 25.6 ms: 1.11x slower                                                 |
| coverage                   | 72.7 ms                                                | 85.3 ms: 1.17x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 5.03 ms: 1.32x slower                                                 |
| python_startup             | 9.55 ms                                                | 13.0 ms: 1.36x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.45 ms: 1.66x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 82.1 ms: 3.42x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (7): richards, scimark_lu, json, asyncio_websockets, richards_super, pycparser, pickle_pure_python
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250225-3.14.0a5+-91d0090-JIT/bm-20250225-linux-x86_64-brandtbucher-jit_recursion-3.14.0a5+-91d0090.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.101x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.10x