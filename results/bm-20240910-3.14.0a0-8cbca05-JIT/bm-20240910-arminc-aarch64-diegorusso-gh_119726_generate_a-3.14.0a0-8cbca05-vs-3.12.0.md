# Results vs. 3.12.0

- fork: diegorusso
- ref: gh_119726_generate_a
- machine: linux-aarch64
- commit hash: 8cbca05
- commit date: 2024-09-10
- overall geometric mean: 1.069x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 376 ms: 1.22x slower                                                        |
| docutils       | 2.98 sec                                                              | 3.94 sec: 1.32x slower                                                      |
| html5lib       | 65.1 ms                                                               | 71.4 ms: 1.10x slower                                                       |
| tornado_http   | 136 ms                                                                | 151 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.18x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 449 ms: 1.39x faster                                                        |
| async_tree_none_tg         | 577 ms                                                                | 423 ms: 1.36x faster                                                        |
| async_tree_memoization_tg  | 740 ms                                                                | 550 ms: 1.35x faster                                                        |
| async_tree_memoization     | 777 ms                                                                | 583 ms: 1.33x faster                                                        |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.23x faster                                                      |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 725 ms: 1.22x faster                                                        |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 761 ms: 1.20x faster                                                        |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                      |
| Geometric mean             | (ref)                                                                 | 1.28x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 87.8 ms: 1.05x faster                                                       |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                        |
| nbody          | 105 ms                                                                | 111 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.99 ms: 1.08x slower                                                       |
| regex_v8       | 28.3 ms                                                               | 30.8 ms: 1.09x slower                                                       |
| regex_compile  | 137 ms                                                                | 186 ms: 1.35x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 187 ms: 1.05x faster                                                        |
| xml_etree_generate   | 112 ms                                                                | 110 ms: 1.02x faster                                                        |
| xml_etree_iterparse  | 150 ms                                                                | 149 ms: 1.01x faster                                                        |
| xml_etree_process    | 79.0 ms                                                               | 79.7 ms: 1.01x slower                                                       |
| tomli_loads          | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                      |
| unpickle_pure_python | 260 us                                                                | 264 us: 1.02x slower                                                        |
| pickle_dict          | 37.3 us                                                               | 38.0 us: 1.02x slower                                                       |
| json_loads           | 30.7 us                                                               | 31.3 us: 1.02x slower                                                       |
| pickle               | 13.4 us                                                               | 13.7 us: 1.02x slower                                                       |
| unpickle_list        | 6.17 us                                                               | 6.34 us: 1.03x slower                                                       |
| unpickle             | 18.5 us                                                               | 19.3 us: 1.04x slower                                                       |
| pickle_pure_python   | 365 us                                                                | 384 us: 1.05x slower                                                        |
| json_dumps           | 12.3 ms                                                               | 13.9 ms: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                                 | 1.02x slower                                                                |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.74 ms: 1.04x slower                                                       |
| python_startup         | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.0 ms: 1.01x slower                                                       |
| django_template | 40.7 ms                                                               | 50.5 ms: 1.24x slower                                                       |
| genshi_text     | 27.4 ms                                                               | 34.9 ms: 1.27x slower                                                       |
| genshi_xml      | 60.6 ms                                                               | 81.5 ms: 1.34x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.21x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 449 ms: 1.39x faster                                                        |
| async_tree_none_tg         | 577 ms                                                                | 423 ms: 1.36x faster                                                        |
| async_tree_memoization_tg  | 740 ms                                                                | 550 ms: 1.35x faster                                                        |
| async_tree_memoization     | 777 ms                                                                | 583 ms: 1.33x faster                                                        |
| deepcopy_memo              | 49.6 us                                                               | 37.7 us: 1.32x faster                                                       |
| async_tree_io              | 1.41 sec                                                              | 1.15 sec: 1.23x faster                                                      |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 725 ms: 1.22x faster                                                        |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 761 ms: 1.20x faster                                                        |
| async_tree_io_tg           | 1.40 sec                                                              | 1.18 sec: 1.19x faster                                                      |
| pathlib                    | 24.5 ms                                                               | 21.7 ms: 1.13x faster                                                       |
| deepcopy                   | 446 us                                                                | 400 us: 1.11x faster                                                        |
| deepcopy_reduce            | 4.10 us                                                               | 3.86 us: 1.06x faster                                                       |
| float                      | 92.1 ms                                                               | 87.8 ms: 1.05x faster                                                       |
| xml_etree_parse            | 195 ms                                                                | 187 ms: 1.05x faster                                                        |
| logging_format             | 8.34 us                                                               | 8.00 us: 1.04x faster                                                       |
| comprehensions             | 25.4 us                                                               | 24.6 us: 1.03x faster                                                       |
| logging_simple             | 7.63 us                                                               | 7.40 us: 1.03x faster                                                       |
| xml_etree_generate         | 112 ms                                                                | 110 ms: 1.02x faster                                                        |
| raytrace                   | 353 ms                                                                | 348 ms: 1.02x faster                                                        |
| xml_etree_iterparse        | 150 ms                                                                | 149 ms: 1.01x faster                                                        |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                        |
| asyncio_websockets         | 658 ms                                                                | 663 ms: 1.01x slower                                                        |
| xml_etree_process          | 79.0 ms                                                               | 79.7 ms: 1.01x slower                                                       |
| mako                       | 12.9 ms                                                               | 13.0 ms: 1.01x slower                                                       |
| json                       | 5.54 ms                                                               | 5.61 ms: 1.01x slower                                                       |
| tomli_loads                | 2.59 sec                                                              | 2.63 sec: 1.01x slower                                                      |
| unpickle_pure_python       | 260 us                                                                | 264 us: 1.02x slower                                                        |
| pickle_dict                | 37.3 us                                                               | 38.0 us: 1.02x slower                                                       |
| json_loads                 | 30.7 us                                                               | 31.3 us: 1.02x slower                                                       |
| pickle                     | 13.4 us                                                               | 13.7 us: 1.02x slower                                                       |
| scimark_lu                 | 146 ms                                                                | 149 ms: 1.02x slower                                                        |
| mdp                        | 3.41 sec                                                              | 3.50 sec: 1.03x slower                                                      |
| unpickle_list              | 6.17 us                                                               | 6.34 us: 1.03x slower                                                       |
| bench_thread_pool          | 1.31 ms                                                               | 1.35 ms: 1.03x slower                                                       |
| thrift                     | 937 us                                                                | 966 us: 1.03x slower                                                        |
| async_generators           | 491 ms                                                                | 510 ms: 1.04x slower                                                        |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.28 sec: 1.04x slower                                                      |
| unpickle                   | 18.5 us                                                               | 19.3 us: 1.04x slower                                                       |
| python_startup_no_site     | 8.37 ms                                                               | 8.74 ms: 1.04x slower                                                       |
| crypto_pyaes               | 86.6 ms                                                               | 90.5 ms: 1.04x slower                                                       |
| pickle_pure_python         | 365 us                                                                | 384 us: 1.05x slower                                                        |
| deltablue                  | 4.12 ms                                                               | 4.33 ms: 1.05x slower                                                       |
| nbody                      | 105 ms                                                                | 111 ms: 1.06x slower                                                        |
| regex_effbot               | 4.64 ms                                                               | 4.99 ms: 1.08x slower                                                       |
| bench_mp_pool              | 7.05 ms                                                               | 7.61 ms: 1.08x slower                                                       |
| logging_silent             | 127 ns                                                                | 137 ns: 1.08x slower                                                        |
| scimark_fft                | 418 ms                                                                | 454 ms: 1.09x slower                                                        |
| regex_v8                   | 28.3 ms                                                               | 30.8 ms: 1.09x slower                                                       |
| scimark_monte_carlo        | 85.1 ms                                                               | 92.8 ms: 1.09x slower                                                       |
| html5lib                   | 65.1 ms                                                               | 71.4 ms: 1.10x slower                                                       |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.80 ms: 1.10x slower                                                       |
| meteor_contest             | 112 ms                                                                | 124 ms: 1.11x slower                                                        |
| tornado_http               | 136 ms                                                                | 151 ms: 1.11x slower                                                        |
| spectral_norm              | 131 ms                                                                | 146 ms: 1.12x slower                                                        |
| asyncio_tcp                | 566 ms                                                                | 632 ms: 1.12x slower                                                        |
| fannkuch                   | 443 ms                                                                | 497 ms: 1.12x slower                                                        |
| json_dumps                 | 12.3 ms                                                               | 13.9 ms: 1.13x slower                                                       |
| typing_runtime_protocols   | 181 us                                                                | 206 us: 1.14x slower                                                        |
| pyflate                    | 559 ms                                                                | 641 ms: 1.15x slower                                                        |
| coverage                   | 87.3 ms                                                               | 100 ms: 1.15x slower                                                        |
| python_startup             | 11.4 ms                                                               | 13.1 ms: 1.15x slower                                                       |
| gc_traversal               | 4.40 ms                                                               | 5.13 ms: 1.17x slower                                                       |
| go                         | 157 ms                                                                | 184 ms: 1.17x slower                                                        |
| sqlglot_normalize          | 126 ms                                                                | 149 ms: 1.19x slower                                                        |
| sqlglot_parse              | 1.46 ms                                                               | 1.74 ms: 1.19x slower                                                       |
| pycparser                  | 1.26 sec                                                              | 1.50 sec: 1.20x slower                                                      |
| sqlglot_transpile          | 1.83 ms                                                               | 2.20 ms: 1.20x slower                                                       |
| telco                      | 8.51 ms                                                               | 10.3 ms: 1.21x slower                                                       |
| 2to3                       | 308 ms                                                                | 376 ms: 1.22x slower                                                        |
| create_gc_cycles           | 1.92 ms                                                               | 2.34 ms: 1.22x slower                                                       |
| nqueens                    | 99.2 ms                                                               | 123 ms: 1.24x slower                                                        |
| django_template            | 40.7 ms                                                               | 50.5 ms: 1.24x slower                                                       |
| sympy_str                  | 280 ms                                                                | 355 ms: 1.27x slower                                                        |
| genshi_text                | 27.4 ms                                                               | 34.9 ms: 1.27x slower                                                       |
| sqlglot_optimize           | 61.3 ms                                                               | 78.7 ms: 1.28x slower                                                       |
| richards_super             | 58.5 ms                                                               | 75.5 ms: 1.29x slower                                                       |
| chaos                      | 71.4 ms                                                               | 92.4 ms: 1.29x slower                                                       |
| dulwich_log                | 62.0 ms                                                               | 80.7 ms: 1.30x slower                                                       |
| sympy_integrate            | 21.6 ms                                                               | 28.2 ms: 1.31x slower                                                       |
| docutils                   | 2.98 sec                                                              | 3.94 sec: 1.32x slower                                                      |
| richards                   | 50.9 ms                                                               | 67.3 ms: 1.32x slower                                                       |
| sympy_expand               | 454 ms                                                                | 601 ms: 1.32x slower                                                        |
| generators                 | 43.5 ms                                                               | 58.1 ms: 1.34x slower                                                       |
| pylint                     | 355 ms                                                                | 475 ms: 1.34x slower                                                        |
| pprint_safe_repr           | 916 ms                                                                | 1.23 sec: 1.34x slower                                                      |
| genshi_xml                 | 60.6 ms                                                               | 81.5 ms: 1.34x slower                                                       |
| sympy_sum                  | 154 ms                                                                | 208 ms: 1.35x slower                                                        |
| regex_compile              | 137 ms                                                                | 186 ms: 1.35x slower                                                        |
| pprint_pformat             | 1.88 sec                                                              | 2.57 sec: 1.37x slower                                                      |
| hexiom                     | 6.98 ms                                                               | 9.91 ms: 1.42x slower                                                       |
| Geometric mean             | (ref)                                                                 | 1.07x slower                                                                |

Benchmark hidden because not significant (5): coroutines, pickle_list, scimark_sor, regex_dna, sqlite_synth
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240910-3.14.0a0-8cbca05-JIT/bm-20240910-arminc-aarch64-diegorusso-gh_119726_generate_a-3.14.0a0-8cbca05.json: bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.069x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.00x