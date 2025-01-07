# Results vs. 3.12.0

- fork: kumaraditya303
- ref: fast_state
- machine: linux-x86_64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.103x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 256 ms: 1.07x faster                                                 |
| docutils       | 2.77 sec                                               | 2.62 sec: 1.06x faster                                               |
| Geometric mean | (ref)                                                  | 1.06x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 577 ms: 2.00x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 594 ms: 1.99x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 298 ms: 1.93x faster                                                 |
| async_tree_none            | 472 ms                                                 | 257 ms: 1.83x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 246 ms: 1.83x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 322 ms: 1.79x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 467 ms: 1.55x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 484 ms: 1.50x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.80x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 73.6 ms: 1.15x faster                                                |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                         |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                 |
| regex_effbot   | 3.61 ms                                                | 3.43 ms: 1.05x faster                                                |
| regex_dna      | 212 ms                                                 | 223 ms: 1.05x slower                                                 |
| regex_v8       | 23.1 ms                                                | 26.4 ms: 1.14x slower                                                |
| Geometric mean | (ref)                                                  | 1.00x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.01 sec: 1.16x faster                                               |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.14x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 96.6 ms: 1.11x faster                                                |
| json_loads           | 28.5 us                                                | 26.4 us: 1.08x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 84.8 ms: 1.05x faster                                                |
| unpickle_pure_python | 230 us                                                 | 220 us: 1.05x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 59.6 ms: 1.04x faster                                                |
| pickle_pure_python   | 324 us                                                 | 321 us: 1.01x faster                                                 |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.10x slower                                                |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.4 ms: 1.10x faster                                                |
| mako            | 11.9 ms                                                | 11.8 ms: 1.01x faster                                                |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 577 ms: 2.00x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 594 ms: 1.99x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 298 ms: 1.93x faster                                                 |
| async_tree_none            | 472 ms                                                 | 257 ms: 1.83x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 246 ms: 1.83x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 322 ms: 1.79x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 467 ms: 1.55x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 484 ms: 1.50x faster                                                 |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 31.3 us: 1.30x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 2.62 us: 1.28x faster                                                |
| comprehensions             | 21.8 us                                                | 17.4 us: 1.25x faster                                                |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.20x faster                                                |
| go                         | 139 ms                                                 | 119 ms: 1.17x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 70.4 ms: 1.16x faster                                                |
| logging_format             | 7.23 us                                                | 6.22 us: 1.16x faster                                                |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.01 sec: 1.16x faster                                               |
| float                      | 84.7 ms                                                | 73.6 ms: 1.15x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.14x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.65 us: 1.14x faster                                                |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                                 |
| sqlalchemy_declarative     | 147 ms                                                 | 129 ms: 1.14x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                                 |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.5 ms: 1.13x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.30 ms: 1.13x faster                                                |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.11x faster                                                 |
| sympy_str                  | 300 ms                                                 | 270 ms: 1.11x faster                                                 |
| scimark_fft                | 382 ms                                                 | 345 ms: 1.11x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 96.6 ms: 1.11x faster                                                |
| async_generators           | 463 ms                                                 | 420 ms: 1.10x faster                                                 |
| chaos                      | 67.0 ms                                                | 60.7 ms: 1.10x faster                                                |
| django_template            | 34.6 ms                                                | 31.4 ms: 1.10x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 68.2 ms: 1.10x faster                                                |
| generators                 | 31.2 ms                                                | 28.4 ms: 1.10x faster                                                |
| json_loads                 | 28.5 us                                                | 26.4 us: 1.08x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.08x faster                                                |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                |
| dulwich_log                | 68.5 ms                                                | 63.9 ms: 1.07x faster                                                |
| 2to3                       | 274 ms                                                 | 256 ms: 1.07x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 724 ms: 1.07x faster                                                 |
| sqlglot_normalize          | 110 ms                                                 | 104 ms: 1.06x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                               |
| json                       | 5.26 ms                                                | 4.97 ms: 1.06x faster                                                |
| docutils                   | 2.77 sec                                               | 2.62 sec: 1.06x faster                                               |
| regex_effbot               | 3.61 ms                                                | 3.43 ms: 1.05x faster                                                |
| pyflate                    | 482 ms                                                 | 458 ms: 1.05x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.81 ms: 1.05x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 84.8 ms: 1.05x faster                                                |
| sympy_expand               | 478 ms                                                 | 456 ms: 1.05x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 220 us: 1.05x faster                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 52.6 ms: 1.04x faster                                                |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.04x faster                                                 |
| mdp                        | 2.63 sec                                               | 2.53 sec: 1.04x faster                                               |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 59.6 ms: 1.04x faster                                                |
| fannkuch                   | 417 ms                                                 | 404 ms: 1.03x faster                                                 |
| richards                   | 45.8 ms                                                | 44.9 ms: 1.02x faster                                                |
| hexiom                     | 6.41 ms                                                | 6.31 ms: 1.02x faster                                                |
| nqueens                    | 83.3 ms                                                | 82.0 ms: 1.02x faster                                                |
| pickle_pure_python         | 324 us                                                 | 321 us: 1.01x faster                                                 |
| mako                       | 11.9 ms                                                | 11.8 ms: 1.01x faster                                                |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                 |
| sqlite_synth               | 2.83 us                                                | 2.85 us: 1.01x slower                                                |
| coroutines                 | 23.2 ms                                                | 23.6 ms: 1.02x slower                                                |
| python_startup_no_site     | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                |
| logging_silent             | 104 ns                                                 | 107 ns: 1.02x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                                 |
| bench_thread_pool          | 842 us                                                 | 866 us: 1.03x slower                                                 |
| regex_dna                  | 212 ms                                                 | 223 ms: 1.05x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.10x slower                                                |
| telco                      | 7.10 ms                                                | 7.84 ms: 1.10x slower                                                |
| coverage                   | 72.7 ms                                                | 82.7 ms: 1.14x slower                                                |
| mypy2                      | 830 ms                                                 | 949 ms: 1.14x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 26.4 ms: 1.14x slower                                                |
| gc_traversal               | 3.79 ms                                                | 4.93 ms: 1.30x slower                                                |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.66x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 81.7 ms: 3.40x slower                                                |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                         |

Benchmark hidden because not significant (5): richards_super, pycparser, asyncio_websockets, scimark_lu, nbody
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250107-3.14.0a3+-7de6e22/bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.103x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.10x