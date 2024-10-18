# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_likely
- machine: linux-x86_64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.03x faster
- HPT reliability: 99.77%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 278 ms: 1.01x slower                                                  |
| docutils       | 2.77 sec                                               | 2.92 sec: 1.06x slower                                                |
| tornado_http   | 103 ms                                                 | 95.0 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 375 ms: 1.53x faster                                                  |
| async_tree_none            | 472 ms                                                 | 329 ms: 1.43x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 320 ms: 1.40x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 420 ms: 1.38x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 854 ms: 1.35x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 556 ms: 1.31x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 572 ms: 1.27x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 971 ms: 1.22x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 84.5 ms: 1.15x faster                                                 |
| float          | 84.7 ms                                                | 76.0 ms: 1.11x faster                                                 |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 143 ms: 1.04x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                 |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                                  |
| regex_v8       | 23.1 ms                                                | 24.7 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 78.8 ms: 1.13x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 55.5 ms: 1.11x faster                                                 |
| unpickle             | 15.9 us                                                | 14.3 us: 1.11x faster                                                 |
| json_loads           | 28.5 us                                                | 26.5 us: 1.07x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 99.7 ms: 1.07x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.05x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 313 us: 1.04x faster                                                  |
| pickle_dict          | 35.5 us                                                | 34.8 us: 1.02x faster                                                 |
| pickle_list          | 5.08 us                                                | 5.13 us: 1.01x slower                                                 |
| pickle               | 11.6 us                                                | 11.9 us: 1.02x slower                                                 |
| unpickle_list        | 5.29 us                                                | 5.53 us: 1.05x slower                                                 |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                 |
| python_startup         | 9.55 ms                                                | 11.9 ms: 1.25x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                 |
| django_template | 34.6 ms                                                | 36.7 ms: 1.06x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 375 ms: 1.53x faster                                                  |
| async_tree_none            | 472 ms                                                 | 329 ms: 1.43x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 320 ms: 1.40x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 420 ms: 1.38x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.8 us: 1.37x faster                                                 |
| deepcopy                   | 371 us                                                 | 274 us: 1.35x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 854 ms: 1.35x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 556 ms: 1.31x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 572 ms: 1.27x faster                                                  |
| comprehensions             | 21.8 us                                                | 17.4 us: 1.25x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 971 ms: 1.22x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 67.7 ms: 1.21x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.20x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.81 us: 1.19x faster                                                 |
| logging_format             | 7.23 us                                                | 6.11 us: 1.18x faster                                                 |
| scimark_fft                | 382 ms                                                 | 323 ms: 1.18x faster                                                  |
| mako                       | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 63.9 ms: 1.18x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.62 us: 1.15x faster                                                 |
| nbody                      | 97.0 ms                                                | 84.5 ms: 1.15x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.27 ms: 1.14x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 78.8 ms: 1.13x faster                                                 |
| chaos                      | 67.0 ms                                                | 59.4 ms: 1.13x faster                                                 |
| raytrace                   | 312 ms                                                 | 278 ms: 1.12x faster                                                  |
| float                      | 84.7 ms                                                | 76.0 ms: 1.11x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 55.5 ms: 1.11x faster                                                 |
| richards                   | 45.8 ms                                                | 41.4 ms: 1.11x faster                                                 |
| unpickle                   | 15.9 us                                                | 14.3 us: 1.11x faster                                                 |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.10x faster                                                  |
| richards_super             | 51.5 ms                                                | 47.2 ms: 1.09x faster                                                 |
| tornado_http               | 103 ms                                                 | 95.0 ms: 1.08x faster                                                 |
| json                       | 5.26 ms                                                | 4.88 ms: 1.08x faster                                                 |
| json_loads                 | 28.5 us                                                | 26.5 us: 1.07x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 99.7 ms: 1.07x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                                  |
| pyflate                    | 482 ms                                                 | 455 ms: 1.06x faster                                                  |
| logging_silent             | 104 ns                                                 | 98.8 ns: 1.06x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.05x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.05x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 742 ms: 1.04x faster                                                  |
| go                         | 139 ms                                                 | 134 ms: 1.04x faster                                                  |
| fannkuch                   | 417 ms                                                 | 401 ms: 1.04x faster                                                  |
| regex_compile              | 148 ms                                                 | 143 ms: 1.04x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 313 us: 1.04x faster                                                  |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.04x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.90 ms: 1.03x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 66.7 ms: 1.03x faster                                                 |
| pickle_dict                | 35.5 us                                                | 34.8 us: 1.02x faster                                                 |
| async_generators           | 463 ms                                                 | 454 ms: 1.02x faster                                                  |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.34 ms: 1.02x faster                                                 |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                 |
| sqlite_synth               | 2.83 us                                                | 2.81 us: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                  |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.01x slower                                                  |
| pickle_list                | 5.08 us                                                | 5.13 us: 1.01x slower                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                |
| sympy_str                  | 300 ms                                                 | 303 ms: 1.01x slower                                                  |
| 2to3                       | 274 ms                                                 | 278 ms: 1.01x slower                                                  |
| asyncio_tcp                | 491 ms                                                 | 499 ms: 1.02x slower                                                  |
| regex_effbot               | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                 |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                 |
| pickle                     | 11.6 us                                                | 11.9 us: 1.02x slower                                                 |
| sympy_sum                  | 169 ms                                                 | 175 ms: 1.04x slower                                                  |
| sqlglot_normalize          | 110 ms                                                 | 115 ms: 1.04x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 878 us: 1.04x slower                                                  |
| unpickle_list              | 5.29 us                                                | 5.53 us: 1.05x slower                                                 |
| mdp                        | 2.63 sec                                               | 2.75 sec: 1.05x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                  |
| docutils                   | 2.77 sec                                               | 2.92 sec: 1.06x slower                                                |
| sympy_expand               | 478 ms                                                 | 505 ms: 1.06x slower                                                  |
| django_template            | 34.6 ms                                                | 36.7 ms: 1.06x slower                                                 |
| nqueens                    | 83.3 ms                                                | 88.6 ms: 1.06x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 24.7 ms: 1.07x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                 |
| telco                      | 7.10 ms                                                | 7.69 ms: 1.08x slower                                                 |
| hexiom                     | 6.41 ms                                                | 7.07 ms: 1.10x slower                                                 |
| sympy_integrate            | 21.4 ms                                                | 23.6 ms: 1.10x slower                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 60.6 ms: 1.11x slower                                                 |
| generators                 | 31.2 ms                                                | 35.2 ms: 1.13x slower                                                 |
| coverage                   | 72.7 ms                                                | 84.6 ms: 1.16x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 4.52 ms: 1.19x slower                                                 |
| python_startup             | 9.55 ms                                                | 11.9 ms: 1.25x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.68 ms: 1.82x slower                                                 |
| unpack_sequence            | 54.0 ns                                                | 108 ns: 2.01x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 84.0 ms: 3.50x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (3): pprint_pformat, pycparser, sqlglot_transpile
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (7) of results/bm-20241018-3.14.0a1+-bad9944-JIT/bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 99.77% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.15x