# Results vs. 3.12.0

- fork: diegorusso
- ref: gh_119726_trampoline
- machine: linux-aarch64
- commit hash: cebe632
- commit date: 2024-06-25
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 364 ms: 1.18x slower                                                        |
| docutils       | 2.98 sec                                                              | 3.53 sec: 1.18x slower                                                      |
| html5lib       | 65.1 ms                                                               | 70.5 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 411 ms: 1.40x faster                                                        |
| async_tree_none            | 624 ms                                                                | 452 ms: 1.38x faster                                                        |
| async_tree_memoization_tg  | 740 ms                                                                | 538 ms: 1.38x faster                                                        |
| async_tree_memoization     | 777 ms                                                                | 582 ms: 1.33x faster                                                        |
| async_tree_io              | 1.41 sec                                                              | 1.07 sec: 1.32x faster                                                      |
| async_tree_io_tg           | 1.40 sec                                                              | 1.11 sec: 1.27x faster                                                      |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 739 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 723 ms: 1.22x faster                                                        |
| Geometric mean             | (ref)                                                                 | 1.32x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 88.7 ms: 1.04x faster                                                       |
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                        |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 251 ms: 1.01x faster                                                        |
| regex_effbot   | 4.64 ms                                                               | 4.87 ms: 1.05x slower                                                       |
| regex_v8       | 28.3 ms                                                               | 30.4 ms: 1.07x slower                                                       |
| regex_compile  | 137 ms                                                                | 173 ms: 1.26x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.09x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 187 ms: 1.04x faster                                                        |
| xml_etree_iterparse  | 150 ms                                                                | 147 ms: 1.02x faster                                                        |
| xml_etree_generate   | 112 ms                                                                | 110 ms: 1.02x faster                                                        |
| pickle_dict          | 37.3 us                                                               | 37.8 us: 1.01x slower                                                       |
| tomli_loads          | 2.59 sec                                                              | 2.68 sec: 1.03x slower                                                      |
| pickle               | 13.4 us                                                               | 14.0 us: 1.04x slower                                                       |
| unpickle_pure_python | 260 us                                                                | 279 us: 1.07x slower                                                        |
| unpickle             | 18.5 us                                                               | 19.9 us: 1.08x slower                                                       |
| json_loads           | 30.7 us                                                               | 33.1 us: 1.08x slower                                                       |
| unpickle_list        | 6.17 us                                                               | 6.67 us: 1.08x slower                                                       |
| pickle_pure_python   | 365 us                                                                | 396 us: 1.09x slower                                                        |
| json_dumps           | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                                 | 1.04x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_process, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 11.1 ms: 1.33x slower                                                       |
| python_startup         | 11.4 ms                                                               | 15.4 ms: 1.36x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.34x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                       |
| django_template | 40.7 ms                                                               | 50.2 ms: 1.23x slower                                                       |
| genshi_text     | 27.4 ms                                                               | 35.1 ms: 1.28x slower                                                       |
| genshi_xml      | 60.6 ms                                                               | 82.6 ms: 1.36x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.22x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 577 ms                                                                | 411 ms: 1.40x faster                                                        |
| async_tree_none            | 624 ms                                                                | 452 ms: 1.38x faster                                                        |
| async_tree_memoization_tg  | 740 ms                                                                | 538 ms: 1.38x faster                                                        |
| async_tree_memoization     | 777 ms                                                                | 582 ms: 1.33x faster                                                        |
| async_tree_io              | 1.41 sec                                                              | 1.07 sec: 1.32x faster                                                      |
| deepcopy_memo              | 49.6 us                                                               | 38.9 us: 1.27x faster                                                       |
| async_tree_io_tg           | 1.40 sec                                                              | 1.11 sec: 1.27x faster                                                      |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 739 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 723 ms: 1.22x faster                                                        |
| deepcopy                   | 446 us                                                                | 386 us: 1.15x faster                                                        |
| generators                 | 43.5 ms                                                               | 38.8 ms: 1.12x faster                                                       |
| pathlib                    | 24.5 ms                                                               | 22.5 ms: 1.09x faster                                                       |
| raytrace                   | 353 ms                                                                | 325 ms: 1.09x faster                                                        |
| comprehensions             | 25.4 us                                                               | 23.5 us: 1.08x faster                                                       |
| logging_simple             | 7.63 us                                                               | 7.19 us: 1.06x faster                                                       |
| logging_format             | 8.34 us                                                               | 8.01 us: 1.04x faster                                                       |
| xml_etree_parse            | 195 ms                                                                | 187 ms: 1.04x faster                                                        |
| float                      | 92.1 ms                                                               | 88.7 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 150 ms                                                                | 147 ms: 1.02x faster                                                        |
| xml_etree_generate         | 112 ms                                                                | 110 ms: 1.02x faster                                                        |
| regex_dna                  | 254 ms                                                                | 251 ms: 1.01x faster                                                        |
| crypto_pyaes               | 86.6 ms                                                               | 85.8 ms: 1.01x faster                                                       |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                        |
| asyncio_websockets         | 658 ms                                                                | 665 ms: 1.01x slower                                                        |
| pickle_dict                | 37.3 us                                                               | 37.8 us: 1.01x slower                                                       |
| coroutines                 | 29.0 ms                                                               | 29.5 ms: 1.02x slower                                                       |
| deepcopy_reduce            | 4.10 us                                                               | 4.17 us: 1.02x slower                                                       |
| dask                       | 376 ms                                                                | 385 ms: 1.02x slower                                                        |
| mdp                        | 3.41 sec                                                              | 3.49 sec: 1.02x slower                                                      |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.02x slower                                                       |
| meteor_contest             | 112 ms                                                                | 115 ms: 1.02x slower                                                        |
| scimark_monte_carlo        | 85.1 ms                                                               | 87.5 ms: 1.03x slower                                                       |
| sqlite_synth               | 3.77 us                                                               | 3.88 us: 1.03x slower                                                       |
| bench_thread_pool          | 1.31 ms                                                               | 1.35 ms: 1.03x slower                                                       |
| tomli_loads                | 2.59 sec                                                              | 2.68 sec: 1.03x slower                                                      |
| async_generators           | 491 ms                                                                | 507 ms: 1.03x slower                                                        |
| thrift                     | 937 us                                                                | 970 us: 1.04x slower                                                        |
| asyncio_tcp_ssl            | 2.19 sec                                                              | 2.28 sec: 1.04x slower                                                      |
| pickle                     | 13.4 us                                                               | 14.0 us: 1.04x slower                                                       |
| fannkuch                   | 443 ms                                                                | 464 ms: 1.05x slower                                                        |
| regex_effbot               | 4.64 ms                                                               | 4.87 ms: 1.05x slower                                                       |
| json                       | 5.54 ms                                                               | 5.82 ms: 1.05x slower                                                       |
| pycparser                  | 1.26 sec                                                              | 1.34 sec: 1.06x slower                                                      |
| unpickle_pure_python       | 260 us                                                                | 279 us: 1.07x slower                                                        |
| regex_v8                   | 28.3 ms                                                               | 30.4 ms: 1.07x slower                                                       |
| unpickle                   | 18.5 us                                                               | 19.9 us: 1.08x slower                                                       |
| richards_super             | 58.5 ms                                                               | 63.1 ms: 1.08x slower                                                       |
| json_loads                 | 30.7 us                                                               | 33.1 us: 1.08x slower                                                       |
| unpickle_list              | 6.17 us                                                               | 6.67 us: 1.08x slower                                                       |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.71 ms: 1.08x slower                                                       |
| html5lib                   | 65.1 ms                                                               | 70.5 ms: 1.08x slower                                                       |
| deltablue                  | 4.12 ms                                                               | 4.47 ms: 1.09x slower                                                       |
| pickle_pure_python         | 365 us                                                                | 396 us: 1.09x slower                                                        |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                                        |
| richards                   | 50.9 ms                                                               | 55.8 ms: 1.10x slower                                                       |
| gc_traversal               | 4.40 ms                                                               | 4.82 ms: 1.10x slower                                                       |
| logging_silent             | 127 ns                                                                | 139 ns: 1.10x slower                                                        |
| json_dumps                 | 12.3 ms                                                               | 13.5 ms: 1.10x slower                                                       |
| sqlglot_transpile          | 1.83 ms                                                               | 2.02 ms: 1.10x slower                                                       |
| scimark_fft                | 418 ms                                                                | 463 ms: 1.11x slower                                                        |
| pyflate                    | 559 ms                                                                | 619 ms: 1.11x slower                                                        |
| dulwich_log                | 62.0 ms                                                               | 68.7 ms: 1.11x slower                                                       |
| bench_mp_pool              | 7.05 ms                                                               | 7.88 ms: 1.12x slower                                                       |
| spectral_norm              | 131 ms                                                                | 146 ms: 1.12x slower                                                        |
| sqlglot_parse              | 1.46 ms                                                               | 1.64 ms: 1.12x slower                                                       |
| go                         | 157 ms                                                                | 178 ms: 1.13x slower                                                        |
| sqlglot_optimize           | 61.3 ms                                                               | 69.5 ms: 1.13x slower                                                       |
| sympy_str                  | 280 ms                                                                | 319 ms: 1.14x slower                                                        |
| sqlglot_normalize          | 126 ms                                                                | 144 ms: 1.14x slower                                                        |
| asyncio_tcp                | 566 ms                                                                | 647 ms: 1.14x slower                                                        |
| typing_runtime_protocols   | 181 us                                                                | 207 us: 1.15x slower                                                        |
| scimark_sor                | 150 ms                                                                | 174 ms: 1.16x slower                                                        |
| 2to3                       | 308 ms                                                                | 364 ms: 1.18x slower                                                        |
| sympy_sum                  | 154 ms                                                                | 183 ms: 1.18x slower                                                        |
| docutils                   | 2.98 sec                                                              | 3.53 sec: 1.18x slower                                                      |
| coverage                   | 87.3 ms                                                               | 103 ms: 1.18x slower                                                        |
| sympy_expand               | 454 ms                                                                | 537 ms: 1.18x slower                                                        |
| telco                      | 8.51 ms                                                               | 10.1 ms: 1.19x slower                                                       |
| pylint                     | 355 ms                                                                | 424 ms: 1.19x slower                                                        |
| nqueens                    | 99.2 ms                                                               | 119 ms: 1.19x slower                                                        |
| sympy_integrate            | 21.6 ms                                                               | 26.2 ms: 1.21x slower                                                       |
| create_gc_cycles           | 1.92 ms                                                               | 2.33 ms: 1.21x slower                                                       |
| chaos                      | 71.4 ms                                                               | 88.1 ms: 1.23x slower                                                       |
| django_template            | 40.7 ms                                                               | 50.2 ms: 1.23x slower                                                       |
| scimark_lu                 | 146 ms                                                                | 181 ms: 1.24x slower                                                        |
| pprint_safe_repr           | 916 ms                                                                | 1.14 sec: 1.24x slower                                                      |
| regex_compile              | 137 ms                                                                | 173 ms: 1.26x slower                                                        |
| pprint_pformat             | 1.88 sec                                                              | 2.38 sec: 1.26x slower                                                      |
| genshi_text                | 27.4 ms                                                               | 35.1 ms: 1.28x slower                                                       |
| hexiom                     | 6.98 ms                                                               | 8.97 ms: 1.29x slower                                                       |
| python_startup_no_site     | 8.37 ms                                                               | 11.1 ms: 1.33x slower                                                       |
| python_startup             | 11.4 ms                                                               | 15.4 ms: 1.36x slower                                                       |
| genshi_xml                 | 60.6 ms                                                               | 82.6 ms: 1.36x slower                                                       |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                                |

Benchmark hidden because not significant (3): xml_etree_process, pickle_list, tornado_http
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20240625-3.14.0a0-cebe632-JIT/bm-20240625-arminc-aarch64-diegorusso-gh_119726_trampoline-3.14.0a0-cebe632.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.01x