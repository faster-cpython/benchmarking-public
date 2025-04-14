# Results vs. 3.12.0

- fork: python
- ref: 05a370abd6cdfe4b54be
- machine: linux-x86_64
- commit hash: 05a370a
- commit date: 2023-12-01
- overall geometric mean: 1.018x faster
- HPT reliability: 99.82%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 266 ms: 1.03x faster                                                   |
| chameleon      | 7.41 ms                                                | 6.94 ms: 1.07x faster                                                  |
| docutils       | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                 |
| tornado_http   | 103 ms                                                 | 95.9 ms: 1.07x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 571 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 740 ms: 1.02x slower                                                   |
| async_tree_none_tg         | 450 ms                                                 | 461 ms: 1.02x slower                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 746 ms: 1.03x slower                                                   |
| async_tree_io              | 1.16 sec                                               | 1.20 sec: 1.04x slower                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 1.23 sec: 1.04x slower                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 631 ms: 1.10x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.03x slower                                                           |

Benchmark hidden because not significant (1): async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 93.2 ms: 1.04x faster                                                  |
| float          | 84.7 ms                                                | 82.5 ms: 1.03x faster                                                  |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 135 ms: 1.10x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.58 ms: 1.01x faster                                                  |
| regex_dna      | 212 ms                                                 | 223 ms: 1.05x slower                                                   |
| regex_v8       | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 324 us                                                 | 303 us: 1.07x faster                                                   |
| tomli_loads          | 2.33 sec                                               | 2.20 sec: 1.06x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 221 us: 1.04x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 87.3 ms: 1.02x faster                                                  |
| json_loads           | 28.5 us                                                | 28.1 us: 1.01x faster                                                  |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 109 ms: 1.03x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 9.03 ms: 1.30x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.6 ms: 1.32x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.31x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.7 ms: 1.09x faster                                                  |
| mako            | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 115 us: 1.37x faster                                                   |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.29x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                   |
| raytrace                   | 312 ms                                                 | 272 ms: 1.15x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 71.3 ms: 1.15x faster                                                  |
| logging_format             | 7.23 us                                                | 6.36 us: 1.14x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.29 ms: 1.13x faster                                                  |
| sympy_str                  | 300 ms                                                 | 266 ms: 1.13x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.83 us: 1.11x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 67.9 ms: 1.11x faster                                                  |
| chaos                      | 67.0 ms                                                | 60.7 ms: 1.10x faster                                                  |
| regex_compile              | 148 ms                                                 | 135 ms: 1.10x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 19.5 ms: 1.10x faster                                                  |
| django_template            | 34.6 ms                                                | 31.7 ms: 1.09x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.2 ms: 1.09x faster                                                  |
| fannkuch                   | 417 ms                                                 | 388 ms: 1.08x faster                                                   |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 3.12 us: 1.07x faster                                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 137 ms: 1.07x faster                                                   |
| tornado_http               | 103 ms                                                 | 95.9 ms: 1.07x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 303 us: 1.07x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.07x faster                                                  |
| chameleon                  | 7.41 ms                                                | 6.94 ms: 1.07x faster                                                  |
| sympy_expand               | 478 ms                                                 | 450 ms: 1.06x faster                                                   |
| deepcopy                   | 371 us                                                 | 349 us: 1.06x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 2.20 sec: 1.06x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                 |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 735 ms: 1.05x faster                                                   |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 38.7 us: 1.05x faster                                                  |
| pyflate                    | 482 ms                                                 | 460 ms: 1.05x faster                                                   |
| generators                 | 31.2 ms                                                | 29.8 ms: 1.05x faster                                                  |
| coroutines                 | 23.2 ms                                                | 22.1 ms: 1.05x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.04x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 221 us: 1.04x faster                                                   |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                                   |
| nbody                      | 97.0 ms                                                | 93.2 ms: 1.04x faster                                                  |
| scimark_fft                | 382 ms                                                 | 367 ms: 1.04x faster                                                   |
| pathlib                    | 19.3 ms                                                | 18.6 ms: 1.04x faster                                                  |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.04x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.03x faster                                                   |
| hexiom                     | 6.41 ms                                                | 6.20 ms: 1.03x faster                                                  |
| 2to3                       | 274 ms                                                 | 266 ms: 1.03x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 66.6 ms: 1.03x faster                                                  |
| float                      | 84.7 ms                                                | 82.5 ms: 1.03x faster                                                  |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                   |
| async_generators           | 463 ms                                                 | 451 ms: 1.03x faster                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 53.5 ms: 1.02x faster                                                  |
| nqueens                    | 83.3 ms                                                | 81.4 ms: 1.02x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.58 sec: 1.02x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 87.3 ms: 1.02x faster                                                  |
| json                       | 5.26 ms                                                | 5.16 ms: 1.02x faster                                                  |
| json_loads                 | 28.5 us                                                | 28.1 us: 1.01x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 571 ms: 1.01x faster                                                   |
| regex_effbot               | 3.61 ms                                                | 3.58 ms: 1.01x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.82 us: 1.01x faster                                                  |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x slower                                                   |
| bench_thread_pool          | 842 us                                                 | 846 us: 1.00x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                  |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                   |
| go                         | 139 ms                                                 | 141 ms: 1.01x slower                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.13 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 740 ms: 1.02x slower                                                   |
| async_tree_none_tg         | 450 ms                                                 | 461 ms: 1.02x slower                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 109 ms: 1.03x slower                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 746 ms: 1.03x slower                                                   |
| async_tree_io              | 1.16 sec                                               | 1.20 sec: 1.04x slower                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 1.23 sec: 1.04x slower                                                 |
| regex_dna                  | 212 ms                                                 | 223 ms: 1.05x slower                                                   |
| richards_super             | 51.5 ms                                                | 54.4 ms: 1.06x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                  |
| richards                   | 45.8 ms                                                | 48.8 ms: 1.06x slower                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 631 ms: 1.10x slower                                                   |
| telco                      | 7.10 ms                                                | 8.46 ms: 1.19x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 9.03 ms: 1.30x slower                                                  |
| coverage                   | 72.7 ms                                                | 95.6 ms: 1.31x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.6 ms: 1.32x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 5.01 ms: 1.32x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (6): pycparser, logging_silent, xml_etree_parse, bench_mp_pool, async_tree_none, gunicorn
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20231201-3.13.0a2+-05a370a/bm-20231201-linux-x86_64-python-05a370abd6cdfe4b54be-3.13.0a2+-05a370a.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.018x faster

# HPT report

- Reliability score: 99.82% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x