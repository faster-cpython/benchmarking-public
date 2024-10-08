# Results vs. 3.12.0

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: linux-aarch64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 374 ms: 1.21x slower                                                      |
| docutils       | 2.98 sec                                                              | 3.85 sec: 1.29x slower                                                    |
| html5lib       | 65.1 ms                                                               | 71.3 ms: 1.10x slower                                                     |
| tornado_http   | 136 ms                                                                | 146 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.17x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 435 ms: 1.43x faster                                                      |
| async_tree_none_tg         | 577 ms                                                                | 421 ms: 1.37x faster                                                      |
| async_tree_memoization     | 777 ms                                                                | 582 ms: 1.34x faster                                                      |
| async_tree_memoization_tg  | 740 ms                                                                | 562 ms: 1.32x faster                                                      |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 746 ms: 1.22x faster                                                      |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 743 ms: 1.19x faster                                                      |
| Geometric mean             | (ref)                                                                 | 1.28x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 87.4 ms: 1.05x faster                                                     |
| nbody          | 105 ms                                                                | 113 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 259 ms: 1.02x slower                                                      |
| regex_effbot   | 4.64 ms                                                               | 5.00 ms: 1.08x slower                                                     |
| regex_v8       | 28.3 ms                                                               | 31.0 ms: 1.09x slower                                                     |
| regex_compile  | 137 ms                                                                | 189 ms: 1.38x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.13x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 191 ms: 1.02x faster                                                      |
| pickle_list          | 5.25 us                                                               | 5.16 us: 1.02x faster                                                     |
| xml_etree_iterparse  | 150 ms                                                                | 148 ms: 1.02x faster                                                      |
| tomli_loads          | 2.59 sec                                                              | 2.58 sec: 1.00x faster                                                    |
| unpickle_pure_python | 260 us                                                                | 263 us: 1.01x slower                                                      |
| pickle               | 13.4 us                                                               | 13.6 us: 1.02x slower                                                     |
| json_loads           | 30.7 us                                                               | 31.4 us: 1.02x slower                                                     |
| pickle_dict          | 37.3 us                                                               | 38.4 us: 1.03x slower                                                     |
| pickle_pure_python   | 365 us                                                                | 377 us: 1.03x slower                                                      |
| unpickle_list        | 6.17 us                                                               | 6.40 us: 1.04x slower                                                     |
| unpickle             | 18.5 us                                                               | 19.3 us: 1.04x slower                                                     |
| json_dumps           | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                              |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.72 ms: 1.04x slower                                                     |
| python_startup         | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.0 ms: 1.01x slower                                                     |
| django_template | 40.7 ms                                                               | 50.0 ms: 1.23x slower                                                     |
| genshi_text     | 27.4 ms                                                               | 34.6 ms: 1.26x slower                                                     |
| genshi_xml      | 60.6 ms                                                               | 80.5 ms: 1.33x slower                                                     |
| Geometric mean  | (ref)                                                                 | 1.20x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 435 ms: 1.43x faster                                                      |
| async_tree_none_tg         | 577 ms                                                                | 421 ms: 1.37x faster                                                      |
| deepcopy_memo              | 49.6 us                                                               | 36.5 us: 1.36x faster                                                     |
| async_tree_memoization     | 777 ms                                                                | 582 ms: 1.34x faster                                                      |
| async_tree_memoization_tg  | 740 ms                                                                | 562 ms: 1.32x faster                                                      |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 746 ms: 1.22x faster                                                      |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                    |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 743 ms: 1.19x faster                                                      |
| deepcopy                   | 446 us                                                                | 385 us: 1.16x faster                                                      |
| pathlib                    | 24.5 ms                                                               | 21.8 ms: 1.13x faster                                                     |
| deepcopy_reduce            | 4.10 us                                                               | 3.79 us: 1.08x faster                                                     |
| float                      | 92.1 ms                                                               | 87.4 ms: 1.05x faster                                                     |
| comprehensions             | 25.4 us                                                               | 24.1 us: 1.05x faster                                                     |
| raytrace                   | 353 ms                                                                | 342 ms: 1.03x faster                                                      |
| xml_etree_parse            | 195 ms                                                                | 191 ms: 1.02x faster                                                      |
| logging_simple             | 7.63 us                                                               | 7.48 us: 1.02x faster                                                     |
| coroutines                 | 29.0 ms                                                               | 28.4 ms: 1.02x faster                                                     |
| logging_format             | 8.34 us                                                               | 8.19 us: 1.02x faster                                                     |
| pickle_list                | 5.25 us                                                               | 5.16 us: 1.02x faster                                                     |
| xml_etree_iterparse        | 150 ms                                                                | 148 ms: 1.02x faster                                                      |
| tomli_loads                | 2.59 sec                                                              | 2.58 sec: 1.00x faster                                                    |
| mako                       | 12.9 ms                                                               | 13.0 ms: 1.01x slower                                                     |
| unpickle_pure_python       | 260 us                                                                | 263 us: 1.01x slower                                                      |
| crypto_pyaes               | 86.6 ms                                                               | 87.9 ms: 1.01x slower                                                     |
| pickle                     | 13.4 us                                                               | 13.6 us: 1.02x slower                                                     |
| mdp                        | 3.41 sec                                                              | 3.47 sec: 1.02x slower                                                    |
| bench_thread_pool          | 1.31 ms                                                               | 1.33 ms: 1.02x slower                                                     |
| regex_dna                  | 254 ms                                                                | 259 ms: 1.02x slower                                                      |
| json                       | 5.54 ms                                                               | 5.65 ms: 1.02x slower                                                     |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.23 sec: 1.02x slower                                                    |
| json_loads                 | 30.7 us                                                               | 31.4 us: 1.02x slower                                                     |
| scimark_lu                 | 146 ms                                                                | 149 ms: 1.02x slower                                                      |
| thrift                     | 937 us                                                                | 961 us: 1.03x slower                                                      |
| pickle_dict                | 37.3 us                                                               | 38.4 us: 1.03x slower                                                     |
| async_generators           | 491 ms                                                                | 506 ms: 1.03x slower                                                      |
| pickle_pure_python         | 365 us                                                                | 377 us: 1.03x slower                                                      |
| unpickle_list              | 6.17 us                                                               | 6.40 us: 1.04x slower                                                     |
| python_startup_no_site     | 8.37 ms                                                               | 8.72 ms: 1.04x slower                                                     |
| unpickle                   | 18.5 us                                                               | 19.3 us: 1.04x slower                                                     |
| bench_mp_pool              | 7.05 ms                                                               | 7.42 ms: 1.05x slower                                                     |
| deltablue                  | 4.12 ms                                                               | 4.34 ms: 1.05x slower                                                     |
| scimark_monte_carlo        | 85.1 ms                                                               | 91.0 ms: 1.07x slower                                                     |
| scimark_fft                | 418 ms                                                                | 448 ms: 1.07x slower                                                      |
| logging_silent             | 127 ns                                                                | 136 ns: 1.07x slower                                                      |
| asyncio_tcp                | 566 ms                                                                | 610 ms: 1.08x slower                                                      |
| tornado_http               | 136 ms                                                                | 146 ms: 1.08x slower                                                      |
| regex_effbot               | 4.64 ms                                                               | 5.00 ms: 1.08x slower                                                     |
| nbody                      | 105 ms                                                                | 113 ms: 1.08x slower                                                      |
| regex_v8                   | 28.3 ms                                                               | 31.0 ms: 1.09x slower                                                     |
| html5lib                   | 65.1 ms                                                               | 71.3 ms: 1.10x slower                                                     |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.80 ms: 1.10x slower                                                     |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                     |
| meteor_contest             | 112 ms                                                                | 123 ms: 1.10x slower                                                      |
| fannkuch                   | 443 ms                                                                | 490 ms: 1.10x slower                                                      |
| spectral_norm              | 131 ms                                                                | 144 ms: 1.11x slower                                                      |
| pyflate                    | 559 ms                                                                | 623 ms: 1.11x slower                                                      |
| typing_runtime_protocols   | 181 us                                                                | 207 us: 1.15x slower                                                      |
| coverage                   | 87.3 ms                                                               | 100 ms: 1.15x slower                                                      |
| python_startup             | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                     |
| sqlglot_parse              | 1.46 ms                                                               | 1.72 ms: 1.17x slower                                                     |
| pycparser                  | 1.26 sec                                                              | 1.48 sec: 1.17x slower                                                    |
| go                         | 157 ms                                                                | 185 ms: 1.17x slower                                                      |
| telco                      | 8.51 ms                                                               | 10.0 ms: 1.18x slower                                                     |
| sqlglot_transpile          | 1.83 ms                                                               | 2.16 ms: 1.18x slower                                                     |
| gc_traversal               | 4.40 ms                                                               | 5.19 ms: 1.18x slower                                                     |
| sqlglot_normalize          | 126 ms                                                                | 149 ms: 1.18x slower                                                      |
| nqueens                    | 99.2 ms                                                               | 119 ms: 1.20x slower                                                      |
| create_gc_cycles           | 1.92 ms                                                               | 2.32 ms: 1.21x slower                                                     |
| 2to3                       | 308 ms                                                                | 374 ms: 1.21x slower                                                      |
| django_template            | 40.7 ms                                                               | 50.0 ms: 1.23x slower                                                     |
| chaos                      | 71.4 ms                                                               | 88.7 ms: 1.24x slower                                                     |
| richards_super             | 58.5 ms                                                               | 72.8 ms: 1.24x slower                                                     |
| genshi_text                | 27.4 ms                                                               | 34.6 ms: 1.26x slower                                                     |
| richards                   | 50.9 ms                                                               | 64.8 ms: 1.27x slower                                                     |
| sympy_str                  | 280 ms                                                                | 359 ms: 1.28x slower                                                      |
| sqlglot_optimize           | 61.3 ms                                                               | 79.0 ms: 1.29x slower                                                     |
| docutils                   | 2.98 sec                                                              | 3.85 sec: 1.29x slower                                                    |
| sympy_integrate            | 21.6 ms                                                               | 28.2 ms: 1.30x slower                                                     |
| generators                 | 43.5 ms                                                               | 56.9 ms: 1.31x slower                                                     |
| sympy_expand               | 454 ms                                                                | 600 ms: 1.32x slower                                                      |
| pprint_safe_repr           | 916 ms                                                                | 1.21 sec: 1.32x slower                                                    |
| dulwich_log                | 62.0 ms                                                               | 82.2 ms: 1.33x slower                                                     |
| pprint_pformat             | 1.88 sec                                                              | 2.50 sec: 1.33x slower                                                    |
| genshi_xml                 | 60.6 ms                                                               | 80.5 ms: 1.33x slower                                                     |
| pylint                     | 355 ms                                                                | 474 ms: 1.34x slower                                                      |
| sympy_sum                  | 154 ms                                                                | 208 ms: 1.34x slower                                                      |
| regex_compile              | 137 ms                                                                | 189 ms: 1.38x slower                                                      |
| hexiom                     | 6.98 ms                                                               | 9.84 ms: 1.41x slower                                                     |
| Geometric mean             | (ref)                                                                 | 1.07x slower                                                              |

Benchmark hidden because not significant (6): scimark_sor, xml_etree_process, asyncio_websockets, pidigits, sqlite_synth, xml_etree_generate
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240926-3.14.0a0-7f9fe5a-JIT/bm-20240926-arminc-aarch64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json: bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.00x