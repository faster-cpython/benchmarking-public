# Results vs. 3.12.0

- fork: brandtbucher
- ref: null_stack_pointer
- machine: linux-x86_64
- commit hash: 7b432e3
- commit date: 2025-03-25
- overall geometric mean: 1.118x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 263 ms: 1.04x faster                                                       |
| docutils       | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 624 ms: 1.89x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 620 ms: 1.86x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.84x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                       |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.80x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.79x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 478 ms: 1.52x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.1 ms: 1.30x faster                                                      |
| nbody          | 97.0 ms                                                | 88.1 ms: 1.10x faster                                                      |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.13x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                       |
| regex_effbot   | 3.61 ms                                                | 3.16 ms: 1.14x faster                                                      |
| regex_v8       | 23.1 ms                                                | 23.2 ms: 1.00x slower                                                      |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                  | 1.07x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.86 sec: 1.25x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.15x faster                                                       |
| xml_etree_generate   | 89.2 ms                                                | 80.2 ms: 1.11x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 56.1 ms: 1.10x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 210 us: 1.10x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 97.8 ms: 1.09x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 321 us: 1.01x faster                                                       |
| json_loads           | 28.5 us                                                | 29.9 us: 1.05x slower                                                      |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.22 ms: 1.18x slower                                                      |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.7 ms: 1.09x faster                                                      |
| mako            | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 624 ms: 1.89x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 620 ms: 1.86x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.84x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                       |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.80x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.79x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 478 ms: 1.52x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                                       |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                       |
| deepcopy_memo              | 40.7 us                                                | 29.5 us: 1.38x faster                                                      |
| float                      | 84.7 ms                                                | 65.1 ms: 1.30x faster                                                      |
| richards                   | 45.8 ms                                                | 35.5 ms: 1.29x faster                                                      |
| richards_super             | 51.5 ms                                                | 40.2 ms: 1.28x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 1.86 sec: 1.25x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                                      |
| scimark_fft                | 382 ms                                                 | 307 ms: 1.24x faster                                                       |
| spectral_norm              | 115 ms                                                 | 92.7 ms: 1.24x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.02 ms: 1.23x faster                                                      |
| logging_format             | 7.23 us                                                | 6.12 us: 1.18x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.49 us: 1.18x faster                                                      |
| comprehensions             | 21.8 us                                                | 18.5 us: 1.18x faster                                                      |
| pathlib                    | 19.3 ms                                                | 16.6 ms: 1.16x faster                                                      |
| raytrace                   | 312 ms                                                 | 270 ms: 1.16x faster                                                       |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                       |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.15x faster                                                       |
| regex_effbot               | 3.61 ms                                                | 3.16 ms: 1.14x faster                                                      |
| dulwich_log                | 68.5 ms                                                | 60.6 ms: 1.13x faster                                                      |
| chaos                      | 67.0 ms                                                | 59.6 ms: 1.12x faster                                                      |
| async_generators           | 463 ms                                                 | 414 ms: 1.12x faster                                                       |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.11x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 80.2 ms: 1.11x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 67.7 ms: 1.11x faster                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.57 ms: 1.11x faster                                                      |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.10x faster                                                       |
| nbody                      | 97.0 ms                                                | 88.1 ms: 1.10x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 56.1 ms: 1.10x faster                                                      |
| generators                 | 31.2 ms                                                | 28.4 ms: 1.10x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 210 us: 1.10x faster                                                       |
| go                         | 139 ms                                                 | 127 ms: 1.09x faster                                                       |
| pyflate                    | 482 ms                                                 | 442 ms: 1.09x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                 | 97.8 ms: 1.09x faster                                                      |
| django_template            | 34.6 ms                                                | 31.7 ms: 1.09x faster                                                      |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.2 ms: 1.09x faster                                                      |
| sympy_str                  | 300 ms                                                 | 275 ms: 1.09x faster                                                       |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                                       |
| sympy_integrate            | 21.4 ms                                                | 20.0 ms: 1.07x faster                                                      |
| logging_silent             | 104 ns                                                 | 98.2 ns: 1.06x faster                                                      |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                      |
| mdp                        | 2.63 sec                                               | 2.49 sec: 1.06x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 77.9 ms: 1.05x faster                                                      |
| 2to3                       | 274 ms                                                 | 263 ms: 1.04x faster                                                       |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                     |
| sqlite_synth               | 2.83 us                                                | 2.73 us: 1.04x faster                                                      |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                       |
| docutils                   | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                     |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.03x faster                                                       |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                       |
| pickle_pure_python         | 324 us                                                 | 321 us: 1.01x faster                                                       |
| regex_v8                   | 23.1 ms                                                | 23.2 ms: 1.00x slower                                                      |
| pprint_safe_repr           | 776 ms                                                 | 783 ms: 1.01x slower                                                       |
| json                       | 5.26 ms                                                | 5.34 ms: 1.02x slower                                                      |
| fannkuch                   | 417 ms                                                 | 425 ms: 1.02x slower                                                       |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                                       |
| nqueens                    | 83.3 ms                                                | 86.2 ms: 1.03x slower                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.62 sec: 1.04x slower                                                     |
| bench_thread_pool          | 842 us                                                 | 883 us: 1.05x slower                                                       |
| json_loads                 | 28.5 us                                                | 29.9 us: 1.05x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                       |
| hexiom                     | 6.41 ms                                                | 6.82 ms: 1.06x slower                                                      |
| telco                      | 7.10 ms                                                | 7.77 ms: 1.09x slower                                                      |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                      |
| coverage                   | 72.7 ms                                                | 86.0 ms: 1.18x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 8.22 ms: 1.18x slower                                                      |
| gc_traversal               | 3.79 ms                                                | 4.84 ms: 1.28x slower                                                      |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 2.50 ms: 1.69x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 83.1 ms: 3.46x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                               |

Benchmark hidden because not significant (3): sympy_expand, coroutines, asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250325-3.14.0a6+-7b432e3-JIT/bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.118x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.11x