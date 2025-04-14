# Results vs. 3.12.0

- fork: brandtbucher
- ref: null_stack_pointer
- machine: linux-x86_64
- commit hash: 7b432e3
- commit date: 2025-03-25
- overall geometric mean: 1.114x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 256 ms: 1.07x faster                                                       |
| docutils       | 2.77 sec                                               | 2.60 sec: 1.06x faster                                                     |
| Geometric mean | (ref)                                                  | 1.07x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 618 ms: 1.91x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 614 ms: 1.88x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.84x faster                                                       |
| async_tree_none            | 472 ms                                                 | 257 ms: 1.84x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 471 ms: 1.54x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 490 ms: 1.48x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 68.9 ms: 1.23x faster                                                      |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.07x faster                                                               |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                       |
| regex_effbot   | 3.61 ms                                                | 3.43 ms: 1.05x faster                                                      |
| regex_v8       | 23.1 ms                                                | 24.2 ms: 1.05x slower                                                      |
| regex_dna      | 212 ms                                                 | 223 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.95 sec: 1.20x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 97.4 ms: 1.10x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 84.5 ms: 1.06x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.06x faster                                                       |
| xml_etree_process    | 61.7 ms                                                | 58.8 ms: 1.05x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 315 us: 1.03x faster                                                       |
| json_loads           | 28.5 us                                                | 29.8 us: 1.05x slower                                                      |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.21 ms: 1.18x slower                                                      |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.38x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.3 ms: 1.11x faster                                                      |
| mako            | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 618 ms: 1.91x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 614 ms: 1.88x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.84x faster                                                       |
| async_tree_none            | 472 ms                                                 | 257 ms: 1.84x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 471 ms: 1.54x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 490 ms: 1.48x faster                                                       |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                                       |
| deepcopy_memo              | 40.7 us                                                | 29.3 us: 1.39x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.62 us: 1.28x faster                                                      |
| go                         | 139 ms                                                 | 113 ms: 1.23x faster                                                       |
| float                      | 84.7 ms                                                | 68.9 ms: 1.23x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.09 ms: 1.20x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 1.95 sec: 1.20x faster                                                     |
| raytrace                   | 312 ms                                                 | 263 ms: 1.19x faster                                                       |
| logging_format             | 7.23 us                                                | 6.15 us: 1.18x faster                                                      |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                       |
| dulwich_log                | 68.5 ms                                                | 58.3 ms: 1.18x faster                                                      |
| async_generators           | 463 ms                                                 | 394 ms: 1.17x faster                                                       |
| spectral_norm              | 115 ms                                                 | 98.6 ms: 1.17x faster                                                      |
| pathlib                    | 19.3 ms                                                | 16.7 ms: 1.16x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.59 us: 1.16x faster                                                      |
| chaos                      | 67.0 ms                                                | 58.4 ms: 1.15x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                       |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                       |
| sqlalchemy_declarative     | 147 ms                                                 | 129 ms: 1.13x faster                                                       |
| pyflate                    | 482 ms                                                 | 429 ms: 1.12x faster                                                       |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                       |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.7 ms: 1.12x faster                                                      |
| generators                 | 31.2 ms                                                | 27.9 ms: 1.12x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 67.4 ms: 1.11x faster                                                      |
| django_template            | 34.6 ms                                                | 31.3 ms: 1.11x faster                                                      |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.11x faster                                                       |
| sympy_integrate            | 21.4 ms                                                | 19.4 ms: 1.10x faster                                                      |
| scimark_fft                | 382 ms                                                 | 348 ms: 1.10x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                 | 97.4 ms: 1.10x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 75.4 ms: 1.09x faster                                                      |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                      |
| 2to3                       | 274 ms                                                 | 256 ms: 1.07x faster                                                       |
| logging_silent             | 104 ns                                                 | 97.8 ns: 1.07x faster                                                      |
| richards                   | 45.8 ms                                                | 42.9 ms: 1.07x faster                                                      |
| docutils                   | 2.77 sec                                               | 2.60 sec: 1.06x faster                                                     |
| mdp                        | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 734 ms: 1.06x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.79 ms: 1.06x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 84.5 ms: 1.06x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.06x faster                                                       |
| regex_effbot               | 3.61 ms                                                | 3.43 ms: 1.05x faster                                                      |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 58.8 ms: 1.05x faster                                                      |
| sympy_expand               | 478 ms                                                 | 457 ms: 1.05x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.04x faster                                                     |
| richards_super             | 51.5 ms                                                | 49.4 ms: 1.04x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 315 us: 1.03x faster                                                       |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                                      |
| hexiom                     | 6.41 ms                                                | 6.29 ms: 1.02x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                       |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                       |
| json                       | 5.26 ms                                                | 5.33 ms: 1.01x slower                                                      |
| fannkuch                   | 417 ms                                                 | 425 ms: 1.02x slower                                                       |
| coroutines                 | 23.2 ms                                                | 23.8 ms: 1.03x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                       |
| bench_thread_pool          | 842 us                                                 | 871 us: 1.03x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 24.2 ms: 1.05x slower                                                      |
| json_loads                 | 28.5 us                                                | 29.8 us: 1.05x slower                                                      |
| regex_dna                  | 212 ms                                                 | 223 ms: 1.05x slower                                                       |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                      |
| telco                      | 7.10 ms                                                | 7.94 ms: 1.12x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 8.21 ms: 1.18x slower                                                      |
| gc_traversal               | 3.79 ms                                                | 4.82 ms: 1.27x slower                                                      |
| coverage                   | 72.7 ms                                                | 93.3 ms: 1.28x slower                                                      |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.38x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 83.2 ms: 3.47x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                               |

Benchmark hidden because not significant (4): nbody, asyncio_websockets, pycparser, nqueens
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250325-3.14.0a6+-7b432e3/bm-20250325-linux-x86_64-brandtbucher-null_stack_pointer-3.14.0a6+-7b432e3.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.114x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.10x