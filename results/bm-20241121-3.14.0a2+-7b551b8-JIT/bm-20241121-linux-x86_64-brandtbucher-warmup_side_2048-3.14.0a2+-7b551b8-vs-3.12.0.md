# Results vs. 3.12.0

- fork: brandtbucher
- ref: warmup_side_2048
- machine: linux-x86_64
- commit hash: 7b551b8
- commit date: 2024-11-21
- overall geometric mean: 1.073x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 261 ms: 1.05x faster                                                     |
| docutils       | 2.77 sec                                               | 2.79 sec: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 326 ms: 1.44x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 399 ms: 1.44x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 314 ms: 1.43x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 415 ms: 1.39x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 921 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 565 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 566 ms: 1.28x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 914 ms: 1.26x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.35x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 82.3 ms: 1.18x faster                                                    |
| float          | 84.7 ms                                                | 77.8 ms: 1.09x faster                                                    |
| pidigits       | 187 ms                                                 | 191 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                  | 1.08x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                     |
| regex_effbot   | 3.61 ms                                                | 3.50 ms: 1.03x faster                                                    |
| regex_dna      | 212 ms                                                 | 226 ms: 1.06x slower                                                     |
| regex_v8       | 23.1 ms                                                | 26.0 ms: 1.12x slower                                                    |
| Geometric mean | (ref)                                                  | 1.00x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 230 us                                                 | 193 us: 1.19x faster                                                     |
| tomli_loads          | 2.33 sec                                               | 1.97 sec: 1.18x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 78.5 ms: 1.14x faster                                                    |
| xml_etree_process    | 61.7 ms                                                | 55.3 ms: 1.12x faster                                                    |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                     |
| json_loads           | 28.5 us                                                | 26.3 us: 1.08x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 100 ms: 1.07x faster                                                     |
| pickle_pure_python   | 324 us                                                 | 316 us: 1.02x faster                                                     |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                    |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.93 ms: 1.20x faster                                                    |
| django_template | 34.6 ms                                                | 33.4 ms: 1.04x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 326 ms: 1.44x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 399 ms: 1.44x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 314 ms: 1.43x faster                                                     |
| deepcopy                   | 371 us                                                 | 267 us: 1.39x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 415 ms: 1.39x faster                                                     |
| deepcopy_memo              | 40.7 us                                                | 29.3 us: 1.39x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 921 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 565 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 566 ms: 1.28x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 914 ms: 1.26x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.24x faster                                                    |
| comprehensions             | 21.8 us                                                | 17.7 us: 1.23x faster                                                    |
| scimark_fft                | 382 ms                                                 | 318 ms: 1.20x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 68.1 ms: 1.20x faster                                                    |
| mako                       | 11.9 ms                                                | 9.93 ms: 1.20x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 193 us: 1.19x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                    |
| tomli_loads                | 2.33 sec                                               | 1.97 sec: 1.18x faster                                                   |
| nbody                      | 97.0 ms                                                | 82.3 ms: 1.18x faster                                                    |
| logging_format             | 7.23 us                                                | 6.18 us: 1.17x faster                                                    |
| richards                   | 45.8 ms                                                | 39.4 ms: 1.16x faster                                                    |
| deltablue                  | 3.72 ms                                                | 3.22 ms: 1.16x faster                                                    |
| logging_simple             | 6.46 us                                                | 5.61 us: 1.15x faster                                                    |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 65.3 ms: 1.15x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 78.5 ms: 1.14x faster                                                    |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                     |
| chaos                      | 67.0 ms                                                | 59.3 ms: 1.13x faster                                                    |
| richards_super             | 51.5 ms                                                | 45.8 ms: 1.13x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 55.3 ms: 1.12x faster                                                    |
| pyflate                    | 482 ms                                                 | 439 ms: 1.10x faster                                                     |
| raytrace                   | 312 ms                                                 | 285 ms: 1.09x faster                                                     |
| json                       | 5.26 ms                                                | 4.80 ms: 1.09x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                     |
| float                      | 84.7 ms                                                | 77.8 ms: 1.09x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.67 ms: 1.08x faster                                                    |
| json_loads                 | 28.5 us                                                | 26.3 us: 1.08x faster                                                    |
| fannkuch                   | 417 ms                                                 | 385 ms: 1.08x faster                                                     |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.3 ms: 1.08x faster                                                    |
| sympy_sum                  | 169 ms                                                 | 157 ms: 1.08x faster                                                     |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 726 ms: 1.07x faster                                                     |
| go                         | 139 ms                                                 | 131 ms: 1.07x faster                                                     |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 100 ms: 1.07x faster                                                     |
| sympy_str                  | 300 ms                                                 | 283 ms: 1.06x faster                                                     |
| 2to3                       | 274 ms                                                 | 261 ms: 1.05x faster                                                     |
| logging_silent             | 104 ns                                                 | 100 ns: 1.04x faster                                                     |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                   |
| django_template            | 34.6 ms                                                | 33.4 ms: 1.04x faster                                                    |
| sympy_integrate            | 21.4 ms                                                | 20.7 ms: 1.03x faster                                                    |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.03x faster                                                    |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                                   |
| regex_effbot               | 3.61 ms                                                | 3.50 ms: 1.03x faster                                                    |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                                     |
| pickle_pure_python         | 324 us                                                 | 316 us: 1.02x faster                                                     |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                                    |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.02x faster                                                    |
| async_generators           | 463 ms                                                 | 455 ms: 1.02x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 67.4 ms: 1.02x faster                                                    |
| sqlglot_normalize          | 110 ms                                                 | 111 ms: 1.00x slower                                                     |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.01x slower                                                     |
| docutils                   | 2.77 sec                                               | 2.79 sec: 1.01x slower                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 55.7 ms: 1.02x slower                                                    |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                                    |
| pidigits                   | 187 ms                                                 | 191 ms: 1.02x slower                                                     |
| bench_thread_pool          | 842 us                                                 | 873 us: 1.04x slower                                                     |
| nqueens                    | 83.3 ms                                                | 87.9 ms: 1.06x slower                                                    |
| mdp                        | 2.63 sec                                               | 2.78 sec: 1.06x slower                                                   |
| regex_dna                  | 212 ms                                                 | 226 ms: 1.06x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                     |
| telco                      | 7.10 ms                                                | 7.63 ms: 1.07x slower                                                    |
| hexiom                     | 6.41 ms                                                | 7.11 ms: 1.11x slower                                                    |
| regex_v8                   | 23.1 ms                                                | 26.0 ms: 1.12x slower                                                    |
| coverage                   | 72.7 ms                                                | 84.2 ms: 1.16x slower                                                    |
| gc_traversal               | 3.79 ms                                                | 4.47 ms: 1.18x slower                                                    |
| generators                 | 31.2 ms                                                | 37.1 ms: 1.19x slower                                                    |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                    |
| create_gc_cycles           | 1.48 ms                                                | 2.64 ms: 1.79x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 79.4 ms: 3.31x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                             |

Benchmark hidden because not significant (3): spectral_norm, coroutines, sympy_expand
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241121-3.14.0a2+-7b551b8-JIT/bm-20241121-linux-x86_64-brandtbucher-warmup_side_2048-3.14.0a2+-7b551b8.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.073x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.10x