# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_up_12_11
- machine: linux-x86_64
- commit hash: 9ee2a07
- commit date: 2025-03-26
- overall geometric mean: 1.110x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 264 ms: 1.04x faster                                                 |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 626 ms: 1.89x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 619 ms: 1.87x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 317 ms: 1.82x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                 |
| async_tree_none            | 472 ms                                                 | 266 ms: 1.77x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 477 ms: 1.52x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.4 ms: 1.30x faster                                                |
| nbody          | 97.0 ms                                                | 87.9 ms: 1.10x faster                                                |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.13x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                 |
| regex_effbot   | 3.61 ms                                                | 3.48 ms: 1.04x faster                                                |
| regex_v8       | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                |
| regex_dna      | 212 ms                                                 | 226 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.88 sec: 1.24x faster                                               |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.14x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 80.5 ms: 1.11x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 97.2 ms: 1.10x faster                                                |
| unpickle_pure_python | 230 us                                                 | 212 us: 1.09x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 57.0 ms: 1.08x faster                                                |
| pickle_pure_python   | 324 us                                                 | 321 us: 1.01x faster                                                 |
| json_loads           | 28.5 us                                                | 29.9 us: 1.05x slower                                                |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.18 ms: 1.18x slower                                                |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.0 ms: 1.09x faster                                                |
| django_template | 34.6 ms                                                | 32.4 ms: 1.07x faster                                                |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 626 ms: 1.89x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 619 ms: 1.87x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 317 ms: 1.82x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                 |
| async_tree_none            | 472 ms                                                 | 266 ms: 1.77x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 477 ms: 1.52x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                 |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 29.0 us: 1.40x faster                                                |
| float                      | 84.7 ms                                                | 65.4 ms: 1.30x faster                                                |
| richards                   | 45.8 ms                                                | 35.9 ms: 1.28x faster                                                |
| richards_super             | 51.5 ms                                                | 40.6 ms: 1.27x faster                                                |
| tomli_loads                | 2.33 sec                                               | 1.88 sec: 1.24x faster                                               |
| spectral_norm              | 115 ms                                                 | 93.0 ms: 1.24x faster                                                |
| scimark_fft                | 382 ms                                                 | 312 ms: 1.22x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.05 ms: 1.22x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 2.75 us: 1.22x faster                                                |
| logging_simple             | 6.46 us                                                | 5.54 us: 1.17x faster                                                |
| raytrace                   | 312 ms                                                 | 268 ms: 1.16x faster                                                 |
| logging_format             | 7.23 us                                                | 6.22 us: 1.16x faster                                                |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.8 ms: 1.15x faster                                                |
| comprehensions             | 21.8 us                                                | 19.0 us: 1.15x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.14x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 60.8 ms: 1.13x faster                                                |
| chaos                      | 67.0 ms                                                | 59.9 ms: 1.12x faster                                                |
| async_generators           | 463 ms                                                 | 415 ms: 1.12x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.11x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 67.6 ms: 1.11x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 80.5 ms: 1.11x faster                                                |
| nbody                      | 97.0 ms                                                | 87.9 ms: 1.10x faster                                                |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.10x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 97.2 ms: 1.10x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.63 ms: 1.09x faster                                                |
| pyflate                    | 482 ms                                                 | 443 ms: 1.09x faster                                                 |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.09x faster                                                |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.2 ms: 1.09x faster                                                |
| sympy_str                  | 300 ms                                                 | 276 ms: 1.09x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 212 us: 1.09x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 57.0 ms: 1.08x faster                                                |
| generators                 | 31.2 ms                                                | 28.9 ms: 1.08x faster                                                |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                                 |
| django_template            | 34.6 ms                                                | 32.4 ms: 1.07x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 20.1 ms: 1.07x faster                                                |
| logging_silent             | 104 ns                                                 | 98.4 ns: 1.06x faster                                                |
| mdp                        | 2.63 sec                                               | 2.51 sec: 1.05x faster                                               |
| go                         | 139 ms                                                 | 133 ms: 1.05x faster                                                 |
| sqlite_synth               | 2.83 us                                                | 2.71 us: 1.05x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 78.6 ms: 1.04x faster                                                |
| 2to3                       | 274 ms                                                 | 264 ms: 1.04x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.48 ms: 1.04x faster                                                |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                               |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.02x faster                                                 |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                 |
| sympy_expand               | 478 ms                                                 | 474 ms: 1.01x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 321 us: 1.01x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 118 ms: 1.00x faster                                                 |
| fannkuch                   | 417 ms                                                 | 419 ms: 1.00x slower                                                 |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.01x slower                                                |
| nqueens                    | 83.3 ms                                                | 84.1 ms: 1.01x slower                                                |
| regex_v8                   | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                |
| bench_thread_pool          | 842 us                                                 | 883 us: 1.05x slower                                                 |
| json_loads                 | 28.5 us                                                | 29.9 us: 1.05x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.07x slower                                                 |
| regex_dna                  | 212 ms                                                 | 226 ms: 1.07x slower                                                 |
| hexiom                     | 6.41 ms                                                | 6.90 ms: 1.08x slower                                                |
| telco                      | 7.10 ms                                                | 7.77 ms: 1.09x slower                                                |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                |
| coverage                   | 72.7 ms                                                | 85.7 ms: 1.18x slower                                                |
| python_startup_no_site     | 6.94 ms                                                | 8.18 ms: 1.18x slower                                                |
| gc_traversal               | 3.79 ms                                                | 4.80 ms: 1.27x slower                                                |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 82.7 ms: 3.44x slower                                                |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                         |

Benchmark hidden because not significant (5): asyncio_websockets, pycparser, pprint_safe_repr, pprint_pformat, json
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250326-3.14.0a6+-9ee2a07-JIT/bm-20250326-linux-x86_64-brandtbucher-jit_up_12_11-3.14.0a6+-9ee2a07.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.110x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.11x