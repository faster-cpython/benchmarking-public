# Results vs. 3.12.0

- fork: python
- ref: 5cdd6e5e758a3fc0a5da
- machine: linux-x86_64
- commit hash: 5cdd6e5
- commit date: 2025-02-12
- overall geometric mean: 1.111x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 258 ms: 1.06x faster                                                   |
| docutils       | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 620 ms: 1.91x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 625 ms: 1.85x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 321 ms: 1.79x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 328 ms: 1.76x faster                                                   |
| async_tree_none            | 472 ms                                                 | 268 ms: 1.76x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 261 ms: 1.72x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 485 ms: 1.50x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.71x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.5 ms: 1.20x faster                                                  |
| nbody          | 97.0 ms                                                | 93.5 ms: 1.04x faster                                                  |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.16 ms: 1.14x faster                                                  |
| regex_dna      | 212 ms                                                 | 207 ms: 1.03x faster                                                   |
| regex_v8       | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.84 sec: 1.27x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 199 us: 1.16x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 138 ms: 1.15x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 78.3 ms: 1.14x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 55.5 ms: 1.11x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 96.2 ms: 1.11x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.02x faster                                                   |
| json_loads           | 28.5 us                                                | 29.0 us: 1.02x slower                                                  |
| json_dumps           | 10.4 ms                                                | 11.9 ms: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                  |
| django_template | 34.6 ms                                                | 31.7 ms: 1.09x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 620 ms: 1.91x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 625 ms: 1.85x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 321 ms: 1.79x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 328 ms: 1.76x faster                                                   |
| async_tree_none            | 472 ms                                                 | 268 ms: 1.76x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 261 ms: 1.72x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 485 ms: 1.50x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                                   |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 30.7 us: 1.33x faster                                                  |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.27x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.84 sec: 1.27x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                                  |
| scimark_fft                | 382 ms                                                 | 312 ms: 1.22x faster                                                   |
| float                      | 84.7 ms                                                | 70.5 ms: 1.20x faster                                                  |
| spectral_norm              | 115 ms                                                 | 95.7 ms: 1.20x faster                                                  |
| mako                       | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                  |
| logging_format             | 7.23 us                                                | 6.12 us: 1.18x faster                                                  |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                   |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.18x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.56 us: 1.16x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 70.7 ms: 1.16x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 199 us: 1.16x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 138 ms: 1.15x faster                                                   |
| chaos                      | 67.0 ms                                                | 58.4 ms: 1.15x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 65.8 ms: 1.14x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.16 ms: 1.14x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 78.3 ms: 1.14x faster                                                  |
| raytrace                   | 312 ms                                                 | 275 ms: 1.13x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.48 ms: 1.13x faster                                                  |
| generators                 | 31.2 ms                                                | 27.7 ms: 1.13x faster                                                  |
| async_generators           | 463 ms                                                 | 413 ms: 1.12x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 55.5 ms: 1.11x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 96.2 ms: 1.11x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.37 ms: 1.10x faster                                                  |
| sympy_str                  | 300 ms                                                 | 275 ms: 1.09x faster                                                   |
| django_template            | 34.6 ms                                                | 31.7 ms: 1.09x faster                                                  |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.07x faster                                                   |
| pycparser                  | 1.18 sec                                               | 1.10 sec: 1.07x faster                                                 |
| go                         | 139 ms                                                 | 131 ms: 1.07x faster                                                   |
| 2to3                       | 274 ms                                                 | 258 ms: 1.06x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 20.2 ms: 1.06x faster                                                  |
| fannkuch                   | 417 ms                                                 | 395 ms: 1.06x faster                                                   |
| pyflate                    | 482 ms                                                 | 457 ms: 1.06x faster                                                   |
| richards                   | 45.8 ms                                                | 43.4 ms: 1.06x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                  |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.04x faster                                                 |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                                   |
| nbody                      | 97.0 ms                                                | 93.5 ms: 1.04x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 66.1 ms: 1.04x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                 |
| richards_super             | 51.5 ms                                                | 49.8 ms: 1.03x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 751 ms: 1.03x faster                                                   |
| regex_dna                  | 212 ms                                                 | 207 ms: 1.03x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                 |
| json                       | 5.26 ms                                                | 5.14 ms: 1.02x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 53.6 ms: 1.02x faster                                                  |
| sympy_expand               | 478 ms                                                 | 470 ms: 1.02x faster                                                   |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.02x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                   |
| logging_silent             | 104 ns                                                 | 106 ns: 1.01x slower                                                   |
| json_loads                 | 28.5 us                                                | 29.0 us: 1.02x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                   |
| bench_thread_pool          | 842 us                                                 | 889 us: 1.06x slower                                                   |
| telco                      | 7.10 ms                                                | 7.59 ms: 1.07x slower                                                  |
| nqueens                    | 83.3 ms                                                | 89.3 ms: 1.07x slower                                                  |
| hexiom                     | 6.41 ms                                                | 6.93 ms: 1.08x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.9 ms: 1.14x slower                                                  |
| coverage                   | 72.7 ms                                                | 89.8 ms: 1.24x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.95 ms: 1.31x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.68x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.2 ms: 3.38x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250212-3.14.0a4+-5cdd6e5-JIT/bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.111x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.11x