# Results vs. 3.12.0

- fork: brandtbucher
- ref: warmup_side_16384
- machine: linux-x86_64
- commit hash: 5092a50
- commit date: 2024-11-21
- overall geometric mean: 1.076x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.06x faster                                                      |
| docutils       | 2.77 sec                                               | 2.75 sec: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 398 ms: 1.44x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 314 ms: 1.43x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 410 ms: 1.41x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 911 ms: 1.30x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 568 ms: 1.28x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 909 ms: 1.27x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 83.4 ms: 1.16x faster                                                     |
| float          | 84.7 ms                                                | 78.9 ms: 1.07x faster                                                     |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.08x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.42 ms: 1.06x faster                                                     |
| regex_dna      | 212 ms                                                 | 223 ms: 1.05x slower                                                      |
| regex_v8       | 23.1 ms                                                | 24.9 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                    |
| unpickle_pure_python | 230 us                                                 | 194 us: 1.18x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 78.7 ms: 1.13x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 55.7 ms: 1.11x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.09x faster                                                      |
| json_loads           | 28.5 us                                                | 26.3 us: 1.08x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                      |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                              |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.11 ms: 1.02x slower                                                     |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.18x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                     |
| django_template | 34.6 ms                                                | 33.4 ms: 1.04x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 398 ms: 1.44x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 314 ms: 1.43x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 410 ms: 1.41x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 29.3 us: 1.39x faster                                                     |
| deepcopy                   | 371 us                                                 | 269 us: 1.38x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 911 ms: 1.30x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 566 ms: 1.28x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 568 ms: 1.28x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 909 ms: 1.27x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.78 us: 1.20x faster                                                     |
| comprehensions             | 21.8 us                                                | 18.2 us: 1.20x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 68.4 ms: 1.20x faster                                                     |
| scimark_fft                | 382 ms                                                 | 320 ms: 1.19x faster                                                      |
| logging_format             | 7.23 us                                                | 6.09 us: 1.19x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 194 us: 1.18x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.49 us: 1.18x faster                                                     |
| mako                       | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.16 ms: 1.17x faster                                                     |
| nbody                      | 97.0 ms                                                | 83.4 ms: 1.16x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 64.8 ms: 1.16x faster                                                     |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                      |
| richards                   | 45.8 ms                                                | 40.2 ms: 1.14x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 78.7 ms: 1.13x faster                                                     |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                      |
| chaos                      | 67.0 ms                                                | 59.7 ms: 1.12x faster                                                     |
| richards_super             | 51.5 ms                                                | 46.2 ms: 1.12x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 55.7 ms: 1.11x faster                                                     |
| go                         | 139 ms                                                 | 126 ms: 1.10x faster                                                      |
| raytrace                   | 312 ms                                                 | 283 ms: 1.10x faster                                                      |
| sympy_sum                  | 169 ms                                                 | 153 ms: 1.10x faster                                                      |
| json                       | 5.26 ms                                                | 4.81 ms: 1.09x faster                                                     |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.1 ms: 1.09x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.64 ms: 1.09x faster                                                     |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.09x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.09x faster                                                      |
| json_loads                 | 28.5 us                                                | 26.3 us: 1.08x faster                                                     |
| fannkuch                   | 417 ms                                                 | 386 ms: 1.08x faster                                                      |
| sympy_str                  | 300 ms                                                 | 279 ms: 1.07x faster                                                      |
| float                      | 84.7 ms                                                | 78.9 ms: 1.07x faster                                                     |
| pyflate                    | 482 ms                                                 | 452 ms: 1.07x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 727 ms: 1.07x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 111 ms: 1.07x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                      |
| regex_effbot               | 3.61 ms                                                | 3.42 ms: 1.06x faster                                                     |
| 2to3                       | 274 ms                                                 | 260 ms: 1.06x faster                                                      |
| logging_silent             | 104 ns                                                 | 98.9 ns: 1.06x faster                                                     |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.04x faster                                                    |
| sqlglot_parse              | 1.36 ms                                                | 1.30 ms: 1.04x faster                                                     |
| sqlglot_transpile          | 1.68 ms                                                | 1.61 ms: 1.04x faster                                                     |
| sympy_integrate            | 21.4 ms                                                | 20.6 ms: 1.04x faster                                                     |
| django_template            | 34.6 ms                                                | 33.4 ms: 1.04x faster                                                     |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                      |
| coroutines                 | 23.2 ms                                                | 22.5 ms: 1.03x faster                                                     |
| async_generators           | 463 ms                                                 | 453 ms: 1.02x faster                                                      |
| dulwich_log                | 68.5 ms                                                | 67.5 ms: 1.02x faster                                                     |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                                     |
| docutils                   | 2.77 sec                                               | 2.75 sec: 1.01x faster                                                    |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                                      |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.01x slower                                                      |
| sqlglot_normalize          | 110 ms                                                 | 111 ms: 1.01x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 55.3 ms: 1.01x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 7.11 ms: 1.02x slower                                                     |
| spectral_norm              | 115 ms                                                 | 119 ms: 1.03x slower                                                      |
| bench_thread_pool          | 842 us                                                 | 875 us: 1.04x slower                                                      |
| mdp                        | 2.63 sec                                               | 2.75 sec: 1.05x slower                                                    |
| hexiom                     | 6.41 ms                                                | 6.73 ms: 1.05x slower                                                     |
| regex_dna                  | 212 ms                                                 | 223 ms: 1.05x slower                                                      |
| nqueens                    | 83.3 ms                                                | 87.8 ms: 1.05x slower                                                     |
| telco                      | 7.10 ms                                                | 7.49 ms: 1.05x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 24.9 ms: 1.08x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                     |
| generators                 | 31.2 ms                                                | 35.2 ms: 1.13x slower                                                     |
| coverage                   | 72.7 ms                                                | 84.1 ms: 1.16x slower                                                     |
| gc_traversal               | 3.79 ms                                                | 4.68 ms: 1.23x slower                                                     |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 2.67 ms: 1.81x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 79.2 ms: 3.30x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                              |

Benchmark hidden because not significant (3): pycparser, sympy_expand, pickle_pure_python
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241121-3.14.0a2+-5092a50-JIT/bm-20241121-linux-x86_64-brandtbucher-warmup_side_16384-3.14.0a2+-5092a50.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.076x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.10x