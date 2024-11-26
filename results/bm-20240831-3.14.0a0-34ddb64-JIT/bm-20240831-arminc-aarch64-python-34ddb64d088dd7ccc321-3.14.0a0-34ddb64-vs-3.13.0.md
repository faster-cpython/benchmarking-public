# Results vs. 3.13.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-aarch64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.083x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 382 ms: 1.26x slower                                                    |
| docutils       | 2.89 sec                                                 | 3.93 sec: 1.36x slower                                                  |
| html5lib       | 66.4 ms                                                  | 70.5 ms: 1.06x slower                                                   |
| tornado_http   | 128 ms                                                   | 151 ms: 1.18x slower                                                    |
| Geometric mean | (ref)                                                    | 1.21x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 558 ms: 1.16x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 571 ms: 1.14x faster                                                    |
| async_tree_none            | 497 ms                                                   | 451 ms: 1.10x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 430 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 720 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 743 ms: 1.03x faster                                                    |
| coroutines                 | 28.5 ms                                                  | 28.3 ms: 1.01x faster                                                   |
| async_tree_io_tg           | 1.13 sec                                                 | 1.16 sec: 1.03x slower                                                  |
| async_generators           | 489 ms                                                   | 507 ms: 1.04x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.19 sec: 1.07x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 88.0 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.3 ms: 1.05x faster                                                   |
| regex_dna      | 253 ms                                                   | 246 ms: 1.03x faster                                                    |
| regex_compile  | 127 ms                                                   | 194 ms: 1.52x slower                                                    |
| Geometric mean | (ref)                                                    | 1.09x slower                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_loads           | 31.7 us                                                  | 32.7 us: 1.03x slower                                                   |
| tomli_loads          | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| unpickle_pure_python | 251 us                                                   | 266 us: 1.06x slower                                                    |
| pickle_pure_python   | 357 us                                                   | 382 us: 1.07x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.02x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_process, json_dumps, xml_etree_iterparse, xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                  | 13.3 ms: 1.16x faster                                                   |
| python_startup_no_site | 8.73 ms                                                  | 8.96 ms: 1.03x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.06x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| django_template | 41.6 ms                                                  | 51.0 ms: 1.23x slower                                                   |
| genshi_text     | 27.7 ms                                                  | 34.4 ms: 1.24x slower                                                   |
| genshi_xml      | 60.3 ms                                                  | 81.1 ms: 1.34x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.19x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.36 ms: 1.42x faster                                                   |
| deepcopy_memo              | 50.4 us                                                  | 37.4 us: 1.35x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 558 ms: 1.16x faster                                                    |
| python_startup             | 15.4 ms                                                  | 13.3 ms: 1.16x faster                                                   |
| gc_traversal               | 5.77 ms                                                  | 5.00 ms: 1.15x faster                                                   |
| async_tree_memoization     | 651 ms                                                   | 571 ms: 1.14x faster                                                    |
| deepcopy                   | 447 us                                                   | 400 us: 1.12x faster                                                    |
| async_tree_none            | 497 ms                                                   | 451 ms: 1.10x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 430 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 720 ms: 1.07x faster                                                    |
| scimark_sor                | 160 ms                                                   | 150 ms: 1.06x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.83 us: 1.06x faster                                                   |
| float                      | 93.3 ms                                                  | 88.0 ms: 1.06x faster                                                   |
| regex_v8                   | 31.8 ms                                                  | 30.3 ms: 1.05x faster                                                   |
| pathlib                    | 22.7 ms                                                  | 21.8 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 743 ms: 1.03x faster                                                    |
| regex_dna                  | 253 ms                                                   | 246 ms: 1.03x faster                                                    |
| mako                       | 13.4 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| thrift                     | 968 us                                                   | 950 us: 1.02x faster                                                    |
| bench_mp_pool              | 7.68 ms                                                  | 7.59 ms: 1.01x faster                                                   |
| coroutines                 | 28.5 ms                                                  | 28.3 ms: 1.01x faster                                                   |
| bpe_tokeniser              | 5.87 sec                                                 | 5.96 sec: 1.02x slower                                                  |
| spectral_norm              | 143 ms                                                   | 146 ms: 1.02x slower                                                    |
| python_startup_no_site     | 8.73 ms                                                  | 8.96 ms: 1.03x slower                                                   |
| async_tree_io_tg           | 1.13 sec                                                 | 1.16 sec: 1.03x slower                                                  |
| json_loads                 | 31.7 us                                                  | 32.7 us: 1.03x slower                                                   |
| logging_silent             | 133 ns                                                   | 137 ns: 1.03x slower                                                    |
| mdp                        | 3.34 sec                                                 | 3.45 sec: 1.03x slower                                                  |
| async_generators           | 489 ms                                                   | 507 ms: 1.04x slower                                                    |
| scimark_fft                | 447 ms                                                   | 463 ms: 1.04x slower                                                    |
| tomli_loads                | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| logging_format             | 7.82 us                                                  | 8.13 us: 1.04x slower                                                   |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 6.81 ms: 1.05x slower                                                   |
| bench_thread_pool          | 1.27 ms                                                  | 1.33 ms: 1.05x slower                                                   |
| logging_simple             | 7.07 us                                                  | 7.41 us: 1.05x slower                                                   |
| html5lib                   | 66.4 ms                                                  | 70.5 ms: 1.06x slower                                                   |
| unpickle_pure_python       | 251 us                                                   | 266 us: 1.06x slower                                                    |
| telco                      | 9.74 ms                                                  | 10.4 ms: 1.06x slower                                                   |
| crypto_pyaes               | 83.7 ms                                                  | 89.4 ms: 1.07x slower                                                   |
| typing_runtime_protocols   | 193 us                                                   | 207 us: 1.07x slower                                                    |
| pickle_pure_python         | 357 us                                                   | 382 us: 1.07x slower                                                    |
| scimark_lu                 | 139 ms                                                   | 149 ms: 1.07x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.19 sec: 1.07x slower                                                  |
| meteor_contest             | 114 ms                                                   | 123 ms: 1.09x slower                                                    |
| scimark_monte_carlo        | 83.6 ms                                                  | 92.2 ms: 1.10x slower                                                   |
| fannkuch                   | 461 ms                                                   | 511 ms: 1.11x slower                                                    |
| pyflate                    | 556 ms                                                   | 630 ms: 1.13x slower                                                    |
| deltablue                  | 3.82 ms                                                  | 4.34 ms: 1.14x slower                                                   |
| go                         | 160 ms                                                   | 188 ms: 1.18x slower                                                    |
| raytrace                   | 300 ms                                                   | 353 ms: 1.18x slower                                                    |
| tornado_http               | 128 ms                                                   | 151 ms: 1.18x slower                                                    |
| pycparser                  | 1.27 sec                                                 | 1.52 sec: 1.19x slower                                                  |
| sqlglot_normalize          | 127 ms                                                   | 151 ms: 1.19x slower                                                    |
| comprehensions             | 20.4 us                                                  | 25.0 us: 1.22x slower                                                   |
| django_template            | 41.6 ms                                                  | 51.0 ms: 1.23x slower                                                   |
| genshi_text                | 27.7 ms                                                  | 34.4 ms: 1.24x slower                                                   |
| nqueens                    | 100 ms                                                   | 125 ms: 1.25x slower                                                    |
| 2to3                       | 304 ms                                                   | 382 ms: 1.26x slower                                                    |
| sqlglot_transpile          | 1.73 ms                                                  | 2.19 ms: 1.26x slower                                                   |
| richards                   | 53.6 ms                                                  | 67.9 ms: 1.26x slower                                                   |
| richards_super             | 60.1 ms                                                  | 76.3 ms: 1.27x slower                                                   |
| sqlglot_optimize           | 62.2 ms                                                  | 79.4 ms: 1.28x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 1.77 ms: 1.28x slower                                                   |
| genshi_xml                 | 60.3 ms                                                  | 81.1 ms: 1.34x slower                                                   |
| chaos                      | 68.0 ms                                                  | 91.5 ms: 1.35x slower                                                   |
| sympy_expand               | 457 ms                                                   | 619 ms: 1.35x slower                                                    |
| docutils                   | 2.89 sec                                                 | 3.93 sec: 1.36x slower                                                  |
| sympy_str                  | 264 ms                                                   | 364 ms: 1.38x slower                                                    |
| pprint_safe_repr           | 926 ms                                                   | 1.28 sec: 1.38x slower                                                  |
| pprint_pformat             | 1.90 sec                                                 | 2.64 sec: 1.39x slower                                                  |
| sympy_integrate            | 20.8 ms                                                  | 29.2 ms: 1.40x slower                                                   |
| pylint                     | 342 ms                                                   | 489 ms: 1.43x slower                                                    |
| hexiom                     | 7.11 ms                                                  | 10.3 ms: 1.45x slower                                                   |
| sympy_sum                  | 144 ms                                                   | 215 ms: 1.50x slower                                                    |
| generators                 | 37.6 ms                                                  | 56.9 ms: 1.51x slower                                                   |
| regex_compile              | 127 ms                                                   | 194 ms: 1.52x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.09x slower                                                            |

Benchmark hidden because not significant (11): xml_etree_process, json_dumps, regex_effbot, xml_etree_iterparse, pidigits, xml_etree_generate, coverage, asyncio_websockets, json, xml_etree_parse, nbody
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (3) of results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log

- Geometric mean (including insignificant results): 1.083x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.00x