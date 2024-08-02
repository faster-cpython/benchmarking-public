# Results vs. base

- fork: Fidget-Spinner
- ref: stackref_all
- machine: linux-x86_64
- commit hash: 6a6bae2
- commit date: 2024-06-04
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 389 ms                                                                | 406 ms: 1.04x slower                                                    |
| docutils       | 3.35 sec                                                              | 3.44 sec: 1.03x slower                                                  |
| html5lib       | 96.8 ms                                                               | 102 ms: 1.05x slower                                                    |
| tornado_http   | 134 ms                                                                | 139 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 708 ms                                                                | 732 ms: 1.03x slower                                                    |
| async_tree_cpu_io_mixed_tg | 653 ms                                                                | 678 ms: 1.04x slower                                                    |
| async_tree_memoization_tg  | 514 ms                                                                | 536 ms: 1.04x slower                                                    |
| async_tree_none            | 449 ms                                                                | 472 ms: 1.05x slower                                                    |
| async_tree_memoization     | 556 ms                                                                | 586 ms: 1.05x slower                                                    |
| async_tree_io              | 928 ms                                                                | 979 ms: 1.06x slower                                                    |
| async_tree_io_tg           | 872 ms                                                                | 927 ms: 1.06x slower                                                    |
| async_tree_none_tg         | 401 ms                                                                | 427 ms: 1.07x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 187 ms: 1.00x slower                                                    |
| float          | 133 ms                                                                | 141 ms: 1.06x slower                                                    |
| nbody          | 220 ms                                                                | 234 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 26.5 ms                                                               | 25.5 ms: 1.04x faster                                                   |
| regex_effbot   | 3.59 ms                                                               | 3.48 ms: 1.03x faster                                                   |
| regex_dna      | 225 ms                                                                | 221 ms: 1.02x faster                                                    |
| regex_compile  | 214 ms                                                                | 227 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle             | 16.3 us                                                               | 16.2 us: 1.01x faster                                                   |
| pickle_dict          | 41.4 us                                                               | 41.1 us: 1.01x faster                                                   |
| json_loads           | 31.7 us                                                               | 31.8 us: 1.00x slower                                                   |
| pickle_list          | 4.84 us                                                               | 4.90 us: 1.01x slower                                                   |
| json_dumps           | 13.7 ms                                                               | 14.2 ms: 1.04x slower                                                   |
| xml_etree_process    | 88.2 ms                                                               | 92.8 ms: 1.05x slower                                                   |
| xml_etree_iterparse  | 112 ms                                                                | 118 ms: 1.05x slower                                                    |
| xml_etree_generate   | 108 ms                                                                | 115 ms: 1.06x slower                                                    |
| tomli_loads          | 3.18 sec                                                              | 3.38 sec: 1.06x slower                                                  |
| xml_etree_parse      | 144 ms                                                                | 154 ms: 1.07x slower                                                    |
| pickle_pure_python   | 569 us                                                                | 611 us: 1.07x slower                                                    |
| unpickle_list        | 5.30 us                                                               | 5.73 us: 1.08x slower                                                   |
| unpickle_pure_python | 386 us                                                                | 423 us: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.04x slower                                                            |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 9.13 ms                                                               | 9.18 ms: 1.01x slower                                                   |
| python_startup         | 13.6 ms                                                               | 13.7 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 60.0 ms                                                               | 62.9 ms: 1.05x slower                                                   |
| mako            | 20.2 ms                                                               | 21.6 ms: 1.06x slower                                                   |
| genshi_xml      | 80.9 ms                                                               | 86.7 ms: 1.07x slower                                                   |
| genshi_text     | 38.5 ms                                                               | 41.6 ms: 1.08x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.07x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8                   | 26.5 ms                                                               | 25.5 ms: 1.04x faster                                                   |
| regex_effbot               | 3.59 ms                                                               | 3.48 ms: 1.03x faster                                                   |
| regex_dna                  | 225 ms                                                                | 221 ms: 1.02x faster                                                    |
| unpickle                   | 16.3 us                                                               | 16.2 us: 1.01x faster                                                   |
| pickle_dict                | 41.4 us                                                               | 41.1 us: 1.01x faster                                                   |
| create_gc_cycles           | 1.38 ms                                                               | 1.37 ms: 1.01x faster                                                   |
| gc_traversal               | 2.79 ms                                                               | 2.78 ms: 1.00x faster                                                   |
| pidigits                   | 187 ms                                                                | 187 ms: 1.00x slower                                                    |
| json_loads                 | 31.7 us                                                               | 31.8 us: 1.00x slower                                                   |
| python_startup_no_site     | 9.13 ms                                                               | 9.18 ms: 1.01x slower                                                   |
| python_startup             | 13.6 ms                                                               | 13.7 ms: 1.01x slower                                                   |
| asyncio_tcp                | 594 ms                                                                | 600 ms: 1.01x slower                                                    |
| pickle_list                | 4.84 us                                                               | 4.90 us: 1.01x slower                                                   |
| dulwich_log                | 86.7 ms                                                               | 89.0 ms: 1.03x slower                                                   |
| telco                      | 9.58 ms                                                               | 9.83 ms: 1.03x slower                                                   |
| async_generators           | 549 ms                                                                | 565 ms: 1.03x slower                                                    |
| docutils                   | 3.35 sec                                                              | 3.44 sec: 1.03x slower                                                  |
| pycparser                  | 1.60 sec                                                              | 1.65 sec: 1.03x slower                                                  |
| bench_thread_pool          | 3.05 ms                                                               | 3.15 ms: 1.03x slower                                                   |
| async_tree_cpu_io_mixed    | 708 ms                                                                | 732 ms: 1.03x slower                                                    |
| sqlite_synth               | 3.14 us                                                               | 3.25 us: 1.04x slower                                                   |
| pylint                     | 391 ms                                                                | 405 ms: 1.04x slower                                                    |
| async_tree_cpu_io_mixed_tg | 653 ms                                                                | 678 ms: 1.04x slower                                                    |
| sympy_integrate            | 28.4 ms                                                               | 29.5 ms: 1.04x slower                                                   |
| sympy_sum                  | 252 ms                                                                | 262 ms: 1.04x slower                                                    |
| tornado_http               | 134 ms                                                                | 139 ms: 1.04x slower                                                    |
| sympy_str                  | 421 ms                                                                | 438 ms: 1.04x slower                                                    |
| async_tree_memoization_tg  | 514 ms                                                                | 536 ms: 1.04x slower                                                    |
| json_dumps                 | 13.7 ms                                                               | 14.2 ms: 1.04x slower                                                   |
| nqueens                    | 117 ms                                                                | 122 ms: 1.04x slower                                                    |
| 2to3                       | 389 ms                                                                | 406 ms: 1.04x slower                                                    |
| pathlib                    | 18.9 ms                                                               | 19.7 ms: 1.04x slower                                                   |
| sqlglot_optimize           | 87.4 ms                                                               | 91.4 ms: 1.05x slower                                                   |
| sympy_expand               | 743 ms                                                                | 778 ms: 1.05x slower                                                    |
| django_template            | 60.0 ms                                                               | 62.9 ms: 1.05x slower                                                   |
| html5lib                   | 96.8 ms                                                               | 102 ms: 1.05x slower                                                    |
| async_tree_none            | 449 ms                                                                | 472 ms: 1.05x slower                                                    |
| deepcopy_reduce            | 5.13 us                                                               | 5.39 us: 1.05x slower                                                   |
| xml_etree_process          | 88.2 ms                                                               | 92.8 ms: 1.05x slower                                                   |
| logging_format             | 11.6 us                                                               | 12.2 us: 1.05x slower                                                   |
| scimark_monte_carlo        | 123 ms                                                                | 130 ms: 1.05x slower                                                    |
| async_tree_memoization     | 556 ms                                                                | 586 ms: 1.05x slower                                                    |
| coverage                   | 761 ms                                                                | 802 ms: 1.05x slower                                                    |
| xml_etree_iterparse        | 112 ms                                                                | 118 ms: 1.05x slower                                                    |
| async_tree_io              | 928 ms                                                                | 979 ms: 1.06x slower                                                    |
| thrift                     | 12.9 ms                                                               | 13.6 ms: 1.06x slower                                                   |
| sqlglot_normalize          | 172 ms                                                                | 182 ms: 1.06x slower                                                    |
| coroutines                 | 31.3 ms                                                               | 33.0 ms: 1.06x slower                                                   |
| float                      | 133 ms                                                                | 141 ms: 1.06x slower                                                    |
| sqlglot_parse              | 2.59 ms                                                               | 2.74 ms: 1.06x slower                                                   |
| deepcopy                   | 566 us                                                                | 598 us: 1.06x slower                                                    |
| typing_runtime_protocols   | 252 us                                                                | 266 us: 1.06x slower                                                    |
| mdp                        | 3.22 sec                                                              | 3.42 sec: 1.06x slower                                                  |
| logging_silent             | 191 ns                                                                | 203 ns: 1.06x slower                                                    |
| meteor_contest             | 145 ms                                                                | 154 ms: 1.06x slower                                                    |
| async_tree_io_tg           | 872 ms                                                                | 927 ms: 1.06x slower                                                    |
| regex_compile              | 214 ms                                                                | 227 ms: 1.06x slower                                                    |
| xml_etree_generate         | 108 ms                                                                | 115 ms: 1.06x slower                                                    |
| go                         | 309 ms                                                                | 329 ms: 1.06x slower                                                    |
| chaos                      | 121 ms                                                                | 129 ms: 1.06x slower                                                    |
| tomli_loads                | 3.18 sec                                                              | 3.38 sec: 1.06x slower                                                  |
| logging_simple             | 10.4 us                                                               | 11.1 us: 1.06x slower                                                   |
| mako                       | 20.2 ms                                                               | 21.6 ms: 1.06x slower                                                   |
| async_tree_none_tg         | 401 ms                                                                | 427 ms: 1.07x slower                                                    |
| nbody                      | 220 ms                                                                | 234 ms: 1.07x slower                                                    |
| sqlglot_transpile          | 3.02 ms                                                               | 3.22 ms: 1.07x slower                                                   |
| xml_etree_parse            | 144 ms                                                                | 154 ms: 1.07x slower                                                    |
| richards                   | 78.2 ms                                                               | 83.6 ms: 1.07x slower                                                   |
| pprint_safe_repr           | 1.29 sec                                                              | 1.38 sec: 1.07x slower                                                  |
| scimark_sor                | 256 ms                                                                | 274 ms: 1.07x slower                                                    |
| deltablue                  | 8.21 ms                                                               | 8.80 ms: 1.07x slower                                                   |
| genshi_xml                 | 80.9 ms                                                               | 86.7 ms: 1.07x slower                                                   |
| crypto_pyaes               | 109 ms                                                                | 117 ms: 1.07x slower                                                    |
| pprint_pformat             | 2.65 sec                                                              | 2.85 sec: 1.07x slower                                                  |
| pickle_pure_python         | 569 us                                                                | 611 us: 1.07x slower                                                    |
| raytrace                   | 583 ms                                                                | 628 ms: 1.08x slower                                                    |
| richards_super             | 93.4 ms                                                               | 101 ms: 1.08x slower                                                    |
| hexiom                     | 11.8 ms                                                               | 12.7 ms: 1.08x slower                                                   |
| genshi_text                | 38.5 ms                                                               | 41.6 ms: 1.08x slower                                                   |
| comprehensions             | 27.4 us                                                               | 29.7 us: 1.08x slower                                                   |
| unpickle_list              | 5.30 us                                                               | 5.73 us: 1.08x slower                                                   |
| deepcopy_memo              | 64.4 us                                                               | 69.8 us: 1.08x slower                                                   |
| scimark_fft                | 466 ms                                                                | 506 ms: 1.09x slower                                                    |
| scimark_lu                 | 233 ms                                                                | 254 ms: 1.09x slower                                                    |
| spectral_norm              | 179 ms                                                                | 195 ms: 1.09x slower                                                    |
| unpickle_pure_python       | 386 us                                                                | 423 us: 1.10x slower                                                    |
| scimark_sparse_mat_mult    | 6.31 ms                                                               | 6.94 ms: 1.10x slower                                                   |
| pyflate                    | 736 ms                                                                | 813 ms: 1.10x slower                                                    |
| fannkuch                   | 558 ms                                                                | 626 ms: 1.12x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.05x slower                                                            |

Benchmark hidden because not significant (6): asyncio_tcp_ssl, pickle, generators, bench_mp_pool, asyncio_websockets, json

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.01x