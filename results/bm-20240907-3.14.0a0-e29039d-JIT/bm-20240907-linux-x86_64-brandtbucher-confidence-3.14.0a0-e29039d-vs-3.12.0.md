# Results vs. 3.12.0

- fork: brandtbucher
- ref: confidence
- machine: linux-x86_64
- commit hash: e29039d
- commit date: 2024-09-07
- overall geometric mean: 1.090x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| docutils       | 2.77 sec                                               | 3.01 sec: 1.09x slower                                            |
| tornado_http   | 103 ms                                                 | 94.9 ms: 1.08x faster                                             |
| Geometric mean | (ref)                                                  | 1.00x slower                                                      |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 394 ms: 1.46x faster                                              |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 312 ms: 1.44x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 403 ms: 1.43x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 546 ms: 1.33x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 897 ms: 1.32x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 565 ms: 1.28x faster                                              |
| async_tree_io              | 1.16 sec                                               | 932 ms: 1.24x faster                                              |
| Geometric mean             | (ref)                                                  | 1.37x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.5 ms: 1.22x faster                                             |
| float          | 84.7 ms                                                | 70.3 ms: 1.20x faster                                             |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                  | 1.14x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 139 ms: 1.06x faster                                              |
| regex_dna      | 212 ms                                                 | 222 ms: 1.05x slower                                              |
| regex_effbot   | 3.61 ms                                                | 3.78 ms: 1.05x slower                                             |
| regex_v8       | 23.1 ms                                                | 24.8 ms: 1.07x slower                                             |
| Geometric mean | (ref)                                                  | 1.02x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.92 sec: 1.21x faster                                            |
| xml_etree_generate   | 89.2 ms                                                | 77.3 ms: 1.15x faster                                             |
| xml_etree_process    | 61.7 ms                                                | 54.8 ms: 1.13x faster                                             |
| xml_etree_parse      | 159 ms                                                 | 145 ms: 1.10x faster                                              |
| unpickle_pure_python | 230 us                                                 | 211 us: 1.09x faster                                              |
| xml_etree_iterparse  | 107 ms                                                 | 98.3 ms: 1.09x faster                                             |
| pickle_pure_python   | 324 us                                                 | 300 us: 1.08x faster                                              |
| unpickle             | 15.9 us                                                | 15.0 us: 1.06x faster                                             |
| pickle_dict          | 35.5 us                                                | 34.8 us: 1.02x faster                                             |
| unpickle_list        | 5.29 us                                                | 5.18 us: 1.02x faster                                             |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                             |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                             |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                      |

Benchmark hidden because not significant (2): pickle_list, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.16 ms: 1.03x slower                                             |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                             |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.84 ms: 1.21x faster                                             |
| django_template | 34.6 ms                                                | 35.5 ms: 1.03x slower                                             |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 26.8 us: 1.52x faster                                             |
| async_tree_memoization     | 578 ms                                                 | 394 ms: 1.46x faster                                              |
| async_tree_none            | 472 ms                                                 | 326 ms: 1.45x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 312 ms: 1.44x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 403 ms: 1.43x faster                                              |
| deepcopy                   | 371 us                                                 | 269 us: 1.38x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 546 ms: 1.33x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 897 ms: 1.32x faster                                              |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 565 ms: 1.28x faster                                              |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.25x faster                                             |
| async_tree_io              | 1.16 sec                                               | 932 ms: 1.24x faster                                              |
| crypto_pyaes               | 81.9 ms                                                | 66.0 ms: 1.24x faster                                             |
| scimark_fft                | 382 ms                                                 | 311 ms: 1.23x faster                                              |
| nbody                      | 97.0 ms                                                | 79.5 ms: 1.22x faster                                             |
| tomli_loads                | 2.33 sec                                               | 1.92 sec: 1.21x faster                                            |
| mako                       | 11.9 ms                                                | 9.84 ms: 1.21x faster                                             |
| float                      | 84.7 ms                                                | 70.3 ms: 1.20x faster                                             |
| richards_super             | 51.5 ms                                                | 43.0 ms: 1.20x faster                                             |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                             |
| scimark_monte_carlo        | 75.1 ms                                                | 63.1 ms: 1.19x faster                                             |
| richards                   | 45.8 ms                                                | 38.9 ms: 1.18x faster                                             |
| logging_format             | 7.23 us                                                | 6.19 us: 1.17x faster                                             |
| spectral_norm              | 115 ms                                                 | 98.6 ms: 1.17x faster                                             |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.36 ms: 1.16x faster                                             |
| deltablue                  | 3.72 ms                                                | 3.22 ms: 1.15x faster                                             |
| xml_etree_generate         | 89.2 ms                                                | 77.3 ms: 1.15x faster                                             |
| chaos                      | 67.0 ms                                                | 58.6 ms: 1.14x faster                                             |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                              |
| logging_simple             | 6.46 us                                                | 5.68 us: 1.14x faster                                             |
| scimark_sor                | 129 ms                                                 | 114 ms: 1.13x faster                                              |
| xml_etree_process          | 61.7 ms                                                | 54.8 ms: 1.13x faster                                             |
| fannkuch                   | 417 ms                                                 | 373 ms: 1.12x faster                                              |
| pyflate                    | 482 ms                                                 | 432 ms: 1.12x faster                                              |
| xml_etree_parse            | 159 ms                                                 | 145 ms: 1.10x faster                                              |
| unpickle_pure_python       | 230 us                                                 | 211 us: 1.09x faster                                              |
| xml_etree_iterparse        | 107 ms                                                 | 98.3 ms: 1.09x faster                                             |
| tornado_http               | 103 ms                                                 | 94.9 ms: 1.08x faster                                             |
| pprint_safe_repr           | 776 ms                                                 | 718 ms: 1.08x faster                                              |
| pickle_pure_python         | 324 us                                                 | 300 us: 1.08x faster                                              |
| go                         | 139 ms                                                 | 130 ms: 1.08x faster                                              |
| scimark_lu                 | 118 ms                                                 | 110 ms: 1.08x faster                                              |
| regex_compile              | 148 ms                                                 | 139 ms: 1.06x faster                                              |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.06x faster                                            |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                              |
| unpickle                   | 15.9 us                                                | 15.0 us: 1.06x faster                                             |
| coroutines                 | 23.2 ms                                                | 22.3 ms: 1.04x faster                                             |
| sqlite_synth               | 2.83 us                                                | 2.74 us: 1.03x faster                                             |
| logging_silent             | 104 ns                                                 | 102 ns: 1.03x faster                                              |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.03x faster                                             |
| pickle_dict                | 35.5 us                                                | 34.8 us: 1.02x faster                                             |
| unpickle_list              | 5.29 us                                                | 5.18 us: 1.02x faster                                             |
| async_generators           | 463 ms                                                 | 456 ms: 1.02x faster                                              |
| gc_traversal               | 3.79 ms                                                | 3.74 ms: 1.01x faster                                             |
| mdp                        | 2.63 sec                                               | 2.60 sec: 1.01x faster                                            |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                             |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                              |
| sqlglot_transpile          | 1.68 ms                                                | 1.67 ms: 1.01x faster                                             |
| bench_thread_pool          | 842 us                                                 | 836 us: 1.01x faster                                              |
| sympy_str                  | 300 ms                                                 | 298 ms: 1.01x faster                                              |
| asyncio_tcp                | 491 ms                                                 | 488 ms: 1.00x faster                                              |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                              |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                            |
| json                       | 5.26 ms                                                | 5.32 ms: 1.01x slower                                             |
| sympy_sum                  | 169 ms                                                 | 172 ms: 1.02x slower                                              |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                             |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                              |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                            |
| nqueens                    | 83.3 ms                                                | 85.5 ms: 1.03x slower                                             |
| django_template            | 34.6 ms                                                | 35.5 ms: 1.03x slower                                             |
| python_startup_no_site     | 6.94 ms                                                | 7.16 ms: 1.03x slower                                             |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                              |
| regex_dna                  | 212 ms                                                 | 222 ms: 1.05x slower                                              |
| regex_effbot               | 3.61 ms                                                | 3.78 ms: 1.05x slower                                             |
| generators                 | 31.2 ms                                                | 32.9 ms: 1.05x slower                                             |
| sympy_expand               | 478 ms                                                 | 505 ms: 1.06x slower                                              |
| sqlglot_optimize           | 54.8 ms                                                | 57.9 ms: 1.06x slower                                             |
| sympy_integrate            | 21.4 ms                                                | 22.7 ms: 1.06x slower                                             |
| hexiom                     | 6.41 ms                                                | 6.83 ms: 1.07x slower                                             |
| regex_v8                   | 23.1 ms                                                | 24.8 ms: 1.07x slower                                             |
| docutils                   | 2.77 sec                                               | 3.01 sec: 1.09x slower                                            |
| telco                      | 7.10 ms                                                | 7.81 ms: 1.10x slower                                             |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                             |
| coverage                   | 72.7 ms                                                | 85.8 ms: 1.18x slower                                             |
| create_gc_cycles           | 1.48 ms                                                | 1.76 ms: 1.19x slower                                             |
| unpack_sequence            | 54.0 ns                                                | 107 ns: 1.98x slower                                              |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                      |

Benchmark hidden because not significant (5): bench_mp_pool, pickle_list, 2to3, dulwich_log, json_loads
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240907-3.14.0a0-e29039d-JIT/bm-20240907-linux-x86_64-brandtbucher-confidence-3.14.0a0-e29039d.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.090x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.06x