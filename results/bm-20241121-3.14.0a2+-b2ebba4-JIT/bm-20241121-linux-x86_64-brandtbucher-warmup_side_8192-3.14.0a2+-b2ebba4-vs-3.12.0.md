# Results vs. 3.12.0

- fork: brandtbucher
- ref: warmup_side_8192
- machine: linux-x86_64
- commit hash: b2ebba4
- commit date: 2024-11-21
- overall geometric mean: 1.077x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.06x faster                                                     |
| docutils       | 2.77 sec                                               | 2.75 sec: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 324 ms: 1.46x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 399 ms: 1.44x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 315 ms: 1.43x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 410 ms: 1.41x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 911 ms: 1.30x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 560 ms: 1.30x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 565 ms: 1.28x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 909 ms: 1.27x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 81.4 ms: 1.19x faster                                                    |
| float          | 84.7 ms                                                | 78.4 ms: 1.08x faster                                                    |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.09x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                     |
| regex_effbot   | 3.61 ms                                                | 3.43 ms: 1.05x faster                                                    |
| regex_dna      | 212 ms                                                 | 224 ms: 1.06x slower                                                     |
| regex_v8       | 23.1 ms                                                | 26.0 ms: 1.12x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 230 us                                                 | 192 us: 1.20x faster                                                     |
| tomli_loads          | 2.33 sec                                               | 2.00 sec: 1.16x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 79.1 ms: 1.13x faster                                                    |
| xml_etree_process    | 61.7 ms                                                | 55.8 ms: 1.11x faster                                                    |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.10x faster                                                     |
| json_loads           | 28.5 us                                                | 26.2 us: 1.09x faster                                                    |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                     |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                             |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                    |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.35x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.3 ms: 1.16x faster                                                    |
| django_template | 34.6 ms                                                | 33.6 ms: 1.03x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 324 ms: 1.46x faster                                                     |
| async_tree_memoization_tg  | 575 ms                                                 | 399 ms: 1.44x faster                                                     |
| async_tree_none_tg         | 450 ms                                                 | 315 ms: 1.43x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 410 ms: 1.41x faster                                                     |
| deepcopy_memo              | 40.7 us                                                | 29.3 us: 1.39x faster                                                    |
| deepcopy                   | 371 us                                                 | 273 us: 1.36x faster                                                     |
| async_tree_io_tg           | 1.18 sec                                               | 911 ms: 1.30x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 560 ms: 1.30x faster                                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 565 ms: 1.28x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 909 ms: 1.27x faster                                                     |
| comprehensions             | 21.8 us                                                | 17.5 us: 1.25x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                | 2.75 us: 1.22x faster                                                    |
| scimark_fft                | 382 ms                                                 | 316 ms: 1.21x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 68.2 ms: 1.20x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 192 us: 1.20x faster                                                     |
| nbody                      | 97.0 ms                                                | 81.4 ms: 1.19x faster                                                    |
| logging_format             | 7.23 us                                                | 6.08 us: 1.19x faster                                                    |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.19x faster                                                    |
| richards                   | 45.8 ms                                                | 38.6 ms: 1.19x faster                                                    |
| deltablue                  | 3.72 ms                                                | 3.18 ms: 1.17x faster                                                    |
| tomli_loads                | 2.33 sec                                               | 2.00 sec: 1.16x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 64.6 ms: 1.16x faster                                                    |
| mako                       | 11.9 ms                                                | 10.3 ms: 1.16x faster                                                    |
| richards_super             | 51.5 ms                                                | 44.5 ms: 1.16x faster                                                    |
| logging_simple             | 6.46 us                                                | 5.59 us: 1.16x faster                                                    |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                     |
| sqlalchemy_declarative     | 147 ms                                                 | 129 ms: 1.14x faster                                                     |
| chaos                      | 67.0 ms                                                | 59.0 ms: 1.14x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 79.1 ms: 1.13x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 55.8 ms: 1.11x faster                                                    |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.0 ms: 1.10x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.62 ms: 1.10x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.10x faster                                                     |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                                     |
| raytrace                   | 312 ms                                                 | 286 ms: 1.09x faster                                                     |
| go                         | 139 ms                                                 | 128 ms: 1.09x faster                                                     |
| json_loads                 | 28.5 us                                                | 26.2 us: 1.09x faster                                                    |
| sympy_sum                  | 169 ms                                                 | 155 ms: 1.09x faster                                                     |
| float                      | 84.7 ms                                                | 78.4 ms: 1.08x faster                                                    |
| sympy_str                  | 300 ms                                                 | 281 ms: 1.07x faster                                                     |
| json                       | 5.26 ms                                                | 4.93 ms: 1.07x faster                                                    |
| scimark_lu                 | 118 ms                                                 | 111 ms: 1.06x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 731 ms: 1.06x faster                                                     |
| pyflate                    | 482 ms                                                 | 455 ms: 1.06x faster                                                     |
| fannkuch                   | 417 ms                                                 | 394 ms: 1.06x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                     |
| 2to3                       | 274 ms                                                 | 260 ms: 1.06x faster                                                     |
| regex_effbot               | 3.61 ms                                                | 3.43 ms: 1.05x faster                                                    |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.05x faster                                                   |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.05x faster                                                   |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                                    |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.04x faster                                                     |
| sympy_integrate            | 21.4 ms                                                | 20.7 ms: 1.03x faster                                                    |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                     |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                    |
| django_template            | 34.6 ms                                                | 33.6 ms: 1.03x faster                                                    |
| dulwich_log                | 68.5 ms                                                | 67.1 ms: 1.02x faster                                                    |
| logging_silent             | 104 ns                                                 | 103 ns: 1.02x faster                                                     |
| async_generators           | 463 ms                                                 | 456 ms: 1.01x faster                                                     |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                                    |
| docutils                   | 2.77 sec                                               | 2.75 sec: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                     |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.01x slower                                                     |
| sqlglot_normalize          | 110 ms                                                 | 111 ms: 1.01x slower                                                     |
| sqlglot_optimize           | 54.8 ms                                                | 55.5 ms: 1.01x slower                                                    |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                    |
| bench_thread_pool          | 842 us                                                 | 871 us: 1.03x slower                                                     |
| regex_dna                  | 212 ms                                                 | 224 ms: 1.06x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                     |
| mdp                        | 2.63 sec                                               | 2.78 sec: 1.06x slower                                                   |
| nqueens                    | 83.3 ms                                                | 89.4 ms: 1.07x slower                                                    |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                    |
| telco                      | 7.10 ms                                                | 7.67 ms: 1.08x slower                                                    |
| hexiom                     | 6.41 ms                                                | 6.96 ms: 1.09x slower                                                    |
| regex_v8                   | 23.1 ms                                                | 26.0 ms: 1.12x slower                                                    |
| generators                 | 31.2 ms                                                | 35.6 ms: 1.14x slower                                                    |
| gc_traversal               | 3.79 ms                                                | 4.35 ms: 1.15x slower                                                    |
| coverage                   | 72.7 ms                                                | 84.3 ms: 1.16x slower                                                    |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.35x slower                                                    |
| create_gc_cycles           | 1.48 ms                                                | 2.64 ms: 1.79x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 79.3 ms: 3.30x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                             |

Benchmark hidden because not significant (3): coroutines, sympy_expand, pickle_pure_python
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241121-3.14.0a2+-b2ebba4-JIT/bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.077x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.10x