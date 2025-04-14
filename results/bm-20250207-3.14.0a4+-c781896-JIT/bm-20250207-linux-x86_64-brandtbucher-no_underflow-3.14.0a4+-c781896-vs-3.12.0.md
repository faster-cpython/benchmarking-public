# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_underflow
- machine: linux-x86_64
- commit hash: c781896
- commit date: 2025-02-07
- overall geometric mean: 1.121x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 259 ms: 1.06x faster                                                 |
| docutils       | 2.77 sec                                               | 2.65 sec: 1.04x faster                                               |
| Geometric mean | (ref)                                                  | 1.05x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 627 ms: 1.89x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 626 ms: 1.85x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 319 ms: 1.80x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 325 ms: 1.78x faster                                                 |
| async_tree_none            | 472 ms                                                 | 269 ms: 1.76x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 259 ms: 1.74x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 484 ms: 1.50x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.71x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.5 ms: 1.22x faster                                                |
| nbody          | 97.0 ms                                                | 94.3 ms: 1.03x faster                                                |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.18x faster                                                 |
| regex_effbot   | 3.61 ms                                                | 3.05 ms: 1.18x faster                                                |
| regex_dna      | 212 ms                                                 | 204 ms: 1.04x faster                                                 |
| regex_v8       | 23.1 ms                                                | 24.2 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                  | 1.09x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.83 sec: 1.27x faster                                               |
| xml_etree_parse      | 159 ms                                                 | 137 ms: 1.16x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 198 us: 1.16x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 78.3 ms: 1.14x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 55.1 ms: 1.12x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 96.4 ms: 1.11x faster                                                |
| pickle_pure_python   | 324 us                                                 | 320 us: 1.01x faster                                                 |
| json_loads           | 28.5 us                                                | 28.6 us: 1.00x slower                                                |
| json_dumps           | 10.4 ms                                                | 11.7 ms: 1.12x slower                                                |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.91 ms: 1.20x faster                                                |
| django_template | 34.6 ms                                                | 32.0 ms: 1.08x faster                                                |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 627 ms: 1.89x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 626 ms: 1.85x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 319 ms: 1.80x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 325 ms: 1.78x faster                                                 |
| async_tree_none            | 472 ms                                                 | 269 ms: 1.76x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 259 ms: 1.74x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 484 ms: 1.50x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                 |
| deepcopy                   | 371 us                                                 | 258 us: 1.44x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 30.7 us: 1.33x faster                                                |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.28x faster                                                |
| tomli_loads                | 2.33 sec                                               | 1.83 sec: 1.27x faster                                               |
| spectral_norm              | 115 ms                                                 | 92.0 ms: 1.25x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                |
| float                      | 84.7 ms                                                | 69.5 ms: 1.22x faster                                                |
| scimark_fft                | 382 ms                                                 | 314 ms: 1.22x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                |
| mako                       | 11.9 ms                                                | 9.91 ms: 1.20x faster                                                |
| regex_compile              | 148 ms                                                 | 125 ms: 1.18x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.05 ms: 1.18x faster                                                |
| go                         | 139 ms                                                 | 118 ms: 1.18x faster                                                 |
| logging_format             | 7.23 us                                                | 6.19 us: 1.17x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 137 ms: 1.16x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 198 us: 1.16x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.59 us: 1.16x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.22 ms: 1.15x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 71.1 ms: 1.15x faster                                                |
| raytrace                   | 312 ms                                                 | 271 ms: 1.15x faster                                                 |
| chaos                      | 67.0 ms                                                | 58.6 ms: 1.14x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 78.3 ms: 1.14x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 66.2 ms: 1.13x faster                                                |
| async_generators           | 463 ms                                                 | 409 ms: 1.13x faster                                                 |
| pyflate                    | 482 ms                                                 | 428 ms: 1.13x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                                 |
| generators                 | 31.2 ms                                                | 27.8 ms: 1.12x faster                                                |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 55.1 ms: 1.12x faster                                                |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.11x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 96.4 ms: 1.11x faster                                                |
| sympy_str                  | 300 ms                                                 | 273 ms: 1.10x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.61 ms: 1.10x faster                                                |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                                 |
| django_template            | 34.6 ms                                                | 32.0 ms: 1.08x faster                                                |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                |
| pprint_safe_repr           | 776 ms                                                 | 723 ms: 1.07x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                               |
| fannkuch                   | 417 ms                                                 | 390 ms: 1.07x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 20.0 ms: 1.07x faster                                                |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.07x faster                                                |
| 2to3                       | 274 ms                                                 | 259 ms: 1.06x faster                                                 |
| mdp                        | 2.63 sec                                               | 2.49 sec: 1.06x faster                                               |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                 |
| richards                   | 45.8 ms                                                | 43.5 ms: 1.05x faster                                                |
| docutils                   | 2.77 sec                                               | 2.65 sec: 1.04x faster                                               |
| dulwich_log                | 68.5 ms                                                | 65.7 ms: 1.04x faster                                                |
| regex_dna                  | 212 ms                                                 | 204 ms: 1.04x faster                                                 |
| sqlite_synth               | 2.83 us                                                | 2.72 us: 1.04x faster                                                |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                                 |
| richards_super             | 51.5 ms                                                | 49.7 ms: 1.04x faster                                                |
| coroutines                 | 23.2 ms                                                | 22.5 ms: 1.03x faster                                                |
| nbody                      | 97.0 ms                                                | 94.3 ms: 1.03x faster                                                |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                                 |
| json                       | 5.26 ms                                                | 5.13 ms: 1.02x faster                                                |
| sqlglot_optimize           | 54.8 ms                                                | 53.6 ms: 1.02x faster                                                |
| sympy_expand               | 478 ms                                                 | 468 ms: 1.02x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.01x faster                                               |
| pickle_pure_python         | 324 us                                                 | 320 us: 1.01x faster                                                 |
| hexiom                     | 6.41 ms                                                | 6.35 ms: 1.01x faster                                                |
| nqueens                    | 83.3 ms                                                | 82.6 ms: 1.01x faster                                                |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                 |
| json_loads                 | 28.5 us                                                | 28.6 us: 1.00x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 160 us: 1.01x slower                                                 |
| logging_silent             | 104 ns                                                 | 106 ns: 1.02x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                |
| bench_thread_pool          | 842 us                                                 | 871 us: 1.03x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 24.2 ms: 1.05x slower                                                |
| telco                      | 7.10 ms                                                | 7.68 ms: 1.08x slower                                                |
| json_dumps                 | 10.4 ms                                                | 11.7 ms: 1.12x slower                                                |
| coverage                   | 72.7 ms                                                | 89.9 ms: 1.24x slower                                                |
| gc_traversal               | 3.79 ms                                                | 4.94 ms: 1.30x slower                                                |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 80.8 ms: 3.37x slower                                                |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                         |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250207-3.14.0a4+-c781896-JIT/bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.121x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.10x