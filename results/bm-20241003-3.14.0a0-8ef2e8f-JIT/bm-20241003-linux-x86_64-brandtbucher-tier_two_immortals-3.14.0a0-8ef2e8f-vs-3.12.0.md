# Results vs. 3.12.0

- fork: brandtbucher
- ref: tier_two_immortals
- machine: linux-x86_64
- commit hash: 8ef2e8f
- commit date: 2024-10-03
- overall geometric mean: 1.087x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 279 ms: 1.02x slower                                                      |
| docutils       | 2.77 sec                                               | 2.92 sec: 1.05x slower                                                    |
| tornado_http   | 103 ms                                                 | 94.9 ms: 1.08x faster                                                     |
| Geometric mean | (ref)                                                  | 1.00x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 317 ms: 1.49x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 387 ms: 1.48x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.46x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 408 ms: 1.42x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 872 ms: 1.36x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 547 ms: 1.33x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 885 ms: 1.31x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.28x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.8 ms: 1.18x faster                                                     |
| nbody          | 97.0 ms                                                | 82.3 ms: 1.18x faster                                                     |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.12x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 143 ms: 1.04x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.69 ms: 1.02x slower                                                     |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                      |
| regex_v8       | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                     |
| Geometric mean | (ref)                                                  | 1.03x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.90 sec: 1.22x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 76.8 ms: 1.16x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 54.4 ms: 1.13x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 145 ms: 1.10x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                 | 98.1 ms: 1.09x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                                      |
| json_loads           | 28.5 us                                                | 26.9 us: 1.06x faster                                                     |
| unpickle             | 15.9 us                                                | 15.0 us: 1.05x faster                                                     |
| pickle_pure_python   | 324 us                                                 | 309 us: 1.05x faster                                                      |
| pickle_list          | 5.08 us                                                | 4.91 us: 1.04x faster                                                     |
| pickle_dict          | 35.5 us                                                | 34.4 us: 1.03x faster                                                     |
| unpickle_list        | 5.29 us                                                | 5.16 us: 1.02x faster                                                     |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                     |
| pickle               | 11.6 us                                                | 11.4 us: 1.02x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                     |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.90 ms: 1.20x faster                                                     |
| django_template | 34.6 ms                                                | 36.9 ms: 1.07x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 40.7 us                                                | 27.1 us: 1.50x faster                                                     |
| async_tree_none            | 472 ms                                                 | 317 ms: 1.49x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 387 ms: 1.48x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.46x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 408 ms: 1.42x faster                                                      |
| deepcopy                   | 371 us                                                 | 271 us: 1.37x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 872 ms: 1.36x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 547 ms: 1.33x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 885 ms: 1.31x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                                     |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 569 ms: 1.28x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.65 us: 1.26x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 65.4 ms: 1.25x faster                                                     |
| scimark_fft                | 382 ms                                                 | 307 ms: 1.24x faster                                                      |
| pathlib                    | 19.3 ms                                                | 15.6 ms: 1.24x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.90 sec: 1.22x faster                                                    |
| mako                       | 11.9 ms                                                | 9.90 ms: 1.20x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 62.5 ms: 1.20x faster                                                     |
| float                      | 84.7 ms                                                | 71.8 ms: 1.18x faster                                                     |
| nbody                      | 97.0 ms                                                | 82.3 ms: 1.18x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.19 ms: 1.16x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 76.8 ms: 1.16x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.36 ms: 1.16x faster                                                     |
| richards                   | 45.8 ms                                                | 39.5 ms: 1.16x faster                                                     |
| logging_format             | 7.23 us                                                | 6.28 us: 1.15x faster                                                     |
| richards_super             | 51.5 ms                                                | 44.7 ms: 1.15x faster                                                     |
| spectral_norm              | 115 ms                                                 | 100 ms: 1.14x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.67 us: 1.14x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 54.4 ms: 1.13x faster                                                     |
| chaos                      | 67.0 ms                                                | 59.7 ms: 1.12x faster                                                     |
| fannkuch                   | 417 ms                                                 | 372 ms: 1.12x faster                                                      |
| raytrace                   | 312 ms                                                 | 278 ms: 1.12x faster                                                      |
| pyflate                    | 482 ms                                                 | 435 ms: 1.11x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 145 ms: 1.10x faster                                                      |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.10x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 98.1 ms: 1.09x faster                                                     |
| tornado_http               | 103 ms                                                 | 94.9 ms: 1.08x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 110 ms: 1.07x faster                                                      |
| json_loads                 | 28.5 us                                                | 26.9 us: 1.06x faster                                                     |
| go                         | 139 ms                                                 | 132 ms: 1.06x faster                                                      |
| unpickle                   | 15.9 us                                                | 15.0 us: 1.05x faster                                                     |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 740 ms: 1.05x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 309 us: 1.05x faster                                                      |
| regex_compile              | 148 ms                                                 | 143 ms: 1.04x faster                                                      |
| json                       | 5.26 ms                                                | 5.06 ms: 1.04x faster                                                     |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                    |
| pickle_list                | 5.08 us                                                | 4.91 us: 1.04x faster                                                     |
| pickle_dict                | 35.5 us                                                | 34.4 us: 1.03x faster                                                     |
| coroutines                 | 23.2 ms                                                | 22.4 ms: 1.03x faster                                                     |
| sqlite_synth               | 2.83 us                                                | 2.76 us: 1.03x faster                                                     |
| async_generators           | 463 ms                                                 | 452 ms: 1.02x faster                                                      |
| unpickle_list              | 5.29 us                                                | 5.16 us: 1.02x faster                                                     |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                     |
| pickle                     | 11.6 us                                                | 11.4 us: 1.02x faster                                                     |
| pprint_pformat             | 1.57 sec                                               | 1.55 sec: 1.01x faster                                                    |
| asyncio_tcp                | 491 ms                                                 | 484 ms: 1.01x faster                                                      |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.35 ms: 1.01x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 68.2 ms: 1.00x faster                                                     |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                    |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                      |
| sympy_str                  | 300 ms                                                 | 303 ms: 1.01x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                     |
| gc_traversal               | 3.79 ms                                                | 3.85 ms: 1.01x slower                                                     |
| 2to3                       | 274 ms                                                 | 279 ms: 1.02x slower                                                      |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                                    |
| regex_effbot               | 3.61 ms                                                | 3.69 ms: 1.02x slower                                                     |
| nqueens                    | 83.3 ms                                                | 85.9 ms: 1.03x slower                                                     |
| sympy_sum                  | 169 ms                                                 | 175 ms: 1.03x slower                                                      |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.04x slower                                                      |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                      |
| docutils                   | 2.77 sec                                               | 2.92 sec: 1.05x slower                                                    |
| telco                      | 7.10 ms                                                | 7.49 ms: 1.05x slower                                                     |
| sympy_expand               | 478 ms                                                 | 505 ms: 1.06x slower                                                      |
| bench_thread_pool          | 842 us                                                 | 896 us: 1.06x slower                                                      |
| django_template            | 34.6 ms                                                | 36.9 ms: 1.07x slower                                                     |
| hexiom                     | 6.41 ms                                                | 6.95 ms: 1.08x slower                                                     |
| sympy_integrate            | 21.4 ms                                                | 23.4 ms: 1.09x slower                                                     |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                                     |
| sqlglot_optimize           | 54.8 ms                                                | 60.3 ms: 1.10x slower                                                     |
| regex_v8                   | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                     |
| generators                 | 31.2 ms                                                | 34.5 ms: 1.11x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 1.73 ms: 1.18x slower                                                     |
| coverage                   | 72.7 ms                                                | 85.8 ms: 1.18x slower                                                     |
| unpack_sequence            | 54.0 ns                                                | 108 ns: 2.01x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 60.2 ms: 2.51x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                              |

Benchmark hidden because not significant (2): logging_silent, sqlglot_transpile
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241003-3.14.0a0-8ef2e8f-JIT/bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.087x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.03x