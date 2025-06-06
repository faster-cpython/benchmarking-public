# Results vs. 3.12.0

- fork: nascheme
- ref: pgo_benchmark_task
- machine: linux-x86_64
- commit hash: 8dd8862
- commit date: 2025-02-28
- overall geometric mean: 1.133x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 258 ms: 1.06x faster                                                   |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 606 ms: 1.95x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 593 ms: 1.95x faster                                                   |
| async_tree_none            | 472 ms                                                 | 248 ms: 1.90x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 306 ms: 1.89x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 305 ms: 1.89x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 240 ms: 1.87x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 459 ms: 1.58x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 468 ms: 1.55x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.82x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.7 ms: 1.22x faster                                                  |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.14 ms: 1.15x faster                                                  |
| regex_dna      | 212 ms                                                 | 188 ms: 1.13x faster                                                   |
| regex_v8       | 23.1 ms                                                | 22.9 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                 | 129 ms: 1.23x faster                                                   |
| tomli_loads          | 2.33 sec                                               | 2.02 sec: 1.15x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 93.9 ms: 1.14x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 80.4 ms: 1.11x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 56.5 ms: 1.09x faster                                                  |
| json_loads           | 28.5 us                                                | 26.7 us: 1.07x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 316 us: 1.03x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 227 us: 1.01x faster                                                   |
| json_dumps           | 10.4 ms                                                | 10.7 ms: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.18 ms: 1.04x slower                                                  |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.19x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                  |
| mako            | 11.9 ms                                                | 11.6 ms: 1.03x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 606 ms: 1.95x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 593 ms: 1.95x faster                                                   |
| async_tree_none            | 472 ms                                                 | 248 ms: 1.90x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 306 ms: 1.89x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 305 ms: 1.89x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 240 ms: 1.87x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 459 ms: 1.58x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 468 ms: 1.55x faster                                                   |
| deepcopy                   | 371 us                                                 | 250 us: 1.48x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 29.8 us: 1.37x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.3 us: 1.34x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.63 us: 1.27x faster                                                  |
| async_generators           | 463 ms                                                 | 365 ms: 1.27x faster                                                   |
| spectral_norm              | 115 ms                                                 | 91.1 ms: 1.26x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 129 ms: 1.23x faster                                                   |
| float                      | 84.7 ms                                                | 69.7 ms: 1.22x faster                                                  |
| go                         | 139 ms                                                 | 117 ms: 1.19x faster                                                   |
| logging_format             | 7.23 us                                                | 6.08 us: 1.19x faster                                                  |
| scimark_fft                | 382 ms                                                 | 323 ms: 1.18x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.15 ms: 1.18x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 64.2 ms: 1.17x faster                                                  |
| chaos                      | 67.0 ms                                                | 57.6 ms: 1.16x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.56 us: 1.16x faster                                                  |
| raytrace                   | 312 ms                                                 | 270 ms: 1.16x faster                                                   |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 2.02 sec: 1.15x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.14 ms: 1.15x faster                                                  |
| fannkuch                   | 417 ms                                                 | 364 ms: 1.15x faster                                                   |
| meteor_contest             | 112 ms                                                 | 98.2 ms: 1.14x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.9 ms: 1.14x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 93.9 ms: 1.14x faster                                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                   |
| regex_dna                  | 212 ms                                                 | 188 ms: 1.13x faster                                                   |
| generators                 | 31.2 ms                                                | 28.0 ms: 1.12x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.11x faster                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 73.7 ms: 1.11x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 80.4 ms: 1.11x faster                                                  |
| pyflate                    | 482 ms                                                 | 435 ms: 1.11x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 700 ms: 1.11x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 56.5 ms: 1.09x faster                                                  |
| sympy_str                  | 300 ms                                                 | 274 ms: 1.09x faster                                                   |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.44 sec: 1.09x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.66 ms: 1.09x faster                                                  |
| django_template            | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                  |
| richards                   | 45.8 ms                                                | 42.8 ms: 1.07x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                 |
| hexiom                     | 6.41 ms                                                | 6.01 ms: 1.07x faster                                                  |
| json_loads                 | 28.5 us                                                | 26.7 us: 1.07x faster                                                  |
| 2to3                       | 274 ms                                                 | 258 ms: 1.06x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 20.2 ms: 1.06x faster                                                  |
| richards_super             | 51.5 ms                                                | 48.8 ms: 1.06x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                 |
| nqueens                    | 83.3 ms                                                | 79.4 ms: 1.05x faster                                                  |
| telco                      | 7.10 ms                                                | 6.81 ms: 1.04x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                  |
| coroutines                 | 23.2 ms                                                | 22.3 ms: 1.04x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.04x faster                                                  |
| mako                       | 11.9 ms                                                | 11.6 ms: 1.03x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                   |
| pickle_pure_python         | 324 us                                                 | 316 us: 1.03x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.76 us: 1.03x faster                                                  |
| sympy_expand               | 478 ms                                                 | 466 ms: 1.03x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 66.9 ms: 1.02x faster                                                  |
| typing_runtime_protocols   | 158 us                                                 | 154 us: 1.02x faster                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 53.7 ms: 1.02x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                   |
| unpickle_pure_python       | 230 us                                                 | 227 us: 1.01x faster                                                   |
| regex_v8                   | 23.1 ms                                                | 22.9 ms: 1.01x faster                                                  |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| logging_silent             | 104 ns                                                 | 105 ns: 1.00x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 10.7 ms: 1.03x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.18 ms: 1.04x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 880 us: 1.04x slower                                                   |
| coverage                   | 72.7 ms                                                | 88.7 ms: 1.22x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.83 ms: 1.27x slower                                                  |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 82.6 ms: 3.44x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                           |

Benchmark hidden because not significant (3): nbody, asyncio_websockets, json
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250228-3.14.0a5+-8dd8862/bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.133x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.07x