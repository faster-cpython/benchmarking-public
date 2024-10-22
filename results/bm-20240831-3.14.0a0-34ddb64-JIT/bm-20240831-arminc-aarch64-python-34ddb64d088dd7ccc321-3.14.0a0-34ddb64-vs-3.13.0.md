# Results vs. 3.13.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-aarch64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.10x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 382 ms: 1.25x slower                                                    |
| docutils       | 2.91 sec                                                 | 3.93 sec: 1.35x slower                                                  |
| html5lib       | 64.3 ms                                                  | 70.5 ms: 1.10x slower                                                   |
| tornado_http   | 131 ms                                                   | 151 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                    | 1.21x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 558 ms: 1.16x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 571 ms: 1.10x faster                                                    |
| async_tree_none            | 493 ms                                                   | 451 ms: 1.09x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 430 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 743 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 720 ms: 1.02x faster                                                    |
| coroutines                 | 28.2 ms                                                  | 28.3 ms: 1.00x slower                                                   |
| asyncio_websockets         | 656 ms                                                   | 663 ms: 1.01x slower                                                    |
| async_generators           | 496 ms                                                   | 507 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.29 sec: 1.05x slower                                                  |
| async_tree_io_tg           | 1.09 sec                                                 | 1.16 sec: 1.06x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.19 sec: 1.07x slower                                                  |
| asyncio_tcp                | 568 ms                                                   | 635 ms: 1.12x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 88.0 ms: 1.07x faster                                                   |
| nbody          | 114 ms                                                   | 116 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.3 ms: 1.04x faster                                                   |
| regex_compile  | 128 ms                                                   | 194 ms: 1.51x slower                                                    |
| Geometric mean | (ref)                                                    | 1.10x slower                                                            |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                  | 13.5 ms: 1.01x slower                                                   |
| xml_etree_iterparse  | 147 ms                                                   | 149 ms: 1.02x slower                                                    |
| json_loads           | 31.4 us                                                  | 32.7 us: 1.04x slower                                                   |
| tomli_loads          | 2.53 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| unpickle_pure_python | 254 us                                                   | 266 us: 1.05x slower                                                    |
| xml_etree_parse      | 188 ms                                                   | 198 ms: 1.05x slower                                                    |
| pickle_pure_python   | 359 us                                                   | 382 us: 1.06x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.03x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.75 ms                                                  | 8.96 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| django_template | 42.3 ms                                                  | 51.0 ms: 1.21x slower                                                   |
| genshi_text     | 27.7 ms                                                  | 34.4 ms: 1.24x slower                                                   |
| genshi_xml      | 60.2 ms                                                  | 81.1 ms: 1.35x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.19x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 51.0 us                                                  | 37.4 us: 1.37x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 558 ms: 1.16x faster                                                    |
| deepcopy                   | 451 us                                                   | 400 us: 1.13x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 571 ms: 1.10x faster                                                    |
| async_tree_none            | 493 ms                                                   | 451 ms: 1.09x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 430 ms: 1.09x faster                                                    |
| float                      | 94.4 ms                                                  | 88.0 ms: 1.07x faster                                                   |
| deepcopy_reduce            | 4.07 us                                                  | 3.83 us: 1.06x faster                                                   |
| scimark_sor                | 159 ms                                                   | 150 ms: 1.06x faster                                                    |
| regex_v8                   | 31.5 ms                                                  | 30.3 ms: 1.04x faster                                                   |
| pathlib                    | 22.4 ms                                                  | 21.8 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 743 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 720 ms: 1.02x faster                                                    |
| mako                       | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| coroutines                 | 28.2 ms                                                  | 28.3 ms: 1.00x slower                                                   |
| asyncio_websockets         | 656 ms                                                   | 663 ms: 1.01x slower                                                    |
| bpe_tokeniser              | 5.90 sec                                                 | 5.96 sec: 1.01x slower                                                  |
| json_dumps                 | 13.4 ms                                                  | 13.5 ms: 1.01x slower                                                   |
| logging_silent             | 135 ns                                                   | 137 ns: 1.01x slower                                                    |
| nbody                      | 114 ms                                                   | 116 ms: 1.01x slower                                                    |
| xml_etree_iterparse        | 147 ms                                                   | 149 ms: 1.02x slower                                                    |
| async_generators           | 496 ms                                                   | 507 ms: 1.02x slower                                                    |
| python_startup_no_site     | 8.75 ms                                                  | 8.96 ms: 1.02x slower                                                   |
| mdp                        | 3.36 sec                                                 | 3.45 sec: 1.02x slower                                                  |
| json                       | 5.61 ms                                                  | 5.76 ms: 1.03x slower                                                   |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.81 ms: 1.03x slower                                                   |
| scimark_fft                | 447 ms                                                   | 463 ms: 1.04x slower                                                    |
| spectral_norm              | 141 ms                                                   | 146 ms: 1.04x slower                                                    |
| logging_format             | 7.83 us                                                  | 8.13 us: 1.04x slower                                                   |
| json_loads                 | 31.4 us                                                  | 32.7 us: 1.04x slower                                                   |
| bench_mp_pool              | 7.30 ms                                                  | 7.59 ms: 1.04x slower                                                   |
| tomli_loads                | 2.53 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| bench_thread_pool          | 1.28 ms                                                  | 1.33 ms: 1.05x slower                                                   |
| unpickle_pure_python       | 254 us                                                   | 266 us: 1.05x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.29 sec: 1.05x slower                                                  |
| logging_simple             | 7.04 us                                                  | 7.41 us: 1.05x slower                                                   |
| xml_etree_parse            | 188 ms                                                   | 198 ms: 1.05x slower                                                    |
| pickle_pure_python         | 359 us                                                   | 382 us: 1.06x slower                                                    |
| telco                      | 9.73 ms                                                  | 10.4 ms: 1.06x slower                                                   |
| async_tree_io_tg           | 1.09 sec                                                 | 1.16 sec: 1.06x slower                                                  |
| scimark_lu                 | 139 ms                                                   | 149 ms: 1.07x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.19 sec: 1.07x slower                                                  |
| typing_runtime_protocols   | 192 us                                                   | 207 us: 1.08x slower                                                    |
| crypto_pyaes               | 82.7 ms                                                  | 89.4 ms: 1.08x slower                                                   |
| meteor_contest             | 113 ms                                                   | 123 ms: 1.09x slower                                                    |
| html5lib                   | 64.3 ms                                                  | 70.5 ms: 1.10x slower                                                   |
| scimark_monte_carlo        | 83.8 ms                                                  | 92.2 ms: 1.10x slower                                                   |
| gc_traversal               | 4.53 ms                                                  | 5.00 ms: 1.10x slower                                                   |
| create_gc_cycles           | 2.12 ms                                                  | 2.36 ms: 1.11x slower                                                   |
| asyncio_tcp                | 568 ms                                                   | 635 ms: 1.12x slower                                                    |
| deltablue                  | 3.85 ms                                                  | 4.34 ms: 1.13x slower                                                   |
| fannkuch                   | 452 ms                                                   | 511 ms: 1.13x slower                                                    |
| pyflate                    | 556 ms                                                   | 630 ms: 1.13x slower                                                    |
| tornado_http               | 131 ms                                                   | 151 ms: 1.15x slower                                                    |
| go                         | 163 ms                                                   | 188 ms: 1.16x slower                                                    |
| sqlglot_normalize          | 128 ms                                                   | 151 ms: 1.18x slower                                                    |
| raytrace                   | 298 ms                                                   | 353 ms: 1.18x slower                                                    |
| pycparser                  | 1.26 sec                                                 | 1.52 sec: 1.20x slower                                                  |
| django_template            | 42.3 ms                                                  | 51.0 ms: 1.21x slower                                                   |
| comprehensions             | 20.4 us                                                  | 25.0 us: 1.22x slower                                                   |
| genshi_text                | 27.7 ms                                                  | 34.4 ms: 1.24x slower                                                   |
| 2to3                       | 306 ms                                                   | 382 ms: 1.25x slower                                                    |
| nqueens                    | 98.7 ms                                                  | 125 ms: 1.26x slower                                                    |
| richards_super             | 60.3 ms                                                  | 76.3 ms: 1.26x slower                                                   |
| sqlglot_transpile          | 1.73 ms                                                  | 2.19 ms: 1.26x slower                                                   |
| richards                   | 53.5 ms                                                  | 67.9 ms: 1.27x slower                                                   |
| sqlglot_optimize           | 62.4 ms                                                  | 79.4 ms: 1.27x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 1.77 ms: 1.28x slower                                                   |
| chaos                      | 68.8 ms                                                  | 91.5 ms: 1.33x slower                                                   |
| genshi_xml                 | 60.2 ms                                                  | 81.1 ms: 1.35x slower                                                   |
| docutils                   | 2.91 sec                                                 | 3.93 sec: 1.35x slower                                                  |
| sympy_expand               | 455 ms                                                   | 619 ms: 1.36x slower                                                    |
| sympy_str                  | 264 ms                                                   | 364 ms: 1.38x slower                                                    |
| pprint_safe_repr           | 926 ms                                                   | 1.28 sec: 1.39x slower                                                  |
| pprint_pformat             | 1.90 sec                                                 | 2.64 sec: 1.39x slower                                                  |
| sympy_integrate            | 21.0 ms                                                  | 29.2 ms: 1.39x slower                                                   |
| pylint                     | 343 ms                                                   | 489 ms: 1.43x slower                                                    |
| hexiom                     | 7.13 ms                                                  | 10.3 ms: 1.44x slower                                                   |
| sympy_sum                  | 143 ms                                                   | 215 ms: 1.50x slower                                                    |
| generators                 | 37.8 ms                                                  | 56.9 ms: 1.50x slower                                                   |
| regex_compile              | 128 ms                                                   | 194 ms: 1.51x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.10x slower                                                            |

Benchmark hidden because not significant (8): xml_etree_process, regex_dna, regex_effbot, pidigits, python_startup, thrift, xml_etree_generate, coverage
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.11x